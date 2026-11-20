# A.S.F.R.E.E

**AI Systems Forensics & Reconstruction Evaluation Engine**

Universal-by-design · Evidence-driven · Supervised engineering

A.S.F.R.E.E is a modular intelligence system for authorized forensic analysis, architecture decomposition, evaluation, diagnosis, controlled remediation, reconstruction and independent verification of AI/software systems.

## Current baseline

- **Canonical plugin package:** v0.3.0 in [`plugin/`](plugin/).
- **Architecture:** one M00 master orchestrator and twelve specialist skills O01–O12.
- **P0 reference runtime:** local Python implementation of Evidence Management, Master Orchestration & Contract Engine, and Supervised Change & Independent Verification.
- **Acceptance specifications:** 30 baseline cases plus 37 P0 cases; these are specifications, not execution records.
- **Production platform:** not deployed or production-verified.

## The three P0 foundations

1. **Evidence Management System** — source/provenance registry; content-addressed artifact storage; immutable evidence records; typed claim/evidence links; case boundaries; hash-chained audit ledger; explicit legacy migration.
2. **Master Orchestration & Contract Engine** — versioned case/task/handoff contracts; deterministic routing to O01–O12; dependency DAG; idempotency; worker/specialist leases; bounded retry; evidence-backed capability readiness; route observability.
3. **Supervised Change & Independent Verification Engine** — proposal digest; exact-path approval scope; authority and expiry checks; fail-closed approval adapter; sandbox-only execution; baseline recheck; atomic change checkpoints; recovery/rollback; independent reviewer plan and verification evidence.

## Repository layout

```text
.
├── plugin/                 # Canonical skills-only package v0.3.0
│   ├── plugin.json
│   ├── .codex-plugin/
│   ├── skills/              # M00 + O01–O12 and compatibility aliases
│   ├── references/          # architecture, contracts, JSON Schemas and controls
│   └── tests/               # baseline + P0 acceptance specifications
├── runtime/                # Separate local Python reference implementation
│   ├── asfree/              # evidence, contracts, orchestration, changes
│   ├── tests/               # executable unit/recovery tests
│   └── examples/            # end-to-end local quickstart
├── docs/implementation/    # P0 architecture and threat model
├── scripts/                # deterministic static validator and bundle unpacker
└── .github/workflows/      # static + runtime test CI
```

## Validate locally

Python 3.11+ is required. The P0 runtime source is distributed as a SHA-256-verified, ordered source archive. The archive may be reconstructed from its nine base64 shards in `implementation-bundles/.p0-v0.3.0/` before running:

```bash
python scripts/unpack_p0_bundle.py
python scripts/validate_package.py
python -m py_compile runtime/asfree/*.py runtime/tests/*.py
PYTHONPATH=runtime python -m unittest discover -s runtime/tests -v
PYTHONPATH=runtime python runtime/examples/quickstart.py
```

The tests use the Python standard library; no third-party runtime dependency is required. The portable plugin remains skills-only; the Python implementation is a separate local reference source bundle, not an embedded hosted runtime.

## Capability and security boundary

The P0 runtime is an executable **local, single-node reference**, not a production A.S.F.R.E.E platform. It uses SQLite and a local content-addressed blob directory. It does not bundle OIDC/MFA, authenticated principal binding, KMS/encryption, remote object storage, tenant isolation, externally anchored WORM audit, OS/container isolation, dynamic test runners, HTTP/MCP servers, worker daemons, cloud deployment, HA, backups, retention/deletion, or production release. Confidential/sensitive records are rejected when encryption is unavailable. Staging and production changes are disabled. Actor/worker identifiers remain caller-supplied labels until an authenticated identity adapter is integrated.

See [`runtime/README.md`](runtime/README.md), [`P0-FOUNDATIONS.md`](docs/implementation/P0-FOUNDATIONS.md), and [`THREAT-MODEL.md`](docs/implementation/THREAT-MODEL.md).

## Contributing and license

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`LICENSE-STRATEGY.md`](LICENSE-STRATEGY.md) before contributing. The current source baseline uses PolyForm Noncommercial License 1.0.0 (source-available, not OSI-approved open source); commercial use requires separate written permission. Brand rights are separate. The initial repository commit contained Apache-2.0, so prior grant history must be reviewed before making broad claims about retroactive restrictions.
