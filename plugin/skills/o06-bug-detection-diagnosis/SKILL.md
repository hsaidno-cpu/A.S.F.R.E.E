---
name: o06-bug-detection-diagnosis
description: Use when suspected or observed bugs, logic errors, runtime failures, configuration problems, contract violations, anomalies, or root causes must be diagnosed.
---

# Bug Detection & Diagnosis Orchestrator

## Mission
Detect and diagnose defects using reproducible observations and a falsifiable root-cause process.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`syntax-bug-detector;logic-bug-detector;runtime-error-detector;configuration-error-detector;dependency-error-detector;integration-bug-detector;api-contract-tester;mcp-protocol-tester;workflow-loop-detector;instruction-conflict-detector;regression-bug-detector;security-bug-detector;resource-leak-detector;performance-anomaly-detector;bug-reproduction-engine;bug-severity-classifier;false-positive-filter;bug-root-cause-engine`

The names above are functional capability labels, not a claim that separate software modules or agents have been deployed. Activate only relevant capabilities.

## Trigger contract

**Required trigger**
- An observed failure, regression, error, contract violation, behavior mismatch, abnormal result or unexplained variance has been reported/captured.
- The roadmap decision depends on identifying whether a defect exists, how it manifests, which component is responsible, or what evidence would confirm the cause.
- A previously passing behavior no longer meets a declared acceptance criterion.

**Limited triage trigger**
A suspicion without reproducible observation may receive bounded static/trace triage. Label it `UNCONFIRMED` or `NOT_REPRODUCIBLE`; do not report a confirmed defect or root cause.

**Do not trigger**
- For a hypothetical threat without observed malfunction (O04).
- For architectural complexity/missing capability without observed incorrect behavior (O02/O04).
- For selecting among candidate fixes (O05) or implementing a known accepted fix (O07).
- To run production experiments or change runtime state without O11 authorization and O09/O10 controls.

## Minimum inputs

Target/version/commit; expected behavior and acceptance oracle; actual behavior; inputs/preconditions; environment/configuration/dependencies; logs/traces/artifacts; frequency/timing; recent changes; and permission to reproduce. Mark missing observations.

## Operating procedure

1. **Capture anomaly:** reporter/source, time, target/version, environment, input, preconditions, expected/observed result and exact evidence locator.
2. **Validate oracle:** expected behavior must come from an authoritative requirement, contract, specification, test or accepted baseline. If ambiguous, diagnose the oracle; do not call surprising behavior a bug.
3. **Bound reproduction:** define safe preconditions and minimal reproduction. O09 performs supported authorized runtime execution; O10 owns controlled test execution. Record attempts/environment parity. Never mutate production merely to reproduce.
4. **Classify reproduction:** `REPRODUCED`, `NOT_REPRODUCIBLE`, `INTERMITTENT`, `BLOCKED`, `INCOMPLETE` or `INVALID_EXPERIMENT`. Failure to reproduce does not prove absence.
5. **Separate layers:** symptom, anomaly, defect, causal mechanism and root cause. A confirmed defect requires demonstrated violation of a valid oracle. A confirmed cause requires decisive evidence or a falsification-capable test discriminating competing causes.
6. **Build competing hypotheses:** candidate cause, predicted observations, support/counterevidence, discriminating test, expected result and confidence. Include environment, data, configuration, dependency, concurrency, timing and integration causes where plausible.
7. **Trace mechanism:** follow relevant control/data flow and dependencies. Correlation, temporal proximity or shared context is not causation. Five Whys generates hypotheses, not proof.
8. **Classify impact/route risk:** scope, frequency, affected versions/users, integrity, availability and downstream milestones; route material security/privacy/safety/operational implications to O04/O11.
9. **Define correction evidence:** smallest diagnostic conclusion, verification tests and regression boundary. Diagnosis does not authorize implementation.
10. **Hand off:** M00 receives defect dossier, hypotheses, confidence, oracle and unknowns. O07/O08 may design remediation only after accepted finding and clear authority.

## Required output contract

Defect/anomaly ID and target/version/commit; source/time/environment/locator/inspection depth; expected result and authoritative oracle; observed result; inputs/preconditions/reproduction steps/attempt count/status; symptom/anomaly/defect classification and evidence; candidate causes/predictions/support/counterevidence/falsification tests; root-cause status/confidence/unknowns; severity/impact/scope with material risk routed to O04; verification/regression tests, owner and next route.

Deliver defect register, reproduction record, diagnostic trace, competing root-cause hypotheses, oracle assessment and verification handoff.

## Route boundaries and handoff

- M00 owns routing, arbitration and final disposition.
- O10 owns test design/execution and independent verification; O09 supplies supported runtime traces inside authorization.
- O04 handles credible risk/threat; O11 authorizes security/consequential operations.
- O05 compares feasible corrective options after sufficient diagnosis.
- O07/O08 own accepted remediation/reconstruction. O06 does not edit, deploy, accept risks or close milestones.

## Quality and stop conditions

Preserve raw logs/failure evidence. Stop for invalid oracle, unsafe environment, unauthorized target or unapproved side effect. Record `NOT_REPRODUCIBLE`, `BLOCKED` or `INCOMPLETE` honestly; do not retry without a new hypothesis/bounded reason. Never confirm cause from correlation, anecdote, model-generated explanation or non-discriminating test.
