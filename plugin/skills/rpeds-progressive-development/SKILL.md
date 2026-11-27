---
name: rpeds-progressive-development
description: Use when a system, product, plugin, repository, capability, or program needs a phased development roadmap with milestones, iterations, evidence-based progress evaluation, stage gates, or adaptive replanning.
---

# RPEDS — Roadmap Progressive Evaluation & Development System

## Mission and architectural position

RPEDS manages the development lifecycle of a roadmap: objective decomposition, progressive delivery, evidence-backed evaluation, adaptive replanning, and closure. It is a lifecycle control plane governed by M00, not a second case-level orchestrator, not an O13 specialist, and not a runtime scheduler by implication.

A.S.F.R.E.E authority boundaries remain unchanged:
- **M00:** case identity, scope, authority, specialist routing, arbitration, final synthesis, and case disposition.
- **O11:** authorization, security, privacy, consequential-action approval, and governance.
- **O12:** evaluation purpose, criteria, measurement validity, evidence interpretation, judgment, impact, and meta-evaluation.
- **O10:** actual test design/execution records and independent verification.
- **O07/O08:** accepted remediation and reconstruction/change design.
- **O09:** supported integration/runtime execution and execution receipts.

RPEDS may schedule and coordinate those responsibilities, but may not absorb, override, or counterfeit them.

## Trigger and non-trigger

Activate RPEDS when a request materially involves:
- creating or governing a multi-phase development roadmap;
- translating strategy into phases, milestones, work items, and dependencies;
- progressive delivery across iterations or versions;
- longitudinal progress monitoring;
- milestone/phase readiness and exit criteria;
- roadmap adaptation after verified evaluation, drift, blockers, changed constraints, or new evidence.

Do not activate merely to create a short checklist, a one-off fix, or a single evaluation record. Do not invent work, owners, time estimates, dates, baselines, resource capacity, progress, or approval.

## Four bounded capability modules

1. **Roadmap Architecture Planner:** strategy, objective hierarchy, roadmap decomposition, baselines, dependencies, phase and milestone design.
2. **Progressive Development Manager:** iterations, work-item orchestration, scope commitment, delivery states, milestone tracking.
3. **Continuous Evaluation Engine:** evaluation checkpoints, measurement registry, progress dimensions, evidence, gates, and handoff to O12/O10.
4. **Adaptive Roadmap Optimization Engine:** drift detection, reprioritization, rebaseline, controlled replanning, decision history, and closure.

These are bounded procedures within RPEDS. They are not separate case coordinators or autonomous agents unless the host explicitly exposes and invokes them. Detailed procedures live under the RPEDS reference directory.

## RPEDS lifecycle

Use the following lifecycle proportionately. R stages are roadmap-management states; they do not replace O12's E0–E7 evaluation lifecycle.

| Stage | Name | Required outcome |
|---|---|---|
| R0 | INTAKE | Intent, target, owner/authority, scope, non-goals, constraints, decision need |
| R1 | STRATEGY & BASELINE | Objective hierarchy, target state, observed baseline, provenance, constraints |
| R2 | ROADMAP DESIGN | Phases, milestones, work items, dependencies, resources, exit criteria, risk assumptions |
| R3 | APPROVAL & BASELINE FREEZE | Roadmap version, decision owner, approved scope, approval evidence, change boundary |
| R4 | ITERATION EXECUTION | Small bounded commitments, actual work states, change/evidence links |
| R5 | FORMATIVE CHECK | Drift, blockers, emerging risks, invalid assumptions, scope and evidence health |
| R6 | MILESTONE ACCEPTANCE | Exit criteria, actual tests, independent verification, O12 disposition, gate decision |
| R7 | OUTCOME & IMPACT | Intended outcome, operational/human impact, benefits, harms, residual risk |
| R8 | ADAPTATION | Continue, resequence, rebaseline, split, merge, defer, pilot, rollback, stop, or close |
| R9 | CLOSURE & LEARNING | Final state, delivered evidence, unresolved risks, lessons, next owner/handoff |

