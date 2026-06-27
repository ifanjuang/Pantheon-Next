# AI Log — Deck card detail toggle

Date: 2026-06-27

Actor: ChatGPT

## Context

The user reported that clicking a card did not hide the front information to show details.

The previous prototype conflated two gestures:

- card click;
- opening a child node in the hierarchy.

## Change made

Updated:

- `docs/assets/pantheon-control/app.js`

## Behavior correction

The renderer now creates two faces for each card:

- `pc-card__front` — fast reading face;
- `pc-card__detail` — detail face.

The interaction is now separated:

- clicking the card toggles detail/front;
- clicking `Ouvrir` descends into the configured child hierarchy;
- clicking `Détail` on a leaf card toggles the detail face;
- clicking `Retour carte` returns to the fast reading face.

## Boundary preserved

Documented non-implemented UI prototype only.

No backend, database, D3 graph, constellation view, Hermes memory adapter, evidence engine, approval engine, memory engine, sender, connector or external action was implemented.

## Repo state

Documented non-implemented.

## To verify

- GitHub Pages cache refresh;
- mobile tap behavior with Swiper;
- whether detail toggle should also be triggered by long press instead of single tap later.
