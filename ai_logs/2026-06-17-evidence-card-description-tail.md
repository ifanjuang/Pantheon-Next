# Evidence card description tail tweak

Date: 2026-06-17

## Scope

Updated the mobile evidence card mockup in `docs/assets/pantheon-control/evidence_cards_game.html`.

## Change

- Kept the large truncated description signal as the primary one-second reading layer.
- Added a much smaller continuation line below the truncated signal using the existing `c.desc` value from `evidence_cards_game_data.json`.
- Added `descriptionTail(c)` to derive the continuation in the view layer without changing the JSON data model.
- Added `.heroTail` styling with a very small typographic scale and a mobile height clamp.

## Governance note

This is a display-layer adjustment only. It does not create doctrine, runtime behavior, approval logic, memory promotion, evidence validation or external action.

## State

Documented non-implementation / UI mockup adjustment.
