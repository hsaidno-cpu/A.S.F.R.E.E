# A.S.F.R.E.E — AI Systems Forensics & Reconstruction Evaluation Engine

**Version:** 0.2.0  
**Package type:** Skills-only plugin  
**Architecture:** M00 + O01–O12; eight system layers; cross-cutting O11 Security & Governance and O12 Evaluation Intelligence  
**Operating model:** Evidence-led supervised engineering; read-only by default  
**Implementation status:** Portable instruction and contract package. External tool/runtime backends are not bundled.

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
- `tests/acceptance-cases.json` — declarative behavior fixtures. They are specifications until executed in a real harness.
- `LICENSE` — PolyForm Noncommercial 1.0.0.
- `TRADEMARKS.md` — separate brand and trademark notice.

## Capability boundary

This package does **not** deploy an API gateway, MCP server, scanner, database, sandbox, cloud runtime, or CI/test service. Access to files, repositories, APIs, MCP servers, runtimes, and write paths depends on actual host tools, connectors, scopes, and infrastructure. Every operation must pass capability-readiness and authorization checks. If unavailable, mark `NOT_CHECKED`, `UNAVAILABLE`, `ACCESS_DENIED`, `BLOCKED`, or `NOT_RUN` and use a safe fallback only.

## Operating model

The forensic depth scale is L0–L6. The supervised authority scale is S0–S5. Read-only is the default. Mutation, upload/publication, permission changes, credential actions, migration, and deployment require exact scoped authorization. Implementation, verification, merge, release, and read-back are distinct states.

## Evaluation

Evaluation is continuous. The package defines 15 internal E.V.A.L.U.A.T.I.O.N values, five supplementary controls, 12 context-sensitive dimensions, and E0–E7 evaluation checkpoints. These are internal design rubrics, not external certification. Scores require operational definitions, methods, data, rubrics, uncertainty, and defensible weights. Critical hard gates cannot be hidden by averages.

## License and brand

The source package is distributed under PolyForm Noncommercial License 1.0.0. It is source-available, not an OSI-approved open-source license, and does not grant third-party commercial-use rights. Separate written commercial permission is required from the applicable rights holder. The software license does not license the A.S.F.R.E.E name, logo, or other brand assets. See `LICENSE` and `TRADEMARKS.md`. Confirm the legally designated rights holder before assigning rights to any future foundation entity.
