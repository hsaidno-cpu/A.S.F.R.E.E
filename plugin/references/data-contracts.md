# A.S.F.R.E.E Canonical Data Contracts

The JSON Schemas under `schemas/` define versioned machine-readable contracts. They are design/validation contracts, not a deployed database, API, event bus, or persistent registry.

## Canonical epistemic labels

`DIRECT_OBSERVATION`, `USER_CLAIM`, `SOURCE_CLAIM`, `VERIFIED_SOURCE_CLAIM`, `ASSUMPTION`, `INFERENCE`, `HYPOTHESIS`, `PREDICTION`, `NORMATIVE_JUDGMENT`, `RECOMMENDATION`.

## Canonical status and severity vocabulary

- Finding status: `OPEN`, `CONFIRMED`, `HYPOTHESIS`, `DISPUTED`, `RESOLVED`, `ACCEPTED_LIMITATION`.
- Severity: `P0_CRITICAL`, `P1_HIGH`, `P2_MEDIUM`, `P3_LOW`, `UNASSESSED`.
- Confidence: `LOW`, `MEDIUM`, `HIGH`, `UNASSESSED`.
- Evidence strength: `E0`–`E5` as defined in `forensic-methods-and-limits.md`.
- Capability: `READY`, `READY_WITH_LIMITATIONS`, `NOT_CHECKED`, `UNAVAILABLE`, `ACCESS_DENIED`, `EXPIRED`, `BLOCKED`, `OUT_OF_SCOPE`.
- Recommendation: `PROPOSED`, `ACCEPTED`, `DEFERRED`, `REJECTED`, `NEEDS_DECISION`.
- Implementation: `NOT_STARTED`, `IMPLEMENTING`, `IMPLEMENTED`, `VERIFICATION_PENDING`.
- Verification: `NOT_RUN`, `PASS`, `FAIL`, `BLOCKED`, `UNVERIFIABLE`, `NOT_APPLICABLE`.
- Release: `NOT_RELEASED`, `RELEASE_APPROVED`, `PR_OPEN`, `MERGED`, `RELEASED`, `DEPLOYED`, `READ_BACK_CONFIRMED`.

Legacy mapping during migration: `P0/P1/P2/P3` map to the matching `P0_CRITICAL/P1_HIGH/P2_MEDIUM/P3_LOW`; `NOT_ASSESSED` maps to `UNASSESSED` only where the field means confidence, not where it means evaluation disposition. Do not silently map semantically different status fields.

## Core record relationships

- A case contains one or more targets and a declared intent/scope/authority.
- Sources and artifacts provide evidence; evidence supports or contradicts claims.
- Findings derive from claims/evidence and methods; causes remain hypotheses until substantiated.
- Recommendations map to findings and requirements.
- Change proposals map to recommendations, affected components, approval, tests, rollback, and residual risk.
- Test records contain observed results. Evaluation records judge their meaning and decision relevance.
- Route receipts disclose routing and observability. They do not prove a specialist agent executed unless `INVOKED` is supported.

## Required trace chain

`CLAIM → EVIDENCE → SOURCE/ARTIFACT → METHOD/OBSERVATION → CONTEXT/TIME → STATUS → ALLOWED_WORDING`.

Material graph edges should be typed: `SUPPORTS`, `CONTRADICTS`, `DERIVED_FROM`, `OBSERVES`, `DEPENDS_ON`, `CAUSAL_HYPOTHESIS`, `MITIGATES`, `VERIFIES`, `SUPERSEDES`. Mark each relationship as observed, documented, inferred, or hypothetical. A graph does not prove causation.

## Record requirements

Every material evidence item should carry an ID, source/artifact reference, type, locator, acquisition method, observation/claim, date/version where observed, scope, integrity checks actually performed, strength, limitations, and counterevidence. A finding should carry target, category, description, evidence refs, method, status, confidence, severity, likelihood only if justified, impact, root-cause hypotheses, and limitations. A change proposal should carry finding/requirement refs, scope/non-goals, proposed change, approval, tests, rollback, residual risks, and lifecycle status. A test record should distinguish expected from actual result and `NOT_RUN` from `PASS`.

## Stable IDs

Use case-local identifiers such as `CASE-`, `TARGET-`, `SRC-`, `CLM-`, `EVD-`, `MTH-`, `FND-`, `CAU-`, `RSK-`, `IMP-`, `REC-`, `REQ-`, `CHG-`, `TST-`, `DEF-`, `UNK-`, `VFY-`, `RCT-`, and `DEC-`. IDs are labels, not proof of persistent storage.

## Schema versioning

All contract changes must update schema version and compatibility notes. Prefer additive optional fields for minor revisions. Breaking field/enum changes require a major schema version and an explicit migration map. Reject or quarantine unknown enum values rather than guessing. Validate producer output and consumer input at handoff boundaries.


## RPEDS roadmap contracts

RPEDS contracts are defined under schemas/rpeds/: roadmap, milestone, iteration, progress measurement, adaptation decision, and risk. They are normative schemas/specifications, not a deployed roadmap service or persistent runtime database.

RPEDS/Notion canonical identifier families: ASRMAP- roadmap, ASRPH- phase, ASRMIL- milestone, ASRITR- iteration, ASRWRK- work item, ASREVL- evaluation/progress measurement, ASRDEC- adaptation decision, and ASRRSK- risk/blocker. IDs are stable references, not proof of persistence or execution. Producers and consumers must preserve the exact ID; do not silently translate to RPDS/RPM/RPI/RPV/RPD/RPR aliases. Keep revision and parent/child references explicit, and preserve superseded roadmap revisions rather than overwriting them.

A progress measurement must carry its indicator definition, method, unit/rubric, baseline, target, observed value only when measured, evidence refs, time/version, confidence and limitations. A missing or stale observation is not zero. Distinct measures must not be aggregated unless normalization, weight rationale, approval and O12 validity review are recorded.

RPEDS records preserve the trace chain OBJECTIVE → ROADMAP REVISION → PHASE → MILESTONE → WORK ITEM/ITERATION → TEST/EVALUATION EVIDENCE → ADAPTATION DECISION → NEXT REVISION. Typed dependency edges and observed/documented/inferred/hypothesis status remain explicit; the graph is not proof of causation.


## RPEDS schema inventory and evolution

The RPEDS contract set contains seven Draft 2020-12 JSON Schemas: roadmap, milestone, iteration, progress measurement, adaptation decision, risk, and work item. A schema version identifies the contract independently of the plugin SemVer. The initial contract baseline is 1.0.0; additive compatible fields may be introduced under the documented migration policy, while changed required fields, status semantics, or ID patterns require a new major schema version and explicit migration tests.

JSON Schema validates record shape and local state invariants. It cannot by itself prove cross-record referential integrity, ID uniqueness, dependency acyclicity, authorization validity, or real test execution. The executable RPEDS contract validator therefore checks schema meta-validity, positive/negative examples, duplicate IDs, dangling references and dependency cycles. Runtime and host-model behavioral tests remain separate gates.
