# RPEDS Architecture — Progressive Roadmap Control Plane

## Executive definition

**RPEDS — Roadmap Progressive Evaluation & Development System** is a lifecycle control plane for planning, sequencing, monitoring and adapting multi-phase development. It turns an objective into a versioned roadmap, decomposes it into phases and milestones, manages iterations and work items, schedules evidence-backed evaluations, and recommends roadmap changes from observed results.

RPEDS is part of the A.S.F.R.E.E ecosystem, but it is not a ninth architectural layer, not a second case-level master, and not O13. M00 remains the only case-level coordinator.

## Architectural boundaries

| Concern | Authority |
|---|---|
| Case intent, scope, routing, arbitration, final disposition | M00 |
| Target anatomy, system decomposition and dependencies | O02 |
| Baseline artifact/source inventory | O01 |
| Verified strength/value preservation where a change may destroy existing value | O03 |
| Adversarial risk, misuse and failure-mode analysis | O04 |
| Normalized comparison of alternative replan paths | O05 |
| Reproduction/diagnosis of defects driving a replan | O06 |
| Evaluation charter, criteria, measurement validity, judgment, impact and meta-evaluation | O12 |
| Test design/execution, actual outcome and independent verification | O10 |
| Corrective/preventive change design | O07 |
| Reconstruction, migration and architecture adaptation | O08 |
| Supported tool/runtime/API/MCP execution | O09 |
| Authorization, privacy, security, consequential approvals | O11 |
| Roadmap objective tree, phase/milestone lifecycle, iterations, progress ledger, replan proposals | RPEDS |

RPEDS orchestrates when these responsibilities are needed; it does not reimplement them. It receives their structured outputs and returns roadmap decisions to M00.

## Conditional O03–O06 route selection

M00 selects each route independently from the actual decision need:

- **O03** when a change could remove/regress evidenced value or capability, or when explicit preservation constraints are required. Output: realized-versus-potential value register, preservation invariants and non-regression criteria.
- **O04** when credible failure, misuse, security/privacy exposure, dependency risk or harmful side effects could change the roadmap. Output: scenario-based risk/failure dossier, evidence status, controls and residual risk.
- **O05** when at least two feasible alternatives or a valid baseline-to-target comparison must be judged. Output: comparability assessment, normalized criteria, hard gates, trade-offs and conditional recommendation.
- **O06** when an observed/reported failure, regression, contract mismatch or unexplained variance needs bounded reproduction and root-cause diagnosis. Output: expected/observed record, oracle, reproduction state, competing hypotheses and falsification path.

Do not activate a route for its non-trigger: O03 is not generic praise; O04 is not unsupported worst-case storytelling; O05 does not invent candidates or compare unlike contexts; O06 does not call an untested suspicion a confirmed defect. O03/O04 can run in parallel on a shared baseline only when their questions are independent. O05 consumes real candidates and can use O03/O04 constraints. O06 precedes remediation design and may precede option comparison. M00 records route decision separately from invocation/execution state and resolves overlap.

No O03–O06 specialist authorizes target mutation, accepts risk, approves a roadmap or marks a gate PASS. O11 owns authorization/security, O10 owns test execution and independent verification, O12 owns evaluation judgment, O09 owns supported runtime execution, and O07/O08 own accepted change design.


## Four internal capability modules

1. **Roadmap Architecture Planner** — objective hierarchy, roadmap revisions, phases, milestone design, dependency DAG, feasibility and baseline.
2. **Progressive Development Manager** — iterative commitments, work-item states, milestone sequencing, scope drift and delivery tracking.
3. **Continuous Evaluation Engine** — evaluation checkpoint schedule, indicator registry, evidence and gate visibility; O12 decides the evaluation.
4. **Adaptive Roadmap Optimizer** — trigger detection, alternative comparison, dependency impact, rebaseline proposal and decision history.

The modules are bounded procedures and references, not claims that separate autonomous agents are deployed.

## Lifecycle model

R0 INTAKE → R1 STRATEGY & BASELINE → R2 ROADMAP DESIGN → R3 APPROVAL & BASELINE FREEZE → R4 ITERATION EXECUTION → R5 FORMATIVE CHECK → R6 MILESTONE ACCEPTANCE → R7 OUTCOME & IMPACT → R8 ADAPTATION → R9 CLOSURE.

The lifecycle loops when evidence requires re-sequencing or replanning. O12's E0–E7 lifecycle remains distinct: E0–E2 establish charter/baseline/evidence, E3–E5 inform formative and milestone/post-change evaluation, E6 evaluates outcomes, and E7 performs meta-evaluation at R9 or a declared periodic review. R8 uses current E3–E6 evidence to adapt; it does not wait for or substitute E7.

## State and hard-gate design

Maintain separate state fields for roadmap lifecycle, phase and milestone progress, iteration status, work-item implementation and verification, test execution, evaluation disposition, decision approval, release and deployment, and outcome/impact confirmation.

A commit is not a merge; a merge is not a release; a release is not deployment; deployment is not proof of impact. NOT_RUN, NOT_ASSESSED, HOLD, FAIL, BLOCKED and UNVERIFIABLE cannot be converted to PASS by a summary score.

A milestone is accepted only against predeclared exit criteria with linked implementation, actual test/verification records, O12 evaluation disposition, required approval and no unresolved hard-gate blocker.

