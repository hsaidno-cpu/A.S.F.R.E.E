#!/usr/bin/env python3
"""Rebuild and safely apply the SHA-256-pinned A.S.F.R.E.E P1 security overlay."""
from __future__ import annotations

import base64
import hashlib
import os
from pathlib import Path, PurePosixPath
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "implementation-bundles"
ARCHIVE = BUNDLES / "asfree-p1-security-v0.2.0.tar.gz"
CHECKSUM = BUNDLES / "asfree-p1-security-v0.2.0.tar.gz.sha256"
SHARDS = BUNDLES / ".p1-security-v0.2.0"
EXPECTED = [f"part{i:02d}.b64" for i in range(16)]
ALLOW = {
    "runtime/asfree/security/__init__.py",
    "runtime/asfree/security/crypto.py",
    "runtime/asfree/security/execution.py",
    "runtime/asfree/security/identity.py",
    "runtime/asfree/security/tenancy.py",
    "runtime/tests/test_p1_security.py",
    "runtime/README.md",
    "runtime/pyproject.toml",
    "docs/implementation/P1-SECURITY-FOUNDATIONS.md",
    "docs/implementation/P1-THREAT-MODEL.md",
    "docs/implementation/P1-OPERATIONS.md",
    "plugin/tests/p1-security-cases.json",
    "plugin/references/schemas/security/authorization-policy.schema.json",
    "plugin/references/schemas/security/encrypted-envelope.schema.json",
    "plugin/references/schemas/security/isolated-execution-request.schema.json",
    "plugin/references/schemas/security/principal.schema.json",
    "plugin/references/schemas/security/tenant-store-binding.schema.json",
}

if not CHECKSUM.is_file():
    raise SystemExit("P1 security checksum sidecar is missing")
tokens = CHECKSUM.read_text(encoding="ascii").strip().split()
if len(tokens) != 2 or tokens[1] != ARCHIVE.name or len(tokens[0]) != 64:
    raise SystemExit("P1 security checksum sidecar is malformed")
expected_digest = tokens[0]
if any(char not in "0123456789abcdef" for char in expected_digest):
    raise SystemExit("P1 security checksum must be lowercase SHA-256")

if not ARCHIVE.is_file():
    names = sorted(path.name for path in SHARDS.glob("part*.b64")) if SHARDS.is_dir() else []
    if names != EXPECTED:
        raise SystemExit(f"P1 security overlay requires 16 ordered shards; found {names}")
    encoded = "".join((SHARDS / name).read_text(encoding="ascii").strip() for name in EXPECTED)
    try:
        payload = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise SystemExit(f"P1 security shard decoding failed: {type(exc).__name__}") from exc
    BUNDLES.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".p1-security-", suffix=".tar.gz", dir=BUNDLES)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, ARCHIVE)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)

actual_digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
if actual_digest != expected_digest:
    raise SystemExit("P1 security archive SHA-256 mismatch; refusing to apply")

prepared: list[tuple[Path, bytes]] = []
seen: set[str] = set()
with tarfile.open(ARCHIVE, "r:gz") as archive:
    for member in archive.getmembers():
        name = member.name
        if "\\" in name or "\x00" in name or name.startswith("/"):
            raise SystemExit(f"unsafe P1 archive path: {name!r}")
        parts = name.split("/")
        if not parts or any(part in {"", ".", ".."} for part in parts):
            raise SystemExit(f"unsafe P1 archive path component: {name!r}")
        rel = PurePosixPath(name)
        normalized = rel.as_posix()
        if normalized not in ALLOW or normalized in seen:
            raise SystemExit(f"unexpected or duplicate P1 archive member: {normalized}")
        if not member.isreg():
            raise SystemExit(f"non-regular P1 archive member rejected: {normalized}")
        destination = ROOT.joinpath(*rel.parts)
        cursor = ROOT
        for part in rel.parts:
            cursor = cursor / part
            if cursor.is_symlink():
                raise SystemExit(f"symlink path component rejected: {normalized}")
        if not destination.parent.resolve(strict=False).is_relative_to(ROOT.resolve()):
            raise SystemExit(f"P1 archive destination escapes repository: {normalized}")
        source = archive.extractfile(member)
        if source is None:
            raise SystemExit(f"cannot read P1 archive member: {normalized}")
        prepared.append((destination, source.read()))
        seen.add(normalized)

if seen != ALLOW:
    raise SystemExit(f"P1 archive inventory mismatch; missing={sorted(ALLOW - seen)}")

# Every path and archive member is validated before the first destination write.
for destination, data in prepared:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not destination.parent.resolve(strict=True).is_relative_to(ROOT.resolve()):
        raise SystemExit(f"P1 destination parent escaped repository: {destination}")
    fd, temp_name = tempfile.mkstemp(prefix=".p1-security-", suffix=".tmp", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, destination)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)

print(f"P1 security overlay applied: sha256={actual_digest}; files={len(prepared)}")
