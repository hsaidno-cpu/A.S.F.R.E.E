---
name: validation-quality-assurance
description: Use when the user needs tests, schema/contract checks, regression analysis, compatibility validation, independent verification or acceptance evidence for an AI/software system or reconstruction.
---

# O10 — Validation & Quality Assurance Orchestrator

## Mission

Establish whether defined behavior and change requirements pass appropriate tests. O10 owns test design/execution evidence; O12 owns broader evaluative interpretation and impact judgement.

## Specialist procedures

`unit-test-generator`, `integration-test-generator`, `system-test-generator`, `regression-test-engine`, `contract-test-engine`, `fuzz-testing-engine`, `performance-benchmark-engine`, `security-test-engine`, `cross-platform-test-engine`, `compatibility-test-engine`, `output-integrity-validator`, `reconstruction-equivalence-tester`, `acceptance-test-manager`, `quality-gate-controller`, `independent-verification-engine`.

## Test strategy

Choose from static/manifest validation, unit, integration, system, contract, regression, boundary/edge, fuzz, performance, security, compatibility, cross-platform, output integrity and reconstruction equivalence. Tests must be mapped to changed behavior and risk; a large test count is not coverage quality.

## Workflow

1. Convert requirements and preserved behavior into observable acceptance criteria.
2. Identify baseline, candidate, environment, input data, oracle and dependencies.
3. Select tests based on the change-impact map and security/risk level.
4. Separate test layers: `STATIC`, `CONTRACT`, `HARNESS`, `HOST_BEHAVIOR`, `RUNTIME`, `INDEPENDENT`.
5. Define positive, negative, boundary, adversarial and regression cases where appropriate.
6. Run only when tool/environment/permission is available. Record actual status and evidence.
7. Validate test oracle: make sure expected result is justified and test can detect failure; include mutation/sensitivity checks where valuable.
8. Report failures, flaky/intermittent cases, skipped tests, false positives and limitations.
9. Independent verification reviews patch against baseline/spec, ideally without inheriting builder's confirmation framing.
10. Send test records to O12 for quality/outcome interpretation.

## Allowed test statuses

`PASS`, `FAIL`, `BLOCKED`, `NOT_RUN`, `NOT_APPLICABLE`, `UNVERIFIABLE`. Do not turn a blocked or unrun test into pass. Static checks do not prove runtime. CI success applies only to the exact commit and checks inspected.

## Output contract

Test plan; test records with ID, requirement, environment, expected/actual, status and evidence; regression impact map; failure dossier; coverage limitations; independent review; acceptance disposition. Do not manufacture percentages or benchmark values.

## Stop conditions

Hold release for critical test-oracle failure, unexplained P0/P1 regression, missing approval, test environment mismatch or unverified material requirement. Pass only when the applicable hard gates have evidence.
