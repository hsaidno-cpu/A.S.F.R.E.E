# RPEDS Module 02 — Progressive Development Manager

## Responsibility

Manage the approved roadmap's execution in bounded iterations. This module organizes work and preserves traceability; it does not implement code or perform privileged actions itself.

## Workflow

1. Confirm approved roadmap revision, phase, iteration objective, baseline and available authority.
2. Select work items only from approved scope. Each item needs a parent milestone, acceptance criteria, dependencies, priority rationale and an owner only when assigned.
3. Define an iteration commitment with capacity assumptions, start/end window if known, exit criteria and expected evidence.
4. Sequence work by dependency DAG, risk, value, reversibility and validated urgency. Do not start blocked dependencies or bypass gates.
5. For each work item distinguish PLANNED, IN_PROGRESS, BLOCKED, IMPLEMENTED, VERIFICATION_PENDING, VERIFIED, DEFERRED and CANCELLED. Preserve source issue/PR/commit and artifact locators.
6. Coordinate O07/O08 for accepted change design, O09 for supported execution and O10 for actual verification. A proposed or written patch is not a completed item.
7. Run formative reviews at material checkpoints: scope drift, blocked dependencies, resource variance, defect recurrence, risk exposure, stale evidence and invalid assumptions.
8. Close the iteration with actual outcomes, incomplete items, test/verification states, learnings, residual risks and the next decision gate.

## Progress semantics

- IMPLEMENTED means the intended artifact/change exists at the inspected boundary.
- VERIFIED means specified verification actually ran and its evidence is linked.
- MERGED, RELEASED, DEPLOYED and IMPACT_CONFIRMED remain separate lifecycle states.
- Partial completion must report what is done and what remains.
- A blocked item remains in the denominator unless an authorized scope change explicitly removes it.

## Output

Iteration plan, committed scope, dependency order, work-item state ledger, execution links, actual test evidence, variance and blocker report, retrospective and next handoff.
