# Project Anatomy Implementation Convergence

Status: candidate support roadmap — documentation-only convergence note.
Boundary profile: architecture_project_understanding_projection.
Date: 2026-08-06.

This note consolidates the implementation trajectory for **Project Anatomy**.
It does not create a new Architecture Project Understanding authority, object
model, graph, runtime or Cockpit truth source.

It is subordinate to the existing owners:

```text
PROJECT_OBJECT_MODEL.md
-> owns the architecture-domain object vocabulary and typed relations.

PROJECT_UNDERSTANDING.md
-> owns the belief, provenance, doubt, contradiction, override and canonization contract.

PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
-> owns the external adapter boundary.

ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md
-> owns the product placement of Anatomie du projet.

REVIT_LOCAL_ADAPTER.md
-> owns the Revit execution boundary.
```

Where this note conflicts with one of those owners or with a reviewed schema,
the owner or schema prevails.

## 1. Objective

Turn the already-defined Architecture Project Understanding foundations into one
coherent implementation path without adding another ontology or another project
graph.

The target is:

```text
heterogeneous project sources
-> structured and provenance-bearing candidates
-> reviewed alignment with stable project objects
-> bounded application into one executable APU owner
-> calculated Project Anatomy projection
-> human review and consequential decisions
```

This note concerns tranche H only. It does not implement or alter tranche F
(ProjectClaims and consequential values) or tranche G (variants). Their final
reviewed owners are dependencies consumed by H, not work absorbed here.

## 2. Canonical distinction

```text
Architecture Project Understanding (APU)
= internal authority for project objects, their domain relations and
  provenance-bearing beliefs.

Project Anatomy / Anatomie du projet
= calculated user-facing projection of APU structure, coverage, provenance,
  uncertainty, contradictions and unresolved mappings.
```

Therefore:

```text
Project Anatomy != a second graph store
Project Anatomy != a new visual card family
Project Anatomy != one IFC or Revit model
Project Anatomy != Document Structure
Project Anatomy != Evidence
Project Anatomy != runtime memory
Project Anatomy != client-computed business truth
```

The server remains authoritative. The Cockpit may render several lenses over the
same APU identities, but no lens owns the underlying object, relation, status,
permission or professional conclusion.

## 3. Existing owners retained

### 3.1 Project object vocabulary

`PROJECT_OBJECT_MODEL.md` and the schemas under
`schemas/architecture-project-understanding/` already define the retained
architecture vocabulary, including:

```text
stable_object
spatial_node
object_identity
object_relation
object_group
property_set / property_claim
instance_override
object_note
phase_state
analysis_context_candidate
```

The model already distinguishes a physical containment hierarchy from transversal
zones and typed relations. H must reuse these responsibilities before proposing a
new object kind, relation family or property carrier.

### 3.2 Belief and proof posture

`PROJECT_UNDERSTANDING.md` already owns:

```text
attribute_claim
calibration
derivation
evidence
doubt
contradiction
human_override
canonization per use
```

Anatomy persistence must not absorb the Evidence, Decision, approval or
canonization lifecycles. A project object describes the project world; separate
governed records explain why a claim is supported, doubtful, contradicted,
reviewed or approved for one use.

### 3.3 Adapter boundary

External readers remain adapters:

```text
PDF / image / IFC / Revit / other source reader
-> Result Candidate + Evidence Pack Candidate
-> no direct APU mutation
```

Hermes may orchestrate an admitted adapter task and return candidates. It may not
create stable identity, canonize a belief, admit Evidence or mutate APU authority.

### 3.4 Revit boundary

The Revit add-in remains an external local executor. Revit ElementIds, IFC GUIDs,
room numbers, source labels and model-local ids are source references or matching
material; they are not Pantheon stable identity.

```text
Revit observation != APU object
transaction success != accepted result
model element id != stable project identity
```

## 4. Observed implementation coverage

The current repositories already cover more than a documentation-only APU sketch.
The following path exists in contracts and, for its MVP portions, in executable
candidate code:

```text
Document
-> Document Structure
-> governed fragments
-> Fragment Qualification Candidate
-> Execution Result persistence
-> APU object mapping candidate
-> human mapping review
-> immutable write-command candidate
-> human authorization event
```

