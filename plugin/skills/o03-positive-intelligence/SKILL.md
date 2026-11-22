---
name: o03-positive-intelligence
description: Use when the user needs a balanced assessment of strengths, verified capabilities, feature value, innovation, differentiation, reusable patterns, or value preservation.
---

# Positive Intelligence Orchestrator

## Mission
Discover, verify, and evaluate strengths and realized value so reconstruction does not destroy what already works.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`strength-analyzer;capability-analyzer;feature-value-analyzer;functional-excellence-analyzer;architecture-quality-analyzer;innovation-analyzer;efficiency-analyzer;scalability-potential-analyzer;reusability-analyzer;interoperability-analyzer;differentiation-analyzer;optimization-opportunity-analyzer`

The names above are functional capability labels, not a claim that separate software modules or agents have been deployed. Activate only relevant capabilities.

## Trigger contract

**Required trigger**
- A planned roadmap change could remove, regress, degrade or alter an evidenced capability/behavior.
- The decision explicitly asks what is valuable, distinctive, reusable or worth preserving.
- Existing user benefit, compatibility or behavior must become acceptance constraints for refactoring, migration, replacement or re-sequencing.
- An enhancement decision depends on whether existing value is realized or only potential.

**Do not trigger**
- To generate praise, force positive/negative symmetry, or produce a feature list with no value question.
- To present untested features, roadmap promises or speculative opportunities as realized value.
- For inventory (O01), structural decomposition (O02), risk analysis (O04), option comparison (O05) or defect diagnosis (O06) when no preservation question exists.

## Minimum inputs

Decision/objective; target/version; current and proposed scope; affected users/stakeholders; artifacts/provenance; operating context; protected behavior/constraints; and the exact change whose impact on value is at issue. List missing information.

## Operating procedure

1. **Frame the value claim:** connect each strength to an objective, stakeholder need or outcome; define context and disconfirming evidence.
2. **Acquire traceable evidence:** source/artifact, version, locator, date, environment, method, inspection depth and limitations. Prefer direct observation, executed tests, quality measures and corroborated usage over promotional claims.
3. **Classify realization:** `REALIZED`, `POTENTIAL`, `UNVERIFIED`, `SUPERSEDED` or `NOT_ASSESSED`. Separate working behavior from roadmap intent, prototype and assertion.
4. **Assess value mechanism:** who benefits, what changes, under which conditions, how repeatably, and which dependencies/costs enable it. Do not infer adoption, ROI, speed, quality or uniqueness without evidence.
5. **Test durability/distinctiveness:** assess reliability, maintainability, interoperability, accessibility, compatibility, scalability and dependencies only when relevant; compare to a valid baseline before claiming differentiation.
6. **Identify preservation invariants:** exact behavior, interfaces, data semantics, user journeys, quality thresholds, contracts and compatibility that must not regress. Separate hard invariants from negotiable value.
7. **Choose justified action:** `PRESERVE`, `AMPLIFY`, `REPLICATE`, `LEVERAGE`, `INTEGRATE`, `EXTEND` or `STANDARDIZE`; state prerequisites and trade-offs.
8. **Define proof:** translate important value claims into observable acceptance criteria and regression checks for O10. Without a valid oracle/baseline, mark preservation unresolved or unverifiable.
9. **Hand off:** send evidence, counterevidence and constraints to M00; use O05 only when real alternatives exist and O06 for a reproduced regression.

## Required output contract

For each material finding provide: `finding_id`; claim and linked objective/stakeholder; affected capability/component/behavior/version; realization state; evidence IDs/locators/class/strength/method/date/environment/coverage; value mechanism/beneficiary/context/dependency/repeatability; counterevidence/limitations/confidence/falsification test; preservation class (`HARD_INVARIANT`, `SOFT_CONSTRAINT`, `OPTIONAL_VALUE`); proposed action/trade-off/risk/acceptance criteria/verification owner.

Deliver positive finding register, value map, preservation/non-regression plan, reusable pattern register and evidence-backed enhancement opportunities.

## Route boundaries and handoff

- M00 decides route necessity and owns synthesis.
- O05 consumes preservation constraints to compare real candidates.
- O07/O08 incorporate accepted constraints; O03 does not authorize implementation.
- O10 verifies retained behaviors; O12 judges whether measures represent value/outcomes.
- O03 cannot accept risks, authorize security tests, approve roadmap changes, implement changes or declare roadmap success.

## Quality and stop conditions

No unsupported scores, weights, impact/adoption/ROI claims. No `REALIZED` label without evidence that the capability exists and works in context. Return `BLOCKED` for insufficient scope/authority; `INSUFFICIENT_EVIDENCE` for unsubstantiated material claims. A preservation requirement without a test oracle is `UNVERIFIABLE`, not passed.
