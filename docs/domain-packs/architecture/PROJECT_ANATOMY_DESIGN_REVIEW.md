# Project Anatomy — historical design rationale

Status: historical design rationale — non-authoritative.
Authority: `PROJECT_ANATOMY_MODEL.md`.
Do not use this document as an implementation contract.

This file preserves the detailed reasoning, alternatives and migration rationale that led to the current Project Anatomy model. It is intentionally retained for auditability and future design review, while `PROJECT_ANATOMY_MODEL.md` is the sole active conceptual authority.

---

# Project Anatomy V0.2 — target core model

Status: candidate target model — documentation only until protected-schema migration is reviewed and merged.
Boundary profile: `architecture_project_understanding_v02`.
Date: 2026-08-07.

This document supersedes the exploratory posture of the first V0.2 review and records the **target simplification** to adopt before Revit 2027, IFC/IDS, drawing takeoff, economy, construction-site, RE2020 and ACV integrations harden the current V0.1 carriers.

It does not itself migrate schemas, persistence or runtime. Until protected-schema work is merged, current reviewed schemas and executable owners remain authoritative.

```text
Pantheon Next governs.
Hermes orchestrates admitted methods.
Revit executes locally.
OpenWebUI / Cockpit exposes.
The human decides consequential effects.
```

## 1. Decision summary

Project Anatomy V0.2 should be built around four orthogonal project-understanding primitives:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

Requirements remain a separate intent/conformance family:

```text
program
requirement
classification_scheme
```

Provenance and governance remain supporting contracts, not project-world identities:

```text
derivation / calculation record
proof-register Evidence references
contradiction / conflict record where needed
Approval / use grant
Decision Request / Decision
WorkIssue
ProjectClaim
Information
```

The target is deliberately smaller than V0.1.

```text
one durable identity carrier
one source-occurrence carrier
one value-claim carrier
one relation-claim carrier
one requirement carrier for prescriptive intent
```

No source adapter, viewer or runtime receives a second way to describe the same project fact.

## 2. Why remodel now

The V0.1 model was deliberately broad while Project Anatomy was documentation-first.

The executable surface is still narrow enough to change safely.

Observed executable MVP state already persists only a small subset:

```text
project owner revision
stable_object payload
optional object_identity payload
object_relation payloads
append-only owner events
bounded add_match_to_existing_object application
```

The executable owner already has to assert that duplicated identity fields agree:

```text
object_identity.stable_id == stable_object.stable_object_id
object_identity.object_kind == stable_object.kind
```

The broader carriers are not yet deeply embedded in persistence:

```text
attribute_claim
spatial_node
object_group
space_group
property_set
instance_override
phase_state
analysis_context_candidate
object_note
classification
human_override
canonization
```

This is the correct point to remove overlapping responsibilities instead of carrying them into Revit, IFC, IDS, OpenTakeoff, economy, thermal and carbon workflows.

```text
implemented H2 != Anatomy model frozen
```

## 3. Non-negotiable invariants

### 3.1 Stable project identity is source-independent

```text
Revit ElementId != stable project identity
Revit UniqueId != stable project identity
IFC GlobalId != stable project identity
PDF room number != stable project identity
OpenTakeoff shape id != stable project identity
photo detection id != stable project identity
```

### 3.2 A source observation is not project truth

```text
observed in Revit != accepted project fact
present in IFC != accepted project fact
measured on PDF != contractual quantity
found in CCTP != executed state
runtime_success != Evidence
```

### 3.3 Project Anatomy is a projection

```text
APU
= governed project-understanding authority.

Project Anatomy
= user-facing projection calculated from that authority.
```

A viewer, graph, BIM database, Revit cache, IFC store or takeoff engine never becomes a competing authority.

### 3.4 Claims preserve disagreement

Competing claims remain separate. A higher-ranked source may influence review but does not erase a lower-ranked observation.

### 3.5 Governance families stay separate

```text
APU object != ProjectClaim
APU object != Information
APU object != WorkIssue
APU object != Decision
APU object != Evidence
```

