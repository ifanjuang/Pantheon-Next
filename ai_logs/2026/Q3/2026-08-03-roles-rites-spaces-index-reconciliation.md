# Roles, Rites and Spaces evolution — authority-index reconciliation

Date: 2026-08-03

Status: applied documentation reconciliation — non-runtime, non-promoting.

## Context

PR #507 adds `docs/governance/EVOLUTION_OF_ROLES_RITES_AND_SPACES.md` as candidate support doctrine. Governance CI correctly refused the unindexed candidate document.

The proposal was compared with the current owner surfaces, including:

- `GOVERNANCE_COLLEGE.md` and the architecture Role documents;
- `docs/governance/rites/RITE_INVOCATION_POLICY.md` and the Rite lifecycle documents;
- `docs/governance/CARD_STACK_MODEL.md` for Scene, Deck, Constellation and Space projection boundaries;
- `docs/governance/AUTHORITY_INDEX.md` for authority classes and promotion rules.

No new Role, Rite, Space, authority status or execution responsibility is introduced by this reconciliation.

## Change

Add one row to `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` classifying the new document as:

```text
candidate support doctrine
repo state: documented non-implemented
```

The row records placement and boundaries only. It does not promote the candidate to active support doctrine.

## Boundaries

```text
indexing != promotion
candidate doctrine != active doctrine
Role documentation != Role execution
Rite documentation != Rite authorization
Space documentation != backend ownership
UI projection != semantic authority
```

## Result

The candidate becomes visible to the authority coverage checker while its owner documents remain authoritative and its implementation status remains unchanged.
