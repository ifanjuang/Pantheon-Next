# Cockpit Capability Management

Status: candidate support doctrine — capability lifecycle management boundary — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines how the Pantheon cockpit may manage the lifecycle of external runtime capabilities — skills, functions, workflows, runtime agents, plugins and MCP bindings — without becoming the execution runtime, plugin manager, workflow engine, agent host, scheduler, provider router or automatic approval system.

It complements `COCKPIT_RUNTIME_CONFIGURATION_ASSISTANCE.md`.

```text
Raw runtime configuration assistance
!= capability lifecycle management
```

The former remains deliberately narrow and version-sensitive. The latter is a central cockpit responsibility.

## 1. Decision

The cockpit must provide a unified capability-management surface for:

```text
skills
functions and tools
workflows
runtime agents / profiles
plugins
MCP servers and bindings
connectors where admitted
```

The selected operating pattern is:

```text
Cockpit displays and captures the human decision
-> Pantheon MCP qualifies the capability, status, scope and requested effect
-> Hermes adapter / native runtime surface performs the admitted operation
-> Cockpit receives the technical receipt and updated observation
-> Pantheon keeps technical success separate from approval, evidence and task authorization
```

The cockpit manages the lifecycle and governance view. Hermes executes native capability operations. The Pantheon MCP remains the policy and validation source.

## 2. Responsibility boundary

```text
exposed_by:
  Pantheon MVP Cockpit, Hermes Pantheon Modules dashboard surface, or another
  reviewed cockpit projection.

executed_by:
  Hermes Agent and its native plugin, skill, tool, MCP, profile and workflow
  mechanisms; another explicitly admitted runtime adapter where applicable.

governed_by:
  Pantheon capability classification, provenance, installation status, health,
  update status, activation, scope, evidence expectations, approval gates,
  rollback posture and non-equivalence rules, exposed through the Pantheon MCP.

approved_by:
  Human for installation, adoption, activation, scope expansion, update,
  replacement, destructive removal and consequential execution permissions.

forbidden:
  Pantheon becoming the plugin manager, skill runtime, workflow engine, agent
  host, MCP host, package installer, scheduler, queue, provider router, secret
  store or automatic approval engine.
```

## 3. User-facing cockpit structure

Recommended top-level cockpit area:

```text
Capabilities / Fonctions
```

Recommended categories:

```text
Skills
Functions & Tools
Workflows
Agents
Plugins
MCP & Connectors
```

The cockpit may use a common card layout, but each card must retain its concrete type and native runtime owner.

Common card fields:

```text
name
type
description
source and provenance
runtime owner
installed version
candidate update
installation status
native enabled state
Pantheon approval status
scope activation
health observation
dependencies
permissions / effects
evidence expectations
last observation
last action receipt
rollback posture
next required decision
```

## 4. Capability types

### 4.1 Skill

A skill is a reusable instruction and resource package consumed by an external runtime.

The cockpit may manage:

```text
discovery
source review
installation proposal
native installation status
enable / disable state
scope and task-family admissibility
version and update status
draft creation or amendment candidate
retirement or replacement
```

The cockpit does not execute the skill by itself.

### 4.2 Function or tool

A function is a callable capability exposed by Hermes, a plugin, an MCP server, a connector or another admitted runtime.

The cockpit may manage:

```text
inventory
origin
input/output contract
side-effect class
native exposure state
allowlist membership
scope activation
preflight requirement
health or probe result
suspension
```

```text
function visible != function authorized
function callable != function authorized for every scope
runtime success != evidence
```

### 4.3 Workflow

A workflow card represents an external runtime workflow or a binding of a Pantheon Workflow Manifest to an external executor.

The cockpit may manage:

```text
draft Workflow Manifest candidate
selected capabilities and dependencies
runtime binding
activation scope
schedule reference when externally owned
run eligibility
suspend / resume state
version and replacement
last run and receipt references
```

Pantheon does not become the workflow engine, scheduler, queue or retry runtime.

```text
Workflow Manifest selected != workflow authorized
workflow installed != workflow active
workflow run succeeded != result approved
```

### 4.4 Runtime agent

