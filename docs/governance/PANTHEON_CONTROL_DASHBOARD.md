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
```

The dashboard should explicitly show when an MCP server is reachable but no tool is task-authorized.

## Preflights as first-class dashboard items

Preflights must not be hidden in logs. They should be visible, repeatable and inspectable.

A preflight answers:

```text
Can the module respond?
Is its configuration compatible?
Are its dependencies connected?
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
```

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
Which preflight failures suspend a module automatically?
Which update classes require a PR before applying to an instance?
Should Notion mirror dashboard status or only track governance decisions?
```

## Final rule

```text
Pantheon Control may show, configure, test, diff, backup and restore.
It must not decide truth, approve actions, promote memory or run hidden work.
```