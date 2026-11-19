# Forensic Methods, Evidence Modes & Limits

## Inspection depth

| Level | Mode | What can be supported |
|---|---|---|
| L0 | Conceptual | User description/specification only |
| L1 | Artifact | Supplied files, manifests, docs, prompts, metadata |
| L2 | Source | Source code and dependencies directly inspected |
| L3 | Dynamic | Authorized execution in an available sandbox/runtime |
| L4 | Adversarial | Authorized resilience/security testing in defined scope |
| L5 | Engineering | Controlled modification under approval |
| L6 | Verified Deployment | Approved release plus target read-back and checks |

Always report the deepest level actually reached. Static inspection does not prove runtime behavior; a package write does not prove tests; a commit does not prove deployment.

## Access modes

- **White-box:** source/configuration/artifacts available. Inspect actual artifacts and version boundaries.
- **Grey-box:** partial internals plus APIs/logs/docs/observable behavior. Label inference and counterevidence.
- **Black-box:** input/output or externally observable behavior only. Do not claim hidden algorithms or implementation internals.

## Target taxonomy

AI systems; applications/packages/libraries; APIs and digital services; automations and CI/CD; cloud/container/database/network infrastructure; REST/GraphQL/MCP/event connectivity; data and knowledge systems; identity/security systems; embedded/firmware/hardware interfaces; other technical targets only when authorized and safely inspectable.

## Method selection

Choose methods by analytical question, evidence, risk, and decision value. Candidate families include first-principles decomposition, systems thinking, issue trees, process/value-stream mapping, root-cause analysis, threat modeling, hypothesis testing, comparative/MCDA, reliability/FMEA, fault-tree/Bow-tie, controlled experiments, and stakeholder/value analysis.

Name a method only when its steps, inputs, assumptions, limitations, and decision value are clear. 5 Whys and Fishbone generate hypotheses, not proof. SWOT is not causal proof. FMEA depends on defined scales and evidence. A weighted decision matrix can hide value choices; show weight provenance and sensitivity. Do not create numeric probabilities or scores as decoration.

## Evidence discipline

Separate source reliability, evidence strength, confidence, severity, likelihood, and impact. Record locator, collection method, scope, date/version, integrity checks actually performed, coverage, limitations, counterevidence, and source independence. Do not invent hashes, signatures, timestamps, logs, screenshots, test output, or source access.

Evidence strength `E0–E5` is an internal rubric, not a probability or external certification:

- `E0`: not inspected.
- `E1`: unsupported assertion/description.
- `E2`: indirect evidence.
- `E3`: direct static inspection/observation.
- `E4`: reproducible dynamic test evidence.
- `E5`: independent reproducible verification.

A source file's existence does not establish deployment. A hash establishes byte identity, not semantic truth. A test suite passing does not establish that its tests are adequate.
