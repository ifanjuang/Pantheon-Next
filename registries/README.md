# Registry Foundation

Status: candidate technical foundation — documented and validation-only.
Boundary profile: candidate_support_note.

This directory defines the cross-repository descriptor contract for machine-readable registry projections. It does not assume that registries are new: `pantheon-mvp` already contains active implementation registries for tags, navigation, status presentation and visual materials.

A registry is a technical contract for stable identifiers and bounded configuration. It is not a new business concept and does not replace its semantic owner.

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

## Existing implementation registries

The current MVP already carries distinct registry shapes, including:

```text
mvp_vertical/cockpit/registries/tag_registry.json
mvp_vertical/cockpit/registries/navigation_registry.json
mvp_vertical/cockpit/registries/status_registry.json
mvp_vertical/cockpit/registries/materials.json
```

This foundation does not migrate, rename or silently normalize them. Their reconciliation requires a specialized schema, explicit ownership and consumer-aware migration.

The first official reconciliation candidate is `tag_registry.json`, because it is already consumed by the server/Cockpit, demo fixtures and Hermes context. Its later specialized schema must preserve existing stable identities and must not turn tags into truth, Evidence, scope or authorization.

## Files

- `registry_index.json` — inventory of registry descriptors admitted in Pantheon-Next;
- `schemas/registry.schema.yaml` — common descriptor validation contract;
- `schemas/examples/registry.example.json` — fictional descriptor example;
- `.github/scripts/check_registry_foundation.py` — deterministic read-only checks.

## Admission rule

Do not create a registry merely because data can be serialized.

A registry is justified only when:

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

A specialized registry schema owns domain structure such as tag groups, navigation roots, material tokens or status-label presentation. The generic contract must not force all operational registries into one business shape.

## Index discipline

`registry_index.json` is the inventory of registry projections governed from this repository.

- listed path must exist;
- listed schema must exist;
- one path may be listed only once;
- one registry identity may be listed only once;
- every `*.registry.json` file stored under this repository's `registries/` directory must be indexed;
- an index entry does not promote, approve or activate the registry;
- external implementation registries are referenced through later reconciliation records, not copied into the index without an explicit adoption decision.

## Initial scope

The Pantheon-Next index intentionally contains no business registry in this foundation PR. This means no business instance is migrated here; it does not mean the ecosystem has no operational registries.

Next admissible work:

```text
1. define a specialized Tag Registry schema in Pantheon-Next;
2. validate the existing pantheon-mvp tag instance against a vendored reference;
3. add drift detection without moving runtime authority;
4. review navigation next;
5. audit status presentation axes before any canonicalization.
```

Roles, Rites and governed Spaces remain document-owned until structured consumption is demonstrated.

```text
empty Pantheon-Next index != no registries in the ecosystem
implementation registry != semantic owner
status label registry != canonical lifecycle
future registry != automatic source of truth
```
