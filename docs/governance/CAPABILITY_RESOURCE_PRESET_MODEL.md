# Capability, Resource and Preset Model

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

## Purpose

This document reduces the dashboard and installation model to five operational objects:

```text
Capability
Resource
Preset
Binding
Provisioner
```

Pantheon governs status, scope, policy, gates, evidence expectations, history and rollback visibility.
Hermes or another external runtime executes authorized work.
OpenWebUI exposes the user-facing surface.
A provisioner performs installation outside Pantheon.
The human approves consequential installation, activation, exposure, secret handling, updates and rollback.

This document does not create schemas, registry files, an installer, provisioner, Docker or Portainer access, shell execution, connector gateway, scheduler, queue, approval engine, memory engine or external action.

## Core model

### Capability

A capability describes the user outcome.

Examples:

```text
document_analysis
hybrid_retrieval
llm_observability
google_drive_read
```

A capability declares required roles and acceptable outcomes. It does not name one mandatory implementation unless a reviewed preset does so.

### Resource

A resource is the concrete component, service, runtime, connector, store or endpoint that may fulfil one or more roles.

Examples:

```text
Docling Serve
Langfuse
Google Drive connector
PostgreSQL
Hermes Agent
```

Each resource retains an explicit internal type such as `infrastructure_module`, `runtime`, `binding`, `data_store`, `observability_surface`, `secret_reference` or `exposure`.

### Preset

A preset is a versioned Pantheon-oriented configuration of one resource or a bounded composition of resources.

A preset may define:

```text
version pins
ports
volumes
resource limits
network exposure
secret references
health checks
backup posture
rollback posture
Hermes bindings
OpenWebUI exposure
indexing or retention policy
```

A preset is not approval and does not execute itself.

### Binding

A binding is a governed relationship between two resources or between a resource and a scope.

Examples:

```text
Hermes -> Docling
Hermes -> Langfuse
Project Leroux -> Google Drive folder
OpenWebUI -> Hermes
```

A binding may be proposed, configured, observed or activated. It is not installed like a container.

### Provisioner

A provisioner is the external mechanism that performs an approved installation or configuration change.

Examples:

```text
Portainer
Docker Compose
NAS package manager
bounded SSH provisioner
manual operator
```

Pantheon may prepare a handoff for a provisioner. Pantheon is not the provisioner.

## Generic relationship

```text
Capability
  requires role
    -> Resource
      configured by
        -> Preset
          connected through
            -> Binding
              deployed or applied by
                -> Provisioner
```

Pantheon surrounds the chain with:

```text
Policy
Gate
Decision
Evidence
Status
History
Rollback
```

## User-facing simplification

The dashboard may expose one simple card grammar:

```text
Title
Description
Simplified status
Tap for details
```

Recommended simplified statuses:

```text
Available
To review
Ready
Installed
Action required
Blocked
```

Detailed internal states remain separate:

```text
catalog_status
install_status
configuration_status
connection_status
health_status
activation_status
adoption_status
```

The simplified status is a projection. It must not collapse the internal distinctions.

## Two user entry paths

### Outcome-first

The user selects a capability such as document analysis. Pantheon resolves candidate resources, detects existing resources, proposes a preset and prepares an installation or adoption candidate.

### Infrastructure-first

Pantheon observes existing resources such as Docker, PostgreSQL, OpenWebUI or Langfuse. The user may adopt, keep external, connect, ignore, replace or repair them.

The two paths meet at the same governed resource model.

## Three proving cases

### Case A — Docling

```yaml
capability:
  id: document_analysis
  required_roles:
    - document_extraction

resource:
  id: docling
  resource_type: infrastructure_module
  provides_roles:
    - document_extraction
    - markdown_derivation

preset:
  id: docling_cpu_internal
  resource: docling
  configuration:
    execution_profile: cpu
    exposure: internal_only
    temporary_storage: isolated
    direct_professional_folder_access: false
  health:
    kind: http
  rollback:
    strategy: previous_image

binding:
  from: hermes
  to: docling
  mode: internal_http

provisioner:
  allowed:
    - portainer
    - docker_compose
```

Governance distinctions:

```text
Markdown derivative != original source
service healthy != extraction validated
installed != authorized for professional dossiers
```

### Case B — Langfuse

```yaml
capability:
  id: llm_observability
  required_roles:
    - llm_trace_observability

resource:
  id: langfuse
  resource_type: observability_surface
  provides_roles:
    - llm_trace_observability

preset:
  id: langfuse_private_redacted
  resource: langfuse
  configuration:
    deployment: self_hosted_candidate
    exposure: internal_only
    prompt_redaction: required
    retention: limited
    environment_separation: required

binding:
  from: hermes
  to: langfuse
  mode: telemetry_export

provisioner:
  allowed:
    - portainer
    - docker_compose
```

Governance distinctions:

```text
trace != evidence
score != professional validation
healthy != safe for sensitive prompts
```

### Case C — Google Drive

```yaml
capability:
  id: google_drive_read
  required_roles:
    - governed_document_source

resource:
  id: google_drive
  resource_type: external_connection
  provides_roles:
    - governed_document_source

preset:
  id: google_drive_project_read_only
  resource: google_drive
  configuration:
    auth: oauth_external_secret
    mode: read_only
    scope: explicit_folders_only
    global_sync: false
    deletion: false
    mutation: false

binding:
  from: project_scope
  to: google_drive_folder
  mode: scoped_read

provisioner:
  allowed:
    - connector_config_adapter
    - manual_oauth_setup
```

Governance distinctions:

```text
connected != authorized for every folder
OAuth valid != mutation allowed
source reachable != source admitted as evidence
```

## Deliberate exclusions

The following are not canonical objects in this first model:

```text
Blueprint
Solution
Capability Pack
Provider as a generic synonym for Resource
Knowledge Card inside the install catalog
```

They may later exist as views, aliases, specialized resources or high-level presets if concrete usage requires them.

`Provider` remains reserved for model or service providers such as OpenAI, Anthropic, Mistral, Ollama endpoints or vLLM endpoints.

## Manifest direction

A future implementation may begin with only:

```text
catalog/capabilities/
catalog/resources/
catalog/presets/
```

Bindings and provisioner declarations may initially remain nested inside presets. They should become independent records only when their lifecycle, reuse or review requirements justify it.

No live catalog directory is created by this document.

## Installation candidate flow

```text
select capability
-> observe existing resources
-> choose candidate resource
-> select preset
-> resolve dependencies and conflicts
-> show impact
-> prepare Installation Candidate
-> human approval
-> external provisioner
-> installation result candidate
-> health observation
-> activation decision
```

Required distinctions:

```text
candidate_prepared != installation_authorized
installation_authorized != installation_executed
installed != configured
configured != connected
connected != activated
healthy != safe
preset_selected != preset_approved
binding_created != binding_activated
```

## Final rule

```text
Capabilities express intent.
Resources provide concrete means.
Presets adapt those means to Pantheon.
Bindings connect them under scope.
Provisioners execute approved changes outside Pantheon.
Pantheon governs.
The human decides.
```