An Agent card refers only to an external runtime agent, profile or agent configuration executed by Hermes or another admitted runtime.

It must not be confused with Pantheon Roles or gods.

```text
Pantheon Role != runtime agent
Zeus / Athena / Hermes as governance viewpoints != autonomous agents
```

The cockpit may manage:

```text
agent/profile inventory
purpose and capability set
model/provider binding reference
skill, function and workflow bindings
scope and data-access limits
native enabled state
activation status
health and last execution receipt
version or profile revision
suspension and retirement
```

The runtime creates and executes the agent. Pantheon governs its admissibility, effects and scope.

### 4.5 Plugin

A plugin is an installable extension package owned by Hermes, OpenWebUI or another admitted host.

The cockpit may manage:

```text
catalog or discovered inventory
source and version
review status
installation proposal
native installation
native enable / disable
capabilities added
permissions and hooks
health / probe result
update availability
update authorization
rollback or disable path
removal proposal
```

```text
installed != approved
enabled != activated for a scope
healthy != safe
update_available != update_authorized
```

### 4.6 MCP server or binding

An MCP server is an external capability provider. Pantheon does not become its host.

The cockpit may manage:

```text
catalog entry or discovered server
source and transport
runtime binding
allowed tools
prompts/resources/sampling posture
authentication presence without secret exposure
native enabled state
probe status
scope activation
update and rollback posture
```

The Hermes MCP client or another admitted runtime owns the connection and execution.

## 5. Lifecycle states

Every capability keeps separate state axes.

### 5.1 Supply and installation

```text
listed
discovered
review_pending
selected
install_proposed
install_authorized
installed
install_failed
external_only
removed
retired
```

### 5.2 Native runtime state

```text
not_configured
configured
disabled
enabled
degraded
unreachable
unknown
```

### 5.3 Pantheon governance state

```text
unreviewed
candidate
approved_for_sandbox
approved_for_project
approved_for_production
suspended
blocked
superseded
```

### 5.4 Update state

```text
update_unknown
up_to_date
update_available
update_review_pending
update_authorized
update_applied
rollback_available
rollback_authorized
rollback_applied
```

These axes must never be collapsed into one badge.

## 6. Cockpit actions

### 6.1 Read actions

```text
refresh inventory
inspect source
inspect manifest or contract
show capabilities and permissions
show dependencies
show native state
show Pantheon status
show scope activation
show health
show update diff
show rollback
show last technical receipt
```

### 6.2 Candidate and authoring actions

```text
propose installation
propose adoption of an existing capability
create a skill draft
create or amend a Workflow Manifest candidate
create or amend a runtime-agent profile candidate
propose a function allowlist
propose plugin activation
propose MCP binding
propose update, replacement or retirement
request review or evidence
```

Creation produces a candidate. It does not install, enable or authorize the result automatically.

### 6.3 Native lifecycle actions

The cockpit may expose bounded actions when a reviewed Hermes/native adapter supports them:

```text
install reviewed package
enable
disable
suspend
resume within an approved scope
probe
apply one authorized update
restore the previous supported version
remove only through a separately gated destructive path
```

Each mutation must be separately confirmed and must return a technical receipt.

The cockpit button does not execute code itself. It requests one native operation from the external executor.

## 7. Action flow

A consequential capability action follows this sequence:

```text
1. Cockpit reads current native state and exact runtime version.
2. Cockpit creates one Capability Action Candidate.
3. Pantheon MCP validates type, source, current state, requested effect, scope,
   required approval, evidence expectation and rollback posture.
4. Human approves one action, one target, one version and one scope.
5. Hermes adapter performs the native operation.
6. Adapter returns a technical receipt and fresh observation.
7. Cockpit shows applied, partial, failed, stale or to_verify.
8. Activation and task authorization remain separately governed.
```

No chained mutation is implied. Installation does not automatically enable. Enablement does not automatically activate for all projects. Update does not automatically authorize use.

## 8. MCP responsibility

The Pantheon MCP is the governance and validation interface for capability management.

It should ultimately be able to qualify or validate caller-provided candidates for:

