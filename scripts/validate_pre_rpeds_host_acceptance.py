#!/usr/bin/env python3
"""Verify a private PRE release against the A.S.F.R.E.E/RPEDS host profile."""
from __future__ import annotations

import hashlib
import json
import os
import sys
import tarfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "plugin/references/afsa/pre-rpeds-shared-dna-0.1.6-acceptance-profile.json"
EXPECTED_SKILLS = {
    "progressive-roadmap-evaluator",
    "adaptive-functional-situational-adapter",
    "adaptive-roadmap-optimizer",
    "capability-learning-federator",
    "continuous-evaluation-engine",
    "federated-release-synchronization-engine",
    "next-step-intelligence-engine",
    "process-documentation-audit-trail",
    "progressive-development-manager",
    "risk-dependency-governor",
    "roadmap-architecture-planner",
    "roadmap-assurance-closure",
    "roadmap-continuation-prompt-generator",
    "roadmap-intake-baseline",
}
MODULE_FILES = {
    "Roadmap Architecture Planner": "plugin/references/rpeds/roadmap-architecture.md",
    "Progressive Development Manager": "plugin/references/rpeds/progressive-development-manager.md",
    "Continuous Evaluation Engine": "plugin/references/rpeds/continuous-evaluation-engine.md",
    "Adaptive Roadmap Optimizer": "plugin/references/rpeds/adaptive-roadmap-optimizer.md",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON {path}: {exc}")


def check_host_profile() -> dict:
    profile = load_json(PROFILE_PATH)
    if profile.get("host_id") != "asfree-rpeds":
        fail("host profile identity mismatch")
    if profile.get("shared_identity") != "pre-rpeds-shared-roadmap-dna":
        fail("shared DNA identity mismatch")
    if profile.get("accepted_release_version") != "0.1.6":
        fail("accepted release version mismatch")
    if profile.get("status") != "VERIFIED_FOR_PRIVATE_NONCOMMERCIAL_ACCEPTANCE_ONLY":
        fail("profile does not constrain verification to private non-commercial acceptance")
    if profile.get("automation", {}).get("auto_adopt_nonbreaking") is not False:
        fail("automatic adoption must remain disabled")
    reuse = profile.get("reuse_basis", {})
    if "UNKNOWN" not in reuse.get("pre_source_rights", ""):
        fail("PRE source rights uncertainty must remain explicit")
    if "does not grant" not in reuse.get("restriction", ""):
        fail("profile must prohibit implied redistribution/commercial rights")
    if "No PRE archive or PRE source content is committed" not in profile.get("privacy_data_boundary", {}).get("public_repo", ""):
        fail("public repository boundary missing")

    merger = (ROOT / "plugin/references/rpeds/pre-rpeds-shared-dna-and-afsa.md").read_text(encoding="utf-8")
    afsa = (ROOT / "plugin/skills/rpeds-adaptive-functional-situational-adapter/SKILL.md").read_text(encoding="utf-8")
    profile_modules = {item.get("name") for item in profile.get("preserved_rpeds_modules", [])}
    if profile_modules != set(MODULE_FILES):
        fail("host profile must enumerate exactly the four native RPEDS modules")
    for module, ref in MODULE_FILES.items():
        if not (ROOT / ref).is_file():
            fail(f"RPEDS native module reference missing: {module}")
        if module not in merger:
            fail(f"shared DNA contract does not preserve RPEDS native module: {module}")
    for token in ("M00", "O11", "O12", "O10", "O09"):
        if token not in afsa and token not in merger:
            fail(f"AFSA authority boundary missing: {token}")
    if "Unknown facts remain" not in afsa and "Unknown is not compatible" not in merger:
        fail("AFSA must fail closed on unknown policy and authority inputs")

    manifest = load_json(ROOT / "plugin/plugin.json")
    if manifest.get("version") != "0.5.0-rc.2" or manifest.get("license") != "PolyForm-Noncommercial-1.0.0":
        fail("A.S.F.R.E.E host version/license mismatch")
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "PolyForm Noncommercial License 1.0.0" not in license_text or "Personal use for research, experiment" not in license_text:
        fail("A.S.F.R.E.E non-commercial testing license basis not present")
    license_policy = (ROOT / "LICENSE-STRATEGY.md").read_text(encoding="utf-8")
    if "separate written commercial license" not in license_policy:
        fail("commercial rights restriction not present")

    afsa_cases = load_json(ROOT / "plugin/tests/rpeds-afsa-acceptance-cases.json")
    rpeds_cases = load_json(ROOT / "plugin/tests/rpeds-acceptance-cases.json")
    if afsa_cases.get("case_count") != 8 or afsa_cases.get("execution_status") != "SPECIFICATION_ONLY":
        fail("AFSA specification inventory or truthful execution state changed")
    if rpeds_cases.get("case_count") != 24 or rpeds_cases.get("execution_status") != "SPECIFICATION_ONLY":
        fail("RPEDS specification inventory or truthful execution state changed")
    return {
        "host_profile": "PASS",
        "rpeds_native_modules": "PASS_4_OF_4_PRESERVED",
        "authority_and_privacy_boundaries": "PASS",
        "license_boundary": "PASS_PRIVATE_NONCOMMERCIAL_TEST_ONLY",
        "afsa_specifications": "8_SPECIFICATION_ONLY_NOT_CLAIMED_EXECUTED",
        "rpeds_specifications": "24_SPECIFICATION_ONLY_NOT_CLAIMED_EXECUTED",
    }


def verify_artifact(artifact: Path) -> dict:
    if not artifact.is_file():
        fail(f"artifact file not found: {artifact}")
    raw = artifact.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    expected_digest = os.environ.get("PRE_RPEDS_EXPECTED_SHA256", "").lower()
    expected_version = os.environ.get("PRE_RPEDS_EXPECTED_VERSION", "0.1.6")
    expected_release = os.environ.get("PRE_RPEDS_EXPECTED_RELEASE_ID", "")
    if not expected_digest or digest != expected_digest:
        fail("downloaded artifact SHA-256 does not match the HSO release record")

    files: dict[str, bytes] = {}
    prefix = "pre-rpeds-shared-roadmap-dna/"
    with tarfile.open(artifact, "r:gz") as archive:
        for member in archive.getmembers():
            path = PurePosixPath(member.name)
            if path.is_absolute() or ".." in path.parts or "\\" in member.name:
                fail(f"unsafe archive path: {member.name}")
            if member.issym() or member.islnk() or member.isdev():
                fail(f"non-regular archive member is prohibited: {member.name}")
            if member.isfile():
                if not member.name.startswith(prefix):
                    fail(f"file is outside canonical package root: {member.name}")
                rel = member.name[len(prefix):]
                if rel in files:
                    fail(f"duplicate archive member: {rel}")
                stream = archive.extractfile(member)
                if stream is None:
                    fail(f"cannot read archive member: {member.name}")
                files[rel] = stream.read()

    def json_bytes(path: str):
        try:
            return json.loads(files[path].decode("utf-8"))
        except Exception as exc:
            fail(f"invalid artifact JSON {path}: {exc}")

    plugin = json_bytes("plugin.json")
    snapshot = json_bytes("SOURCE-SNAPSHOT.json")
    source = snapshot.get("source_snapshot", {})
    if plugin.get("name") != "progressive-roadmap-evaluator":
        fail("artifact plugin identity mismatch")
    if plugin.get("version") != expected_version or source.get("version") != expected_version:
        fail("artifact version mismatch")
    if snapshot.get("canonical_identity") != "pre-rpeds-shared-roadmap-dna":
        fail("artifact canonical identity mismatch")
    pins = snapshot.get("imported_blobs", {})
    if len(pins) != 37 or source.get("imported_text_files") != 37:
        fail("artifact source snapshot does not contain the 37 pinned imports")
    for rel, sha in pins.items():
        content = files.get(rel)
        if content is None:
            fail(f"pinned source file missing from artifact: {rel}")
        git_blob = hashlib.sha1(
            b"blob " + str(len(content)).encode("ascii") + b"\0" + content
        ).hexdigest()
        if git_blob != sha:
            fail(f"Git blob SHA-1 mismatch inside artifact: {rel}")

    skill_paths = [p for p in files if p.startswith("skills/") and p.endswith("/SKILL.md")]
    skill_names = {p.split("/")[1] for p in skill_paths}
    if len(skill_paths) != 14 or skill_names != EXPECTED_SKILLS:
        fail("PRE artifact does not contain the exact 14-skill inventory")
    if expected_release and not expected_release.startswith("pre-rpeds-0.1.6-"):
        fail("unexpected release ID")
    if source.get("artifact_sha256") != "COMPUTED_PER_RELEASE_MANIFEST":
        fail("source manifest does not use the per-release digest contract")

    return {
        "artifact_sha256": digest,
        "artifact_bytes": len(raw),
        "artifact_identity": snapshot["canonical_identity"],
        "artifact_version": plugin["version"],
        "source_blob_pins": 37,
        "skill_count": 14,
        "release_id": expected_release,
        "status": "PASS",
    }


def main() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == "--contract-only":
        print(json.dumps(check_host_profile(), sort_keys=True))
        return
    if len(sys.argv) != 2:
        fail("usage: validate_pre_rpeds_host_acceptance.py --contract-only | <release.tar.gz>")
    results = check_host_profile()
    results["artifact"] = verify_artifact(Path(sys.argv[1]))
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    main()