A roadmap may loop from R5/R6/R7 to R8 and back to R2/R4. Do not force every small task through every stage.

## Mandatory records and traceability

For a material roadmap, maintain:
- Roadmap: stable ID, objective, scope/non-goals, target/system, baseline/version/ref, target state, owner/decision authority, phases, dependency model, progress policy, risk tolerance, source provenance, revision history.
- Phase: sequence, objective, entry/exit criteria, dependencies, target window only where approved, milestones, gate result, evidence.
- Milestone: stable ID, acceptance criteria, dependency references, owner if assigned, target date if committed, gate state, evidence and decision.
- Iteration: objective, baseline, committed scope, work items, exit criteria, start/end only when known, actual outcome, retrospective.
- Progress measurement: indicator definition, method, unit/rubric, baseline, target, observed value, evidence, uncertainty, confidence, environment, version, timestamp.
- Adaptation decision: trigger, evidence, alternatives, selected action, rationale, owner, required approval, implementation status, impact, residual risk, superseded revision.
- Risk/blocker: category, severity, likelihood where justified, impact, trigger, treatment, owner if assigned, status, review/evidence.

Use the JSON Schemas under the RPEDS schemas directory. Keep identifiers stable and link records rather than duplicating mutable facts.

## Progress measurement policy

Progress is multi-dimensional. Never collapse delivery, verification, quality, outcome attainment, and impact into an unqualified single percentage.

Minimum separate measures:
- Delivery completion: verified in-scope work items / total in-scope work items.
- Milestone acceptance: accepted milestones / total approved milestones.
- Verification coverage: required tests actually executed with recorded outcomes / declared required tests.
- Outcome attainment: measured indicator compared with its approved target, using that indicator's defined unit and direction.
- Risk posture: open/accepted/resolved risks with severity and uncertainty visible.
- Schedule variance: only when baseline dates, approved changes, and actual dates exist.

Default progress method is evidence-count based. Weighted progress is permitted only when weights are justified, approved by the decision owner, comparable, normalized, recorded, and validated by O12. Hard gates override averages. Unassessed, stale, blocked, NOT_RUN, UNVERIFIABLE, or missing evidence is never silently counted as PASS or completion.

A roadmap-level summary must show measurement date, denominator, scope, excluded items, status definitions, evidence coverage, and uncertainty. Do not report a fabricated percentage when the denominator or state is unknown.

## Gate and decision rules

A milestone can be accepted only when:
1. entry/exit and acceptance criteria were declared before evaluation;
2. scope and baseline are clear;
3. required work items have a recorded implementation state;
4. required tests have actual results from O10 or a declared authorized test executor;
5. O12 has evaluated the relevant evidence against the charter;
6. no unresolved hard-gate failure/P0/P1 blocker remains, unless applicable policy expressly allows a documented hold or risk acceptance by the authorized owner;
7. required approvals and evidence locators exist.

Valid gate dispositions: NOT_RUN, NOT_ASSESSED, PASS, PASS_WITH_CAVEATS, HOLD, FAIL, BLOCKED, NOT_APPLICABLE. NOT_RUN, NOT_ASSESSED, HOLD, FAIL, and BLOCKED are not PASS.

M00 and the authorized human decision owner retain final authority. RPEDS produces recommendations, not self-approval.

## Adaptive roadmap rules

Replan only from a material trigger:
- failed/held milestone or evaluation gate;
- evidence-backed scope, baseline, dependency, or assumption drift;
- newly observed security, legal, technical, operational, cost, or human-impact risk;
- dependency failure or resource/capacity constraint;
- validated opportunity with documented trade-off;
- measured outcome materially diverging from an approved target.

