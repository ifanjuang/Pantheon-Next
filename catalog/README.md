# Pantheon candidate catalog

Status: candidate declarative data — non-executable.

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

Historical installation-composition manifests and their schema have been removed. They remain available only through Git history and are listed in `docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md`.

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
