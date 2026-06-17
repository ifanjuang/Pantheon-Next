# 2026-06-17 card revision proposal lifecycle

Status: documented non-implemented.

Created `docs/assets/pantheon-control/card_revision_proposal_lifecycle.md` to formalize pending card modification and research behavior:

- modification, research and complementary analysis requests do not mutate the current card;
- each request creates a revision proposal attached to the card;
- proposals can be accepted, modified, developed further, deleted, rejected, superseded or archived;
- accepting a proposal creates a new card version and archives the previous state;
- deleting a proposal removes it from active review but keeps a minimal trace;
- proposal relations remain candidate until the proposal is accepted;
- one active proposal per card per proposal type is recommended;
- anti-loop rules ensure that suggestions, searches and logs do not trigger automatic propagation.

No runtime, registry write, approval, memory promotion or external action was added.
