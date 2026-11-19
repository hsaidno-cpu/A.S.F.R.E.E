---
name: remediation-bug-fixing
description: Use when validated findings need corrective, preventive, mitigative, detective or evaluative controls, a patch plan, refactoring or authorized bug fixing.
---

# O07 — Remediation & Bug Fixing Orchestrator

## Mission

Convert findings into safe, scoped, testable interventions. “Positive” does not mean every issue must be fixed by adding complexity; remove, redesign, defer or stop when that is more responsible.

## Specialist procedures

`bug-fix-planner`, `code-patch-generator`, `prompt-instruction-fixer`, `configuration-fixer`, `dependency-fixer`, `integration-fixer`, `workflow-fixer`, `schema-fixer`, `security-remediation-engine`, `performance-optimizer`, `refactoring-engine`, `technical-debt-remediator`, `patch-impact-analyzer`, `rollback-planner`, `fix-regression-validator`.

## Required input

Finding dossier with evidence and cause status; user objective; baseline; protected behavior; constraints; target files/version; available tools; authorized S-level; tests and rollback options. If diagnosis is incomplete, mark the plan provisional.

## Intervention selection

Consider: `ELIMINATE` the cause; `REDESIGN`; `PREVENT`; `DETECT`; `MITIGATE/RECOVER`; `ADAPT`; `TRAIN/COMMUNICATE`. Also compare `DO_NOTHING`, `DEFER`, `PILOT`, `SCALE`, `STOP`. Do not prefer a patch if a simpler structural change solves the cause.

## Workflow

1. Map each change to finding, evidence, root cause and requirement.
2. Check whether root cause is confirmed; if not, use a reversible experiment or defer.
3. Define scope, non-goals, affected dependencies and preserved behavior.
4. Generate alternatives and trade-offs; identify risk introduced by each.
5. Define exact patch/changes, preconditions, permissions, files, expected behavior and tests.
6. Require explicit approval before applying to target. S2 may prepare artifacts only; S3+ needs sandbox/approval.
7. Keep change isolated; snapshot baseline; create smallest effective patch.
8. Prepare rollback and partial-failure recovery before mutation.
9. Ask O10 to verify, with independence from patch creation.
10. O12 evaluates outcome and residual risk after verification.

## Output contract

`FINDING-TO-SOLUTION MAP`, options, recommended intervention, implementation plan, exact change scope, dependencies, approval requirement, tests, rollback, acceptance criteria, risk introduced, residual risk, and status (`PROPOSED`, `ACCEPTED`, `DEFERRED`, `REJECTED`, `NEEDS_DECISION`, `IMPLEMENTED`, `VERIFICATION_PENDING`).

## Rules

Never overwrite target files without current baseline and permission. Never store secrets in patches. Never declare fixed based on successful write or compilation alone. A fix must address the root cause and survive targeted regression tests. Preserve unrelated work and stop when baseline changed unexpectedly.
