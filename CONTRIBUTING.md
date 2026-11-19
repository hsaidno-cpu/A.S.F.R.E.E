# Contributing

## Before submitting

1. Read `LICENSE`, `LICENSE-STRATEGY.md` and `TRADEMARKS.md`.
2. Do not submit work unless you own it or have authority to contribute it under the project license.
3. Never submit API keys, passwords, tokens, private keys, customer data or unapproved target artifacts.
4. Open an issue or discussion for material architecture, licensing, compatibility or governance changes before broad implementation.

## Change requirements

- Preserve the user's/project's intent and existing valid behavior.
- Keep one clear responsibility per orchestrator/skill.
- Every material behavior change must map to a finding/requirement, a changed file, and an acceptance case.
- Keep evaluation and security as cross-cutting services.
- Distinguish declared, observed, tested and deployed capability.
- Add evidence and limitations; do not fabricate test/benchmark/runtime claims.
- Prefer a small coherent patch over unnecessary new agents or frameworks.

## Pull request checklist

- [ ] Scope and non-goals are explicit.
- [ ] License and contributor authority are clear.
- [ ] Skills have valid frontmatter and unique names.
- [ ] Shared references and paths resolve.
- [ ] Acceptance fixtures added/updated.
- [ ] Static validator passes.
- [ ] Security, privacy and prompt-injection implications reviewed.
- [ ] No secrets or private/customer data included.
- [ ] Limitations and unrun tests are disclosed.

A DCO/CLA mechanism is not yet configured. Until a formal contribution agreement is adopted, maintainers must verify contributor authority before accepting substantial third-party work.
