#!/usr/bin/env python3
"""Rebuild and safely apply the SHA-256-pinned P0 hardening overlay."""
from __future__ import annotations
import base64
import hashlib
import os
from pathlib import Path, PurePosixPath
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "implementation-bundles"
ARCHIVE = BUNDLES / "asfree-p0-hardening-v0.3.1.tar.gz"
CHECKSUM = BUNDLES / "asfree-p0-hardening-v0.3.1.tar.gz.sha256"
SHARDS = BUNDLES / ".p0-hardening-v0.3.1"
EXPECTED = [f"part{i:02d}.b64" for i in range(16)]
ALLOW = {
    "runtime/asfree/change_control.py", "runtime/asfree/evidence.py",
    "runtime/tests/test_change_control.py", "runtime/tests/test_evidence.py",
    "runtime/README.md", "runtime/pyproject.toml",
    "docs/implementation/P0-FOUNDATIONS.md", "docs/implementation/THREAT-MODEL.md",
    "docs/implementation/P0-HARDENING-REVIEW.md",
    "plugin/tests/p0-hardening-cases.json",
}

if not CHECKSUM.is_file():
    raise SystemExit("P0 hardening checksum sidecar is missing")
tokens = CHECKSUM.read_text(encoding="ascii").strip().split()
if len(tokens) != 2 or len(tokens[0]) != 64 or any(c not in "0123456789abcdef" for c in tokens[0]):
    raise SystemExit("P0 hardening checksum sidecar is malformed")
expected_digest = tokens[0]

if not ARCHIVE.is_file():
    names = sorted(p.name for p in SHARDS.glob("part*.b64")) if SHARDS.is_dir() else []
    if names != EXPECTED:
        raise SystemExit(f"P0 hardening overlay requires 16 ordered shards; found {names}")
    encoded = "".join((SHARDS / name).read_text(encoding="ascii").strip() for name in EXPECTED)
    try:
        payload = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise SystemExit(f"P0 hardening shard decoding failed: {type(exc).__name__}") from exc
    BUNDLES.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".p0-hardening-", suffix=".tar.gz", dir=BUNDLES)
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
    raise SystemExit("P0 hardening archive SHA-256 mismatch; refusing to apply")

prepared = []
seen = set()
with tarfile.open(ARCHIVE, "r:gz") as archive:
    for member in archive.getmembers():
        name = member.name
        if "\\" in name or "\x00" in name or name.startswith("/"):
            raise SystemExit(f"unsafe archive path: {name!r}")
        parts = name.split("/")
        if not parts or any(part in {"", ".", ".."} for part in parts):
            raise SystemExit(f"unsafe archive path component: {name!r}")
        rel = PurePosixPath(name)
        normalized = rel.as_posix()
        if normalized not in ALLOW or normalized in seen:
            raise SystemExit(f"unexpected or duplicate archive path: {normalized}")
        if not member.isreg():
            raise SystemExit(f"non-regular archive member rejected: {normalized}")
        seen.add(normalized)
        destination = ROOT.joinpath(*rel.parts)
        cursor = ROOT
        for part in rel.parts:
            cursor = cursor / part
            if cursor.is_symlink():
                raise SystemExit(f"symlink path component rejected: {normalized}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.parent.resolve(strict=True).is_relative_to(ROOT.resolve()):
            raise SystemExit(f"archive destination escapes repository: {normalized}")
        source = archive.extractfile(member)
        if source is None:
            raise SystemExit(f"cannot read archive member: {normalized}")
        prepared.append((destination, source.read()))

if seen != ALLOW:
    raise SystemExit(f"archive inventory mismatch; missing={sorted(ALLOW-seen)}")

# All paths, members and bytes are validated before the first destination write.
for destination, data in prepared:
    fd, temp_name = tempfile.mkstemp(prefix=".p0-hardening-", suffix=".tmp", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, destination)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)

print(f"P0 hardening overlay applied: sha256={actual_digest}; files={len(prepared)}")
