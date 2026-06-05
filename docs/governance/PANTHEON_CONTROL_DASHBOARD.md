# Pantheon Control Dashboard

Status: candidate — to verify. This document captures the proposed dashboard and installer surface for managing a Pantheon-oriented tool stack.

This document is documentation only. It does not implement a UI, installer, Docker stack, API gateway, MCP runtime, connector runtime, scheduler, queue, plugin manager, update engine, backup engine, approval engine or memory promotion engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Control is the proposed administration surface for a local, server or NAS-hosted Pantheon tool stack.

It should let an administrator see:

```text
what is installed
what is configured
what is connected
what is healthy
what is authorized
what is blocked
what requires approval
what is only candidate
what changed since the last version
```

It is more than a first-run installer. It is a persistent dashboard for installation, configuration, preflight, updates, backup, restore, module selection and connection review.

## Boundary

Pantheon Control is not Pantheon Next itself.

Pantheon Next holds governance doctrine, rules, manifests, templates and candidate specs.

Pantheon Control, if built, would read those specs and generate or manage operational configuration outside the governance repository.

```text
Pantheon Next defines the rules.
Pantheon Control displays and applies stack configuration under those rules.
Docker and external tools execute.
The human decides.
```

Pantheon Control must not become:

```text
a hidden runtime
a scheduler
a queue
a provider router
a role executor
a rite executor
a connector gateway with automatic authority
a plugin marketplace with implicit approval
a memory promotion engine
a truth engine
a substitute for human approval
```

## Core distinction

The dashboard must make four states visibly different:

```text
installed != connected
connected != authorized
authorized != validated
validated != automatic action
```

A module card must therefore show at least:

```text
installation status
configuration status
connection status
health status
activation status
task authorization status
risk class
required gate
last preflight result
```

## Dashboard areas

The proposed dashboard should contain these areas:

```text
Overview
Modules
Connections
Preflights
Instances
Machine inventory
Runtime endpoints
Model catalog
Stack generator
Config versions
Updates
Backup / Restore
Secrets metadata
Logs / audit
Expert mode
```

### Overview

The overview is a status cockpit. It should show the stack at a glance:

```text
OpenWebUI: healthy
Hermes Agent: healthy
PostgreSQL / pgvector: healthy
Valkey / Redis: healthy
SearXNG: degraded
Qdrant: healthy
ComfyUI: stopped
GitHub sync: active
NAS mirror: last sync known
Telegram: receiving, sending gated
Google: token expiring
Ollama workstation: reachable
GPU worker: degraded
```

### Modules

The module view lists all declared modules and their status.

A module card should include:

```text
module id
role
status
required / optional
installed version
config schema version
primary / secondary role
allowed outputs
forbidden outputs
risk level
dependencies
conflicts
preflight summary
machine assignment
endpoint links
actions: configure, test, disable, update, logs
```

Example statuses:

```text
unavailable
detected
disabled
candidate
sandbox_enabled
project_enabled
dossier_enabled
domain_enabled
organization_enabled
task_authorized
suspended
deprecated
rejected
```

### Connections

Connections must be displayed as governed links, not just network links.

A connection card should declare:

```text
source module
target module
connection type
direction
mode
scope
secret status
version
health
risk
required gate
last checked
```

Connection types include:

```text
HTTP API
MCP
OAuth
Webhook
Database
Vector store
Filesystem
Git remote
Browser worker
Runtime worker
Message channel
Local model endpoint
GPU worker endpoint
```

The dashboard should explicitly show when an MCP server is reachable but no tool is task-authorized.

## Machine inventory

Pantheon Control should not only list Docker services. It should also inventory machines that expose useful local capabilities.

Examples:

```text
NAS main
server test
server prod
workstation GPU
laptop local
remote browser worker
remote ComfyUI worker
```

A machine record should include:

```text
machine id
name
role
location
network address
last seen
operating system
Docker availability
GPU availability
Ollama availability
ComfyUI availability
browser worker availability
MCP servers exposed
storage paths exposed
privacy class
allowed scopes
health status
```

Machine statuses:

```text
offline
reachable
healthy
degraded
overloaded
blocked_by_policy
unknown
```

Machine inventory must remain descriptive. It must not become a scheduler, queue or provider router.

## Runtime endpoints

Runtime endpoints should be displayed as governed execution surfaces.

Examples:

