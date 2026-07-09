# Governed Resource Dashboard Model

Status: candidate support doctrine — documented non-implemented.

Boundary profile: candidate_support_note.

Placement: runtime-adapter support / dashboard governance candidate.

This document defines a simplified dashboard model for governing installable modules, runtime surfaces, AI nodes, model bindings, exposures and policies without collapsing Pantheon Next into a runtime, installer, provider router, plugin marketplace, scheduler, queue or approval engine.

It is not a UI implementation.

It is not a schema.

It is not a Docker, Portainer, OpenWebUI, Hermes, Ollama, PostgreSQL, reverse-proxy or secret-store installation plan.

It is not an authorization to modify protected paths.

## Purpose

Pantheon runtime governance needs to be understandable for non-expert users without losing the internal distinctions that keep governance separate from execution.

The proposed simplification is:

```text
User-facing surface:
  Resource Card

Internal model:
  strictly typed governed resource
```

A user may see one simple card pattern.

Pantheon must still keep the real type, dependency, adapter, gate, evidence expectation, rollback posture and forbidden inference for each resource.

## Problem

A dashboard that only says `modules` is too coarse.

It hides material differences between:

```text
PostgreSQL container
OpenWebUI instance
Hermes runtime
Hermes provider binding
Hermes toolset policy
Hermes skill
Ollama workstation node
local model
OpenWebUI -> Hermes connection
public HTTPS exposure
secret reference
memory policy
```

These do not share the same lifecycle, risk, adapter, evidence or approval gate.

A dashboard that exposes every distinction directly is too complex for a beginner.

The model therefore separates the interface simplification from the governance ontology.

## Core rule

```text
Resource Card is a UX simplification.
Governed Resource is the internal typed object.
```

Pantheon may display different resource kinds through a common card surface.

Pantheon must not flatten them internally.

## User-facing Resource Card

A Resource Card may show:

```text
name
description
status summary
risk summary
dependencies
actions
last observation
next required decision
rollback / backup note
```

Common user-facing actions may include:

```text
install
adopt
configure
activate
deactivate
update
downgrade
repair
remove
replace
keep external
view risks
view diff
view rollback
```

The fact that actions appear under one common surface does not mean they are executed the same way or carry the same gate.

## Internal resource types

Every Resource Card must map to one explicit internal type.

```text
infrastructure_module
runtime
runtime_surface
ai_runtime_node
model
binding
policy
secret_reference
exposure
data_store
prompt_surface
observability_surface
backup_surface
```

### Type guidance

```text
infrastructure_module:
  installable or adoptable external component such as OpenWebUI, PostgreSQL,
  pgvector, Portainer, Langfuse or SearXNG.

runtime:
  external execution runtime such as Hermes Agent.

runtime_surface:
  configurable native surface of a runtime, such as Hermes providers, models,
  toolsets, MCP entries, skills, profiles, memory settings, cron, gateway or API server.

ai_runtime_node:
  workstation or server exposing local inference capacity, such as Ollama, vLLM,
  LM Studio or LocalAI.

model:
  model artifact or served model observed on a runtime node or provider.

binding:
  governed relationship between resources, such as OpenWebUI -> Hermes,
  Hermes -> model endpoint, model -> node, provider -> scope, or tool -> project.

policy:
  rule surface for approvals, memory, evidence, external actions, network,
  fallback, data sensitivity or retention.

secret_reference:
  reference to a secret or credential location. The dashboard may govern
  status and handling but must not become a secret store by implication.

exposure:
  network or publication surface such as localhost, LAN, public HTTPS,
  reverse proxy, CORS or WebSocket handling.

data_store:
  persistent state, database, volume, vector store or managed data directory.

prompt_surface:
  governed prompt-related surface such as SOUL.md, context files, system prompt
  overlays, role prompts or tool policy excerpts.

observability_surface:
  health, logs, runtime traces or telemetry status.

backup_surface:
  backup, restore, snapshot or rollback posture.
```

## Lifecycle states

The common lifecycle vocabulary is:

```text
listed
observed
detected
selected
adoption_pending
adopted
install_pending
installed
configured
configuration_observed
health_observed
activation_pending
activated
degraded
update_available
update_authorized
update_applied
rollback_available
rollback_authorized
deactivation_pending
deactivated
removal_pending
removed
retired
blocked
```

Not every type uses every state.

A state must be interpreted through the resource type.

