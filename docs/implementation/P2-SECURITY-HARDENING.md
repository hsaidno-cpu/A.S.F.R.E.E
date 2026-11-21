# A.S.F.R.E.E P2 Security & Trust Hardening

**Portable plugin package:** 0.4.0  
**Reference runtime package:** `asfree-runtime` 0.2.0  
**Source overlay:** P2 trust hardening 0.3.0  
**Disposition:** local reference implementation tested; production deployment HOLD.

## 1. What changed

P2 connects the four trust boundaries that were only partially covered by P1:

- provider-conformant OIDC/MFA profile and Ed25519 cross-process delegated capabilities;
- shared atomic replay/revocation and tenant-resource binding registries;
- SCIVE method-level policy coverage and signed actor/resource bindings;
- KMS adapter, fail-closed SQLCipher store, encrypted audit/log sinks and encrypted backup/temp stream;
- bounded OCI stdout/stderr streaming, host quota receipts and delegated streaming dispatcher;
- external WORM anchoring protocol, signed infrastructure tenant receipts and independent production admission.

The implementation remains an integration reference. It does not configure or deploy the external providers named by these contracts.

## 2. Trust components

| Component | Contract / enforcement | Local test evidence | Remaining production proof |
|---|---|---|---|
| `OIDCProviderConformanceProbe` | HTTPS discovery, pinned issuer, JWKS, RS256 | Fake discovery document | Actual IdP client and claim semantics |
| `MFAClaimProfile` / `MFAClaimAttestor` | ACR/AMR profile and fresh auth time bound to issuer/subject/token | Profile and stale-auth tests | IdP's signed MFA semantics and step-up deployment |
| `DelegatedCapabilityIssuer` / `Verifier` | Ed25519 signed cross-process authority with audience/resource/scope/role/MFA claims | Independent keysets, tamper and replay tests | KMS/HSM signer, rotation and key distribution |
| `RedisCapabilityStateStore` | Lua atomic revocation + one-time JTI use | Fake Redis state tests | Real Redis TLS/ACL/HA/failover |
| `SCIVEPolicyBoundary` | Registry for public Evidence/Orchestration/Change operations | Coverage and proposer/approver tests | Gateway-only exposure; raw service encapsulation in deployed API |
| `AWSKMSKeyProvider` | Tenant-bound GenerateDataKey/Decrypt/ReEncrypt | Injected KMS client | Actual role, key policy, audit, rotation and region controls |
| `SQLCipherStore` | Refuses non-SQLCipher fallback; KMS-wrapped DB DEK; WAL and rekey recovery | Fail-closed and sidecar/concurrency tests | SQLCipher driver, KMS-backed DB and restore drills |
| `EncryptedRecordSink` | Encrypt records before backend persistence | Plaintext absence test | Full log/SIEM/telemetry wiring |
| `EncryptedStreamFile` | Chunked AES-GCM backup/temp with authenticated commit | Roundtrip/tamper/abort tests | Tmpfs/swap/core dump and backup pipeline evidence |
| `StreamingRootlessOCIExecutor` | Popen/selectors bounded logs, process kill, signed host quota | Fake executor and hostile-output test | Rootless Docker + gVisor/Kata + actual quota host agent |
| `RedisInfrastructureBindingRegistry` | Shared atomic backend-resource-to-tenant binding | Two-client conflict test | Real shared registry durability/HA |
| `InfrastructureTenantStoreRouter` | Signed dedicated DB receipt plus shared binding | Fake provider and cross-tenant reuse test | Independent DB/IAM/network/KMS isolation |
| `AnchoredAccessDecisionRecorder` | Local outbox to external WORM receipt, verified and reconciled | Test anchor only | Object Lock compliance retention and separate admin account |
| `ProductionAdmissionGate` | Release-commit attestation + independent signed human review; default HOLD | Signed fixture and missing-control test | Actual provider proofs and human approval authority |

## 3. Critical implementation notes

### 3.1 Delegated authority

The signed capability is the portable authority token. It contains issuer, audience, subject, tenant, action, resource binding, delegated scopes/roles, one-time JTI, lifetime and MFA evidence. The receiver validates claims and signature before a local `AuthorizedRequest` is minted. That local ticket must never be serialized or treated as a portable credential.

