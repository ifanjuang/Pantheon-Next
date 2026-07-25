# Pantheon Cockpit V2 — Structured Agency Interface

Status: candidate support doctrine — documented non-implemented product specification; executable foundations exist externally in `pantheon-mvp` PR #65.

Boundary profile: candidate_support_note.

Decision date: 2026-07-24.

## 1. Product statement

Pantheon Cockpit is the user-friendly interface to a structured professional data system shared between the agency and AI-assisted work.

It is not primarily a dashboard and not primarily a generic chat application.

```text
agency records
+ professional sources
+ typed relations
+ governed records
+ AI assistance
        ↓
spatial Card interface
```

The Cockpit makes distributed professional information understandable without collapsing ownership or authority.

```text
OpenWebUI / Cockpit exposes and captures bounded intent.
Hermes Agent performs bounded AI/tool operations externally.
Pantheon Next governs scope, status, evidence, consequential decisions and activation.
External owner systems retain native data authority where declared.
The human decides consequential effects.
```

Mandatory distinctions:

```text
card != source of truth
conversation != authorization
tag != established fact
Document != Evidence
Document != Knowledge
Decision projection != Decision record
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != Evidence
```

## 2. Jurisdiction and owner documents

This document owns the Cockpit V2 product placement, spatial navigation, universal Card anatomy, Context Resolver UX, Tag presentation and cross-space composition.

It does not replace the existing owner documents.

```text
PANTHEON_GRAPH_MODEL.md
  owns the generic node/relation grammar.

CARD_STACK_MODEL.md
  owns Card / Scene / Deck / Constellation semantics.

TRIPARTITE_INTERFACE_SPEC.md
  owns exposure/runtime/governance handoff objects.

DECISION_SURFACE_SPEC.md
  owns formal decision-review specialization.

DOCUMENT_LIFECYCLE_GOVERNANCE.md
  owns document lifecycle semantics.

SKILL_LIFECYCLE.md and capability doctrine
  own capability states and gates.

ROLE_FACETS.md
  owns documentary god/role definitions.

NOTION_AGENCY_DATA_BINDING.md
  owns the optional Notion Agency Data specialization.
```

If this document conflicts with an owner document, the owner document wins.

## 3. Data architecture principle

The Cockpit is not the database owner merely because it displays data.

A useful conceptual decomposition is:

```text
Agency Data
  Projects, People, Organizations, business relations, business facts

Source Systems
  original files, emails, Docs, Sheets, Paperless/NAS records, URLs

Pantheon Governance
  scope, Evidence, gates, formal Decisions, governed relation qualification

Runtime Observations
  Hermes runs, hosts, models, health/update observations

Derived/Search Data
  extraction, chunks, vectors, summaries, indexes
```

Physical co-location in one database does not collapse semantic ownership.

```text
same PostgreSQL != same authority
cached value != current owner value
projection != ownership transfer
```

## 4. Relations before presentation

Cockpit V2 follows the Graph Model principle:

```text
Entity identifies.
Relation qualifies.
Evidence supports or contradicts.
Decision accepts, limits or refuses within scope.
External runtime performs the operation.
Card exposes the result to the user.
```

Strong recurrent business relations should remain typed where appropriate:

```text
ProjectParticipation
CompanyEngagement
DocumentRevision
DocumentRepresentation
TagAssignment
```

Cross-domain governed relations may use the generic relation grammar:

```text
Knowledge --applicable_to--> Project
Evidence --supports-------> assertion / relation
Capability --available_on-> RuntimeHost observation
Decision --applies_to-----> action / relation / resource
```

A Card does not invent a relation because two records are visually near each other.

## 5. Spatial navigation model

The primary horizontal constellation is:

```text
Pantheon ↔ Décisions ↔ Affaires ↔ Connaissances ↔ Outils
```

### 5.1 Horizontal movement

At root depth, left/right moves among the five primary spaces.

At deeper depth, left/right moves only among siblings in the current collection.

Example:

```text
Affaires root
  ↓
Lieurey ↔ Mannevillette ↔ Trouville
```

A project-level horizontal gesture must not silently jump into another primary space.

### 5.2 Vertical movement

```text
swipe up   = descend into the current Card's declared children
swipe down = return to the parent container
```

Motion semantics:

```text
horizontal next/previous
  current and adjacent Cards translate laterally

descend
  current Card rises
  child Card enters from below

ascend
  parent Card enters from above
  motion is not a simple reversal of descend
```

Navigation never means moving or renaming the source record.

### 5.3 Non-touch access