```text
Ollama endpoint
OpenAI-compatible endpoint
vLLM endpoint
llama.cpp server
LM Studio endpoint
ComfyUI endpoint
Playwright browser worker
MCP server
Hermes worker
```

An endpoint record should include:

```text
endpoint id
machine id
type
base URL or local socket
version
health
models or tools exposed
read/write capability
external effect capability
privacy class
allowed scopes
required gate
last preflight result
```

A reachable endpoint is not an authorization. A model endpoint may be healthy while still unauthorized for a task.

## Model catalog

Pantheon Control should expose a model catalog for local and remote models.

A model record should include:

```text
model id
provider
runtime endpoint
machine id
model family
context window
input modes
output modes
embedding dimension when applicable
vision support
audio support
local / LAN / external classification
allowed scopes
recommended uses
forbidden uses
last availability check
```

Example:

```text
llama-local-01
provider: Ollama
endpoint: workstation-ollama
machine: workstation-gpu
mode: local LAN
supports: chat
forbidden: external delivery without review
```

Changing an embedding model should trigger a reindex warning because vector spaces are not interchangeable.

## Module-to-machine links

The dashboard should show where each module actually runs or which machine capability it depends on.

Examples:

```text
OpenWebUI -> NAS main
Hermes Agent -> server test
ComfyUI -> workstation GPU
Qdrant -> NAS main
Ollama chat model -> workstation GPU
Playwright worker -> server test
SearXNG -> NAS main
```

A module may be installed but unavailable if its assigned machine is offline.

The dashboard should show:

```text
module
assigned machine
required endpoint
fallback endpoint
current health
last machine preflight
scope restrictions
```

## Preflights as first-class dashboard items

Preflights must not be hidden in logs. They should be visible, repeatable and inspectable.

A preflight answers:

```text
Can the module respond?
Is its configuration compatible?
Are its dependencies connected?
Is its assigned machine available?
Is the required endpoint reachable?
Is the required model present?
Is it activated for this scope?
Is it authorized for this task?
Does it produce the required evidence?
Does it respect memory rules?
Does it refuse forbidden actions?
```

The dashboard should show preflights in three layers:

```text
Technical preflight
Connection preflight
Governance preflight
```

And specialized suites:

```text
Machine preflight
Endpoint preflight
Model preflight
Memory preflight
Invocation preflight
Update preflight
Backup / restore preflight
```

### Preflight result shape

A minimal preflight result should include:

```yaml
preflight_result:
  module_id:
  preflight_type:
  status:
  detected:
  configured:
  connected:
  healthy:
  machine_available:
  endpoint_available:
  model_available:
  activation_status:
  task_authorized:
  allowed_uses:
  blocked_uses:
  required_gates:
  evidence_required:
  memory_behavior:
  refusal_tests:
  last_checked_at:
  next_action:
```

### Preflight display states

Suggested display states:

```text
pass
pass_with_gate
warning
blocked
failed
unknown
not_applicable
```

Examples:

```text
Telegram receive: pass
Telegram send: pass_with_gate
GitHub direct merge: blocked
Vector retrieval as proof: blocked
Memory auto-promotion: blocked
SearXNG search: warning if degraded engines
PostgreSQL extension vector: pass
Ollama endpoint reachable: pass
Model missing on assigned machine: failed
GPU worker overloaded: warning
```

## Machine and model preflight display

Machine and model preflights should verify local execution surfaces without turning them into automatic routing.

Minimum checks:

```text
machine reachable
Docker available when required
required ports reachable
Ollama endpoint reachable when declared
model list readable
required model present
embedding model matches index metadata
GPU visible when required
VRAM sufficient for declared workload
ComfyUI queue reachable when declared
browser worker can read/screenshot only unless gated
MCP tools listed but not task-authorized by default
```

The dashboard may show eligible endpoints, but it must not silently choose a runtime for consequential work.

## Memory preflight display

The dashboard should show memory preflight results separately, because memory errors persist.

Minimum visible checks:

```text
Memory Candidate creation
Evidence linkage
Scope isolation
Automatic promotion blocked
OpenWebUI Knowledge != Canonical Memory
Hermes candidate-only behavior
Embedding match != memory
Private data minimization
Revocation path
Supersession path
```

A compliant memory layer is one that can retain, refuse, isolate, supersede, revoke and require approval.

## Invocation preflight display

Invocation preflight should expose the eligibility of:

