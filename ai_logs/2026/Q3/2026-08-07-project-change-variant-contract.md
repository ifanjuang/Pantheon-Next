# Project change variant candidate contract

Date: 2026-08-07
Status: schema candidate for tranche G0; no executable persistence or selection added.

## Objective

Start tranche G with the smallest contract that the current repositories do not
already own: transport two or more competing Project attribute alternatives through
the canonical Execution Result spine while keeping comparison, human selection and
application separate.

## Existing owners reused

```text
Execution Result
-> immutable typed runtime candidates.

agency_change_candidates in pantheon-mvp
-> exact Project base revision, field-level diff, optimistic concurrency,
   append-only review history and human apply / reject / revision request.

knowledge_edit_variant
-> already proves bounded A/B alternatives for one exact Knowledge selection.
```

The repository therefore does not need a universal `InformationBranch`, a second
ChangeCandidate owner or a generic branch runtime.

## Contract decision

One `project_change_variant` payload represents one alternative. Sibling
alternatives share:

```text
request_ref
request_scope_digest
project_ref
base_revision
target_schema_id
```

They differ by `variant_label`, proposed descriptive attributes, rationale,
assumptions, compatibility findings, questions, basis references and limitations.

```text
one admitted execution
-> one or more project_change_variant candidates
-> later binding validation against the exact Project schema
-> existing ChangeCandidate persistence owner
-> comparison projection
-> human selection or refusal
-> separate governed application
```

## Field posture

The schema can carry JSON-shaped proposed attributes because the authoritative field
posture belongs to the target Agency schema and may evolve independently. The
receiving binding must fail closed unless every proposed field is mutable in the
exact observed target schema.

Consequential values remain ProjectClaims. System, immutable, claim-projection and
otherwise non-editable fields must be refused by the binding rather than admitted as
Project attribute alternatives.

## Authority boundary

The candidate cannot:

```text
create a persisted ChangeCandidate
select itself
apply a Project mutation
create a ProjectClaim
adopt Project truth
create a Decision
admit Evidence
authorize an effect
```

```text
variant produced != ChangeCandidate persisted
variant persisted != variant selected
variant selected != Project mutation applied
variant selected != Decision recorded
variant source reference != Evidence
```

## Verification

The tranche adds:

- Draft 2020-12 schema validation;
- one valid architecture alternative example;
- authority-escalation refusal for every authority flag;
- required exact request scope and non-empty proposed change;
- explicit absence of branch identity;
- two sibling alternatives inside one canonical Execution Result envelope.

## Next executable slice

The next pantheon-mvp tranche starts deliberately red and must prove:

1. the exact vendored schema is pinned to this merged contract;
2. sibling alternatives share one request scope and current Project revision;
3. every proposed field is mutable in the exact target Agency schema;
4. runtime output is projected into the existing ChangeCandidate owner;
5. selection is persisted separately from application;
6. a stale Project revision refuses selection or application without mutation;
7. disabling Hermes does not remove retained alternatives or applied Project state.

No migration, API, Cockpit action, runtime launch, Project mutation, Decision,
ProjectClaim, Evidence admission or memory promotion is added by G0.
