# A.S.F.R.E.E — AI Systems Forensics & Reconstruction Evaluation Engine

**Version:** 1.0.0  
**Package type:** Skills-only ChatGPT plugin  
**Architecture:** M00 + O01–O12, with cross-cutting Evaluation and Security control planes  
**Operating model:** Supervised engineering, read-only by default  
**Implementation status:** Instruction package prepared; tool/runtime backends are not bundled.

## What it does

A.S.F.R.E.E coordinates evidence-led examination of authorized technical systems: artifact inventory, structural and functional decomposition, positive and negative analysis, comparison, defect diagnosis, remediation design, reconstruction planning, tool readiness, QA and continuous evaluation.

## Architecture

- `M00` — master intent, scope, routing, task graph, arbitration and synthesis.
- `O01–O10` — artifact, anatomy, positive, negative, comparative, diagnostics, remediation, reconstruction, runtime integration and QA specialists.
- `O11` — Security & Governance cross-cutting control plane.
- `O12` — Evaluation Intelligence cross-cutting control plane.

The 65 O12 sub-specialist procedures are grouped into eight families. They are not separate runtime agents by default. This is deliberate: explicit contracts and evidence are more valuable than multiplying agents that merely hand work to one another.

## Package contents

- `plugin.json` — Agent Plugins 1.0 manifest.
- `skills/` — 13 callable skill instruction units (M00 + O01–O12).
- `references/` — shared architecture, evidence contracts, evaluation, security, methods, recovery and tool-adapter rules.
- `tests/acceptance-cases.json` — static behavioral acceptance fixtures; not proof of runtime execution.

## Important capability boundary

This package contains instructions and orchestration procedures. It does **not** deploy an API gateway, MCP server, scanner, database, sandbox, cloud runtime or CI service. Actual filesystem/repository/API/MCP access and tests depend on tools, connectors, permission scopes and execution infrastructure available in the host. Each operation must pass a readiness/authorization check. If a capability is missing, the workflow records `NOT_CHECKED`, `UNAVAILABLE`, `ACCESS_DENIED`, `BLOCKED` or `NOT_RUN` and falls back only when safe.

## Use

Invoke `A.S.F.R.E.E` with a target artifact/system and the intended objective. For a full-cycle task, state the authorized scope, target/version, desired outcome and whether you are authorizing only a read-only audit or a specific engineering scope. Do not provide passwords, API keys, tokens or private keys in prompts.

## Forensic and authority model

Inspection depth is reported as L0 conceptual through L6 verified deployment. Change authority ranges from S0 Observe to S5 Production Release. Read-only is the default; mutation, upload, permission changes, migration and deployment require scoped authorization. Implementation, test, merge and release statuses remain separate.

## Evaluation

Evaluation is continuous, not a final score. A.S.F.R.E.E defines 15 internal evaluation values, five supplementary control values and 12 context-sensitive dimensions. Scores require defined methods, data, rubrics and uncertainty; critical hard gates cannot be hidden by averages.

## License and brand

This source-available package is distributed under PolyForm Noncommercial License 1.0.0. It is not an OSI-approved open-source license and does not grant third-party commercial-use rights. Separate written commercial permission is required from the rights holder. The A.S.F.R.E.E name and branding are not licensed by the software license. See `LICENSE` and `TRADEMARKS.md` in the project repository for policy details.
