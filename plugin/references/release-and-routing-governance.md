# Release, Source-of-Truth & Routing Governance

**Status:** normative repository contract  
**Applies to:** the portable A.S.F.R.E.E plugin, its Plugin Creator deployment, compatibility skill paths, and the separate reference runtime.

## 1. Distinct version planes

A.S.F.R.E.E has multiple versioned artifacts. Their versions are related by a release process, not required to be numerically identical.

| Artifact | Version authority | Rule |
|---|---|---|
| Portable plugin package | `plugin/plugin.json` | Canonical package SemVer for the repository release |
| Compatibility manifest | `plugin/.codex-plugin/plugin.json` | Must match the portable manifest name, version, description, license, and interface metadata |
| Plugin package README | `plugin/README.md` | Must report the same package version |
| Plugin Creator deployment | Plugin Creator release metadata | Must be updated from the reviewed repository package and read back after update |
| Repository release notes | `CHANGELOG.md` | Must explain the package change; a changelog entry alone does not create a release |
| Local reference runtime | `runtime/pyproject.toml` after bundle reconstruction | Independent runtime SemVer; do not bump merely because the plugin package changes |
| Runtime source bundles | `implementation-bundles/*` | Each archive/overlay retains its own version and SHA-256 sidecar |
| Legacy redirect plugin | Its own Plugin Creator metadata | Remains a compatibility pointer; never treat its version as the canonical package version |

At this release boundary, plugin package version is **0.3.2** and the P1 local reference runtime remains **0.2.0**. The P0 baseline and hardening bundle identifiers are also independent versioned artifacts.

## 2. Source-of-truth precedence

1. The reviewed Git commit is the source snapshot for a repository package release.
2. `plugin/plugin.json` is the canonical package manifest in that snapshot.
3. `plugin/.codex-plugin/plugin.json` is a compatibility mirror, not a second authority.
4. M00 and O01–O12 are the only canonical specialist procedures.
5. Plugin Creator stores the deployed app-backed release. Its release metadata and file read-back must be checked after every deployment update.
6. A GitHub commit, open PR, Plugin Creator upload, and deployed release are separate states. Never infer one from another.

Never use the Plugin Creator release version as a substitute for the repository source version, and never use the runtime package version as the plugin package version.

## 3. Canonical specialist topology

M00 is the only case-level coordinator. O01–O12 are the canonical specialist procedures. Their routing IDs and paths are defined in `skills/asfree-master-orchestrator/SKILL.md`.

The repository retains historical, unnumbered skill paths for backward compatibility. They are **redirect-only aliases**, not independent specialists:

| Historical path | Canonical destination |
|---|---|
| `skills/anatomy-decomposition/SKILL.md` | `skills/o02-anatomy-decomposition/SKILL.md` |
| `skills/artifact-intelligence/SKILL.md` | `skills/o01-artifact-intelligence/SKILL.md` |
| `skills/bug-detection-diagnosis/SKILL.md` | `skills/o06-bug-detection-diagnosis/SKILL.md` |
| `skills/comparative-intelligence/SKILL.md` | `skills/o05-comparative-intelligence/SKILL.md` |
| `skills/evaluation-intelligence/SKILL.md` | `skills/o12-evaluation-intelligence/SKILL.md` |
| `skills/integration-runtime-lab/SKILL.md` | `skills/o09-integration-runtime-lab/SKILL.md` |
| `skills/negative-intelligence/SKILL.md` | `skills/o04-negative-intelligence/SKILL.md` |
| `skills/positive-intelligence/SKILL.md` | `skills/o03-positive-intelligence/SKILL.md` |
| `skills/reconstruction-adaptation/SKILL.md` | `skills/o08-reconstruction-adaptation/SKILL.md` |
| `skills/remediation-bug-fixing/SKILL.md` | `skills/o07-remediation-bug-fixing/SKILL.md` |
| `skills/security-governance/SKILL.md` | `skills/o11-security-governance/SKILL.md` |
| `skills/validation-quality-assurance/SKILL.md` | `skills/o10-validation-qa/SKILL.md` |

An alias must contain only a pointer to its canonical destination. It must not duplicate methods, authority rules, schemas, state, or a separate specialist workflow. M00 routes only to the numbered canonical O01–O12 paths. New functionality belongs in the canonical skill and must be reviewed for impact on schemas, references, fixtures, and consumers.