The implemented first write-command vocabulary is intentionally limited to:

```text
add_match_to_existing_object
```

The current chain explicitly preserves these distinctions:

```text
fragment detected != project fact
qualification candidate != reviewed classification
mapping candidate != APU object
selected existing object != stable identity confirmed
write command prepared != APU write
write authorized != write applied
```

### 4.1 Present now

```text
Pantheon Next
- APU object and belief schemas;
- shared E0-E4 certainty vocabulary;
- read-only schema validation;
- cross-file referential-integrity checks;
- document-fragment qualification contract;
- candidate mapping contract;
- mapping-review contract;
- write-command and write-authorization contracts;
- Revit and generic adapter boundaries.

pantheon-mvp
- structured document projection and read API;
- Hermes fragment-qualification skill;
- immutable Execution Result persistence;
- deterministic conversion to APU mapping candidates;
- mapping review persistence;
- write-command preparation;
- human authorization persistence.
```

### 4.2 Not established yet

```text
- one executable project-scoped APU persistence owner;
- application of an authorized APU write command;
- creation and lifecycle of stable objects in executable persistence;
- executable APU domain-relation owner;
- Project Anatomy read API;
- Cockpit Project Anatomy projection;
- governed cross-links from Information, WorkIssue, Decision and ProjectClaim;
- real-project PDF / IFC / Revit / photograph / CCTP convergence proof;
- production Revit add-in or adopted adapter binding.
```

The system currently prepares and authorizes a bounded write. It does not yet apply
that write or expose a complete Project Anatomy.

## 5. Source-to-Anatomy path

The retained source path is:

```text
Source
-> optional Document authority
-> Document Structure
-> fragments and locators
-> semantic qualification candidate
-> stable-object mapping candidate
-> human review
-> exact write-command candidate
-> exact human authorization
-> server-side application
-> APU event and revised projection
```

Each stage preserves the source, structure, fragment and candidate references.
No stage may collapse source chronology, document revision, project phase, variant,
certainty or professional approval into one status.

Applicable sources may include:

```text
PDF plans, sections and details
IFC
Revit observations
plan images and sketches
site photographs
CCTP and DPGF
reports and meeting minutes
emails and professional notes
manual professional input
```

A source may support an object or claim without determining its stable identity.
Cross-source identity remains reviewed and auditable.

## 6. First executable owner responsibilities

Before implementing persistence, H must inventory the current APU schemas, MVP
stores, EntityRef resolvers, ProjectClaim backing references and active consumers.
The implementation may use several PostgreSQL tables, but it must expose one
coherent authority boundary.

The first executable APU owner must preserve at least:

```text
project-scoped stable identity
object kind and architecture-domain identity
parent / containment and transversal grouping where applicable
typed APU domain relations
phase state and validity
source aliases and external identifiers
provenance-bearing attribute or property claims
certainty and unresolved doubt / contradiction references
optimistic revision or equivalent conflict control
append-only material-change history
retirement or supersession without destructive history loss
```

It must refuse:

```text
cross-project object references
unknown stable-object references
silent direct runtime writes
unreviewed candidate application
stale command digests or target revisions
automatic Evidence admission
automatic canonization or professional validation
implicit ProjectClaim mutation
```

## 7. First write application

The first applied operation should reuse the existing contract:

```text
add_match_to_existing_object
```

No `create_stable_object` operation is admitted by this convergence note.
Automatic object creation would add a distinct authority responsibility and must be
justified by real-project evidence and a separate reviewed contract.

Application must verify together:

```text
command identity and immutable payload digest
latest human authorization over the exact digest
target Project and stable object existence
source mapping and review identity
selected candidate membership
expected owner revision / freshness
idempotency and prior application posture
```

Successful application records only the bounded match and its provenance.
It does not by itself confirm professional truth, admit Evidence, close a WorkIssue,
resolve a Decision Request or authorize an external effect.

```text
write applied != identity professionally validated
write applied != claim canonized
write applied != Evidence admitted
write applied != WorkIssue done
```

## 8. Relation convergence

Two relation responsibilities must remain separate.

### APU domain relations

Spatial, constructive, technical and functional meanings remain governed by the
APU object model and `object_relation` vocabulary, for example:

