# 2026-06-17 full-height card body with checkbox suggestions

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html`:

- the main card body now occupies the available height between card metadata and footer buttons;
- the body contains a very large bold description, dependency band/detail and suggested actions;
- suggested actions are rendered as checkbox items inside the main body, not as a bottom action text block;
- when dependency detail is opened, description and suggested actions are hidden so relation reading uses the full body height;
- dependency pills remain aligned horizontally;
- bottom action buttons remain as controls only.

No runtime, registry write, approval, memory promotion or external action was added.
