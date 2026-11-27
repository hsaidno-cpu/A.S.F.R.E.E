---
name: rpeds-adaptive-functional-situational-adapter
description: Use before applying shared PRE–RPEDS roadmap capabilities in A.S.F.R.E.E when an incoming release, method, recommendation, or contribution must be checked against A.S.F.R.E.E SOP, authority, security, privacy, data boundaries, runtime limits, or retained RPEDS-specific behavior.
---

# RPEDS Adaptive Functional Situational Adapter (AFSA)

## Mission

Adapt the application of the shared PRE–RPEDS DNA kernel to the verified A.S.F.R.E.E case and host context. Preserve canonical shared roadmap semantics while retaining RPEDS's native A.S.F.R.E.E identity, four modules, procedures, M00 handoff and O01–O12 authority boundaries.

AFSA is a host-policy and functional-compatibility control. It is not a second roadmap engine, a replacement for RPEDS, a permission grant, an SOP rewrite tool, or an automatic approval mechanism.

## When mandatory

Apply this procedure before:
- using a newly released shared-core capability or applying it to an A.S.F.R.E.E/RPEDS workflow;
- changing how an RPEDS-native module consumes a new PRE capability;
- accepting a capability-learning contribution from A.S.F.R.E.E into the shared kernel;
- changing roadmap data flows, authority, permissions, retention, tools, approvals, or gate semantics;
- resolving an apparent conflict between a PRE core update and A.S.F.R.E.E SOP or established behavior.

Routine use of an unchanged, previously accepted capability may reuse its last valid AFSA profile and receipt only while the host policy version and capability digest remain unchanged.

## Required input envelope

Resolve and record:
- host identity: `asfree-rpeds`, A.S.F.R.E.E package version, source commit and environment;
- shared DNA identity: `pre-rpeds-shared-roadmap-dna`, PRE release, capability ID/version, contract version and content digest;
- RPEDS adapter version and affected native module(s);
- applicable A.S.F.R.E.E SOP/policy references and effective version/date;
- M00 decision owner/delegation, O11 controls and approvals required;
- data classification, permitted/prohibited data flow, retention and privacy boundary;
- available host tools/runtime, audit sink, required tests and rollback target;
- source provenance, origin lineage, reuse/license basis and prior adoption receipts.

Unknown facts remain `UNKNOWN`. Never infer authority, tools, policy, approval, license or compatibility from a skill name or prior narrative.

## Authority precedence

Apply this order:
1. Applicable law, binding platform constraints and non-waivable security/privacy requirements.
2. A.S.F.R.E.E approved SOP, policy, access controls and data-protection rules.
3. M00 case scope, decision rights and authorized delegation.
4. O11 security/authorization/privacy controls and designated approvals.
5. Shared PRE–RPEDS core contracts and capability behavior.
6. Convenience, speed or local preference.

A lower layer cannot weaken a higher one. AFSA may create a deterministic host adapter where permitted; it must not silently modify A.S.F.R.E.E SOP or lower shared-core acceptance criteria.

## Classification of incoming changes

Classify each capability separately:
- `SHARED_DNA`: host-neutral roadmap capability, contract or method intended for the common kernel.
- `HOST_ADAPTATION`: shared capability requiring an explicit A.S.F.R.E.E mapping or controlled implementation.
- `RPEDS_NATIVE_EXTENSION`: unique A.S.F.R.E.E roadmap behavior that remains owned by RPEDS.
- `HOST_SPECIFIC`: A.S.F.R.E.E policy, private case context, identity, permission, credential or non-exportable operational data.
- `QUARANTINED_OR_REJECTED`: untrusted, unsafe, unlicensed, provenance-deficient, contradictory or non-waivable incompatible material.

Only sanitized, validated `SHARED_DNA` may enter a common release. `HOST_ADAPTATION` requires a target adapter and host review. `RPEDS_NATIVE_EXTENSION` is preserved, not overwritten by a similar PRE feature. `HOST_SPECIFIC` never propagates as shared DNA.

## Compatibility dispositions

