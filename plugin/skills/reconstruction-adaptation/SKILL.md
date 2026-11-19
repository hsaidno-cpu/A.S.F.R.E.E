---
name: reconstruction-adaptation
description: Use when the user needs an authorized system, architecture, workflow, prompt, skill, tool, API adapter or software component reconstructed, modularized, migrated or adapted across platforms.
---

# O08 — Reconstruction & Adaptation Orchestrator

## Mission

Rebuild or adapt systems from available evidence while preserving verified behavior and clearly separating observed specification from inferred internals. Reconstruction is not permission to clone proprietary material or bypass access controls.

## Specialist procedures

`architecture-reconstruction`, `functional-reconstruction`, `workflow-reconstruction`, `skill-reconstruction`, `orchestrator-reconstruction`, `prompt-reconstruction`, `tool-reconstruction`, `api-adapter-generator`, `mcp-adapter-generator`, `cross-platform-adapter`, `schema-converter`, `protocol-adapter`, `compatibility-layer-generator`, `modularization-engine`, `architecture-migration-engine`, `capability-extension-engine`, `legacy-system-adapter`, `reconstruction-validator`.

## Access modes

- White-box: reconstruct from source/config/docs available.
- Grey-box: combine partial implementation with API/log/behavior evidence; mark inferred areas.
- Black-box: reproduce observable behavior only; do not claim internal algorithm equivalence.

## Workflow

1. Define target, authorized source, desired outcome, scope, non-goals and protected behavior.
2. Acquire O01 inventory and O02 architecture/function maps.
3. Capture a baseline: version, interfaces, input/output examples, tests, known limitations and dependencies.
4. Identify gaps, conflicting descriptions and unknown internal behavior.
5. Define reconstruction requirements and invariants; distinguish exact equivalence from improvement.
6. Choose architecture/adapter/migration strategy; prefer stable versioned contracts and loose coupling.
7. Plan modular boundaries, schemas, compatibility layer, versioning, state migration and failure modes.
8. Produce a reconstruction blueprint and reversible change set. Require approval before applying.
9. Use O09 for supported sandbox/tool execution and O11 for access/security approval.
10. O10 tests functional/contract/regression equivalence; O12 evaluates quality gains/trade-offs.

## Output contract

Baseline and evidence; target architecture; before/after responsibility map; interface contracts; compatibility/migration matrix; planned/actual changes; preservation matrix; test plan; rollback; residual unknowns; implementation status.

## Quality gate

All material outputs map to evidence or labelled assumptions. Existing valuable behavior has regression coverage. Schema/protocol compatibility is explicitly decided. Black-box inference is not overstated. No external system or proprietary target is modified/copied without permission.
