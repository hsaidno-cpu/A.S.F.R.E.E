#!/usr/bin/env python3
"""Static validation for A.S.F.R.E.E plugin contracts and P0 reference runtime."""
from pathlib import Path
import json
import re
import sys
import hashlib
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "plugin"
errors: list[str] = []

def check(ok: bool, message: str) -> None:
    if not ok:
        errors.append(message)

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return None

manifest = load_json(PKG / "plugin.json")
compat = load_json(PKG / ".codex-plugin" / "plugin.json")
if not isinstance(manifest, dict):
    print("STATIC VALIDATION: FAIL")
    print("- plugin manifest is unavailable")
    sys.exit(1)
check(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "plugin manifest schema is missing/incorrect")
check(manifest.get("version") == "0.3.0", "P0 canonical plugin manifest must be version 0.3.0")
check(bool(re.fullmatch(r"[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?", manifest.get("name", ""))), "invalid plugin name")
check(bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", manifest.get("version", ""))), "plugin version is not strict SemVer")
interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
check(len(interface.get("shortDescription", "")) <= 30, "shortDescription exceeds 30 characters")
check(interface.get("category") in {"Business & Operations","Communication","Creativity","Data & Analytics","Developer Tools","Education & Research","Entertainment","Finance","Healthcare","Other","Productivity","Scientific Research","Security","Travel"}, "unsupported plugin category")
check(isinstance(interface.get("capabilities"), list), "interface.capabilities must be an array")
if isinstance(compat, dict):
    check(compat.get("name") == manifest.get("name"), "compatibility manifest name differs")
    check(compat.get("version") == manifest.get("version"), "compatibility manifest version differs")
    c_interface = compat.get("interface", {})
    for field in ("displayName", "shortDescription", "longDescription", "category", "defaultPrompt"):
        if field in interface:
            check(c_interface.get(field) == interface.get(field), f"compatibility manifest interface.{field} differs")
else:
    check(False, "compatibility manifest is missing or invalid")

skills_root = PKG / "skills"
skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir()) if skills_root.exists() else []
required_canonical = {
    "asfree-master-orchestrator",
    *{f"o{i:02d}-{name}" for i, name in enumerate([
        "artifact-intelligence", "anatomy-decomposition", "positive-intelligence", "negative-intelligence",
        "comparative-intelligence", "bug-detection-diagnosis", "remediation-bug-fixing", "reconstruction-adaptation",
        "integration-runtime-lab", "validation-qa", "security-governance", "evaluation-intelligence"
    ], 1)}
}
found_dirs = {p.name for p in skill_dirs}
check(required_canonical.issubset(found_dirs), f"missing canonical skills: {sorted(required_canonical-found_dirs)}")
frontmatter_names = []
for folder in skill_dirs:
    skill = folder / "SKILL.md"
    check(skill.is_file(), f"missing SKILL.md: {skill.relative_to(ROOT)}")
    if not skill.is_file():
        continue
    content = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    check(match is not None, f"missing YAML frontmatter: {skill.relative_to(ROOT)}")
    if not match:
        continue
    fm = match.group(1)
    name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", fm)
    desc = re.search(r"(?m)^description:\s*(.+)$", fm)
    check(name is not None, f"missing/invalid frontmatter name: {skill.relative_to(ROOT)}")
    check(desc is not None and bool(desc.group(1).strip()), f"missing frontmatter description: {skill.relative_to(ROOT)}")
    if name:
        frontmatter_names.append(name.group(1))
    check(len(content.encode("utf-8")) <= 1024 * 1024, f"skill exceeds 1 MiB: {skill.relative_to(ROOT)}")
check(len(frontmatter_names) == len(set(frontmatter_names)), "duplicate skill frontmatter names")

