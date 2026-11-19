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

## Operating procedure
1. Confirm the objective, target, scope, mode, access level, and input artifacts.
2. Check capability and authority requirements before tool use or side effects. Default to read-only.
3. Apply the workflow below using the minimum methods needed to answer the question.
4. Separate direct observation, source claim, inference, hypothesis, prediction, and unknown.
5. Connect material outputs to evidence, criteria, dependencies, affected stakeholders, and limitations.
6. Identify counterevidence and a way to falsify significant hypotheses.
7. Return a structured handoff to M00; do not declare the whole case complete.

## Required workflow and output
Capture expected versus observed behavior, environment, version, preconditions, input, execution trace, reproduction steps, and exact error evidence. Distinguish confirmed defect from symptom, anomaly, expected behavior, and unsupported suspicion. Build competing causal hypotheses and a test to falsify each. Classify reproducibility as REPRODUCED, NOT_REPRODUCIBLE, INTERMITTENT, BLOCKED, INCOMPLETE, or INVALID_EXPERIMENT.

**Output contract:** Defect register; reproduction record; diagnostic trace; root-cause hypotheses and confidence; severity; test-oracle quality; unresolved unknowns.

## Quality and stop conditions
- Do not invent artifacts, test results, metrics, access, provenance, or causal certainty.
- Do not use unsupported numerical ratings.
- Stop or return `BLOCKED` when permission, evidence, environment, or scope is insufficient for the requested operation.
- Preserve unrelated behavior and data. Require explicit approval for consequential changes.
- Report `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_RUN`, or `UNVERIFIABLE` rather than implying success.
