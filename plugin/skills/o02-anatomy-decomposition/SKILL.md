---
name: o02-anatomy-decomposition
description: Use when the target system must be decomposed into components, responsibilities, interfaces, data/control flows, dependencies, or architecture layers.
---

# Anatomy & Decomposition Orchestrator

## Mission
Reconstruct the observable structural and functional model of a technical target at atomic, component, system, ecosystem, and infrastructure levels.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`plugin-anatomy-analyzer;skill-anatomy-analyzer;agent-anatomy-analyzer;orchestrator-anatomy-analyzer;tool-anatomy-analyzer;prompt-anatomy-analyzer;api-anatomy-analyzer;mcp-anatomy-analyzer;runtime-anatomy-analyzer;software-architecture-analyzer;component-dependency-mapper;functional-relationship-mapper;data-flow-analyzer;control-flow-analyzer;interface-contract-analyzer;capability-mapping-engine;architecture-visualizer`

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
Map each component to a unique responsibility, input/output, state, dependencies, interface contract, failure modes, and consumers. Distinguish direct observation, documented dependency, inferred relationship, and causal hypothesis. Look for duplication, missing owners, cyclic dependencies, hidden coupling, boundary mismatches, single points of failure, and orphan components. Do not claim hidden internals from black-box behavior.

**Output contract:** Structural blueprint; component/ownership inventory; function map; data/control-flow map; dependency and interaction graph; capability matrix; architecture gaps.

## Quality and stop conditions
- Do not invent artifacts, test results, metrics, access, provenance, or causal certainty.
- Do not use unsupported numerical ratings.
- Stop or return `BLOCKED` when permission, evidence, environment, or scope is insufficient for the requested operation.
- Preserve unrelated behavior and data. Require explicit approval for consequential changes.
- Report `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_RUN`, or `UNVERIFIABLE` rather than implying success.
