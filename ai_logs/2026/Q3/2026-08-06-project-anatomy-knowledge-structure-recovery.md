# AI intervention trace — Project Anatomy knowledge-structure recovery

Status: completed documentation trace — no implementation, schema change or activation.
Date: 2026-08-06.

## Objective

Compare the Project Anatomy convergence note with the earlier design discussions
and record useful material that was not explicit enough in the first draft.

## Repository state checked

```text
PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
PROJECT_OBJECT_MODEL.md
PROJECT_UNDERSTANDING.md
PROGRAM_AND_CONFORMANCE.md
PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
REVIT_LOCAL_ADAPTER.md
ARCHITECTURAL_PROJECT_GRAPH.md
WHAT_RUNS.md
```

The existing owners already covered object identity, beliefs, provenance,
requirements, typed relations, certainty, adapter boundaries and runtime status.
No new authority or ontology was required.

## Recovered discussion outcomes

The first consolidation under-specified:

```text
multi-view spatial reconstruction from plans, sections, details, photos, IFC and Revit;
knowledge strata separating identity, representations, properties, requirements,
observations, derivations, doubts and decisions;
architecture-led first wave including economy, site/DET, thermal/RE2020 and ACV/carbon;
rich Revit Context Pack requirements;
technical assemblies and interfaces as preserved later extensions;
practical candidate output families: Spatial, Element, Requirement, Observation,
Contradiction and Missing Information.
```

## Change

Added:

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_KNOWLEDGE_STRUCTURE.md
```

The annex remains subordinate to the current owners and to
`PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md`.

## Boundaries retained

```text
multi-view hypothesis != complete automatic 3D reconstruction
representation != stable object
IFC/Revit id != Pantheon stable identity
quantity candidate != accepted DPGF quantity
thermal/carbon input != validated regulatory conclusion
site observation != as-built canonization
candidate-family label != new persistence owner
```

No schema, migration, API, Cockpit code, Hermes configuration, adapter runtime,
ProjectClaim implementation, variant implementation, Evidence admission, APU write
or external action was added.
