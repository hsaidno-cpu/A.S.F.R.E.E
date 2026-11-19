# Shared Data & Handoff Contracts

These are portable logical contracts. They are not claims that a live database or JSON API exists. Use JSON/YAML examples as structured work products and keep IDs unique within a case/release.

## Common identifiers

`CASE-###`, `TARGET-###`, `ART-###`, `SRC-###`, `CLM-###`, `EVD-###`, `MTH-###`, `FND-###`, `CAU-###`, `RSK-###`, `IMP-###`, `DEC-###`, `OPT-###`, `REC-###`, `REQ-###`, `TST-###`, `DEF-###`, `FAI-###`, `UNK-###`, `RCT-###`, `VFY-###`.

IDs are trace labels, not evidence of persistence.

## Finding contract

```yaml
finding_id: FND-001
target_id: TARGET-001
category: POSITIVE | NEGATIVE | DEFECT | RISK | GAP | OBSERVATION
type: STRUCTURAL_WEAKNESS
statement: "Precise, falsifiable finding"
status: OBSERVED | SUPPORTED | HYPOTHESIS | UNKNOWN
severity: P0 | P1 | P2 | P3 | NOT_RATED
confidence: LOW | MEDIUM | HIGH | NOT_ASSESSED
evidence_ids: [EVD-001]
method_ids: [MTH-001]
scope: "Affected component or behavior"
root_cause_hypotheses: ["CAU-001"]
impact: "Observed or reasoned consequence"
limitations: ["What was not inspected"]
recommendation_ids: [REC-001]
```

## Evidence contract

```yaml
evidence_id: EVD-001
source_id: SRC-001
kind: FILE | CODE | DOCUMENT | OBSERVATION | TOOL_OUTPUT | TEST_RESULT | MEASUREMENT | USER_CLAIM
aquisition_method: DIRECT_READ | STATIC_INSPECTION | DYNAMIC_TEST | USER_SUPPLIED | EXTERNAL_SOURCE
locator: "path, line, URL, symbol, test ID, or timestamp if available"
collected_at: "timestamp only if observed"
version_or_context: "version/ref/environment when known"
integrity_check: NOT_RUN | CHECKSUM_VERIFIED | SIGNATURE_VERIFIED | OTHER
supports_claims: [CLM-001]
contradicts_claims: []
strength: E0 | E1 | E2 | E3 | E4 | E5
limitations: ["Coverage or access limitations"]
```

## Change proposal contract

```yaml
change_id: CHG-001
recommendation_id: REC-001
finding_ids: [FND-001]
status: PROPOSED | ACCEPTED | DEFERRED | REJECTED | NEEDS_DECISION
scope: ["Files/components in scope"]
non_goals: ["Unchanged behavior"]
baseline_ref: "commit/version/snapshot, if known"
proposed_changes: ["Exact changes"]
preconditions: ["Required access/tools/approvals"]
risks_and_tradeoffs: ["New risk and cost"]
rollback: "Reversible rollback steps or NOT_AVAILABLE"
acceptance_tests: [TST-001]
residual_risk: ["Remaining uncertainty"]
approval: PENDING | APPROVED | REJECTED | NOT_REQUIRED
```

## Test record

```yaml
test_id: TST-001
requirement_id: REQ-001
layer: STATIC | CONTRACT | HARNESS | HOST_BEHAVIOR | RUNTIME | INDEPENDENT
setup: "Version, environment and inputs"
expected: "Observable expected result"
actual: "Observed actual result or NOT_RUN"
status: PASS | FAIL | BLOCKED | NOT_RUN | NOT_APPLICABLE | UNVERIFIABLE
evidence_ids: [EVD-002]
limitations: []
```

## Claim, provenance and trace

Separate direct observation, user/source claim, verified-source claim, assumption, inference, hypothesis, prediction, normative judgement and recommendation. Trace material conclusions:

`CLM → EVD → SRC/ARTIFACT → METHOD/OBSERVATION → CONTEXT/TIME → STATUS → ALLOWED WORDING`.

Trace edges must be typed (`SUPPORTS`, `CONTRADICTS`, `DERIVED_FROM`, `OBSERVES`, `DEPENDS_ON`, `CAUSAL_HYPOTHESIS`, `MITIGATES`, `VERIFIES`, `SUPERSEDES`). Mark edges as observed, documented, inferred or causal hypothesis. A graph does not prove causation.

## Required handoff payload

Intent/scope, target/version, required capability, source/evidence refs, assumptions/unknowns, methods, dependencies, result/findings, risk/approval status, output contract, acceptance criteria, status and next owner. Keep fields explicit; no silent inference.
