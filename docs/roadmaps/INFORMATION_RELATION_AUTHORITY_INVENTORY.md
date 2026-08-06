# Information relation authority inventory

Status: validation-only inventory — documented, not implemented.
Boundary profile: candidate_support_note.
Date: 2026-08-05

## Why this document exists

`ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md` §9 makes one precondition explicit before
the four minimal Information relations may be implemented:

```text
The exact storage field, relation authority, vocabulary identifiers and review
status must be decided after inventory of the existing generic graph, domain
relations and APU mapping contracts.
```

This document is that inventory and nothing more. It observes what already carries a
relation across both repositories, names the shapes those carriers use, and states the
decisions the implementing tranche still has to make.

It decides no storage field, grants no relation authority, canonizes no vocabulary and
promotes nothing. A carrier described here as existing is not thereby approved as the
target of the tranche.

## 1. The generic graph

### 1.1 `EntityRef` — the identity primitive

`pantheon-mvp:mvp_vertical/entity_ref.py` defines the only cross-domain identity
primitive: a frozen pair.

```text
EntityRef = (entity_type, entity_id)
```

Its docstring states the boundary precisely: it "does not validate that the referenced
owner exists, resolve scope, grant access, establish truth or authorize an effect."
`unique_entity_refs()` normalizes and deduplicates while preserving first-seen order.

Consumers today: `card_scope.py`, `hermes_scoped_context.py`.

`EntityRef` is the natural key shape for a heterogeneous relation, and it is the only
existing primitive that can address two objects of different families. It carries no
relation semantics of its own.

### 1.2 The Cockpit map — a derived, in-memory graph

`pantheon-mvp:mvp_vertical/cockpit/map/map_graph_model.js` builds a read-only projection
of the card graph into `{ nodes, links }`. Its links are **derived, never stored**, and
use exactly two kinds:

```text
containment   parent -> child, from the child-collection projection
lineage       previous -> next, from a shared series_id or an explicit base_acted_id
```

`map_corroboration.js` adds a third, currently inert overlay: it returns `[]` until cards
carry support references, and its own comment states that "corroboration never implies
promotion: a certainty ring is a candidate signal, not Evidence."

Observation: the Cockpit already renders a graph, but that graph is a projection of
containment and versioning. It is not a relation store and holds no authored edge.

## 2. Domain relations

Three distinct relation carriers exist in `pantheon-mvp`, with three different shapes.
Two of them were introduced by tranches A and B.

### 2.1 `agency_source_relations` — tranche A

`sql/010_source_intake_admission.sql`.

```text
relation_id      TEXT PRIMARY KEY
source_id        -> agency_sources
target_source_id -> agency_sources
relation_type    TEXT CHECK (relation_type = 'contains')
UNIQUE (source_id, target_source_id, relation_type)
CHECK (source_id <> target_source_id)
```

Homogeneous (Source to Source), typed, closed vocabulary of exactly one value, self-loop
refused, event-sourced through `agency_source_events` with the `source_relation_created`
event type.

This is the closest existing prototype of an authored, typed, stored relation.

### 2.2 `agency_information_document_links` — tranche B

`sql/012_information_card_projection.sql`.

```text
PRIMARY KEY (information_id, document_id)
role             TEXT CHECK (role IN ('primary', 'supporting', 'attachment'))
observed_version INTEGER
observed_digest  TEXT
```

Heterogeneous (Information to Document), **untyped in the relation sense**: `role`
qualifies the document's part in the Information, not a meaning between two
Informations. Project scope is enforced by a `BEFORE INSERT OR UPDATE` trigger that
refuses a cross-project link.

`docs/information_projection.md` records that this slice "deliberately excludes
Information-to-Information relations".

### 2.3 What is *not* a relation

Two tables read like relations and are not. Recording this prevents a later tranche from
mistaking them for prior art.

