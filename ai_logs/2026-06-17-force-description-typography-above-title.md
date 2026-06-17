# 2026-06-17 force description typography above title

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html`:

- changed the selector from `.heroText` to `.sec p.heroText` so it wins over the generic `.sec p` rule;
- set description text to `font-size: 44px`, approximately twice the card title maximum size;
- set description text to `font-weight: 900`;
- tightened line height and tracking for a stronger title-like problem statement;
- set the reduced-height media query to `40px` with the same higher-specificity selector.

No runtime, registry write, approval, memory promotion or external action was added.
