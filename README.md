# A.S.F.R.E.E

**AI Systems Forensics & Reconstruction Evaluation Engine**

Universal-by-design · Evidence-driven · Supervised engineering

A.S.F.R.E.E is a modular intelligence system for authorized forensic analysis, architecture decomposition, evaluation, diagnosis, controlled remediation, reconstruction and independent verification of AI/software systems.

## Current baseline

- **Canonical plugin package:** v0.3.2 in [`plugin/`](plugin/).
- **Architecture:** one M00 master orchestrator and twelve specialist skills O01–O12.
- **P0 reference runtime:** local Python implementation of Evidence Management, Master Orchestration & Contract Engine, and Supervised Change & Independent Verification.
- **Acceptance specifications:** 30 baseline + 37 P0 + 8 P0 hardening + 33 P1 security cases. The executable runtime suite has 79 P0 + 31 P1 tests (110 total); specifications and executed tests remain distinct.
- **Production platform:** not deployed or production-verified.

## The three P0 foundations

1. **Evidence Management System** — source/provenance registry; content-addressed artifact storage; immutable evidence records; typed claim/evidence links; case boundaries; hash-chained audit ledger; explicit legacy migration.
2. **Master Orchestration & Contract Engine** — versioned case/task/handoff contracts; deterministic routing to O01–O12; dependency DAG; idempotency; worker/specialist leases; bounded retry; evidence-backed capability readiness; route observability.
3. **Supervised Change & Independent Verification Engine** — proposal digest; exact-path approval scope; authority and expiry checks; fail-closed approval adapter; sandbox-only execution; baseline recheck; atomic change checkpoints; recovery/rollback; independent reviewer plan and verification evidence.

## P1 Security & Trust Plane (local reference)

P1 adds an integration layer around P0, not a hosted multi-tenant platform:

- **Identity and access:** narrow OIDC RS256 access-token validation, server-pinned HTTPS issuer/audience/JWKS, default-deny tenant-first policy, MFA/separation-of-duties rules, allow/deny audit and short-lived process-local authorization capabilities.
- **Tenant partitioning:** authenticated tenant-derived SQLite/blob partitions and capability-checked storage facades. This is local filesystem partitioning, not independent cloud IAM or OS isolation.
- **Encryption:** AES-256-GCM envelope encryption for artifact blob bytes through a KMS provider contract. The in-memory provider is test-only; no cloud KMS/HSM adapter is supplied. SQLite metadata, audit rows, WAL, logs, temporary files and backups remain plaintext; confidential/sensitive metadata stays blocked.
- **Execution boundary:** worker identity and task:execute capability bound to tenant/job, immutable image digest allowlisting, and a fail-closed rootless OCI adapter requiring seccomp, gVisor/Kata and host output quotas. Runtime tests use mocks; actual OCI execution is NOT_RUN.

P1 contributes 31 executable security tests. Together with P0, 110 tests pass locally. These results do not prove a live IdP, KMS, encrypted metadata, external audit anchoring, cloud tenant isolation, kernel/container isolation or production readiness. See [P1 foundations](docs/implementation/P1-SECURITY-FOUNDATIONS.md), [P1 threat model](docs/implementation/P1-THREAT-MODEL.md) and [P1 operator notes](docs/implementation/P1-OPERATIONS.md).

## Release and routing governance

The portable plugin package is versioned independently from the local reference runtime and its source bundles. `plugin/plugin.json` is the repository's package-version authority; the compatibility manifest and package README must match it. Plugin Creator is a separate app-release registry and must be updated from a reviewed source snapshot, then read back before the app is called synchronized.

M00 and numbered O01–O12 are the only canonical specialist procedures. Historical unnumbered skill folders are retained only as redirect-only compatibility aliases. See [Release, Source-of-Truth & Routing Governance](docs/architecture/RELEASE-AND-ROUTING-GOVERNANCE.md).
 
## Repository layout

```text
.
├── plugin/                 # Canonical skills-only package v0.3.0
│   ├── plugin.json
│   ├── .codex-plugin/
│   ├── skills/              # M00 + O01–O12; historical names are redirect-only aliases
│   ├── references/          # architecture, contracts, JSON Schemas and controls
│   └── tests/               # baseline + P0 acceptance specifications
├── docs/implementation/    # P0/P1 architecture and threat models
├── implementation-bundles/ # SHA-256-pinned P0/P1 source overlays
├── scripts/                # deterministic validator and P0/P1 bundle appliers
└── .github/workflows/      # static + runtime test CI
```

## Validate locally

Python 3.11+ is required. The P0 runtime source is distributed as a SHA-256-verified baseline archive plus a separately verified hardening overlay. The archive may be reconstructed from its nine base64 shards in `implementation-bundles/.p0-v0.3.0/` before running:

```bash
python scripts/unpack_p0_bundle.py
python scripts/apply_p0_hardening.py
python scripts/apply_p1_security.py
python -m pip install -e ./runtime
python scripts/validate_package.py
python -m py_compile runtime/asfree/*.py runtime/asfree/security/*.py runtime/tests/*.py
PYTHONPATH=runtime python -m unittest discover -s runtime/tests -v
PYTHONPATH=runtime python runtime/examples/quickstart.py
```

The tests use the Python standard library; no third-party runtime dependency is required. The portable plugin remains skills-only; the Python implementation is a separate local reference source bundle, not an embedded hosted runtime.

## Capability and security boundary

P0 remains an executable **local, single-node, workspace-bounded reference**. P1 adds local OIDC validation and policy facades, tenant-partitioned stores, blob envelope encryption, and a fail-closed OCI execution adapter. It is still not a deployed or production-verified service. There is no configured IdP, live cloud KMS, encrypted SQLite metadata/WAL/logs/backups, externally anchored WORM audit, independently isolated cloud tenant storage, provisioned OCI runtime/quota provider, HTTP/MCP service, worker fleet, HA, backup/restore, retention/deletion or production release. The authorization capability is process-local; the legacy P0 ChangeManager actor-string interface still needs a request-bound policy adapter. Confidential/sensitive metadata remains rejected. Actual OCI execution and hostile-workload isolation are NOT_RUN. Staging and production changes remain disabled.

See [Local Reference Runtime Source & Reproduction Notes](docs/implementation/RUNTIME-REFERENCE.md) for the exact bundle reconstruction sequence and verification limits.

## Contributing and license

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`LICENSE-STRATEGY.md`](LICENSE-STRATEGY.md) before contributing. The current source baseline uses PolyForm Noncommercial License 1.0.0 (source-available, not OSI-approved open source); commercial use requires separate written permission. Brand rights are separate. The initial repository commit contained Apache-2.0, so prior grant history must be reviewed before making broad claims about retroactive restrictions.