- `contradictory_review_candidates` (`sql/003_…`) stores a review **report** about one
  candidate — `review_status`, `report_digest`, four `CHECK` constraints refusing
  Evidence, approval, ZEUS closure and task authorization. It is not an edge between two
  Informations. The canonical relation `contredit` therefore has **no** existing carrier.
- `knowledge_edit_variants` (`sql/014_…`) stores A/B replacement candidates on one
  Knowledge item. It belongs to the variants tranche, not to relations.

## 3. APU mapping contracts

### 3.1 `object_relation.schema.yaml` — an existing typed relation contract

`Pantheon-Next:schemas/architecture-project-understanding/object_relation.schema.yaml`
already defines a typed binary relation with an optional qualifier:

```text
required: [relation_id, type, from, to]
optional: qualifier (object), source_refs, notes, governance_refs
```

Its `$defs/relation_type` closes on **25** values: `contains`, `part_of`, `located_in`,
`mounted_on`, `hosted_by`, `faces`, `serves`, `depends_on`, `adjacent_to`,
`connected_to`, `separated_by`, `opens_to`, `crosses`, `penetrates`, `aligns_with`,
`above`, `below`, `near`, `opposite`, `left_of`, `right_of`, `belongs_to_zone`,
`belongs_to_system`, `belongs_to_group`, `has_phase_state`.

That vocabulary is **spatial and physical**: it describes how building objects relate.
Exactly one value, `contains`, overlaps the Information vocabulary discussed in §9 of the
plan. The other 24 have no Information meaning.

Consequence for the tranche: `object_relation` is a usable *shape* precedent
(`relation_id` / `type` / `from` / `to` / `qualifier` / `source_refs`), but its
*vocabulary* is a different domain and must not be reused as the Information vocabulary.

### 3.2 The write-authorization chain

Four contracts landed on 2026-08-05 and complete the APU mapping lane:

```text
adapter_result.schema.yaml            mappings[].status: unmatched |
                                      candidate_matches | needs_clarification
mapping_review.schema.yaml            action: select_existing_object | mark_unmatched |
                                      needs_clarification | reject_mapping
write_command_candidate.schema.yaml   command_id, operation, five source refs,
                                      target_stable_object_ref, payload_digest
write_authorization_event.schema.yaml action: authorize_application |
                                      reject_application
```

Implemented in `pantheon-mvp` as `apu_mapping_reviews.py` (`sql/011_…`) and
`apu_write_preparation.py` (`sql/012_…`).

This chain is the repository's demonstrated pattern for **how a proposed structural
change becomes an authorized one**: adapter result → review event → command candidate →
authorization event, each step append-only and digest-bound, with the human authorization
separated from the proposal. A relation asserted by a runtime, rather than authored by a
human in the Cockpit, would need to travel this lane rather than be written directly.

Note that `adapter_result` and `write_command_candidate` reference
`shared.schema.yaml#/$defs/certainty` and `#/$defs/object_kind`, while `mapping_review`
and `write_authorization_event` define their enums locally.

## 4. Consolidated observation

```text
carriers of a relation today      : 3 stored + 1 derived
distinct shapes                   : 4
shared relation vocabulary        : none
shared relation storage           : none
generic heterogeneous edge        : none
```

| Carrier | Endpoints | Typed | Stored | Scope rule | Event-sourced |
|---|---|---|---|---|---|
| `agency_source_relations` | Source → Source | yes, 1 value | yes | none | yes |
| `agency_information_document_links` | Information → Document | no (`role` only) | yes | same-project trigger | yes |
| `map_graph_model.js` links | card → card | 2 kinds | no, derived | none | n/a |
| `object_relation` (APU) | object → object | yes, 25 values | contract only | none | n/a |

Two facts follow directly and are the substance of this inventory.

**First: the four canonical relations have no carrier.** §9 names `répond à`,
`s'appuie sur`, `remplace`, `contredit` as the first implementation. None exists in any
shape. The one relation that *is* implemented, `contains` in
`agency_source_relations`, belongs to §9's "additional candidates may be tested later"
list, not to the four. The plan states those candidates "are not canonical until real
project use and authority inventory demonstrate that they represent distinct
responsibilities."

