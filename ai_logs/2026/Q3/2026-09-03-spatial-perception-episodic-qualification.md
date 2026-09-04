# Spatial perception + episodic memory qualification

Date: 2026-09-03
Status: qualification-only implementation candidate — review pending.
Boundary profile: guidance / validation-only.

## Objective

Turn issue #949 into a bounded executable qualification contract without adding a
new semantic owner, memory product, vision runtime or spatial truth store.

The motivating technical/theoretical proposition is:

```text
dense perception
+ free episodic/associative memory
+ structured Project Anatomy semantics
+ bounded working context
```

can provide richer architectural-project understanding than forcing every useful
observation into one structured graph.

This qualification does not assert that the proposition is already proven. It
only makes the distinctions and future experiment machine-checkable enough to
review without prematurely adopting a runtime.

## Repository state checked

Exact base before this branch:

```text
Pantheon-Next/main = d3f0fab72f64714010e30abc3e03c001b441eb1b
```

That base already includes merged #951:

```text
docs(memory): preserve free episodic memory beside structured project knowledge
```

Therefore this branch does not modify `MEMORY.md` and does not restate a second
memory doctrine.

Existing owners checked:

- `docs/governance/MEMORY.md` — runtime memory / Registre Probatoire boundary;
- `docs/domain-packs/architecture/PROJECT_ANATOMY_MODEL.md` — four project-world
  primitives, source-local representations, unresolved identity, raw-vs-retained
  boundary and Observation Bundle seam;
- `schemas/architecture-project-understanding/observation_bundle.schema.yaml`;
- H5.3 document/PDF/photo qualification corpus and M4 private-drawing bridge;
- issue #949 — owner of the bounded spatial/episodic experiment.

No open PR was found implementing #949's spatial-perception qualification.

## Convergence decision

Do not add:

```text
SpatialGraph
EpisodicMemory Pantheon object
SpatialMemory database
vision-specific Project Anatomy primitive
second scene graph
second Project Anatomy
```

Instead keep the existing owner topology and qualify four distinct cognitive
layers with governance orthogonal to them.

## Four-layer model

### 1. Perception — dense, source-linked, recalculable

Perception outputs are technical derivatives of a source, not durable semantic
truth merely because a model produced them.

Candidate replaceable stages include:

```text
segmentation
object detection
monocular depth
surface normals
camera pose / feature tracks
multi-view geometry
point map / point cloud / mesh when useful
```

Examples of replaceable model families may include SAM-like segmentation,
YOLO-like detection, Depth-Anything-like monocular depth and any suitable normal
or multi-view estimator. Mentioning a family does not adopt it.

The important owner rule is about the output, not the vendor:

```text
mask
bbox / region
class score
depth field
normal field
camera transform
track cluster
reconstruction
```

remain derived representations until deliberately distilled.

### 2. Episodic / associative runtime memory — free payload, small envelope

The runtime may preserve singular, unusual, ambiguous or narrative project
material without forcing it into a semantic taxonomy first.

Example:

```text
"The wall appears slightly irregular near the opening.
Compare with the previous visit before treating it as a defect."
```

This may remain useful even when no stable object or professional conclusion is
known.

Preferred principle already adopted by #951:

```text
free payload
+ minimal routing envelope when honestly available
```

The qualification envelope uses only concepts such as:

```text
episode identity
scope
time when useful
free content
refs when known
runtime/provider provenance
```

No Pantheon schema is introduced for these episodes.

### 3. Structured semantics — existing governed owners only

Project Anatomy remains the owner for machine-addressable project-world
semantics:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

Requirements remain separate, and Knowledge / Work / Evidence / Decision retain
their existing owners.

Only selected observations that actually benefit from structure should cross the
existing Observation Bundle seam.

### 4. Working context — temporary composition

Hermes or another admitted runtime should receive the smallest useful slice for
one question or task:

```text
structured project facts
+ exact source regions
+ selected episodic observations
+ selected spatial derivatives
```

A Context Pack is neither memory authority nor persistence.

## Why this is technically useful

### Segmentation answers region membership, not identity

Segmentation can isolate an opening, wall region, crack-like area or object
silhouette. It improves localization and allows downstream operations to reason
about one region instead of the whole image.

But:

```text
same-looking mask across photos
!= same physical object admitted
```

### Detection answers probable class/localization, not Project Anatomy object

