# Shared Data & Handoff Contracts — Compatibility Entry

This file is retained as a stable entry point for users of the earlier `asfree-master-orchestrator` package. The authoritative, consolidated contracts now live in:

- `data-contracts.md` — canonical entities, relationships, epistemic labels, status vocabulary, and migration guidance.
- `schemas/*.schema.json` — machine-readable validation contracts.
- `../skills/asfree-master-orchestrator/SKILL.md` — routing, authority, lifecycle, and handoff rules.

Do not introduce a second definition of a field or enum here. If the canonical model changes, update `data-contracts.md`, the affected JSON Schemas, and compatibility notes together.

## Required handoff payload

A specialist handoff should contain: case/target/task identity; intent and scope; non-goals; inputs and provenance; capability and permission status; method; findings and evidence references; assumptions and unknowns; dependencies; expected output schema; acceptance criteria; risk/approval status; completion status; next owner.

Missing values must be explicitly marked unknown or not applicable. Case-local IDs are trace labels, not evidence of persistent storage.
