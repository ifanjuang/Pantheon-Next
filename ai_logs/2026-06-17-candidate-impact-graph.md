# 2026-06-17 candidate impact graph lifecycle

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/sols_3_fiches_draft.md` to clarify the candidate impact graph logic:

- The candidate card contains the list of affected cards and potential degradation levels.
- Target cards are not modified while the source card remains candidate.
- Impact links are regenerated on every analysis, modification, or detail request.
- `Recherche+` / detail requests can recompute DTU, manufacturer, support and structure checks without writing to target cards.
- If the candidate card is confirmed as-is, degradations are applied atomically to explicitly listed cards.
- Candidate links are then removed from the confirmed source card unless a permanent business dependency is explicitly approved.
- Candidate cards cannot degrade other candidate cards or create recursive activation loops.

No runtime, registry write, memory promotion, approval or external action was added.
