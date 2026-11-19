# Evaluation Intelligence Control Plane

## Foundational position

Evaluation is the purpose, method, decision discipline, and proof standard across A.S.F.R.E.E. It is not synonymous with testing. A test provides an observation; evaluation judges whether the observed result satisfies the declared purpose, criteria, impact expectations, and residual-risk tolerance.

## E.V.A.L.U.A.T.I.O.N values

This is an internal design rubric, not an external or accredited standard.

| ID | Value | Operational meaning |
|---|---|---|
| V01 | Validity | Measure the construct that matters |
| V02 | Veracity | Preserve evidence truth and integrity |
| V03 | Objectivity | Reduce avoidable assessor bias |
| V04 | Reliability | Apply sufficiently consistent, repeatable criteria |
| V05 | Completeness | Cover material dimensions without claiming omniscience |
| V06 | Relevance | Fit purpose and context |
| V07 | Proportionality | Match depth to risk and consequence |
| V08 | Transparency | Expose criteria and decision basis |
| V09 | Traceability | Link claims, evidence, findings, decisions, and tests |
| V10 | Reproducibility | Enable independent repetition where feasible |
| V11 | Independence | Allow reviewers to disagree with builders |
| V12 | Fairness | Avoid unjustified bias or asymmetric standards |
| V13 | Actionability | Convert findings into feasible decisions |
| V14 | Sustainability | Consider maintenance and long-term viability |
| V15 | Continuous Improvement | Use outcomes to refine methods and controls |

Supplementary controls: **Contextual Fitness**, **Positive-Negative Balance**, **Uncertainty Awareness**, **Value Preservation**, and **Impact Accountability**.

## Twelve evaluation dimensions

1. Structural Quality.
2. Functional Quality.
3. Capability & Value.
4. Technical Quality.
5. Security & Safety.
6. Reliability & Resilience.
7. Interoperability.
8. Maintainability.
9. Efficiency & Economics.
10. Usability & Human Impact.
11. Adaptability & Sustainability.
12. Evidence & Governance.

Assess only applicable indicators and explain exclusions. An unobserved dimension is not strong by default.

## Evaluation charter

Before a material evaluation, define target/version, purpose and decision, users/stakeholders, scope/non-goals, baseline, context/time anchor, criteria, indicators, methods, units/rubrics, thresholds, weight rationale/approval (if used), evidence requirements, uncertainty, limitations, decision owner, and review trigger.

## Indicator registry

Each indicator should have `indicator_id`, dimension, operational definition, method, type (`QUANTITATIVE`, `QUALITATIVE`, `MIXED`), unit, baseline, target, observed value, threshold, weight/approval basis if used, evidence refs, uncertainty, limitations, environment, version, and timestamp only when observed.

No number without definition, method, unit/rubric, and evidence. No weight without rationale and approval where material. Do not aggregate incomparable indicators. Hard gates override averages. Keep confidence, severity, likelihood, importance, evidence strength, and impact separate.

## Evaluation dispositions

`NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `WEAK`, `ADEQUATE`, `STRONG`, `OPTIMIZED`. These are contextual judgments, not universal grades. `INSUFFICIENT_EVIDENCE` is not equivalent to `WEAK`.

## Continuous evaluation lifecycle

- `E0 CHARTER`: purpose, object, scope, evaluator, decision authority, non-goals.
- `E1 BASELINE & CRITERIA`: current state, criteria, indicators, baseline, targets/thresholds.
- `E2 EVIDENCE PLAN`: sources, methods, access, coverage, and evidence needs.
- `E3 FORMATIVE`: check process quality, drift, evidence gaps, invalid assumptions, emerging risks.
- `E4 SUMMATIVE`: judge investigation, alternatives, and result against declared criteria.
- `E5 POST-CHANGE`: compare the changed system to baseline and verify intended technical outcomes.
- `E6 OUTCOME/IMPACT`: assess intended benefits, human/operational effects, distribution, and second-order harms.
- `E7 META-EVALUATION`: audit rubric, evaluator bias, coverage, repeatability, metric gaming, and calibration.

Run stages proportionately. A completed test does not imply E5/E6, and a planned evaluation does not prove impact.
