# Universal Tool Adapter Contract

The adapter catalogue may include parsers, source-control clients, SAST/DAST, dependency/SBOM scanners, secret scanners, dynamic test runners, fuzzers, API/MCP clients, containers/sandboxes, observability, and documentation tools. A catalogue entry is not proof that a tool is installed or available.

## Adapter manifest

```yaml
tool_id: scanner.static.example
tool_version: PINNED_VERSION
adapter_version: 1.0.0
capabilities: [static_analysis, vulnerability_detection]
input_schema: contracts/tool-input.schema.json
output_schema: contracts/tool-output.schema.json
permissions:
  filesystem: read_only
  network: disabled_by_default
  credential_access: denied_by_default
execution:
  timeout_seconds: 120
  retry_limit: 1
  idempotent: true
  sandbox_required: true
trust:
  source: approved_tool_registry
  verification: required
status: REGISTERED
```

`REGISTERED` is declarative. Runtime readiness must be checked immediately before operation.

## Readiness record

Record capability ID, exact operation, provider/tool and version, identity/scope if visible (never secret values), permission, environment, status (`READY`, `READY_WITH_LIMITATIONS`, `NOT_CHECKED`, `UNAVAILABLE`, `ACCESS_DENIED`, `EXPIRED`, `BLOCKED`, `OUT_OF_SCOPE`), evidence of check, constraints, and approved fallback.

## Execution policy

Validate inputs against schema; use allowlists; redact secrets; enforce timeouts, bounded retries, and resource limits; use sandbox/egress policy where available; capture exit status/stdout/stderr/log refs only when actually available; preserve tool/version/environment metadata; normalize results; state limitations and false-positive caveats.

Use provider-neutral, versioned contracts. Never hardcode secrets. Never imply a connector has filesystem, local runtime, shell, network, or write access unless its exposed contract says so.
