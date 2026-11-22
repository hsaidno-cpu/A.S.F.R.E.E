# Roadmap

## Phase 0 — P0 reference foundations (implemented locally)

The repository now contains a local reference runtime for Evidence Management, M00 Orchestration & Contract Engine, and Supervised Change & Independent Verification. The v0.3.1 hardening overlay adds proposal/approval-to-audit-event integrity, permission-mode-aware approvals and rollback, stricter evidence contracts, metadata-only artifact listing, and honest reviewer-independence status.

**Gate status:** 79 local unit/recovery tests, Python compilation and end-to-end quickstart pass; GitHub CI must verify the exact PR head. This does not satisfy production readiness.

**P0→P1 boundary:** local reference controls now exist for authenticated principals, default-deny policy, tenant-scoped stores, blob envelope encryption and a fail-closed OCI adapter. Production gates remain open for live IdP configuration, cross-process signed delegation, managed KMS, encrypted metadata, external audit anchoring, cloud tenant isolation, actual OCI runtime and quota/log supervision.

## P1 — Security & Trust Plane (reference layer implemented; production gate HOLD)

P1 adds OIDC RS256 token validation, default-deny tenant-first authorization, MFA/separation-of-duties policy rules, process-local authorization capabilities, tenant-derived local partitions, AES-256-GCM envelope encryption for artifact blobs, KMS provider contracts, and a worker-token-bound rootless OCI execution adapter.

**Verification:** 31 P1 security tests and 79 P0 regression tests pass locally (110 total); Python compilation and the P0 end-to-end quickstart pass. The 33 P1 acceptance specifications are declarative cases, not all separate executed tests. OCI runtime behavior is tested with mocks; actual runtime execution is NOT_RUN. Local editable installation was not verified in this offline environment because pip build isolation could not retrieve setuptools.

**Production gate remains HOLD** until a real IdP and its claim/MFA semantics are configured; distributed authorization uses signed delegated capabilities; cloud KMS/HSM and secret management are implemented; database/WAL/log/backup metadata encryption is complete; tenant partitions use independently enforced infrastructure IAM; audit records are externally anchored; rootless OCI/gVisor/Kata and host quota/streaming-log supervisors run on the target kernel; hostile-workload and concurrency tests pass; and human security review approves deployment.

## Phase 1 — Forensic MVP

O01 artifact inventory, O02 anatomy maps, O03 positive analysis, O04 negative analysis, O12 evaluation core, report generator.

**Gate:** artifact-based findings are evidence-linked and limitations visible.

## Phase 2 — Comparative and diagnostic intelligence

O05 comparison, O06 defect reproduction/root-cause workflow, benchmark and risk-impact records.

**Gate:** tests distinguish observed defects from hypotheses and false positives.

## Phase 3 — Supervised engineering expansion

The local sandbox-only change engine is implemented as a reference. Next: connect the authenticated policy facade to every SCIVE mutation and approval path, implement signed cross-process authorization delegation, provision and test the isolated worker runtime, add dynamic test adapters, provenance, and stronger rollback/restore guarantees.

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

## P1.1 — Security-to-production reconstruction (architecture and acceptance candidate)

The P1.1 contract now defines hard gates for real IdP/MFA assurance, asymmetric cross-process delegation, authorization at every SCIVE transition, complete encryption of metadata/WAL/temp/log/audit/backup, managed KMS/HSM, rootless OCI with gVisor/Kata, host-enforced quotas and bounded streaming, external WORM audit anchoring, infrastructure tenant isolation, concurrency/resilience testing and independent human security review.

**Current repository state:** portable plugin instructions, reference contracts, four new JSON Schemas and 20 acceptance specifications are recorded. The P1.1 cases are specification-only. The extended local runtime prototype is not yet part of the tracked GitHub source bundle and is not part of the current repository CI. The active P1 runtime remains 0.2.0.

**Gate:** no production promotion until runtime implementation is integrated, CI tests it, real IdP/KMS/database/WORM/OCI/quota providers are provisioned and read-back verified, hostile-workload and cross-tenant tests pass, key rotation/restore/concurrency are tested, and an independent human security review is signed. Current production status: NOT READY.



## Phase 7 — Progressive roadmap evaluation and development (RPEDS)

The 0.5.0-rc.1 candidate introduces RPEDS as a subordinate lifecycle control plane for versioned roadmaps, objective/phase/milestone decomposition, iterative development, evidence-based progress measures, evaluation checkpoints and adaptive replanning. It delegates evaluation judgment to O12, actual test execution/verification to O10, authorization to O11, change design to O07/O08 and supported runtime execution to O09. M00 remains the sole case-level coordinator.

**Candidate delivery:** portable RPEDS skill, four bounded reference modules, six JSON Schemas, 24 specification-only acceptance cases, M00/O12/architecture/data-contract integration, and a Notion operational tracking surface.

**Gate:** static package validation and exact pull-request CI must pass; PR review must confirm responsibility boundaries and evidence semantics. Merge, Plugin Creator package publication/read-back, runtime scheduler, persistent service, and automatic GitHub–Notion synchronization are separate future gates. This roadmap entry does not imply a merged or deployed release.
