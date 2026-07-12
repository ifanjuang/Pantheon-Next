# Pantheon candidate catalog

Status: candidate declarative data — non-executable.

This directory is a bounded proving ground for the reduced catalog model:

```text
Capability
Resource
Preset
```

Bindings and provisioner declarations remain nested inside presets for this first slice.

The files in this directory do not create a live registry, installer, provisioner, connector, OAuth flow, secret store, runtime, scheduler, queue, approval engine, memory engine or activation path.

They are data candidates for future dashboard rendering and validation only.

Current proving cases:

- Docling for document analysis;
- Langfuse for LLM observability;
- Google Drive for scoped read-only document access.

Required distinctions:

```text
manifest_present != resource_installed
preset_available != preset_approved
binding_declared != binding_activated
provisioner_named != execution_authorized
connected != authorized_for_scope
healthy != safe
```
