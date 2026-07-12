# AI intervention trace — declarative capability manifests

Date: 2026-07-11
Status: validation-only trace

## Change

Added a bounded non-executable candidate catalog under `catalog/` for three proving cases:

- Docling / document analysis;
- Langfuse / LLM observability;
- Google Drive / scoped read-only source access.

The slice contains candidate manifests for:

```text
Capability
Resource
Preset
```

Bindings and provisioner declarations remain nested inside presets.

## Boundary

No schema, validator, live registry, dashboard loader, installer, provisioner, connector, OAuth flow, secret store, runtime, scheduler, queue, approval engine, memory engine or activation path is implemented.

## Preserved distinctions

```text
manifest_present != resource_installed
preset_available != preset_approved
binding_declared != binding_activated
provisioner_named != execution_authorized
connected != authorized_for_scope
healthy != safe
trace != evidence
```

## Result

The reduced model is represented as data without adding new canonical layers or executable behavior. Review and validation remain required before any promotion or implementation.
