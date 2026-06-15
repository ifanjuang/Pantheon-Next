# AI Log — flow2a mobile regression observed

Date: 2026-06-15

## Trigger

After PR #136 was merged, the maintainer shared a mobile screenshot of the landing page showing text overlap in the `Entrées · Sorties · Mémoire` D3 diagram.

## Observation

The mobile rendering of `flow2a` is not acceptable:

- several card labels overlap;
- the issue is visible in `Corpus`, `Contexte`, `Workflow IA`, `Résultat candidat qualifié`, `Décision`, `Action externe` and `Mémoire`;
- the lateral arrows remain conceptually useful but the text layout makes the diagram hard to read.

## Likely cause

The mobile `card(...)` helper uses generic vertical offsets (`y+42`, `y+h-20`) that are too compressed for small cards.

## Action taken

Reopened issue #131 and updated its body with a regression section and acceptance criteria for a focused hotfix.

## Boundary

No code fix was applied in this intervention.

Repo state remains documented non-implemented for this visual asset.

No runtime, approval engine, memory engine, connector, scheduler, queue, external action, dependency or protected-path change.