The same navigation must remain available by click, trackpad and keyboard.

Candidate keyboard grammar:

```text
Left / Right  sibling
Up            descend
Down          ascend
Enter         open / flip according to focus
Escape        return / close detail
```

A compact location indicator should keep the user oriented, for example:

```text
Affaires / Lieurey / Documents
```

## 6. Universal Card model

A Card is a stable Cockpit projection of one identifiable governed or owner record.

```text
one entity
many bounded presentations
no identity duplication
```

Universal anatomy:

```text
┌──────────────────────────────────────────────┐
│ TOP LEFT                         TOP RIGHT   │
│ index/version OR container/family mark       │
│                                              │
│ TITLE                                        │
│ summary / principal content                  │
│                                              │
│                                              │
│ family/context mark      tags/status/metrics │
│ BOTTOM LEFT                   BOTTOM RIGHT   │
└──────────────────────────────────────────────┘
```

Minimum projection contract:

```text
card_projection_id
entity_type
entity_id
role: conversation | container | entity
family
front_model
back_model
parent_relation
children relation/query
horizontal collection identity
status projections
tag projections
context rule
source attribution
```

### 6.1 Front and back

```text
front = minimum decision-useful information
back  = detail + provenance + relations + permitted actions
```

They are two faces of the same object.

```text
front != separate record
back != separate record
```

### 6.2 Field versus sub-card

Preserve the existing Card Stack rule:

```text
Field when normal.
Sub-card when it blocks, conflicts, fails, repeats,
is newly proposed, changes scope or requires arbitration.
```

A date, surface or budget is normally a field on Project back, not automatically a separate Card.

## 7. Visual grammar

All Cards share anatomy and indicator positions. Families change skin, not fundamental layout.

### 7.1 Common indicator rail

All circles use the same primitive geometry:

```text
StatusOrb
MetricOrb
TagOrb
```

Their size, spacing and baseline are global tokens. Individual business Cards do not reposition them.

### 7.2 Color semantics

Keep independent visual concepts:

```text
family color    = object family
identity color  = project/resource identity
tag color       = vocabulary item
status color    = current state
```

These colors must not be collapsed into one meaning.

### 7.3 Project

Front:

```text
white background
large Impact-style identity typography
restrained project identity accent
```

Back:

```text
white background
thin project-color keyline
```

Project identity color does not encode truth, risk or approval.

### 7.4 Document / Evidence / Knowledge

Front:

```text
solid family color or approved family skin
```

Back:

```text
white background
family-color border
```

Document, Evidence and Knowledge may share visual grammar while preserving different semantic identity.

### 7.5 Capability

```text
active front   = gradient fill
inactive front = neutral / outlined
back           = white with thick gradient border
```

Visual activation is a projection of owner state, not the activation mechanism.

### 7.6 Motion accessibility

Processing may use a slow pulse ring, not aggressive blinking.

The implementation must respect reduced-motion preferences and expose icon/text semantics in addition to color.

## 8. Context Resolver

The Pantheon conversation input includes a JavaScript Context Resolver.

It is a client interaction/federation layer over bounded owner search providers. It is not the canonical index and not a memory engine.

Namespaces:

```text
_  Affaires / Projects
#  Capabilities
@  People / participants
*  global permitted search
```

Examples:

```text
_LIE       -> Lieurey-prefixed/matching projects
#paper     -> Paperless-related capabilities
@lebre     -> matching people
*charpente -> matching permitted titles, aliases, tags or metadata
```

Search priority should normally be:

```text
stable/exact identity
prefix
label/title
aliases
tags
structured metadata / full text
semantic retrieval only when justified
```

### 8.1 Result contract

```text
entity_id
entity_type
label
secondary_label
icon_key
tags
scope
status
source
matched_field
match_reason
```

Selection is owned by active Context, not by the search result.

```text
search result != selected
suggested != selected
selected != relied upon
relied upon != Evidence
```

### 8.2 Provider federation

Several providers may contribute to one namespace.

Example:

```text
_  Agency Data / Notion provider + another project owner provider
*  Projects + Documents + Knowledge + capabilities + allowed external records
```

One provider registration must not silently replace another.

Provider failure should be visible as an observation without necessarily destroying results from healthy providers.

### 8.3 Scope and security

The browser must not receive third-party provider secrets.

Search authorization and field minimization belong to the bounded owner/connector layer.

A result without stable identity may be displayed as a candidate but should not be committed as a durable context selection until identity is resolved.

## 9. Tag Registry

Tags are reusable structured vocabulary objects, not hard-coded boolean project columns.

