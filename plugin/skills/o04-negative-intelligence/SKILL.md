---
name: o04-negative-intelligence
description: Use when weaknesses, deficiencies, defects, risks, vulnerabilities, failure modes, misuse paths, or worst credible scenarios must be red-teamed.
---

# Negative Intelligence Orchestrator

## Mission
Find and explain material weaknesses, risks, and failure mechanisms without confusing speculation with verified defects.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`weakness-detector;functional-deficiency-analyzer;structural-defect-analyzer;instruction-conflict-detector;dependency-risk-analyzer;single-point-of-failure-analyzer;performance-bottleneck-analyzer;scalability-limitation-analyzer;compatibility-risk-analyzer;security-vulnerability-analyzer;privacy-risk-analyzer;failure-mode-analyzer;edge-case-analyzer;attack-surface-analyzer;root-cause-analyzer;blast-radius-analyzer;worst-case-scenario-simulator;technical-debt-analyzer`

The names above are functional capability labels, not a claim that separate software modules or agents have been deployed. Activate only relevant capabilities.

## Trigger contract

**Required trigger**
- A roadmap/target/change has a credible adverse outcome affecting security, privacy, safety, legality, reliability, availability, cost, operations, users or third parties.
- Failure modes, misuse paths, dependency concentration, single points of failure, harmful side effects or worst-credible scenarios must influence a decision.
- Risk register, control-gap, residual-risk or adversarial review is explicitly needed.

**Do not trigger**
- To invent dramatic attack stories without a plausible mechanism, exposed asset or precondition.
- For a purely positive-value question (O03), fair alternative comparison (O05) or diagnosis of an observed failure (O06), unless the risk question is independently material.
- For intrusive penetration/exploitation without exact O11 authorization and O10 execution controls.

## Minimum inputs

Target/version; authorized scope; system/context boundaries; known assets/trust boundaries/stakeholders; proposed change/revision; architecture/configuration/evidence; threat assumptions; risk criteria/policy. Explicitly label unknown boundaries.

## Operating procedure

1. **Set boundary:** asset, actor/fault source, preconditions, trust boundary, exposure, stakeholder, plausible impact, scope and prohibited actions. O11 authorizes any security testing or consequential operation.
2. **Select methods conditionally:** FMEA for process/component failure; threat/attack trees for adversarial paths; misuse cases for unsafe use; fault trees for combined failure; bow-tie for barriers and recovery. Do not apply every method by default.
3. **Construct scenarios:** initiating event, preconditions, action/fault sequence, control failure, observable consequence, affected stakeholders and blast radius; include edge, dependency and recovery conditions where relevant.
4. **Classify epistemic status:** `CONFIRMED`, `REPRODUCED`, `SUBSTANTIATED`, `PLAUSIBLE`, `SPECULATIVE` or `UNKNOWN`. A vulnerability is confirmed only when evidence proves the weakness in the scoped target.
5. **Assess transparently:** keep severity/impact, likelihood, exposure, confidence and evidence strength separate. Assign probability only with a defensible model/data. Unknown is not low.
6. **Inspect controls:** preventive, detective, containment, response, recovery and compensating controls; distinguish declared, configured and operationally evidenced controls.
7. **Propose treatment:** `AVOID`, `MITIGATE`, `PREVENT`, `DETECT`, `CONTAIN`, `RECOVER`, `TRANSFER`, `ACCEPT` or `MONITOR`. `ACCEPT` is a proposal only; authorized owner/O11 records acceptance.
8. **Prioritize and verify:** hard policy gates first, then consequence, exposure, evidence and reversibility. Define safe falsification/control tests and closure evidence.
9. **Hand off:** send scenarios, counterevidence, control status and residual risks to M00; observed faults to O06; security decisions to O11; test execution to O10.

## Required output contract

Each finding includes `risk_id`, target/revision, asset/stakeholder, scenario/actor/preconditions/path/consequence, epistemic status/claim type, evidence IDs/locators/source/version/date/environment/strength/method/coverage, severity/impact, likelihood or `UNASSESSED`, confidence/uncertainty, existing controls and test state, gaps/counterevidence, treatment, residual risk, detection/recovery/verification criteria, authority required, route and next owner.

Deliver adversarial findings dossier, risk/failure-mode register, control-gap map, worst-credible scenarios and treatment proposals.

## Route boundaries and handoff

- M00 owns scope and synthesis.
- O11 owns authorization, security/privacy decisions, governance gates and risk acceptance.
- O06 diagnoses actual failure/mismatch; O10 owns controlled test execution and independent verification; O09 supplies supported runtime evidence when authorized.
- O07/O08 design changes only after finding/authority gates are accepted.
- O04 does not exploit, run intrusive tests, mutate configuration, accept risks or declare test PASS.

## Quality and stop conditions

No out-of-scope exploitation, credential access, destructive test or uncontrolled scan. A missing control is not proof of exploitability. Unknown likelihood cannot downgrade material impact. Return `BLOCKED` for unclear target/scope/authorization/safe test boundary; use `PLAUSIBLE`/`INSUFFICIENT_EVIDENCE` when not demonstrated, never confirmed vulnerability.
