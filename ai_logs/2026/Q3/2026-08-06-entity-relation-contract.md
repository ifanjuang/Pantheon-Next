# EntityRef relation contract

Date: 2026-08-06

## Observed state

The relation authority inventory established that no existing carrier can express the four first Information relations. `agency_source_relations` is Source-only, `agency_information_document_links` carries document roles rather than Information semantics, the Cockpit graph is derived, and the APU relation vocabulary is spatial.

`EntityRef(entity_type, entity_id)` already exists in `pantheon-mvp` as the cross-domain identity primitive. `agency_project_claims` already demonstrates a polymorphic backing reference without a database foreign key, protected by pair-presence checks and domain validation.

## Decision

Define one generic relation shape keyed by two EntityRef values, with an initial admitted endpoint set limited to Information.

The first vocabulary is closed:

```text
responds_to
relies_on
supersedes
contradicts
```

The executable owner must compensate for the absence of polymorphic foreign keys by enforcing a closed entity-type set, endpoint existence, same-project scope, relation project equality, self-loop refusal and active-edge uniqueness.

## Boundaries

```text
generic shape != universal graph
human-created relation != runtime candidate
relation stored != fact validated
retired != deleted
```

No persistence, API, Cockpit behavior, Evidence admission, runtime or task authorization is added in Pantheon-Next.
