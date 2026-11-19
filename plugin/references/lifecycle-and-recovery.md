# Lifecycle, Gates, Recovery & Release States

## Case lifecycle

INTAKE → SCOPE/AUTHORIZATION → CAPABILITY READINESS → BASELINE → FORENSIC PLAN → INSPECTION/DECOMPOSITION → POSITIVE/NEGATIVE/COMPARATIVE ANALYSIS → DIAGNOSIS → EVALUATION → SOLUTION OPTIONS → APPROVAL → CONTROLLED ENGINEERING → TEST/INDEPENDENT VERIFICATION → POST-CHANGE/IMPACT EVALUATION → FINAL AUTHENTICATION → HANDOFF/CLOSE.

Tailor the stages. Read-only or conceptual work should not be forced through engineering/deployment steps.

## Evaluation checkpoints

E0 charter; E1 baseline/criteria; E2 evidence plan; E3 formative; E4 summative; E5 post-change; E6 outcome/impact; E7 meta-evaluation.

## Severity

- P0 Critical: safety/legal/security, data loss, unauthorized side effect, or fundamental integrity failure. Stop and escalate.
- P1 High: core result cannot be trusted or critical function/control fails. Hold.
- P2 Medium: meaningful quality/operational degradation with safe fallback. Continue only with caveats or bounded scope.
- P3 Low: cosmetic or non-material issue. Record/repair proportionately.

Severity is not likelihood or confidence.

## Exception taxonomy

`MISSING`, `AMBIGUOUS`, `CONFLICT`, `INVALID`, `OUT_OF_RANGE`, `STALE`, `ADVERSARIAL`, `CAPABILITY_UNAVAILABLE`, `PERMISSION_DENIED`, `EXECUTION_FAILURE`, `PARTIAL`, `RESOURCE_LIMIT`, `UNEXPECTED_SIDE_EFFECT`, `BASELINE_CHANGED`.

For each exception record trigger, affected IDs, severity, detection, response, retry condition/limit, fallback, rollback precondition, approval, verification and residual risk.

## Recovery policy

Preserve the original evidence. Classify before acting. Choose `REJECT_INPUT`, `CLARIFY`, `RETRY`, `FALLBACK`, `PARTIAL_RESULT`, `ROLLBACK`, `ESCALATE` or `STOP`. Retry only transient failures with a finite cap and idempotency where needed. Never retry to bypass denied permissions, missing data, or a safety restriction. Re-run only affected tasks and dependencies. Report partial completion explicitly.

## Quality gate / fail-closed

`PASS` only when all applicable hard gates and required checks pass with adequate evidence and no unresolved P0/P1. `PASS_WITH_CAVEATS` only for disclosed noncritical limitations. `HOLD` for missing critical evidence, permissions, coverage, approvals, tests or unresolved blockers. `FAIL` for integrity breach, falsified evidence, unauthorized action, or broken core contract.

## Separate lifecycle statuses

`DESIGN_DRAFT`, `STATIC_REVIEWED`, `READY_FOR_HANDOFF`, `READY_WITH_LIMITATIONS`, `BLOCKED`, `HOLD`, `IMPLEMENTED`, `VERIFICATION_PENDING`, `VERIFIED`, `PR_OPEN`, `MERGED`, `RELEASED`, `TESTED_ON_TARGET`.

Do not infer one status from another. Package creation is not runtime verification. File write is not test success. PR open is not merged. Merged is not released. `NOT_RUN`, `UNKNOWN`, `BLOCKED`, `UNVERIFIABLE` and `PARTIAL` are never PASS.