```text
god call
rite call
place / scope
connection requirements
task contract
expected outputs
forbidden outputs
refusal tests
```

This links to the candidate `MODULE_INVOCATION_PREFLIGHT.md` work. The dashboard should not execute gods or rites. It should display which governance roles and rites are required or suggested.

## Stack generator

The dashboard may generate operational files from governed declarations.

Inputs:

```text
module catalog
stack blueprint
instance manifest
connection registry
machine inventory
endpoint registry
model catalog
config schemas
compatibility matrix
secret names
user selections
```

Outputs, outside Pantheon Next:

```text
docker-compose.yml
docker-compose.override.yml
.env local file
Caddyfile or reverse proxy config
module config files
connection registry instance file
machine inventory instance file
endpoint registry instance file
model catalog instance file
versions.lock.json
backup scripts
update scripts
healthcheck definitions
```

The dashboard must show a diff before writing generated files.

## Config versioning and update gates

The dashboard should not allow runtime updates when the target configuration is not known and versioned.

Rule:

```text
No compatible config, no update.
No validated migration, no update.
No backup, no update.
No healthcheck, elevated risk.
```

Required objects:

```text
versions.lock.json
config-history/
compatibility.matrix.yml
config schemas
migration scripts
checksums
```

When a module update is detected, the dashboard should display:

```text
installed image version
target image version
current config schema
target config schema
migration availability
backup requirement
risk level
healthcheck availability
approval requirement
```

Major database updates, schema migrations, OAuth scope changes, reverse proxy changes and write-capable connector changes should be blocked by default until reviewed.

## Backup and portable export

The dashboard should support a portable export of user data and configuration.

Suggested artifact:

```text
pantheon-export-YYYYMMDD-HHMM.pantheon.zip
pantheon-export-YYYYMMDD-HHMM.pantheon.tar.zst
```

It should include:

```text
manifest.json
checksums.sha256
versions.lock.json
redacted env
optional encrypted secrets
PostgreSQL dumps
Qdrant or Chroma snapshots if enabled
OpenWebUI user data
Hermes configuration and useful logs
ComfyUI workflows and custom nodes manifest
SearXNG settings
Git bundle of Pantheon Next
install / update / sync events
connection registry
module registry
machine inventory
endpoint registry
model catalog
```

Secrets must not be exported in clear text. Connectors with external write ability should be disabled by default after restore until explicitly revalidated.

## Module choice rules

The dashboard should expose conflicts and overlaps.

Examples:

```text
Reverse proxy: Caddy OR Traefik OR Nginx Proxy Manager
Vector store primary: pgvector OR Qdrant OR Chroma OR OpenSearch
Search web primary: SearXNG OR Brave Search API OR Tavily
Local model runtime: Ollama OR vLLM OR llama.cpp OR LM Studio endpoint
Cache: Valkey OR Redis
Workflow orchestrator: Hermes primary, others secondary unless explicitly scoped
Browser agent: Playwright primary; Brave human browser optional
```

Multiple tools may coexist only when their roles are explicit: primary, fallback, secondary, sandbox or migration target.

## Expert mode

Expert mode may allow:

```text
port changes
volume changes
endpoint changes
machine assignment changes
model endpoint assignment changes
custom module declarations
plugin/addon activation
generated file override
raw logs
docker compose dry-run
manual preflight rerun
pinning versions
ignoring a version
rollback
```

Expert changes must create a visible diff and a config snapshot.

## Repository relationship

This candidate does not authorize adding executable dashboard code, Docker files, `operations/`, `platform/` files or `.env` files to Pantheon Next.

Allowed here:

```text
doctrine
candidate specs
templates
fictional examples
AI logs
```

Executable implementation, if later approved, should live outside Pantheon Next or behind an explicitly validated boundary.

## Open questions

```text
Should Pantheon Control be a separate repository?
Should dashboard module specs live under docs/governance or templates first?
Should connection registry and preflight registry be split?
Should machine inventory, endpoint registry and model catalog be separate specs?
Which preflight failures suspend a module automatically?
Which update classes require a PR before applying to an instance?
Should Notion mirror dashboard status or only track governance decisions?
```

## Final rule

```text
Pantheon Control may show, configure, test, diff, backup and restore.
It may show available machines, endpoints and models.
It must not decide truth, approve actions, promote memory, route providers silently or run hidden work.
```