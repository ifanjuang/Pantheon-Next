# 2026-05-29 - Rites P1 anti-drift hardening

## Summary

Added P1 anti-drift doctrine for the Rites lane only.

This pass does not add new operational rites.

It strengthens misuse prevention, closure criteria and conflict handling.

## Files changed

- `docs/governance/rites/RITE_ANTI_PATTERNS.md`
- `docs/governance/rites/RITE_EXIT_CRITERIA_AND_CONFLICTS.md`
- `docs/governance/rites/README.md`

## Added

`RITE_ANTI_PATTERNS.md` records recurring rite misuse patterns:

- rite as workflow;
- rite as agent debate;
- rite as proof theater;
- rite as approval bypass;
- rite as memory shortcut;
- rite as context deletion;
- rite as style ritual;
- rite overuse;
- rite chaining;
- UI activity illusion;
- ZEUS as truth oracle.

`RITE_EXIT_CRITERIA_AND_CONFLICTS.md` defines:

- global exit requirements;
- ZEUS closure statuses;
- exit criteria for each existing rite;
- claim statuses for source concordance;
- assumption statuses for hidden premises;
- conflict policy between rites;
- User Decision Gate escalation conditions.

`docs/governance/rites/README.md` now indexes both documents and records the core anti-drift rule:

```text
A rite must end with status, retained output, preserved tensions and an explicit next allowed action.
```

## Boundary

This pass is documentation-only.

It does not implement:

- rite runtime;
- automatic rite trigger engine;
- hidden rite debate loop;
- scheduler;
- queue;
- OpenWebUI function, tool, pipe, filter, action or pipeline;
- Hermes skill installation;
- automatic approval;
- automatic memory promotion.

## Deferred raccords

`STATUS.md`, `CHANGELOG.md` and `OPENWEBUI_INTEGRATION.md` were not rewritten in this pass.

Reason: those files are long and are currently affected by parallel development lanes.

They should be reconciled in a separate low-conflict micro-pass when safe.

## Final rule

The more disciplined a rite looks, the more carefully its authority must be bounded.