For each adaptation:
1. preserve the prior roadmap revision;
2. record the trigger and evidence;
3. compare DO_NOTHING, CONTINUE, RESEQUENCE, REBASELINE, SPLIT, MERGE, DEFER, PILOT, ROLLBACK, STOP, and CLOSE as applicable;
4. show scope, dependency, date, resource, compatibility, risk, and stakeholder impact;
5. identify decision owner and required authority/approval;
6. create a new roadmap revision or explicit delta; never overwrite history;
7. validate affected milestones and indicators with O10/O12 as relevant.

Replanning must not bypass O11, convert a failed gate into a pass, or erase inconvenient evidence.

## Handoff contract

Return to M00:
- roadmap ID/revision and target;
- lifecycle stage and current state;
- baseline and evidence provenance;
- phase/milestone/iteration/work-item references;
- separate progress measures and their denominators;
- gate dispositions, actual tests, and O12 evaluation references;
- blockers/risks/assumptions and counterevidence;
- adaptation options and recommended decision;
- approval/authority requirements;
- next owner, next gate, and explicit unknowns.

Use PROCEDURE_APPLIED if the host does not expose a distinct RPEDS invocation; never claim an autonomous service, agent, scheduler, database engine, or background monitor is running without evidence.

## Stop conditions

Stop or hold when target/authority is unclear, baseline is materially changed without authorization, critical evidence is missing or contradicted, a dependency cycle is unresolved, a P0/P1 risk is uncontrolled, required verification failed/not run, the decision owner is absent, or a requested mutation lacks exact approval.

The portable RPEDS package is a skills-and-contract specification. A persistent service, automatic GitHub/Notion synchronization, scheduled monitoring, runtime database, and autonomous replanning engine are not provided by this package.


## Trigger precedence and conditional specialist routes

RPEDS is selected only for lifecycle governance across multiple phases, milestones, iterations or roadmap revisions. A one-off checklist, standalone evaluation, one-time architecture review, single bug fix or direct implementation request without longitudinal state does not activate RPEDS.

### Route selection

M00 decides each route separately. Use the route only when its distinct output can change a preservation constraint, risk posture, candidate ranking, diagnosis, acceptance gate or next action.

| Specialist | Select when | Output required by RPEDS |
|---|---|---|
| O03 | A roadmap/revision change may destroy or alter evidenced capability, stakeholder value, differentiator, reusable behavior or compatibility. | Verified-vs-potential value register; hard/soft preservation invariants; regression/acceptance conditions; enhancement opportunities. |
| O04 | A credible adverse scenario, security/privacy exposure, dependency/failure mode, misuse path or material side effect must influence roadmap design/approval. | Scenario-based risk register; epistemic status; severity/likelihood separated; controls, residual risk and safe verification route. |
| O05 | Two or more feasible roadmap paths, versions or adaptation alternatives must be chosen on normalized criteria. | Comparable candidate set; criteria and hard gates; trade-offs/deltas; missing data; sensitivity and conditional recommendation. |
| O06 | An observed/reported mismatch, failed behavior, regression or unexplained variance must be diagnosed before planning a correction. | Valid test oracle; expected/observed record; reproduction state; competing causal hypotheses; falsification path and root-cause confidence. |

### Decision and sequencing rules

1. Establish current source/version/baseline through O01/O02 when needed.
2. Select O03 only when a preservation/value question exists; O04 only when an adverse-risk question exists. They may run in parallel on one authorized baseline only when their outputs are independent.
3. Select O06 only for an observed anomaly or bounded suspicion requiring diagnosis. An unconfirmed suspicion remains unconfirmed; a hypothesis is not a defect.
4. Select O05 only after real candidates and the decision question are defined. Feed it O03 preservation constraints and O04 risk constraints when relevant. If candidates cannot be normalized, report non-comparability.
5. Route material threats/security decisions to O11; actual test execution/independent verification to O10; supported runtime evidence to O09; evaluation criteria, measurement validity and judgment to O12; accepted engineering changes to O07/O08.
6. No route may self-approve, mutate a target, accept a risk, mark a milestone PASS or bypass M00/human authority.