```text
capability identity and type
source and provenance
installation-status consistency
native-state consistency
permission and effect class
dependency and conflict status
scope activation
human gate requirement
update admissibility
rollback requirement
refusal or revision reason
action receipt consistency
```

The MCP may return a decision or candidate validation result. It does not install, enable, execute, update or remove the capability.

The runtime inventory itself may come from Hermes or its adapter. Pantheon should not invent live state.

## 9. Hermes adapter responsibility

The Hermes adapter or Pantheon Modules plugin is the Policy Enforcement Point for native capability operations.

It may:

```text
read native capability inventory
map native objects to cockpit capability cards
call Pantheon preflight before a mutation
perform one admitted native action
return the native response and fresh state
refuse unsupported runtime versions or unknown object kinds
```

It must not:

```text
bypass Pantheon preflight for consequential actions
self-approve installation or activation
retain broad administrator secrets in Pantheon
invent compatibility across Hermes versions
silently translate unknown configuration structures
chain install -> enable -> activate without separate decisions
```

## 10. Version and configuration drift

Capability management must not rely on permanent assumptions about Hermes or OpenWebUI configuration files.

Each adapter declares:

```text
runtime product
supported version range
native API, CLI or plugin surface used
capability types supported
actions supported
readback method
rollback method
known migration requirements
```

After an update:

```text
observe exact runtime version
-> select a compatible adapter contract
-> refresh capability inventory
-> disable unsupported mutation actions
-> run native validation or migration checks where available
-> preserve read-only visibility when safe
```

Unknown version behavior:

```text
read-only inventory when safely supported
mutation disabled
status: adapter_compatibility_to_verify
no guessed YAML, JSON, environment or file patch
```

## 11. OpenWebUI placement

OpenWebUI remains primarily the conversational exposure surface.

It may display capability availability or route the user to the cockpit, but it should not become the canonical lifecycle manager when Hermes owns the capabilities.

```text
OpenWebUI exposes.
Hermes executes and owns native capability mechanisms.
Pantheon governs.
The human decides.
```

OpenWebUI-specific plugins or functions may still appear as capability cards, with OpenWebUI identified as their native host.

## 12. Permissions and scope

Every capability card must expose the consequence-bearing dimensions relevant to its type:

```text
read access
write access
external communication
browser or network access
filesystem access
secret use
memory effect
scheduling effect
model/provider effect
project and user scope
professional-use ceiling
```

A capability with broad or unknown effects remains inactive or blocked until reviewed.

## 13. Default posture

```text
catalog visibility                 -> allowed
read-only inventory                -> separately admitted probe
candidate creation                 -> allowed
native installation                -> human gate
native enable / disable            -> human gate
scope activation                   -> human gate
update                             -> separate authorization
removal                            -> destructive gate
automatic activation               -> forbidden
automatic update                   -> forbidden
cross-project activation inheritance -> forbidden
```

The preferred reversible action is `suspend` or `disable`, not uninstall.

## 14. Current implementation status

```text
implemented as documentation:
  capability taxonomy, lifecycle axes, action flow, boundary and version-drift rules.

partial external referent:
  the Pantheon Modules Hermes dashboard plugin already exposes a bounded subset
  of native inventory and separately confirmed Hermes administration actions.

implemented MCP support today:
  bounded read-only policy and candidate validation surfaces only; no general
  capability lifecycle mutation interface.

documented non-implemented:
  unified cockpit capability cards, authoring surfaces, full capability inventory,
  generic Capability Action Candidate contract and broader Hermes adapter mappings.

voluntarily absent:
  Pantheon-owned plugin manager, workflow runtime, agent host, MCP host, scheduler,
  queue, provider router, secret store and automatic approval engine.
```

## 15. Immediate design target

The first cockpit slice should not attempt every action. It should establish the shared capability card and support:

```text
inventory
inspect
status separation
scope display
enable / disable for one reviewed native type
probe
update available display
MCP-backed preflight
technical receipt
```

Recommended first native types:

```text
Hermes plugins
Hermes MCP bindings
Hermes skills when the native management surface is sufficiently stable
```

Workflow and runtime-agent authoring should reuse the same card and candidate model after their native contracts are clarified.
