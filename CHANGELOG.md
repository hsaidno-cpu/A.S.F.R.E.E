# Changelog

## 0.5.0-rc.1 — 2026-11-22

- Add RPEDS as a subordinate roadmap lifecycle control plane governed by M00; retain O01–O12 as the canonical numbered specialist set.
- Add four bounded RPEDS modules for roadmap architecture, progressive development, continuous evaluation scheduling, and adaptive roadmap optimization.
- Add seven RPEDS JSON Schemas, including the missing work-item contract; add 14 executable positive/negative schema fixtures and four semantic dependency/reference scenarios alongside 24 still-specification-only behavioral acceptance cases.
- Integrate RPEDS routing and authority boundaries into M00, O12, architecture, evaluation and data-contract documentation.
- Define explicit conditional O03–O06 route contracts: positive-value preservation, adversarial risk, normalized option comparison, and observed-defect diagnosis, with distinct triggers/non-triggers, handoff fields, sequence/parallelism and authority boundaries.
- Add RPEDS architecture and implementation-status documentation; explicitly state that no persistent scheduler, automatic monitor, runtime database or automatic GitHub–Notion sync is deployed by this package.
- Establish package version candidate 0.5.0-rc.1; local runtime and source-bundle version planes remain unchanged.


## 0.4.0-rc.1 — 2026-11-21

- Add the ecosystem identity registry and JSON Schema, with CI-enforced uniqueness/role/redirect/version-source checks; add a normative migration and deprecation policy and six release-governance acceptance specifications.
- Add P1.1 security-to-production hard gates for IdP/MFA assurance, cross-process signed delegation, full SCIVE operation authorization, complete at-rest encryption scope, isolated execution, host-enforced quotas, external WORM audit, infrastructure tenant isolation, concurrency testing and independent human review.
- Extend M00 and O09/O11/O12 procedures so security authorization, runtime readiness and evaluation evidence are enforced as distinct responsibilities.
- Add normative P1.1 readiness contract, reconstruction/evidence-boundary note, four JSON Schemas and 20 acceptance specifications. All P1.1 cases remain SPECIFICATION_ONLY until implementation and execution evidence is integrated.
- Preserve the local reference runtime at 0.2.0. The P1.1 local prototype is not included in this repository source bundle or the current CI baseline.
- Release candidate only; no live IdP/KMS/HSM, rootless OCI/gVisor/Kata, host quota agent, WORM anchor, production tenant isolation or independent human sign-off is claimed.

## 0.3.2 — 2026-11-21

- Align the canonical plugin and compatibility manifests, package README and static validator at package version 0.3.2; keep the local runtime and source-bundle versions independent.
- Convert twelve historical unnumbered skill paths into redirect-only compatibility aliases to the canonical O01–O12 procedures.
- Add release/source-of-truth governance for repository and Plugin Creator app releases, guarded updates, read-back verification, and lifecycle-state reporting.
- Add a tracked runtime source/reproduction guide and replace the missing `runtime/README.md` repository link.
- Preserve the 30 baseline acceptance cases and add five dedicated release/routing governance specifications; strengthen static validation to enforce both sets.
- Strengthen static validation for manifest parity, README versions, registered skill paths, redirect-only aliases and tracked governance references.

## Runtime 0.2.0 — P1 Security & Trust Plane — 2026-11-20

- Add OIDC RS256 access-token validation against server-configured HTTPS issuer, audience and JWKS; reject token-controlled key URLs and enforce token claims.
- Add default-deny tenant-first authorization policy, MFA/separation-of-duties rules, access-decision audit and integrity-bound process-local authorization capabilities.
- Add tenant-derived local SQLite/blob partitions and capability-checked storage facade.
- Add AES-256-GCM envelope encryption for artifact blob bytes and a KMS provider contract with rewrap support.
- Add worker-token-bound execution dispatcher and fail-closed rootless OCI preflight for immutable image digests, seccomp, gVisor/Kata, no-network execution and host quota receipts.
- Add five security JSON Schemas, 33 P1 acceptance specifications, 31 executable P1 tests and threat/operations documentation.
- Bundle P1 source as a SHA-256-pinned 17-file overlay; runtime package version is 0.2.0. The canonical skills-only plugin manifest remains v0.3.0.
- Explicitly retain production caveats: no configured IdP, live KMS, encrypted metadata, external WORM audit, distributed signed capability, provisioned OCI/quota backend, actual hostile-workload validation or production deployment.

## 0.3.1 — 2026-11-20

- Bind proposal and approval records to their original hash-chained audit events; detect persisted-row tampering before filesystem mutation.
- Include POSIX before/after file modes in the approved proposal digest, baseline drift checks and rollback; new files default to 0600.
- Add metadata-only artifact inventory and strict claim-link/context validation.
- Keep reviewer source independence UNKNOWN unless authenticated identity and independent provenance can substantiate it.
- Clarify the execution boundary as workspace-bounded, not OS/container isolation.
- Add eight P0 hardening acceptance specifications and expand the executable suite from 70 to 79 tests.

## 0.3.0 — 2026-11-20

- Implement the three P0 foundations as an executable local Python reference runtime.
- Add source, artifact, evidence and claim registries with content-addressed SHA-256 blobs and case-scoped provenance links.
- Add append-only hash-chained audit records and explicit legacy schema migration to unverified provenance placeholders.
- Add M00 task orchestration with versioned contracts, DAG validation, idempotency, worker/specialist leases, bounded retries and evidence-backed capability readiness.
- Add scoped change proposals, fail-closed approval, sandbox-only apply, baseline rechecks, checkpointed recovery/rollback, and separate independent review plans.
- Add 37 P0 acceptance specifications, five runtime JSON Schemas, a local end-to-end quickstart, runtime tests and CI execution.
- Clarify that the portable plugin remains skills-only and the runtime is a separate local reference implementation, not a deployed production service.

## 0.2.1 — 2026-11-20

- Consolidate both A.S.F.R.E.E plugin variants into one canonical package.
- Normalize M00 and O01–O12, including operating modes, forensic depth L0–L6 and authority levels S0–S5.
- Unify finding, evidence, claim, severity, confidence, approval and lifecycle vocabulary.
- Expand machine-readable contracts to 16 JSON Schemas.
- Merge and deduplicate acceptance fixtures into 30 unique cases.
- Integrate forensic methodology, recovery, security/authority, tool-adapter and merge-lineage references.
- Preserve a skills-only boundary: runtime execution and MCP/API adapters are not claimed as deployed.

## 1.0.0 — 2026-11-20

- Establish the initial M00 master orchestrator and O01–O12 specialist skill package.
- Define O11 Security & Governance and O12 Evaluation Intelligence as cross-cutting control planes.
- Add shared evidence, finding, change, tool-adapter and test contracts.
- Add continuous evaluation, supervised authority, recovery and release-state rules.
- Add declarative acceptance fixtures and static package validation.
- Set the source-available / noncommercial license baseline; review historical Apache-2.0 snapshot implications before distribution.
