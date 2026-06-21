# 2026-06-21 APU $defs factoring — program/conformance + object model

Status: implemented (schema refactor; no behavior change).

Completes the incremental migration deferred after #173: the program/conformance
and object-model schemas in `schemas/architecture-project-understanding/` no
longer re-declare definitions that already live in the family's
`shared.schema.yaml`. Each duplicated local `$def` is replaced by a cross-file
`$ref: "shared.schema.yaml#/$defs/X"`, resolved through the
`referencing.Registry` that every validation path already builds (CI doctor
scripts, root pytest, and the mcp-server APU tool). This removes drift: the
shared catalogue is now the single source for these enums and shapes.

Factored to shared (only true duplicates of an existing shared `$def`):

- program.schema.yaml — human_ref, scope_type, proof_status,
  source_authority_level (local `$defs` removed).
- requirement.schema.yaml — human_ref, claim_modality, scope_type, proof_status,
  source_authority_level (kept local: requirement_kind, req_target).
- deviation.schema.yaml — uuid, locator, evidence_ref (kept local:
  resolution_option, resolution_state — deviation-specific, distinct from the
  shared resolution_action acquisition vocabulary).
- program_change.schema.yaml — uuid, date, source_authority_level, locator,
  evidence_ref (local `$defs` removed; the inline change_kind add/modify/remove
  stays — it is distinct from the shared spatial-lifecycle change_kind).
- space_group.schema.yaml — human_ref, claim_modality, proof_status (removed).
- classification.schema.yaml — uuid, claim_modality, proof_status,
  source_authority_level, locator, evidence_ref (kept local: class_target).
- classification_scheme.schema.yaml — schema_status (removed).
- spatial_node.schema.yaml — human_ref (kept local: node_kind, zone_type).
- object_identity.schema.yaml — human_ref, date (removed).
- object_note.schema.yaml — date (kept local: note_type, visibility,
  note_status).
- object_group.schema.yaml — human_ref (removed).

Deliberately left local (schema-specific, or duplicated only among object-model
schemas with no shared counterpart — promoting these to shared would add new
shared vocabulary and should follow a doc update first): requirement_kind,
req_target, deviation resolution_option/resolution_state, program_change inline
change_kind, classification class_target, spatial_node node_kind/zone_type,
object_note note_type/visibility/note_status, object_relation relation_type,
property_set value_type/property_status, instance_override property_status,
phase_state state, analysis_context_candidate status.

The 9 core APU schemas were already factored (#173); this finishes the family.

Validation: tests/test_governance_schemas.py + tests/test_schema_examples.py
9 passed; check_apu_referential_integrity.py (16 instances) and
check_register_instances.py (5 instances) green; mcp-server suite 33 OK;
check_status_headers / check_internal_links / check_index_coverage clean;
check_axis_vocabulary green against the baseline (no new occurrences).

Boundary: pure governance-core schema change. No runtime, no module behavior
change, one-way dependency intact.