## Progress measurement

Default to evidence-count measures and present them separately:
- delivery completion = verified in-scope work items / approved in-scope work items;
- milestone acceptance = accepted milestones / approved milestones;
- verification coverage = actually executed required tests / declared required tests;
- outcome attainment = each observed indicator against its own approved target and unit;
- schedule variance = actual versus approved dates, only when both exist;
- risk posture = exposure by severity/likelihood/impact with uncertainty.

Never add different dimensions into one percentage. A weighted aggregate is optional and requires documented scale normalization, rationale, approved weights, O12 validity review and sensitivity analysis. Missing values remain missing.

## Adaptive decisions

A material change produces a new revision and decision record. Supported actions include continue, resequence, rebaseline, split, merge, defer, pilot, rollback, stop and close. Every proposal needs a trigger, evidence, counterevidence, alternatives, impact analysis, risk, decision owner, approvals and verification/rollback path.

## Failure modes and controls

| Failure mode | Required control |
|---|---|
| Roadmap is a wish list, not a dependency-aware plan | Objective tree, phase exit criteria, dependency DAG and feasibility check |
| Progress percentage is gamed | Evidence-linked denominators; separate implementation, verification and outcome |
| A milestone is declared complete without tests | O10 actual execution record and independent verification |
| An evaluation score is self-assigned by planner | O12 owns evaluation method and disposition |
| A failed gate is averaged away | Hard gates override summaries |
| Replanning erases history | Immutable decision record and versioned roadmap snapshots |
| Unauthorized change is smuggled through a replan | O11 gate and exact approval; M00/human authority |
| Integration is represented as running when only documented | Capability readiness and actual execution evidence |

## Canonical contracts

Machine-readable contracts reside under plugin/references/schemas/rpeds/: roadmap, milestone, iteration, progress measurement, adaptation decision, risk and work item. The canonical ID prefixes align with Notion's generated IDs: ASRMAP, ASRPH, ASRMIL, ASRITR, ASRWRK, ASREVL, ASRDEC and ASRRSK.

Behavioral acceptance specifications reside in plugin/tests/rpeds-acceptance-cases.json and remain SPECIFICATION_ONLY until executed by a named harness. Schema fixtures in plugin/tests/rpeds-schema-fixtures.json are executable positive/negative contract examples. scripts/validate_rpeds_contracts.py meta-validates Draft 2020-12 schemas and checks record-reference and dependency-DAG invariants. These contract tests do not prove that RPEDS works as a host-model behavior or deployed runtime.

## Notion operating surface

The A.S.F.R.E.E Control Center has linked data sources for roadmaps, milestones, iterations, work items, evaluation/progress records, adaptation decisions, and risks/blockers. Notion is the operational tracking surface; GitHub remains normative for technical contracts, versions, commits, tests and releases. This initial setup is manually synchronized, not an automatic integration or runtime database.

## Implementation boundary

The RPEDS portable plugin contribution consists of skill instructions, reference modules, schemas, documentation and acceptance specifications. It does not implement a persistent scheduler, automatic monitoring, GitHub/Notion synchronizer, API/MCP service, autonomous worker, or new runtime database. The current local Python runtime is not modified by this RPEDS package change.

## PRE Core identity consolidation amendment — 2026-11-27

The roadmap capability historically named RPEDS is now treated as the A.S.F.R.E.E host adapter for the canonical PRE Core identity. The R0–R9 lifecycle and existing four RPEDS modules are preserved as compatibility mappings; the broader PRE skill set is the shared functional core. No duplicate roadmap state, competing release stream or second coordinator is introduced.

M00 remains the only case-level coordinator. The A.S.F.R.E.E host adapter runs AFSA before invoking shared PRE behavior and preserves O11/O12/O10/O09/O07/O08 authority boundaries. A core upgrade can be applied directly only when version, digest, contract, SOP compatibility and required host checks pass. Otherwise the adapter records an approved adaptation, holds for authority or quarantines the change.

This source amendment does not prove that a live webhook, persistent release registry or cross-host updater is deployed.

## PRE–RPEDS shared DNA merger amendment — 2026-11-27

This architecture does not replace RPEDS with PRE or delete RPEDS. PRE Standalone and RPEDS are two first-class manifestations of one jointly evolved roadmap competency. PRE continues to operate independently outside A.S.F.R.E.E. RPEDS remains the native A.S.F.R.E.E roadmap workstream and retains its identity, four original modules, local procedures, references and M00/O01–O12 integration.

Their shared DNA is the roadmap kernel: R0–R9 semantics, roadmap object model, objective/phase/milestone/work-item relations, dependency graph, multi-dimensional progress, evidence/gate contracts, adaptation semantics, process audit, assurance/closure, capability learning and release compatibility. Host-specific extensions remain separate. Validated, sanitized improvements from either manifestation can become shared DNA; private case records, credentials, host-only SOP and authority do not.

The A.S.F.R.E.E profile uses AFSA before applying a kernel update. The four RPEDS modules map to shared capabilities but are not erased. M00 remains sole case-level coordinator; O11 security/authorization/privacy, O12 independent evaluation, O10 verification and O09 runtime retain their own authority. Automatic kernel adoption requires authenticated release, compatibility, policy disposition, host tests, read-back and receipt; otherwise open a gated PR or hold/quarantine.
