# RPEDS Module 01 — Roadmap Architecture Planner

## Responsibility

Translate an approved intent into a versioned, dependency-aware roadmap. This module owns decomposition and roadmap structure only. M00 owns case scope and final arbitration; O02 owns target anatomy and dependency discovery; O12 owns evaluation criteria and judgments; O11 owns authorization and governance.

## Workflow

1. Resolve intent: outcome, target/system and version, decision owner, beneficiaries, constraints, non-goals, risk tolerance, and decision need.
2. Establish baseline using O01/O02 artifacts and verified repository/system evidence. Record exact refs, versions, dates and inspection depth. Mark unknowns; never infer a missing baseline.
3. Build objective hierarchy: strategic outcome → capability outcome → phase objective → milestone → work item. Every child must contribute to a parent objective.
4. Design phases with sequence, objective, scope, entry criteria, exit criteria, deliverables, dependencies, risk assumptions and gate owner.
5. Model dependencies as typed DEPENDS_ON relationships. Validate a directed acyclic graph. A cycle is an invalid plan requiring redesign.
6. Assess capacity, skills, budget, tooling, external dependencies and critical path only when source data exists. Unknown capacity is not zero capacity.
7. Set progress policy. Default to verified work-item counts and separate quality/impact measures. Weighted progress requires documented comparable scales, approved weights and O12 validation.
8. Version and hand off a roadmap revision, baseline snapshot, assumptions register, risk register and approval request. M00/human authority decides approval.

## Required design checks

- No orphan milestone or work item without a parent objective.
- No duplicate scope hidden in parallel phases.
- No circular dependency.
- No target date without an agreed commitment or schedule basis.
- No owner assignment inferred from prior participation.
- No baseline or success target derived from guesswork.
- No weighted composite without rationale, normalization, approval and sensitivity review.

## Output

Roadmap contract, objective tree, phase/milestone map, dependency DAG, baseline and assumptions register, feasibility notes, progress policy, acceptance gates, risks, unknowns and approval needs.
