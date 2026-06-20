# 2026-06-20 architecture project understanding belief contract

Status: documented non-implemented (candidate doctrine + validation schemas).

Froze the "Architecture Project Understanding" belief contract discussed from a
shared ChatGPT design note, after two rounds of critique and enrichment.

Scope of intervention (governance/documentation only — no runtime):

- added `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING.md`: the belief
  contract (placement, five laws, nine core objects, three time axes,
  responsibility axis, aligned vocabulary, governance invariants, out-of-scope
  extensions, evaluation);
- added schema family `schemas/architecture-project-understanding/`:
  `shared`, `stable_object`, `attribute_claim`, `calibration`, `derivation`,
  `evidence`, `doubt`, `contradiction`, `human_override`, `canonization`;
- added fictional examples under
  `schemas/examples/architecture-project-understanding/`;
- registered the new family in `tests/test_governance_schemas.py` and
  `tests/test_schema_examples.py`, and in `schemas/README.md`.

Doctrine decisions encoded (from the critique):

- no `can_support_regulatory_claim` boolean; the regulatory right is the new
  `regulatory_claim` `use_type`, opened only by the gate (L5), enforced by an
  `allOf` requiring `approved_for_contractual_action` + evidence;
- status / source-authority / use vocabularies reuse the proof register
  (no parallel enum); the flat `raw..canonical_active` ladder was dropped;
- object identity (`stable_object.matches`) is modeled as a probative candidate;
  the diff runs only on confirmed matches;
- confidence/tolerance are derivation outputs (provenance DAG), not hand inputs;
- calibration is gated and multi-witness; divergence caps proof at
  `requires_more_evidence`;
- contradictions are held, never auto-resolved; human corrections are governed
  overrides routed through the chokepoint, never source writes.

Schemas are self-contained (local `$defs` only) to match the proof-register
convention and the standalone validator in the test suite.

No runtime, extraction engine, OCR, vision model, Revit plugin, MCP server,
registry write, approval engine, memory promotion or external action was added.
The execution side remains in separate `ifj-*` repositories per the contract.
