# Axis Vocabulary Reconciliation Proposal

Status: validation-only — coordinated schema + example proposal, applied only after approval.

Date: 2026-06-15

## Purpose

Reconcile two residual axis-vocabulary deviations in the schema corpus with the
E/V/K/C axes owned by `GLOSSARY.md`. This is a declarative proposal: it defines
the target state and the exact edits, applies nothing, and adds no runtime,
migration or auto-resolution.

## Canonical axes (owned by `GLOSSARY.md`)

- `E0–E4` — probative certainty.
- `V` — answer verification (never `C`).
- `K0–K4` — consequence level.
- `C0–C5` — approval ceiling.

A certainty level is not an approval, not an answer-verification level and not a
consequence level. `K` and `C` are deliberately split so consequence never
collides with the approval ceiling.

## Why this is a coordinated proposal, not piecemeal example edits

`confidence` is a **required** property in `evidence_pack.schema.yaml` (evidence
item) and `role_signal.schema.yaml`, and `tests/test_schema_examples.py`
validates `schemas/examples/evidence_pack.example.yaml` and
`schemas/examples/role_signal.example.yaml` against those schemas with
`jsonschema`. Renaming the field in the examples alone would produce examples
that violate their own schema's `required` list. The rename is therefore
intrinsically atomic across schema and example and must land together, under
review — never as an example-only edit.

## Reconciliation A — `confidence` → `certainty`

The probative-certainty axis is named `certainty` and owned by `GLOSSARY.md`.
`schemas/register_candidate.schema.yaml` already records `confidence` as a
"Legacy confidence flag superseded by certainty", so the direction is settled;
this proposal extends it to the remaining schemas and their examples.

Proposed edits (apply atomically):

- `schemas/evidence_pack.schema.yaml` — rename the evidence-item property
  `confidence` to `certainty`, including its entry in the item `required` list.
- `schemas/role_signal.schema.yaml` — rename the top-level property `confidence`
  to `certainty`, including its entry in the top-level `required` list.
- `schemas/examples/evidence_pack.example.yaml` — rename the field key.
- `schemas/examples/role_signal.example.yaml` — rename the field key.
- `docs/examples/evidence_topology/evidence_pack_topology_examples.yaml` —
  rename the field key (2 occurrences) so the documentary corpus stays
  consistent with the schema.

The enum values (`low` / `medium` / `high`, `partial`, etc.) are unchanged; only
the field name moves to the canonical axis term.

## Reconciliation B — `approval_impact` → `approval_ceiling`

`approval_impact` carries a `C` value (e.g. `C3`). Per `GLOSSARY.md`, `C0–C5` is
the **approval ceiling**, so the value is on the correct axis — but the field
name reads as a consequence ("impact"), which collides with the `K` consequence
axis and trips the read-only axis check. Renaming the field to
`approval_ceiling` removes the collision and states the axis plainly.

Proposed edits (apply atomically):

- `schemas/evidence_pack.schema.yaml` — rename property `approval_impact` to
  `approval_ceiling`.
- `schemas/role_signal.schema.yaml` — rename property `approval_impact` to
  `approval_ceiling`.
- `schemas/task_contract_revision.schema.yaml` — rename property
  `approval_impact` to `approval_ceiling`, including its `required` entry.
- The corresponding example files — rename the field key and keep the existing
  `C#` ceiling value and descriptive text.

## Boundary

This proposal decides nothing on its own. It is read-only direction; the edits
above are a single reviewable change applied through the normal approval path.
No engine, migration, alias runtime or auto-resolution is created.
