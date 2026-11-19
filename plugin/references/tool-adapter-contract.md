# Universal Tool Adapter Contract

A.S.F.R.E.E may integrate parsers, source-control clients, SAST/DAST, dependency/SBOM scanners, secret scanners, dynamic test runners, fuzzers, API/MCP clients, containers/sandboxes, observability, and documentation tools. The list is a capability catalogue, not a declaration that any tool is installed.

## Adapter manifest

```yaml
tool_id: scanner.static.example
tool_version: "PINNED_VERSION"
adapter_version: "1.0.0"
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

`REGISTERED` is declarative only. Runtime readiness must be checked immediately before use.

## Readiness record

Record capability ID, exact operation, provider/tool and version, authentication/scope if visible (never reveal secret values), permission, environment, status (`READY`, `READY_WITH_LIMITATIONS`, `NOT_CHECKED`, `UNAVAILABLE`, `ACCESS_DENIED`, `EXPIRED`, `BLOCKED`, `OUT_OF_SCOPE`), evidence of check, constraints, and approved fallback.

## Execution policy

Validate inputs against schema; apply allowlists; redact secrets; enforce timeout, bounded retry and resource limits; use sandbox/egress policy where available; capture exit status/stdout/stderr/log refs only when actually available; preserve tool/version/environment metadata; normalize results; and include limitations/false-positive caveats.

Use provider-neutral adapters and versioned contracts. Never hardcode secrets. Never imply a connector has filesystem, local runtime, shell, network or write access unless its exposed contract says so.
