# Information card projection contract

Status: validation-only trace.

Date: 2026-08-05

## Observed state

- `Information` is already the accepted default visual family for project content.
- `Document` remains the backend authority for files and source-bearing documentary records.
- `pantheon-mvp` already owns `agency_information_cards` with ACTED immutability and source-version derivation.
- The missing seam is explicit optional Document backing, distinct business dates, media modes and contact projection.

## Decision

Extend the existing Information model instead of creating another project-content entity.

```text
native | single_document | multiple_documents
```

Document references remain references. They do not copy documentary authority into Information.

## Deferred

- Information-to-Information relations;
- variants/branches;
- APU object relations;
- automatic Hermes retention;
- ProjectClaim promotion.

## Non-equivalence

```text
Information displayed != Document authority transferred
business date != complete chronology
professional index != technical revision
contact projection != Participation authority
schema valid != professional truth
```
