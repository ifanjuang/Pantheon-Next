# AI Log — Deck nested Swiper navigation correction

Date: 2026-06-28

Actor: ChatGPT

## Context

The user clarified that the deck should use Swiper for both horizontal and vertical navigation, rather than a custom gesture fallback.

## Source review

Reviewed active governance posture before the change:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

## Change made

Updated:

- `docs/assets/pantheon-control/app.js`
- `docs/assets/pantheon-control/deck.html`

## Behavior correction

The prototype now uses nested Swiper instances:

- vertical parent Swiper for hierarchy depth;
- horizontal child Swipers for sibling cards at each level.

Current behavior:

- horizontal swipe switches sibling cards in the current level;
- vertical swipe moves between hierarchy levels;
- card click toggles front/detail;
- button Descendre remains as a desktop/accessibility fallback.

## Note on Swiper manipulation methods

Swiper documentation exposes methods such as appendSlide, prependSlide, removeSlide and removeAllSlides.

For this prototype, the UI is still regenerated from the hierarchy configuration instead of incrementally appending or removing slides. This keeps the prototype simpler while the hierarchy is still unstable.

A later optimization can use Swiper manipulation methods if the deck becomes large enough to justify incremental updates.

## Boundary preserved

Documented non-implemented UI prototype only.

No backend, database, graph runtime, Hermes memory adapter, evidence engine, approval engine, memory engine, sender, connector or external action was implemented.

## Repo state

Documented non-implemented.

## To verify

- Mobile behavior on GitHub Pages.
- Interaction between vertical parent Swiper and horizontal child Swipers.
- Whether future large decks need append/remove methods instead of full state-driven rerendering.
