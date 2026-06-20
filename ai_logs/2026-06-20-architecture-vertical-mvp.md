# 2026-06-20 — Architecture vertical MVP slice

Status: validation trace — documented non-implemented.

## Context

The Architecture Project Understanding belief contract and project object model were added as candidate v0.1 doctrine and validation artifacts. A follow-up critique recommended stopping ontology expansion and confronting the model with a real vertical slice:

```text
PDF → rooms + doors → delta against a five-line program → human correction
```

## Active sources reviewed

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING.md`
- `docs/governance/ARCHITECTURE_PROJECT_OBJECT_MODEL.md`
- recent PR and review context for #163, #165, #166, #167

## Decision

Accepted:

- freeze doctrine for this topic during the slice;
- treat existing project-understanding schemas as v0.1 hypotheses, not final ontology;
- materialize one narrow MVP slice through non-executable templates;
- keep adapter execution outside Pantheon;
- require human correction as a visible gate;
- record ontology feedback rather than adding new objects during the slice.

To verify:

- `zone_type` should be required when `node_kind` is `zone` before schema reliance;
- referential-integrity controls are missing for ids and refs;
- duplicated `$defs` should be factored if the schema family remains foundational;
- `certainty_score` versus `E0–E4` remains unresolved and must be reduced to one representation.

Refused:

- adding new ontology objects before the vertical slice;
- turning the MVP into regulatory compliance checking;
- placing PDF extraction/OCR/vision runtime inside Pantheon.

## Files added

- `templates/architecture_vertical_mvp/README.md`
- `templates/architecture_vertical_mvp/program_5_lines.md`
- `templates/architecture_vertical_mvp/result_candidate.example.yaml`
- `templates/architecture_vertical_mvp/human_correction_sheet.md`

## Repository state

Documented non-implemented.

No `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env` or `pyproject.toml` changes were made.

## Next action

Run the slice on one real project PDF and record:

```text
source inventory
five-line program
rooms/doors Result Candidate
Evidence Pack Candidate
program delta
human correction sheet
ontology feedback
Zeus decision
```
