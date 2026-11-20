# A.S.F.R.E.E — AI Systems Forensics & Reconstruction Evaluation Engine

**Version:** 0.3.0  
**Package type:** Portable skills-only plugin  
**Architecture:** M00 + O01–O12; eight system layers; cross-cutting O11 Security & Governance and O12 Evaluation Intelligence  
**Operating model:** Evidence-led supervised engineering; read-only by default  
**Implementation boundary:** The portable plugin contains instruction and contract files. A separate local reference runtime exists in the source repository under `../runtime/`; it is not bundled with this plugin.

## What it does

A.S.F.R.E.E coordinates authorized technical investigation: artifact intake, provenance, structural/functional decomposition, strengths and value preservation, adversarial weakness analysis, comparison, defect diagnosis, evaluation, supervised remediation, reconstruction, tool adaptation, QA, independent verification, and impact review.

## Architecture

- **M00:** intent, scope, operating mode, authority, routing, task graph, arbitration, synthesis, lifecycle disposition.
- **O01–O10:** artifact, anatomy, positive, negative, comparative, diagnostics, remediation, reconstruction, integration/runtime, and validation/QA specialists.
- **O11:** Security & Governance control plane across all layers.
- **O12:** Evaluation Intelligence control plane across all stages.

The specialist files define bounded procedures. Their capability catalogues are not claims that separate autonomous agents have been deployed. If the host does not expose separate invocation, report `PROCEDURE_APPLIED` rather than `INVOKED`.

## Package contents

- `plugin.json` — portable Agent Plugins 1.0 manifest.
- `.codex-plugin/plugin.json` — synchronized compatibility manifest.
- `skills/` — M00 and O01–O12 instructions.
- `references/` — architecture, data contracts, evaluation, forensic limits, lifecycle/recovery, security/authority, tool-adapter contract, and JSON Schemas.
- `tests/acceptance-cases.json` and `tests/p0-foundations-cases.json` — declarative behavior fixtures, not test execution evidence.
- `LICENSE` — PolyForm Noncommercial 1.0.0.
- `TRADEMARKS.md` — separate brand and trademark notice.

## Capability boundary

The portable plugin does **not** include or deploy the adjacent `runtime/` project, an API gateway, MCP server, scanner, database, sandbox, cloud runtime, or CI/test service. The repository's optional Python reference runtime is a separate local single-node development/evaluation adapter. Access to files, repositories, APIs, MCP servers, runtimes, and write paths depends on actual host tools, connectors, scopes, and infrastructure. Every operation must pass capability-readiness and authorization checks.

## Operating model

The forensic depth scale is L0–L6. The supervised authority scale is S0–S5. Read-only is the default. Mutation, upload/publication, permission changes, credential actions, migration, staging/production deployment require exact scoped authorization. Implementation, verification, merge, release, and read-back are distinct states.

## License and brand

The source package is distributed under PolyForm Noncommercial License 1.0.0. It is source-available, not an OSI-approved open-source license, and does not grant third-party commercial-use rights. Separate written commercial permission is required from the applicable rights holder. The software license does not license the A.S.F.R.E.E name, logo, or other brand assets. Confirm the legally designated rights holder before assigning rights to any future foundation entity.