```text
contains
part_of
located_in
hosted_by
serves
adjacent_to
connected_to
opens_to
crosses
belongs_to_zone
belongs_to_system
has_phase_state
```

### Cross-family references

`EntityRef`-based links allow other governed objects to concern an APU object:

```text
Information -> APU object
WorkIssue scope -> APU object
Decision Request / Decision -> APU object
ProjectClaim backing reference -> APU object
```

These references do not transfer authority to the generic Information-relation
vocabulary. The current four Information meanings remain:

```text
responds_to
relies_on
supersedes
contradicts
```

```text
generic EntityRef shape != universal semantic relation vocabulary
cross-family reference != APU domain relation
APU relation != Information relation
```

## 9. ProjectClaims and variants boundary

### Tranche F

H may consume a reviewed ProjectClaim backing reference to an APU object when the
APU owner exists. H does not define ProjectClaim value, contradiction,
obsolescence, adoption or consequence rules.

```text
APU object exists != ProjectClaim created
ProjectClaim backed by object != object claim canonized
```

### Tranche G

Variants, revisions, professional indices and phase states remain distinct.
Anatomy must not merge competing variants into one object state without an explicit
governed selection or relation.

The first H slice may project only the current reviewed reference when variant
ownership is not yet available, but it must retain source variant and phase
provenance so later convergence does not require destructive migration.

This note does not freeze F or G internal fields. H begins only after their reviewed
owner contracts are stable enough to consume.

## 10. Decision and Work boundaries

An unresolved ambiguity, requested validation or consequential application uses the
existing Decision Request / Decision path. It does not become an APU proof status or
a graph-node status invented for Anatomy.

A task concerning one or several APU objects remains one `WorkIssue` with explicit
scope links. A projection under an object does not duplicate the WorkIssue.

```text
mapping needs clarification -> Decision Request or bounded review question
human response -> separate Decision record where applicable
Decision recorded != APU command applied
APU object shown in task view != task authorized
same WorkIssue in two Anatomy views != duplicate WorkIssue
```

## 11. Project Anatomy projection

The first Cockpit surface should be read-only and server-calculated. It does not
need a full 3D viewer to be useful.

Minimum useful lenses:

```text
Structure
- project, site, parcel, building, level, zone, space and object hierarchy.

Relations
- selected APU domain relations around one object.

Phases and states
- existing, demolition, projected, modified, temporary and as-built posture.

Coverage and provenance
- supporting sources, fragments, locators and source types.

Uncertainty
- certainty bands, doubts, contradictions and clarification needs.

Unmapped material
- reviewed or pending fragments not yet aligned with stable objects.
```

The Project overview may display a concise Anatomy summary, but the detailed
projection remains a secondary Project view.

The UI may reuse Information visual grammar for compact cards or details. This is a
presentation reuse only:

```text
Anatomy card displayed != Information entity created
projection field visible != field editable
relation visible != relation canonicalized by UI
```

2D overlays, IFC viewers, Revit selection links and 3D navigation are optional later
lenses. They must consume the same server-owned identities and provenance rather
than becoming parallel stores.

## 12. Hermes and adapter behavior

Hermes may:

```text
analyze admitted fragments
propose object kinds or matches
propose APU relation candidates
ask discriminating questions
return limitations and source references
```

Hermes may not:

```text
create or mutate stable APU identity directly
apply an authorized command
canonize a claim or relation
resolve a contradiction
admit Evidence
approve its own result
extend task scope or permissions
```

Adapter success, model agreement and high certainty remain candidate observations.

```text
Hermes relation candidate != APU relation
runtime success != accepted result
retrieved or detected != truth
```

## 13. H implementation sequence

### H0 — current-state inventory

Verify current `main`, active branches and file-path collisions. Inventory:

```text
APU schemas and referential-integrity checks
MVP persistence and composed startup migrations
EntityRef endpoint resolvers
ProjectClaim backing references
WorkIssue scopes
Decision Request links
Information relation owner
Document Structure and Execution Result stores
Cockpit projection definitions
```

Exit: no assumed owner, hidden duplicate or parallel active implementation remains.

### H1 — executable read owner

