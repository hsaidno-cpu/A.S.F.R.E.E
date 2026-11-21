# Lifecycle, Gates, Recovery & Release States

## Case lifecycle

`INTAKE → SCOPE/AUTHORIZATION → CAPABILITY READINESS → BASELINE → FORENSIC PLAN → INSPECTION/DECOMPOSITION → POSITIVE/NEGATIVE/COMPARATIVE ANALYSIS → DIAGNOSIS → EVALUATION → SOLUTION OPTIONS → APPROVAL → CONTROLLED ENGINEERING → TEST/INDEPENDENT VERIFICATION → POST-CHANGE/IMPACT EVALUATION → FINAL AUTHENTICATION → HANDOFF/CLOSE`.

Tailor the lifecycle. Conceptual and read-only requests must not be forced through engineering or deployment stages.

## Evaluation checkpoints

`E0` Charter; `E1` Baseline/criteria; `E2` Evidence plan; `E3` Formative; `E4` Summative; `E5` Post-change; `E6` Outcome/impact; `E7` Meta-evaluation. These are process checkpoints, not claims of autonomous modules.

## Severity

- `P0_CRITICAL`: serious safety/legal/security/privacy, data-loss, unauthorized side effect, or fundamental integrity failure. Stop and escalate.
- `P1_HIGH`: core behavior or critical control cannot be trusted. Hold.
- `P2_MEDIUM`: material quality/operational weakness with a safe fallback. Continue only with caveats and bounded scope.
- `P3_LOW`: limited clarity or polish issue. Record proportionately.

Severity is separate from likelihood and confidence.

## Exception taxonomy

`MISSING`, `AMBIGUOUS`, `CONFLICT`, `INVALID`, `OUT_OF_RANGE`, `STALE`, `ADVERSARIAL`, `CAPABILITY_UNAVAILABLE`, `PERMISSION_DENIED`, `EXECUTION_FAILURE`, `PARTIAL`, `RESOURCE_LIMIT`, `UNEXPECTED_SIDE_EFFECT`, `BASELINE_CHANGED`.

For each exception, record trigger, affected IDs, severity, detection, response, retry condition/limit, fallback, rollback precondition, approval, verification, and residual risk.

## Recovery policy

Preserve original evidence. Classify before acting. Choose `REJECT_INPUT`, `CLARIFY`, `RETRY`, `FALLBACK`, `PARTIAL_RESULT`, `ROLLBACK`, `ESCALATE`, or `STOP`. Retry only transient failures with finite limits and idempotency where relevant. Never retry to bypass permission denial, missing authorization/data, or safety restrictions. Re-run only affected tasks and dependencies. Report partial completion and exact system state.

## Fail-closed dispositions

- `PASS`: applicable hard gates and mandatory checks pass with adequate evidence; no unresolved P0/P1.
- `PASS_WITH_CAVEATS`: no critical blocker; bounded limitations are disclosed and accepted.
- `HOLD`: critical evidence, permission, approval, coverage, or test is unresolved.
- `FAIL`: integrity, authority, safety, or core contract is violated.
- `BLOCKED`: essential capability or permission is unavailable.

Unknown, incomplete, blocked, not-run, unverified, and unobserved must never be mapped to PASS.

## Separate lifecycle statuses

Case: `OPEN`, `IN_PROGRESS`, `HOLD`, `BLOCKED`, `CLOSED`.
Recommendation: `PROPOSED`, `ACCEPTED`, `DEFERRED`, `REJECTED`, `NEEDS_DECISION`.
Implementation: `NOT_STARTED`, `IMPLEMENTING`, `IMPLEMENTED`, `VERIFICATION_PENDING`.
Verification: `NOT_RUN`, `PASS`, `FAIL`, `BLOCKED`, `UNVERIFIABLE`, `NOT_APPLICABLE`.
Release: `NOT_RELEASED`, `RELEASE_APPROVED`, `PR_OPEN`, `MERGED`, `RELEASED`, `DEPLOYED`, `READ_BACK_CONFIRMED`.

Never infer later states from earlier states.
## P1.1 security release gates

Apply four non-aggregatable hard gates before staging/production disposition:
1. Identity & SCIVE: verified IdP/MFA assurance, cross-process signed delegation, replay/revocation tests, and policy coverage for every SCIVE transition.
2. Encryption & key lifecycle: managed KMS/HSM, live metadata/WAL/temp/log/audit/backup encryption, key rotation, revocation and restore evidence.
3. Execution & tenant isolation: rootless OCI plus gVisor/Kata or approved equivalent, host-enforced quotas, bounded streaming output, hostile-workload and cross-tenant tests.
4. Trust & oversight: independent external WORM anchor and read-back, infrastructure tenant isolation, concurrency/TOCTOU tests, independent signed human review.

A required control that is absent or untested is NOT_RUN/BLOCKED/HOLD, not PASS. A green CI result for local tests cannot substitute for live provider integration or human review. See [P1.1 Security-to-Production Readiness Contract](p1.1-security-production-readiness.md).