Cross-links are explicit references.

## 4. Layer model

V0.2 separates five conceptual layers.

### Layer A — project identity

```text
stable_object
```

Answers:

> What project entity are we talking about across sources and indices?

### Layer B — source-bound occurrences

```text
source_representation
```

Answers:

> What exactly did a source or adapter expose, where, when and under which technical context?

### Layer C — assertions

```text
attribute_claim
relation_claim
```

Answers:

> What value or relationship is being asserted, by which source or derivation, with which proof posture?

### Layer D — intent and requirements

```text
program
requirement
classification_scheme
```

Answers:

> What is required, expected or prescribed, independently of what is currently observed?

### Layer E — proof, derivation and governance

```text
Proof Register / Evidence
Derivation record
Contradiction / conflict
Approval / use grant
Decision Request / Decision
WorkIssue
```

Answers:

> Why may this claim be trusted for a declared use, what conflicts remain, and what requires a human decision?

These layers must not be collapsed into one universal graph record.

## 5. Canonical reference shape

V0.2 should introduce one reusable typed reference for APU entities.

Candidate semantic shape:

```yaml
entity_ref:
  entity_type: stable_object | source_representation | requirement | program
  entity_id: <stable id>
```

Claims can therefore exist before source-to-project identity resolution.

Example:

```text
Revit element observed
-> source_representation REVREP-40291
-> width claim about REVREP-40291
-> candidate identity relation to DOOR-0042
-> reviewed identity relation
-> optional derived width claim about DOOR-0042
```

This is preferable to forcing every source observation to know a stable object before it can be represented.

## 6. Primitive 1 — `stable_object`

### Responsibility

`stable_object` owns exactly one thing: **durable project identity**.

It should not also become:

```text
source observation log
property bag
evidence record
decision
classification database
workflow state
Revit mirror
IFC entity clone
```

### Target semantic shape

```yaml
stable_object:
  stable_object_id: OBJ-...
  project_ref: PROJECT-...
  object_family: spatial | element | assembly | material | system | datum | group | type_definition
  nomenclature:
    internal_code: optional
    display_name: optional
    aliases: []
    name_history: []
```

Exact schema details are defined by the protected-schema migration, but the semantic responsibilities are fixed here.

### Object family

The family vocabulary must remain broad and source-independent.

Preferred initial families:

```text
spatial
  site, building, level, zone, room, space through classification claims.

element
  wall, door, window, slab, roof, furniture, equipment occurrence, etc.

assembly
  layered envelope assembly, construction complex, kit or composed object.

material
  project material identity when it needs independent quantities/provenance.

system
  architectural or project system identity where useful without implying CVC design authority.

datum
  level/grid/reference datum when durable identity is needed.

group
  apartment, functional zone, work zone, package, transversal set, etc.

type_definition
  durable project type/typology used by occurrences.
```

Exact métier meaning comes from claims/classifications, not from a growing Revit-like enum.

```text
Revit Category != object_family
IFC Class != object_family
DPGF lot != object_family
```

### Identity candidates

A `stable_object` should exist only once identity creation has passed the relevant governed gate.

Candidate identities belong in ResultCandidate / review flow, not as half-canonical `stable_object` rows with ambiguous proof posture.

## 7. Primitive 2 — `source_representation`

### Responsibility

A source representation records one source-bound occurrence without claiming that it is a stable project identity.

Examples:

```text
Revit element
IFC entity
PDF room polygon
OpenTakeoff shape
schedule row
photo detection
manual annotation
scan / point-cloud occurrence
```

### Minimum semantic contract

```yaml
source_representation:
  representation_id: REP-...
  project_ref: PROJECT-...
  source_artifact_ref: ...
  source_version_ref: optional
  source_kind: revit | ifc | drawing | drawing_takeoff | image | photo | manual | other
  identifiers:
    - scheme: revit.unique_id
      value: ...
    - scheme: revit.element_id
      value: ...
  locators: []
  observed_at: ...
  binding_ref: ...
  adapter_version: ...
  freshness_token: ...
  content_digest: optional
  coordinate_frame: optional
  calibration_ref: optional
  context: {}
  limitations: []
```

