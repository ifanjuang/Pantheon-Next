# Architecture Project Object Model

Status: candidate doctrine — project object model for Architecture Project Understanding (v0.1).

This document defines the **project object model**: the métier vocabulary that
describes the project world — spatial hierarchy, transversal zones, typed object
relations, internal nomenclature, semi-structured properties, phase states and
non-normative analysis contexts.

It is documentation only. It adds no runtime, OCR, vision, solver or extraction.
It is a sibling of the belief contract (Architecture Project Understanding, PR
#163) and of the external references register (PR #164); it does not modify them.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Doctrine: describe the world, reference the registers

The review of the belief contract drew one line clearly, and this model honors it:

```text
The project base describes the world of the project:
objects, hierarchies, zones, relations, properties, phases, names.

The Pantheon registers say why we believe it, what is doubtful,
what changed and what is decided: evidence, doubt, contradiction,
decision, approval, canonization.
```

So the project object model **references** the governance registers through
`*_ref` fields (`evidence_ref`, `doubt_ref`, `decision_ref`, `change_ref`,
`source_ref`). It does not embed their lifecycle. Evidence, doubt, contradiction,
human override and canonization remain Pantheon contracts (belief contract +
proof register), not central objects of the project base.

## Identity is not the name

An object's name or source number is information, not identity. Internal project
identity is owned here (`object_identity`), independent of any IFC GlobalId, Revit
ElementId, room number or source label — which are sources/evidence. If a door is
renamed between two indices, the internal identity survives; the old names move to
`aliases` / `name_history`.

## Objects

Each object below has a self-contained validation schema under
`schemas/architecture-project-understanding/`.

### 1. `spatial_node` — containment hierarchy

The physical tree: `project → site / parcel → building → level → zone → space →
room → subspace`. A node has a `node_kind`, an optional `parent_id`, and may span
levels. **Zones are not only rigid physical containers**: a `zone` carries a
`zone_type` (`functional | programmatic | technical | spatial | phasing | facade |
work_zone`) and may contain several rooms, cross several levels, or group
non-contiguous objects. The model is a physical tree **plus** transversal groups,
never a tree alone.

### 2. `object_identity` — internal nomenclature

`stable_id`, optional `internal_code`, `current_display_name`, `human_ref`,
`source_refs` (per-source values), `aliases`, `name_history`. The durable identity
layer for any object.

### 3. `object_relation` — typed dependencies

An object does not only *belong* to a container; it has several typed relations,
each optionally qualified (e.g. a wall face). Relation types: `contains`,
`part_of`, `located_in`, `mounted_on`, `hosted_by`, `faces`, `serves`,
`depends_on`, `adjacent_to`, `connected_to`, `separated_by`, `opens_to`, `crosses`,
`penetrates`, `aligns_with`, `above`, `below`, `near`, `opposite`, `left_of`,
`right_of`, `belongs_to_zone`, `belongs_to_system`, `belongs_to_group`,
`has_phase_state`.

### 4. `object_group` — transversal grouping for inheritance

A group of objects (possibly non-contiguous, possibly mixed kinds) that share
properties. Distinct from the belief contract's `space_group` (a composite spatial
identity such as a T2): `object_group` exists to attach a shared `property_set` and
inherit it, with per-instance exceptions.

### 5. `property_set` + `property_claim` — semi-structured properties

A minimal rigid core plus optional, qualified property sets. A `property_set`
applies to an object or a group, has a `property_set_type`, and holds
`property_claim`s (`property_key`, `value`, `value_type`, `status`). Inheritance is
by type or group; exceptions are per occurrence (see `instance_override`).
Properties are never frozen into rigid columns for every door/wall/window.

The `value_type` and `status` vocabularies are shared, source-agnostic
definitions (in the family `shared.schema.yaml`), so `property_set` and
`instance_override` carry the same enums rather than two private copies:

- `value_type`: `controlled_label | number | boolean | text | range | reference`.
- `property_status` (the `status` of a property claim or override):
  `candidate | specified_candidate | observed | to_verify | reviewed | rejected`.


### 6. `instance_override` — per-occurrence exception

Overrides one property of an inherited `property_set` for one object, with a
reason and a status (e.g. doors 21/23/24 are EI30, but 24 is EI60 because it serves
the main technical room).

### 7. `object_note` — descriptions and remarks

Any object may receive notes: `description`, `comment`, `internal_note`,
`site_observation`, `design_intent`, `visa_note`, `coordination_note`. A note is
attached, typed and may reference Pantheon registers — but a remark never becomes a
property or a truth automatically.

### 8. `phase_state` — existing / demolition / construction

The base knows project states, because they describe the project itself, not only
a decision: `existing | to_demolish | demolished | to_create | new | modified |
moved | temporary | as_built | unknown`. Essential for extension, renovation,
school, clinic, site phasing, existing/proposed/demolition.

### 9. `analysis_context_candidate` — possible analysis, never a conclusion

The model does **not** know norms. It describes the project in a vocabulary
compatible with later analysis. It does not say "this is compliant" or "this door
must be fire-rated". It attaches non-normative context tags so Hermes / Pantheon /
domain packs can activate the right analysis later: e.g.
`bathroom_electrical_safety`, `accessible_route`, `fire_separation_review`,
`wet_room_detail`, `facade_water_management`, `acoustic_partition_context`,
`structural_opening_context`, `maintenance_access`, `site_coordination`,
`urban_planning_volume`.

## Governance invariants

1. The project base describes the world; it references — never embeds — evidence,
   doubt, decision, approval and canonization.
2. Identity (`object_identity`) is independent of names, numbers and source ids.
3. Relations are typed and may be qualified; containment is not the only relation.
4. Properties stay semi-structured: core + property sets + per-instance overrides.
5. The model carries `analysis_context_candidate`, never a normative conclusion;
   norms are activated downstream by domain packs.
6. Phase state is descriptive project data, distinct from any decision.

## Governance references

- docs/governance/ARCHITECTURE_PROJECT_OBJECT_MODEL.md
- docs/governance/CAPABILITY_PLACEMENT.md
- docs/governance/EVIDENCE_PACK.md
- docs/governance/GLOSSARY.md
- schemas/shared_axes.schema.yaml
