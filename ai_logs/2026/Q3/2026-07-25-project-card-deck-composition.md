# 2026-07-25 — Architecture project card-deck composition contract

Status: validation-only intervention trace.

## Request

The maintainer observed that a project should not be modelled as a wide row of
fields. Working from the IFJA `_Affaires` Notion structure, they noted that many
rich fields (Zone PLU, GEORISQUE, surfaces, dates, contracts) are really
source-backed elements that arrive progressively, and that some are "voués à
disparaître" — they should leave the flat project record and become cards
(for example a GEORISQUE `dossier`/`evidence` card, a PLU-rule Knowledge card)
accumulated as the affair advances.

## Documents consulted

The composition rule was reconciled against, and specializes or constrains:

- `docs/governance/CARD_STACK_MODEL.md`;
- `docs/domain-packs/architecture/PROJECT_NAVIGATION_UX.md`;
- `docs/governance/AGENCY_DATA_SYSTEM_OF_RECORD.md`;
- `docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md`;
- `docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md`;
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`.

## Decision recorded

A new architecture-domain composition doctrine was added:

- `docs/domain-packs/architecture/PROJECT_CARD_DECK_COMPOSITION.md`.

It owns one rule for the architecture domain:

```text
agency_projects record = stable identity + revision + a few operational fields
everything rich          = a linked card with its own owner, provenance, status
the Project Card display = claims that CITE a backing card, status-qualified
the deck                 = grows au fur et à mesure, by phase, never one big form
```

It fixes the card families and their existing owners (Document, Evidence,
Knowledge/Référence, Décision, Surface/Fact, Jalon, Participation), maps the
IFJA `_Affaires` fields onto those cards, and defines "voués à disparaître" as
removed **from the project record**, not deleted: the field becomes a card with
provenance, status and a lifecycle a flat field never had.

## Non-equivalences recorded

```text
displayed != opposable
surface displayed != filing value approved
zone displayed != regulatory conclusion
document held != Evidence admitted
Knowledge != Evidence
Agency Decision != Pantheon governance Decision
field migrated out != field deleted
progressive accumulation != automatic ingestion (each card is governed)
```

## Classification

```text
authority class: candidate support doctrine
repository state: documented non-implemented
runtime state: unchanged
protected paths touched: none
schema or test change: none
installation or activation: none
```

An explicit row was added to
`docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md` (before the
`PROJECT_NAVIGATION_UX.md` row) with a negative-scope clause recording that the
document creates no CRM, ERP, cadastral or PLU service, no ingestion runtime,
no database and admits no Evidence.

## Non-effects

This intervention creates no:

- schema or migration;
- CRM, ERP, cadastral or PLU connector;
- ingestion, extraction or OCR runtime;
- project database or storage change;
- Cockpit component;
- Hermes Skill;
- approval, memory or Evidence-admission engine;
- external action.
