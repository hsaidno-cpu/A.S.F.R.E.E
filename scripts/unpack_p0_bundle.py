#!/usr/bin/env python3
"""Verify and safely apply the versioned A.S.F.R.E.E P0 source overlay."""
from __future__ import annotations

import base64
import hashlib
from pathlib import Path, PurePosixPath
import tarfile

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "implementation-bundles" / "asfree-p0-foundations-v0.3.0.tar.gz"
CHECKSUM = ROOT / "implementation-bundles" / "asfree-p0-foundations-v0.3.0.tar.gz.sha256"
if not CHECKSUM.is_file():
    raise SystemExit("P0 source bundle checksum missing")
expected = CHECKSUM.read_text(encoding="ascii").strip().split()[0]

# GitHub's text-content upload path imposes practical payload limits. The
# canonical source archive may therefore be represented by ordered base64
# shards in Git. Reassemble only when the archive itself is absent; the exact
# SHA-256 sidecar remains the authority for accepting the reconstructed bytes.
if not BUNDLE.is_file():
    shard_dir = ROOT / "implementation-bundles" / ".p0-v0.3.0"
    shards = sorted(shard_dir.glob("part[0-9][0-9].b64"))
    if len(shards) != 9 or [p.name for p in shards] != [f"part{i:02d}.b64" for i in range(9)]:
        raise SystemExit("P0 source archive missing and its nine ordered base64 shards are incomplete")
    encoded = "".join(p.read_text(encoding="ascii").strip() for p in shards)
    try:
        archive_bytes = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        raise SystemExit(f"P0 source shard decoding failed: {exc}") from exc
    BUNDLE.parent.mkdir(parents=True, exist_ok=True)
    BUNDLE.write_bytes(archive_bytes)

actual = hashlib.sha256(BUNDLE.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit("P0 source bundle SHA-256 mismatch; refusing to apply")

allowed_exact = {
    "runtime/.gitignore", "runtime/README.md", "runtime/pyproject.toml",
    "plugin/plugin.json", "plugin/.codex-plugin/plugin.json", "plugin/README.md",
    "plugin/references/p0-runtime-architecture.md", "plugin/tests/p0-foundations-cases.json",
}

# The original P0 source archive also carries package metadata snapshots from
# the package version that existed when that runtime bundle was cut. Those
# entries remain checksum-verified and allowlisted for provenance, but they
# must never overwrite the current repository package source of truth.
LEGACY_PACKAGE_METADATA = {
    "plugin/plugin.json",
    "plugin/.codex-plugin/plugin.json",
    "plugin/README.md",
}
allowed_prefixes = (
    "runtime/asfree/", "runtime/tests/", "runtime/examples/",
    "docs/implementation/", "plugin/references/schemas/runtime/",
)
seen: set[str] = set()
applied = 0
ignored_legacy_metadata = 0
with tarfile.open(BUNDLE, "r:gz") as bundle:
    for member in bundle.getmembers():
        rel = PurePosixPath(member.name)
        if rel.is_absolute() or ".." in rel.parts or not rel.parts:
            raise SystemExit(f"unsafe archive path: {member.name}")
        name = rel.as_posix()
        if name in seen:
            raise SystemExit(f"duplicate archive path: {name}")
        seen.add(name)
        if name not in allowed_exact and not any(name.startswith(prefix) for prefix in allowed_prefixes):
            raise SystemExit(f"path outside P0 overlay allowlist: {name}")
        if not member.isfile():
            raise SystemExit(f"non-regular archive member rejected: {name}")
        destination = (ROOT / Path(*rel.parts)).resolve()
        if not destination.is_relative_to(ROOT.resolve()):
            raise SystemExit(f"archive path escapes repository: {name}")
        source = bundle.extractfile(member)
        if source is None:
            raise SystemExit(f"cannot read archive member: {name}")
        payload = source.read()
        if name in LEGACY_PACKAGE_METADATA:
            ignored_legacy_metadata += 1
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
        applied += 1

if not LEGACY_PACKAGE_METADATA.issubset(seen):
    missing_metadata = sorted(LEGACY_PACKAGE_METADATA - seen)
    raise SystemExit(f"expected legacy package metadata entries missing from P0 bundle: {missing_metadata}")

required = [
    ROOT / "runtime/asfree/evidence.py",
    ROOT / "runtime/asfree/orchestration.py",
    ROOT / "runtime/asfree/change_control.py",
    ROOT / "runtime/tests/test_evidence.py",
    ROOT / "runtime/examples/quickstart.py",
    ROOT / "docs/implementation/P0-FOUNDATIONS.md",
    ROOT / "plugin/references/p0-runtime-architecture.md",
    ROOT / "plugin/references/schemas/runtime/source-record.schema.json",
    ROOT / "plugin/tests/p0-foundations-cases.json",
]
missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
if missing:
    raise SystemExit("P0 overlay incomplete: " + ", ".join(missing))
print(f"P0 overlay applied and checksum-verified: {actual} ({applied} files applied; {ignored_legacy_metadata} legacy package metadata entries verified but ignored)")