For example, a `runtime_surface` is usually configured or activated, not installed as a standalone module.

A `binding` is created, verified and activated; it is not installed like a container.

A `secret_reference` may be present or missing; it must not be treated as Pantheon-owned secret material.

## Chronological phases

The dashboard must avoid circular dependencies.

```text
Phase 0 — Seed
  Minimal Pantheon bootstrap.
  No dependency on OpenWebUI, Hermes, PostgreSQL, Portainer, Ollama or Langfuse.

Phase 1 — Bootstrap Dashboard
  Minimal local dashboard or setup surface.
  Uses bootstrap state only.
  Displays enough to install, adopt or keep external the baseline resources.

Phase 2 — Discovery
  Detects container runtime, existing modules, existing runtimes, ports,
  volumes, managed config locations, AI runtime nodes and candidate bindings.

Phase 3 — Adoption / installation
  Human chooses per resource: adopt existing, install missing, ignore,
  keep external, replace or repair.

Phase 4 — Durable state
  Persistent state store is installed or adopted where required.
  Bootstrap state may be migrated.

Phase 5 — Full Dashboard
  Full resource dashboard becomes available after baseline state and control
  surfaces are installed or adopted.

Phase 6 — Runtime configuration
  Runtime surfaces are configured through adapters that use native mechanisms.
  Hermes configuration is applied through Hermes-native configuration surfaces,
  not by treating every Hermes surface as a Pantheon module.

Phase 7 — Bindings
  Connections are created or updated only after both sides exist or are adopted.

Phase 8 — Activation
  Consequential uses are activated after configuration, health observation,
  scope review and human approval where required.

Phase 9 — Maintenance
  Updates, downgrades, backups, restore checks, deactivation, removal and
  retirement are handled as governed lifecycle actions.
```

## Dependency rule

```text
A resource may be displayed before installation.
A resource may be discovered before adoption.
A resource may be configured only after installation or adoption.
A resource may be activated only after configuration and observation.
A consequential use requires a separate approval gate.
```

This rule prevents cycles such as:

```text
Full dashboard requires PostgreSQL,
but PostgreSQL requires the full dashboard to be installed.
```

The correct pattern is:

```text
bootstrap dashboard -> install/adopt PostgreSQL -> migrate state -> full dashboard
```

It also prevents:

```text
OpenWebUI is required to configure Hermes,
but Hermes is required before OpenWebUI can bind to Hermes.
```

The correct pattern is:

```text
bootstrap / adapter configures Hermes -> Hermes API observed -> OpenWebUI binding created
```

## Adapter model

A Resource Card never executes by itself.

Each actionable resource resolves to an adapter or external runtime.

Candidate adapter families:

```text
container_adapter:
  Docker, Podman, Portainer or equivalent external provisioner.

hermes_config_adapter:
  Hermes-native configuration surfaces such as config commands, config files,
  managed scope, model selection, tools, MCP, skills, profiles, gateway and doctor checks.

openwebui_config_adapter:
  OpenWebUI installation/adoption, initial environment, persisted configuration,
  provider/agent connections, admin settings and health checks.

ai_runtime_node_adapter:
  local or remote inference-node discovery, pairing, adoption, model inventory,
  context qualification, model install request and health status.

exposure_adapter:
  reverse proxy, HTTPS, CORS, WebSocket, public/LAN/localhost exposure and
  exposure rollback.

secret_reference_adapter:
  external secret-store reference, credential presence checks, redaction and
  secret-handling gates.

backup_adapter:
  backup, restore, snapshot, rollback and destructive-action preflight.
```

Adapters may apply changes only when the action is authorized under the relevant gate.

Pantheon governs the decision and state.

The adapter or external runtime performs the operation.

## Gates

Every action must resolve to a gate class.

```text
safe_read:
  read-only status or documentation display.

normal_change:
  reversible configuration or installation change with limited blast radius.

sensitive_change:
  provider, model, tool, memory, network, connector, runtime surface or scope change.

destructive_change:
  deletion, volume removal, irreversible reset, downgrade with data migration risk,
  secret removal or state-store replacement.

external_exposure:
  public/LAN exposure, reverse proxy, webhook, gateway or outbound connector surface.

secret_handling:
  API keys, OAuth, tokens, shared env, service accounts or credentials.

memory_or_evidence:
  memory capture, memory promotion, evidence claim, trace admission or register update.

runtime_execution:
  operation that invokes an external runtime, provisioner, node agent, CLI, container,
  SSH, MCP server, gateway or model endpoint.
```

