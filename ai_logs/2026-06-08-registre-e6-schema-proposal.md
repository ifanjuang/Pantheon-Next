# AI log — E6: Registre Probatoire schema rename proposal

Date: 2026-06-08.

## Intent

Prepare the sixth downstream step (E6) of the Registre Probatoire direction
without touching any protected path: a proposal to rename the
`memory_candidate` schema to `register_candidate` and align its fields to the
Registre Probatoire, ready for explicit approval.

## What was produced

`docs/governance/REGISTRE_PROBATOIRE_SCHEMA_PROPOSAL.md` (validation-only),
specifying:

- the files to rename/edit once approved (`schemas/memory_candidate.schema.yaml`
  and its example, `tests/test_governance_schemas.py`,
  `tests/test_schema_examples.py`, `schemas/README.md`);
- the field mapping: keep most fields; rename `confidence` (low/medium/high) to
  `certainty` (E0–E4, the GLOSSARY axis); add optional Registre provenance fields
  (dates, citation, exhibits); keep deprecated aliases during migration;
- the full proposed schema and example, printed inside the note (not as
  executable files);
- a clean-rename migration approach (recommended) and an approval checklist.

## Boundary

Documentation only. No file under `schemas/`, `tests/`, `operations/`,
`platform/`, `pyproject.toml`, Docker or `.env` was changed. The rename is
applied only after the maintainer approves this proposal. The PR is kept as a
draft for that reason. Verified clean against the governance forbidden-phrase
lint.
