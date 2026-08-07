# Project Anatomy V0.2 Design Review

Status: candidate design review — documentation only.
Boundary profile: architecture_project_understanding_model_review.
Date: 2026-08-07.

This review re-reads the current Architecture Project Understanding (APU) / Project Anatomy model after the executable H1/H2 progress in `pantheon-mvp` and before fixing the Revit 2027 adapter data contract.

It does not introduce a new ontology, runtime, persistence owner, graph, approval path, Revit capability or migration. It proposes a simplification target and identifies where the current v0.1 model is now too redundant or too narrow for the first professional wave.

The existing owners remain authoritative until a reviewed schema change says otherwise:

```text
PROJECT_UNDERSTANDING.md
-> belief, provenance, doubt, contradiction, derivation and canonization rules.

PROJECT_OBJECT_MODEL.md
-> current architecture-domain project object vocabulary.

PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
-> current external adapter chokepoint.

PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
-> current H implementation convergence note.

REVIT_LOCAL_ADAPTER.md
-> local Revit execution boundary.
```

Where this review conflicts with a current reviewed schema or executable owner, the current schema or owner wins until a dedicated migration is reviewed and merged.

## 1. Why re-open the model now

The v0.1 contracts were deliberately conservative. That was appropriate while Project Anatomy was documentation-only.

The repository state has now changed materially.

Observed on 2026-08-07:

```text
Pantheon-Next main
= a15f5c418560f292df1b915572b21a04fc9fdf23

pantheon-mvp main observed
= f1c0dcd56bafb9a8fd7a2be985ca6bc3340afd86
```

`pantheon-mvp` now has an executable project-scoped APU owner and applies the bounded `add_match_to_existing_object` operation after exact review, authorization, target revision and idempotency checks.

Current executable persistence is still intentionally small:

```text
project owner revision
stable_object payload
optional object_identity payload
object_relation payloads
append-only owner events
bounded source match application
```

The broader v0.1 vocabulary is not yet deeply embedded in executable persistence:

```text
attribute_claim
spatial_node
property_set
instance_override
object_group
phase_state
analysis_context_candidate
```

This creates a narrow window where structural simplification is cheaper than preserving all v0.1 distinctions through Revit, IFC, IDS, drawing takeoff, economy, RE2020 and ACV integrations.

```text
implemented H2 != complete Anatomy model frozen
```

## 2. Core decisions that remain correct

This review keeps the following principles unchanged.

### 2.1 One project identity independent of source systems

```text
Revit ElementId != stable project identity
Revit UniqueId != stable project identity
IFC GlobalId != stable project identity
PDF label != stable project identity
room number != stable project identity
```

Source identifiers remain evidence and matching material.

### 2.2 Project Anatomy is a projection, not a second authority

```text
APU
= project-understanding authority.

Project Anatomy
= calculated user-facing projection over that authority.
```

No viewer, Revit cache, IFC database, graph renderer or local adapter becomes a competing source of truth.

### 2.3 Facts remain claims with per-field provenance

```text
source observation != truth
source agreement != truth
runtime success != Evidence
calculated value != approved use
```

The existing `attribute_claim` posture is retained as the preferred fact carrier.

### 2.4 Contradictions are preserved

Competing claims stay visible until governed review. An adapter or model does not resolve a contradiction by overwriting the lower-ranked source.

### 2.5 Cross-family records keep their own authority

```text
APU object != ProjectClaim
APU object != WorkIssue
APU object != Decision
APU object != Information
```

They may reference the same stable object without being absorbed into a universal graph record.

## 3. Finding A — `stable_object` and `object_identity` overlap

Current state:

`stable_object` carries:

```text
stable_object_id
kind
human_ref
scope
proof_status
matches
```

`object_identity` independently carries:

```text
stable_id
object_kind
human_ref
internal_code
current_display_name
source_refs
aliases
name_history
```

The executable H1 owner already has to enforce:

```text
object_identity.stable_id == stable_object.stable_object_id
object_identity.object_kind == stable_object.kind
```

and stores both payloads inside one project object row.

This is a duplicated identity responsibility.

### V0.2 recommendation

Retain exactly one canonical identity carrier.

Preferred target:

```text
stable_object
├── stable_object_id
├── object_family
├── project_ref / scope
├── identity_status
├── nomenclature
│   ├── internal_code
│   ├── current_display_name
│   ├── aliases
│   └── name_history
└── classification references
```

`object_identity` should either:

1. disappear after compatibility migration; or
2. become a pure value object subordinate to `stable_object`, with no duplicate stable id, object kind or authority fields.

