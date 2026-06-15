# AI Log — Axis vocabulary reconciliation proposal (Lot E)

Date: 2026-06-15

## Trigger

Lot E of the governance-hygiene pass (map in
`GOVERNANCE_LINKAGE_RECONCILIATION.md`, #138). Eight `check_axis_vocabulary.py`
findings across schemas and examples.

## Doctrine read first

`GLOSSARY.md` owns the axes: `E0–E4` certainty, `V` answer verification,
`K0–K4` consequence, `C0–C5` approval ceiling. Confirmed `confidence` is a
**required** property in `evidence_pack.schema.yaml` and `role_signal.schema.yaml`,
and that `tests/test_schema_examples.py` validates the matching examples against
those schemas with `jsonschema`.

## Corrected approach

The user initially chose "edit examples, propose schemas". Investigation showed
that path is not viable for the `confidence` findings: because `confidence` is a
required schema property and the examples are schema-validated, renaming it in
the examples alone would produce examples that violate their own schema. The
`approval_impact` findings are likewise schema-level (the field is defined in
`evidence_pack`, `role_signal` and `task_contract_revision` schemas). Surfaced
this; the user then chose a single coordinated proposal.

## Change

- Added `docs/governance/AXIS_VOCABULARY_RECONCILIATION_PROPOSAL.md`
  (Status: validation-only). It specifies two atomic schema + example edits to be
  applied only after approval:
  - **A.** `confidence` → `certainty` (probative-certainty axis term;
    `register_candidate.schema.yaml` already records `confidence` as legacy
    superseded by certainty).
  - **B.** `approval_impact` → `approval_ceiling` (the `C#` value is already the
    correct approval-ceiling axis; the field name read as a consequence and
    collided with the `K` axis).
- Excluded the new proposal doc from `check_axis_vocabulary.py` (its before/after
  vocabulary would otherwise self-trigger), consistent with the existing
  exclusion of `SHARED_AXES_PROPOSAL` / `REGISTRE_PROBATOIRE_SCHEMA_PROPOSAL`.
- Added an `AUTHORITY_INDEX.md` row for the proposal.

## Boundary

Documentation proposal + one check exclusion. No schema or example edited; the
rename is deferred to a single reviewable change through the approval path. No
runtime, migration or alias engine.

## Verification

- The 8 axis findings remain as a pending governed proposal by design (schemas
  are protected; the rename is coupled and must be approved).
- The proposal doc does not self-trigger the axis check (excluded).
- All four read-only checks with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings.
