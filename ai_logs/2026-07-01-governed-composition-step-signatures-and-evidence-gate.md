# AI log — governed_composition: complete signatures + conditional evidence gate (#218)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Re-land the governed-composition schema fields (#218, stranded when PR #53 closed)
on current `main`, and harden them per the maintainer's three tasks:

1. make the `capability_steps` signatures complete;
2. make V/E mandatory when `post_execution_evidence.required = true`;
3. add negative tests.

## Change

- Rebased the #218 branch onto current `main` (it was 144 commits behind); resolved
  the one CHANGELOG conflict by keeping main's changelog and writing a fresh 0.1.60
  entry.
- `schemas/workflow_manifest.schema.yaml`:
  - `capability_steps.items.required` now covers the full governance signature
    (`capability_id`, `declared_scope`, `forbidden_scope`, `required_task_contract`,
    `evidence_pack_shape`, `approval_ceiling`, `register_behavior`, `risk_class`,
    `refusal_tests`); `skill_manifest_ref` and `depends_on` stay optional.
  - `post_execution_evidence` gains an `if/then`: when `required` is `true`,
    `answer_verification` (V0–V4) and `probative_certainty` (E0–E4) are required.
- `tests/test_schema_examples.py`: three new tests — incomplete step signature is
  rejected (each required field, plus an unknown property), a required evidence gate
  missing V or E is rejected while `required: false` may omit them, and a bad gate
  decision enum is rejected.
- `VERSION` / `pyproject.toml` / `mcp-server/pyproject.toml` -> `0.1.60` (B-7 invariant).

## Validation

`python3 -m pytest tests/` -> 12 passed (positive example + the new negatives).
Runtime-phrase guard green.

## Boundary

Protected `schemas/` + `tests/` change, explicitly authorized by the maintainer.
Structure only — no forge engine, dispatch, scheduling or memory promotion. A forged
manifest stays a candidate; `forged != authorized`, `completed != approved`.
