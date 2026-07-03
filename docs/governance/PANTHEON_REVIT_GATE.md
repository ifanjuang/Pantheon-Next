# Pantheon Revit Gate — local architecture plugin framing

Status: candidate support doctrine — Pantheon Revit Gate framing. Repository state: documented non-implemented.

This dossier frames a **local Revit architecture plugin** governed by Pantheon. The plugin is runtime and lives outside Pantheon, on the architect's machine and/or Hermes local side. Pantheon governs the vocabulary of capability status, evidence, traceability, approval posture and later regulation. Nothing here is implemented.

It implements no plugin, no Revit add-in, no MCP server, no schema, no test, no Docker and no operations change. It does not claim the plugin exists.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Current arbitration — V0 Free Exploration Mode

Decision status: accepted as a **sandbox / exploration orientation**, not as production policy.

```text
V0 Revit Plugin = free exploration mode.
Architecture only.
Offline local first.
Hermes may act through the plugin.
No heavy governance in V0.
Minimal traces are mandatory from the beginning.
Regulation comes later from observed use.
```

This updates the earlier read-only MVP posture without promoting any implementation. The conservative read-first model remains the safe production direction. The V0 exploration posture exists to learn which architectural actions are useful before freezing a strict control matrix.

The decision does **not** mean:

- the plugin exists;
- the repository implements a runtime;
- Pantheon executes Revit actions;
- Revit model changes are professionally validated by Hermes;
- deletion, save, sync or arbitrary code execution are safe.

It means:

- the first runnable plugin may be permissive in a sandbox;
- the interface should expose a broad architecture capability catalogue;
- actions may be tried freely on test copies;
- traces must be captured so the later governed version can be based on real usage rather than speculation.

## Purpose

The purpose is to design a local Revit plugin that lets an architect converse with the open model through Hermes and, eventually, execute architectural operations from controlled natural-language or graphical intents.

V0 is not a compliance gate. It is a learning instrument:

```text
free enough to discover useful workflows;
traced enough to regulate later;
local enough to respect the offline requirement;
explicit enough to avoid mistaking runtime success for professional validation.
```

## Placement

The plugin is an adapter/runtime surface, not Pantheon doctrine.

```text
OpenWebUI / dashboard exposes.
Hermes prepares, orchestrates and calls.
The Revit plugin executes locally inside Revit.
Pantheon records the capability grammar and later governance posture.
The human remains responsible for project decisions.
```

Pantheon owns only the documented classification of capability effects and the later rules for promotion, evidence, memory, scope and approval. Installation, local relay, MCP, Revit API calls, queues, async workers, transactions and logs are runtime concerns outside the Pantheon repository.

## Scope

V0 is **architecture only**.

In scope:

```text
project / document context
views, sheets, schedules
walls, floors, ceilings, roofs
rooms, areas and surfaces
doors, windows and openings
curtain walls and façade composition
stairs and railings, when architectural
families and types used for architecture
materials and finishes
parameters
annotations, detail lines, dimensions
local exports and view snapshots
visual context packs
sketch / detail-line interpretation
```

Out of scope for V0:

```text
MEP
HVAC
structure
loads / sizing / calculations
networked cloud automation
APS as required dependency
linked-model write control
central/workshared production automation
```

## V0 non-negotiable traces

Free exploration does not mean invisible execution. Even in permissive sandbox mode, every consequential Revit action should produce a minimal trace.

Required from the first writable prototype:

```text
1. Display the active RVT document name before action.
2. Use a named Revit transaction for every committed write.
3. Write a local action log.
4. List created, modified and deleted ElementIds where possible.
5. Keep a stop / disable-Hermes control visible in the plugin.
```

Preferred when feasible, but not mandatory for the earliest sandbox spike:

```text
preview or dry-run
before/after snapshot
affected-elements table
failure packet
rollback note
local evidence pack candidate
```

## Free Exploration profiles

The interface should expose profiles, but V0 may default to the permissive one.

| Profile | Intended use | Posture |
|---|---|---|
| `Sandbox libre` | Test file, local copy, disposable model | broad freedom, logs mandatory |
| `Projet agence` | Real project copy or low-risk work session | broad freedom, confirmation light, logs mandatory |
| `Client / production` | Engaging model | regulated later, not V0 default |
| `Locked client model` | Sensitive or contractual model | read / inspect only |

The V0 accepted profile is `Sandbox libre`. The other profiles are placeholders for later regulation.

## Capability registry posture

The plugin settings should expose a **Capability Registry** rather than hiding powerful functions.

Each capability row should carry at least:

