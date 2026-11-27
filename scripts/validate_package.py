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
EXPECTED_PLUGIN_VERSION = "0.5.0-rc.2"
check(manifest.get("version") == EXPECTED_PLUGIN_VERSION, f"canonical plugin manifest must be version {EXPECTED_PLUGIN_VERSION}")
check(bool(re.fullmatch(r"[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?", manifest.get("name", ""))), "invalid plugin name")
check(bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", manifest.get("version", ""))), "plugin version is not strict SemVer")
interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
check(len(interface.get("shortDescription", "")) <= 30, "shortDescription exceeds 30 characters")
check(interface.get("category") in {"Business & Operations","Communication","Creativity","Data & Analytics","Developer Tools","Education & Research","Entertainment","Finance","Healthcare","Other","Productivity","Scientific Research","Security","Travel"}, "unsupported plugin category")
check(isinstance(interface.get("capabilities"), list), "interface.capabilities must be an array")
if isinstance(compat, dict):
    check(compat.get("name") == manifest.get("name"), "compatibility manifest name differs")
    check(compat.get("version") == manifest.get("version"), "compatibility manifest version differs")
    check(compat.get("description") == manifest.get("description"), "compatibility manifest description differs")
    check(compat.get("repository") == manifest.get("repository"), "compatibility manifest repository differs")
    check(compat.get("license") == manifest.get("license"), "compatibility manifest license differs")
    c_interface = compat.get("interface", {})
    for field in ("displayName", "shortDescription", "longDescription", "category", "defaultPrompt"):
        if field in interface:
            check(c_interface.get(field) == interface.get(field), f"compatibility manifest interface.{field} differs")
else:
    check(False, "compatibility manifest is missing or invalid")

package_readme_path = PKG / "README.md"
root_readme_path = ROOT / "README.md"
package_readme = package_readme_path.read_text(encoding="utf-8") if package_readme_path.is_file() else ""
root_readme = root_readme_path.read_text(encoding="utf-8") if root_readme_path.is_file() else ""
check(f"**Version:** {EXPECTED_PLUGIN_VERSION}" in package_readme, "plugin README version must match canonical manifest")
check("Canonical plugin candidate:** v0.5.0-rc.2" in root_readme, "root README candidate version must match canonical manifest")
check("docs/implementation/RUNTIME-REFERENCE.md" in root_readme, "root README must link to the tracked runtime reference")
check("runtime/README.md" not in root_readme, "root README contains a missing runtime/README.md link")

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
rpeds_control_planes = {"rpeds-progressive-development", "rpeds-adaptive-functional-situational-adapter"}
check(required_canonical.issubset(found_dirs), f"missing canonical skills: {sorted(required_canonical-found_dirs)}")
check(rpeds_control_planes.issubset(found_dirs), f"missing registered RPEDS control plane: {sorted(rpeds_control_planes-found_dirs)}")
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

legacy_aliases = {
    "anatomy-decomposition": "o02-anatomy-decomposition",
    "artifact-intelligence": "o01-artifact-intelligence",
    "bug-detection-diagnosis": "o06-bug-detection-diagnosis",
    "comparative-intelligence": "o05-comparative-intelligence",
    "evaluation-intelligence": "o12-evaluation-intelligence",
    "integration-runtime-lab": "o09-integration-runtime-lab",
    "negative-intelligence": "o04-negative-intelligence",
    "positive-intelligence": "o03-positive-intelligence",
    "reconstruction-adaptation": "o08-reconstruction-adaptation",
    "remediation-bug-fixing": "o07-remediation-bug-fixing",
    "security-governance": "o11-security-governance",
    "validation-quality-assurance": "o10-validation-qa",
}
check(found_dirs == required_canonical | set(legacy_aliases) | rpeds_control_planes, "skill folders must be exactly M00/O01–O12, registered aliases, and the RPEDS lifecycle control plane")
for alias, canonical in legacy_aliases.items():
    alias_path = skills_root / alias / "SKILL.md"
    canonical_path = skills_root / canonical / "SKILL.md"
    if alias_path.is_file() and canonical_path.is_file():
        alias_text = alias_path.read_text(encoding="utf-8")
        canonical_text = canonical_path.read_text(encoding="utf-8")
        check("# COMPATIBILITY ALIAS" in alias_text, f"legacy skill must be redirect-only: {alias}")
        check(f"plugin/skills/{canonical}/SKILL.md" in alias_text, f"legacy alias destination mismatch: {alias}")
        check(alias_text != canonical_text, f"legacy alias must not duplicate canonical procedure: {alias}")
    else:
        check(False, f"missing alias or canonical destination: {alias} -> {canonical}")

schema_files = sorted((PKG / "references" / "schemas").rglob("*.json"))
for schema_path in schema_files:
    schema = load_json(schema_path)
    check(isinstance(schema, dict) and schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", f"invalid/missing JSON Schema declaration: {schema_path.relative_to(ROOT)}")
check(len(schema_files) >= 29, f"expected at least 29 P0/P1/P1.1 JSON schemas, found {len(schema_files)}")
p0_runtime_schemas = sorted((PKG / "references" / "schemas" / "runtime").glob("*.json"))
check(len(p0_runtime_schemas) == 5, f"expected five P0 runtime schemas, found {len(p0_runtime_schemas)}")

base_cases = load_json(PKG / "tests" / "acceptance-cases.json")
release_cases = load_json(PKG / "tests" / "release-governance-cases.json")
release_governance = PKG / "references" / "release-and-routing-governance.md"
runtime_reference = ROOT / "docs" / "implementation" / "RUNTIME-REFERENCE.md"
check(release_governance.is_file(), "missing release and routing governance reference")
check(runtime_reference.is_file(), "missing tracked runtime reference guide")
p0_cases = load_json(PKG / "tests" / "p0-foundations-cases.json")
hardening_cases = load_json(PKG / "tests" / "p0-hardening-cases.json")
for label, cases_doc, minimum in (("base", base_cases, 30), ("P0", p0_cases, 30)):
    cases = cases_doc.get("cases", []) if isinstance(cases_doc, dict) else []
    ids = [c.get("id") for c in cases if isinstance(c, dict)]
    check(len(cases) >= minimum, f"{label} acceptance fixtures fewer than {minimum}")
    if label == "base":
        check(len(cases) == 30, f"expected 30 baseline acceptance specifications, found {len(cases)}")
        check(cases_doc.get("schema_version") == "1.1.0", "baseline acceptance fixture schema_version must be 1.1.0")
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

release_list = release_cases.get("cases", []) if isinstance(release_cases, dict) else []
release_ids = [case.get("id") for case in release_list if isinstance(case, dict)]
check(len(release_list) == 11, f"expected eleven release-governance acceptance specifications, found {len(release_list)}")
check(len(release_ids) == len(set(release_ids)), "duplicate release-governance acceptance IDs")
if isinstance(release_cases, dict):
    check(release_cases.get("case_count") == len(release_list), "release-governance case_count does not match cases length")

rpeds_cases = load_json(PKG/"tests"/"rpeds-acceptance-cases.json")
rpeds_list = rpeds_cases.get("cases", []) if isinstance(rpeds_cases, dict) else []
rpeds_ids = [case.get("id") for case in rpeds_list if isinstance(case, dict)]
check(len(rpeds_list) == 24, f"expected 24 RPEDS acceptance specifications, found {len(rpeds_list)}")
check(len(rpeds_ids) == len(set(rpeds_ids)), "duplicate RPEDS acceptance IDs")
if isinstance(rpeds_cases, dict):
    check(rpeds_cases.get("schema_version") == "1.0.0", "RPEDS acceptance schema_version must be 1.0.0")
    check(rpeds_cases.get("case_count") == len(rpeds_list), "RPEDS acceptance case_count does not match cases length")
    check(rpeds_cases.get("execution_status") == "SPECIFICATION_ONLY", "RPEDS acceptance fixture status must remain SPECIFICATION_ONLY")
check(all(case.get("execution_status") == "SPECIFICATION_ONLY" for case in rpeds_list if isinstance(case, dict)), "RPEDS acceptance cases must not imply test execution")
afsa_skill_path = PKG/"skills"/"rpeds-adaptive-functional-situational-adapter"/"SKILL.md"
check(afsa_skill_path.is_file(), "missing RPEDS Adaptive Functional Situational Adapter skill")
afsa_cases = load_json(PKG/"tests"/"rpeds-afsa-acceptance-cases.json")
afsa_list = afsa_cases.get("cases", []) if isinstance(afsa_cases, dict) else []
afsa_ids = [case.get("id") for case in afsa_list if isinstance(case, dict)]
check(len(afsa_list) == 8, f"expected eight RPEDS AFSA acceptance specifications, found {len(afsa_list)}")
check(len(afsa_ids) == len(set(afsa_ids)), "duplicate RPEDS AFSA acceptance IDs")
if isinstance(afsa_cases, dict):
    check(afsa_cases.get("schema_version") == "1.0.0", "RPEDS AFSA schema_version must be 1.0.0")
    check(afsa_cases.get("case_count") == len(afsa_list), "RPEDS AFSA case_count does not match cases length")
    check(afsa_cases.get("execution_status") == "SPECIFICATION_ONLY", "RPEDS AFSA fixtures must remain SPECIFICATION_ONLY")
check(all(case.get("execution_status") == "SPECIFICATION_ONLY" for case in afsa_list if isinstance(case, dict)), "RPEDS AFSA cases must not imply test execution")

rpeds_skill_path = PKG/"skills"/"rpeds-progressive-development"/"SKILL.md"
check(rpeds_skill_path.is_file(), "missing RPEDS lifecycle-control skill")
rpeds_modules = [
    PKG/"references"/"rpeds"/"roadmap-architecture.md",
    PKG/"references"/"rpeds"/"progressive-development-manager.md",
    PKG/"references"/"rpeds"/"continuous-evaluation-engine.md",
    PKG/"references"/"rpeds"/"adaptive-roadmap-optimizer.md",
]
for module_path in rpeds_modules:
    check(module_path.is_file(), f"missing RPEDS module: {module_path.relative_to(ROOT)}")
rpeds_schema_dir = PKG/"references"/"schemas"/"rpeds"
rpeds_schemas = sorted(rpeds_schema_dir.glob("*.json")) if rpeds_schema_dir.exists() else []
check(len(rpeds_schemas) == 7, f"expected seven RPEDS schemas, found {len(rpeds_schemas)}")
for required_doc in ("docs/architecture/RPEDS-ARCHITECTURE.md", "docs/implementation/RPEDS-IMPLEMENTATION-STATUS.md"):
    check((ROOT/required_doc).is_file(), f"missing RPEDS documentation: {required_doc}")
check((PKG/"tests"/"rpeds-schema-fixtures.json").is_file(), "missing RPEDS schema/semantic fixtures")
check((ROOT/"scripts"/"validate_rpeds_contracts.py").is_file(), "missing executable RPEDS contract validator")

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
check(len(p1_security_schemas) == 9, f"expected nine P1.0/P1.1 security schemas, found {len(p1_security_schemas)}")

p11_required_schemas = {"delegated-capability.schema.json", "host-quota-receipt.schema.json", "external-audit-anchor.schema.json", "human-security-review.schema.json"}
found_p11_schemas = {p.name for p in p1_security_schemas}
check(p11_required_schemas.issubset(found_p11_schemas), f"missing P1.1 security schemas: {sorted(p11_required_schemas-found_p11_schemas)}")
p11_cases = load_json(PKG/"tests"/"p1-security-hardening-cases.json")
p11_list = p11_cases.get("cases", []) if isinstance(p11_cases, dict) else []
p11_ids = [case.get("id") for case in p11_list if isinstance(case, dict)]
check(len(p11_list) == 20, f"expected 20 P1.1 security acceptance specifications, found {len(p11_list)}")
check(len(p11_ids) == len(set(p11_ids)), "duplicate P1.1 security acceptance IDs")
if isinstance(p11_cases, dict):
    check(p11_cases.get("schema_version") == "1.0.0", "P1.1 acceptance schema_version must be 1.0.0")
    check(p11_cases.get("case_count") == len(p11_list), "P1.1 acceptance case_count does not match cases length")
    check(p11_cases.get("execution_status") == "SPECIFICATION_ONLY", "P1.1 acceptance fixture status must remain SPECIFICATION_ONLY")
check(all(case.get("execution_status") == "SPECIFICATION_ONLY" for case in p11_list if isinstance(case, dict)), "P1.1 acceptance cases must not imply test execution")
p11_reference = PKG/"references"/"p1.1-security-production-readiness.md"
p11_reconstruction = ROOT/"docs"/"implementation"/"P1.1-SECURITY-RECONSTRUCTION.md"
check(p11_reference.is_file(), "missing P1.1 security-to-production readiness contract")
check(p11_reconstruction.is_file(), "missing P1.1 reconstruction evidence-boundary document")

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


# Ecosystem identity registry: one canonical plugin identity per product.
identity_registry_path = PKG / "references" / "ecosystem-identity-registry.json"
identity_schema_path = PKG / "references" / "schemas" / "governance" / "ecosystem-identity-registry.schema.json"
migration_policy_path = PKG / "references" / "migration-and-deprecation-policy.md"
identity_registry = load_json(identity_registry_path)
identity_schema = load_json(identity_schema_path)
check(identity_registry_path.is_file(), "missing ecosystem identity registry")
check(identity_schema_path.is_file(), "missing ecosystem identity registry JSON Schema")
check(migration_policy_path.is_file(), "missing ecosystem migration and deprecation policy")
check(isinstance(identity_schema, dict) and identity_schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
      "ecosystem identity registry schema declaration is invalid")
check(isinstance(identity_registry, dict), "ecosystem identity registry must be a JSON object")

if isinstance(identity_registry, dict):
    check(identity_registry.get("registry_schema_version") == "1.0.0", "unsupported ecosystem identity registry schema version")
    check(identity_registry.get("registry_id") == "asfree-ecosystem-identities", "unexpected ecosystem registry ID")
    schema_version_const = identity_schema.get("properties", {}).get("registry_schema_version", {}).get("const") if isinstance(identity_schema, dict) else None
    check(schema_version_const == identity_registry.get("registry_schema_version"), "ecosystem registry/schema version mismatch")
    products = identity_registry.get("products", [])
    check(isinstance(products, list) and len(products) >= 1, "ecosystem registry must contain at least one product")
    product_ids = [p.get("product_id") for p in products if isinstance(p, dict)]
    check(len(product_ids) == len(set(product_ids)), "duplicate ecosystem product_id")

    all_identity_ids = []
    all_plugin_ids = []
    all_plugin_names = []
    for product in products if isinstance(products, list) else []:
        if not isinstance(product, dict):
            check(False, "ecosystem registry product entry must be an object")
            continue
        plugins = product.get("plugins", [])
        check(isinstance(plugins, list) and len(plugins) >= 1, f"product {product.get('product_id')} has no registered plugins")
        if not isinstance(plugins, list):
            continue
        canonical_plugins = [p for p in plugins if isinstance(p, dict) and p.get("role") == "CANONICAL"]
        check(len(canonical_plugins) == 1, f"product {product.get('product_id')} must have exactly one CANONICAL plugin")
        for plugin in plugins:
            if not isinstance(plugin, dict):
                check(False, f"product {product.get('product_id')} has a non-object plugin entry")
                continue
            for key in ("identity_id", "plugin_id", "plugin_name", "version_source", "change_history_source"):
                check(isinstance(plugin.get(key), str) and bool(plugin.get(key).strip()),
                      f"registered plugin missing {key}: {plugin.get('plugin_name', '<unknown>')}")
            check(plugin.get("role") in {"CANONICAL", "COMPATIBILITY_REDIRECT", "INDEPENDENT_PLUGIN"},
                  f"invalid plugin registry role: {plugin.get('role')}")
            all_identity_ids.append(plugin.get("identity_id"))
            all_plugin_ids.append(plugin.get("plugin_id"))
            all_plugin_names.append(plugin.get("plugin_name"))
        canonical_identity_ids = {p.get("identity_id") for p in canonical_plugins}
        for plugin in plugins:
            if isinstance(plugin, dict) and plugin.get("role") == "COMPATIBILITY_REDIRECT":
                check(plugin.get("target_identity_id") in canonical_identity_ids,
                      f"redirect {plugin.get('plugin_name')} must target the sole canonical plugin for {product.get('product_id')}")
                check(plugin.get("version_scope") == "LEGACY_REDIRECT_SHELL_ONLY",
                      f"redirect {plugin.get('plugin_name')} must scope its SemVer to the redirect shell")
        artifacts = product.get("independent_artifacts", [])
        check(isinstance(artifacts, list), f"independent_artifacts must be an array for {product.get('product_id')}")

    check(len(all_identity_ids) == len(set(all_identity_ids)), "duplicate plugin identity_id across ecosystem registry")
    check(len(all_plugin_ids) == len(set(all_plugin_ids)), "duplicate Plugin Creator plugin_id across ecosystem registry")
    check(len(all_plugin_names) == len(set(all_plugin_names)), "duplicate plugin package name across ecosystem registry")

    asfree_products = [p for p in products if isinstance(p, dict) and p.get("product_id") == "ASFREE"]
    check(len(asfree_products) == 1, "registry must contain exactly one ASFREE product record")
    if len(asfree_products) == 1:
        asfree = asfree_products[0]
        check(asfree.get("canonical_repository") == "https://github.com/hsaidno-cpu/A.S.F.R.E.E",
              "ASFREE canonical repository identity mismatch")
        asfree_plugins = asfree.get("plugins", [])
        canonical = next((p for p in asfree_plugins if isinstance(p, dict) and p.get("role") == "CANONICAL"), {})
        redirect = next((p for p in asfree_plugins if isinstance(p, dict) and p.get("role") == "COMPATIBILITY_REDIRECT"), {})
        check(canonical.get("identity_id") == "asfree-canonical-plugin", "ASFREE canonical identity_id mismatch")
        check(canonical.get("plugin_id") == "plugins_6aff3f4ff7d48191a411f6efb0cc435a",
              "ASFREE canonical Plugin Creator ID mismatch")
        check(canonical.get("plugin_name") == manifest.get("name") == "asfree",
              "ASFREE canonical package name does not match the root manifest")
        check(canonical.get("version_source") == "plugin/plugin.json#/version",
              "ASFREE package version source must be the canonical root manifest")
        check("reviewed commit merged into main" in canonical.get("source_activation_rule", ""),
              "ASFREE active-version rule must require a reviewed merge to main")
        check(redirect.get("identity_id") == "asfree-legacy-redirect", "ASFREE legacy redirect identity_id mismatch")
        check(redirect.get("plugin_id") == "plugins_6aff3ad51a408191a8d49b1c6003195b",
              "ASFREE legacy redirect Plugin Creator ID mismatch")
        check(redirect.get("plugin_name") == "asfree-master-orchestrator", "ASFREE legacy redirect name mismatch")
        check(redirect.get("target_identity_id") == canonical.get("identity_id"),
              "ASFREE legacy redirect must point to canonical plugin identity")
        check(redirect.get("role") == "COMPATIBILITY_REDIRECT", "ASFREE legacy package must be redirect-only")
        check(redirect.get("version_scope") == "LEGACY_REDIRECT_SHELL_ONLY",
              "ASFREE legacy version scope must not be canonical product SemVer")
        check(asfree.get("migration_policy_path") == "plugin/references/migration-and-deprecation-policy.md",
              "ASFREE migration policy path mismatch")
        for artifact in asfree.get("independent_artifacts", []):
            if isinstance(artifact, dict) and artifact.get("artifact_id") in {"local-reference-runtime", "implementation-source-bundles"}:
                check(artifact.get("version_relation") == "INDEPENDENT" and artifact.get("must_match_canonical_plugin_version") is False,
                      f"independent artifact version plane incorrectly coupled: {artifact.get('artifact_id')}")

migration_policy = migration_policy_path.read_text(encoding="utf-8") if migration_policy_path.is_file() else ""
check("exactly one" in migration_policy and "CANONICAL" in migration_policy,
      "migration policy must define the single-canonical-plugin invariant")
check("quarantined" in migration_policy.lower(), "migration policy must define a quarantine path for ambiguous values")
check("never" in migration_policy.lower() and "fallback" in migration_policy.lower(),
      "migration policy must prohibit fallback to superseded behavior")

if errors:
    print("STATIC VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(
    "STATIC VALIDATION: PASS — "
    f"{len(required_canonical)} canonical skills/{len(skill_dirs)} total skill folders, "
    f"{len(schema_files)} JSON schemas, "
    f"{len(base_cases['cases'])} baseline cases, {len(p0_cases['cases'])} P0 cases, {len(hardening_list)} P0 hardening cases, {len(p1_list)} P1 security cases, {len(p11_list)} P1.1 specification cases, {len(p0_runtime_schemas)} P0 runtime schemas, {len(p1_security_schemas)} P1 security schemas"
)
