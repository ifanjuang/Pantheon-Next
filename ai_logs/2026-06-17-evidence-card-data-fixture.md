# 2026-06-17 evidence card data fixture split

Status: documented non-implemented.

Separated the mobile evidence card-game prototype data from the HTML view:

- created `docs/assets/pantheon-control/evidence_cards_game_data.json` as a static data fixture;
- moved project/card examples into the JSON fixture;
- updated `docs/assets/pantheon-control/evidence_cards_game.html` to load the fixture through `fetch()`;
- kept the HTML responsible for rendering, gestures and layout only;
- added a visible failure state if the JSON fixture cannot be loaded.

Rationale:

- examples can now be modified without editing the HTML rendering code;
- the JSON shape can later be replaced by a governed evidence datastore or evidence log export;
- this remains a static prototype and does not implement runtime storage, approval, memory promotion or external actions.
