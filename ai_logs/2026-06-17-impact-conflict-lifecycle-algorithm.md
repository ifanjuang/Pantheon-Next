# 2026-06-17 impact conflict lifecycle algorithm

Status: documented non-implemented.

Created `docs/assets/pantheon-control/impact_conflict_lifecycle.md` to formalize card impact and conflict logic:

- Candidate cards compute impact graphs without mutating target cards.
- Validating a candidate with possible conflict requires preflight warning and human confirmation.
- If validation creates a conflict with another confirmed card, both confirmed cards become conflict participants.
- The UI must list affected cards and proposed status changes before applying.
- Confirmed impact links remain available for audit and future reanalysis, but are passive by default.
- Conflict detection and conflict propagation are separated.
- Propagation requires explicit human validation.
- Anti-loop invariants are documented.

No runtime, registry write, memory promotion, approval or external action was added.