```text
tool_id
label
domain
operation_family
read_create_modify_model_modify_delete_export
architecture_only flag
default_profile availability
risk note
requires_log
requires_named_transaction
requires_preview when known
disabled_reason when blocked
```

The registry is allowed to be permissive in V0, but it must already be structured enough to support future regulation.

## Target capability families

V0 exploration may list the full architecture surface, even if only part of it is initially implemented.

```text
Read / inspect
Create
Modify
Model
Parameterize
Annotate
Dimension
Views / sheets
Schedules
Materials / finishes
Families / types
Sketch / detail-line interpretation
Visual context pack
Export
Log / action report
```

Example capability groups:

- read document, active view, selection, visible elements, parameters and families;
- capture active view image and visual context pack;
- create walls, floors, ceilings, roofs, rooms, doors, windows, curtain walls, railings and architectural components;
- modify element position, type, level, phase, geometry and façade composition;
- write parameters on selection or filtered sets;
- create annotations, detail lines, filled regions, tags and dimensions;
- create or modify views, sheets, schedules, filters and graphic overrides;
- interpret selected detail lines as profiles, façade guides or modeling references;
- interpret an imported sketch as a composition candidate;
- export local images, CSV, JSON, PDF or IFC candidates;
- generate logs, action reports, before/after summaries and failure packets.

## Visual context pack

Hermes should not rely only on text commands. The plugin should let the user send the active Revit context to Hermes.

A visual context pack may include:

```text
active view snapshot
view id and name
view type, scale and level
selected element ids
visible element ids
rooms / walls / doors / windows visible in the view
key parameters
user-drawn detail lines or model lines
optional cropped region
```

This is the preferred way to support commands such as:

```text
look at this façade
use these lines as the top profile of the wall
create a curtain wall composition from this sketch
place a door aligned to the selected reference door
remove or demolish the window nearest to the tree
```

Image-only interpretation is always weaker than image + Revit data. A sketch or screenshot may generate a method candidate, not a professional truth.

## Method-first modeling

For spatial or graphical commands, Hermes must propose a modeling method before the plugin applies a transaction in any regulated profile. In sandbox V0 this may be reduced to a light confirmation, but the method should still be recorded in the log.

Examples:

```text
intent: cut the top of walls along selected detail lines
possible_methods:
  - edit wall profile
  - void cut
  - attach wall to host
  - create graphic-only representation
  - create reference mass
```

```text
intent: compose curtain wall from sketch
possible_methods:
  - Revit curtain wall with grid and mullions
  - independent window/panel families
  - 2D façade drafting only
```

The method is part of the trace because the method changes quantities, model semantics, documentation and future edits.

## Async posture

Async is allowed for analysis and preparation, not for uncontrolled model mutation.

Allowed async work:

```text
context extraction from a snapshot
Hermes analysis
sketch interpretation
candidate generation
preview table preparation
report generation
local export preparation
```

Committed Revit model changes still occur through the plugin in the Revit context, using a named transaction. If the model changed between candidate generation and execution, the action should be marked stale when the plugin can detect it.

## MCP / API binding

MCP is optional. The safer development sequence is:

```text
Phase 1: local plugin API / local relay for debugging
Phase 2: MCP wrapper around the same capability registry
Phase 3: stricter governed handoff once real use is understood
```

MCP must not become the authority layer. It is a transport / adapter. The same action should carry the same capability id and trace whether it arrives through local API, MCP or another local bridge.

## Free exploration versus production regulation

The current working distinction:

| Mode | Purpose | Governance posture |
|---|---|---|
| Free exploration | learn uses, prototype broad actions | permissive, trace mandatory |
| Guided agency use | useful project work, still local | confirmation light, preview when feasible |
| Regulated production | model-changing consequential work | preview, affected elements, approval, report |
| Locked / sensitive | client-sensitive or contractual file | read-only / inspect |

The later Pantheon-regulated version should be built from logs and observed failures, not from a premature theoretical matrix.

## Boundary

- No plugin, add-in, MCP server, runtime, schema, test, Docker or operations change is added.
- V0 Free Exploration Mode is a documented orientation, not an implementation.
- The Revit plugin executes locally outside Pantheon.
- Hermes may orchestrate and call the plugin.
- Pantheon remains the governance vocabulary and later status/approval layer.
- The human decides whether the resulting workflow is acceptable in practice.

## Governance references

- docs/governance/STATUS.md
- docs/governance/CAPABILITY_PLACEMENT.md
- docs/governance/MODULAR_DOMAIN_REORIENTATION.md
- docs/governance/DOMAIN_PACK_SPEC.md
- docs/governance/PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md
- docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
- docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
