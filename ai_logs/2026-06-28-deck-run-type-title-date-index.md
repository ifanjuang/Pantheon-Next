# AI Log — Deck run type title and metadata cleanup

Date: 2026-06-28

Actor: ChatGPT

## Context

The user requested that run type cards should not repeat `Run type —` in their visible titles. The user also requested date and ABCD-style index metadata.

## Change made

Updated:

- `docs/assets/pantheon-control/app.js`

## Behavior / data correction

Run cards now render fields:

- `date`
- `indice`
- `output`
- `next`

Draft cards now render fields:

- `date`
- `indice`
- `version`
- `output`
- `next`

Run type card titles were cleaned:

- `Finalisation CR`
- `Photo doute chantier`
- `Analyse facture`
- `Devis supplémentaire`

The run type nature is now carried by the hierarchy path (`home / Général / Corpus IFJ / Runs types / ...`) and by metadata/chips, not repeated in every title.

## Boundary preserved

Documented non-implemented UI prototype only.

No backend, database, graph runtime, Hermes memory adapter, evidence engine, approval engine, memory engine, sender, connector or external action was implemented.

## Repo state

Documented non-implemented.
