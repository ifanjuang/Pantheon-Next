# Architecture Project Understanding — worked dossier (schema-conformant)

Status: example — fictional, candidate-only, schema-conformant fixture.

This is one small, coherent, end-to-end project dossier ("Résidence Les
Tilleuls") expressed **only with the existing v0.1 schemas** of
`schemas/architecture-project-understanding/`. Its purpose is to confront the
belief contract + project object model with one concrete case and to give the
referential-integrity check a real fixture.

It addresses issue #169 ("add referential-integrity controls for ids and refs")
**without changing any schema**. The check that validates this dossier is
`.github/scripts/check_apu_referential_integrity.py` (wired into Governance CI):
it validates every file against its real schema and verifies that ids and
references resolve.

## What it threads

```text
program (5-line intent) ── requirement (required) ── deviation (écart) → human gate
source SRC-042 → calibration → derivation → attribute_claim (observed) → stable_object
stable_object (spaces, opening) ── object_relation ── space_group (T2) ── spatial_node (level)
opening identity (aliases / name_history) + human_override (door, not window)
```

The headline case: the bedroom area is **observed 8.4 m² < required 9 m²**, so a
`deviation` (`area_below_min`) is raised and left `pending_human` with
bidirectional resolution options.

## Status of the schemas it uses

These schemas are **v0.1 hypotheses** (per #168/#169), explicitly revisable by the
first real adapter. This dossier is the conformant counterpart to the
non-conformant shape sketch in `templates/architecture_vertical_mvp/`. It is not
doctrine promotion and decides nothing.

## Known schema debt (tracked in #169, not solved here)

- factor duplicated `$defs`;
- single certainty representation — **resolved (decision A)**: governance certainty is `E0–E4`, banded from a numeric score that lives only in `derivation.produced_certainty_score`;
- require `zone_type` when `node_kind` is `zone`.

These require explicit approval before any `schemas/` change.
