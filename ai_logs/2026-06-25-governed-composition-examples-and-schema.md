# AI Log — Governed composition: examples and schema fields (re-land)

Date: 2026-06-25

## Scope

Re-landed onto current `main` the parts of the governed-composition work that were
stranded when PR #53 was closed without merge: two end-to-end examples and the
`governed_composition` schema fields. The composition *doctrine*
(`WORKFLOW_SCHEMA.md` "Governed composition", `CAPABILITY_REGISTRY.md`, reference
reviews, role-registry entries) had already reached `main` and was evolved further,
so the schema here is aligned to the doctrine on `main`, not to the older draft.

## Added

- `docs/examples/governed_composition_cerfa/` — composition mechanics on the CERFA
  dossier (registry declarations, forged manifest with per-step signatures, two
  gates, retrieve/reuse/revise/retain with a governed cap revision).
- `docs/examples/governed_composition_marche_public/` — reuse on a DC1/DC2
  candidature: eight capabilities reused, one added; the fan-out gains one branch.

## Changed

- `schemas/workflow_manifest.schema.yaml`: optional `governed_composition` object,
  aligned with main's doctrine — gate decision enum
  (allow / allow_with_gate / block / needs_revision / needs_evidence), V0–V4 answer
  verification, E0–E4 probative certainty, `approval_ceiling` C0–C5,
  `register_behavior`, refusal tests, declared/forbidden scope, required Task
  Contract, `skill_manifest_ref` join and shared risk scale (low/medium/high/critical).
- `schemas/examples/workflow_manifest.example.yaml`, `schemas/README.md`,
  `docs/governance/CAPABILITY_REGISTRY.md` (shared-vocabulary subsection),
  `docs/examples/README.md`.

## Why a fresh branch

PR #53's branch (`claude/review-recent-changes-flSzY`) is closed and far behind
`main`. The user chose to re-land on a new branch off current `main`. The
actively-developed `skill_manifest.schema.yaml` and the SkillsGate section of
`CAPABILITY_REGISTRY.md` are left untouched; the alignment references them.

## Validation

- `jsonschema` draft 2020-12 check and example validation pass;
- negative checks: gate `decision` enum and step `additionalProperties: false`
  enforced;
- `tests/test_schema_examples.py` — passes;
- governance forbidden-phrase lint (CI scope) — clean.

## Boundary

Structure, doctrine cross-reference and examples only. No execution, dispatch,
installation or memory promotion. forged != authorized; completed != approved;
returned != a Registre Probatoire entry.
