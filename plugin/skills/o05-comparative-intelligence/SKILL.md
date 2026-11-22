---
name: o05-comparative-intelligence
description: Use when comparing versions, architectures, systems, tools, policies, methods, solutions, or current state against a baseline or target.
---

# Comparative Intelligence Orchestrator

## Mission
Produce fair, context-sensitive comparisons with normalized criteria, traceable deltas, and explicit trade-offs.

## Responsibility boundary
Own only the specialist work described here. M00 retains case orchestration, scope arbitration, and final synthesis. O11 retains cross-cutting authorization and governance; O12 retains cross-system evaluation authority. Use this skill as a logical workstream if the host cannot expose a separate skill invocation; do not claim an autonomous agent ran.

## Specialist capability catalogue
`version-comparison;architecture-comparison;skill-comparison;orchestrator-comparison;feature-comparison;capability-comparison;performance-comparison;security-comparison;efficiency-comparison;compatibility-comparison;dependency-comparison;benchmark-comparison;strength-gap-analyzer;weakness-gap-analyzer;tradeoff-analyzer;comparative-recommendation-engine`

The names above are functional capability labels, not a claim that separate software modules or agents have been deployed. Activate only relevant capabilities.

## Trigger contract

**Required trigger**
- At least two identifiable, feasible alternatives could meet the same decision need.
- A current version/baseline must be compared with a specified target/revision/standard.
- Roadmap adaptation, architecture choice, migration, prioritization or technology selection depends on explicit trade-offs.

**Do not trigger**
- For single-object strengths/weaknesses without a comparator.
- When candidates are vague, infeasible, different in scope or invented to fill a table.
- To make the final decision; M00 recommends and the authorized human owner decides.

## Minimum inputs

Decision question; baseline/candidate identities and versions; use case/users; scope/exclusions; context/environment/time window; constraints/hard gates; evidence; criteria/policy. If criteria or weights are missing, propose for approval or compare without weights.

## Operating procedure

1. **Frame decision:** state decision, owner, horizon and outcome defining suitability.
2. **Identify candidate set:** include current/status quo and only feasible options; include `DO_NOTHING`, `DEFER`, `PILOT` or `STOP` when real. Record exclusions.
3. **Test comparability:** align scope, workload, user group, version, environment, method and data freshness. Mark unnormalizable dimensions; do not compare unlike objects as equal.
4. **Define criteria before scoring:** meaning, direction, unit/rubric, evidence, hard-gate status and relevance. Separate mandatory constraints from preferences. Use O12 for validity/measurement design when weighted or outcome-sensitive judgment matters.
5. **Normalize evidence:** convert units only validly; align test conditions and denominators; separate measurements, claims and inferences. Missing is `UNKNOWN`, not zero.
6. **Analyze deltas/trade-offs:** strengths, weaknesses, compatibility, operating cost, dependencies, risks, effort, reversibility and stakeholder impact.
7. **Control aggregation:** default to unweighted criterion-by-criterion matrix. Weighted composite requires documented rationale, comparable scales, sensitivity analysis, O12 validity review and decision-owner approval. Hard-gate failure cannot be compensated by other scores.
8. **Check sensitivity/dominance:** identify dominated options, threshold breaches and conclusions that change under reasonable assumptions; state evidence that could reverse the recommendation.
9. **Recommend conditionally:** specify which option fits which constraints, confidence and risk appetite; include no-decision path where relevant.
10. **Hand off:** send matrix and limitations to M00; O12 reviews validity as required; M00/human owner retains decision authority.

## Required output contract

Decision question/owner/horizon; baseline and candidates with version/scope/environment/inclusion rationale; comparability/normalization; criteria register with definition/direction/unit/hard-gate/provenance; candidate evidence values/missingness/uncertainty; deltas/trade-offs/stakeholder effects; weight rationale/approvals or no aggregate; sensitivity/dominance/evidence gaps; conditional recommendation/reversibility/revisit trigger/next owner.

Deliver comparative baseline, normalized criteria matrix, delta/trade-off analysis, comparability limits and decision brief.

## Route boundaries and handoff

- M00 owns scope and synthesis; O05 does not choose for the user.
- O03 supplies preservation constraints; O04 supplies risk/control constraints.
- O12 owns evaluation validity, indicators, measurement and interpretation; it validates weights/aggregation where material.
- O10 supplies actual comparable test results; no invented benchmarks.
- O07/O08 design the selected option only after M00/human decision and O11 approval where required.

## Quality and stop conditions

No score/weighted ranking without operational criteria, evidence and defensible scale. Mark unlike contexts `NOT_COMPARABLE`. If only one feasible candidate remains, stop comparison and route to the relevant single-object analysis. Return `BLOCKED` for unclear decision scope/target/data authority, or `INCOMPLETE` with unknowns that could alter the decision.