### Routing observability and stop conditions

For each O03–O06 record separately:
- `route_decision`: `REQUIRED`, `OPTIONAL`, `NOT_REQUIRED` or `UNRESOLVED`, with rationale.
- `execution_state`: `INVOKED`, `PROCEDURE_APPLIED`, `BEHAVIOR_ONLY`, `NOT_RUN`, `BLOCKED` or `UNAVAILABLE`.
- `handoff_ref`, evidence refs, limitations, next owner and acceptance criterion.

Never claim `INVOKED` without host evidence. A materially triggered route lacking authority, source, data or environment remains `UNRESOLVED`/`BLOCKED`, not silently skipped. Standalone evaluation routes to O12; one-off defect/remediation routes to O06 then O07/O08 as appropriate; a simple checklist has no RPEDS lifecycle overhead. M00 arbitrates overlap, prevents duplicate deliverables and owns final synthesis.

## PRE–RPEDS shared DNA integration contract

RPEDS remains an A.S.F.R.E.E-native roadmap workstream, not an alias-only shim. Its original four modules and A.S.F.R.E.E-specific procedures remain first-class: Roadmap Architecture Planner; Progressive Development Manager; Continuous Evaluation Engine; Adaptive Roadmap Optimizer. They map to the jointly evolved PRE–RPEDS shared DNA kernel; they are not deleted or renamed away.

The shared DNA consists of R0–R9 semantics, roadmap object model, dependency graph, progress/evidence measures, gate semantics, adaptation decisions, process audit, assurance/closure, capability learning and release compatibility. PRE Standalone remains independently usable and may contribute reusable improvements to the common kernel. RPEDS may contribute validated A.S.F.R.E.E patterns to the same kernel. Host-only authority, case evidence, private SOP and security policy never become shared DNA.

M00 remains the sole case coordinator. O11 retains authorization/security/privacy, O12 independent evaluation, O10 test/verification and O09 runtime execution. RPEDS coordinates roadmap work; it does not assume those roles. Route shared-core operations through the host adapter exactly once; preserve RPEDS-native functions in the A.S.F.R.E.E profile.

Use AFSA to classify a proposed core update as DIRECT_COMPATIBLE, ADAPTED_COMPATIBLE, HELD_FOR_AUTHORITY or QUARANTINED_OR_REJECTED. Preserve RPEDS-specific behavior when a PRE update does not subsume it. When one host learns a potentially reusable method, propose it through capability federation with provenance, sanitization, tests and adoption receipt.


## Shared PRE–RPEDS DNA and mandatory AFSA

PRE Standalone and RPEDS are peer manifestations of the shared `pre-rpeds-shared-roadmap-dna` kernel. RPEDS retains its native A.S.F.R.E.E identity and four modules; it is not replaced by PRE or reduced to a compatibility alias. Shared contracts and validated methods may evolve in either direction without erasing host extensions.

Before a shared release, capability or learned method is applied to A.S.F.R.E.E, apply `rpeds-adaptive-functional-situational-adapter`. It verifies source/release/digest, host SOP/policy, M00 decision rights, O11 security/privacy, data flow, tools, tests, audit sink and rollback; then returns DIRECT_COMPATIBLE, ADAPTED_COMPATIBLE, HELD_FOR_AUTHORITY or QUARANTINED_OR_REJECTED. Unknown is not compatible.

Only an explicitly non-breaking, pure SHARED_DNA update may be eligible for automatic host testing under a verified policy profile and explicit host opt-in. RPEDS-native extensions, HOST_ADAPTATION, HOST_SPECIFIC information or mixed/unknown classes require host review/hold. M00 remains case coordinator; O11/O12/O10/O09 keep their declared authority. No adapter may silently rewrite SOP or self-approve.
