# Card Stack Hardening Note

Date: 2026-07-06

Status: documented non-implemented

Type: candidate support note

Related issue: #293

## Summary

Added a hardening note for `CARD_STACK_MODEL.md` to clarify the distinction between lieux, scenes, decks, cards and sub-cards; reduce card inflation; and make the boundaries between Context Cards, Evidence Cards, Guide/Ressource/Template Cards and Gate Cards explicit.

## Files changed

- `docs/governance/CARD_STACK_HARDENING_NOTE.md`
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`
- `ai_logs/2026-07-06-card-stack-hardening-note.md`

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

This change is documentation only.

It does not create:

- UI;
- renderer;
- schema;
- test;
- runtime;
- state machine;
- approval engine;
- memory engine;
- OpenWebUI plugin;
- Hermes skill;
- connector;
- external action.

## Decision

Do not rewrite `CARD_STACK_MODEL.md` wholesale.

Do not create a competing card model.

Record the hardening rules as a candidate support note first, then use them for a later focused patch if needed.

## Key rule

```text
The card is not a documentary sheet.
The card is a governed conduct unit.
It appears when something must be seen, decided, verified, blocked, linked or transmitted.
```
