# 2026-06-17 floor selection regression logic

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/sols_3_fiches_draft.md` to add controlled validation regression semantics.

Key point: when a new material selection list introduces a support / finish incompatibility, previously validated cards such as material choice, structure/support and estimate are not deleted or silently overwritten. They move to a revision state: `Validé précédemment — remis en question par nouvelle source`.

No runtime, registry write, memory promotion, approval or external action was added.
