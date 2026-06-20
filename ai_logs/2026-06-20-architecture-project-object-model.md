# 2026-06-20 architecture project object model

Status: documented non-implemented (candidate doctrine + validation schemas).

Added the project object model as a documentation-only sister PR (branch
`docs/apu-object-model`, based on `main`), answering the review of PR #163: the
belief contract is a good governance layer but lacked the métier object vocabulary
to describe a project. Sibling of #163 (belief contract) and #164 (external
references); does not modify them.

Added:

- `docs/governance/ARCHITECTURE_PROJECT_OBJECT_MODEL.md`: doctrine — describe the
  world, reference the registers; identity is not the name; nine objects;
  governance invariants;
- schema family additions under `schemas/architecture-project-understanding/`:
  `spatial_node`, `object_identity`, `object_relation`, `object_group`,
  `property_set`, `instance_override`, `object_note`, `phase_state`,
  `analysis_context_candidate`;
- fictional examples (incl. the "prise hotte" relation, the doors 21/23/24 shared
  EI30 property set with an EI60 per-instance override, a transversal night-care
  zone spanning levels, and a renamed-door identity with aliases/name_history);
- test-suite registration in both test files; `schemas/README.md` and
  `AUTHORITY_INDEX.md` entries.

Doctrine decisions encoded (from the review arbitration):

- the project base describes the world and references — never embeds — the
  Pantheon registers (evidence/doubt/contradiction/decision/approval/
  canonization stay in the belief contract + proof register); references travel as
  `*_ref` / `source_refs` / `register_refs` ids ("reference, not centralize");
- internal identity (`object_identity`) is independent of names, room/door numbers
  and source ids (IFC GlobalId, Revit ElementId), which are sources/evidence;
- relations are typed and may be qualified; containment is not the only relation;
- zones are typed and may be transversal (cross levels, group non-contiguous
  objects); physical tree plus transversal groups, never a tree alone;
- properties stay semi-structured: core + property sets + per-instance overrides;
- the model carries `analysis_context_candidate`, never a normative conclusion;
  norms are activated downstream by domain packs;
- phase state is descriptive project data, distinct from any decision.

No runtime, extraction, OCR, vision, solver, registry write, approval engine,
memory promotion or external action was added.
