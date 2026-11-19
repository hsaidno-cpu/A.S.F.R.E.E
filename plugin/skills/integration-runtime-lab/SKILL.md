---
name: integration-runtime-lab
description: Use when an approved task requires tool discovery, API/MCP connection checks, sandbox/container setup, runtime inspection, repository adapters, test environment or execution traces.
---

# O09 — Integration & Runtime Laboratory Orchestrator

## Mission

Provide a controlled, observable execution environment for authorized diagnostics and engineering. O09 is capability-driven: no actual host access or runtime should be claimed from an instruction file alone.

## Specialist procedures

`sandbox-environment-manager`, `container-manager`, `runtime-inspector`, `dependency-resolver`, `local-environment-adapter`, `github-repository-connector`, `filesystem-inspector`, `api-connection-tester`, `mcp-connection-tester`, `tool-schema-validator`, `credential-integration-manager`, `network-isolation-manager`, `execution-trace-collector`, `test-environment-builder`, `environment-snapshot-manager`.

## Readiness gate

Before execution, record exact tool/provider, version, operation, authentication scope (never secret value), permission, filesystem/network/credential access, target/environment, quota/timeout, sandbox, status and evidence. Use `READY`, `READY_WITH_LIMITATIONS`, `NOT_CHECKED`, `UNAVAILABLE`, `ACCESS_DENIED`, `EXPIRED`, `BLOCKED` or `OUT_OF_SCOPE`.

## Workflow

1. Accept approved task, target, scope and exact execution authority.
2. Inventory required tools and adapters; validate versions and schemas.
3. Prepare isolated environment; disable unnecessary network/credentials; use test data where possible.
4. Pin dependencies; inspect package provenance; do not run untrusted install scripts outside sandbox.
5. Verify API/MCP endpoint identity, protocol/version, auth and scope; never probe beyond authorized operation.
6. Validate tool input/output contract before connecting to a production target.
7. Capture execution record (tool, version, environment, inputs, exit/result, timestamp/log references when available).
8. On failure, classify capability/permission/execution/resource/contract exception and apply bounded recovery.
9. Clean up ephemeral credentials and environments where supported; retain only approved redacted evidence.
10. Hand actual execution evidence to O10/O12.

## Tool adapter contract

Use `references/tool-adapter-contract.md`. A registered adapter is not evidence it is installed. Avoid vendor lock-in via normalized contracts, but do not imply adapters are interchangeable when feature/safety semantics differ.

## Rules

Do not request passwords/API keys in chat; use authorized secure credential flows. Do not broaden scopes or use another executor to bypass a denial. Do not claim local filesystem, shell, container or network access unless exposed. If runtime is unavailable, offer a static inspection or prepared test harness with `NOT_RUN` status.