**Second: no existing carrier can express an Information-to-Information edge.**
`agency_source_relations` is homogeneous on Sources. `agency_information_document_links`
crosses Information and Document but carries no meaning. The Cockpit graph is derived.
`object_relation` is a spatial vocabulary. The tranche is therefore building a new
carrier, not extending one — and the inventory's value is that this is now an observed
fact rather than an assumption.

## 5. Decisions the tranche still owes

§9 names four. Each is restated with the options the inventory makes visible. This
document selects none of them.

**Storage field — decided 2026-08-06, recorded in the plan's §9.** Options
observed here: a dedicated typed table on the `agency_source_relations` model
(homogeneous, closed `CHECK`); a generic `EntityRef`-keyed edge table
(`from_entity_type`/`from_entity_id` → `to_entity_type`/`to_entity_id`); or an
extension of `agency_information_document_links` (rejected on its face — that
table's `role` is a document part, not a meaning). The plan's §21 non-goals forbid
"a second relation graph", which constrained the choice; §11's polymorphic Tâche
links resolved it. The generic carrier was selected, with the vocabulary kept
closed to the four meanings. This document records that a decision was taken; the
decision itself lives in the plan.

**Relation authority.** The APU lane (§3.2) shows the repository's answer for
runtime-proposed structural change. The open question is whether a Cockpit-authored
relation between two Informations is a direct human write — like
`agency_source_relations`, whose events record `actor_kind IN ('human','hermes','system')`
— or must travel a candidate/authorization pair. §9 states that "explicit relation !=
inferred candidate relation", which implies the two paths differ.

**Vocabulary identifiers.** The four French labels in §9 have no identifier form. The
repository's two existing conventions diverge: `agency_source_relations.relation_type`
uses bare lowercase (`contains`), `object_relation` uses the same style with 25 values.
Whether the Information vocabulary lives in its own `$defs`, in `shared_defs.schema.yaml`
or inline is undecided; note that `shared_defs.schema.yaml` currently declares itself
consumed by no schema.

**Review status.** `agency_source_relations` has none — a relation is created and that is
final. `agency_information_document_links` has none either. Every other candidate-bearing
table in the repository carries a review or disposition state. Whether a relation is
reviewable, and against which vocabulary, is open.

## 6. Scope-order observation — resolved 2026-08-06

This document originally recorded that the plan's §19 placed the four minimal
relations *after* `Tâches` and Decisions, while the working order placed them before,
and left the divergence for the human to resolve.

It was resolved in favour of relations first, and §19 now reads that way. The
deciding evidence was internal to the plan: §11 states a Tâche may concern a Project,
Information, Decision, Contact or Anatomy object — several at once — which is a
polymorphic many-to-many link, and §21 forbids a second relation graph. Building
Tâches first therefore forced the violation. The reasoning is recorded in §19.

## 7. Boundary

This document does not:

- create, rename or migrate any table, column or schema;
- grant relation authority to any actor, human or runtime;
- canonize, reject or rank any relation vocabulary;
- promote `contains` from candidate to canonical, or demote it;
- authorize the implementation of the relations tranche;
- convert an observed carrier into an approved target;
- admit Evidence, promote memory or close any gate.

```text
inventory != decision
existing carrier != approved carrier
observed shape != canonical shape
```

## 8. Governing references

- `docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md` §9, §19, §21
- `schemas/architecture-project-understanding/object_relation.schema.yaml`
- `schemas/architecture-project-understanding/adapter_result.schema.yaml`
- `schemas/architecture-project-understanding/mapping_review.schema.yaml`
- `schemas/architecture-project-understanding/write_command_candidate.schema.yaml`
- `schemas/architecture-project-understanding/write_authorization_event.schema.yaml`
- `docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md`
