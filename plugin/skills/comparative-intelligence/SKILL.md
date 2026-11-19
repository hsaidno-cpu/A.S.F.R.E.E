---
name: comparative-intelligence
description: Use when the user needs a fair comparison of two or more systems, versions, architectures, tools, features, alternatives, benchmarks or before-and-after states.
---

# O05 — Comparative Intelligence Orchestrator

## Mission

Compare alternatives with normalized, context-appropriate criteria and explain trade-offs. Do not manufacture a winner or add scores without a valid measurement model.

## Specialist procedures

`version-comparison`, `architecture-comparison`, `skill-comparison`, `orchestrator-comparison`, `feature-comparison`, `capability-comparison`, `performance-comparison`, `security-comparison`, `efficiency-comparison`, `compatibility-comparison`, `dependency-comparison`, `benchmark-comparison`, `strength-gap-analyzer`, `weakness-gap-analyzer`, `tradeoff-analyzer`, `comparative-recommendation-engine`.

## Workflow

1. Define comparison question, decision owner, alternatives, time/version, operating context and constraints.
2. Set a shared baseline and comparable criteria. Record criteria that cannot be normalized.
3. Gather evidence for each alternative using equivalent methods and environments where feasible.
4. Separate measured values, qualitative judgments, vendor/user claims and unknowns.
5. Identify positive delta, negative delta, quality gaps, risk gaps and cost-benefit trade-offs.
6. Test sensitivity to weights, assumptions, missing data and context.
7. Explain the conditions under which each alternative is preferable.
8. Recommend only when the criteria support a context-specific decision; include do-nothing/defer/pilot options where relevant.

## Modes

A vs B; old vs new version; actual vs desired architecture; internal vs external option; benchmark vs target; before vs after change. For before/after comparisons, check environment, input and configuration comparability.

## Output contract

- Comparison charter and baseline.
- Criteria matrix with source, method and evidence status.
- Per-criterion comparison and confidence.
- Positive/negative delta and gap diagnosis.
- Trade-off and sensitivity report.
- Contextual recommendation, assumptions, unknowns and conditions for reversal.

## Rules

Do not average incomparable metrics. Do not treat missing evidence as zero or failure. Do not copy a benchmark ranking without matching workload/hardware/configuration. Do not claim statistical significance without a suitable analysis. Hand criteria design to O12 and test metrics to O10.
