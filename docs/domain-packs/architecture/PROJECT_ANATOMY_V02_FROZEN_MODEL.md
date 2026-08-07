# Project Anatomy V0.2 — Frozen Conceptual Model

Status: candidate support doctrine — frozen conceptual target, documentation only.
Boundary profile: architecture_project_understanding_projection.
Frozen: 2026-08-07.

This document freezes the conceptual target for Project Anatomy after the V0.2 schema refactor merged on `main` at `98be3a1dd07be6b6ee2847127d698618f6ff703a`.

It does **not** claim that all mechanisms described below are implemented. The four V0.2 core schemas are implemented at contract/validation level; Revision Sets, Profiles, Observation Bundles, semantic lenses and Proof integration remain documented non-implemented until their own reviewed slices land.

When this document conflicts with an active reviewed schema, the schema prevails. When it conflicts with older candidate support notes describing V0.1 carriers or pre-H4 implementation state, this document is the current conceptual target for post-V0.2 work.

## 1. Frozen core

Project Anatomy keeps exactly four project-world primitives:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

Prescriptive intent remains separate through:

```text
requirement
```

Supporting provenance such as `derivation` is not a fifth project-world primitive.

```text
stable_object != source occurrence
source_representation != project truth
attribute_claim != ProjectClaim
relation_claim != generic Pantheon graph edge
requirement != observed fact
projection != authority
```

A new core primitive requires a separate architecture decision demonstrating that the need cannot be represented by the existing four primitives plus profiles, provenance, requirements and governance records.

## 2. Stable identity

`stable_object` is durable Project identity and nomenclature only.

It must not become a copy of Revit, IFC, a DPGF row, a thermal object or a carbon object. Source-native identifiers, detailed classifications, geometry, quantities, prices, proof state and approval state do not belong in the identity carrier.

Objects are normally retained through lifecycle transitions instead of destructive deletion.

Typical identity lifecycle relations are expressed as governed relation claims, for example:

```text
identity.replaced_by
identity.split_into
identity.merged_into
identity.supersedes
```

Retirement, replacement, split or merge must preserve historical references.

## 3. No canonical BIM kind taxonomy

The V0.2 target does not introduce a growing canonical `kind` taxonomy on `stable_object`.

Detailed semantics are provided through versioned classifications and predicates owned by profiles. Structural facets may be derived and indexed for query/performance, but a derived semantic index is rebuildable projection state, not Project Anatomy authority.

Examples:

```text
architecture.class = window
ifc.class = IfcWindow
revit.category = OST_Windows
thermal.class = exterior_opening
economy.class = exterior_joinery
```

```text
classification != identity
Revit category != Pantheon object kind
IFC entity != Pantheon object kind
```

## 4. Profiles and registries

Extensibility comes from versioned profiles rather than arbitrary JSON fields or new core primitives.

Candidate profiles include:

```text
architecture@1
revit@2027
ifc@4.3
ids@1
economy@1
construction@1
re2020@1
carbon@1
```

A profile may define:

```text
predicate vocabulary
relation vocabulary
classification schemes
value schemas
units and dimensions
endpoint rules
derived structural facets
validation rules
```

Profiles may evolve independently of the V0.2 core.

```text
profile installed != profile admitted
predicate visible != predicate approved
classification proposed != classification retained
```

The intended pattern is a governed Predicate/Relation/Profile Registry. Its exact executable contract is not implemented by this document.

## 5. Revision Sets — documentary Project baselines

A group of coordinated Project files carrying the same professional index and issue date is treated as a `Revision Set` support concept.

A Revision Set represents a declared documentary state of the Project at an instant; it is not a claim that every source in the set agrees and it is not Project truth.

Typical metadata:

```text
revision_set_id
project_ref
professional_index
issued_at
received_at where relevant
artifact refs
coverage
supersedes_revision_set_ref
content digest / manifest
```

Professional indices are opaque business identifiers. Pantheon must not infer ordering from lexical values such as `A < B` or `P1 < P2`; sequence is established explicitly by lineage, dates and reviewed supersession.

```text
same revision index != source agreement
Revision Set != complete dossier
latest Revision Set != universally applicable truth
```

A Revision Set may be incomplete. Later receipt of a missing artifact may enrich the same declared set when the professional issue context is unchanged.

## 6. Source representations

