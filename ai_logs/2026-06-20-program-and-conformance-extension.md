# 2026-06-20 program and conformance extension

Status: documented non-implemented (candidate doctrine + validation schemas).

Extended the Architecture Project Understanding belief contract with a
program-as-source and conformance layer, following the design discussion
(program-only / partial birth, écart vs program, multiple typologies, composite
and multi-level identities). Governance/documentation only — no runtime.

Added:

- `docs/governance/PROGRAM_AND_CONFORMANCE.md`: the extension doctrine (modality
  axis, typed/layered/versioned program, email-triggered program_change,
  requirements, multi-scheme extensible classification, composite multi-level
  groups, per-kind attribute vocabulary, deviation with bidirectional
  resolution, governance invariants);
- schema family additions under `schemas/architecture-project-understanding/`:
  `program`, `requirement`, `classification`, `classification_scheme`,
  `space_group`, `program_change`, `deviation`;
- core additions: `modality` on `attribute_claim`; `spans_levels` and a
  `cross_level` match axis on `stable_object`;
- fictional examples (including the end-to-end "8 T2 required / 6 observed"
  deviation and an email-triggered program change);
- test-suite registration in both test files; `schemas/README.md`,
  `AUTHORITY_INDEX.md` and core-doc cross-references.

Doctrine decisions encoded:

- intent vs state is an explicit `claim_modality` (required/proposed/observed/
  as_built); deviation = required without observed, or observed contradicting
  required;
- classification schemes are registered and extensible, not a hard-coded
  taxonomy; a regulatory classification grounds a conclusion only via
  `regulatory_claim` (L5);
- a `program_change` is never auto-applied; it is a candidate through the gate;
- a `deviation` is never resolved by the system; resolution is bidirectional
  (amend_design / amend_program / accept_deviation), and a waiver
  (accept_deviation) must be justified and attributed;
- vertical identity (duplex, lift shaft, stairwell, curtain wall) via
  `spans_levels` and the `cross_level` matching axis.

No runtime, extraction, OCR, vision, solver, scheduler, conformance engine,
registry write, approval engine, memory promotion or external action was added.