### Source identifiers

Use namespaced identifier pairs rather than source-specific columns.

```text
revit.unique_id
revit.element_id
ifc.global_id
pdf.page_bbox
drawing.shape_id
opentakeoff.shape_id
photo.region_id
```

This avoids changing the core schema for each adapter.

### Freshness

Representations are observations in time.

```text
representation persisted != representation current
freshness token match != project truth
```

A new Revit snapshot may create a new representation revision or supersede the technical freshness of an older one without destroying history.

## 8. Primitive 3 — `attribute_claim`

### Responsibility

`attribute_claim` becomes the **only canonical value-bearing project-understanding claim**.

No numeric/textual project fact should need to choose between:

```text
attribute_claim
property_set.claim
instance_override
phase_state
classification value
human_override assertion
```

### Subject

An attribute claim may be about:

```text
stable_object
source_representation
```

and, where required by the requirement model, another typed APU reference.

### Target semantic shape

```yaml
attribute_claim:
  attribute_claim_id: CLAIM-...
  subject_ref:
    entity_type: stable_object | source_representation
    entity_id: ...
  attribute_key: architecture.width
  value:
    value_type: number | boolean | text | range | reference | controlled_label | structured
    value: ...
    unit: optional
    scheme: optional
  assertion_mode: observed | proposed | derived | human_asserted | as_built
  source_authority: ...
  proof_status: ...
  certainty: optional E0-E4
  source_representation_refs: []
  derivation_refs: []
  evidence_refs: []
  supersedes_claim_ref: optional
  validity: {}
```

### Units

Contracts exposed to Hermes/adapters should use explicit SI semantics.

Examples:

```text
length -> mm or m with explicit unit
area -> m2
volume -> m3
angle -> degree
thermal resistance / conductivity -> explicit engineering unit
carbon -> explicit kgCO2e basis
cost -> explicit currency and price basis
```

Internal Revit feet never leak as an implicit public contract.

### Classification

Classification is an attribute claim, not a second claim type.

Examples:

```yaml
attribute_key: classification.ifc
value: { value_type: controlled_label, value: IfcDoor, scheme: IFC4.3 }

attribute_key: classification.revit_category
value: { value_type: controlled_label, value: OST_Doors, scheme: revit.2027 }

attribute_key: classification.agency
value: { value_type: controlled_label, value: porte_interieure, scheme: ifja.architecture }
```

Multiple classifications may coexist without changing `object_family`.

### Phase / lifecycle state

`phase_state` becomes a claim.

```yaml
attribute_key: lifecycle.project_state
value: existing | to_demolish | demolished | to_create | new | modified | moved | temporary | as_built | unknown
```

Source-specific phase information remains a source-representation claim until mapped/reviewed.

### Human correction

A human override becomes a new claim with higher authority and explicit supersession:

```text
machine/source claim A
-> human claim B
-> B.supersedes_claim_ref = A
```

The original claim is never mutated or erased.

```text
human correction != source mutation
```

## 9. Primitive 4 — `relation_claim`

### Responsibility

Every meaningful relationship that may be sourced, inferred, contradicted or revised uses one claim carrier.

This includes both project-world relations and representation-to-project identity alignment.

### Target semantic shape

```yaml
relation_claim:
  relation_claim_id: REL-...
  subject_ref: { entity_type: ..., entity_id: ... }
  relation_type: architecture.opens_to
  object_ref: { entity_type: ..., entity_id: ... }
  qualifier: optional
  assertion_mode: observed | proposed | derived | human_asserted | as_built
  source_authority: ...
  proof_status: ...
  certainty: optional E0-E4
  source_representation_refs: []
  derivation_refs: []
  evidence_refs: []
  supersedes_claim_ref: optional
  validity: {}
```

### Namespaced relation vocabulary

Do not freeze all future relations into a giant enum.

Use a reviewed registry of namespaced relation ids, for example:

