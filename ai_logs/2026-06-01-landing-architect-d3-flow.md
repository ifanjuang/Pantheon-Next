# AI Log — Landing page: architect flow as a D3.js diagram

Date: 2026-06-01

## Scope

Replaced the CSS flow strip in the architect dropdown with a real D3.js diagram,
styled to match the existing repo map.

## Changes made

Updated:

- `docs/index.html` (CSS `.archdiag`; replaced `.flow` markup with an
  `#archFlow` SVG; added a D3 v7 script that renders the flow).

Added:

- `ai_logs/2026-06-01-landing-architect-d3-flow.md`.

## What it renders

A horizontal five-step dossier flow, drawn with D3 into an inline responsive SVG
(viewBox 960x230):

```text
Vous (le dossier) -> Entre (cadré) -> L'IA prépare (brouillon)
-> Porte (statut) -> Vous (décision)
```

plus a dashed gold return curve "décision & mémoire vous reviennent" from the
gate back to the practitioner. Forward links use an animated dash flow
(disabled under prefers-reduced-motion). Node colors reuse the page palette:
exposure cool, execution warm, governance gold, the human in neutral.

D3 is loaded from the same CDN as the existing map
(`cdn.jsdelivr.net/npm/d3@7`). The script is guarded: it no-ops if the SVG or d3
is missing, so the page degrades gracefully offline.

## Verification

- HTML tags balanced (svg, script, defs, table, details, etc.);
- the script block parses and runs without error against a mocked d3 chain;
- no forbidden affirmative phrase.

(Full visual render requires a browser; logic verified headless.)

## Discipline

Tool-agnostic, sober, oriented to liberal professions. No product names. No
forbidden claims. The diagram is illustrative, not a runtime.

## Explicit non-implementation

No runtime added. No files touched under `schemas/`, `tests/`, `hermes/`,
`operations/`, `pyproject.toml`, or `CLAUDE.md`.
