# AI Log — Deck axis hierarchy fix

Date: 2026-06-27

Actor: ChatGPT

## Context

The user observed that, inside the hierarchy deck prototype, `Documents` and `Runs types` appeared one page after another through vertical navigation.

This exposed a flaw in the prototype renderer: every child deck was treated as vertical, regardless of hierarchy level.

## Change made

Updated:

- `docs/assets/pantheon-control/app.js`
- `docs/assets/pantheon-control/deck.html`

## Design correction

`PC_DECK_CONFIG.levels` now carries an `axis` property:

```text
project -> horizontal
scene -> horizontal
subject -> horizontal
card -> vertical
```

The renderer now reads the next child level axis and passes it to Swiper through `data-axis`.

This means:

- project siblings are horizontal;
- scene siblings such as `Documents` and `Runs types` are horizontal;
- subject siblings are horizontal;
- operational cards remain vertical.

## Boundary preserved

Documented non-implemented UI prototype only.

No D3, constellation, backend, database, Hermes adapter, evidence engine, approval engine, memory engine, sender, connector or external action was implemented.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- hierarchy level controls axis;
- `Documents` and `Runs types` should not be vertical siblings;
- Swiper direction must be driven by config, not hard-coded.

To verify:

- GitHub Pages cache refresh;
- mobile behavior of horizontal scene cards;
- whether card-level vertical should begin at level `card` or be configurable per branch later.
