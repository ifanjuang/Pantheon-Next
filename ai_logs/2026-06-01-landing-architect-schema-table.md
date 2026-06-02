# AI Log — Landing page: architect schema + table, other professions to-study

Date: 2026-06-01

## Scope

Per user direction, kept architecture as the only fully detailed profession,
marked the other professions as "à l'étude" (envisageable but needing a
practitioner's input first), and enriched the architect dropdown with a flow
schema and a table, readable by liberal professionals. The page stays oriented
to liberal professions (a developer-oriented README will come later).

## Changes made

Updated:

- `docs/index.html` (CSS for `.flow`, `.tbl`, level dots, `.t-study` tag,
  `.studynote`; metier section restructured; architect dropdown enriched).

Added:

- `ai_logs/2026-06-01-landing-architect-schema-table.md`.

## What changed

- intro reworded: architecture is the first worked profession; others are "à
  l'étude" and require a practitioner before being offered;
- the Avocat / Médecin / Expert-comptable cards now carry a dashed "à l'étude"
  tag and "piste envisagée … à cadrer avec un praticien" copy, plus a study note;
- architect dropdown now contains:
  - a horizontal flow schema (Vous → Entre/Cadré → L'IA prépare → Porte/Statut →
    Vous/Décision) with a caption;
  - a four-column table (Usage / Ce que l'IA prépare / Niveau / Ce qui vous
    revient) for the six usages, with colored level dots;
  - the deontological red-lines note (unchanged).
- the previous `.steps` list was replaced by the table (clearer, comparable).

## Discipline

- tool-agnostic: capabilities and risks only, no product names in the page body;
- editorial: no forbidden affirmative phrase ("opposable" avoided, etc.);
- honest: other professions are explicitly study-stage, not implemented;
- responsive: flow stacks and table linearizes on small screens.

## Verification

HTML tags balanced (table/thead/tbody/tr, details, divs); no forbidden phrase.
`index.html` is not covered by the governance phrase scan.

## Explicit non-implementation

No runtime added. No files touched under `schemas/`, `tests/`, `hermes/`,
`operations/`, `pyproject.toml`, or `CLAUDE.md`.
