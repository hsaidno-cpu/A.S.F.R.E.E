# Workflow and Status — Compatibility Entry

This compatibility file is retained for earlier A.S.F.R.E.E references. The canonical lifecycle and recovery rules now live in `lifecycle-and-recovery.md`; the authoritative authority levels and action controls live in `security-and-authority.md`; and M00 routing/decision rules live in `../skills/asfree-master-orchestrator/SKILL.md`.

Do not define competing lifecycle enums here. When a status changes, update the canonical reference, relevant JSON Schema, and migration notes together.

## Core rule

Never infer a later state from an earlier one. `IMPLEMENTED` is not `VERIFIED`; `PR_OPEN` is not `MERGED`; `MERGED` is not `DEPLOYED`; and `DEPLOYED` is not proof of outcome or impact.
