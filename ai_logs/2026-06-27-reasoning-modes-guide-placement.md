# AI Log — Reasoning modes library placement remediation

Date: 2026-06-27

Actor: Claude (claude-opus-4-8)

## Context

Repository verification of recent ChatGPT-attributed work surfaced
`schemas/reasoning_mods.json`: a 1490-line reasoning-mode library (meta / 61
tools / selector / controls) added directly to `main` via the GitHub web editor
(commits "Create reasoning_mode.json" → "Delete" → "Create reasoning_mods.json"),
bypassing PR and CI.

Anomalies: it is content, not a JSON Schema, yet placed in `schemas/` (a
protected implementation path); it is orphaned (nothing references it); it is
ungoverned (absent from AUTHORITY_INDEX.md, no accompanying doc, no status); its
`$schema` URI is malformed; and it encodes a Métis selector/controls
orchestration design without governance classification.

The architect chose: treat it as a candidate Guide de compétence, in two pieces.

## Change made

Moved:

- `schemas/reasoning_mods.json` -> `templates/competence/reasoning_modes_guide_candidate.json`
  (`templates/` is the non-protected reusable-artifact zone, grouped in
  `check_index_coverage`; `competence/` matches `COMPETENCE_MODEL.md`). Renamed
  to drop the erroneous "mods".

Edited (resource header):

- removed the misleading `$schema` key; added `_artifact` (states it is a Guide
  de compétence candidate, not a JSON Schema) and `_status: candidate`, pointing
  to the governance frame.

Created:

- `docs/governance/REASONING_MODES_LIBRARY.md` — candidate support doctrine
  classifying the resource as a Guide de compétence and setting the hard
  boundary: the selector/controls are an advisory description, not a
  router/agent/executor; no automatic selection or execution in the governance
  core; any runnable selector lives Hermes-side; a prescribed mode is a prompt
  injection that validates/approves/canonizes nothing.

Updated:

- `docs/governance/AUTHORITY_INDEX.md` — index the new note (the JSON is covered
  by the grouped `templates/` row).

## Boundary preserved

Documentation + a relocated candidate resource. Removing a file from `schemas/`
is the remediation of a misplacement, done by PR (not direct to main) under
explicit architect approval. No new schema, runtime, selector engine,
orchestrator, agent, approval engine or memory engine. No `tests/`,
`operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md`
change. No external action. No Registre Probatoire entry. Nothing promoted.

## Repo state

Documented non-implemented (governance frame + candidate Guide de compétence).

## Decision status

Accepted:

- treat the reasoning-mode library as a candidate Guide de compétence;
- relocate it out of `schemas/`, classify and index it, fix the `$schema` defect.

To verify / to arbitrate (left to the human):

- generic vs per-domain split of the library;
- whether any mode becomes a Hermes skill later;
- whether a small JSON shape check belongs in `tests/` later (not now).
