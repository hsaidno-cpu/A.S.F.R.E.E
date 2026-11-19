# A.S.F.R.E.E Architecture & Routing Contract

## Product identity

A.S.F.R.E.E means **AI Systems Forensics & Reconstruction Evaluation Engine**. It is a portable, evidence-driven, modular, supervised engineering intelligence package. Its object model and adapter contracts are designed for extension, but access and execution depend on actual host capabilities, authorization, and external infrastructure.

## Eight architectural layers

| Layer | Name | Responsibility |
|---|---|---|
| L01 | Interface & Access | User/API/CLI/SDK/MCP entry, identity, request scope |
| L02 | Artifact Acquisition | Discovery, parsing, provenance, integrity, inventory |
| L03 | Intelligence & Analysis | Anatomy, positive/negative/comparative analysis, diagnosis |
| L04 | Orchestration & Control | M00 intent, routing, task graph, state, arbitration |
| L05 | Engineering & Transformation | Remediation, reconstruction, adaptation, refactoring |
| L06 | Execution & Integration | Approved adapters, tool broker, isolated runtime |
| L07 | Verification & Assurance | QA, independent review, acceptance, release verification |
| L08 | Governance & Observability | Security, privacy, audit, telemetry, cost, retention |

O11 Security & Governance controls all layers. O12 Evaluation Intelligence defines and checks criteria, measurement validity, evidence sufficiency, impact, and meta-evaluation across all layers.

## Master and specialist registry

See `../skills/asfree-master-orchestrator/SKILL.md` for the authoritative O01–O12 routing registry. The specialist skill files define their bounded mission, operating procedure, deliverables, and stop conditions. The specialist catalogue labels are capabilities/procedures, not separate deployed agents by default.

## Four intelligence engines

1. **Positive Analysis:** identify → verify → evaluate contextual value → preserve/amplify/replicate/leverage/integrate/standardize.
2. **Negative Analysis:** detect → substantiate → diagnose → prioritize proportionately → correct/prevent/detect/mitigate/recover/avoid/transfer/accept/monitor.
3. **Comparative Analysis:** establish baseline → normalize criteria → compare deltas → identify gaps → assess trade-offs → recommend conditionally.
4. **Evaluation-to-Transformation:** finding/value → root cause or value mechanism → intervention → authorization → implementation → verification → impact and residual-risk review.

Evaluation governs all four engines. Do not turn the four engines into mandatory sequential phases when the task does not need them.

## Handoff contract

Each specialist handoff should carry: `case_id`, `task_id`, `target_id`, purpose, scope/non-goals, inputs/provenance, required capability/permission, method, findings/evidence IDs, assumptions/unknowns, dependencies, expected output schema, acceptance criteria, risk/authority gate, status, and next owner. Missing fields must be explicit as unknown or not applicable.

## Parallelism and delegation

Parallelize only genuinely independent read-only tasks. Sequence dependent tasks. Bound retries and delegation depth. Report an invocation as `INVOKED` only when a host tool confirms it; otherwise use `PROCEDURE_APPLIED`, `BEHAVIOR_ONLY`, or `NOT_OBSERVABLE` as appropriate.