The issuer and worker need independently configured trust keysets. The issuer's private signing key must remain in a managed signing boundary. Worker processes receive public keys only. Revocation and JTI consumption are atomic in shared state; local in-memory state is test-only.

### 3.2 SCIVE enforcement

`SCIVEPolicyBoundary.coverage_report()` inventories public methods and identifies unmapped or duplicate routes. `ChangeManager.propose_change()` now performs an internal authorizer check as well as approval/apply/verify/rollback/recovery checks. The boundary still is a facade, not runtime interception: production adapters must not expose raw methods.

### 3.3 Database and encrypted I/O

`SQLCipherStore` fails closed when the SQLCipher library is unavailable; ordinary SQLite is not an accepted downgrade. The KMS-wrapped DEK sidecar contains no plaintext key. WAL/temp/rekey settings and cross-process key initialization coordination are applied where supported. `EncryptedRecordSink` encrypts audit/log records before they reach the backend.

`EncryptedStreamFile` encrypts backup/temp streams with AES-256-GCM and authenticates tenant/object/purpose. Plaintext is committed to the approved transactional sink only after the final tag verifies. These adapters do not automatically encrypt arbitrary OS logs, crash dumps, swap, telemetry, CI artifacts or external backup agents. Every data path must be explicitly wired and independently checked.

### 3.4 Execution

The streaming supervisor drains pipes while storing only bounded output bytes. `stdout_bytes_seen`/`stderr_bytes_seen` count total stream volume; retained buffers obey configured caps. A signed `HostQuotaReceipt` is required before process creation. The actual quota mechanism is a host-level dependency; the runtime rejects missing/invalid receipts and does not pretend that measuring output after the fact enforces a filesystem limit.

### 3.5 WORM and admission

WORM writes use an outbox/receipt/reconciliation pattern. A local chain is not independently immutable. The production admission gate requires every control in `REQUIRED_PRODUCTION_CONTROLS`, a signed attestation for the exact release commit, and a separate signing key for an independent human reviewer. Missing evidence returns `HOLD`.

## 4. Security test results

The P2 hardening suite contains 25 executable test methods. The complete reference runtime suite on the current working tree passed **135 tests**, followed by the P0 quickstart (`verification=PASS`, 3 checks). These are local reference tests using injected/fake provider components; they are not live integration tests and do not establish production deployment.

Executed test categories include independent Ed25519 issuer/worker keysets, capability tampering, audience binding, replay, MFA and signed resource attributes; shared Redis adapter semantics and cross-tenant backend-resource reuse; OIDC provider discovery conformance; encrypted KMS context, SQLCipher fail-closed behavior, key sidecar and concurrent initialization; encrypted log backend and encrypted stream backup tamper/abort; bounded hostile output stream and host quota receipts; WORM receipt anchoring/reconciliation and test-only anchor rejection; SCIVE operation coverage, actor binding and internal change-proposal identity gate; independent production attestation and human review requirements.

## 5. Residual risks and explicit NOT_RUN items

- No real IdP is configured; provider-specific ACR/AMR semantics are unverified.
- No real KMS/HSM key or workload identity is configured.
- SQLCipher-capable deployment and live encrypted metadata/WAL are not proven by the local test environment.
- Actual gVisor/Kata execution, hostile workload containment and kernel escape tests are NOT_RUN.
- Real host filesystem quotas, disk exhaustion and worker failover are NOT_RUN.
- Real external WORM retention, legal hold and cross-account immutability are NOT_RUN.
- Dedicated cloud DB, tenant IAM, network and KMS policy isolation are NOT_RUN.
- Production-scale concurrent tenant stress, chaos/failover and restore tests are NOT_RUN.
- No production release, HTTP/MCP service, worker fleet, HA or disaster recovery is deployed.

## 6. Deployment admission

Production status remains `HOLD` until actual infrastructure controls are measured and attested against the exact release commit, the evidence is signed by a trusted infrastructure authority, and a distinct human security reviewer signs the required review scopes. A passed reference fixture does not satisfy this gate in a real deployment.
