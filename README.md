# A.S.F.R.E.E

**AI Systems Forensics & Reconstruction Evaluation Engine**

Universal-by-design · Evidence-driven · Supervised engineering

A.S.F.R.E.E is a modular intelligence system for authorized forensic analysis, architecture decomposition, evaluation, diagnosis, controlled remediation, reconstruction and independent verification of AI/software systems.

## Current unified baseline

- **Canonical plugin package:** v0.2.1 in [`plugin/`](plugin/).
- **Architecture:** one M00 master orchestrator and twelve specialist skills O01–O12.
- **Contracts:** 16 JSON Schemas covering case, target, source, claim, evidence, findings, methods, requirements, changes, tests, evaluation, capability readiness, routing, audit events and release disposition.
- **Acceptance fixtures:** 30 deduplicated declarative cases.
- **Runtime platform:** not yet implemented or deployment-verified.
- **Cloud/API/MCP services:** not included in this skills-only package.

## Architecture at a glance

- **M00:** intent, scope, capability readiness, routing, arbitration and final synthesis.
- **O01–O10:** artifact intelligence; anatomy; positive and negative intelligence; comparison; bug diagnosis; remediation; reconstruction; integration/runtime; validation/QA.
- **O11:** Security & Governance cross-cutting authority.
- **O12:** Evaluation Intelligence cross-cutting control plane.

Evaluation operates before, during and after the work. Read-only is the default; engineering changes are separately authorized and independently verified. Operating modes, forensic depth L0–L6, and authority levels S0–S5 govern how far a workflow may proceed.

## Repository layout

```text
.
├── plugin/                 # Canonical importable skills-only package v0.2.1
│   ├── plugin.json
│   ├── .codex-plugin/
│   ├── LICENSE
│   ├── TRADEMARKS.md
│   ├── skills/              # M00 + O01–O12
│   ├── references/          # architecture, contracts, schemas and controls
│   └── tests/               # 30 declarative acceptance fixtures
├── docs/                    # project-level architecture and policy
├── scripts/                 # deterministic static package validation
├── tests/                   # repository-level acceptance fixtures
└── .github/workflows/       # static validation CI
```

## Use the plugin source

The `plugin/` directory is the standalone package root. Its skills are reusable instruction units; the package does not itself provision a scanner, local shell, container sandbox, API gateway, MCP server, database, telemetry or cloud runtime. Real capabilities must be connected and checked in the host environment. Unavailable or denied capabilities remain explicitly blocked/not run.

## Validation status

The package source and manifests have been read back; all 16 JSON Schema files parse as JSON and the 30 acceptance case identifiers are unique. These are static package checks, not runtime acceptance-test results. Runtime tests and MCP/API adapter deployments remain unimplemented.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the license before submitting changes. Contributions must preserve traceability, add acceptance cases for material behavior changes, and never include secrets or unauthorized target data.

## License & brand

This repository's current source baseline uses **PolyForm Noncommercial License 1.0.0** (source-available, noncommercial; not an OSI-approved open-source license). Commercial use by third parties requires separate written permission from the rights holder. The A.S.F.R.E.E name and visual identity are separate from the software license; see [`TRADEMARKS.md`](TRADEMARKS.md) and [`LICENSE-STRATEGY.md`](LICENSE-STRATEGY.md).

**Historical notice:** the initial repository commit contained an Apache-2.0 license. A later license change does not automatically revoke license grants made for earlier snapshots. Obtain qualified legal review before commercial distribution, contributor onboarding or foundation transfer.
