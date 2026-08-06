# Project Anatomy Knowledge Structure

Status: candidate support doctrine — discussion-recovery annex, documentation only.
Boundary profile: architecture_project_understanding_projection.
Date: 2026-08-06.

This annex records the parts of the Project Anatomy discussions that were not
explicit enough in `PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md`.

It is subordinate to the existing owners:

```text
PROJECT_OBJECT_MODEL.md
-> project-world objects, spatial structure, properties and APU domain relations.

PROJECT_UNDERSTANDING.md
-> beliefs, provenance, derivation, uncertainty, contradiction and canonization.

PROGRAM_AND_CONFORMANCE.md
-> requirements, classifications, deviations and program intent.

PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
-> external PDF / image / IFC / Revit adapter boundary.

PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
-> implementation sequence and executable-owner trajectory.

REVIT_LOCAL_ADAPTER.md
-> local Revit observation and mutation boundary.
```

This document creates no fourth APU authority, no new ontology, no graph store,
no extraction runtime and no automatic professional conclusion. Where it
conflicts with an owner or reviewed schema, the owner or schema prevails.

## 1. Recovered intent

The intended capability is not merely to list rooms or import an IFC tree.
Pantheon must progressively build a governed, queryable understanding of an
architectural project from heterogeneous and partially contradictory material:

```text
plans
sections
elevations
details
CCTP and DPGF
IFC
Revit observations
plan images and scans
site photographs
reports and meeting minutes
manual professional input
```

The target is a coherent spatial and technical hypothesis that can be inspected,
corrected and qualified. It must explain:

```text
what object is being discussed
where it is located
what it contains or connects to
which source and exact fragment support each attribute
which state, phase, index and variant the statement concerns
what is required, proposed, observed or as-built
what is missing, doubtful or contradictory
what requires a human decision
```

```text
coherent hypothesis != complete geometric reconstruction
multi-source agreement != truth
3D-compatible understanding != BIM authority
```

## 2. Knowledge strata

Project Anatomy must not flatten all project knowledge into one object record.
The same stable object may be read through several governed strata.

### 2.1 Identity and project-world structure

Owner: `PROJECT_OBJECT_MODEL.md`.

```text
stable identity
object kind
spatial hierarchy
transversal groups
APU domain relations
phase state
aliases and source identifiers
```

Examples:

```text
Project
-> Site
-> Building
-> Level
-> Zone
-> Space
-> Architectural element or system
```

Identity remains independent of a Revit ElementId, IFC GUID, room number, drawing
label or CCTP article number.

### 2.2 Source representations and geometry

A stable object may have several source representations:

```text
plan occurrence
section occurrence
elevation occurrence
detail occurrence
photo observation
IFC representation
Revit representation
manual sketch or annotation
```

A representation carries source identity, source version or index, locator,
coordinate frame, registration/calibration posture and geometry claims where
available. A representation is not a second stable object.

```text
one object -> several representations
one representation -> one source-bound observation
representation id != stable object id
```

### 2.3 Attributes, properties, quantities and materials

Owner: APU `attribute_claim`, `property_set`, `property_claim` and
`instance_override` responsibilities.

The object may carry sourced claims such as:

```text
dimensions
areas and volumes
clear heights
counts and quantities
materials and layers
opening dimensions and operation
fire, acoustic and thermal properties
system or assembly references
condition and observed defects
```

Each value must retain modality, source, locator, certainty, time and applicable
variant or phase.

```text
quantity extracted != quantity contractually accepted
material mentioned != material installed
property present in Revit != professionally validated property
```

### 2.4 Intent, requirements and classifications

Owner: `PROGRAM_AND_CONFORMANCE.md` and ProjectClaim where a consequential value
requires its own project-value lifecycle.

Intent may originate from:

```text
client program
CCTP
regulatory or urban-planning source
approved design decision
professional brief
```

Requirements remain distinct from observed state:

```text
required
proposed
observed
as_built
```

A requirement can concern an object, a class of objects, a space group, a zone or
a relation. A detected deviation remains a governed candidate requiring review.

### 2.5 Site and operational observations

Site photographs, reports, meeting minutes and manual observations may describe:

```text
work executed
work absent
reserve or defect
temporary condition
access obstruction
material substitution
interface issue
progress or phasing state
```

They must be linked to the relevant stable object, zone or source representation
when the localization is reviewable. An uncertain location remains explicit.

```text
photo timestamp != work acceptance
site observation != as-built canonization
meeting-minute statement != executed fact
```

