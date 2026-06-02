# AI log — landing architecture mobile D3 refocus

Date: 2026-06-02

## Scope

Updated `docs/index.html` after editorial review of the landing page.

## Changes

- Recentered the public landing page on architecture agencies rather than a broad professions-libérales list.
- Replaced the hero with the line: `L'IA à la mesure d'une pratique.`
- Added a clearer positive value proposition: structure projects and dossiers, clarify sources and decisions, reduce blind spots and avoidable errors.
- Removed the profession cards for lawyer / doctor / accountant from the public landing page.
- Kept D3 for the main dossier-flow diagram, but reworked its spatial model:
  - desktop: horizontal dossier flow with Pantheon as a visible frame around context, execution, output, decision and memory;
  - mobile: vertical stacked flow for phone screens.
- Reduced menu, button and block density for mobile readability.
- Replaced public wording around `gouverne` with more concrete terms: cadre, borne, qualifie, preuve, décision, mémoire.

## Doctrine impact

No doctrine change.

The canonical doctrine remains:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

This update is editorial and visual only.

## Repo state

Documented, non-implemented.

## Risk

Low. Modified only `docs/index.html` and this AI log.

## Follow-up

Review rendered GitHub Pages output on desktop and phone. Check D3 label spacing and mobile diagram height after deployment.
