# Evaluation Intelligence Control Plane

## Foundational position

Evaluation is the philosophy, control mechanism, decision discipline, and proof standard across A.S.F.R.E.E. It is not synonymous with testing. A passed test is an observation; the evaluator judges whether the result satisfies the purpose, quality criteria, impact and residual-risk requirements.

## E.V.A.L.U.A.T.I.O.N — internal Evaluation Values & Assessment Intelligence Framework

This is an internal values framework, not an external or accredited standard.

| ID | Value | Operational meaning |
|---|---|---|
| V01 | Validity | Measure the property that actually matters |
| V02 | Veracity | Preserve evidence truth and integrity |
| V03 | Objectivity | Reduce assessor bias |
| V04 | Reliability | Produce sufficiently consistent assessments |
| V05 | Completeness | Cover material dimensions without pretending exhaustive coverage |
| V06 | Relevance | Fit the target purpose and context |
| V07 | Proportionality | Match depth to uncertainty, risk and consequence |
| V08 | Transparency | Make criteria and decision basis visible |
| V09 | Traceability | Link claims, evidence, findings, decisions and tests |
| V10 | Reproducibility | Enable independent repetition where feasible |
| V11 | Independence | Permit reviewers to disagree with builders |
| V12 | Fairness | Avoid unjustified bias and asymmetric standards |
| V13 | Actionability | Translate findings into feasible decisions/actions |
| V14 | Sustainability | Preserve maintainability and long-term viability |
| V15 | Continuous Improvement | Use outcomes to refine the system and its evaluation |

Additional control values: **Contextual Fitness**, **Positive-Negative Balance**, **Uncertainty Awareness**, **Value Preservation**, **Impact Accountability**.

## Twelve evaluation dimensions

ED01 Structural Quality; ED02 Functional Quality; ED03 Capability & Value; ED04 Technical Quality; ED05 Security & Safety; ED06 Reliability & Resilience; ED07 Interoperability; ED08 Maintainability; ED09 Efficiency & Economics; ED10 Usability & Human Impact; ED11 Adaptability & Sustainability; ED12 Evidence & Governance.

Not every dimension or indicator applies to every target. Explain exclusions. Do not treat an unobserved dimension as strong.

## Evaluation charter

Before material evaluation, define: target and version; purpose and decision to be supported; intended users/stakeholders; scope/non-goals; baseline; context/time anchors; applicable standards/rubrics; indicators; measurement methods; thresholds; weighting rationale/approval; evidence requirements; uncertainty and limitations; decision owner; review date or trigger.

## Measurement registry

Each indicator record should contain `indicator_id`, dimension, operational definition, measurement method, type (`QUANTITATIVE`, `QUALITATIVE`, `MIXED`), unit, baseline, target, observed value, threshold, weight and approval basis (if used), evidence references, uncertainty, limitations, environment, version, and timestamp when actually observed.

Never invent precision. Do not aggregate incomparable indicators. A weighted score requires a defensible rubric and approved weights. Hard gates override averages: a critical auth failure cannot be hidden by a high overall average.

## Status and evidence scales

Assessment status: `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `WEAK`, `ADEQUATE`, `STRONG`, `OPTIMIZED`.

Evidence strength rubric: `E0` not inspected; `E1` assertion without independent evidence; `E2` indirect evidence; `E3` direct static inspection/observation; `E4` reproducible dynamic test; `E5` independent reproducible verification. This is an internal rubric, not a probability or universal evidence standard.

Keep evidence strength, confidence, severity, likelihood and impact separate. `INSUFFICIENT_EVIDENCE` is not the same as `WEAK`.

## Continuous evaluation lifecycle

- E0 Evaluation Charter.
- E1 Baseline & Criteria.
- E2 Evidence Planning.
- Forensic investigation and formative evaluation.
- Findings, diagnosis and summative evaluation.
- Solution/alternative evaluation.
- Human approval where required.
- Supervised reconstruction.
- Test/independent verification.
- E5 Post-change evaluation.
- E6 Outcome & impact evaluation.
- E7 Meta-evaluation of methods, metrics, bias, coverage and calibration.

Formative asks whether the process is on track; summative asks how good the result is; impact asks whether the change produced the promised effect.

## Meta-evaluation

Audit evaluator bias, rubric quality, evidence sufficiency, coverage, repeatability, metric gaming, sensitivity to weights/assumptions, false positives/negatives, and whether metrics incentivize harmful behavior. Revisit the evaluation design when the result is unstable or not decision-useful.