A `source_representation` is one localizable observation in one exact source/version context.

Applicable sources include:

```text
Revit
IFC
PDF plans / sections / elevations / details
OpenTakeoff output
photographs
CCTP / DPGF fragments
meeting minutes / reports / emails
structured databases
manual professional description
```

A source representation may exist before stable identity is resolved.

It should be able to preserve, when applicable:

```text
source / artifact ref
source version or digest
revision_set_ref
native identity
locator
coordinate frame / calibration
observed_at
method / binding / adapter version
coverage
limitations
```

```text
source-native id != stable_object_id
representation observed != stable identity resolved
same label across sources != identity confirmed
```

## 7. Incompleteness and coverage

Incomplete data is normal.

Absence of an attribute claim normally means that Project Anatomy has no retained claim for that predicate; it should not be filled with synthetic `unknown` values merely to make records complete.

Operational states such as:

```text
not_observed
withheld
ambiguous
missing_input
conflicting_sources
```

belong primarily in Observation Bundles, Execution Results, WorkIssues or Decision Requests unless a source explicitly asserts such a fact.

Coverage is required whenever an adapter or analysis intends to interpret absence.

```text
not found != absent
missing from snapshot != deleted Project object
absence of claim != negative claim
```

A source may legitimately cover only one floor, category, phase, discipline, drawing area or task scope.

## 8. Claims are temporal and append-oriented

New observations do not silently rewrite prior claims.

Example:

```text
Revision B -> width = 900 mm
Revision C -> width = 1000 mm
```

Both observations may remain traceable. A later claim may supersede an earlier claim for a specific projection/use without erasing the history.

At minimum the architecture must keep distinct:

```text
source version / revision context
observed_at
effective interval where materially required
```

These are not interchangeable dates.

```text
latest observation != universally current value
superseded != deleted
historical claim != current projection
```

## 9. Multiple Project lenses, no universal `current_value`

Project Anatomy stores claims and relations; consumers calculate purpose-specific projections.

Candidate lenses include:

```text
design-current
architecture
economy
construction / as-built
RE2020
carbon
contractual review
Cockpit
Hermes Context Slice
```

A lens is a projection policy over the same identities and claims. It is not another authority or graph.

```text
accepted for economy != accepted for contractual action
accepted for RE2020 input != professional regulatory approval
Cockpit display != persisted authority
```

## 10. Observation Bundles for Hermes and adapters

Hermes and external adapters should not be coupled directly to PostgreSQL persistence shapes.

The target external seam is an `Observation Bundle` / bounded candidate envelope carrying, as applicable:

```text
project_ref
basis / revision_set_ref
source representations
candidate attribute claims
candidate relation claims
coverage
gaps
withheld items
warnings
method provenance
capability_id
binding_id
adapter/runtime version
```

Pantheon/MVP validates, normalizes, reviews and selectively applies candidates through governed owners.

```text
Hermes output != APU mutation
Observation Bundle valid != candidate accepted
candidate retained != Evidence admitted
runtime success != project truth
```

## 11. Delta-first high-density adapters

High-density sources such as Revit and IFC should support snapshot/delta operation rather than forcing full semantic re-ingestion on every observation.

Typical delta categories:

```text
added source representations
changed source representations
missing source representations
unchanged source representations
```

A missing source occurrence only becomes a retirement/deletion candidate when declared coverage and method semantics make that conclusion supportable.

```text
missing from Revit delta != Project object deleted
new IFC GlobalId != new Pantheon identity automatically
```

## 12. Change Requests are based on explicit baselines

A consequential modification request should normally identify the exact Project baseline it was made against, typically a Revision Set or equivalent reviewed source state.

```text
Change Request
-> base Revision Set
-> target / locator / stable-object candidates
-> requested change
-> dependencies / preconditions
```

If the Project has advanced since the request baseline, Hermes must compare/rebase the request before execution.

Possible operational outcomes include:

```text
clean
conflict
blocked
requires_review
```

A stale baseline does not necessarily block independent actions in the same Task.

```text
request based on Revision C != permission to mutate Revision D blindly
technical rebase possible != modification authorized
```

## 13. Proof and governance remain outside Anatomy

Project Anatomy does not own Evidence admission, Proof, professional approval, Decision, WorkIssue or ProjectClaim authority.

