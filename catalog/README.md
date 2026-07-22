# Pantheon candidate catalog

Status: candidate declarative data — non-executable; legacy composition files obsolete.

This directory is a bounded proving ground for independent capability and resource records used by the common installation baseline.

```text
Capability
Resource
Binding status
Module status
```

The common required component set is defined only by:

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
```

The historical files under `catalog/presets/` and `catalog/schemas/preset.schema.json` are superseded installation-composition experiments. They are retained temporarily as historical artifacts and must not be loaded, displayed or used to determine an installation.

The remaining catalog files do not create a live registry, installer, provisioner, connector, OAuth flow, secret store, runtime, scheduler, queue, approval engine, memory engine or activation path.

Required distinctions:

```text
manifest_present != resource_installed
resource_required != binding_active
binding_declared != binding_activated
provisioner_named != execution_authorized
connected != authorized_for_scope
healthy != safe
```
