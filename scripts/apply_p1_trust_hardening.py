#!/usr/bin/env python3
"""Verify and atomically apply the checksum-pinned P2 trust-hardening overlay."""
from __future__ import annotations

import base64
import hashlib
import os
from pathlib import Path, PurePosixPath
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "implementation-bundles"
ARCHIVE = BUNDLES / "asfree-p1-trust-hardening-v0.3.0.tar.gz"
CHECKSUM = BUNDLES / "asfree-p1-trust-hardening-v0.3.0.tar.gz.sha256"
SHARDS = BUNDLES / ".p1-trust-hardening-v0.3.0"
EXPECTED_SHARDS = [f"part{i:02d}.b64" for i in range(8)]
ALLOW = {
    "docs/implementation/P1-OPERATIONS.md",
    "docs/implementation/P1-SECURITY-FOUNDATIONS.md",
    "docs/implementation/P1-THREAT-MODEL.md",
    "docs/implementation/P2-SECURITY-HARDENING.md",
    "runtime/README.md",
    "runtime/asfree/change_control.py",
    "runtime/asfree/security/__init__.py",
    "runtime/asfree/security/admission.py",
    "runtime/asfree/security/audit_anchor.py",
    "runtime/asfree/security/delegation.py",
    "runtime/asfree/security/encrypted_io.py",
    "runtime/asfree/security/identity.py",
    "runtime/asfree/security/provider_adapters.py",
    "runtime/asfree/security/scive_boundary.py",
    "runtime/asfree/security/sqlcipher_store.py",
    "runtime/asfree/security/streaming_execution.py",
    "runtime/asfree/security/tenancy.py",
    "runtime/examples/quickstart.py",
    "runtime/tests/test_change_control.py",
    "runtime/tests/test_p2_security_hardening.py",
}


def fail(message: str) -> None:
    raise SystemExit(message)


if not CHECKSUM.is_file():
    fail("P2 trust-hardening checksum sidecar is missing")
tokens = CHECKSUM.read_text(encoding="ascii").strip().split()
if len(tokens) != 2 or tokens[1] != ARCHIVE.name or len(tokens[0]) != 64:
    fail("P2 trust-hardening checksum sidecar is malformed")
expected_digest = tokens[0]
if any(char not in "0123456789abcdef" for char in expected_digest):
    fail("P2 trust-hardening checksum must be lowercase SHA-256")

if not ARCHIVE.is_file():
    names = sorted(path.name for path in SHARDS.glob("part*.b64")) if SHARDS.is_dir() else []
    if names != EXPECTED_SHARDS:
        fail(f"P2 trust-hardening overlay requires exactly eight ordered shards; found {names}")
    encoded = "".join((SHARDS / name).read_text(encoding="ascii").strip() for name in EXPECTED_SHARDS)
    try:
        payload = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        fail(f"P2 trust-hardening shard decoding failed: {type(exc).__name__}")
    BUNDLES.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".p2-trust-", suffix=".tar.gz", dir=BUNDLES)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, ARCHIVE)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)

actual = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
if actual != expected_digest:
    fail("P2 trust-hardening archive SHA-256 mismatch; refusing to apply")

prepared: list[tuple[Path, bytes]] = []
seen: set[str] = set()
with tarfile.open(ARCHIVE, "r:gz") as archive:
    for member in archive.getmembers():
        name = member.name
        if "\\" in name or "\x00" in name or name.startswith("/"):
            fail(f"unsafe P2 archive path: {name!r}")
        parts = name.split("/")
        if not parts or any(part in {"", ".", ".."} for part in parts):
            fail(f"unsafe P2 archive path component: {name!r}")
        normalized = PurePosixPath(name).as_posix()
        if normalized not in ALLOW or normalized in seen:
            fail(f"unexpected or duplicate P2 archive member: {normalized}")
        if not member.isreg():
            fail(f"non-regular P2 archive member rejected: {normalized}")
        destination = ROOT.joinpath(*parts)
        cursor = ROOT
        for part in parts:
            cursor = cursor / part
            if cursor.is_symlink():
                fail(f"symlink path component rejected: {normalized}")
        if not destination.parent.resolve(strict=False).is_relative_to(ROOT.resolve()):
            fail(f"P2 archive destination escapes repository: {normalized}")
        source = archive.extractfile(member)
        if source is None:
            fail(f"cannot read P2 archive member: {normalized}")
        prepared.append((destination, source.read()))
        seen.add(normalized)

if seen != ALLOW:
    fail(f"P2 archive inventory mismatch: missing={sorted(ALLOW - seen)}; extra={sorted(seen - ALLOW)}")

# Validate the whole archive before the first write; publish every file atomically.
for destination, data in prepared:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.parent.resolve(strict=True).is_relative_to(ROOT.resolve()):
        fail(f"P2 destination parent escaped repository: {destination}")
    fd, temp_name = tempfile.mkstemp(prefix=".p2-trust-", suffix=".tmp", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, destination)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)

print(f"P2 trust-hardening overlay applied: sha256={actual}; files={len(prepared)}")