Recommendation: prefer option 1 unless a real consumer demonstrates independent lifecycle value.

## 4. Finding B — `attribute_claim`, `property_set.claims` and `instance_override` create three fact channels

The belief contract correctly defines `attribute_claim` as the elementary sourced datum. It carries:

```text
about
value
modality
source authority
derivation
certainty
tolerance
proof status
approval state
allowed / forbidden use
evidence
validity
```

The project object model then introduces another value-bearing path inside `property_set.claims`:

```text
property_key
value
value_type
unit
status
source_refs
```

and a third one in `instance_override`:

```text
target
overrides
value
status
source_refs
```

This becomes dangerous as soon as the same window may carry:

```text
Revit width
PDF width
CCTP required width
DPGF quantity
thermal performance
environmental product candidate
site-observed substitution
```

### V0.2 recommendation

Make `attribute_claim` the only canonical value-bearing claim.

```text
attribute_claim
= elementary datum with provenance and use posture.

property_set
= organization / grouping / inheritance metadata over claim references.

instance override
= precedence / exception relation between claims, not another value carrier.
```

Possible target:

```text
property_set
├── property_set_id
├── applies_to
├── property_set_type
└── attribute_claim_refs[]

claim_override
├── override_id
├── target_object_ref
├── inherited_claim_ref
├── replacement_claim_ref
└── reason
```

No numeric or textual project fact should need to choose between `attribute_claim`, inline property value or inline override value.

## 5. Finding C — `spatial_node` duplicates stable spatial identity

Current v0.1 has two partially overlapping classifications:

```text
stable_object.kind
= space | boundary | opening | path | level | grid | vertical_connection

spatial_node.node_kind
= project | site | parcel | building | level | zone | space | room | subspace
```

This leaves ambiguous cases:

```text
Revit Room -> stable_object(space) + spatial_node(room)?
IFC IfcSpace -> same?
Level -> stable_object(level) + spatial_node(level)?
Zone -> spatial_node only or stable object too?
```

### V0.2 recommendation

A project entity that needs durable identity should have one `stable_object_id`.

Spatial hierarchy should become either:

- a spatial role/profile of the stable object; and/or
- typed `contains`, `located_in`, `belongs_to_zone` relation claims.

Preferred target:

```text
stable_object
family: spatial
classification: room | level | zone | building | site | ...
```

`spatial_node` then becomes a calculated projection or a compatibility view, not a second identity owner.

## 6. Finding D — source representations are described in doctrine but not first-class in the model

Project Anatomy already states that one stable object may have several source-bound representations:

```text
Revit element
IFC entity
PDF plan occurrence
section/elevation/detail occurrence
OpenTakeoff shape
site photograph observation
manual annotation
```

The current `stable_object.matches` array is too small to carry the information needed by a production Revit 2027 adapter:

```text
source candidate id
source artifact id
certainty
status
match axis
match evidence
```

It cannot cleanly own:

```text
native source identity
source revision/index
binding / adapter version
freshness token
observation timestamp
coordinate frame
calibration
view / sheet / locator
phase / design option / workset
geometry digest
limitations
```

### V0.2 recommendation — introduce `source_representation`

Candidate shape:

```text
source_representation
├── representation_id
├── source_type
├── source_artifact_ref
├── source_version_ref
├── native_identity
├── locator
├── observed_at
├── binding_ref
├── adapter_version
├── freshness_token
├── coordinate_frame
├── calibration_ref
├── context
├── limitations[]
└── evidence_refs[]
```

A representation may exist before identity matching.

Matching is a separate governed statement:

```text
representation_match
├── representation_ref
├── stable_object_ref
├── match_axis
├── certainty
├── proof_status
├── evidence_refs
└── review refs
```

This replaces the overloaded `stable_object.matches` list over time.

```text
representation observed != stable identity matched
match accepted != project fact canonized
```

## 7. Finding E — relations need the same proof posture as attributes

Current `object_relation` contains:

```text
relation_id
type
from
to
qualifier
source_refs
```

But a project relation can be uncertain or contradictory:

```text
Revit: door hosted by wall A
PDF inference: door belongs to wall B
site photo: host not visible
```

A relation such as `opens_to`, `hosted_by`, `adjacent_to` or `serves` may be derived and therefore must be reviewable like a dimensional claim.

### V0.2 recommendation — promote `relation_claim`

Candidate shape:

```text
relation_claim
├── relation_claim_id
├── type
├── from_stable_object_ref
├── to_stable_object_ref
├── qualifier
├── modality
├── proof_status
├── certainty
├── derivation_refs
├── evidence_refs
├── validity
└── allowed / forbidden use where relevant
```

The current `object_relation` may remain as a compatibility projection of accepted relation claims.

## 8. Finding F — `object_kind` is too narrow and mixes semantic family with tool classification

The current enum is:

```text
space
boundary
opening
path
level
grid
vertical_connection
```

That was sufficient for a minimal plan-understanding proof but not for the now-confirmed first wave:

```text
architecture
economy / quantities
construction-site / DET
RE2020 data preparation
ACV / carbon
```

The solution is not to create a giant enum mirroring Revit categories.

### V0.2 recommendation — broad stable families + external classifications

Suggested stable families:

```text
spatial
element
opening
boundary
assembly
interface
material
product
path
datum
system
group
```

Exact discipline/tool classifications remain external or claim-backed:

```text
architecture: door
Revit category: OST_Doors
Revit family/type: ...
IFC class: IfcDoor
agency classification: ...
lot / DPGF classification: ...
```

```text
Revit category != Pantheon object family
IFC class != Pantheon object family
```

This keeps Project Anatomy stable while adapters evolve.

## 9. Finding G — `stable_object.matches` mixes representation storage and identity proof

H2 currently appends a reviewed source candidate into `stable_object.matches`. This is correct for the intentionally bounded first write, but it should not become the long-term storage pattern for all Revit/IFC/PDF observations.

Otherwise the stable object JSON grows into a heterogeneous embedded source log and every new source type changes the identity payload.

### V0.2 recommendation

Preserve H2 semantics and event history, but plan a compatibility migration:

```text
source_match_applied event
-> representation_match row / projection
-> stable object identity unchanged
```

The H2 authorization, freshness, digest and idempotency semantics remain valuable and should survive unchanged.

## 10. Finding H — documentation and executable state have diverged

`PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md` still describes authorized APU write application as not established.

Current MVP now implements the bounded H2 application path.

The authority index also still describes the core APU documents as `documented non-implemented` without noting that downstream H1/H2 executable owners now consume part of the contract.

This should be corrected after the V0.2 decision without pretending the complete Anatomy model is implemented.

Preferred state classification:

```text
Project Anatomy / APU contract family
= partial

implemented:
- project-scoped read owner for reviewed bootstrap dossier
- bounded source match preparation / authorization / application
- revision freshness
- idempotent replay
- append-only material event
- bounded Decision Request -> APU scope refs

documented but not implemented:
- complete claim persistence
- source representation owner
- relation-claim owner
- full Project Anatomy API / Cockpit projection
- production adapters
- Revit add-in
```

## 11. Finding I — examples already show vocabulary drift

The architecture vertical example uses values such as:

```text
object_kind: door
```

while the current shared schema enum does not contain `door`.

This is not only an example defect; it demonstrates that exact architectural classifications are already trying to escape the narrow v0.1 object-kind vocabulary.

V0.2 should resolve the model rather than merely adding more enum literals.

## 12. Candidate V0.2 core

The smallest coherent target is:

```text
Project
│
├── stable_object
│   ├── one durable project identity
│   ├── broad semantic family
│   ├── nomenclature
│   └── classification refs / claims
│
├── source_representation
│   ├── Revit
│   ├── IFC
│   ├── PDF / drawing
│   ├── OpenTakeoff
│   ├── photo
│   └── manual
│
├── representation_match
│   └── reviewed identity alignment
│
├── attribute_claim
│   └── all sourced / derived values
│
├── relation_claim
│   └── all sourced / derived domain relations
│
├── object_group
│   └── grouping / inheritance only
│
├── requirement / classification / program objects
│   └── existing program-and-conformance owner
│
└── governance cross-links
    ├── Information
    ├── ProjectClaim
    ├── WorkIssue
    └── Decision Request / Decision
```

Supporting governance stays outside the project object itself:

```text
evidence
derivation
doubt
contradiction
human override
canonization
```

## 13. Revit 2027 consequence

The Revit add-in should not produce `stable_object` records directly.

Its bounded output should be closer to:

```text
Revit Context Snapshot
+ source_representation candidates
+ attribute observations
+ relation observations
+ technical warnings / limitations
```

Hermes may propose:

```text
classification candidates
representation_match candidates
relation candidates
questions / blockers
```

Pantheon/MVP then owns review and bounded application.

Example:

