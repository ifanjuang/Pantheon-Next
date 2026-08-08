# APU V0.2 adapter chokepoint convergence

Date: 2026-08-08

## Objective

Converge the active Architecture Project Understanding adapter contract with the frozen Project Anatomy V0.2 model after the executable MVP owner migration and Revit observation-seam stabilization.

## Repo state checked

- Project Anatomy V0.2 core schemas and V0.1 compatibility are merged.
- `PROJECT_ANATOMY_MODEL.md` is the active conceptual model.
- pantheon-mvp H4c executable owner migration is merged.
- Revit V0.2 observation contract is merged.
- the existing `PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md` still exposed V0.1 carriers (`stable_object.matches`, `object_identity`, `spatial_node`, `object_relation`, `human_override`).
- draft PR #579 also edits that adapter contract, but is based 19 commits behind current `main` and is not mergeable; its OpenTakeoff-specific work must be re-ported after this generic chokepoint is stabilized.

## Decision

Reuse the existing generic bridge seam instead of creating a parallel execution-result authority.

```text
Task Contract + bounded context
-> external APU adapter
-> Observation Bundle Candidate
 + Evidence Pack Candidate
```

`Observation Bundle Candidate` is the APU specialization of the generic bridge `result_candidate` slot. It is not the provisioning-specific `ExecutionResultCandidate` schema and it is not Project Anatomy persistence.

## V0.2 output posture

Adapters may propose:

- `source_representation` records;
- `attribute_claim` candidates;
- `relation_claim` candidates;
- coverage and delta information;
- gaps, withheld items and warnings;
- method / binding / operation provenance.

Adapters do not create durable `stable_object` identity automatically.

Identity alignment is only a candidate relation from a source representation to an already-known stable object supplied by governed context:

```text
source_representation
-- identity.represents -->
stable_object
```

Unresolved observations remain attached to their source representation.

## Removed active V0.1 output carriers

The adapter chokepoint no longer presents these as canonical outputs:

```text
stable_object.matches
object_identity
spatial_node
object_relation
instance_override
phase_state
human_override
```

Their historical/compatibility role is not erased.

## Boundaries preserved

```text
Observation Bundle Candidate != APU mutation
Observation Bundle Candidate != Evidence Pack
candidate match != identity accepted
not found != absent
missing source occurrence != project object deleted
runtime success != Evidence
proof_status != Proof object
required != observed
```

## Not implemented by this change

- executable Observation Bundle schema;
- adapter ingestion API;
- Hermes workflow;
- Revit/IFC/PDF/image runtime adapter;
- stable-object creation flow;
- Evidence admission or Proof;
- Cockpit projection.

Those remain separate reviewed slices.
