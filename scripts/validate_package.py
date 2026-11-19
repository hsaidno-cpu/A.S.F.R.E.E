#!/usr/bin/env python3
"""Deterministic static checks for the A.S.F.R.E.E skills-only package."""
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "plugin"
errors = []

def check(condition, message):
    if not condition: errors.append(message)

manifest_path = PKG / "plugin.json"
try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"FAIL: cannot parse plugin.json: {exc}")
    sys.exit(1)
check(manifest.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "plugin.json has wrong/missing $schema")
check(bool(re.fullmatch(r"[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?", manifest.get("name", ""))), "invalid plugin name")
check(bool(re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", manifest.get("version", ""))), "version is not strict SemVer")
interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
check(len(interface.get("shortDescription", "")) <= 30, "shortDescription exceeds 30 characters")
check(interface.get("category") in {"Business & Operations","Communication","Creativity","Data & Analytics","Developer Tools","Education & Research","Entertainment","Finance","Healthcare","Other","Productivity","Scientific Research","Security","Travel"}, "unsupported category")
check(isinstance(interface.get("capabilities"), list), "interface.capabilities must be an array")

skill_dirs = sorted((PKG / "skills").glob("*"))
check(bool(skill_dirs), "no top-level skills found")
names = []
for folder in skill_dirs:
    skill = folder / "SKILL.md"
    check(skill.is_file(), f"missing SKILL.md: {folder.name}")
    if not skill.exists(): continue
    content = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    check(match is not None, f"missing YAML frontmatter: {skill}")
    if not match: continue
    fm = match.group(1)
    name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", fm)
    desc = re.search(r"(?m)^description:\s*(.+)$", fm)
    check(name is not None, f"missing name in frontmatter: {skill}")
    check(desc is not None and bool(desc.group(1).strip()), f"missing description in frontmatter: {skill}")
    if name: names.append(name.group(1))
    check(len(content.encode("utf-8")) <= 1024*1024, f"skill exceeds 1 MiB: {skill}")
check(len(names) == len(set(names)), "duplicate skill names")
check(len(skill_dirs) == 13, f"expected 13 skill folders (M00 + O01–O12), found {len(skill_dirs)}")

for rel in ["references/architecture-and-routing.md", "references/evaluation-framework.md", "references/contract-specifications.md", "references/security-and-authority.md", "references/forensic-methods-and-limits.md", "references/lifecycle-and-recovery.md", "references/tool-adapter-contract.md", "tests/acceptance-cases.json", "LICENSE", "README.md"]:
    check((PKG / rel).is_file(), f"required package file missing: {rel}")
try:
    cases = json.loads((PKG / "tests/acceptance-cases.json").read_text(encoding="utf-8"))
    check(len(cases.get("cases", [])) >= 20, "acceptance fixtures fewer than 20")
except Exception as exc:
    errors.append(f"cannot parse acceptance-cases.json: {exc}")

if errors:
    print("STATIC VALIDATION: FAIL")
    for e in errors: print(f"- {e}")
    sys.exit(1)
print(f"STATIC VALIDATION: PASS — {len(skill_dirs)} skills, {len(cases['cases'])} fixtures, manifest and required references present")
