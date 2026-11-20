# Roadmap

## Phase 0 — P0 reference foundations (implemented locally)

The repository now contains a local reference runtime for Evidence Management, M00 Orchestration & Contract Engine, and Supervised Change & Independent Verification. It includes provenance lineage, hash-addressed blobs, append-only audit chain, task DAG/leases, evidence-backed capability readiness, approval-bound sandbox changes, recovery and independent static review.

**Gate status:** local unit/recovery suite and end-to-end quickstart pass in the developer workspace; GitHub CI must verify the exact PR head. This does not satisfy production readiness.

**Remaining gate:** authenticate actors/workers; add encryption/KMS and remote object storage; externally anchor audit integrity; implement OS/container isolation; integrate dynamic test runners and operational recovery before any staging/production service.

## Phase 1 — Forensic MVP

O01 artifact inventory, O02 anatomy maps, O03 positive analysis, O04 negative analysis, O12 evaluation core, report generator.

**Gate:** artifact-based findings are evidence-linked and limitations visible.

## Phase 2 — Comparative and diagnostic intelligence

O05 comparison, O06 defect reproduction/root-cause workflow, benchmark and risk-impact records.

**Gate:** tests distinguish observed defects from hypotheses and false positives.

## Phase 3 — Supervised engineering expansion

The local sandbox-only change engine is implemented as a reference. Next: isolated worker runtime, signed approvals from authenticated principals, external policy enforcement, dynamic test adapters, provenance, and stronger rollback/restore guarantees.

**Gate:** no target mutation without authorization; failures and partial changes are recoverable; the executor must be a real OS/container/VM isolation boundary before handling untrusted workloads.

## Phase 4 — Reconstruction and independent evaluation

O08 reconstruction/adaptation, O10 independent QA, O12 post-change and benefit evaluation.

**Gate:** preserved behavior, contract/regression results and residual risks are evidenced.

## Phase 5 — Interoperability and governance

Versioned API/MCP/tool adapters, identity/access policies, isolation, audit trails and observability.

**Gate:** contract, security and compatibility tests pass for each supported adapter.

## Phase 6 — Operational maturity

Longitudinal evaluation, calibration, cost controls, incident response, release automation and continuous improvement.

**Gate:** operational readiness is demonstrated with real measurements and authorized deployment evidence.

Cloud provider, programming language, database, workflow engine, model providers, budgets and performance targets remain open decisions until workload and security requirements are defined.