Examples:

```text
ABF
ERP
Littoral
Argiles
Rénovation
Neuf
Tertiaire
Zone naturelle
Lotissement
Structure
Contrat
DCE
```

Tag definition candidate:

```text
tag_id
name
description
icon_key
color
aliases
optional category
status/provenance
```

Tag assignment is a relation:

```text
tag_assignment_id
tag_id
entity_type
entity_id
reason
source_ref
assigned_by
status
created_at
```

### 9.1 Tag semantics

```text
tag = retrieval/reasoning hint + user-facing qualification
tag != proof
tag != regulatory conclusion
tag != authorization
```

`ABF` may orient Hermes toward heritage/authorization material; it does not establish the exact regulatory consequence.

### 9.2 Hermes tag behavior

When Hermes creates or materially modifies a card-backed record, it may:

```text
inspect existing applicable tags
reuse an existing tag
propose assignment of an existing tag
propose a new Tag Candidate if no adequate tag exists
use aliases/similarity to avoid duplicate vocabulary
```

New vocabulary is not automatically canonical.

### 9.3 Tag UI

Front:

```text
standardized colored icon circles
```

Back:

```text
[ ABF ] [ ERP ] [ ARGILES ] [ + ]
```

The `+` control searches existing Tags before offering a new Tag Candidate.

The front should cap visible tags and summarize overflow, for example `+3`.

## 10. Level A — Pantheon Card

Pantheon is the cover Card and primary conversational surface.

### 10.1 Front

The principal surface is a dialogue box with Hermes.

The input hosts the Context Resolver and shows selected Context explicitly.

### 10.2 Back

The back projects external-runtime work related to the current user context:

```text
requested/delegated runs
currently running work
waiting-human work
waiting-external work
completed runs
failed/cancelled runs
future runtime-owned time-based observations when such execution exists externally
```

Pantheon only displays these states; it does not own time-based execution.

```text
scheduled projection != Pantheon execution authority
```

## 11. Persistent Hermes Card Assistant

Eligible Cards expose a fixed Hermes question control at the lower-left viewport area above the Card.

The control is presentation only and cannot widen scope.

### 11.1 Card Context Envelope

A question from a Card is bounded to:

```text
root current entity
+ declared governed descendants
+ permitted linked source representations
+ explicit user additions
- explicit exclusions
- unrelated Affaires
- unrelated general Knowledge unless admitted
```

The implementation should converge this envelope with the existing `context_pack` owner contract rather than create a competing context model.

### 11.2 Visible scope

Before send, the assistant should show a compact scope summary, for example:

```text
Lieurey · 34 Documents · 7 Knowledge references · 3 open human-attention items
```

Scope additions/removals remain visible and reversible.

### 11.3 Attached answers

A scoped Hermes answer remains attached to its root Card as a conversation projection.

Suggested retained reference:

```text
card_comment_id
entity_type
entity_id
author_type
question
answer
context_snapshot_ref
source_refs
created_at
status
```

Historical answers are not silently revalidated when descendants or sources change.

The UI should flag answers based on an older Context snapshot.

## 12. Level B — Affaires

### 12.1 B1 category Card

Front:

```text
AFFAIRES
active project count
archived project count
```

Metric circles occupy the standard indicator rail.

Descend opens Project Cards.

### 12.2 B2 Project Card

Front:

```text
project name/code
project business status
address/location
primary client / maîtrise d'ouvrage
selected project Tag icons
```

Back is progressively populated from typed owner relations and facts.

Strong structured relations may include:

```text
address
clients
contacts and participants
parcel references
PLU / PLUi references and zones
```

Extensible ProjectFacts may carry less-stable values such as:

```text
land surface
current project surface
current budget
permit filing date
permit approval date
site opening date
reception date
other dated/typed facts
```

Recommended fact direction:

```text
project_fact_id
project_id
fact_type
value_type
value
unit
source_ref
status/review
valid_from
valid_until
display_order
```

`ProjectFact` must not replace a strong typed owner relation when one exists.

Back also projects applicable Knowledge with distinct relation states:

```text
applicable_candidate
selected
relied_upon
```

### 12.3 B3 Project material Cards

Project material may include Document and Evidence Cards. They retain separate identity even when the visual skin is related.

Document front:

```text
index/version top-left
issuer
title
brief description
selected Tag icons
status/activity icon bottom-right
```

Activity semantics:

```text
processing      -> slow pulse ring
stable state    -> visible ring
not ready       -> icon without ring
```

Animation never changes owner state.

Document back:

