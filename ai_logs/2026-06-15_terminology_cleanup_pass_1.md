# AI log — terminology cleanup pass 1

Date: 2026-06-15

## Request

User said "Allons y" after adding `TERMINOLOGY_BOUNDARIES.md`, understood as starting a first progressive cleanup of existing terminology.

## Coordination checked

Read issue #41 and its accepted disposition before changing more files. It states:

- prefer PRs over direct-to-main for significant changes;
- pause new governance-document creation;
- still allow corrections, indexation, reconciliation, review responses and status clarification.

Therefore this pass was made on branch `docs/terminology-cleanup-pass-1` and does not create new governance doctrine.

## Sources read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/TERMINOLOGY_BOUNDARIES.md`
- `docs/governance/CORE_CONCEPTS_MAP.md`
- `docs/governance/DOSSIER_SITUATION_INTAKE.md`
- `docs/governance/WORKFLOW_FORGING_PROTOCOL.md`
- GitHub issue #41 and its disposition comment

## Changes made

Updated:

- `docs/governance/CORE_CONCEPTS_MAP.md`
- `docs/governance/DOSSIER_SITUATION_INTAKE.md`
- `docs/governance/WORKFLOW_FORGING_PROTOCOL.md`

No protected path was touched.

## Cleanup decisions

Accepted:

- Add `TERMINOLOGY_BOUNDARIES.md` into the stable read path of `CORE_CONCEPTS_MAP.md`.
- Replace the system-level wording `Minimal dossier flow` with `Minimal Case flow` while preserving public `dossier` as an allowed alias when unambiguous.
- Clarify that `Register Candidate` carries a durable Assertion, not a generic claim.
- Clarify that repeated material is not Register.
- Clarify that `Dossier Situation Intake` remains a legacy/public-facing label and should be read as Case/Situation intake.
- Clarify `Approach / Démarche` vs `Workflow Candidate` in the forging protocol.
- Add `approach_family` as documentary/explanatory wording only, explicitly not a schema change.

Refused:

- Broad automatic renaming of all existing `workflow` occurrences.
- File renaming.
- Schema or test changes.
- New governance documents.

To verify:

- Whether later PRs should migrate `dossier_situation_brief` identifiers or keep them as compatibility names.
- Whether `Workflow Candidate` remains the best term for runtime-facing generated plans once schema work resumes.

## Repo state

Documented non-implemented.

This pass clarifies terminology only. It does not implement runtime behavior, schema changes, linter checks, memory behavior or approval behavior.
