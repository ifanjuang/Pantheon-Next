# Card Projection Definition Model

Status: candidate support doctrine — implementation-bounded.
Boundary profile: projection_definition.

## Purpose

A Card Projection Definition describes how an already governed entity may be exposed by the Cockpit. It does not define the underlying business object, lifecycle, authority, truth, Evidence status, authorization or execution.

```text
owner object + owner schema
→ authoritative server projection
→ Card Projection Definition
→ card model
→ Cockpit renderer
```

This model complements `CARD_STACK_MODEL.md`.

```text
CARD_STACK_MODEL
= doctrine and projection grammar

Card Projection Definition
= machine-readable mapping for bounded configurable projections
```

## Scope

A definition may declare:

- stable projection identity and revision;
- applicable entity types;
- card role and presentation family;
- mappings for identity, title, summary, category, index and date;
- tag source fields and visible subject limit;
- bounded detail-field selection;
- references to server-projected actions and relations;
- static presentation text for projection-only entities such as navigation spaces.

A definition must not contain:

- SQL, endpoint URLs or transport rules;
- lifecycle transitions;
- approval, authorization or permission decisions;
- provider, runtime or binding selection;
- Evidence or truth qualification;
- hidden execution instructions;
- complete business-object schemas.

## Ownership

Pantheon-Next owns the definition contract and its boundaries.

`pantheon-mvp` may own operational definition instances consumed by the server and Cockpit. The server remains authoritative for entity data, status, available actions, relations and permissions.

```text
projection definition valid != object valid
field visible != field editable
action visible != action authorized
renderer compatible != semantically adopted
```

## Minimal contract

A definition contains:

```yaml
schema_id: cockpit.card_projection_definition
revision: 1
definition_id: navigation-space
entity_types: [cockpit_space]
card_role: container
presentation_family: project
identity:
  id_field: entity_id
  title_field: title
summary:
  static: Projects and related work.
detail:
  static_rows: []
actions:
  source: server_projection
relations:
  children_source: navigation_registry
```

Mappings may be field-based or static, but static values are limited to projection-only metadata. They must not override an owner-projected status, authorization, Evidence posture or consequential decision.

## First pilot

The first implementation pilot is limited to the root navigation cards:

```text
space:pantheon
space:affaires
space:connaissances
space:outils
```

The pilot may move titles, summaries, card roles, presentation families and static boundary notes out of `cockpit_projection.js`.

The following remain outside the pilot:

- Project, Information, Work, Decision and Evidence business rules;
- status calculation;
- available-action calculation;
- child collection assembly;
- API loading and authorization;
- renderer-specific layout algorithms.

## Evolution rule

A new configurable field is admitted only when:

1. at least two projections need the same mapping concept, or the navigation pilot proves a stable need;
2. the field has a clear owner and boundary;
3. moving it to configuration reduces hard-coded duplication without hiding business logic;
4. validation remains deterministic;
5. rollback does not require data migration.

## Core invariants

```text
card projection definition != underlying object schema
projection configuration != workflow
projection relation source != relation authority
static label != lifecycle state
visible action != authorized action
registry-selected definition != dependency adoption
Cockpit rendering != execution
```
