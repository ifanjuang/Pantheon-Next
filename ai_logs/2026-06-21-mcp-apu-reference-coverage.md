# 2026-06-21 Harden mcp-server APU validation reference coverage

Status: implemented (bounded read-only mcp-server tool; tests added).

Follow-up to #184. The `validate_apu_dossier` tool indexed only 12 of the 25 APU
object types and only resolved references for the conformance subset
(attribute_claim / requirement / deviation). References *into* project
object-model objects (relations, property sets, overrides, groups, spatial
nodes) were never checked, and ids of object-model objects were not indexed — so
a valid in-dossier reference to one of them could not resolve.

Changes (mcp-server/pantheon_mcp/apu.py):

- `_ID_FIELD` now covers all 25 object types (id field = each schema's first
  required field), so any in-dossier reference can resolve. object_identity
  (object model, `stable_id`) and stable_object (belief contract,
  `stable_object_id`) are distinct identities and both index. Completing the
  index can only turn a would-be "unresolved" into "resolved" — it never creates
  a new error.
- Added `_ref` / `_refs` reference helpers and object-model reference checks:
  object_relation.from/to, property_set.applies_to, instance_override.target +
  overrides (property_set id prefix), object_group.members, object_note
  .target_object, phase_state.target, analysis_context_candidate.target,
  spatial_node.parent_id + member_object_ids, classification.about
  (stable_object_id / space_group_id), program_change.target_program,
  space_group.parent_group_id / members / requirement_ids. All tolerate the
  documented external prefixes and absent fields; only an in-dossier-looking id
  that does not resolve is an error.
- Unresolved-reference messages now include the offending id consistently
  (matching how derived_from already reported), which is more actionable.

Tests (mcp-server/tests/test_apu.py): a coherent object-model dossier (8
objects: two object_identity, object_group, property_set, instance_override,
object_relation, two spatial_node) validates with every reference resolving;
a dangling object_relation target is reported. Adjusted one existing assertion
to match the value-inclusive message format. Suite: 35 OK (was 33).

Boundary unchanged: read-only, candidate-only, the gate/human decides. No
execution, routing, scheduling or approval. One-way dependency intact.
