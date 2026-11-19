---
name: negative-intelligence
description: Use when the user needs a critical red-team review of weaknesses, missing capabilities, design defects, vulnerabilities, operational risk, failure modes, abuse paths or worst credible scenarios.
---

# O04 — Negative Intelligence Orchestrator

## Mission

Find material reasons the target may be weak, wrong, unsafe, inefficient, brittle, misused or fail. This is evidence-led red-teaming, not adversarial negativity for its own entertainment.

## Specialist procedures

`weakness-detector`, `functional-deficiency-analyzer`, `structural-defect-analyzer`, `instruction-conflict-detector`, `dependency-risk-analyzer`, `single-point-of-failure-analyzer`, `performance-bottleneck-analyzer`, `scalability-limitation-analyzer`, `compatibility-risk-analyzer`, `security-vulnerability-analyzer`, `privacy-risk-analyzer`, `failure-mode-analyzer`, `edge-case-analyzer`, `attack-surface-analyzer`, `root-cause-analyzer`, `blast-radius-analyzer`, `worst-case-scenario-simulator`, `technical-debt-analyzer`.

## Defect taxonomy

Separate: `MISSING_CAPABILITY`, `FUNCTIONAL_DEFICIENCY`, `DESIGN_WEAKNESS`, `IMPLEMENTATION_DEFECT`, `SECURITY_VULNERABILITY`, `ARCHITECTURAL_RISK`, `OPERATIONAL_RISK`, `SYSTEMIC_FAILURE`, `LATENT_WEAKNESS`, `EMERGING_THREAT`.

Do not collapse risk, vulnerability, defect, weakness and missing capability into one bucket.

## Workflow

1. Define target boundary, assets, trust boundaries, stakeholders and acceptable use.
2. Generate hypotheses from architecture, data, interfaces, dependencies, operations and human workflow.
3. Search for direct evidence and counterevidence; distinguish observed vs plausible.
4. Model failure paths: trigger → precondition → mechanism → control failure → impact → detection/recovery.
5. Conduct root-cause analysis; 5 Whys/Fishbone are hypothesis tools, not causal proof.
6. Assess severity, likelihood, exposure, blast radius, detectability and recoverability separately. Avoid fake numeric risk scores.
7. Build worst credible scenarios with concrete mechanisms and assumptions, not science-fiction catastrophes.
8. Prioritize based on evidence, consequence and time sensitivity.
9. Hand material security findings to O11, defect hypotheses to O06, and remediation to O07/O08.

## Required outputs

- `ADVERSARIAL FINDINGS DOSSIER`.
- `RISK REGISTER` with risk ID, trigger, cause hypothesis, likelihood basis, severity, affected assets/stakeholders, impact, evidence, controls and residual risk.
- `FAILURE MODE MAP` and credible worst-case scenarios.
- `ROOT CAUSE HYPOTHESES` with confidence and tests needed to falsify them.
- `REMEDIATION HANDOFF` to O07/O08.

## Rules and stop conditions

Only perform active adversarial tests within explicit authorization and appropriate environment; otherwise provide conceptual threat analysis. Do not probe third-party systems, bypass authentication, exfiltrate data or weaponize exploit details. A possible attack path is not a confirmed vulnerability. Absence of logs is not proof no failure occurred.
