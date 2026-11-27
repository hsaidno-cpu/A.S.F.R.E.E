---
name: pre-adaptive-functional-situational-adapter
description: Use before applying PRE Core capabilities inside A.S.F.R.E.E or when a roadmap method or release may conflict with A.S.F.R.E.E SOP, M00 authority, O11 security/privacy, O12 evaluation, O10 verification, O09 runtime or data boundaries.
---

# PRE Host Adapter — A.S.F.R.E.E Situational Profile

## Mission

Map the shared PRE Core capability to the verified A.S.F.R.E.E situation while preserving the host's SOP, authority model and canonical PRE semantics. This is the A.S.F.R.E.E implementation profile for PRE's generic `adaptive-functional-situational-adapter`.

## Mandatory order

1. Resolve the active A.S.F.R.E.E package version, source commit, PRE release, capability/contract version and artifact digest.
2. Resolve current host policy/SOP version, case scope and M00 decision authority.
3. Determine whether the capability touches O11 security/authorization/privacy, O12 evaluation judgment, O10 tests/verification, O09 runtime, or O07/O08 engineering. Preserve those owners.
4. Classify each item as `SHARED_CAPABILITY`, `HOST_ADAPTATION`, `HOST_SPECIFIC` or `QUARANTINED_OR_REJECTED`.
5. Compare the required behavior with A.S.F.R.E.E controls and current runtime capabilities.
6. Return one disposition: `DIRECT_COMPATIBLE`, `ADAPTED_COMPATIBLE`, `HELD_FOR_AUTHORITY` or `QUARANTINED_OR_REJECTED`.
7. Record tests, policy references, rollback and host adoption receipt.

## Host authority precedence

Applicable law and platform constraints → A.S.F.R.E.E approved SOP/security/privacy → M00 case scope and authorized delegation → PRE Core shared capability → convenience. PRE cannot change the A.S.F.R.E.E role model. M00 cannot grant itself authority. O11 must approve sensitive access/policy changes; O12 remains independent of PRE; O10 supplies actual test/verification evidence; O09 must verify supported runtime capability.

## RPEDS compatibility rule

`RPEDS` is the A.S.F.R.E.E name/adapter for the single canonical `progressive-roadmap-evaluator` PRE Core. Existing RPEDS docs, schemas and module names are compatibility references. They must not create a parallel roadmap state, release lineage or second case coordinator. Route through M00 to PRE Core once; do not invoke both the RPEDS alias and the canonical PRE destination separately.

## Disposition rules

- `DIRECT_COMPATIBLE`: all source, policy, authority, contract and capability prerequisites are verified.
- `ADAPTED_COMPATIBLE`: a versioned and approved adapter preserves the shared semantics and local SOP.
- `HELD_FOR_AUTHORITY`: policy interpretation, security review or decision-owner approval is missing.
- `QUARANTINED_OR_REJECTED`: digest/provenance fails, license is not established, data transfer is prohibited, or the proposal conflicts with non-waivable controls.

Do not automatically rewrite an A.S.F.R.E.E SOP to fit a PRE upgrade. Never promote an unknown or unauthorized behavior to PASS.

## Output

Host profile/version; PRE source/version/digest/contract; mapped capabilities; policy references; conflicts; adaptation; disposition; approval reference; actual regression evidence; rollback version; adoption receipt; residual risks.