The app-backed Plugin Creator package contains M00 and O01–O12 as its canonical specialist set. Repository compatibility aliases must not be mistaken for additional app agents or additional independent authority.

## 4. Release transaction

A package release is complete only when the applicable stages are evidenced:

1. **Prepare:** update package source on a dedicated branch; preserve the main-branch baseline and unrelated assets.
2. **Static validate:** check both manifests, README version, canonical skill registry, alias redirects, schemas, acceptance fixtures, and release documentation.
3. **CI verify:** inspect the workflow run for the exact PR head SHA. Report test steps and failed/skipped steps, not just a green badge.
4. **Review and merge:** inspect the diff and dependency impact; merge only under the repository's review policy.
5. **Deploy app package:** build an overlay containing the reviewed changed files and update the existing Plugin Creator plugin using its current release ID as a concurrency guard.
6. **Read back:** inspect Plugin Creator metadata and file contents; confirm the deployed package version and content match the merged repository snapshot.
7. **Close the release:** record commit SHA, CI run, PR, Plugin Creator release ID/version, verification status, and known limitations in the changelog or release record.

If the GitHub PR is open but not merged, record `PR_OPEN`. If the Plugin Creator update has not been read back, record deployment as unverified. A successful local ZIP build is not a plugin update. A Plugin Creator upload is not a verified release until metadata and files are read back.

## 5. Required release invariants

- The two manifests must have matching package identity and version.
- The package README version must match the canonical manifest.
- Runtime and bundle versions remain independently declared.
- Every historical skill name must map to exactly one canonical O01–O12 destination.
- Every compatibility alias must be redirect-only.
- M00 remains the only case-level coordinator.
- No new specialist is added without a demonstrated single-responsibility need, routing rule, handoff contract, acceptance coverage, and lifecycle owner.
- Every material capability claim must distinguish declarative contract, implemented source, executed test, live integration, and verified deployment.
- No version, test, approval, release, or deployment claim may be inferred from an adjacent lifecycle state.

## 6. Rollback and compatibility

Keep the previous Plugin Creator release and Git commit available as recovery points. A rollback must identify the exact target version and the reason for rollback; do not silently rewrite historical releases. Compatibility aliases remain until their consumers are migrated or a separately reviewed deprecation removes them.


## 7. Ecosystem identity registry

The normative identity catalog is `references/ecosystem-identity-registry.json`, validated by `references/schemas/governance/ecosystem-identity-registry.schema.json`. Do not create an identity or infer a canonical role from display names.

- Each product has one stable `product_id` and exactly one registered plugin with role `CANONICAL`.
- Every plugin has one stable registry `identity_id`, one immutable Plugin Creator `plugin_id`, one package name, one declared version source, and one declared change-history source.
- A compatibility redirect must map to exactly one canonical plugin within the same product. It is not another M00, product authority, version authority, or execution fallback.
- New independent products/plugins require distinct purpose, identity, ownership, source/version authority, changelog, migration policy, and acceptance coverage before registry admission.
- CI must reject duplicate IDs/names, multiple canonical plugins for a product, missing redirect targets, and absent version/history sources.

The registry is the ecosystem identity authority. The canonical package manifest remains the package SemVer authority. These are different responsibilities and must not be collapsed into a single overloaded version field.

## 8. Canonical source and active-version rule

For A.S.F.R.E.E, only `plugin/plugin.json#/version` in a reviewed commit merged into `main` is the active canonical plugin package version. A branch, release candidate, open PR, archive, or Plugin Creator upload is not an active source release.

The Plugin Creator canonical plugin ID is stable and is registered once. Its release ID and deployed files form deployment evidence. They must be reconciled against the reviewed repository commit by metadata and file read-back. They do not supersede or redefine the repository version authority.

The legacy `asfree-master-orchestrator` Plugin Creator ID is registered as `COMPATIBILITY_REDIRECT`. Its own SemVer versions only the redirect shell. Never copy the canonical package version into legacy manifests, skill instructions, or descriptions.

## 9. Migration and deprecation

Follow `references/migration-and-deprecation-policy.md` for identity mapping, version boundaries, change history, schema/status conversion, manual context migration, redirect constraints, and retirement gates.

No dual authority, dual-run orchestration, silent schema coercion, or automatic legacy fallback is permitted. If the canonical destination or a required migration mapping is unavailable, stop and report the blocker. Keep old releases and evidence recoverable; retirement requires an explicit human decision.