Gate result vocabulary:

```text
allow
allow_with_gate
needs_approval
needs_evidence
needs_revision
block
to_verify
```

## Non-equivalence rules

```text
listed ≠ authorized
observed ≠ adopted
detected ≠ approved
installed ≠ activated
adopted ≠ safe
configured ≠ effective
configuration_observed ≠ usage_authorized
healthy ≠ safe
connected ≠ approved_for_scope
node_detected ≠ node_adopted
model_downloaded ≠ model_approved
provider_configured ≠ provider_authorized
binding_created ≠ binding_activated
secret_present ≠ secret_governed
managed_scope_applied ≠ hard_security_boundary
public_url_reachable ≠ public_exposure_approved
update_available ≠ update_authorized
update_applied ≠ validated
downgrade_possible ≠ downgrade_safe
backup_exists ≠ backup_verified
rollback_known ≠ rollback_decided
removed ≠ data_forgotten
```

## OpenWebUI placement

An installed or adopted OpenWebUI instance is an `infrastructure_module` resource.

The OpenWebUI user interface is exposed by that module, but the instance itself is not typed as `exposure`.

Its connection to Hermes, Ollama, OpenAI-compatible endpoints or other providers is a `binding`, not the same resource as the OpenWebUI instance.

Its localhost, LAN or public HTTPS availability is a separate `exposure` resource, not proof that the interface is safe or approved.

OpenWebUI must not become the governor, installer, provider authority, model authority, memory authority, approval engine or unmanaged model marketplace by implication.

## Hermes placement

Hermes Agent is an external execution runtime.

Hermes itself may be represented as a `runtime` resource.

Hermes-native configuration areas are `runtime_surface` resources, not installable Pantheon modules by default.

Examples:

```text
provider/model configuration
toolset policy
MCP entries
skills
profiles
memory settings
cron
gateway / API server
SOUL.md and context surfaces
```

Pantheon may govern intended configuration, approval gates and observed status.

Hermes-native mechanisms or a Hermes adapter apply the configuration.

Hermes execution results return as candidates until governed review is complete.

## AI runtime node placement

A local or remote inference host is an `ai_runtime_node`.

Examples include a workstation running Ollama, a GPU server running vLLM, LM Studio on a desktop, LocalAI, or another OpenAI-compatible local endpoint.

A model on that node is a `model` resource.

The relationship between a model, node, runtime and usage scope is a `binding`.

A node may be detected before adoption.

A model may be observed or downloaded before it is authorized for Hermes, OpenWebUI, a project or sensitive data.

## Forbidden interpretations

This model must not be read as creating:

```text
live dashboard implementation
module registry
plugin marketplace
installer
Portainer stack
Docker file
shell runner
provider router
MCP host
scheduler
queue
automatic approval engine
automatic memory engine
secret store
model marketplace
runtime orchestrator
automatic fallback router
external-send channel
```

Any such implementation must be introduced as a separate implementation artifact or external runtime adapter and classified under the existing protected-path and authority rules.

## Implementation status

```text
implemented:
  none in this document.

documented non-implemented:
  Governed Resource Dashboard model, Resource Card simplification, internal
  type taxonomy, lifecycle states, chronological phases, dependency rule,
  adapter classes and gate classes.

partial:
  Existing repository documentation already contains related runtime-adapter,
  Hermes, OpenWebUI, install catalog, status and non-equivalence doctrine.
  This document consolidates the dashboard-facing model only.

to verify:
  Exact future adapter contracts, UI behavior, state storage, health checks,
  external runtime compatibility, OpenWebUI behavior, Hermes behavior and
  AI runtime node mechanics.

obsolete:
  Any interpretation that treats a preset, module list or resource card as
  automatic installation, activation, approval, safety or adoption.

non applicable:
  Direct runtime execution by Pantheon.
```

## Promotion path

This candidate may be promoted only if a referent is added under the repository authority rules, such as:

```text
read-only status report for resource cards
schema for governed resources
test coverage for lifecycle/non-equivalence rules
static prototype explicitly marked documented non-implemented
human decision recorded in ai_logs
```

Until then, this document remains candidate support doctrine and must not be treated as implemented behavior.

## Final rule

```text
Simplify the user surface.
Do not simplify away the governance ontology.
```
