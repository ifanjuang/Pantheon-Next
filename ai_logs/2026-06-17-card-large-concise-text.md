# 2026-06-17 large concise card text update

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html`:

- the card recto now renders shortened display text for description, suggestion and actions;
- primary card text size was increased for description, suggestion and actions;
- full detail remains available through the existing tap behavior and the JSON fixture still holds the longer source text;
- the change is presentation-only and does not mutate evidence data or create runtime behavior.

No runtime, registry write, approval, memory promotion or external action was added.
