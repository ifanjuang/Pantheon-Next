# 2026-06-18 editorial magazine evidence card direction

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/evidence_cards_game.html` to apply the first visual direction discussed with the user: revue critique / editorial magazine.

Changes:

- kept the page standalone fullscreen, without shared drawer shell;
- changed the recto signal from a single large phrase to a composed editorial signal:
  - `FOURNITURES`
  - `MOA`
  - `hors circuit`
- added separate signal lines with distinct scale, weight and offsets;
- added controlled typographic ghost layers behind the main signal;
- kept the full description as a smaller contextual note under the signal;
- compacted `RES-001` to `RES` in compact dependency pills while preserving the full id in dependency details;
- kept data loading from `evidence_cards_game_data.json`.

No runtime, registry write, approval, memory promotion or external action was added.
