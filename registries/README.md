# Registry Foundation

Status: candidate technical foundation — documented and validation-only.
Boundary profile: candidate_support_note.

This directory contains machine-readable registry projections used by more than one reviewed consumer.

A registry is a technical contract for stable identifiers and bounded configuration. It is not a new business concept and does not replace its semantic owner.

```text
owner doctrine or server-owned model
-> registry projection
-> read-only validation
-> API or adapter consumption
-> Cockpit / Hermes projection
```

## Authority boundary

```text
owner document != registry
registry entry != complete doctrine
registry valid != entry approved
registry indexed != binding activated
registry consumed != task authorized
UI projection != semantic authority
```

The declared `authority_document` remains the semantic owner. The registry only carries fields required by reviewed consumers.

## Files

- `registry_index.json` — inventory of admitted registry files;
- `schemas/registry.schema.yaml` — common validation contract;
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

## Common contract

Every registry declares:

```text
schema_version
registry_id
registry_kind
version
status
owner
authority_document
entries
x_boundary
```

Every entry has a stable `id`. Domain-specific fields are defined by a later specialized schema or by a reviewed extension of the common contract.

## Index discipline

`registry_index.json` is the only inventory of registry files.

- listed path must exist;
- listed schema must exist;
- one path may be listed only once;
- one registry identity may be listed only once;
- every `*.registry.json` file must be indexed;
- an index entry does not promote, approve or activate the registry.

## Initial scope

This foundation intentionally contains no business registry.

The first pilot should be selected only after confirming real consumers, likely among Capability Slots, statuses, tags, subjects or Cockpit field definitions. Roles, Rites and governed Spaces remain document-owned until structured consumption is demonstrated.

```text
empty foundation != incomplete migration
no registry yet != missing authority
future registry != automatic source of truth
```