```text
title
index
index date
issuer
downloadable source representation
working/editable representation
changes since previous index
requested modifications / issue-like comments
full Tags + add control
replace-source candidate action
change-state candidate action
```

Document identity should separate:

```text
Document
├── DocumentRevision
├── DocumentRepresentation
├── DocumentIssue
├── TagAssignment
└── provenance/source links
```

Status axes remain independent:

```text
document_lifecycle
review_state
activity_state
```

A replacement source must not erase revision history.

## 13. Level C — Décisions

`Décisions` replaces the former generic `Traitement` idea.

It is a cross-object human-attention Scene plus formal Pantheon Decision objects where they exist.

Candidate views:

```text
À rédiger
À compléter
À examiner
À valider
À viser
À transmettre
Questions Hermes
Approbations
Décisions formelles
```

These labels are projections of owner statuses, not a new universal lifecycle.

Example:

```text
Document.review_state = pending
  -> À valider

received Document + requires_human_review
  -> À examiner

Work Issue blocked by a human question
  -> Questions Hermes
```

The underlying record retains identity.

```text
appearance in Décisions != copied record
human attention != formal Decision
Decision Request != Decision
Decision recorded != effect executed
```

A generic internal `HumanAttentionProjection` may be useful for presentation, but it is not a governance Decision record.

## 14. Level D — Connaissances

### 14.1 D1 Connaissances category

Front shows principal family counts through standardized metrics.

Back may show:

```text
processing observations
items requiring review/validation
```

Descend opens family Cards.

### 14.2 D2 family Card

Front:

```text
family name
item count
```

Back:

```text
family metadata
processing observations
review/validation items
```

Descend opens Knowledge Items.

### 14.3 D3 Knowledge Item

Front:

```text
title
brief description
small useful governance/processing indicators
```

Possible separate axes:

```text
activation/review state
origin/source class
indexing observation
chunking observation
```

Technical plumbing should remain secondary to professional usefulness.

Back:

```text
file/title
date
source relation
downloadable representation
summary
provenance/version
full Tags + add control
```

## 15. Level E — Outils

`Outils` should distinguish semantically different container branches.

```text
Outils
├── Capacités
│   ├── Skills
│   ├── Functions
│   ├── Workflows
│   ├── Plugins
│   └── Connecteurs / MCP
├── Postes
├── Modèles
└── Références Pantheon
    └── Rôles
```

### 15.1 Capability type Card

Front:

```text
type title
active/enabled count
known count
```

Back:

```text
currently enabled/active projections
known available/activable candidates
```

### 15.2 Capability Card

Front:

```text
name
version
one-line description
state
update observation
```

Back:

```text
detailed description
source/version
installation status
enablement status
activation scope
governance authorization status
health observation
update observation
dependencies
risks/limitations
rollback/suspend path
```

Consequential state changes remain governed and externally executed.

```text
forged candidate != declared
!= validated
!= admitted
!= installed
!= enabled
!= activated for scope
```

### 15.3 Capability forging

The Outils category back may let the user describe a desired capability to Hermes.

Hermes may propose the appropriate Capability Slot/type. This is a proposal path, not installation or activation.

## 16. Runtime Hosts / Postes and Models

A workstation is not a capability.

RuntimeHost observation candidate:

```text
host_id
hostname
OS
CPU
RAM
GPU
VRAM
Hermes runtime/version observation
last_seen
service observations
health observations
```

Models should retain one identity with host-specific observations rather than duplicate model identity per machine.

```text
ModelResource
  ↑ available_on
RuntimeHostObservation
```

Model distinctions:

```text
discovered != available
available != configured
configured != selected
selected != task-authorized
```

Pantheon displays and qualifies observations; external hosts/runtimes perform discovery and use.

## 17. Pantheon role reference Cards

`Outils → Références Pantheon → Rôles` may expose the role definitions already documented in `ROLE_FACETS.md`.

Examples:

```text
Zeus
Athena
Themis
Mnemosyne
Hermes
Hephaestus
Iris
Hestia
Apollo
Chronos
Ploutos
```

Role Cards may show jurisdiction, facets, expressions, consultations, gates and limits.

```text
documented role != runtime agent
role card != installed capability
role selection != execution authority
```

They expose no install/activate action unless a completely separate executable capability record exists.

## 18. Optional Notion binding

Notion may serve as an optional Agency Data binding for the IFJA pilot.

See `NOTION_AGENCY_DATA_BINDING.md` for the owner map and connector boundary.

Observed pilot mapping:

