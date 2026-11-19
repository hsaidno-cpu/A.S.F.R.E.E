---
name: positive-intelligence
description: Use when the user asks to identify and evaluate strengths, valuable capabilities, effective features, architectural advantages, innovation, differentiation or growth opportunities in a technical system.
---

# O03 — Positive Intelligence Orchestrator

## Mission

Discover, verify and evaluate what works well and what should be preserved, amplified, replicated or leveraged. “Positive” means constructive, not flattering. Do not infer a strength from a feature list alone.

## Specialist procedures

`strength-analyzer`, `capability-analyzer`, `feature-value-analyzer`, `functional-excellence-analyzer`, `architecture-quality-analyzer`, `innovation-analyzer`, `efficiency-analyzer`, `scalability-potential-analyzer`, `reusability-analyzer`, `interoperability-analyzer`, `differentiation-analyzer`, `optimization-opportunity-analyzer`.

## Workflow

1. Define the target purpose, users and success context with M00/O12.
2. Identify claimed strengths and candidate capabilities from artifact/behavior evidence.
3. Verify existence: distinguish declared, implemented, observed, tested and externally validated capabilities.
4. Evaluate significance, user value, reliability, security, maintainability, efficiency and contextual relevance.
5. Compare with baseline or alternatives only where relevant; avoid ungrounded “best-in-class” claims.
6. Look for compounding opportunities, reusable patterns and underused capabilities.
7. Check preservation dependencies: what could regress if this strength is modified?
8. Convert into action labels and acceptance criteria.

## Action model

- `PRESERVE`: maintain proven behavior/quality and protect regression tests.
- `AMPLIFY`: enhance an already demonstrated strength.
- `REPLICATE`: reuse a proven pattern in another component/context after compatibility review.
- `LEVERAGE`: use an existing capability to unlock new value.
- `INTEGRATE`: combine complementary capabilities with explicit contracts.
- `STANDARDIZE`: formalize a repeatable successful pattern.

## Output contract

For each positive finding: `finding_id`, specific strength, evidence, scope, confidence, context of value, limitations, affected components, action label, expected benefit, regression guard and measure of realized value. Summarize `PRESERVE / AMPLIFY / REPLICATE / LEVERAGE` opportunities with an evidence-backed priority.

## Rules

Do not call an untested claim a proven capability. “Modular”, “scalable”, “innovative”, “efficient” and “secure” require operational definitions and evidence. Do not optimize a metric while degrading the user's actual purpose. Hand negative side effects to O04/O12.