Return exactly one primary disposition:
- `DIRECT_COMPATIBLE`: contracts, policy, authority and capability requirements are verified; no adaptation is required.
- `ADAPTED_COMPATIBLE`: a versioned deterministic adapter preserves shared semantics and satisfies A.S.F.R.E.E SOP; required approval is recorded.
- `HELD_FOR_AUTHORITY`: policy meaning, approval, permission, owner decision or evidence is missing.
- `QUARANTINED_OR_REJECTED`: integrity/provenance fails, reuse basis is absent, data transfer is prohibited, or the change conflicts with a non-waivable control.

Unknown is not compatible. A held or quarantined change does not block unrelated, already-compatible shared capabilities.

## RPEDS native preservation map

| RPEDS-native module | Shared-kernel relationship | A.S.F.R.E.E-specific behavior to preserve |
|---|---|---|
| Roadmap Architecture Planner | Maps to shared objective/phase/milestone/work-item model | Case-derived decomposition and M00 handoff |
| Progressive Development Manager | Uses common iteration/progress/audit semantics | A.S.F.R.E.E work-state coordination and engineering handoff |
| Continuous Evaluation Engine | Uses common indicator/evidence/checkpoint contracts | Prepares local evidence/checkpoints; O12 retains evaluation judgment |
| Adaptive Roadmap Optimizer | Uses common adaptation alternatives and next-action intelligence | Host-aware replan proposal using O03–O06/O11/O12 inputs when triggered |

Do not remove, rename or silently collapse these modules. PRE Standalone remains a separate first-class manifestation. RPEDS remains the A.S.F.R.E.E-native manifestation under M00.

## Decision procedure

1. Verify the envelope, source, digest, release lineage and reuse/license basis.
2. Establish current A.S.F.R.E.E case, SOP version, M00 authority and affected RPEDS module.
3. Identify the semantic delta: additive, corrective, breaking, host adaptation, or host extension.
4. Map data, tools, side effects, permissions and authority to the host profile.
5. Assess backward compatibility, regressions, dependency changes, risk, reversibility and rollback.
6. Select the disposition and cite policy/evidence references.
7. Route security/privacy/permission changes to O11; evaluation-method/judgment changes to O12; actual tests/verification to O10; runtime use to O09; accepted reconstruction/remediation to O08/O07; final case arbitration stays with M00.
8. Run required regression/non-regression checks. A plan is not a test result.
9. Record a per-release host receipt with previous/candidate version, digest, adapter version, policy refs, disposition, tests, approvals, PR/commit/deployment, exact read-back and rollback reference.
10. Mark `VERIFIED` only when read-back version/digest match and every required test/approval passes.

## Safe synchronization rules

- An authenticated release event is not a host adoption.
- Automatic queueing is eligible only when the event is explicitly non-breaking, every capability class is `SHARED_DNA`, the host policy profile is verified, and an approved host policy explicitly enables auto-adoption.
- Any event containing `HOST_ADAPTATION`, `RPEDS_NATIVE_EXTENSION`, `HOST_SPECIFIC`, or unknown classifications is held for review.
- Authority, identity, security, privacy, licensing, permissions, data-flow, required approval, breaking-schema, major-version and irreversible changes require a host gate.
- Keep idempotency keys, origin lineage, previous version and rollback reference; never overwrite an existing receipt or erase prior revision history.
- A host adoption failure must not republish the same capability as a new origin. Record failure and bounded retry/dead-letter state.

## Output contract

Return host/profile version; PRE–RPEDS release and digest; affected modules; classified capabilities; SOP/policy refs; authority/approval needs; risk and data-flow delta; disposition; adapter decision; regression evidence; adoption state; target read-back; rollback reference; residual risk and next owner.

## Stop conditions

Stop or hold when source identity/digest is unverified, license/reuse basis is unclear, authority or policy profile is missing, non-waivable controls conflict, prohibited data would cross a host boundary, required tests fail/not run, rollback is unavailable for a consequential update, or target read-back does not match.

Never claim a distinct AFSA invocation unless the host confirms it. Where only this procedure is applied, record `PROCEDURE_APPLIED`.
