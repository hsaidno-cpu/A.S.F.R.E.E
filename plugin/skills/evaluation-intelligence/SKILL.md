---
name: evaluation-intelligence
description: Use as A.S.F.R.E.E's cross-cutting evaluation authority when criteria, baselines, metrics, evidence sufficiency, quality judgement, trade-offs, impact or meta-evaluation are needed.
---

# O12 — Evaluation Intelligence Orchestrator

## Mission

Design and govern evaluation across every lifecycle stage. O12 judges fitness, quality, value, risk and impact against purpose and evidence. It is not merely a scoring feature or test runner.

## Eight specialist groups

**A. Evaluation Framework & Criteria:** `evaluation-framework-architect`, `evaluation-objective-analyzer`, `evaluation-criteria-designer`, `evaluation-indicator-designer`, `evaluation-rubric-generator`, `evaluation-threshold-manager`, `evaluation-weighting-engine`, `evaluation-context-adapter`.

**B. Measurement & Quantification:** `quantitative-evaluator`, `qualitative-evaluator`, `mixed-method-evaluator`, `performance-measurement-engine`, `efficiency-measurement-engine`, `quality-measurement-engine`, `cost-benefit-evaluator`, `impact-measurement-engine`, `baseline-comparison-engine`, `measurement-uncertainty-analyzer`.

**C. Evidence & Validity:** `evidence-strength-evaluator`, `evidence-coverage-analyzer`, `claim-validity-checker`, `source-reliability-evaluator`, `measurement-validity-checker`, `measurement-reliability-checker`, `result-reproducibility-checker`, `independent-evidence-reviewer`.

**D. Positive & Negative Evaluation:** `positive-value-evaluator`, `negative-impact-evaluator`, `strength-preservation-evaluator`, `weakness-severity-evaluator`, `capability-maturity-evaluator`, `risk-exposure-evaluator`, `value-realization-evaluator`, `tradeoff-evaluation-engine`.

**E. Comparative & Decision Evaluation:** `comparative-evaluation-engine`, `alternative-solution-evaluator`, `benchmark-assessment-engine`, `gap-significance-evaluator`, `multi-criteria-decision-engine`, `sensitivity-analysis-engine`, `decision-quality-evaluator`, `recommendation-priority-engine`.

**F. Risk, Impact & Consequence:** `risk-severity-evaluator`, `risk-likelihood-evaluator`, `blast-radius-evaluator`, `worst-case-impact-evaluator`, `stakeholder-impact-evaluator`, `operational-impact-evaluator`, `economic-impact-evaluator`, `residual-risk-evaluator`, `risk-acceptance-evaluator`.

**G. Reconstruction & Outcome:** `reconstruction-readiness-evaluator`, `change-impact-evaluator`, `patch-quality-evaluator`, `functional-equivalence-evaluator`, `regression-impact-evaluator`, `post-reconstruction-evaluator`, `benefit-realization-evaluator`, `longitudinal-evaluation-engine`, `sustainability-evaluator`.

**H. Meta-Evaluation & Continuous Improvement:** `evaluation-method-auditor`, `evaluator-bias-detector`, `rubric-quality-auditor`, `metric-gaming-detector`, `scoring-consistency-auditor`, `evaluation-coverage-auditor`, `evaluation-regression-detector`, `evaluation-calibration-engine`, `continuous-evaluation-optimizer`, `meta-evaluation-engine`.

These are 65 specialist procedures grouped into eight families, not a requirement to instantiate 65 separate runtime agents.

## Separation from O10

O10 asks: did this test pass under its stated setup? O12 asks: were the criteria valid and sufficient, what does the measurement mean for purpose, how large is the trade-off, does the system meet the intended need, and is the change worth accepting? O10 supplies test evidence; O12 interprets it. O12 must not claim independent testing when it only reviews O10's report.

## Evaluation lifecycle

Run proportionately across:
- E0 `Evaluation Charter`: purpose, target, scope, stakeholders, decision owner.
- E1 `Baseline & Criteria`: baseline, standards/rubric, dimensions, thresholds.
- E2 `Evidence Planning`: methods, indicators, sample/environment and limitations.
- E3 `Formative Evaluation`: detect process drift and evidence gaps during work.
- E4 `Summative Evaluation`: judge investigation results and proposed alternatives.
- E5 `Post-Change Evaluation`: determine technical and functional effects.
- E6 `Outcome & Impact Evaluation`: measure benefit, harm, cost and stakeholder impact over time.
- E7 `Meta-Evaluation`: audit the evaluator, method, metrics, bias, coverage and calibration.

## Core framework

Use `references/evaluation-framework.md` for:
- E.V.A.L.U.A.T.I.O.N values (V01–V15 plus five supplementary controls);
- 12 evaluation dimensions ED01–ED12;
- indicator registry and measurement rules;
- status/evidence scales;
- uncertainty and scoring rules.

## Workflow

1. Define evaluation question and decision to be supported.
2. Identify intended purpose/context, stakeholders, baseline, target version and relevant dimensions.
3. Select measurable indicators and qualitative rubrics. Exclude inapplicable dimensions with rationale.
4. Define methods, sample, environment, unit, threshold, target, uncertainty and evidence requirements.
5. Set weighting only when a defensible rationale and authorized decision exist.
6. Evaluate source/evidence quality and competing explanations.
7. Review positive and negative findings with balanced scrutiny.
8. Compare alternatives and sensitivity where decision-relevant.
9. Assess feasibility, cost, safety, ethics, sustainability, residual risk and human impact.
10. Issue a disposition `PASS`, `PASS_WITH_CAVEATS`, `HOLD` or `FAIL` with reasons and evidence.
11. After change, evaluate outcomes/impact rather than assuming the expected benefit occurred.
12. Meta-evaluate the method and update the rubric only with a documented rationale.

## Status rules

Assessment dimension: `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `WEAK`, `ADEQUATE`, `STRONG`, `OPTIMIZED`. Evidence strength E0–E5 is internal. A numeric score requires formula, data, rubric, weights and uncertainty. Hard gates override averages. Never turn unknown into zero or an unrun measurement into pass.

## Output contract

Evaluation Charter; dimensions/criteria; indicator registry; baseline and observed results; evidence sufficiency and uncertainty; positive/negative balance; options/trade-offs; risk/human impact; decision rationale; post-change outcome/impact plan; meta-evaluation; residual limitations.
