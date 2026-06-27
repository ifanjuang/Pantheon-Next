# AI Log — Pantheon Control hierarchy deck prototype

Date: 2026-06-27

Actor: ChatGPT

## Context

The user requested a reduced cockpit implementation direction:

- one CSS file for the whole cockpit;
- one JS file for the deck logic;
- use Swiper.js;
- avoid hard-coding each card type;
- make the system empty / configurable by hierarchy so the structure can later change through JSON.

## Change made

Created:

- `docs/assets/pantheon-control/deck.html`
- `docs/assets/pantheon-control/app.js`

Updated:

- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/style.css`

## Design choice

`app.js` is hierarchy-driven.

It reads:

```text
PC_DECK_CONFIG.levels
PC_DECK_CONFIG.root
```

The renderer does not hard-code `Project -> Scene -> Subject -> Deck -> Card` as executable logic.

The default configuration currently demonstrates that hierarchy, but later the hierarchy can be changed by changing the JSON-like configuration.

## Card generation

Card rendering is data-driven through:

```text
PC_CARD_TYPES
```

Each type defines:

- label;
- CSS class;
- background impact word;
- fields to show.

Adding a type should mostly mean adding one configuration entry and data nodes, not writing a new renderer.

## Navigation

The prototype uses:

- breadcrumb navigation;
- sibling rail navigation;
- vertical Swiper for child cards;
- click-to-open children;
- leaf cards remain detail-only and do not execute anything.

## Boundary preserved

Documented non-implemented mockup.

No backend, database, D3 graph, constellation view, Hermes memory adapter, evidence engine, approval engine, memory engine, sender, connector or external action was implemented.

Swiper is used as a front-end display/navigation dependency loaded from CDN on the prototype page.

No schema, test, platform, operation, Docker, `.env`, `pyproject.toml` or runtime file was changed.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- one shared `style.css`;
- one `app.js` for deck logic;
- hierarchy-driven JSON-like configuration;
- card type table instead of hard-coded card functions;
- no D3 / no constellation for this pass;
- Swiper for vertical card navigation.

Refused:

- many CSS / JS files;
- hard-coded per-card rendering;
- runtime implementation;
- automatic approval or action.

To verify:

- visual behavior on GitHub Pages after cache refresh;
- whether Swiper CDN should later be vendored locally for NAS/offline use;
- whether root should open on all projects or directly on the General project.

To arbitrate:

- whether the hierarchy config should remain inside `app.js` for now or move to a separate JSON file once the prototype stabilizes.
