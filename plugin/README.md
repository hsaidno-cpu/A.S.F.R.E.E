# A.S.F.R.E.E — AI Systems Forensics & Reconstruction Evaluation Engine

**Version:** 0.5.0-rc.1  
**Package type:** Portable skills-only plugin  
**Architecture:** M00 + O01–O12; subordinate RPEDS roadmap lifecycle control plane; eight system layers; cross-cutting O11 Security & Governance and O12 Evaluation Intelligence  
**Operating model:** Evidence-led supervised engineering; read-only by default  
**Implementation boundary:** The portable plugin contains instruction and contract files only. The separate local Python reference runtime is distributed through checksum-pinned source bundles under `../implementation-bundles/` and reconstructed by repository scripts for local/CI validation; it is not bundled with this plugin.

## What it does

A.S.F.R.E.E coordinates authorized technical investigation: artifact intake, provenance, structural/functional decomposition, strengths and value preservation, adversarial weakness analysis, comparison, defect diagnosis, evaluation, supervised remediation, reconstruction, tool adaptation, QA, independent verification, and impact review.

## Architecture

- **M00:** intent, scope, operating mode, authority, routing, task graph, arbitration, synthesis, lifecycle disposition.
- **O01–O10:** artifact, anatomy, positive, negative, comparative, diagnostics, remediation, reconstruction, integration/runtime, and validation/QA specialists.
- **O11:** Security & Governance control plane across all layers.
- **O12:** Evaluation Intelligence control plane across all stages.

The specialist files define bounded procedures. Their capability catalogues are not claims that separate autonomous agents have been deployed. If the host does not expose separate invocation, report `PROCEDURE_APPLIED` rather than `INVOKED`.

## Canonical routing and release governance

M00 is the only case-level coordinator. Numbered O01–O12 paths are the only canonical specialist procedures. Historical unnumbered names retained in the source repository are redirect-only compatibility aliases; they do not represent additional specialists and are not part of this canonical app-backed skill set.

The repository package version is declared by `plugin.json`; `.codex-plugin/plugin.json` and this README must match it. Plugin Creator app releases are separate deployments and require a guarded update plus metadata/file read-back. Local runtime and source-bundle versions are independent. See [Release, Source-of-Truth & Routing Governance](references/release-and-routing-governance.md).
 
## Package contents

- `plugin.json` — portable Agent Plugins 1.0 manifest.
- `.codex-plugin/plugin.json` — synchronized compatibility manifest.
- `skills/` — M00 and O01–O12 instructions.
- `references/` — architecture, release/routing governance, P1.1 security-to-production readiness, data contracts, evaluation, forensic limits, lifecycle/recovery, security/authority, tool-adapter contract, and JSON Schemas.
- `references/schemas/rpeds/` — seven Draft 2020-12 contracts for roadmap, milestone, iteration, progress, adaptation, risk and work item.
- `tests/rpeds-schema-fixtures.json` and `scripts/validate_rpeds_contracts.py` — executable schema and graph-integrity checks; 24 behavioral acceptance cases remain specification-only.
- `tests/acceptance-cases.json` — 30 baseline fixtures; `tests/release-governance-cases.json` — five release/routing fixtures; `tests/p1-security-hardening-cases.json` — 20 P1.1 security acceptance specifications. Fixtures are specifications, not test execution evidence.
- `LICENSE` — PolyForm Noncommercial 1.0.0.
- `TRADEMARKS.md` — separate brand and trademark notice.

## Capability boundary

The portable plugin does **not** include or deploy the adjacent `runtime/` project, an API gateway, MCP server, scanner, database, sandbox, cloud runtime, or CI/test service. The repository's optional Python reference runtime is a separate local single-node development/evaluation adapter. Access to files, repositories, APIs, MCP servers, runtimes, and write paths depends on actual host tools, connectors, scopes, and infrastructure. Every operation must pass capability-readiness and authorization checks.

## Operating model

The forensic depth scale is L0–L6. The supervised authority scale is S0–S5. Read-only is the default. Mutation, upload/publication, permission changes, credential actions, migration, staging/production deployment require exact scoped authorization. Implementation, verification, merge, release, and read-back are distinct states.

## License and brand

The source package is distributed under PolyForm Noncommercial License 1.0.0. It is source-available, not an OSI-approved open-source license, and does not grant third-party commercial-use rights. Separate written commercial permission is required from the applicable rights holder. The software license does not license the A.S.F.R.E.E name, logo, or other brand assets. Confirm the legally designated rights holder before assigning rights to any future foundation entity.

## P1.1 security-to-production gates

Release candidate 0.4.0-rc.1 adds explicit architecture and acceptance contracts for verified IdP/MFA assurance, signed cross-process delegation, authorization at every SCIVE transition, encrypted metadata/WAL/temp/log/audit/backup, managed KMS/HSM, provisioned rootless OCI plus gVisor/Kata, host-enforced quotas, bounded streaming output, external WORM audit anchoring, infrastructure-level tenant isolation, concurrency testing and independent human security review.

These are hard gates and acceptance specifications, not proof that production providers or hosts are provisioned. See [P1.1 Security-to-Production Readiness](references/p1.1-security-production-readiness.md). The local reference runtime remains on its separately declared version until an independently reviewed runtime source overlay is integrated.


## Ecosystem identity and migration governance

This package follows the ecosystem's Single Canonical Source of Truth contract. The identity catalog is [Ecosystem Identity Registry](references/ecosystem-identity-registry.json); migration and retirement rules are in [Migration and Deprecation Policy](references/migration-and-deprecation-policy.md). Every product has one canonical plugin identity; redirect packages are registered aliases, not alternate orchestrators. The canonical version comes from the reviewed repository manifest merged into `main`; Plugin Creator deployment metadata is verified separately by read-back.


## RPEDS progressive roadmap control plane

RPEDS manages versioned roadmaps, phases, milestones, iterations, work-item states, evidence-count progress, evaluation checkpoints and adaptive replan proposals. It is subordinate to M00 and delegates evaluation judgment to O12, actual test verification to O10, authorization to O11, engineering to O07/O08, and supported execution to O09. It is not an additional case-level orchestrator or O13 specialist. The portable package adds instructions, reference modules, schemas and acceptance specifications only; it does not deploy a persistent scheduler, automatic monitor, runtime database or GitHub–Notion synchronizer.
