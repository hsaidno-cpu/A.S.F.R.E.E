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
| Evaluation charter, criteria, measurement validity, judgment, impact and meta-evaluation | O12 |
| Test design/execution, actual outcome and independent verification | O10 |
| Corrective/preventive change design | O07 |
| Reconstruction, migration and architecture adaptation | O08 |
| Supported tool/runtime/API/MCP execution | O09 |
| Authorization, privacy, security, consequential approvals | O11 |
| Roadmap objective tree, phase/milestone lifecycle, iterations, progress ledger, replan proposals | RPEDS |

RPEDS orchestrates when these responsibilities are needed; it does not reimplement them. It receives their structured outputs and returns roadmap decisions to M00.

## Four internal capability modules

1. **Roadmap Architecture Planner** — objective hierarchy, roadmap revisions, phases, milestone design, dependency DAG, feasibility and baseline.
2. **Progressive Development Manager** — iterative commitments, work-item states, milestone sequencing, scope drift and delivery tracking.
3. **Continuous Evaluation Engine** — evaluation checkpoint schedule, indicator registry, evidence and gate visibility; O12 decides the evaluation.
4. **Adaptive Roadmap Optimizer** — trigger detection, alternative comparison, dependency impact, rebaseline proposal and decision history.

The modules are bounded procedures and references, not claims that separate autonomous agents are deployed.

## Lifecycle model

R0 INTAKE → R1 STRATEGY & BASELINE → R2 ROADMAP DESIGN → R3 APPROVAL & BASELINE FREEZE → R4 ITERATION EXECUTION → R5 FORMATIVE CHECK → R6 MILESTONE ACCEPTANCE → R7 OUTCOME & IMPACT → R8 ADAPTATION → R9 CLOSURE.

The lifecycle loops when evidence requires re-sequencing or replanning. O12's E0–E7 evaluation lifecycle remains distinct and is mapped onto the R stages rather than replaced.

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

Machine-readable contracts reside under plugin/references/schemas/rpeds/: roadmap, milestone, iteration, progress measurement, adaptation decision and risk.

Acceptance specifications reside in plugin/tests/rpeds-acceptance-cases.json. They remain SPECIFICATION_ONLY until executed by a named test harness with evidence.

## Notion operating surface

The A.S.F.R.E.E Control Center has linked data sources for roadmaps, milestones, iterations, work items, evaluation/progress records, adaptation decisions, and risks/blockers. Notion is the operational tracking surface; GitHub remains normative for technical contracts, versions, commits, tests and releases. This initial setup is manually synchronized, not an automatic integration or runtime database.

## Implementation boundary

The RPEDS portable plugin contribution consists of skill instructions, reference modules, schemas, documentation and acceptance specifications. It does not implement a persistent scheduler, automatic monitoring, GitHub/Notion synchronizer, API/MCP service, autonomous worker, or new runtime database. The current local Python runtime is not modified by this RPEDS package change.