A detector may say "window" with a confidence score and locate it in the image.
This can guide retrieval and association, but a detector class is a model output,
not stable project identity or professional classification.

### Depth contributes 2.5D structure before it contributes metric geometry

Monocular depth can often provide useful ordering and local shape cues even when
metric scale is unresolved.

That means it can help answer:

```text
which visible surface is nearer?
what regions share a similar depth layer?
is this apparent object in front of that surface?
```

without justifying:

```text
exact project XYZ
exact professional distance
surveyed deformation
```

Metric depth requires the specific model/mode plus calibration/scale evidence
appropriate to the intended use.

### Surface normals contribute orientation cues, not measured orientation

Normal estimation can help distinguish approximately vertical/horizontal planes,
local changes of orientation and likely geometric boundaries.

A predicted normal still remains model-derived. It is not a surveyed wall tilt or
a professionally measured deformation.

### Multi-view geometry is the stronger spatial step

Several overlapping photos can contribute:

```text
camera poses
feature tracks
cross-view associations
local point maps / reconstruction
```

This may transform isolated 2.5D observations into a more coherent local 3D
representation.

However:

```text
multi-view consistency
!= Pantheon identity accepted
```

A persistent track can be a strong matching signal while remaining only a
candidate relation to a stable project object.

## Coordinate-frame discipline

The qualification fixes this conceptual ladder:

```text
PIXEL
-> CAMERA
-> LOCAL_RECONSTRUCTION
-> PROJECT
```

Each transition changes what coordinates mean.

Rules:

```text
pixel bbox != camera-space geometry
camera-space depth != project coordinate
local reconstruction XYZ != project XYZ
PROJECT coordinates require explicit alignment/calibration provenance
```

A transform or alignment proposal remains a candidate until the relevant owner
admits it.

This protects against one of the most dangerous spatial-AI errors: numbers that
look metric and precise while belonging to the wrong or unknown frame.

## Dense representations versus semantic retention

The core scaling rule is:

```text
dense perception stays dense and derived
semantic Project Anatomy stays selective and addressable
```

Do not create:

```text
one attribute_claim per depth pixel
one claim per normal sample
one stable object per mask
one semantic relation per feature track
one canonical object per point-cloud cluster
```

The derived artifact may be large; the retained semantic observation should stay
small enough to justify its project meaning.

## Theoretical rationale

The architecture is deliberately analogous to a complementary-memory strategy,
without claiming that Pantheon implements a biological memory model.

A fast episodic side is good at preserving:

```text
specific events
exceptions
ambiguity
context
unusual detail
narrative
```

A structured semantic side is good at preserving:

```text
stable identity
comparable properties
explicit relations
machine-actionable project state
```

If every episode is normalized immediately, Pantheon risks losing the very
singularity that later explains a project decision or anomaly.

If nothing is ever structured, Pantheon loses comparison, computation,
traceability and governed reuse.

The intended balance is therefore:

```text
preserve first when ambiguity matters
structure selectively when a stable/useful semantic carrier is justified
```

This is a stability/plasticity design principle, not a new authority model.

## Structured/free asymmetry

The direction of retrieval and the direction of authority are intentionally not
symmetrical.

```text
Project Anatomy / Knowledge
-> bounded runtime context / episodic retrieval
= composition allowed

runtime episode / perception output
-> Project Anatomy / Knowledge / Requirement / Register
= proposal only
= existing owner validates and applies
```

Short form:

```text
retrieval may be bidirectional
promotion remains governed and one-way
```

A memory association does not become `relation_claim` merely because it is
repeated, high-confidence or supported by multiple views.

## Qualification fixture

The branch adds one non-canonical fixture under `tests/fixtures/`.

It exercises:

1. **free observation, no stable identity**
   - an apparent wall irregularity remains free text;
   - it references exact source/derived regions;
   - no stable object is required.

2. **cross-episode association**
   - three photos may be grouped as the same-feature candidate;
   - the association remains runtime memory;
   - no `identity.represents` is admitted.

3. **structured context enriches recall**
   - an existing Project Anatomy object is allowed as retrieval context;
   - related free episodes may be recalled;
   - recall does not promote them.

4. **ambiguity survives**
   - one photo feature may point to two candidate project objects;
   - no silent winner is selected.

5. **one selected promotion**
   - one useful episodic observation is distilled into the existing canonical
     Observation Bundle candidate;
   - the claim targets a `source_representation`, not a fabricated stable object;
   - identity and professional measurement remain explicitly unresolved/withheld.

