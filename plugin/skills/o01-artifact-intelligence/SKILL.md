---
name: o01-artifact-intelligence
description: Use when files, repositories, packages, manifests, versions, dependencies, provenance, or artifact integrity must be inventoried before analysis.
---

# Artifact Intelligence Orchestrator

## Mission
Acquire, identify, inventory, and establish the provenance and inspection boundary of target artifacts.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`artifact-discovery;file-format-analyzer;metadata-forensics;instruction-extractor;package-inspector;dependency-inventory;version-history-analyzer;source-provenance-tracker;duplicate-component-detector;artifact-integrity-checker`

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
List artifacts and their exact paths/locators, formats, versions, sizes where observed, source/provenance state, dependencies, duplicates, missing references, integrity checks actually run, and access limitations. Do not infer a source file exists because a manifest references it. Do not execute artifacts during intake.

**Output contract:** Artifact inventory; source register; dependency list; missing/duplicate artifact report; integrity and provenance limitations.

## Quality and stop conditions
- Do not invent artifacts, test results, metrics, access, provenance, or causal certainty.
- Do not use unsupported numerical ratings.
- Stop or return `BLOCKED` when permission, evidence, environment, or scope is insufficient for the requested operation.
- Preserve unrelated behavior and data. Require explicit approval for consequential changes.
- Report `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_RUN`, or `UNVERIFIABLE` rather than implying success.
