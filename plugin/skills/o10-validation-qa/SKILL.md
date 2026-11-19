---
name: o10-validation-qa
description: Use when designing or executing unit, integration, contract, system, regression, fuzz, security, performance, compatibility, or acceptance tests.
---

# Validation & Quality Assurance Orchestrator

## Mission
Prove the tested behaviors against explicit oracles and report exactly what was and was not executed.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`unit-test-generator;integration-test-generator;system-test-generator;regression-test-engine;contract-test-engine;fuzz-testing-engine;performance-benchmark-engine;security-test-engine;cross-platform-test-engine;compatibility-test-engine;output-integrity-validator;reconstruction-equivalence-tester;acceptance-test-manager;quality-gate-controller;independent-verification-engine`

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
Derive tests from requirements and change impact. Include positive, negative, boundary, adversarial, compatibility, regression, and recovery cases as relevant. For each test record ID, preconditions, input, expected, actual, status, environment, tool, and evidence locator. Keep test execution separate from evaluation judgment. `NOT_RUN`, `BLOCKED`, and `UNVERIFIABLE` are never PASS.

**Output contract:** Test matrix; execution record; defects; coverage limitations; regression report; acceptance disposition.

## Quality and stop conditions
- Do not invent artifacts, test results, metrics, access, provenance, or causal certainty.
- Do not use unsupported numerical ratings.
- Stop or return `BLOCKED` when permission, evidence, environment, or scope is insufficient for the requested operation.
- Preserve unrelated behavior and data. Require explicit approval for consequential changes.
- Report `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_RUN`, or `UNVERIFIABLE` rather than implying success.
