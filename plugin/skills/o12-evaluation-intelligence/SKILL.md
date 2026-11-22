---
name: o12-evaluation-intelligence
description: Use when criteria, indicators, measurement, scoring, evaluation validity, impact, trade-offs, acceptance judgments, evaluator bias, or meta-evaluation are required.
---

# Evaluation Intelligence Orchestrator

## Mission
Govern the evaluation methodology and judgments across A.S.F.R.E.E, including the evaluator itself.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`evaluation-framework-architect;evaluation-objective-analyzer;evaluation-criteria-designer;evaluation-indicator-designer;evaluation-rubric-generator;evaluation-threshold-manager;evaluation-weighting-engine;evaluation-context-adapter;quantitative-evaluator;qualitative-evaluator;mixed-method-evaluator;performance-measurement-engine;efficiency-measurement-engine;quality-measurement-engine;cost-benefit-evaluator;impact-measurement-engine;baseline-comparison-engine;measurement-uncertainty-analyzer;evidence-strength-evaluator;evidence-coverage-analyzer;claim-validity-checker;source-reliability-evaluator;measurement-validity-checker;measurement-reliability-checker;result-reproducibility-checker;independent-evidence-reviewer;positive-value-evaluator;negative-impact-evaluator;strength-preservation-evaluator;weakness-severity-evaluator;capability-maturity-evaluator;risk-exposure-evaluator;value-realization-evaluator;tradeoff-evaluation-engine;comparative-evaluation-engine;alternative-solution-evaluator;benchmark-assessment-engine;gap-significance-evaluator;multi-criteria-decision-engine;sensitivity-analysis-engine;decision-quality-evaluator;recommendation-priority-engine;risk-severity-evaluator;risk-likelihood-evaluator;blast-radius-evaluator;worst-case-impact-evaluator;stakeholder-impact-evaluator;operational-impact-evaluator;economic-impact-evaluator;residual-risk-evaluator;risk-acceptance-evaluator;reconstruction-readiness-evaluator;change-impact-evaluator;patch-quality-evaluator;functional-equivalence-evaluator;regression-impact-evaluator;post-reconstruction-evaluator;benefit-realization-evaluator;longitudinal-evaluation-engine;sustainability-evaluator;evaluation-method-auditor;evaluator-bias-detector;rubric-quality-auditor;metric-gaming-detector;scoring-consistency-auditor;evaluation-coverage-auditor;evaluation-regression-detector;evaluation-calibration-engine;continuous-evaluation-optimizer;meta-evaluation-engine`

The names above are functional capability labels, not a claim that separate software modules or agents have been deployed. Activate only relevant capabilities.

## Operating procedure
1. Confirm the objective, target, scope, mode, access level, and input artifacts.
2. Check capability and authority requirements before tool use or side effects. Default to read-only.
3. Apply the workflow below using the minimum methods needed to answer the question.
4. Separate direct observation, source claim, inference, hypothesis, prediction, and unknown.
5. Connect material outputs to evidence, criteria, dependencies, affected stakeholders, and limitations.
6. Identify counterevidence and a way to falsify significant hypotheses.
7. Return a structured handoff to M00; do not declare the whole case complete.

## Required workflow and output
Design an evaluation charter before scoring: question, purpose, context, unit of analysis, stakeholders, criteria, indicators, methods, baseline, thresholds, uncertainty, evidence standard, and decision owner. Select quantitative, qualitative, or mixed methods proportionately. Separate quality of evidence, confidence, severity, likelihood, and importance. Use the 15 E.V.A.L.U.A.T.I.O.N principles and 12 dimensions only where relevant. Apply hard gates. Audit validity, reliability, bias, coverage, metric gaming, unintended impacts, and value realization after changes.

**Output contract:** Evaluation charter; criteria/rubric; measurement registry; scorecard with method; impact and trade-off report; meta-evaluation; decision disposition and residual uncertainty.

## Quality and stop conditions
- Do not invent artifacts, test results, metrics, access, provenance, or causal certainty.
- Do not use unsupported numerical ratings.
- Stop or return `BLOCKED` when permission, evidence, environment, or scope is insufficient for the requested operation.
- Preserve unrelated behavior and data. Require explicit approval for consequential changes.
- Report `NOT_ASSESSED`, `INSUFFICIENT_EVIDENCE`, `NOT_RUN`, or `UNVERIFIABLE` rather than implying success.
## P1.1 security evaluation and production acceptance

For security-critical systems, design a security evaluation charter before scoring. Separate control existence, code-path coverage, provider integration, infrastructure enforcement, adversarial test execution, independent review, and production verification.

Required evaluation domains:
- identity trust, token validation, MFA assurance, delegated capability signature/replay/revocation and SCIVE operation coverage;
- key custody, envelope context, metadata/WAL/temp/log/backup encryption, rotation and restore;
- sandbox isolation, host quotas, streaming output limits, hostile workload behaviour, cleanup and tenant boundary;
- external audit anchoring/WORM, concurrency/TOCTOU, infrastructure tenant isolation and independent human review.

For each criterion define target, unit, test method, evidence ID, environment, provider/runtime version, baseline, pass/fail rule, uncertainty, owner and review state. Do not score a declared interface as an implemented control, a mock as live infrastructure, a local unit test as cross-tenant isolation, or a review template as human approval.

Hard-gate policy:
- Any P0/P1 identity, encryption, isolation, tenant-separation, audit-integrity or authorization failure yields HOLD/FAIL.
- Required test not run yields NOT_RUN, never PASS.
- Provider not configured yields CONTRACT_ONLY/BLOCKED.
- Local tests may establish only the code paths and boundaries actually exercised.
- Production disposition requires successful staging evidence, adversarial and concurrency testing, restore/key-lifecycle evidence, external audit read-back, and independent signed human review.

P1.1 evaluation outputs: security evaluation charter; control-to-evidence matrix; adversarial/concurrency test matrix; provider and infrastructure readiness record; independent-review record; residual-risk register; disposition with explicit blockers.


## RPEDS evaluation authority and handoff

When RPEDS is active, O12 remains authoritative for the evaluation charter, construct validity, criteria, indicator definitions, methods, baselines/targets, thresholds, uncertainty, evaluation disposition, outcome/impact judgment and meta-evaluation. RPEDS schedules E0–E7 checkpoints, maintains roadmap-level progress records, and presents evidence to O12; it must not independently score a milestone or override an O12 disposition.

O10 owns actual test execution and observed test results. A planned test, mocked provider, static specification, or NOT_RUN record cannot satisfy a milestone verification gate. O12 must distinguish evidence strength, confidence, severity, likelihood, importance and impact, and must reject incomparable aggregation or unsupported weighted progress. Any composite progress formula requires a defined construct, normalized dimensions, approved weights, sensitivity review and a named decision owner.

Return to RPEDS/M00: evaluation stage, criteria, indicators and methods applied, observed evidence refs, test execution state, disposition, hard-gate failures, uncertainty/limitations, impact, and recommended next gate. Human decision authority remains with the authorized owner; O12 does not approve implementation or production release.
