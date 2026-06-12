# AI log — PR #35 reprise: review and completion

Date: 2026-06-12.

## Intent

Review the ChatGPT-track reprise of PR #35
(`chatgpt/reprise-pr35-architecture-proof-register`) and complete the
protected-path registration its guardrail cannot perform, per the
maintainer's standing instruction on this track.

## What the branch brought (verified)

Six Architecture Proof Register schemas rebuilt on the baseline
conventions: YAML, `x-boundary` blocks, `governance_refs` defaults,
consequence migrated from the former `C0_administrative…C5_*` labels to
the **K0–K4 axis** referencing `schemas/shared_axes.schema.yaml`
(explicit note: C0–C5 is approval only), plus six examples.

## Completed in review

- **Unquoted YAML dates** in five examples parsed as `date` objects and
  failed `type: string` validation — quoted; all six examples now
  validate (Draft 2020-12).
- **Root test registration** (protected path): the six schema/example
  pairs added to `tests/test_governance_schemas.py` and
  `tests/test_schema_examples.py` — 7 root tests green.
- `schemas/README.md` lists the family.
- **Axis check refinement**: lines that explicitly attribute C to
  approval ("C0-C5 is approval only") are clarifications, not misuses;
  the check now skips them (same spirit as the GLOSSARY exemption).
- Merged current `main` into the branch.

## Boundary

Validation-only schemas; no runtime, storage, OCR, pgvector or
approval engine; protected-path edits limited to the two root test files
and `schemas/` per the reprise instruction. PR #35 is superseded and
closed with a pointer.
