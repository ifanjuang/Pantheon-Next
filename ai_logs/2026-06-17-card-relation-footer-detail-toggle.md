# 2026-06-17 card relation footer detail toggle

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html`:

- removed repeated relation labels from the footer; relation colors now carry the type information;
- tapping the card body toggles source / analysis / notes / journal only;
- relation details no longer open with the body details;
- tapping the relation band toggles full-width relation details;
- relation details show card number, title and reason;
- each related card is separated by a thin line;
- relation detail data now includes an explicit reason string when available.

No runtime, registry write, approval, memory promotion or external action was added.