schema_files = sorted((PKG / "references" / "schemas").rglob("*.json"))
for schema_path in schema_files:
    schema = load_json(schema_path)
    check(isinstance(schema, dict) and schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", f"invalid/missing JSON Schema declaration: {schema_path.relative_to(ROOT)}")
check(len(schema_files) >= 25, f"expected at least 25 P0/P1 JSON schemas, found {len(schema_files)}")
p0_runtime_schemas = sorted((PKG / "references" / "schemas" / "runtime").glob("*.json"))
check(len(p0_runtime_schemas) == 5, f"expected five P0 runtime schemas, found {len(p0_runtime_schemas)}")

base_cases = load_json(PKG / "tests" / "acceptance-cases.json")
p0_cases = load_json(PKG / "tests" / "p0-foundations-cases.json")
hardening_cases = load_json(PKG / "tests" / "p0-hardening-cases.json")
for label, cases_doc, minimum in (("base", base_cases, 30), ("P0", p0_cases, 30)):
    cases = cases_doc.get("cases", []) if isinstance(cases_doc, dict) else []
    ids = [c.get("id") for c in cases if isinstance(c, dict)]
    check(len(cases) >= minimum, f"{label} acceptance fixtures fewer than {minimum}")
    if label == "P0":
        check(len(cases) == 37, f"expected 37 P0 acceptance specifications, found {len(cases)}")
    check(len(ids) == len(set(ids)), f"duplicate {label} acceptance case IDs")
    if isinstance(cases_doc, dict) and "case_count" in cases_doc:
        check(cases_doc["case_count"] == len(cases), f"{label} case_count does not match cases length")

hardening_list = hardening_cases.get("cases", []) if isinstance(hardening_cases, dict) else []
hardening_ids = [c.get("id") for c in hardening_list if isinstance(c, dict)]
check(len(hardening_list) == 8, f"expected eight P0 hardening acceptance specifications, found {len(hardening_list)}")
check(len(hardening_ids) == len(set(hardening_ids)), "duplicate P0 hardening acceptance IDs")
if isinstance(hardening_cases, dict):
    check(hardening_cases.get("case_count") == len(hardening_list), "P0 hardening case_count does not match cases length")

runtime_archive = ROOT/"implementation-bundles"/"asfree-p0-foundations-v0.3.0.tar.gz"
runtime_checksum = ROOT/"implementation-bundles"/"asfree-p0-foundations-v0.3.0.tar.gz.sha256"
check(runtime_archive.is_file(), "missing P0 implementation source bundle")
check(runtime_checksum.is_file(), "missing P0 implementation source-bundle checksum")
if runtime_archive.is_file() and runtime_checksum.is_file():
    import hashlib
    expected_digest = runtime_checksum.read_text(encoding="ascii").strip().split()[0]
    actual_digest = hashlib.sha256(runtime_archive.read_bytes()).hexdigest()
    check(actual_digest == expected_digest, "P0 implementation bundle checksum mismatch")
check((ROOT/"scripts"/"unpack_p0_bundle.py").is_file(), "missing P0 bundle extraction/allowlist script")

hardening_archive = ROOT/"implementation-bundles"/"asfree-p0-hardening-v0.3.1.tar.gz"
hardening_checksum = ROOT/"implementation-bundles"/"asfree-p0-hardening-v0.3.1.tar.gz.sha256"
hardening_shard_dir = ROOT/"implementation-bundles"/".p0-hardening-v0.3.1"
check((ROOT/"scripts"/"apply_p0_hardening.py").is_file(), "missing P0 hardening overlay applier")
check(hardening_archive.is_file(), "missing P0 hardening source overlay")
check(hardening_checksum.is_file(), "missing P0 hardening source-overlay checksum")
expected_shards = [f"part{i:02d}.b64" for i in range(16)]
actual_shards = sorted(p.name for p in hardening_shard_dir.glob("part*.b64")) if hardening_shard_dir.exists() else []
check(actual_shards == expected_shards, f"P0 hardening source requires sixteen ordered shards, found {actual_shards}")
if hardening_archive.is_file() and hardening_checksum.is_file():
    import hashlib
    expected_hardening = hardening_checksum.read_text(encoding="ascii").strip().split()[0]
    actual_hardening = hashlib.sha256(hardening_archive.read_bytes()).hexdigest()
    check(actual_hardening == expected_hardening, "P0 hardening overlay checksum mismatch")


p1_archive = ROOT/"implementation-bundles"/"asfree-p1-security-v0.2.0.tar.gz"
p1_checksum = ROOT/"implementation-bundles"/"asfree-p1-security-v0.2.0.tar.gz.sha256"
check((ROOT/"scripts"/"apply_p1_security.py").is_file(), "missing P1 security overlay applier")
check(p1_archive.is_file(), "missing P1 security source overlay")
check(p1_checksum.is_file(), "missing P1 security source-overlay checksum")
if p1_archive.is_file() and p1_checksum.is_file():
    tokens = p1_checksum.read_text(encoding="ascii").strip().split()
    check(len(tokens) == 2 and tokens[1] == p1_archive.name, "P1 source overlay checksum sidecar malformed")
    if len(tokens) == 2:
        actual_p1 = hashlib.sha256(p1_archive.read_bytes()).hexdigest()
        check(actual_p1 == tokens[0], "P1 security source overlay checksum mismatch")

p1_cases = load_json(PKG/"tests"/"p1-security-cases.json")
p1_list = p1_cases.get("cases", []) if isinstance(p1_cases, dict) else []
p1_ids = [case.get("id") for case in p1_list if isinstance(case, dict)]
check(len(p1_list) == 33, f"expected 33 P1 security acceptance specifications, found {len(p1_list)}")
check(len(p1_ids) == len(set(p1_ids)), "duplicate P1 security acceptance IDs")
if isinstance(p1_cases, dict):
    check(p1_cases.get("case_count") == len(p1_list), "P1 security case_count does not match cases length")
p1_security_schemas = sorted((PKG/"references"/"schemas"/"security").glob("*.json"))
check(len(p1_security_schemas) == 5, f"expected five P1 security schemas, found {len(p1_security_schemas)}")

try:
    runtime_project = tomllib.loads((ROOT/"runtime"/"pyproject.toml").read_text(encoding="utf-8"))
    project_meta = runtime_project.get("project", {})
    check(project_meta.get("name") == "asfree-runtime", "unexpected P1 runtime package name")
    check(project_meta.get("version") == "0.2.0", "P1 runtime package version must be 0.2.0")
    check(any(dep.startswith("cryptography>=42") for dep in project_meta.get("dependencies", [])), "P1 cryptography dependency missing")
except Exception as exc:
    errors.append(f"cannot parse P1 runtime pyproject.toml: {type(exc).__name__}: {exc}")

for rel in (
    "asfree/security/__init__.py",
    "asfree/security/identity.py",
    "asfree/security/crypto.py",
    "asfree/security/tenancy.py",
    "asfree/security/execution.py",
):
    check((ROOT/"runtime"/rel).is_file(), f"missing P1 runtime module after overlay: runtime/{rel}")
check((ROOT/"runtime"/"tests"/"test_p1_security.py").is_file(), "missing P1 executable security tests")

runtime_required = [
    ROOT/"runtime"/"pyproject.toml", ROOT/"runtime"/"asfree"/"store.py", ROOT/"runtime"/"asfree"/"evidence.py",
    ROOT/"runtime"/"asfree"/"contracts.py", ROOT/"runtime"/"asfree"/"orchestration.py",
    ROOT/"runtime"/"asfree"/"change_control.py", ROOT/"runtime"/"examples"/"quickstart.py"
]
# The source bundle is a tracked source distribution. CI and local developers unpack it before runtime tests.
for path in runtime_required:
    if path == ROOT/"runtime"/"pyproject.toml":
        continue
    if not path.exists():
        check(runtime_archive.is_file(), f"runtime source not extracted and bundle unavailable: {path.relative_to(ROOT)}")

if errors:
    print("STATIC VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(
    "STATIC VALIDATION: PASS — "
    f"{len(required_canonical)} canonical skills/{len(skill_dirs)} total skill folders, "
    f"{len(schema_files)} JSON schemas, "
    f"{len(base_cases['cases'])} baseline cases, {len(p0_cases['cases'])} P0 cases, {len(hardening_list)} P0 hardening cases, {len(p1_list)} P1 security cases, {len(p0_runtime_schemas)} P0 runtime schemas, {len(p1_security_schemas)} P1 security schemas"
)