### 2.6 Derived analyses and hypotheses

Hermes or an adapter may propose:

```text
object kind
spatial correspondence
cross-level identity
relation candidate
quantity candidate
material or assembly candidate
thermal-zone candidate
access or circulation path candidate
source incompatibility
```

These remain derivations with premises, method, limitations and certainty. They do
not overwrite the source or become authoritative automatically.

### 2.7 Doubt, contradiction and missing information

Owner: `PROJECT_UNDERSTANDING.md`.

The Anatomy must expose, not hide:

```text
unknown identity
missing source
unmapped fragment
insufficient calibration
conflicting dimensions
conflicting materials
index mismatch
program/design deviation
planned/observed/as-built conflict
ambiguous location
```

A doubt records what would resolve it and what it blocks. A contradiction retains
all competing claims and their provenance until human qualification.

### 2.8 Human decisions, overrides and use-specific canonization

Owner: existing Decision, approval, `human_override` and canonization contracts.

```text
human correction != source mutation
Decision recorded != APU mutation applied
APU write applied != regulatory conclusion authorized
canonical for internal coordination != canonical for contractual action
```

### 2.9 Operational cross-links

The same APU identity may be referenced by:

```text
Information
ProjectClaim
WorkIssue
Decision Request / Decision
Document fragment or source representation
```

These links do not duplicate the object or transfer its authority.

## 3. Spatial reconstruction is progressive and multi-view

The discussed objective was a three-dimensionally coherent understanding, not an
obligation to generate a complete mesh before the Anatomy becomes useful.

### 3.1 Coordinate and registration frames

The existing APU frames remain authoritative:

```text
PIXEL
PAGE
MODEL_LOCAL
PROJECT
GEO_NGF
```

Every geometric claim must state its frame or explicit absence of frame.
Registration between sources is a reviewed calibration problem.

Examples:

```text
PDF plan page coordinates -> PROJECT frame candidate
section level marks -> vertical calibration witness
IFC local coordinates -> PROJECT frame candidate
Revit model coordinates -> MODEL_LOCAL / PROJECT observation
site photo -> located viewpoint candidate, possibly approximate
```

Divergent witnesses cap the permissible certainty of derived measurements.

### 3.2 Views and occurrences

A plan, section, elevation or detail shows an occurrence of an object, not a new
object. Cross-source and cross-level matching must preserve:

```text
source_ref
source version / professional index
view or sheet identity
fragment or element locator
match axis
match rationale
certainty
review status
```

Cross-level identity is necessary for stairs, shafts, ducts, curtain walls,
duplexes and other objects spanning levels.

### 3.3 Geometry and topology remain distinct

The Anatomy may know a useful topology before it knows exact geometry:

```text
contained in
adjacent to
opens to
connected to
above / below
crosses
serves
belongs to zone or system
```

Exact geometry, topology and professional attributes must not be collapsed into
one confidence field.

```text
topological relation known != geometry fully reconstructed
geometry aligned != object identity confirmed
object identity confirmed != all attributes valid
```

### 3.4 Progressive visual lenses

The same server-owned identities may later support:

```text
hierarchical tree
2D plan overlay
section/elevation overlay
photo-to-zone or photo-to-object links
IFC viewer selection
Revit selection link
3D navigation
change or index comparison
```

No viewer becomes a parallel authority or stores its own business truth.

## 4. Source-specific knowledge expectations

### 4.1 Plans, sections, elevations and details

The system must preserve the distinction between:

```text
plan position and containment
section/elevation height and vertical continuity
detail assembly or interface intent
annotation and dimension claims
revision/index context
```

Technical details may refer to several objects and one interface. They must not be
forced into a single-room or single-element attachment.

### 4.2 CCTP and DPGF

Textual documents can contribute:

```text
requirements
materials and layer descriptions
performance targets
lot or work-package references
quantities or pricing-support references
execution constraints
interface responsibilities
```

CCTP or DPGF fragments may concern objects, groups, zones, systems or classes of
objects. They remain source-backed requirements or values, not direct object
mutation.

### 4.3 Site photographs

A photograph may carry:

```text
capture time
source and author
project phase
viewpoint or zone candidate
visible object candidates
observation candidates
occlusion and localization limitations
```

A photo may corroborate or contradict another source while remaining insufficient
to prove hidden geometry, dimensions or contractual acceptance.

### 4.4 IFC and Revit

IFC and Revit are high-density representations, not the Pantheon ontology.

They may provide:

