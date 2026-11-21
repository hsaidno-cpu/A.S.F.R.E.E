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

## Canonical routing and compatibility aliases

The numbered O01–O12 paths listed in M00 are the only canonical specialist procedures. The repository may retain historical, unnumbered paths for backward compatibility, but each such path must be a redirect-only pointer to exactly one numbered specialist. It must not carry an alternate workflow, methods, schemas, authority decisions, or independent state.

The canonical alias map and release-version authority are maintained in [Release, Source-of-Truth & Routing Governance](release-and-routing-governance.md). M00 must route to the numbered destination, not invoke both the historical alias and its canonical destination. If an alias target is unavailable, report the relevant capability as unavailable instead of reviving a stale implementation.

## Release synchronization boundary

The repository package manifest is the source version authority for a portable package release. The compatibility manifest and package README must match it. The Plugin Creator app release is a separate deployed artifact and must be updated from the reviewed source package, then verified by metadata and file read-back. Runtime and source-bundle versions are independent version planes. A commit, open pull request, package upload, app release, and production deployment are distinct lifecycle states.
## P1.1 cross-layer security contract

O11 governs the trust policy and hard gates across L01–L08; O09 owns runtime/provider capability evidence; O12 evaluates validity, test coverage and residual risk; M00 retains case-level arbitration. No additional case-level orchestrator is introduced.

The security facade must sit at the operation boundary rather than only at the API entry point. Every SCIVE transition is separately authorized and tenant-bound. Cross-process delegation must be signed, audience/action/resource-bound, attenuable, expiring, replay-protected and revocable. Sensitive storage coverage includes metadata, WAL, temp, logs, audit and backup, not just blob content.

Production execution is not established by container flags or a command builder. Require host-provisioned sandbox and quota enforcement, bounded streaming, real tenant isolation tests, external WORM read-back, concurrency testing and independent human review. See [P1.1 Security-to-Production Readiness Contract](p1.1-security-production-readiness.md).