Implement project-scoped persistence and read projection for an existing reviewed
APU dossier. Preserve stable identities, domain relations, provenance and revision.
Do not add automatic object creation.

Exit: one Project can return a coherent APU structure from server-owned persistence.

### H2 — apply the existing bounded match command

Implement exact application of `add_match_to_existing_object` with digest,
authorization, freshness, idempotency and append-only event checks.

Exit: one reviewed fragment mapping can be applied to one existing stable object
without canonization, Evidence admission or unrelated mutation.

### H3 — governed cross-family links

Open `apu_object` only where the reviewed owner exists and add bounded links from
WorkIssue, Decision and ProjectClaim owners without creating a second graph.

Exit: the same underlying identities appear across projections with no duplicated
business record.

### H4 — Project Anatomy API and Cockpit projection

Expose the calculated hierarchy, relations, coverage, uncertainty and unmapped
material. Keep mutation controls separate from the read projection.

Exit: a user can understand what is known, sourced, uncertain and unresolved about
the project structure.

### H5 — adapter and real-project validation

Validate progressively against representative sources after each relevant slice,
not only after all adapters exist.

Preferred order follows demonstrated need, not technology prestige:

```text
structured PDF / text-backed project document
plan image or photograph where location is reviewable
IFC mapping
Revit local observation
multi-source conflict and index change
```

Exit: at least one real or safely anonymized project proves identity continuity,
provenance retention, contradiction handling and correction without source mutation.

## 14. First vertical acceptance slice

The smallest useful end-to-end proof is:

```text
one Project
-> one existing reviewed APU dossier with one stable object
-> one governed Document Structure
-> one Fragment Qualification Candidate
-> one persisted Execution Result
-> one APU mapping candidate
-> one human mapping review selecting the existing object
-> one immutable add_match_to_existing_object command
-> one exact human authorization
-> one server-side application
-> one read-only Project Anatomy projection showing the new source match
```

The proof must also demonstrate:

```text
stale digest refusal
cross-project refusal
unknown object refusal
idempotent replay
append-only application history
no direct Hermes write
no Evidence admission
no automatic canonization
no WorkIssue or Decision transition inferred
```

## 15. Entry criteria for H

H starts only when:

```text
1. the current repository heads and parallel branches are inspected;
2. the final reviewed F/G owners required by the slice are available;
3. APU schema and referential-integrity checks are green;
4. the executable owner and migration lineage are explicitly identified;
5. no active branch touches the same implementation files without coordination;
6. the first vertical fixture and expected source provenance are defined;
7. rollback and data-migration posture are documented.
```

A mergeable branch, a valid schema or a successful parser is not sufficient.

## 16. Completion criteria

Tranche H is complete when all of the following are verified:

```text
- one executable project-scoped APU authority exists;
- stable objects and APU domain relations retain project scope and provenance;
- the existing authorized match command can be applied safely;
- direct Hermes and adapter writes are impossible;
- cross-family references reuse governed identities;
- Project Anatomy is calculated server-side and exposed read-only in Cockpit;
- hierarchy, relations, phases, sources, uncertainty and unmapped material are visible;
- ProjectClaim, Decision, WorkIssue, Evidence and APU authorities remain distinct;
- optional IFC, Revit or viewer adapters can be disabled without losing APU authority;
- a representative project validates continuity across sources and revisions;
- tests cover conflict, idempotency, append-only history and authority boundaries;
- active documentation, schemas, tests and code agree on implemented status.
```

## 17. Non-goals

This convergence does not authorize:

```text
Pantheon as a BIM runtime or model authoring tool
a mandatory graph database
IFC as the canonical Pantheon data model
full 3D reconstruction before a useful read projection
a universal relation vocabulary
a new Information or Task ontology
a hidden agent loop, scheduler or queue
a provider router or plugin manager
a canonical runtime memory graph
automatic stable-object creation
automatic contradiction resolution
automatic compliance conclusions
automatic Evidence admission or canonization
automatic Revit save, sync, publish or model mutation
```

## 18. Final boundary

```text
Sources describe and support.
Adapters detect and propose.
Hermes may orchestrate and return candidates.
APU owns reviewed project objects and domain relations.
Project Anatomy projects that authority for the user.
Pantheon governs consequential state.
The human decides consequential effects.
```