```text
object candidates
levels and spaces
geometry and topology
parameters and classifications
systems and host relations
phase/design-option observations
source identifiers and model version
```

Source-native ids remain aliases or evidence for matching. Optional adapters may
be disabled without losing authoritative APU data already reviewed and persisted.

## 5. First professional wave

The first useful wave is deliberately architecture-led. It includes conception,
economy, site/DET, thermal/RE2020 and environmental/ACV use cases because they
share the same stable project objects and source provenance.

Detailed structural engineering and detailed MEP/CVC engineering are not required
for the first wave. Structural and technical systems may appear at architectural
coordination and interface level without Pantheon pretending to replace the BET.

### 5.1 Architectural design

The Anatomy should support:

```text
program and space organization
areas and dimensions
circulation and accessibility paths
levels, zones and functional groups
openings and interfaces
existing / demolition / projected states
variant and index comparison
```

### 5.2 Economy and quantities

The shared object structure should allow sourced quantities to be attached to the
objects or groups they measure:

```text
areas
lengths
counts
volumes
materials and layers
lot/work-package references
DPGF/CCTP source links
```

Cost, amount, budget and contractual adoption remain ProjectClaim or other
reviewed business-value responsibilities. Anatomy supplies the object and quantity
context; it does not become an accounting or estimating authority.

```text
APU quantity != accepted DPGF quantity
quantity x unit price != approved budget
object linked to lot != enterprise commitment
```

### 5.3 Site and DET

The Anatomy should locate and historize:

```text
site observations
photos
reserves and defects
work zones
temporary states
implemented substitutions
as-built observations
related WorkIssues and Decisions
```

A reserve remains a WorkIssue or governed project record linked to an APU object;
it does not become an object status hidden inside the graph.

### 5.4 Thermal and RE2020

The same objects may carry or reference sourced candidates for:

```text
thermal envelope boundaries
openings
areas and orientations
thermal zones
materials and layer compositions
system-level architectural interfaces
calculation assumptions
calculation result references
```

A regulatory or compliance conclusion requires its governed use and human gate.
The Anatomy provides the project structure and inputs; it does not replace an
approved RE2020 calculation engine or professional validation.

```text
thermal property candidate != validated calculation input
calculation success != RE2020 compliance decision
```

### 5.5 Environmental and ACV/carbon

The shared object/material structure may support source-backed references to:

```text
material and product identity candidates
quantities and units
service-life or scenario assumptions
FDES / PEP or environmental-source references
environmental indicator candidates
replacement and demolition scenarios
calculation result references
```

Environmental data, product matching and carbon results preserve source version,
applicability, assumptions and uncertainty. A calculated result does not become a
validated project conclusion automatically.

```text
product candidate matched != product specified
FDES referenced != FDES applicable
carbon result computed != ACV approved
```

## 6. Technical assemblies and interfaces

Our discussions included CCTP details, sections and constructive interfaces. They
must not disappear merely because the first executable slice starts with existing
stable objects.

The existing belief contract already identifies later extensions:

```text
technical_assembly
interface_detail
issue_coordination
```

These remain extensions after the core spatial graph proves itself. Until their
reviewed contracts exist, the implementation must preserve enough structure to
avoid a dead end:

```text
object groups
property sets and materials
qualified APU relations
source-fragment links
notes and analysis-context candidates
Information / WorkIssue / Decision cross-links
```

Examples of future interface understanding include:

```text
wall / slab / façade junction
opening and host relation
waterproofing continuity
thermal bridge context
rainwater path
reservation or penetration
existing/new connection
maintenance access
```

A technical assembly or interface candidate remains separate from compliance,
execution acceptance and professional visa.

## 7. Time, index, phase and validity

The Anatomy must preserve three independent time axes already defined by APU:

```text
documentary time
- drawing/model/document indices and versions

project and phase time
- existing, demolition, proposed, construction, temporary, as-built

claim-validity time
- when one object attribute or interpretation was applicable
```

A stable object may persist while representations, names, properties and phase
states change.

```text
not present in index B != demolished
shown in PRO != executed
observed on site != valid for all later indices
same source id across versions != same reviewed object automatically
```

Variant, document revision, professional index, phase state and claim validity
remain distinct.

## 8. Required Revit Context Pack

A future Revit observation task must carry a sufficiently rich and fresh Context
Pack. An active document name alone is insufficient.

Minimum reviewed context for a read task should include, when applicable:

