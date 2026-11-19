---
name: anatomy-decomposition
description: Use when the user needs structural, functional, architectural, dependency, interaction, data-flow or control-flow decomposition of an authorized technical system.
---

# O02 — Anatomy & Decomposition Orchestrator

## Mission

Reconstruct an evidence-grounded model of what the target contains, what each component does, why it exists, what it depends on and how behavior/control/data cross boundaries. O02 owns the maps, not the final value/risk judgment or the implementation.

## Specialist procedures

`plugin-anatomy-analyzer`, `skill-anatomy-analyzer`, `subskill-anatomy-analyzer`, `orchestrator-anatomy-analyzer`, `agent-anatomy-analyzer`, `tool-anatomy-analyzer`, `prompt-anatomy-analyzer`, `api-anatomy-analyzer`, `mcp-anatomy-analyzer`, `runtime-anatomy-analyzer`, `software-architecture-analyzer`, `component-dependency-mapper`, `functional-relationship-mapper`, `data-flow-analyzer`, `control-flow-analyzer`, `interface-contract-analyzer`, `capability-mapping-engine`, and `architecture-visualizer`.

Select only the procedures that fit the artifact. A diagram is a model; it is not proof of runtime behavior.

## Decomposition levels

1. Atomic: instruction, parameter, variable, rule, function, schema, metadata.
2. Component: tool, subskill, skill, module, API endpoint, agent, service.
3. System: plugin, workflow, application, orchestrator, runtime.
4. Ecosystem: multiple products, integrations, identity boundaries and cross-platform exchange.
5. Infrastructure: deployment topology, storage, network, compute, security and operations.

## Workflow

1. Accept O01's artifact register and state the inspection depth (L0–L6).
2. Define system boundary, entry/exit points, actors, trust boundaries and environment.
3. Identify components with stable IDs and single responsibility; mark duplicated/overlapping roles.
4. Map inputs, outputs, state, control flow, data flow, dependencies and interface contracts.
5. Separate declared structure from observed behavior; tag documented, observed, inferred and hypothesized relationships.
6. Identify orphans, cycles, hidden couplings, single points of failure and ownership gaps.
7. Map capabilities to components and tool requirements; do not equate declarations with availability.
8. Create a functional decomposition and architecture graph; provide Mermaid/ASCII only when useful.
9. Hand structural gaps to O04; value opportunities to O03; criteria to O12; fixes to O07/O08.

## Required outputs

- `STRUCTURAL BLUEPRINT` with target boundary and inspection depth.
- `COMPONENT INVENTORY` with component ID, role, inputs, outputs, owner, dependencies and evidence.
- `FUNCTIONAL DECOMPOSITION MAP` with capability → responsible component → expected outcome.
- `DEPENDENCY GRAPH` and `INTERACTION MAP` with typed edges.
- `DATA FLOW` and `CONTROL FLOW` maps where evidence permits.
- `INTERFACE / CONTRACT MAP` for APIs, tools, MCP, schemas and handoffs.
- `CAPABILITY MATRIX` and `ARCHITECTURAL WEAKNESS MAP`.
- `UNKNOWN / OBSERVABILITY GAPS`.

## Quality gate

Every component and material relationship must have a basis or be explicitly marked inferred/hypothesized. Do not claim full coverage when files, endpoints, runtime or layers are inaccessible. Do not infer a microservice from a folder name or infer agent execution from a skills directory.
