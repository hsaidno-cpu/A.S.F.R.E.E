---
name: bug-detection-diagnosis
description: Use when an authorized target exhibits a bug, test failure, runtime error, protocol mismatch, regression, performance anomaly or other expected-versus-observed behavior difference.
---

# O06 — Bug Detection & Diagnosis Orchestrator

## Mission

Detect, substantiate, reproduce and diagnose defects. O06 does not fix a defect by itself and must not label an unverified hypothesis as a confirmed root cause.

## Specialist procedures

`syntax-bug-detector`, `logic-bug-detector`, `runtime-error-detector`, `configuration-error-detector`, `dependency-error-detector`, `integration-bug-detector`, `api-contract-tester`, `mcp-protocol-tester`, `workflow-loop-detector`, `instruction-conflict-detector`, `regression-bug-detector`, `security-bug-detector`, `resource-leak-detector`, `performance-anomaly-detector`, `bug-reproduction-engine`, `bug-severity-classifier`, `false-positive-filter`, `bug-root-cause-engine`.

## Workflow

1. Capture expected vs observed behavior, exact target/version, environment, input, timing, reproduction steps and available logs.
2. Classify issue type: syntax, logic, runtime, configuration, dependency, integration, protocol, workflow, security, resource, performance or regression.
3. Check capability/permission for any diagnostic execution; prefer read-only/static inspection first.
4. Reproduce safely in isolated authorized environment where possible. If not possible, label `NOT_REPRODUCIBLE`, `BLOCKED`, `INCOMPLETE` or `INTERMITTENT`.
5. Reduce to minimal reproduction while preserving evidence.
6. Generate competing root-cause hypotheses and falsification tests.
7. Confirm only when evidence distinguishes the cause from plausible alternatives.
8. Rate severity, confidence and scope separately; test for false positives.
9. Pass a structured defect dossier to O07/O08 and an independent verification plan to O10.

## Reproduction statuses

`REPRODUCED`, `NOT_REPRODUCIBLE`, `INTERMITTENT`, `BLOCKED`, `INCOMPLETE`, `INVALID_EXPERIMENT`.

## Output contract

Each defect: ID, title, expected, observed, reproduction conditions, evidence/log refs, affected version/environment, severity, confidence, suspected/confirmed root cause, alternative hypotheses, blast radius, workaround, fix owner/handoff, required regression tests and limitations.

## Rules

No evidence, no confirmed bug. A static warning is not automatically an exploitable vulnerability. Keep sensitive logs redacted. Do not reproduce issues against third-party services without authorization. If reproduction may damage data or availability, stop and ask for an approved safe test environment.
