# 2026-06-17 floor selection pending impact lifecycle

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/sols_3_fiches_draft.md` to refine the floor selection scenario lifecycle:

- A new material list creates an impact candidate, not an immediate state regression.
- Previously validated cards remain validated until the new list is confirmed.
- If the new list is confirmed with the incompatible floor option, dependent structure and estimate cards can move to alert / revision states.
- If the list is modified and the incompatibility disappears, candidate alert relations are closed and are not retained by inertia.
- Materials are grouped by selection topic to avoid creating one card per material.

No runtime, registry write, memory promotion, approval or external action was added.
