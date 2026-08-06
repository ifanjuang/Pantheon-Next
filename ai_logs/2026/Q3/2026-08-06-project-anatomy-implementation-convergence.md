# Project Anatomy implementation convergence — 2026-08-06

Status: completed documentation trace — no implementation or activation.

## Objective

Consolidate the current Architecture Project Understanding material into one
bounded implementation trajectory for Project Anatomy, while leaving tranche F,
tranche G and the Revit binding to their separate owners.

## Repository state checked

### Pantheon-Next

Reviewed current owner surfaces and status material:

```text
docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md
docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
docs/governance/FRAGMENT_QUALIFICATION_CANDIDATE.md
docs/governance/REVIT_LOCAL_ADAPTER.md
docs/governance/ARCHITECTURAL_PROJECT_GRAPH.md
docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md
docs/governance/WHAT_RUNS.md
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
schemas/architecture-project-understanding/
```

Issue #169 and its closure record were checked. Shared definitions, E0-E4
certainty, zone typing, cross-file referential integrity and duplicate-id refusal
are present. Issue closure did not promote Project Understanding into an
executable project authority.

### pantheon-mvp

Reviewed merged implementation coverage for:

```text
Document Structure projection and read API
Hermes fragment-qualification skill
Execution Result persistence
fragment qualification -> APU mapping conversion
mapping review events
write-command preparation
write authorization events
```

The current path prepares and authorizes `add_match_to_existing_object`. It does
not yet apply that command, establish the complete executable APU owner or expose
Project Anatomy in Cockpit.

## Convergence decision

No fourth APU authority is created.

The implementation trajectory is carried by:

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
```

A condensed subordinate annex preserves only the discussion requirements that
were not explicit enough in the owner documents:

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_KNOWLEDGE_STRUCTURE.md
```

It retains the current owner split:

```text
PROJECT_OBJECT_MODEL
-> project-world objects and domain relations.

PROJECT_UNDERSTANDING
-> belief, provenance, APU derivation, doubt, contradiction and canonization.

PROJECT_UNDERSTANDING_ADAPTER_CONTRACT
-> external candidate-only adapter seam.

ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN
-> Project Anatomy product placement.

REVIT_LOCAL_ADAPTER
-> local Revit binding, context, preflight and transaction boundary.
```

## Main decisions

```text
APU
= internal project-object and domain-relation authority.

Project Anatomy
= server-calculated user projection of APU coverage, provenance and uncertainty.
```

The first executable write remains the existing bounded operation:

```text
add_match_to_existing_object
```

Automatic stable-object creation is not admitted by this note. It requires a
separate demonstrated need and reviewed contract.

APU domain relations remain distinct from the four Information relation meanings.
`EntityRef` may provide cross-family references without becoming a universal
semantic relation vocabulary.

The first useful Cockpit slice is read-only and does not require full 3D. It must
expose structure, domain relations, phase state, provenance coverage, uncertainty,
contradictions and unmapped material from server-owned identities.

## Coordinated boundary with Revit

Project Anatomy owns the professional multi-source understanding and first-wave
viewpoints:

```text
architecture and spatial design
project economy and quantities
construction-site review and DET support
thermal-data preparation and RE2020 consistency
life-cycle assessment and carbon analysis
```

`REVIT_LOCAL_ADAPTER.md` owns only the replaceable Revit binding: transport,
manifest, Context Snapshot, freshness, preflight, authorization correlation,
transaction discipline and Action Report.

```text
Project Anatomy != Revit model
Revit Context Snapshot != Project Anatomy
APU mapping applied != Revit model modified
```

The condensed annex references the Revit owner instead of repeating its detailed
Context Pack.

## F and G boundary

```text
H may consume final reviewed F/G owners.
H does not define or modify them.
```

ProjectClaim remains a governed knowledge unit, not a universal reasoning unit.
This convergence introduces no generic `Derivation` object or `Consequence`
attribute. Work and decisions continue to use WorkIssue and DecisionRequest.

Variant selection and evolution remain in G. H preserves source phase and variant
provenance and must not collapse competing variants into one object state.

## Implementation sequence recorded

```text
H0 current-state and owner inventory
H1 executable project-scoped read owner
H2 apply authorized add_match_to_existing_object
H3 governed cross-family links
H4 Project Anatomy API and Cockpit projection
H5 progressive adapter and real-project validation
```

The first vertical proof is one Project, one existing reviewed stable object, one
Document Structure fragment, one reviewed mapping, one authorized match
application and one read-only Anatomy projection.

## Non-effects

```text
no schema change
no PostgreSQL migration
no API
no Cockpit code
no APU write application
no object creation
no Revit add-in
no Hermes configuration
no runtime launch
no ProjectClaim implementation
no variant implementation
no Evidence admission
no canonization
no memory promotion
no task authorization
```

## Completion assessment

Documentation convergence and Project Anatomy/Revit responsibility split:
complete for this PR.

Project Anatomy implementation: not started by this change.

The next legitimate H action is the H0 inventory after the reviewed F/G owners
required by the first slice are available and parallel file-path work is
reconciled.
