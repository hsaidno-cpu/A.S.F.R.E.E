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


## PRE–RPEDS shared roadmap DNA — native RPEDS workstream

PRE Standalone and RPEDS are two first-class manifestations of one jointly evolved roadmap DNA. PRE remains independently usable; RPEDS remains the native A.S.F.R.E.E roadmap workstream, retaining its identity, four original modules and host-specific procedures. They share the R0–R9 kernel, roadmap object model, evidence/measurement/gate contracts, adaptive decisions, process history, assurance/closure, learning federation and release lineage. RPEDS is not deleted, reduced to a name-only redirect or replaced by a competing engine. It remains subordinate to M00, which is the sole case coordinator. The four bounded RPEDS modules and lifecycle are specified in `skills/rpeds-progressive-development/SKILL.md` and `references/rpeds/`.

### Conditional O03–O06 routing contract

M00 evaluates each route independently against the decision question, current evidence and scope. A route is not activated merely to complete a fixed bundle.

| Specialist | Trigger condition | Required work product | Explicit non-trigger |
|---|---|---|---|
| O03 Positive Intelligence | A material roadmap change may remove/regress evidenced value, capability, compatibility or protected behavior; or the decision asks what must be preserved/amplified. | Evidence-backed value register, realized/potential classification, preservation invariants, non-regression criteria. | Generic praise, unverified potential, or inventory without a value/preservation question. |
| O04 Negative Intelligence | A credible adverse scenario, failure mode, misuse path, security/privacy exposure or operational hazard could change the decision. | Scenario dossier, epistemic state, impact/severity, likelihood/uncertainty, control gaps and residual risk. | Speculation without a plausible mechanism; an observed defect needing root-cause work alone. |
| O05 Comparative Intelligence | Two or more feasible options or a baseline-to-target comparison must be judged against common criteria. | Candidate set, comparability analysis, normalized criteria, hard-gate matrix, trade-offs and conditional recommendation. | Single-object assessment or invented/incomparable alternatives. |
| O06 Bug Detection & Diagnosis | An observed failure, regression, contract mismatch or unexplained variance needs reproduction and causal diagnosis. | Valid oracle, expected/observed record, reproduction state, competing hypotheses, falsification evidence and confidence. | Hypothetical threat or structural design concern with no observed malfunction. |

**Routing sequence:** establish baseline with O01/O02 where necessary; run O03/O04 in parallel only when value and risk questions are independent; run O06 when observed behavior needs diagnosis; invoke O05 when real candidate paths exist and can be normalized. O05 may consume O03 preservation constraints and O04 risk constraints. O06 commonly precedes comparison of corrective options. M00 deduplicates findings and resolves overlap.

**Authority:** O03–O06 analyze and recommend only. O11 controls authorization, security/privacy and risk acceptance; O10 owns test execution and independent verification; O12 owns evaluation criteria, measurement validity and judgment; O09 owns supported runtime execution; O07/O08 own accepted change design. No O03–O06 specialist may approve a roadmap, mutate a target, accept a risk or declare a gate PASS.

Every handoff records route rationale, evidence/provenance, method, claim/evidence class, counterevidence, uncertainty, constraints, next owner, acceptance criterion and stop condition. Route decision (`REQUIRED/OPTIONAL/NOT_REQUIRED/UNRESOLVED`) is separate from execution state (`INVOKED/PROCEDURE_APPLIED/BEHAVIOR_ONLY/NOT_RUN/BLOCKED/UNAVAILABLE`). A selected route lacking permission/evidence remains blocked/unresolved, not silently skipped.

## PRE–RPEDS shared DNA and host adaptation

The shared kernel and host manifestations are separate architectural concepts. The kernel owns common roadmap semantics and contract lineage. PRE Standalone and A.S.F.R.E.E RPEDS retain separate host-facing identities, extensions and release/adoption receipts. RPEDS keeps its four original modules and native M00/O01–O12 handoffs. Shared-core behavior must not be duplicated into diverging copies; host-specific logic remains in the host extension.

AFSA evaluates each incoming shared-core release against host-approved SOP, authority, security, privacy, data boundaries, supported tools, audit sink and rollback. Additive compatible changes may auto-adopt after tests. Conflicts must be adapted under authority, held or quarantined. A host-specific extension may be proposed back to the shared kernel only after sanitization, validation and federation review.
