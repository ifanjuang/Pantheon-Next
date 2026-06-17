# 2026-06-17 remove bottom action summary and align dependencies

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html`:

- removed the bottom `Actions` summary block from each card;
- kept the four action buttons as controls only;
- changed card grid rows accordingly so the top card content and dependency band are not affected by a bottom text block;
- aligned dependency / impact / coherence / warning / resolution pills horizontally using a grid-based pill row;
- normalized pill width and height to avoid uneven horizontal alignment;
- kept the full dependency detail view available on tapping the relation band.

No runtime, registry write, approval, memory promotion or external action was added.
