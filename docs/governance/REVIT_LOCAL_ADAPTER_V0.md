# Revit Local Adapter V0

Status: candidate support doctrine — Revit local adapter boundary — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines the V0 boundary for a future local Revit adapter. It creates no Revit add-in, no C# project, no Revit API dependency, no Hermes skill, no OpenWebUI action, no transaction runner, no scheduler, no queue, no provider router, no plugin manager, no installer, no updater, no approval engine and no memory or Registre Probatoire promotion.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
Revit executes locally.
The human decides.
```

## Purpose

The Revit local adapter exists to make professional model work governable without moving Revit execution into Pantheon.

V0 frames:

```text
local model observation
context-pack preparation
action-candidate preparation
preflight classification
named Revit transaction discipline
blocked-action handling
candidate logs and evidence posture
human decision gates
```

It does not define a working plugin implementation. The C#/.NET add-in belongs in a separate sibling repository unless a future explicit arbitration changes the code-hosting boundary.

## Repository state

```text
implemented in Pantheon Next:
  this documentation only.

documented non-implemented:
  Revit Gate / Revit Local Adapter V0 boundary.

not implemented in Pantheon Next:
  Revit add-in, C# project, Revit API package, command bindings,
  UI ribbon, local IPC, transaction runner, installer, updater,
  deployment package or runtime telemetry service.

future external implementation:
  sibling repository / local Revit add-in, to verify before use.
```

## Capability slot

```yaml
capability_id: revit_local_adapter
function: local Revit model inspection, context packs, candidate actions, controlled local transactions and action logs
preferred_binding: Pantheon Revit Gate local plugin
owner_layer: Revit local plugin / Hermes local side
exposed_by: OpenWebUI cockpit or project surface
executed_by: Revit local plugin under explicit local user session, optionally orchestrated by Hermes
observed_by: Revit local plugin and returned action logs
governed_by: Pantheon Next
approved_by: human decision gate for consequential effects
binding_status: candidate
install_status: absent / not_implemented
health_status: unknown
activation_status: unavailable
allowed_outputs:
  - Visual Context Pack Candidate
  - Model Observation Candidate
  - Method Candidate
  - Preflight Report Candidate
  - Review Action Candidate
  - Action Log Candidate
  - Evidence Pack Candidate
  - Capability Gap
forbidden_outputs:
  - professional validation
  - automatic save
  - automatic sync
  - purge
  - delete
  - linked-model write
  - arbitrary generated-code execution
  - silent background write
  - approval
  - Registre Probatoire admission
risk_surfaces:
  - live model mutation
  - phases and design options
  - worksharing
  - linked models
  - pinned, grouped or constrained elements
  - families and types
  - levels, grids and hosts
  - production files
