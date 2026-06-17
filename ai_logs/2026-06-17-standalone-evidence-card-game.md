# 2026-06-17 standalone evidence card game rewrite

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html` after mobile review showed the shared drawer still squeezing the prototype:

- removed dependency on the shared `nav.js` shell for this prototype page;
- made the evidence card game a standalone fullscreen mobile page;
- removed the left drawer at source rather than relying on cached CSS overrides;
- kept loading `evidence_cards_game_data.json` as the data fixture;
- kept horizontal project swipe, vertical card swipe, detail tap, relation tap and dezoom behavior;
- rendered the fast-read problem as an explicit layered text pair inside the card, not only via external CSS pseudo-elements;
- preserved the distinction between UI prototype and non-implemented governed runtime.

No runtime, registry write, approval, memory promotion or external action was added.
