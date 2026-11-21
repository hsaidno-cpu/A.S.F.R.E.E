# Ecosystem Identity, Version, Migration & Deprecation Policy

**Status:** normative governance contract  
**Owner:** A.S.F.R.E.E canonical repository maintainers  
**Registry:** [Ecosystem Identity Registry](ecosystem-identity-registry.json)

## 1. Purpose and authority

This policy prevents identity collisions, competing version authorities, duplicated orchestrators, and unsafe migration across the A.S.F.R.E.E ecosystem.

The ecosystem registry is the authoritative catalog of product identities, Plugin Creator IDs, plugin roles, version sources, history sources, and compatibility destinations. A product may have multiple plugin packages only when each has a unique registered identity and a declared role. Each product must have exactly one plugin with role `CANONICAL`.

A display name, package name, repository URL, plugin URL, or copied description is not a substitute for the immutable Plugin Creator `plugin_id`. Never create a second plugin to represent the same product role without an approved registry change.

## 2. Identity invariants

1. Every product has a stable `product_id`.
2. Every plugin has one stable `identity_id`, one unique Plugin Creator `plugin_id`, one package name, and one registry role.
3. Every product has exactly one `CANONICAL` plugin.
4. A `COMPATIBILITY_REDIRECT` must point to exactly one canonical plugin in the same product.
5. An `INDEPENDENT_PLUGIN` must have a distinct purpose, owner, lifecycle, version source, history source, and acceptance boundary. It must not duplicate the canonical orchestrator.
6. A plugin ID must never be reassigned to another product or recreated under a different name to evade history.
7. Renaming or replacing an identity requires an explicit migration record; old IDs remain historical and are not recycled.

## 3. Version authority

### Canonical product package

- The canonical package SemVer is the `version` field in the single registered source manifest, currently `plugin/plugin.json#/version`.
- The active version is the value from a reviewed commit merged into the registered default branch (`main` for A.S.F.R.E.E).
- A local working copy, feature branch, release candidate, pull request, or uploaded ZIP is not an active release.
- The compatibility manifest and package README mirror the canonical manifest. They may be validated copies, but they never become separate authorities.
- The Plugin Creator deployment is a released platform artifact. Its version and file read-back must be reconciled with the reviewed source commit after deployment. A successful upload alone is not synchronization.

### Other version planes

- A redirect plugin has its own version line because its redirect package can change independently. That version identifies only the redirect shell.
- Runtime packages and source bundles have their own version authority and integrity record. They must not be forced to match the plugin package SemVer.
- Schema contracts have their own schema versions and explicit migration rules.

Do not copy the canonical product version into legacy instructions or metadata. Resolve the canonical destination using its stable identity and resolve its active version from the registered source manifest.

## 4. Change history and provenance

Every canonical source change must be recorded in Git history and the repository `CHANGELOG.md`. Each deployed Plugin Creator release must retain its platform release ID and be verified by metadata and file read-back against the source commit.

Every independent plugin maintains its own changelog and platform release history. A compatibility redirect maintains only its redirect-shell history. Never merge the changelogs of a redirect and canonical product into one ambiguous version stream.

For every release record, preserve where available:
- `product_id`, `identity_id`, immutable plugin ID and package name;
- package SemVer and source commit SHA;
- pull request and CI run/check result for the exact commit;
- Plugin Creator release ID and observed deployed version;
- read-back verification result and timestamp;
- approval/review status, migration impact, rollback target, and known limitations.

If a value was not observed, record it as unknown or not recorded. Never reconstruct missing release provenance by guessing.

## 5. Migration protocol

Migration is a controlled transition, not a copy-and-paste of files under a new name.

1. **Inventory:** identify old plugin ID, package/version, repository/ref, manifests, skills, schemas, data, consumers, dependencies, permissions, and history.
2. **Freeze:** stop adding new product behavior to the superseded package. Preserve its last known-good release and source snapshot.
3. **Map:** create a one-to-one mapping from each retained legacy capability, schema, identity and status to its canonical destination. Mark removed, ambiguous, unsupported, or unknown items explicitly.
4. **Preserve provenance:** retain original source, timestamp, version, ownership, and integrity metadata where known. A copied claim is not a verified observation.
5. **Transform:** apply only documented schema and enum migrations. Prefer additive changes. Breaking changes require a new major schema version and an explicit migration map.
6. **Quarantine ambiguity:** unknown enum values, conflicting identities, invalid references, and lossy conversions must be rejected or quarantined. Never silently coerce them into a nearby value.
7. **Validate:** test schema validity, referential integrity, routing, permissions, behavior, compatibility and rollback against the declared migration acceptance cases.
8. **Switch:** route new work exclusively to the canonical identity after the required review and release gates pass.
9. **Retain compatibility:** keep a narrow redirect or adapter only while it serves a supported consumer. It must not own business logic, state, or a second release authority.
10. **Close:** record migrated scope, exclusions, unresolved unknowns, evidence, reviewer, decision, and the recovery point.

### Conversation and user-state boundary

A plugin redirect cannot automatically move ChatGPT conversation history, user memory, files, active sessions, or external persisted case state. Users must open the canonical plugin and manually carry forward the relevant task intent, authorized scope, decisions, evidence references, and required files. Preserve provenance and do not transfer secrets or credentials.

### Status migration

Use the canonical mappings in `data-contracts.md`. Map only semantically equivalent values. In particular, a legacy `NOT_ASSESSED` value may map to `UNASSESSED` only when the target field means confidence; it must not be coerced into an evaluation disposition. Unknown values remain unknown or quarantined.

## 6. Redirect, deprecation and retirement

A redirect has a deliberately small contract:
- identify its superseded state;
- resolve one canonical destination;
- explain manual migration limits;
- stop if that destination is unavailable.

It must not re-enable the old orchestrator, run both implementations, duplicate specialist instructions, or fall back to stale code. Canonical unavailability is a blocker, not permission to revive an obsolete authority.

No fallback to superseded behavior is permitted when the canonical destination or a required migration mapping is unavailable. Stop and report the blocker.

A redirect may be retired only after:
1. all known supported consumers have a documented migration path;
2. migration notices and destination references have been maintained;
3. evidence supports that the compatibility route is no longer needed;
4. historical releases, source, changelog and provenance remain recoverable;
5. a human owner approves retirement and the decision is recorded.

Do not automatically delete old plugin identities, historical releases, audit evidence, or source history. Retirement changes lifecycle state; it does not erase identity history.

## 7. Enforcement

The static package validator must reject:
- duplicate product IDs, plugin identity IDs, plugin IDs, or plugin names;
- more than one canonical plugin per product;
- missing or invalid redirect targets;
- absent version or history sources;
- drift between source manifest, compatibility manifest, and package README;
- a release-candidate branch being represented as an active release;
- missing migration/deprecation policy or unregistered compatibility roles.

The registry is a governance catalog, not a deployed service or an automatic migration engine. Enforcement is only as strong as the validator, CI rules, review requirements, and release process that actually execute it.
