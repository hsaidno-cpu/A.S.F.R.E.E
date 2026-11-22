# RPEDS Module 03 — Continuous Evaluation Engine

## Responsibility

Schedule and maintain evaluation checkpoints for the roadmap. O12 retains evaluation authority: it defines the construct, criteria, indicator validity, methods, thresholds, judgment, impact and meta-evaluation. O10 retains test execution and observed test reporting. RPEDS does not independently invent scores or declare acceptance.

## Evaluation mapping

Map roadmap lifecycle checkpoints to O12's existing evaluation lifecycle without conflating roadmap control with evaluation authority:

- R0–R1: E0 Charter, E1 Baseline & Criteria, and E2 Evidence Plan.
- R4–R5: E3 Formative evaluation for delivery/process drift, evidence gaps, invalid assumptions and emerging risks.
- R6: E4 Summative acceptance; run E5 Post-Change after a material change or reconstruction.
- R7: E6 Outcome/Impact for intended benefits, harms and realized effects.
- R8: use relevant E3–E6 findings, test results and risk evidence as inputs to adaptation. E7 is not a substitute for current milestone evidence and must not be used to turn a failed gate into a pass.
- R9: E7 Meta-Evaluation reviews the evaluation system itself: criteria, coverage, reliability, evaluator bias, metric gaming, reproducibility and calibration. For long-running roadmaps, E7 may also run at a declared periodic cadence.

The R and E states are related but not interchangeable. A roadmap phase may revisit multiple E checkpoints; every evaluation record must state its E stage, purpose, criteria, evidence, evaluator, disposition and limitations.

## Measurement protocol

For each indicator record stable ID, evaluation dimension, operational definition, decision relevance, quantitative/qualitative/mixed type, method, unit or rubric, baseline, target, threshold, observed value only when measured, evidence refs, method/environment, time/version, scope, uncertainty, confidence, coverage and limitations.

Keep evidence strength, confidence, severity, likelihood, importance and impact separate. Do not aggregate incomparable units. A missing observation is NOT_ASSESSED or INSUFFICIENT_EVIDENCE, not zero.

## Hard gates

- Required test not executed: NOT_RUN, never PASS.
- Required evidence absent: INSUFFICIENT_EVIDENCE or HOLD.
- P0/P1 hard-gate failure cannot be averaged away.
- Mocked provider or static instruction cannot establish live infrastructure or dynamic behavior.
- A completed test is an observation; O12 decides what it means against the evaluation charter.
- Progress percentages require an explicit denominator and approved calculation. Weighted aggregation requires O12 validity review and decision-owner approval.

## Output

Evaluation checkpoint schedule, indicator registry, baseline/target/evidence status, actual O10 test refs, O12 disposition, hard-gate status, uncertainty and next evaluation trigger.
