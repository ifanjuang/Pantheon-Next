# 2026-06-21 Promote property vocab to shared catalogue

Status: implemented (schema + doc; no behavior change).

Follow-up to the APU $defs factoring (#185): `value_type` and `property_status`
were duplicated identically between two object-model schemas (`property_set` and
`instance_override`) but had no counterpart in the family's shared catalogue, so
they were left local rather than collapsed. Per the work rules (document the
governance change first), this promotes them to shared vocabulary.

Changes:

- docs/governance/ARCHITECTURE_PROJECT_OBJECT_MODEL.md — documents `value_type`
  and `property_status` as shared, source-agnostic definitions with their enum
  values, so the Markdown source of truth records the vocabulary the schemas now
  share (rather than two private copies).
- schemas/architecture-project-understanding/shared.schema.yaml — adds a new
  "Object-model property vocabulary" `$defs` block:
  - `value_type`: [controlled_label, number, boolean, text, range, reference];
  - `property_status`: [candidate, specified_candidate, observed, to_verify,
    reviewed, rejected].
- property_set.schema.yaml — `value_type` and `status` now
  `$ref: "shared.schema.yaml#/$defs/..."`; local `$defs` removed.
- instance_override.schema.yaml — `status` now references shared; local `$defs`
  removed.

These were the only object-model-only duplicates flagged in #185's ai_log; the
APU family now has no duplicated `$defs` left. Drift between the two property
status copies is no longer possible.

Validation: tests/test_governance_schemas.py + tests/test_schema_examples.py
9 passed; check_apu_referential_integrity.py (16) and
check_register_instances.py (5) green; mcp-server suite 33 OK; status_headers /
internal_links / index_coverage clean; check_axis_vocabulary green vs baseline.

Boundary: governance-core schema + doc change. No runtime, no module behavior
change, one-way dependency intact.
