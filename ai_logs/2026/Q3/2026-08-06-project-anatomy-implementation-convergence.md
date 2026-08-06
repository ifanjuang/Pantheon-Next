# Project Anatomy implementation convergence — 2026-08-06

Status: completed documentation trace — no implementation or activation.

## Objective

Consolidate the current Architecture Project Understanding material into one
bounded implementation trajectory for Project Anatomy, while leaving tranche F
and tranche G to their separate workstreams.

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

Issue #169 and its closure record were checked. The earlier schema debt is
resolved: shared definitions, E0-E4 certainty, zone typing, cross-file
referential integrity and duplicate-id refusal are present. Issue closure did not
promote Project Understanding into an executable project authority.

### pantheon-mvp

Reviewed recent merged implementation coverage for:

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

### Parallel work

Open F-to-J trajectory and relation-review work was checked. This consolidation
uses a separate file path and does not modify tranche F or tranche G files.

## Convergence decision

No fourth APU authority document is created.

The new note is a subordinate implementation convergence surface:

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
```

It retains the current owner split:

```text
PROJECT_OBJECT_MODEL
-> project-world objects and domain relations.

PROJECT_UNDERSTANDING
-> belief, provenance, doubt, contradiction, override and canonization.

PROJECT_UNDERSTANDING_ADAPTER_CONTRACT
-> external adapter seam.

ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN
-> Project Anatomy product placement.

REVIT_LOCAL_ADAPTER
-> local Revit execution boundary.
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

## Discussion-recovery annex

A comparison with the earlier product discussions showed that the first note did
not state several outcomes explicitly enough. They are now captured in:

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_KNOWLEDGE_STRUCTURE.md
ai_logs/2026/Q3/2026-08-06-project-anatomy-knowledge-structure-recovery.md
```

The recovered material covers:

```text
multi-view spatial understanding from plans, sections, details, photos, IFC and Revit;
knowledge strata separating identity, representations, properties, requirements,
observations, derivations, doubts and decisions;
architecture-led first wave including economy, site/DET, thermal/RE2020 and ACV/carbon;
rich Revit Context Pack requirements;
technical assemblies and interfaces retained as later extensions;
Spatial, Element, Requirement, Observation, Contradiction and Missing Information
candidate-routing categories.
```

The annex is subordinate to the same owners. It adds no schema, object, relation
vocabulary or persistence authority.

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

## F and G boundary

```text
H may consume final reviewed F/G owners.
H does not define or modify them.
```

ProjectClaim value authority remains in F. Variant selection and evolution remain
in G. H preserves source phase and variant provenance and must not collapse
competing variants into one object state.

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

Documentation consolidation and discussion recovery: complete.

Project Anatomy implementation: not started by this change.

The next legitimate H action is the H0 inventory after the final reviewed F/G
owners required by the first slice are available and parallel file-path work is
reconciled.
