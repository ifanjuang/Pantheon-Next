# Pantheon candidate catalog

Status: candidate declarative data — non-executable.

This directory is a bounded proving ground for independent capability, resource and binding records used by the common installation baseline.

```text
Capability
Resource
Capability Binding
Module status
```

A `CapabilityBinding` is a relation only:

```text
Capability Slot
-> Capability Passport reference
-> exact immutable implementation anchor
```

It does not copy the Capability Passport or implementation provenance body, and it does not install, adopt, activate or authorize anything. `unbound` is an explicit valid state when a slot remains profile- or project-specific.

The common required component set is defined only by:

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
```

Historical installation-composition manifests and their schema have been removed. They remain available only through Git history and are listed in `docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md`. The new bounded binding relation does not restore those Presets or installation-composition manifests.

The remaining catalog files do not create a live registry, installer, provisioner, connector, OAuth flow, secret store, runtime, scheduler, queue, approval engine, memory engine or activation path.

Required distinctions:

```text
manifest_present != resource_installed
candidate_resource != selected_binding
binding_selected != dependency_adopted
binding_selected != installed
binding_selected != activated
binding_selected != task_authorized
unbound != missing_governance
connected != authorized_for_scope
healthy != safe
```