```text
identity.represents
spatial.contains
spatial.located_in
spatial.adjacent_to
architecture.opens_to
architecture.hosted_by
assembly.part_of
model.instance_of
project.belongs_to_group
lifecycle.supersedes
```

Adapters cannot invent arbitrary executable capabilities from this vocabulary; it is descriptive only.

### Identity matching

A source-to-project match is a relation claim:

```text
source_representation
-- identity.represents -->
stable_object
```

Therefore V0.2 does **not** need a fifth `representation_match` carrier.

Candidate, presumed, reviewed and rejected mappings are expressed through the relation claim's proof/review posture and external review records.

This is a deliberate simplification over the initial V0.2 draft.

```text
representation observed != identity matched
identity relation accepted != every source attribute canonized
```

### Source-level relations

A Revit adapter may observe:

```text
REVREP-door
-- architecture.hosted_by -->
REVREP-wall
```

before either occurrence is matched to a stable project object.

After identity review, Hermes may derive a project-level candidate relation between the corresponding stable objects.

## 10. Requirements — keep intent separate from facts

A required condition is not an observed attribute claim.

V0.2 therefore removes `required` from the meaning of ordinary source observations and keeps prescriptive intent in `requirement`.

### Requirement sources

Requirements may come from more than a programme:

```text
programme
client decision
CCTP
contract
IDS
regulation
approved technical brief
agency standard where explicitly applicable
```

The current `from_program`-only posture is too narrow for the intended integrations.

### Target direction

A future generic requirement should carry:

```text
requirement_id
source_ref / source_artifact_ref
target selector or explicit entity ref
requirement type
predicate / attribute / relation being constrained
expected value
comparison/operator
tolerance
scope/applicability
source authority
proof/evidence refs
validity
```

A requirement never becomes an observed project state.

### IDS

IDS should map into requirement candidates and deterministic validation, not into stable-object classification fields.

```text
IDS requirement
+ source observations
-> deterministic validation
-> ResultCandidate / Evidence candidate
-> human/professional gate where consequential
```

## 11. Supporting provenance contracts

### 11.1 Derivation

Keep a derivation/calculation record, but generalize it to produce either attribute or relation claims.

It should record at minimum:

```text
method id + version
input refs
binding/tool/adapter version where applicable
deterministic vs model-assisted method
formula/rule where applicable
produced claim refs
computed uncertainty/tolerance
```

The derivation record explains how a claim was produced; it is not an executor.

### 11.2 Calibration

Calibration remains useful as source-processing provenance for drawings, scans and coordinate transforms.

It is supporting provenance, not a project object.

### 11.3 Evidence

Do not maintain a second APU evidence lifecycle.

The Architecture Proof Register remains the evidence authority. APU claims reference proof-register evidence/anchors.

The current APU `evidence.schema.yaml`, which mirrors the proof-register shape, should be deprecated once direct references are migrated.

```text
localized evidence needed
!= second Evidence authority needed
```

## 12. Conflict and uncertainty

### Contradiction / claim conflict

Contradiction remains important, but it is an **epistemic governance record**, not a project-world object.

It groups competing claim refs and records unresolved/resolved posture without rewriting the claims.

A future rename to `claim_conflict` may be considered, but the current semantic responsibility is valid.

### Doubt

The dedicated APU `doubt` carrier should not remain a second operational backlog.

Use:

```text
claim proof_status = requires_more_evidence / source_missing / contradictory_evidence
+
WorkIssue when work is required
+
Decision Request when human arbitration is required
```

The old `doubt` schema may remain as a compatibility input during migration, but it should not be a V0.2 core authority.

## 13. Grouping, spatial hierarchy and inheritance

### 13.1 `spatial_node` is deprecated as an identity carrier

A room, level, building or zone that needs durable project identity is a `stable_object` with `object_family: spatial` or `group` and appropriate classification claims.

Spatial hierarchy is expressed by relation claims:

```text
spatial.contains
spatial.located_in
project.belongs_to_group
```

