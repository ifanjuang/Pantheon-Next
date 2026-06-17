# 2026-06-17 card log and link rules

Status: documented non-implemented.

Created `docs/assets/pantheon-control/card_log_and_link_rules.md` to document:

- append-only log per card;
- manual confirmed-to-candidate override behavior;
- conflict suspension instead of deletion when a confirmed card is reopened as candidate;
- many impact links and many conflict links per card;
- link uniqueness by source, target, reason and hypothesis version;
- UX separation between outgoing impacts, received impacts, active conflicts, suspended conflicts and history.

No runtime, registry write, memory promotion, approval or external action was added.