```text
Pantheon Project reference
Revit document/model identity
binding and Revit version
model fingerprint, digest or freshness token
active view identity, type and discipline
selected elements or explicit work area
levels
views and sheets relevant to the task
rooms / spaces and their source identifiers
phases and phase filters
design options
worksets and ownership observations
linked Revit, IFC and CAD references
categories and requested element classes
coordinate/base-point observations
requested source version or professional index
exact Task Contract and Context Pack scope
```

For a write, the stricter preflight in `REVIT_LOCAL_ADAPTER.md` also applies.

```text
model open != correct model
active view != complete task scope
fresh Context Pack != task authorization
ElementId resolved != stable identity confirmed
```

## 9. Professional questions the projection must answer

A useful Anatomy should eventually answer, with provenance and uncertainty:

```text
What exists in this project and where?
Which rooms, zones, elements and systems belong together?
Which objects span several levels or sources?
Which plan, section, detail, photo, IFC or Revit element supports this statement?
Which CCTP requirement or DPGF line concerns this object or group?
What changed between two indices or observations?
What is required, proposed, observed or as-built?
Which dimensions, materials or quantities conflict?
Which fragments remain unmapped?
Which site observation or reserve concerns this location?
Which WorkIssues and Decisions are linked without being duplicated?
Which thermal or carbon assumptions concern this object?
What is known, what is derived, what is missing and what must be arbitrated?
```

The answer surface must expose limitations instead of compressing them into one
opaque confidence number.

## 10. Candidate output families

The earlier discussions used a practical set of candidate outputs. They remain
presentation and routing categories over existing owners, not new canonical
entities:

```text
Spatial candidate
- location, hierarchy, zone, geometry or topological relation.

Element candidate
- stable-object kind, identity match, material, property or assembly reading.

Requirement candidate
- program, CCTP, regulatory or approved-intent requirement.

Observation candidate
- drawing/model/site/photo observation with time and provenance.

Contradiction candidate
- competing sourced claims requiring qualification.

Missing-information candidate
- absent source, unresolved identity, insufficient calibration or required question.
```

They should be carried through the existing Result Candidate, APU mapping,
ProjectClaim, Information, doubt, contradiction, WorkIssue and Decision owners as
appropriate.

```text
candidate-family label != new persistence owner
```

## 11. Consequences for the H implementation sequence

The H sequence in `PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md` remains valid,
but each step must preserve the recovered structure.

### H1 read owner

Must support stable objects, domain relations, source representations, phase/time
posture and provenance-bearing claims. It need not implement every professional
extension immediately.

### H2 match application

Must attach a reviewed source representation or candidate match to an existing
object without flattening its source, index, view, fragment or match axis.

### H3 cross-family links

Must allow Information, ProjectClaim, WorkIssue and Decision to concern an APU
object without copying their lifecycle into APU.

### H4 projection

Should expose, progressively:

```text
structure and hierarchy
source representations
relations and paths
properties / quantities / materials
requirements and observations
phases, indices and variants
coverage and provenance
doubts, contradictions and missing information
linked work and decisions
```

### H5 validation

Representative validation must not stop at one room-from-PDF example. The staged
set should cover:

```text
plan + section identity continuity
CCTP requirement linked to an object or group
site photo/observation linked with explicit localization limits
IFC or Revit representation matched to an existing object
quantity/material candidate supporting economy use
thermal or carbon input with preserved assumptions
multi-index or multi-source contradiction
human correction without source mutation
```

## 12. Non-goals and boundaries

This annex does not authorize:

```text
full automatic 3D reconstruction
a geometry engine inside Pantheon
IFC or Revit as canonical project authority
a detailed structural or MEP engineering model in the first wave
a cost-estimating or accounting authority
a RE2020 or ACV calculation engine inside Pantheon
automatic compliance conclusions
automatic stable-object creation
automatic cross-source identity confirmation
automatic contradiction resolution
a second evidence, task, decision or relation lifecycle
a runtime memory graph as project truth
```

## 13. Recovery conclusion

The original consolidation retained the main authority and implementation
boundaries, but it under-specified four discussion outcomes:

```text
1. Project Anatomy is a progressive multi-view spatial hypothesis, not only a tree.
2. Knowledge is layered: identity, representations, properties, requirements,
   observations, derivations, doubts and decisions remain distinct.
3. The first professional wave includes architecture, economy, site/DET,
   thermal/RE2020 and environmental/ACV use cases over shared stable objects.
4. A Revit task requires a rich Context Pack, not only an active-model reference.
```

These points are now recorded without changing the owners, schemas or current H
implementation order.