No second `spatial_node_id` identity owner is needed.

### 13.2 `space_group` and `object_group` collapse into stable objects

A T2, duplex, work zone, functional group or transversal set that needs identity becomes a stable object, usually `object_family: group` or `spatial`.

Membership and nesting use relation claims.

```text
space_group != special identity system
object_group != special identity system
```

### 13.3 Type and inheritance

Do not keep property inheritance in a separate `property_set` value channel.

A type definition is a stable object:

```text
object_family: type_definition
```

Occurrences link to it:

```text
occurrence -- model.instance_of --> type_definition
```

Attributes may be asserted on the type definition. Resolution logic may inherit those accepted claims to instances, while an instance-specific claim supersedes the inherited value for that context.

The override is therefore a claim precedence relationship, not another value carrier.

## 14. Notes and Information

`object_note` overlaps Pantheon's Information family.

V0.2 should not maintain a parallel note authority inside APU.

Use an Information record linked to the stable object through the existing cross-family reference mechanism.

Examples:

```text
site observation
visa note
coordination note
internal note
design intent narrative
```

If a note asserts a machine-actionable project fact, that fact becomes a reviewed claim; the note itself stays Information.

## 15. Analysis context

`analysis_context_candidate` should not remain a dedicated carrier.

Possible analysis applicability is represented by a classification/attribute claim or by a ResultCandidate generated by an admitted domain method.

Examples:

```text
analysis.context.accessibility
analysis.context.fire_separation
analysis.context.wet_room
analysis.context.re2020_envelope
analysis.context.acv_product_mapping
```

A context tag remains non-normative.

```text
analysis context != compliance conclusion
```

## 16. Approval, canonization and use grants

The current APU `canonization` concept encodes a useful rule — a claim may be legitimate for one use and not another — but this responsibility belongs to Pantheon governance, not to the project object model.

V0.2 target:

```text
claim
+
proof / evidence
+
explicit approval or use grant
```

The approval/use-grant record states:

```text
claim/ref
scope
use granted
approval level/state
reviewer/role
evidence refs
decision refs
validity
```

It does not mutate the claim and does not execute anything.

The current `canonization.schema.yaml` should be migrated toward the general approval/proof owner or retained only as a compatibility projection until that owner is executable.

```text
approved for internal review
!= approved for contractual action
```

## 17. Program changes and deviations

### Program change

`program_change` currently duplicates Decision/versioning responsibilities.

Preferred V0.2 posture:

```text
new/changed requirement candidate
+ source Information / Decision ref
+ explicit human Decision where needed
+ immutable previous requirement/version history
```

Do not maintain a second programme-decision lifecycle inside APU.

### Deviation

A deviation is derived from:

```text
requirement
vs
observed/accepted claims
```

It is therefore an analysis result, not a primitive project-world object.

Preferred path:

```text
validator / Hermes method
-> ResultCandidate
-> WorkIssue candidate and/or Decision Request when consequential
```

The old `deviation` carrier should become compatibility-only rather than the canonical V0.2 result authority.

## 18. V0.1 carrier disposition

