# Relation tranche: implementation order corrected, storage carrier decided

Date: 2026-08-06

Status: validation-only intervention trace — records two human decisions.

Change level: ordering correction and one design decision inside an existing
candidate roadmap. No schema, migration, API or Cockpit code is created here.

## Observed need

`INFORMATION_RELATION_AUTHORITY_INVENTORY.md` satisfied the §9 precondition and
left four decisions open. Two of them were taken; this records them and corrects
the plan they belong to.

## Order: relations before Tâches

`ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md` §19 placed `Tâches` and Decisions at
step 3 and the four minimal Information relations at step 4. The working order
used by the implementation repository placed relations first. Both orders were in
circulation, so the two agents working the roadmap were operating on different
preconditions.

The plan decided it against itself:

```text
§11  a Tâche may concern a Project, Information, Decision, Contact or Anatomy
     object, several of these at once
§21  do not create a second relation graph
```

A Tâche therefore needs a polymorphic many-to-many link. Building Tâches before a
relation carrier exists leaves only two outcomes — invent a link table dedicated
to Tâches, which is the graph §21 forbids, or stall waiting for one.

Relations now precede Tâches in §19, with the reasoning recorded there. No
completion criterion changed: §20 lists requirements, not a sequence.

## Storage field: one generic carrier keyed on EntityRef

Recorded in §9. The carrier is generic in shape and closed in meaning:

```text
relation_id
from_entity_type / from_entity_id     closed entity_type set
to_entity_type   / to_entity_id
relation_type                          closed: the four canonical meanings
```

Considered and rejected: a table dedicated to Information-to-Information edges on
the `agency_source_relations` model. It would have kept foreign-key integrity, but
§11 and §21 together mean Tâches, Anatomy and Compétences would each then build
their own carrier — the outcome §21 exists to prevent.

The convention is not new to the implementation: `agency_project_claims` already
stores a polymorphic reference as `backing_entity_type` + `backing_entity_id` with
a both-or-neither CHECK, over the `EntityRef` primitive that `card_scope`,
`hermes_scoped_context`, `card_tag_context` and `tag_registry` already consume.

Accepted cost: no foreign key to a single target table. Bounded by keeping
`entity_type` closed, so each extension is a visible reviewed change, and by a
project-scope trigger of the kind `agency_information_document_links` already
applies.

A Tâche that *concerns* an object is a scope link, not one of the four meanings.
Opening the carrier to it is a separate reviewed decision, not a consequence of
this one.

## Still open

Relation authority, vocabulary identifiers and review status. The inventory states
the options for each; none is decided here.

## Boundary

This trace records decisions. It creates no table, grants no relation authority,
canonizes no vocabulary and authorizes no implementation. The relations tranche
remains a candidate until reviewed.