## Retrieval comparison

The fixture frames one qualitative question:

> What do we know around this opening, including structured project facts,
> photos, unusual observations and unresolved hypotheses?

It compares:

```text
structured-only context
vs
structured + episodic + spatial-derived context
```

The branch deliberately claims no benchmark superiority. The first qualification
question is whether the richer composition retrieves useful project context that
structured semantics alone would intentionally not retain.

A later executed slice under #949 must use real/synthetic non-sensitive images
and record exact model identity, version, configuration and source basis for each
perception stage it actually runs.

## Selected Observation Bundle bridge

The test validates one embedded candidate against the existing canonical
Observation Bundle schema.

Its result is intentionally narrow:

```text
free episode
-> selected visual observation
-> source_representation candidate
-> physical.apparent_condition candidate
```

It explicitly does not create:

```text
stable_object
identity.represents
Evidence
Decision
Requirement
professional defect conclusion
metric geometry
APU write authorization
```

This demonstrates the intended free-to-structured bridge without a parallel
semantic carrier.

## Confidence and certainty boundary

Perception-model scores, matching scores and multi-view consistency should remain
method-specific provenance/quality signals.

They must not be silently mapped to Pantheon professional certainty levels.

```text
model confidence != proof status
model confidence != Evidence strength
multi-view agreement != professional validation
```

If a later adapter needs a normalization between model score and a candidate
certainty description, that mapping must be explicit, versioned and qualified.

## Temporal consequence

Spatial memory also needs temporal discipline.

Two photos of the same apparent area at different dates remain distinct source
observations. A later observation does not erase the earlier episode or claim.

Likewise:

```text
feature absent from later photo
!= project object deleted
```

unless declared coverage and method semantics justify an absence inference.

This reuses the current Project Anatomy temporal/coverage doctrine rather than
adding a spatial-specific currentness model.

## Storage consequence

This branch adopts no storage system.

Expected placement is responsibility-based:

```text
original image/video/scan
-> existing Source / document owners

dense masks/depth/normals/point maps
-> derived representation storage where an existing owner applies

free episodic payload
-> Hermes native or optional runtime-memory provider

selected semantic observation
-> canonical Observation Bundle candidate
-> existing Project Anatomy review/application path
```

A future need for a dedicated blob/cache mechanism must be demonstrated by the
executed corpus rather than anticipated here.

## Replaceability

No model family is selected by this PR.

The meaningful interface is conceptual:

```text
source-linked derivative
+ exact method provenance
+ coordinate frame / calibration context
+ limitations
```

A SAM-like model may later be replaced by another segmenter, a YOLO-like detector
by another detector, or a depth/multi-view estimator by a different provider
without changing Project Anatomy identity or memory authority.

## Tests added

`tests/test_spatial_perception_episodic_memory_qualification.py` verifies:

- qualification-only / no authority adoption;
- exactly four cognitive layers;
- replaceable perception stages;
- explicit coordinate-frame ladder;
- dense outputs remain derived/non-measured;
- free episode survives without stable identity;
- cross-episode association is not a Project Anatomy relation;
- structured context may enrich recall without promotion;
- ambiguity remains unresolved;
- retrieval comparison is qualitative, not a benchmark claim;
- one selected episode validates through the canonical Observation Bundle;
- no pixel/point-level canonical claim explosion.

## Non-goals

- no new Project Anatomy primitive;
- no new semantic graph;
- no new runtime-memory owner;
- no vision model adoption;
- no provider installation;
- no schema for free episodes;
- no pixel/point claim explosion;
- no automatic identity resolution;
- no automatic Evidence/Decision/Register promotion;
- no claim that monocular depth is professional measurement;
- no universal project currentness inference;
- no production storage decision.

## Final invariants

```text
free != untraceable
structured != universally true
memory != Evidence
association != relation_claim
perception != measurement
source representation != stable object
model confidence != professional certainty
local reconstruction != project geometry
retrieved != true
candidate != admitted
projection != persistence
runtime success != authorization
```

## Open after this PR

If this qualification lands, #949 remains open for the executed experiment:

```text
3-10 overlapping non-sensitive architectural photos
-> run exact perception stages
-> retain exact model/config provenance
-> compare structured-only vs enriched recall
-> attempt one candidate semantic promotion
-> inspect ambiguity, coordinate alignment and failure modes
```

Only that executed slice can justify any further runtime, storage or adapter
abstraction.