| V0.1 carrier | V0.2 disposition | Replacement / owner |
|---|---|---|
| `stable_object` | **retain, simplify** | sole durable identity carrier |
| `object_identity` | **deprecate** | nomenclature folded into `stable_object` |
| `stable_object.matches` | **deprecate** | `relation_claim(identity.represents)` |
| `spatial_node` | **deprecate** | `stable_object` + spatial relation claims |
| `space_group` | **deprecate** | group/spatial stable object + relation claims |
| `object_group` | **deprecate** | group stable object + relation claims |
| `object_relation` | **replace** | `relation_claim` |
| `property_set.claims` | **deprecate as value carrier** | `attribute_claim` |
| `instance_override` | **deprecate** | superseding instance claim + type/group relation |
| `phase_state` | **deprecate** | `attribute_claim(lifecycle.project_state)` |
| `classification` | **deprecate as separate claim carrier** | namespaced classification `attribute_claim` |
| `classification_scheme` | **retain** | vocabulary/registry definition |
| `analysis_context_candidate` | **deprecate** | attribute/classification claim or ResultCandidate |
| `object_note` | **deprecate** | Information + entity reference |
| `human_override` | **deprecate as separate carrier** | human-authored superseding claim/relation |
| `attribute_claim` | **retain, generalize** | sole value claim carrier |
| `derivation` | **retain, generalize** | claim provenance/calculation record |
| `calibration` | **retain as support** | source-processing provenance |
| APU `evidence` | **deprecate duplicate authority** | Architecture Proof Register Evidence |
| `contradiction` | **retain outside world core** | epistemic conflict record over claim refs |
| `doubt` | **deprecate operational authority** | proof status + WorkIssue / Decision Request |
| `program` | **retain** | requirement source/container |
| `requirement` | **retain, generalize** | generic prescriptive intent |
| `program_change` | **deprecate lifecycle** | requirement versioning + Decision |
| `deviation` | **deprecate as core object** | ResultCandidate + WorkIssue / Decision Request |
| `canonization` | **migrate out of APU core** | approval/use-grant governance |

This table is a target disposition. Existing schemas remain valid until their migration PR explicitly changes status or compatibility handling.

## 19. Revit 2027 contract consequence

The Revit add-in must not manufacture APU stable identities or directly write arbitrary Anatomy state.

Its bounded output should be source-oriented:

```text
Revit Context Snapshot
source_representation observations
attribute_claim candidates about those representations
relation_claim candidates between those representations
technical warnings / limitations
```

Example:

```text
Revit Element 40291
-> REP-RVT-40291
-> claim REP-RVT-40291 architecture.width = 900 mm
-> relation REP-RVT-40291 architecture.hosted_by REP-RVT-39810
-> candidate relation REP-RVT-40291 identity.represents OBJ-DOOR-0042
-> human/review gate
-> reviewed identity relation
-> optional derived stable-object claims
```

The plugin owns:

```text
real Revit observation
native identifiers
freshness
preflight
named transaction
technical result
```

It does not own:

```text
stable project identity
Evidence admission
Decision
WorkIssue closure
contractual truth
regulatory conclusion
```

## 20. IFC consequence

```text
IfcDoor / GlobalId
-> source_representation(ifc)
-> source-level claims
-> candidate identity.represents relation
-> reviewed stable-object alignment
```

IFC remains a representation and classification source, not the Anatomy ontology.

## 21. IDS consequence

IDS should feed the requirement/conformance layer.

```text
IDS specification
-> requirement candidates
-> deterministic validator over IFC/Revit representations/claims
-> conformance ResultCandidate
-> Evidence candidate
-> human/professional gate as required
```

No IDS result automatically canonizes a claim.

## 22. OpenTakeoff / drawing consequence

```text
OpenTakeoff shape
-> source_representation(drawing_takeoff)
-> area / length / count claims about representation
-> optional source-level relations
-> candidate identity.represents relation
```

Engine-local `AGENT` or `APPROVED` marks remain source metadata. They do not become Pantheon approval states.

## 23. Economy consequence

Economy reads the same project object and claims rather than creating a quantity object silo.

Example window occurrence:

```text
stable object
├── Revit representation
├── drawing representation
├── IFC representation
├── quantity claims
├── material claims
├── lot classification claim
├── price / contractual values via ProjectClaim or economy authority
└── relation to type / assembly
```

```text
quantity computed != quantity contractually accepted
```

## 24. Construction-site / DET consequence

Photos and site observations remain source representations or Information depending on structure.

Machine-actionable observations become claims tied to the representation/stable object.

Reservations and corrective work remain WorkIssue territory.

```text
site observation != WorkIssue automatically
transaction success != reserve closed
```

## 25. RE2020 consequence

Envelope geometry, orientation, areas, glazing, assemblies and material properties become claims.

A specialist local calculation engine consumes qualified claims/representations and returns sourced results.

```text
Hermes reasoning != certified regulatory calculation
```

