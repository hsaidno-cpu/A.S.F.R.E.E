# Forensic Methods, Evidence Modes & Limits

## Inspection depth

| Level | Mode | What can be supported | Output |
|---|---|---|---|
| L0 | Conceptual | User description/specification only | Conceptual audit |
| L1 | Artifact | Supplied files, manifests, docs, prompts | Structural/artifact audit |
| L2 | Source | Source code and dependencies inspected | Static technical audit |
| L3 | Dynamic | Authorized execution in sandbox | Runtime findings |
| L4 | Adversarial | Authorized security/resilience testing | Security assessment |
| L5 | Engineering | Controlled modification under approval | Patch/reconstruction |
| L6 | Verified Deployment | Release process and target read-back | Verified release |

Always report the deepest level actually performed. Do not infer L2 from reading a README; do not infer L3 from a mock run; do not infer L6 from a commit.

## Reverse-engineering access modes

- **White-box:** code/config/source artifacts available. Inspect actual artifacts and version boundaries.
- **Grey-box:** partial internals plus APIs/logs/documentation/observable behavior. Separate direct evidence from inference.
- **Black-box:** only input/output/behavior available. Infer external behavior, not hidden implementation. Do not claim to know internal algorithms.

## Target taxonomy

AI systems (plugins, skills, agents, orchestrators, model wrappers); software (applications, packages, libraries, frameworks); digital services (web/backend/SaaS); automation/workflows; infrastructure (cloud, database, container); connectivity (REST, GraphQL, MCP, events); data/knowledge systems; security/identity systems; hardware/firmware/embedded systems; other technical systems only when safely representable and authorized.

## Method selection

Pick a method based on the question and accessible evidence: first-principles decomposition for assumptions/components; systems thinking for feedback/dependencies; root-cause analysis for failure mechanisms; issue trees for decomposition; threat modeling for attack surfaces; design/JTBD for user value; hypothesis testing for falsifiable claims; comparative/MCDA for alternatives; reliability/failure-mode methods for resilience; controlled experiments for before/after claims. Name a method only when its steps, inputs, assumptions, limitations and decision value are specified.

5 Whys/Fishbone generate hypotheses; they do not prove causality. A static scan does not prove runtime behavior. A test suite passing does not prove that the tests are adequate. A source file is not proof of deployment. A hash proves byte integrity, not semantic truth.

## Evidence and confidence

Separate source reliability, evidence strength, confidence and severity. Record counterevidence, date/version, locator, acquisition method, scope, coverage, limitations and unknowns. Never manufacture hashes, signatures, logs, timestamps, screenshots or source access.