Future Proof should qualify whether claims are sufficiently supported **for a declared purpose, policy, scope and time**, not assert a universal boolean truth.

Conceptually:

```text
Claim
-> Evidence
-> Proof / review policy
-> sufficient for declared use
```

Examples of different uses:

```text
preliminary design
quantity takeoff
RE2020 input
contractual acceptance
regulatory submission
```

```text
supported for one use != supported for every use
Evidence present != Proof conclusion
Proof conclusion != task authorization
```

## 14. Raw source data is not automatically Project Anatomy

Adapters may observe substantially more source data than Pantheon needs to retain as semantic claims.

For example, a Revit model may expose hundreds of thousands of elements and millions of parameter values. This does not imply one canonical `attribute_claim` per raw parameter.

```text
raw observed != canonically retained
source cache != Project authority
adapter index != Project Anatomy
```

Raw snapshots, caches and indexes may use storage optimized for their task while Project Anatomy retains only semantically useful, provenance-bearing Project knowledge.

## 15. Source-specific target flow

The common flow is:

```text
Source
-> exact source state / Revision Set where applicable
-> source representations
-> observation/candidate bundle
-> Hermes orchestration / matching / analysis where useful
-> reviewed attribute/relation candidates
-> governed APU owner
-> Project Anatomy projection
-> purpose-specific lenses
```

Examples:

```text
Revit add-in
-> controlled Context Snapshot / delta
-> source representations + observed candidates
-> no direct stable identity decision

IFC / IfcOpenShell
-> source representations + deterministic facts
-> reviewed identity/classification/relation candidates

PDF / OpenTakeoff
-> source representations + geometry/quantity candidates
-> no direct accepted quantity

photo / site observation
-> source representation + visible-object/location candidates
-> no automatic as-built canonization

user description / professional note
-> source-backed candidate claims or requirements
-> no silent overwrite of existing claims
```

## 16. Frozen invariants

The following distinctions are part of the frozen V0.2 target:

```text
1. source != Project truth
2. source representation != stable object
3. missing != deleted
4. same revision != source agreement
5. attribute/relation claim != ProjectClaim
6. claim != Evidence
7. latest != universally applicable
8. projection != authority
9. accepted for one purpose != accepted for every purpose
10. installed != approved
11. runtime_success != Evidence
12. generated possibility != authorization
```

For Revit specifically:

```text
successful_transaction != governance_approval
Revit UniqueId / ElementId != Pantheon stable identity
binding available != capability authorized
```

## 17. Implementation status and next sequence

Observed repo status at freeze time:

```text
Pantheon-Next V0.2 core schemas       implemented at contract/validation level
Pantheon-Next V0.1 compatibility      implemented at contract/validation/MCP compatibility level
pantheon-mvp H1/H2/H3 owner slices    implemented against the pre-V0.2 executable carrier
H4c V0.2 executable owner migration   not implemented at freeze time
Revision Set contract                 documented non-implemented
Profile/Predicate Registry            documented non-implemented
Observation Bundle contract           documented non-implemented
semantic lens policy                  documented non-implemented
future Proof purpose model            documented non-implemented
Revit production add-in               documented non-implemented
```

The dependency order is frozen as:

```text
V0.2 conceptual target
-> V0.2 schemas + compatibility
-> H4c executable MVP owner preserving H1/H2/H3 history
-> generic Observation Bundle / profile seams where needed
-> external adapters (Revit / IFC / drawing)
-> Cockpit/Hermes projections
-> purpose-specific Proof policies later
```

H4c must not rewrite historical V0.1 rows as though source representation, method, timestamps, coverage or Evidence had always existed.

## 18. Change control

This model is frozen to reduce architectural churn before executable H4c and Revit adapter implementation.

Allowed evolution without reopening the core:

```text
new profile
new registered predicate
new registered relation
new lens
new adapter binding
new source representation locator
new purpose-specific Proof policy
```

Changes that require explicit architecture review:

```text
adding a fifth project-world primitive
putting approval/Evidence/Proof inside APU
making a source-native id authoritative Project identity
adding a generic ungoverned extension bag
making Hermes write APU directly
making one lens own universal current truth
turning Revision Set into Project truth
```

The design goal is not maximal genericity. It is a small stable semantic core with explicit, versioned extension mechanisms and auditable provenance.