```text
_Affaires      -> Project
_Personnes     -> Person
_Sociétés      -> Organization
_Intervenants  -> ProjectParticipation / CompanyEngagement projection
_Décisions     -> AgencyDecisionRecord candidate, not Pantheon Governance Decision
```

The first target mode is read-only.

```text
Notion enabled != Cockpit dependency
Notion record != Pantheon governance record
connected != adopted
read permission != write authorization
```

Notion credentials remain outside the browser and outside Pantheon governance artifacts.

## 19. CSS/component architecture

Avoid one CSS component per business object.

Recommended conceptual layers:

```text
tokens
base
card primitive/anatomy/faces
themes/families
tags
states
motion
context
navigation
utilities
```

Core orthogonal selectors:

```text
data-role="container | entity | conversation"
data-family="..."
data-face="front | back"
data-processing="idle | running | blocked | failed"
data-active="true | false"
data-review="..."
```

Subtype such as `skill`, `workflow`, `email` or `sheet` should not normally redefine layout.

Candidate file decomposition:

```text
styles/
├── tokens.css
├── card/
│   ├── primitive.css
│   ├── anatomy.css
│   ├── faces.css
│   ├── families.css
│   ├── states.css
│   └── motion.css
├── tags/
│   ├── tag.css
│   └── tag-picker.css
├── context/
│   ├── resolver.css
│   ├── hermes-dock.css
│   └── card-comments.css
└── navigation/
    └── spatial-stack.css
```

## 20. JavaScript/module direction

Candidate decomposition:

```text
structured_interface.js
context_resolver.js
card_renderer.js
spatial_navigation.js
card_context.js
tag_registry.js
hermes_dock.js
optional owner bindings such as notion_agency_binding.js
```

These modules remain presentation/interaction code. They do not become canonical databases, approval engines, external connector runtimes or Hermes runtime components.

## 21. Data-model direction

Conceptual records visible through Cockpit may include:

```text
Project / Affaire
Person
Organization
ProjectParticipation
CompanyEngagement
ProjectFact
Document
DocumentRevision
DocumentRepresentation
DocumentIssue
Evidence
Knowledge
Tag
TagAssignment
WorkIssue
DecisionRequest
Decision
CapabilityRecord
RuntimeHostObservation
RuntimeModelObservation
CardComment
AgencyDecisionRecord when an external agency owner provides one
```

The list is a presentation/data-integration direction, not authorization to create one new table per item.

Relations should preserve one identity / many bounded projections.

## 22. Implementation sequence

Recommended sequence after the V2 foundation:

```text
1. universal Card primitive + front/back anatomy
2. standardized indicator rail
3. spatial navigation engine + keyboard/click parity
4. Context Resolver visible UI
5. optional live Agency Data read binding pilot (Notion)
6. Tag Registry owner API + picker
7. real Project / Person / Organization / Participation Cards
8. Document revision/representation/issues Cards
9. Décisions human-attention projection
10. Knowledge hierarchy
11. Outils capability hierarchy
12. RuntimeHost/model observations
13. role-reference Cards
14. scoped Hermes Card Assistant + attached answers
```

UI scaffolding, owner persistence and consequential external effects remain separate implementation concerns.

## 23. Status matrix

```text
five-space product concept                 documented / refined
spatial navigation                         documented non-implemented
universal Card V2 grammar                  documented non-implemented
Context Resolver contract                  documented; executable foundation in pantheon-mvp #65
Context Resolver provider federation       executable candidate in pantheon-mvp #65
Tag Registry / TagAssignment               documented non-implemented
ProjectFact direction                      documented non-implemented
optional Notion Agency Data binding        documented; read-only JS seam in pantheon-mvp #65
live Notion connector                      not connected
Document revision/representation/issues    partially exists elsewhere / V2 integration pending
Décisions human-attention projection       documented non-implemented
Knowledge V2 hierarchy                     documented non-implemented
capability lifecycle backend               implemented externally in pantheon-mvp
RuntimeHost/model observations             documented non-implemented
role facets                                already documented candidate; UI projection pending
scoped Hermes Card Assistant               documented non-implemented
```

## 24. Forbidden collapses

```text
user-friendly UI != flattened semantics
tagging != proof
search != context admission
card comment != canonical Knowledge
Hermes answer != professional validation
runtime host observed != healthy/safe
model discovered != task-authorized
role reference != agent
Document view in Décisions != Decision record
card status animation != owner status change
Notion record != Pantheon governance record
AgencyDecisionRecord != PantheonGovernanceDecision
```

The Cockpit may make the system simple to use; it must not make consequential distinctions disappear.