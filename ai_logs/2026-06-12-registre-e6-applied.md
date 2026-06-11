# AI log — E6 applied: register_candidate rename + spine schemas completed

Date: 2026-06-12.

## Intent

Complete the E6 application started on the ChatGPT track (`chatgpt/reg-e6`),
per the approved proposal in `REGISTRE_PROBATOIRE_SCHEMA_PROPOSAL.md`
(PR #87) and the maintainer's instruction to verify, fix and merge.

## What the branch brought

Five new validation-only schemas with x-boundary markers:
`register_candidate` (certainty E0–E4, provenance fields, deprecated
`confidence` alias), `shared_axes` (the E/V/K/C axes), `capability_passport`,
`policy_decision`, `answer_status` — plus one example (shared_axes).

## What was completed in review

- **Option A clean rename finished**: `schemas/memory_candidate.schema.yaml`
  and its example removed (the branch had only added the new schema).
- **Examples added** for the four schemas that lacked one; all five validate
  against their schemas (Draft 2020-12).
- **Root tests updated** (`tests/test_governance_schemas.py`,
  `tests/test_schema_examples.py`): renamed pair swapped, the five new
  schemas added to the mappings — 7 tests green.
- **`schemas/README.md`** listing updated.
- **Three doctrine references** to the old path updated with a
  "formerly memory_candidate" note (MEMORY.md, REGISTRE_PROBATOIRE_DIRECTION.md,
  ROADMAP.md) — caught by the Lot 1 internal-links check.
- **Axis check fixed** to honor its own documented exception: a
  `confidence:` field explicitly marked deprecated/legacy in context is
  allowed (the new schema's deprecated alias tripped it).

## Verification

7 root tests green; the four Lot 1 checks and both legacy lints green with
baseline `origin/main`; all five examples validate.

## Boundary

Protected-path edits (`schemas/`, `tests/`) are exactly those specified by
the approved E6 proposal checklist. No runtime, no approval engine, no
memory promotion; every schema keeps its x-boundary block.
