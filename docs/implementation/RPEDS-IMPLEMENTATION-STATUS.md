# RPEDS Implementation Status and Evidence Boundary

## Snapshot

- Repository baseline: main commit 5dff096a03cbfb7d089f43fdfcdf39ae1e3c6133.
- Baseline portable package candidate: 0.4.0-rc.1.
- Proposed package candidate: 0.5.0-rc.1.
- Delivery method: feature branch and pull request; no direct edit to main.
- RPEDS package scope: one bounded control-plane skill, four reference modules, seven JSON Schemas including the work-item contract, 24 behavioral acceptance specifications, 14 schema fixtures, semantic dependency/reference checks, M00/O03–O12 conditional routing and documentation. The O03–O06 route definitions are explicit and role-specific; their route decisions are separated from execution/invocation states.

## What this change does

It defines a reproducible, evidence-led lifecycle for roadmaps, phases, milestones, iterations, work items, progress measures, evaluation gates and adaptive decisions. It establishes authority boundaries, status semantics, dependency and history requirements, progress calculation policy and machine-readable contracts.

## What this change does not do

It does not implement or deploy:
- a persistent runtime roadmap engine or scheduler;
- a background monitor or autonomous replanner;
- a production database or event bus;
- automatic GitHub ↔ Notion synchronization;
- a new API, MCP server, worker, CI service or cloud runtime;
- a new Python runtime capability.

Notion databases are a human-operable tracking surface. The portable plugin is an instruction-and-contract package. The local Python reference runtime remains on its separate version plane and is unchanged.

## Verification plan

1. Static package validator checks manifest parity, skill registration, seven RPEDS schemas and behavioral acceptance fixture shape.
2. The RPEDS contract validator meta-validates all Draft 2020-12 schemas, executes 14 positive/negative schema fixtures, and executes four semantic graph scenarios for acyclic dependencies, cycles, duplicate IDs and dangling references.
3. GitHub Actions runs the existing checksum-verified P0/P1 reconstruction, RPEDS contract validation, runtime test suite, package validator and quickstart on the exact PR head.
4. PR review inspects routing and responsibility boundaries, schema quality, evidence claims and version changes.
5. After merge (not part of this change), the installed Plugin Creator package must be independently updated and read back against the merged source commit.
6. Runtime scheduler, persistence, automatic sync or dynamic roadmap actions require a separately scoped implementation and test project.

Current execution status must be read from the exact PR/CI run. Specification presence is not test execution or deployment evidence.

## PRE–RPEDS shared DNA consolidation amendment — 2026-11-27

- PRE Standalone and RPEDS are peer, first-class manifestations of one jointly evolved roadmap competency, not a parent/alias relationship or replacement.
- RPEDS remains the native A.S.F.R.E.E roadmap workstream with its identity, four original modules, procedures, references and M00/O01–O12 integration.
- Shared DNA includes the R0–R9 kernel, roadmap object model, dependencies, progress/evidence/gate contracts, adaptation, process audit, assurance/closure, capability learning and release lineage.
- PRE current package read-back: v0.1.5, release `pluginrel_6b095bf2f4308191bf7d46ce98da36f7`.
- AFSA governs application to local SOP/authority/security/privacy/data boundaries; incompatible or authority-sensitive changes are adapted only under approved policy, held or quarantined.
- This source amendment does not deploy a release registry, webhook/event consumer, host updater, persistent receipt store or cross-host runtime.
