# A.S.F.R.E.E Local Reference Runtime — Source & Reproduction Notes

## Purpose and boundary

The portable A.S.F.R.E.E plugin is skills-only. The local Python reference runtime is a separate implementation used for development, evaluation, and reproducible CI checks. It is **not** a hosted service, API gateway, MCP server, worker fleet, or production deployment.

The repository does not track the expanded `runtime/` workspace as a normal source directory. Instead, it tracks checksum-pinned source distributions and deterministic extraction/overlay scripts. CI reconstructs the working runtime before validation. Therefore, a link to `runtime/README.md` is not a valid repository source link.

## Source distribution

- P0 baseline source is represented by ordered base64 shards under `implementation-bundles/.p0-v0.3.0/` and its SHA-256 sidecar.
- P0 hardening is a separately versioned overlay under `implementation-bundles/.p0-hardening-v0.3.1/` with its own SHA-256 sidecar.
- P1 security is a separately versioned overlay under `implementation-bundles/.p1-security-v0.2.0/` with its own SHA-256 sidecar.
- `scripts/unpack_p0_bundle.py`, `scripts/apply_p0_hardening.py`, and `scripts/apply_p1_security.py` reconstruct the runtime workspace from those sources.
- `scripts/validate_package.py` checks package structure, schemas, fixtures, bundle integrity, and required runtime files after reconstruction.

The bundle version is not the plugin package version. The current portable plugin package version and the local runtime project version are tracked separately in the manifests and package metadata.

## Reproduce the CI validation sequence

Use Python 3.11+ (the repository CI currently runs Python 3.12). From the repository root:

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

These commands are a reproduction procedure; they are not evidence that a particular machine has run them. Use the CI run associated with the exact commit SHA when reporting a verified result.

## Verification limits

Passing static checks and local unit tests establishes only the covered contracts and test paths. It does not establish a configured external identity provider, live cloud KMS/HSM, encryption of metadata/WAL/logs/backups, externally anchored immutable audit, independently enforced cloud tenant isolation, real rootless OCI/gVisor/Kata runtime isolation, hostile-workload containment, production availability, backup/restore, or a production deployment.

The P1 execution adapter uses mocked runtime tests in the current reference baseline; actual OCI execution and hostile-workload isolation remain `NOT_RUN` until demonstrated on the target infrastructure. Production readiness remains a separate, human-approved gate.

## Change policy

Treat the source shards, extraction scripts, and checksum sidecars as one integrity-controlled source set. Any bundle update must include:

1. deterministic shard ordering and exact expected shard count;
2. checksum verification before extraction;
3. an extraction allowlist and path-traversal protections;
4. a versioned overlay with a separate checksum;
5. static package validation and runtime regression tests;
6. explicit documentation of what was and was not executed.
