# A.S.F.R.E.E Unified Merge Lineage

## Canonical identity

The canonical account plugin is `asfree` (`plugins_6aff3f4ff7d48191a411f6efb0cc435a`). The `asfree-master-orchestrator` package supplied the earlier operational specification and remains a recoverable historical baseline. It is not a second source of truth for new development.

## Merge decisions

| Component | Canonical source / decision | Treatment |
|---|---|---|
| Product identity | `asfree` | Preserved as plugin identity |
| M00 + specialist registry | `asfree` O01–O12 architecture | Retained and strengthened with mode, depth, authority, and routing controls from the master package |
| Specialist skills | `asfree` O01–O12 skill units | Retained as canonical; no artificial proliferation of agents |
| Eight architectural layers | Both packages | Consolidated in one architecture reference |
| Operating modes | `asfree-master-orchestrator` | Imported into canonical M00 |
| S0–S5 authority | `asfree-master-orchestrator` | Imported into M00 and security reference |
| Evaluation control plane | Both packages | Unified with E0–E7 lifecycle and explicit O10/O11/O12 ownership boundaries |
| Data contracts | `asfree` | Made canonical; aliases and migration rules documented |
| JSON Schemas | `asfree` five schemas | Corrected and expanded to cover case, target, source, claim, method, requirement, test, capability readiness, change impact, audit event, and release disposition |
| Forensic methods/limits | `asfree-master-orchestrator` | Imported |
| Lifecycle/recovery | `asfree-master-orchestrator` | Imported and normalized to canonical status vocabulary |
| Tool adapter contract | `asfree-master-orchestrator` | Imported as a declarative contract, not an implemented adapter claim |
| Security/authority | Both packages | Consolidated with trust boundaries, action classes, approvals, and authority levels |
| Acceptance tests | Both packages | Semantic duplicates merged; 30 unique declarative cases retained/added |
| Packaging/legal | `asfree-master-orchestrator` | LICENSE, README and trademark notice added; manifest synchronized |

## Status of this merge

The plugin source update and file read-back are verified. JSON manifests and schemas were parsed/validated in the package workspace before upload; required paths and release metadata were checked after upload. The acceptance cases are declarative fixtures and have **not** been executed in a runtime test harness. No scanner, MCP server, API gateway, database, sandbox, CI service, or execution backend was deployed by this merge.

## Migration policy

- Treat `asfree` as the only canonical development target.
- Do not add new behavior to the legacy package.
- Recover prior content from its historical release if required.
- Migrate legacy status enums only through the documented map in `data-contracts.md`; do not silently coerce semantically different values.
- Keep plugin identity and repository lineage explicit. Do not infer that the repository's legal ownership has transferred to a future foundation until the relevant legal assignment is completed.


## Ecosystem identity registry

The authoritative A.S.F.R.E.E ecosystem identity record is `plugin/references/ecosystem-identity-registry.json`. It registers canonical plugin ID `plugins_6aff3f4ff7d48191a411f6efb0cc435a` and legacy redirect ID `plugins_6aff3ad51a408191a8d49b1c6003195b` as distinct package identities with distinct roles. The canonical product is represented only by the `asfree` plugin; the legacy package is `COMPATIBILITY_REDIRECT`, not a second product implementation.

The legacy redirect has its own shell version line, changelog, and Plugin Creator release history. Its version must never be compared numerically with or substituted for the canonical package SemVer. Canonical package changes belong in the repository manifest, Git history and root changelog; app deployment IDs are separately recorded as read-back evidence.

See `plugin/references/migration-and-deprecation-policy.md` for the normative migration and retirement protocol.
