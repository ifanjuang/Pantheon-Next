# 2026-07-08 — Static pages runtime-language pass

## Status

Validation-only trace.

This log records a wording pass on static public/prototype pages. It does not create doctrine, runtime behavior, approval, memory promotion, provider routing, scheduling, installation, update execution or external action.

## Scope

Files changed:

```text
docs/assets/pantheon-control/pages/home.js
docs/assets/pantheon-control/index.html
docs/rag-probatoire.html
```

## What changed

- Pantheon Control home now opens with a visible status panel: static mockup, declared/fictive data, no real service control, no account connection and no action authorization.
- Pantheon Control summary cards now use declared-state language (`déclarés en ligne`, `déclarées actives`, `déclarés actifs`) instead of presenting mock states as direct runtime facts.
- Pantheon Control home title and lede now identify the page as a static mockup with no real control plane effect.
- `docs/rag-probatoire.html` now labels the Pantheon Control link as `Maquette cockpit` rather than `Cockpit`.

## Why

`WHAT_RUNS.md` states that `docs/index.html`, `docs/rag-probatoire.html` and `docs/assets/pantheon-control/` must not imply live product capability or runtime availability.

The inspected pages were mostly well bounded, but the visible wording still carried a small ambiguity:

```text
Cockpit
services en ligne
connexions actives
machines allumées
skills actifs
```

On a static prototype, those terms need visible qualification so the reader does not infer live control-plane status.

## Boundary kept

This intervention did not add or authorize:

```text
runtime
agent loop
scheduler
queue
provider router
MCP host gateway
plugin manager
installer
updater
automatic approval
automatic memory promotion
external sender
service control
account connection
external routing
```

The changed pages remain static documentation/prototype assets.

## Risks and limitations

- No CI or full link checker was run in this intervention.
- `docs/index.html` is a monolithic public landing page and was not edited in this pass; it already contains several non-runtime disclaimers, but still links to `assets/pantheon-control/index.html` with the shorter label `Cockpit`.
- A later refactor should extract shared labels/components so public landing pages can consistently use `Maquette cockpit` without hand-editing monolithic HTML.

## Result

The Pantheon Control entry point is less likely to be read as a live cockpit:

```text
maquette statique
statuts déclarés
aucun pilotage réel
aucune action autorisée
```
