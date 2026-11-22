# RPEDS Module 04 — Adaptive Roadmap Optimization Engine

## Responsibility

Recommend controlled roadmap adjustments when evidence shows the current plan is no longer valid, feasible, safe or valuable. This module cannot approve its own proposal, alter authoritative baselines silently, or override O11/O12/M00.

## Trigger catalogue

- milestone/test/evaluation gate failure or hold;
- dependency, schedule or capacity drift;
- changed requirements, external constraints or technical assumptions;
- newly discovered defect, risk, security exposure or human-impact concern;
- measured outcome divergence;
- validated opportunity whose trade-offs justify reprioritization.

A trigger must be linked to evidence or explicitly labelled as an assumption/hypothesis.

## Decision workflow

1. Preserve the current roadmap snapshot and plan.
2. State the trigger, evidence, counterevidence and confidence.
3. Identify impacted objectives, phases, milestones, work items, dependencies, dates, resource assumptions, integrations, stakeholders and risks.
4. Compare relevant alternatives: CONTINUE, RESEQUENCE, REBASELINE, SPLIT, MERGE, DEFER, PILOT, ROLLBACK, STOP and CLOSE.
5. Evaluate intended benefits, opportunity cost, compatibility, security, reversibility, migration, residual risk and downstream effects.
6. Obtain O12 evaluation for material trade-offs and O11 approval for governed or consequential actions.
7. Route the final decision to M00 and the authorized human decision owner.
8. If approved, create a new roadmap revision/delta and update affected gates. Preserve superseded data and decisions.
9. Define a review trigger and rollback/recovery route.

## Output

Adaptation proposal, alternatives matrix, impact/dependency analysis, required approvals, immutable decision record, revised roadmap delta, verification plan, residual risk, and explicit defer/stop criteria.
