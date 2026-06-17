# 2026-06-17 confirmed impact links and conflict rules

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/sols_3_fiches_draft.md` to revise impact-link lifecycle and conflict propagation:

- Candidate impact links are not removed after confirmation.
- On confirmation, candidate links become confirmed impact links and stay available for audit and future reanalysis.
- Confirmed impact links do not trigger automatic propagation.
- If a confirmed card is rechecked and conflicts with other cards, the recently checked / recently validated card carries the conflict first.
- Related conflicting cards enter conflict mode only if the conflict card is explicitly validated by a human.
- This avoids recursive activation loops while preserving impact traceability.

No runtime, registry write, memory promotion, approval or external action was added.
