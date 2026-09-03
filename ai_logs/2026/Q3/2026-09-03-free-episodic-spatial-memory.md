# Free episodic memory and derived spatial perception convergence

Date: 2026-09-03
Status: candidate doctrine update — review pending.
Boundary profile: guidance.

## Objective

Allow more freedom in runtime memory without weakening Pantheon governance or creating a second semantic graph.

The motivating architectural question is whether useful project memory should preserve both:

```text
free / episodic / associative material
and
structured / semantic project knowledge
```

and whether dense visual perception outputs such as segmentation, object detection, depth and surface normals should enrich spatial understanding without becoming canonical project truth.

## Repository state checked

Baseline before change:

```text
Pantheon-Next/main = 61715aa1cea4171f0faede88daffda059d45299f
```

This baseline already includes merged #948, which frames Pantheon as a governed cognitive ecology and explicitly rejects a central-brain interpretation.

Existing owners checked:

- `docs/governance/MEMORY.md`;
- `docs/domain-packs/architecture/PROJECT_ANATOMY_MODEL.md`;
- canonical Project Anatomy Observation Bundle boundaries;
- current Hindsight/Hermes provider-agnostic memory posture.

No open PR was found covering episodic/free memory plus derived spatial perception.

## Convergence decision

Do not add a new Pantheon memory primitive, graph or store.

Keep Project Anatomy unchanged. Its current core already supports the necessary semantic side:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

and already states:

```text
source representation may exist before stable identity resolution
raw observed != canonically retained
Hermes output != APU mutation
```

The smaller change is to clarify the Memory owner.

## Free episodic memory

Runtime memory may retain narrative observations, hypotheses, ambiguity, unusual details and associations without first forcing them into a structured semantic vocabulary.

Preferred principle:

```text
free payload
+ minimal routing envelope when available
```

Candidate envelope concepts are only guidance:

```text
episode identity
scope
time when useful
free content
refs when known
runtime/provider provenance
```

No Pantheon schema is adopted by this change.

## Structured/free asymmetry

```text
structured owner -> runtime context / recall
= bounded retrieval

runtime memory -> structured owner
= proposal only
= existing owner validates/adopts
```

Therefore:

```text
retrieval may be bidirectional
promotion remains governed and one-way
```

Memory association is not a Project Anatomy relation claim.

## Spatial perception

Dense outputs from replaceable perception tools remain source-linked derived runtime representations unless a selected observation is deliberately distilled through the canonical Observation Bundle.

Examples:

```text
segmentation masks
object detections
depth maps
surface-normal maps
embeddings
camera pose / tracks
point maps / point clouds / meshes
```

Required distinctions:

```text
segmentation != stable identity
detection != Project Anatomy object
depth prediction != surveyed geometry
normal prediction != measured orientation
multi-view association != identity accepted
derived spatial representation != Evidence
```

Project Anatomy should receive only selected, useful semantic observations rather than one canonical claim per pixel or point.

## Qualification follow-up

Issue #949 was opened to qualify the idea on a bounded non-sensitive multi-photo corpus.

The qualification should compare structured-only retrieval against structured + episodic + derived-spatial recall and should attempt one candidate promotion through the existing Observation Bundle without adding a parallel semantic carrier.

## Files changed

- `docs/governance/MEMORY.md`;
- this intervention log.

Project Anatomy doctrine is deliberately not changed because its existing boundaries already support the proposed composition.

## Non-goals

- no schema;
- no SQL migration;
- no `EpisodicMemory` Pantheon object;
- no `SpatialGraph`;
- no fifth Project Anatomy primitive;
- no automatic semantic promotion;
- no automatic Evidence/Decision/Register promotion;
- no perception model adoption;
- no runtime installation or provider selection.

## Final invariants

```text
free != untraceable
structured != universally true
memory != Evidence
association != relation_claim
perception != measurement
retrieved != true
candidate != admitted
projection != persistence
runtime success != authorization
```