```

## Layer split

### What Pantheon governs

Pantheon governs:

```text
Task Contract legitimacy
scope and effect classification
approval ceiling
allowed and forbidden actions
evidence expectations
preflight status vocabulary
risk level
candidate status
register and memory boundaries
activation and adoption status
rollback visibility
```

Pantheon does not execute Revit commands.

### What Hermes executes

Hermes may, if a future adapter exists and the Task Contract allows it:

```text
prepare a governed execution handoff
ask Revit for local observations
request preflight classification
propose method candidates
sequence independent actions
hold dependent actions while blocked
resume blocked actions after user/local validation
return result candidates and action-log candidates
```

Hermes must not treat technical possibility as authorization.

### What Revit executes locally

The Revit plugin is the only layer that may touch the live model.

It may, once implemented and explicitly enabled:

```text
observe the current document
read selected elements and model context
run preflight checks
prepare previews
open named transactions for approved local mutations
journal changed element ids and observed effects
return local action logs
```

It must execute inside the controlled Revit context, not through silent background writes.

### What OpenWebUI exposes

OpenWebUI may expose:

```text
capability card
connection and health status
current Task Contract summary
context-pack preview
preflight report
blocked action state
action preview
human decision gate
result candidate
action log candidate
risk warning
```

OpenWebUI display is not execution, proof, approval, memory admission, save authority or sync authority.

### What the human validates

Human validation is required for:

```text
activating the adapter
running on a real project file
changing the task perimeter
allowing any write transaction
accepting a candidate result
accepting an Evidence Pack Candidate as evidence
saving, syncing, publishing or transmitting any output
promoting anything to the Registre Probatoire
using generated code or macros
moving from W2 to W3 or above
```

## Warning levels

The adapter uses simple warning levels. These are Revit operational levels, not Pantheon approval levels.

### W0 — read / observation

```text
read model metadata
read active document status
read selected element ids and categories
read visible view context
collect warnings
prepare screenshots or visual context packs
prepare a model observation candidate
```

Default posture: admissible only when the Task Contract allows local observation and no model mutation occurs.

### W1 — proposal / preview

```text
method candidate
action preview
selection set proposal
family/type requirement report
transaction plan candidate
rollback note candidate
```

Default posture: no transaction, no write. Output remains candidate.

### W2 — light reversible write

```text
small local draft annotation
temporary view or non-production working artifact
clearly reversible parameter or marker when explicitly authorized
```

Default posture: blocked in V0 implementation until a sandbox rule, named transaction rule and human approval gate are implemented and reviewed.

### W3 — model modification with dependencies

```text
create, move or modify model elements
load or swap families
change types
modify rooms, areas, tags, dimensions or sheets when dependencies matter
```

Default posture: blocked until a later reviewed implementation level.

### W4 — destructive or difficult to reverse

```text
delete
purge
bulk write
save
sync
publish
relinquish ownership automatically
modify linked models
modify production-wide standards
```

Default posture: refused for V0.

### W5 — generated code or uncontrolled execution

```text
run generated code
run macros
run arbitrary Python/C#/Dynamo scripts
install plugins
modify add-in manifests
execute unreviewed external commands
```

Default posture: refused for V0. Future use requires a separate explicit decision path.

## Task and action lifecycle

A user request becomes a governed task. A task contains actions.

An action may be:

```text
independent
dependent
blocked
pending_user
failed
retryable
fallback_available
finalized
refused
```

A blocked action must not automatically block the whole task. Example: if an annotation family is missing, Hermes may ask the user to load or approve the family, keep that action blocked, continue independent read-only or preview actions, then resume only after local validation.

The adapter must preserve:

```text
what was requested
what is in progress
what is blocked
what failed
why it failed
which fallback exists
what was validated
what was finalized
what must not be repeated
```

## Preflight requirements

Before any Revit write action, the local plugin should return a preflight report candidate covering at least:

```text
document identity and title
central/local/worksharing status
active view and view type
selection scope
target element ids and categories
linked-model involvement
phase and design-option context
level, grid, host and constraint dependencies
pinned/grouped/workset ownership status
family/type availability
transaction name candidate
warning level W0-W5
approval reference
rollback or manual reversal note
expected changed element classes
forbidden-effect check
```

If the preflight cannot classify scope, target, effect, approval or rollback posture, the correct output is a visible Capability Gap, not an improvised transaction.

## Transaction rule

Every Revit mutation must pass through a controlled local Revit context with a named transaction.

Required transaction naming pattern:

```text
PantheonGate:<task_id>:<action_id>:<short_effect>
```

The plugin must journal:

```text
transaction name
warning level
approval reference
started_at / finished_at
changed element ids when available
created element ids when available
warnings observed
rollback status or manual reversal note
result status
```

A successful Revit transaction is not governance approval, professional validation, proof, evidence admission, save authority or sync authority.

## Evidence posture

The real Revit model observed by the local plugin is the priority source for model state.

However:

```text
observed != validated
transaction_success != approval
model_warning_absent != safe
screenshot != proof
action_log != Evidence Pack
Evidence Pack Candidate != validated evidence
```

A Revit action log may support an Evidence Pack Candidate. It does not replace professional review.

## V0 implementation floor

The first external implementation should be narrow:

```text
1. C#/.NET add-in shell outside Pantheon Next.
2. W0 read-only document and selection observation.
3. W0 visual context pack candidate.
4. W1 preview/action-plan candidate without transaction.
5. Preflight report candidate.
6. Action log candidate.
7. No W2 transaction until sandbox approval and tests exist.
8. No W3/W4/W5 behavior.
```

## Adoption gates

Before adoption or activation, all of these must be reviewed:

```text
code-hosting repository identified
Revit version and API target declared
C#/.NET project structure reviewed
local install posture declared
no silent startup mutation
no automatic save/sync/delete/purge
transaction naming implemented
preflight object implemented
W0/W1 tests or manual verification fixtures exist
W2+ refusal behavior proven
logs redact sensitive file paths where needed
human approval gate visible before mutation
rollback/manual reversal posture documented
```

## Final rule

```text
Pantheon may govern the Revit adapter.
Hermes may orchestrate bounded work.
Revit executes locally.
OpenWebUI exposes the review surface.
The human decides consequential effects.
V0 does not write silently.
```
