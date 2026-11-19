# A.S.F.R.E.E

**AI Systems Forensics & Reconstruction Evaluation Engine**

Universal-by-design · Evidence-driven · Supervised engineering

A.S.F.R.E.E is a modular intelligence system for authorized forensic analysis, architecture decomposition, evaluation, diagnosis, controlled remediation, reconstruction and independent verification of AI/software systems.

## Project status

- **Architecture baseline:** established.
- **Master orchestrator package:** v1.0.0 prepared in [`plugin/`](plugin/).
- **Runtime platform:** not yet implemented or deployment-verified.
- **Cloud/API/MCP services:** not included in this skills-only package.

## Architecture at a glance

- **M00:** intent, scope, capability readiness, routing, arbitration and final synthesis.
- **O01–O10:** artifact intelligence; anatomy; positive and negative intelligence; comparison; bug diagnosis; remediation; reconstruction; integration/runtime; validation/QA.
- **O11:** Security & Governance cross-cutting authority.
- **O12:** Evaluation Intelligence cross-cutting control plane.

Evaluation operates before, during and after the work. The four transformation engines (Positive, Negative, Comparative, Conversion & Solution) share one evidence/contract architecture. Read-only is the default; engineering changes are separately authorized and independently verified.

## Repository layout

```text
.
├── plugin/                 # Importable skills-only plugin package
│   ├── plugin.json
│   ├── LICENSE
│   ├── skills/              # M00 + O01–O12
│   ├── references/          # shared contracts and control rules
│   └── tests/               # declarative acceptance fixtures
├── docs/                    # project-level architecture and policy
├── scripts/                 # deterministic static package validation
├── tests/                   # repository-level acceptance fixtures
└── .github/workflows/       # static validation CI
```

## Use the plugin source

The `plugin/` directory is the standalone package root. Its skills are reusable instruction units; the package does not itself provision a scanner, local shell, container sandbox, API gateway, MCP server, database, telemetry or cloud runtime. Real capabilities must be connected and checked in the host environment. Unavailable or denied capabilities remain explicitly blocked/not run.

## Initial implementation priorities

1. Evidence management, finding/evaluation contracts and M00 routing.
2. O01/O02 and O03/O04 for evidence-backed forensic evaluation.
3. O05/O06 for comparison and diagnosis.
4. O11 security/authorization controls from the first phase.
5. O07–O10 for supervised engineering, runtime integration and independent verification.
6. O12 outcome/impact and meta-evaluation across the lifecycle.
7. API/MCP adapters and deployment infrastructure only after contracts and security controls are validated.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and the license before submitting changes. Contributions must preserve traceability, add acceptance cases for material behavior changes, and never include secrets or unauthorized target data.

## License & brand

This repository's new source baseline uses **PolyForm Noncommercial License 1.0.0** (source-available, noncommercial; not an OSI-approved open-source license). Commercial use by third parties requires separate written permission from the rights holder. The A.S.F.R.E.E name and visual identity are separate from the software license; see [`TRADEMARKS.md`](TRADEMARKS.md) and [`LICENSE-STRATEGY.md`](LICENSE-STRATEGY.md).

**Historical notice:** the initial repository commit contained an Apache-2.0 license. A later license change does not automatically revoke license grants made for earlier snapshots. Obtain qualified legal review before commercial distribution, contributor onboarding or foundation transfer.
