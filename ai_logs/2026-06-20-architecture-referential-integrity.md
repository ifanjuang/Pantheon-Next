# 2026-06-20 architecture project understanding referential integrity

Status: documented non-implemented (example + read-only check; no schema change).

Addresses the highest-value, non-schema-touching item of issue #169 ("add
referential-integrity controls for ids and refs, otherwise provenance chains
cannot be trusted"), and provides the schema-conformant counterpart to the shape
sketch in PR #168.

Added:

- `docs/examples/architecture_project_understanding_dossier/`: one coherent,
  fictional, end-to-end project dossier (Résidence Les Tilleuls) expressed only
  with the existing v0.1 `architecture-project-understanding` schemas — program,
  requirements, calibration → derivation → evidence → observed attribute_claim,
  stable_objects, object_identity, object_relation, spatial_node, space_group, a
  bedroom-area deviation (8.4 < 9 m²) and a human_override (door, not window);
- `.github/scripts/check_apu_referential_integrity.py`: read-only check that
  validates every dossier instance against its real schema and verifies that ids
  and references resolve, tolerating known external prefixes (SRC-, DET-, EQ-,
  SYS-, OP-CAND-); plus one invariant (a deviation targets a required
  requirement);
- a new Governance CI step running that check (installs jsonschema/pyyaml like
  the register-instance step).

Boundary and scope respected:

- no change under `schemas/` (issue #169 requires explicit approval for that);
- the certainty unification (`certainty_score` vs `E0–E4`), `$defs` factoring and
  the `zone_type`-when-zone requirement remain open in #169, to arbitrate /
  approve before any schema patch;
- this PR demonstrates the family is internally coherent on a real case and makes
  that coherence machine-checked, which is what #168's non-conformant example
  could not do.

No runtime, extraction, OCR, vision, registry write, approval engine, memory
promotion or external action was added.
