---
name: o07-remediation-bug-fixing
description: Use when a verified or accepted finding needs a corrective plan, controlled patch, configuration repair, refactoring, optimization, mitigation, or rollback design.
---

# Remediation & Bug Fixing Orchestrator

## Mission
Translate accepted findings into minimal, scoped, reversible fixes and controls with explicit verification.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`bug-fix-planner;code-patch-generator;prompt-instruction-fixer;configuration-fixer;dependency-fixer;integration-fixer;workflow-fixer;schema-fixer;security-remediation-engine;performance-optimizer;refactoring-engine;technical-debt-remediator;patch-impact-analyzer;rollback-planner;fix-regression-validator`

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
Require traceability from finding to root cause to requirement to changed file/component to test. Compare eliminate, redesign, correct, prevent, detect, mitigate/recover, transfer, accept, defer, and monitor. Preserve unrelated behavior. Check dependencies and side effects. Require explicit approval for material mutations, security/permission changes, production changes, deletion, or release. Never write without a verified target, baseline, and authority.

**Output contract:** Remediation options; selected change proposal; patch scope and diff plan; test plan; rollback and residual-risk record.

## Quality and stop conditions
- Do not invent artifacts, test results, metrics, access, provenance, or causal certainty.
- Do not use unsupported numerical ratings.
- Stop or return `BLOCKED` when permission, evidence, environment, or scope is insufficient for the requested operation.
- Preserve unrelated behavior and data. Require explicit approval for consequential changes.
- Report `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_RUN`, or `UNVERIFIABLE` rather than implying success.
