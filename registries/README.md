# Registry Foundation

Status: candidate technical foundation — documented and validation-only.
Boundary profile: candidate_support_note.

This directory defines the cross-repository descriptor contract for machine-readable registry projections. It does not assume that registries are new: `pantheon-mvp` already contains active implementation registries for tags, navigation, status presentation and visual materials.

A Registry is a technical mechanism for stable identifiers and bounded shared configuration. It is not a business object model, a lifecycle owner, a runtime router or a source of authorization.

```text
owner doctrine or server-owned model
-> registry descriptor and specialized schema
-> implementation instance
-> read-only validation and drift detection
-> API or adapter consumption
-> Cockpit / Hermes projection
```

## Authority boundary

```text
owner document != registry
registry descriptor != specialized registry schema
registry entry != complete doctrine
registry valid != entry approved
registry indexed != binding activated
registry consumed != task authorized
UI projection != semantic authority
```

The declared `authority_document` remains the semantic owner. Pantheon-Next owns canonical validation contracts and boundaries. `pantheon-mvp` may own operational instances consumed by the server and Cockpit. Hermes receives only bounded projections.

## Minimal taxonomy

The initial Registry taxonomy is deliberately narrow.

```text
Registry
├── vocabulary
├── projection_config
└── presentation
```

### `vocabulary`

Carries controlled identifiers and meanings shared by more than one reviewed consumer.

Typical examples:

```text
tags
subjects
other bounded shared vocabularies
```

A vocabulary may provide aliases, descriptions, deprecation metadata and bounded Hermes context. It does not establish truth, Evidence, scope or authorization.

### `projection_config`

Carries configuration for how governed objects are exposed or assembled without owning the underlying business model.

Typical examples:

```text
navigation
visible field configuration
view configuration
bounded card-composition parameters
```

```text
projection config != business schema
navigation order != workflow
visible field != authoritative field
```

### `presentation`

Carries visual metadata without semantic authority.

Typical examples:

```text
materials
icons
colors
gradients
patterns
```

```text
presentation token != status
icon != meaning
color != authorization
visual grouping != ontology
```

## Excluded from the operational taxonomy

The following are not reclassified as Registry families by default:

```text
Roles
Rites
Governed Spaces
Capabilities
Capability Slots
Bindings
Providers
InstallationCandidates
HealthObservations
Task Contracts
Evidence
Claims
ChangeCandidates
```

These retain their existing owner doctrines and schemas. A future Registry may expose stable references to them only when reviewed consumers require it; that projection does not become their model or authority.

```text
registry reference != concept ownership
binding listed != binding selected
provider listed != provider adopted
capability visible != task authorized
```

## Classification test

Before admitting a new Registry, ask in order:

1. Is this already an existing governed object, schema or record? If yes, extend or reference that owner instead.
2. Does it carry controlled shared meaning? Use `vocabulary`.
3. Does it configure bounded exposure or assembly? Use `projection_config`.
4. Does it carry visual metadata only? Use `presentation`.
5. If none applies, do not invent a new family without observed repeated need and explicit review.

```text
unclassified data != new Registry family
serializable != registry-worthy
shared file != canonical vocabulary
```

## Existing implementation registries

The current MVP already carries distinct registry shapes, including:

```text
mvp_vertical/cockpit/registries/tag_registry.json
mvp_vertical/cockpit/registries/navigation_registry.json
mvp_vertical/cockpit/registries/status_registry.json
mvp_vertical/cockpit/registries/materials.json
```

Their current intended classification is:

```text
tag_registry.json        -> vocabulary
navigation_registry.json -> projection_config
materials.json           -> presentation
status_registry.json     -> presentation candidate pending axis audit
```

`status_registry.json` is not a canonical lifecycle Registry. It currently projects labels and visual treatment across potentially distinct status axes and must be audited before any stronger classification.

This foundation does not migrate, rename or silently normalize these files. Their reconciliation requires a specialized schema, explicit ownership and consumer-aware migration.

The first official reconciliation candidate is `tag_registry.json`, because it is already consumed by the server/Cockpit, demo fixtures and Hermes context. Its specialized schema must preserve existing stable identities and must not turn tags into truth, Evidence, scope or authorization.

## Files

- `registry_index.json` — inventory of registry descriptors admitted in Pantheon-Next;
- `schemas/registry.schema.yaml` — common descriptor validation contract;
- `schemas/examples/registry.example.json` — fictional descriptor example;
- `.github/scripts/check_registry_foundation.py` — deterministic read-only checks.

## Admission rule

Do not create a Registry merely because data can be serialized.

A Registry is justified only when:

1. at least two real consumers require the same stable identifiers or configuration;
2. the semantic owner is explicit;
3. the structured fields are narrower than the complete doctrine;
4. versioning, deprecation and rollback are defined;
5. validation can remain deterministic;
6. no runtime, router, scheduler, queue, approval engine or memory promotion is introduced.

## Descriptor versus specialized schema

The common descriptor carries only cross-registry metadata:

```text
schema_version
registry_id
registry_kind
version
status
owner
authority_document
governance_refs
entries or descriptor references
x_boundary
```

A specialized Registry schema owns domain structure such as tag groups, navigation roots, material tokens or status-label presentation. The generic contract must not force all operational Registries into one business shape.

## Index discipline

`registry_index.json` is the inventory of Registry projections governed from this repository.

- listed path must exist;
- listed schema must exist;
- one path may be listed only once;
- one Registry identity may be listed only once;
- every `*.registry.json` file stored under this repository's `registries/` directory must be indexed;
- an index entry does not promote, approve or activate the Registry;
- external implementation Registries are referenced through later reconciliation records, not copied into the index without an explicit adoption decision.

## Initial scope

The Pantheon-Next index intentionally contains no business Registry in the foundation tranche. This means no business instance is migrated here; it does not mean the ecosystem has no operational Registries.

Next admissible work:

```text
1. define and merge the specialized Tag Registry schema;
2. validate the existing pantheon-mvp tag instance against a vendored reference;
3. add drift detection without moving runtime authority;
4. reconcile navigation as projection_config;
5. audit status presentation axes before any canonicalization.
```

Roles, Rites and governed Spaces remain document-owned until structured consumption is demonstrated.

```text
empty Pantheon-Next index != no registries in the ecosystem
implementation registry != semantic owner
status label registry != canonical lifecycle
future registry != automatic source of truth
```
