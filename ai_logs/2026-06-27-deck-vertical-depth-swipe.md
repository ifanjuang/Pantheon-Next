# AI Log — Deck vertical hierarchy swipe correction

Date: 2026-06-27

Actor: ChatGPT

## Context

The user clarified that moving up/down the hierarchy must happen through vertical swipe.

The previous prototype still used vertical Swiper behavior for operational card decks, which contradicted the agreed UX rule.

## Change made

Updated:

- `docs/assets/pantheon-control/app.js`

## Behavior correction

The deck now follows this rule:

```text
horizontal swipe = sibling cards at the current level
vertical swipe up = descend into the active card's first child
vertical swipe down = ascend to the parent level
card click = toggle front/detail
fallback button = Descendre / Détail for desktop and accessibility
```

The renderer now displays the siblings of the currently selected node instead of always displaying the selected node's children.

## Boundary preserved

Documented non-implemented UI prototype only.

No backend, database, D3 graph, constellation view, Hermes memory adapter, evidence engine, approval engine, memory engine, sender, connector or external action was implemented.

## Repo state

Documented non-implemented.

## To verify

- Mobile touch behavior on GitHub Pages.
- Whether swipe up should descend into the first child or open a child selector later.
- Whether swipe down from the root-level project should stay blocked or show a root overview card.
