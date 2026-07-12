# AI intervention trace — reduced catalog model

Date: 2026-07-11
Status: validation-only trace

## Change

Added `docs/governance/CAPABILITY_RESOURCE_PRESET_MODEL.md` on the static install-catalog prototype branch.

The candidate reduces the operational model to:

```text
Capability
Resource
Preset
Binding
Provisioner
```

It tests the model against three cases:

```text
Docling
Langfuse
Google Drive
```

## Boundary

Documentation only.

No schema, live registry, catalog runtime, installer, provisioner, Docker or Portainer access, shell execution, OAuth connection, secret store, scheduler, queue, approval engine, memory engine or external action is added.

## Preserved distinctions

```text
capability != resource
preset != approval
binding != adoption
provisioner_available != execution_authorized
connected != authorized_for_scope
healthy != safe
trace != evidence
Markdown_derivative != original_source
```

## Result

The reduced model is expressive enough for one installable service, one observability surface and one external connection without requiring Blueprint, Solution or Capability Pack as first-class canonical objects.

Review remains required before promotion or implementation.