Regulatory results carry engine/version/input provenance and are not conversationally invented.

## 26. ACV / carbon consequence

Material quantities, product mappings and environmental-data associations use the same claims and source representations.

```text
product matched != environmental data validated
```

FDES/PEP/generic-data links remain sourced and reviewable.

## 27. H2 compatibility

Current H2 appends a reviewed source candidate into `stable_object.matches` and records append-only application history.

Do not rewrite or erase those events.

Migration target:

```text
existing source_match_applied event
-> compatibility projection
-> equivalent source_representation where reconstructable
-> equivalent relation_claim(identity.represents)
```

Preserve:

```text
stable_object_id
owner revision
object revision
command digest
authorization ref
idempotency key
review ref
source candidate ref
source artifact ref
execution result ref
```

Do not invent missing certainty, Evidence or approval state during migration.

## 28. Canonicalization rules after V0.2

### Rule A — no inline project facts in identity objects

`stable_object` carries identity/nomenclature only.

### Rule B — no source-specific columns in the project identity core

Source-native identifiers belong to `source_representation`.

### Rule C — no second value channel

Any machine-actionable project value is an `attribute_claim`.

### Rule D — no second relation channel

Any sourced/inferred relationship is a `relation_claim`.

### Rule E — requirements are not facts

Requirements stay in `requirement`, even when they target the same attribute key as an observed claim.

### Rule F — review does not mutate history

Human correction creates superseding claims/relations or review/grant records.

### Rule G — source observations may exist unmatched

An adapter must be allowed to report the real source before Pantheon knows which stable object it represents.

### Rule H — projections are disposable

Spatial trees, property views, grouping views and viewer scene graphs are calculated from the canonical primitives and may be rebuilt.

## 29. What V0.2 must not become

Do not turn the new model into:

```text
RDF platform
property graph runtime
IFC clone
Revit database
BIMserver replacement
viewer-owned database
universal reasoning object
workflow engine
memory engine
approval engine
```

The model is a governed project-understanding contract, not a generic knowledge graph product.

## 30. Migration gates

Protected-schema migration should not be considered complete until all of the following are demonstrated:

```text
one canonical identity path
one canonical value path
one canonical relation path
source occurrence can exist before identity match
current H2 events remain auditable
legacy dossier validation has an explicit compatibility posture
MCP validation cannot silently admit deprecated carriers as new canonical output
pantheon-mvp owner can project the V0.2 model
Revit 2027 DTOs can map without source-specific schema hacks
IFC/IDS/OpenTakeoff can map without creating parallel truth stores
```

## 31. Recommended stacked migration — dependency order only

This is not a delivery schedule. It is the technical dependency order that minimizes mixed authorities.

```text
A. freeze this V0.2 target model

B. protected-schema core
   - typed entity ref
   - simplified stable_object
   - source_representation
   - generalized attribute_claim
   - relation_claim
   - generalized requirement

C. compatibility layer
   - deprecated carrier statuses
   - old dossier adapters
   - MCP validator update
   - fixtures/examples update

D. pantheon-mvp owner migration
   - new persistence/projections
   - legacy H2 event compatibility
   - source representation persistence
   - claim/relation persistence

E. external adapter contracts
   - Revit 2027
   - IFC/IDS
   - drawing takeoff

F. Cockpit / Project Anatomy projections
```

No Revit model-write capability depends on completing this migration; Revit writes remain separately governed external effects.

## 32. Final decision

Project Anatomy V0.1 should **not** be preserved structurally for compatibility convenience.

Its strongest governance principles remain correct, but its carrier model contains overlapping identities, value channels, grouping systems and local governance records that would become expensive once multiple adapters depend on them.

The V0.2 target is therefore intentionally smaller:

```text
stable_object
source_representation
attribute_claim
relation_claim
requirement
```

with supporting provenance and governance outside those project-world primitives.

```text
simplify carriers
!= simplify proof

fewer object types
!= less provenance

one model
!= one authority for everything
```

The purpose of this refactor is to make the project model **more rigorous precisely by making it smaller**.