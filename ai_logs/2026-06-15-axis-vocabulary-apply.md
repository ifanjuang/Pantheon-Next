# AI Log — Apply axis vocabulary reconciliation (Lot E application)

Date: 2026-06-15

## Trigger

User approved applying `AXIS_VOCABULARY_RECONCILIATION_PROPOSAL.md` (Lot E
proposal). This carries out the two coordinated renames across the schema corpus
and the validated examples.

## Doctrine read first

- The proposal doc (the spec being applied).
- Mapped every `confidence` / `approval_impact` occurrence. Confirmed the
  read-only axis check's `BAD_FIELD` rule applies to YAML files only, so the
  rename scope is the schema corpus and YAML examples — prose and illustrative
  `.md` code blocks are out of scope and untouched.
- `schemas/register_candidate.schema.yaml` keeps its `confidence` field, which is
  explicitly documented as the legacy term superseded by certainty — left as is.

## Change (single coordinated rename)

`confidence` → `certainty` (field key + every `required` entry):
- `schemas/evidence_pack.schema.yaml` (property + required + one description line).
- `schemas/role_signal.schema.yaml` (property + required).
- `schemas/examples/evidence_pack.example.yaml`, `schemas/examples/role_signal.example.yaml`.
- `docs/examples/evidence_topology/evidence_pack_topology_examples.yaml` (all four field keys — the check reports only two because it dedupes by line text, but all four had to move).
- `schemas/README.md` documentation line.

`approval_impact` → `approval_ceiling` (field key + required entry):
- `schemas/evidence_pack.schema.yaml`, `schemas/role_signal.schema.yaml`.
- `schemas/task_contract_revision.schema.yaml` (property + required; enum values unchanged).
- `schemas/examples/evidence_pack.example.yaml`, `schemas/examples/role_signal.example.yaml`, `schemas/examples/task_contract_revision.example.yaml`.

The `C#` ceiling values and all enum values are unchanged; only field names move
to the canonical axis vocabulary owned by `GLOSSARY.md` (certainty axis; `C0–C5`
is the approval ceiling, distinct from the `K` consequence axis).

## Boundary

Declarative schema + example rename only. No runtime, migration, alias engine or
auto-resolution. `additionalProperties: false` objects keep matching names
because schema and example were renamed together.

## Verification

- `pytest tests/` (incl. `test_schema_examples.py` validating examples against
  schemas with `jsonschema`): **9 passed**.
- Absolute `check_axis_vocabulary` findings: 8 → **0**.
- No YAML field key `confidence:` / `approval_impact:` remains in the schema or
  example corpus (register_candidate's documented legacy field excepted).
- All four read-only checks with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings.