```text
Revit Element 40291
-> source_representation(revit)
-> candidate match to DOOR-0042
-> human review
-> governed representation_match application
-> width/material/type observations become attribute claims
-> hosted_by / opens_to become relation claims
```

This prevents the plugin from becoming an APU writer or identity authority.

## 14. IFC and IDS consequence

IFC remains a source representation, not the Anatomy ontology.

```text
IfcDoor / GlobalId
-> source_representation(ifc)
-> reviewed match to stable object
```

IDS is best treated as a machine-readable requirement source and deterministic validation input:

```text
IDS requirement
+ IFC/Revit observations
-> deterministic validator
-> derivation / conformance candidate
-> Evidence candidate
-> human / professional gate
```

No IDS result automatically canonizes an APU claim.

## 15. OpenTakeoff consequence

OpenTakeoff should produce drawing-bound source representations and quantity/geometry claims:

```text
OpenTakeoff shape
-> source_representation(drawing_takeoff)
-> quantity / geometry attribute_claim candidate
-> optional match candidate to existing stable object
```

Its own approved/agent review marks remain engine-local observations and do not become Pantheon approval states.

## 16. First-wave professional coverage check

### Architecture

Covered through stable spatial/element identities, source representations, attribute claims and relation claims.

### Economy

```text
quantity claim
lot / classification claim
price source / ProjectClaim
```

Computed quantity remains distinct from contractual quantity.

### Construction site / DET

Photos and site observations become source representations and claims attached to stable objects. WorkIssue remains the task/reserve owner.

### RE2020

Envelope, orientation, areas, materials and zone data become sourced claims. Regulatory computation remains in a separate admitted calculation binding.

### ACV / carbon

Material/product/quantity/environmental-data associations become claims with explicit source, version, applicability and uncertainty. Product matching does not imply environmental-data validation.

## 17. Compatibility posture

This review does not recommend destructive replacement of H1/H2 history.

A future migration should preserve:

```text
stable object ids
project owner revisions
object revisions
source_match_applied events
command digests
authorization refs
idempotency keys
review refs
source candidate refs
```

Candidate compatibility mappings:

```text
object_identity
-> fold nomenclature into stable_object, then deprecate duplicate identity carrier.

stable_object.matches
-> representation_match projection, preserving H2 event provenance.

property_set.claims
-> attribute_claim records; property_set keeps claim refs only.

instance_override
-> replacement/precedence relation between attribute claims.

spatial_node
-> stable spatial object + relation projection.

object_relation
-> relation_claim; accepted relation projection may keep old shape temporarily.
```

No migration should invent evidence, certainty or approval state for old rows.

## 18. What should not be changed by V0.2

Do not revisit these boundaries:

```text
Pantheon governs.
Hermes orchestrates and executes admitted methods.
Revit executes locally.
OpenWebUI / Cockpit exposes.
The human decides consequential effects.
```

Do not move into APU:

```text
Evidence lifecycle
Decision lifecycle
WorkIssue lifecycle
ProjectClaim values
Hermes runtime state
plugin capability authorization
regulatory calculation authority
```

Do not turn Project Anatomy into:

```text
IFC clone
Revit database
property graph runtime
viewer-owned state
BIMserver replacement
scheduler / queue / workflow engine
```

## 19. Recommended design decisions before protected-schema edits

The following questions should be resolved explicitly before touching `schemas/` or MVP migrations:

1. Is `object_identity` removed or retained as a subordinate value object?
2. Is `spatial_node` deprecated into a projection, or retained as a strict one-to-one profile of a stable object?
3. Exact `source_representation` minimum fields and lifecycle.
4. Whether identity matching is named `representation_match` or another existing-compatible term.
5. Whether `object_relation` is replaced by `relation_claim` or extended in place.
6. Broad `object_family` vocabulary and classification placement.
7. How old H2 `matches` material is projected without rewriting append-only event history.
8. Which current fixtures and MCP validation surfaces need compatibility support during migration.

## 20. Review conclusion

The v0.1 Project Anatomy concept should be retained, but its internal carrier model should be simplified before Revit 2027 and the wider first-wave adapters harden it.

The highest-value changes are:

```text
one identity carrier
one value-claim carrier
one relation-claim carrier
first-class source representations
broad semantic families + external classifications
spatial hierarchy as a projection/role, not a second identity system
```

The current executable H1/H2 work is not wasted. Its strongest mechanisms — project scope, stable ids, review, authorization, freshness, idempotency and append-only application history — remain the foundation of V0.2.

```text
simplify carriers
!= discard governance
```

No schema, runtime, migration or production adapter is changed by this design review.
