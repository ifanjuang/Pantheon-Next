# Pantheon Cockpit V2 — Structured Agency Interface

Status: candidate support doctrine — documented non-implemented.

Boundary profile: candidate_support_note.

Decision date: 2026-07-24.

## 1. Product statement

Pantheon Cockpit is the user-friendly interface to a structured professional data system shared between the agency and AI-assisted work.

It is not primarily a dashboard and not primarily a chat application.

```text
agency records + professional sources + governed relations + AI assistance
                              ↓
                         Card interface
```

The Cockpit exposes structured records, relationships, statuses and scoped AI assistance without turning Pantheon into the runtime that stores every file, executes every tool, schedules work or approves professional consequences.

```text
Pantheon Next governs.
Hermes executes bounded AI/tool operations.
OpenWebUI/Cockpit exposes structured records and captures bounded intent.
External owner systems retain their native data/runtime authority.
The human decides consequential effects.
```

Core distinctions remain mandatory:

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

## 2. Spatial navigation model

The Cockpit uses one universal card grammar and a spatial navigation model rather than a conventional page/menu hierarchy.

### Horizontal axis — primary spaces

```text
Pantheon ↔ Décisions ↔ Affaires ↔ Connaissances ↔ Outils
```

Left/right swipe changes sibling primary space or sibling card at the same depth.

### Vertical axis — hierarchy

```text
swipe up   = descend into the current card's governed children
swipe down = return to the parent level
```

Motion semantics:

```text
horizontal next/previous
  both cards translate laterally

descend / swipe up
  current card moves upward
  child card enters from below

ascend / swipe down
  current card does not simply reverse the previous animation
  parent card enters from above, expressing return to the containing level
```

Navigation is a projection over stable record identities. A swipe never implies moving, copying, renaming or re-owning the underlying source.

## 3. Universal Card model

Every visible professional object uses the same structural anatomy.

```text
┌──────────────────────────────────────────────┐
│ TOP LEFT                         TOP RIGHT   │
│ index/version OR container mark              │
│                                              │
│ TITLE                                        │
│ summary / principal content                  │
│                                              │
│                                              │
│ family/context mark      tags/status/metrics │
│ BOTTOM LEFT                   BOTTOM RIGHT   │
└──────────────────────────────────────────────┘
```

A Card has at minimum:

```text
card_projection_id
entity_type
entity_id
role: container | entity | conversation
family
front_model
back_model
parent_relation
children_query or declared child relation
horizontal collection identity
status projections
tag projections
context envelope rule
```

A Card is a projection, never the owner database by itself.

### Front / back

Front presents the minimum decision-useful information.

Back presents detail, source relations, provenance, editable bounded metadata and permitted actions.

```text
front != separate record
back != separate record
```

## 4. Context Resolver

The Pantheon conversation input includes a JavaScript Context Resolver.

The resolver is a client-side interaction layer over owner search/query APIs; it is not the canonical search index or a memory engine.

Namespaces:

```text
_  Affaires / Projects
#  Capabilities: skills, functions, workflows, plugins, connectors, MCP entries
@  People / participants
*  global indexed search across permitted card information
```

Examples:

```text
_LIE       -> projects whose searchable identity begins with or matches Lie...
#paper     -> Paperless-related skills/functions/connectors
@lebre     -> people matching Le Breton / Lebre...
*charpente -> permitted matches in title, description, aliases, tags and indexed metadata
```

The resolver may search:

```text
display title
aliases
description
tags
structured project facts
document metadata
Knowledge metadata
person identity fields
capability descriptions
```

Every result returns a normalized projection such as:

```text
entity_id
entity_type
label
secondary_label
icon_key
tags
scope
status
selected
```

Non-equivalence:

```text
search result != selected context
suggested != selected
selected != relied upon
relied upon != Evidence
```

The namespace registry must be extensible without rewriting the conversation component.

## 5. Tag Registry

Tags are reusable structured objects, not hard-coded boolean project columns.

Typical examples:

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

A Tag definition includes:

```text
tag_id
name
description
icon_key
color
aliases
optional category
review/status metadata
```

Tag assignment is a separate relation:

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

Tags may apply to Projects, Documents, Knowledge, capabilities and other compatible entities.

### Tag creation/use by Hermes

When Hermes creates or materially modifies a card-backed record, it should:

```text
1. inspect existing tags relevant to the object;
2. reuse an existing tag when semantically appropriate;
3. add an existing tag when allowed by the owner workflow;
4. propose a new Tag Candidate when no adequate tag exists;
5. avoid duplicate vocabulary through aliases and similarity checks.
```

A new tag proposed by Hermes is not automatically canonical.

```text
tag = retrieval/reasoning hint and user-facing qualification
tag != proof
tag != regulatory conclusion
tag != authorization
```

### Tag UI

Front:

```text
icons in standardized colored circles
```

Back:

```text
[ ABF ] [ ERP ] [ ARGILES ] [ + ]
```

The `+` control searches existing tags first and only then offers a governed new-tag proposal.

## 6. Level A — Pantheon Card

Pantheon is the cover page and primary working card.

### Front

The principal surface is a dialogue box with Hermes.

The conversation input hosts the Context Resolver and can select/search `_`, `#`, `@`, `*` entities.

The active context must remain visible and reversible.

### Back

The back projects Hermes/runtime work related to the current user context:

```text
requested/delegated runs
currently running work
waiting-human work
waiting-external work
completed runs
failed/cancelled runs
future runtime-owned scheduled observations when a scheduler exists externally
```

Pantheon does not become the scheduler.

```text
scheduled projection != Pantheon scheduling authority
```

## 7. Persistent Hermes Card Assistant

Every eligible card has access to a fixed Hermes question control anchored at the lower-left viewport area above the card.

The fixed button is presentation only. It does not widen scope.

On activation it opens a compact dialogue + send surface.

### Context rule

A question from a card is bounded to a Card Context Envelope:

```text
root current entity
+ declared governed descendants
+ explicitly linked source representations permitted for that entity
+ explicit user additions
- unrelated Affaires
- unrelated general Knowledge unless explicitly admitted
```

Examples:

Project Card:

```text
Project
├── project facts and tags
├── participants
├── project documents
├── project Evidence links
├── project Knowledge
├── project Decisions / Work Issues
└── declared descendants
```

Document Card:

```text
Document
├── revisions
├── representations
├── extraction/chunks
├── tags
├── comments/issues
└── linked Evidence candidates/records
```

Knowledge Card:

```text
Knowledge
├── source relations
├── versions
├── chunks
├── vector/index observations
└── declared descendants
```

Cross-scope additions must remain explicit.

### Attached answers

Hermes answers from the fixed assistant are attached to the card as scoped conversation projections, with a snapshot of the context used.

A compact answer/comment button appears above the fixed Hermes button.

Suggested record shape:

```text
card_comment_id
entity_type
entity_id
author_type: human | hermes
question
answer
context_snapshot_ref
source_refs
created_at
status
```

A historical answer is not silently revalidated after descendants change.

## 8. Level B — Affaires

### B1 category card

Front:

```text
AFFAIRES
active project count
archived project count
```

Counts are displayed in standardized colored metric circles.

Swipe up opens the first Project Card; horizontal swipe browses projects.

### B2 Project Card

Front:

```text
project name
project status
address
primary client / maîtrise d'ouvrage
selected project tags as icon circles
```

Project tags are free, extensible and registry-backed: ABF, ERP, Littoral, Argiles, Rénovation, Neuf, etc.

Project front is white with large Impact-style typography. Project identity color is an accent, not a truth/risk/status code.

Back:

The back is progressively populated rather than constrained to a fixed visual list.

Core structured relations:

```text
address
clients
contacts and participants
parcel references
PLU/PLUi references and zones
```

Typed project facts may include:

```text
land surface
current project surface
current budget
permit filing date
permit approval date
site opening date
reception date
other future dated or typed facts
```

Suggested extensible fact record:

```text
project_fact_id
project_id
fact_type
label
value
unit
date_value
source_ref
status
valid_from
valid_to
display_order
```

This extensibility must not replace strong typed owner relations where they exist.

The Project back also shows applicable Knowledge projections as colored Knowledge references.

Knowledge applicability states should remain distinguishable:

```text
applicable_candidate
selected
relied_upon
```

Swipe left/right browses Projects.

Swipe up opens project Documents/Evidence material cards.

### B3 Project Document / Evidence material

Document and Evidence retain different semantic identities but may share the same visual card grammar.

Front Document information:

```text
index/version in bold Impact-style top-left
issuer
card title
brief description
selected tag icons
status/activity icon at bottom-right
```

Visual activity semantics:

```text
active processing -> slow pulse ring
stable active/final state -> visible ring
not ready/not activated -> icon without ring
```

Animation is not a status authority.

Back Document information:

```text
title
index
index date
issuer
downloadable source representation
working/editable document representation
changes since previous index
open requested modifications / issue-like comments
tags with + control
replace-source candidate action
change-state candidate action
```

Document representations may include:

```text
email received
email sent
PDF
Markdown
Google Doc
Google Sheet
Excel workbook
local file
Canvas link
URL / web source
other owner-system representation
```

Suggested separation:

```text
Document identity
├── DocumentRevision
├── DocumentRepresentation
├── DocumentIssue / requested modification
├── TagAssignment
└── source/provenance links
```

Recommended independent status axes:

```text
document_lifecycle: draft | working | transmitted | received | closed | archived ...
review_state: none | pending | approved | rejected ...
activity_state: idle | running | blocked | failed ...
```

Do not force all these meanings into one enum.

Evidence remains a separate governed object/record when proof status is actually established.

## 9. Level C — Décisions

Décisions replaces the former notion of a generic `Traitement` space.

It is a cross-Affaire classification/projection of existing records based on what requires human attention, plus actual Pantheon Decision Requests/Decisions.

Possible views include:

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

These are projections over owner statuses and may not create a second lifecycle vocabulary.

Examples:

```text
Document.review_state = pending
→ appears in À valider

received Document + requires_human_review
→ appears in À examiner

Work Issue blocked by a human question
→ Decision Request appears in Questions Hermes
```

The source object keeps its identity.

```text
appearance in Décisions != copied record
human-attention projection != formal Decision
Decision Request != Decision
Decision recorded != effect executed
```

## 10. Level D — Connaissances

### D1 category card

Front shows total Knowledge/document counts by principal family through standardized metric circles or compact metrics.

Back shows:

```text
Knowledge processing/runs observations
items requiring review/validation
```

Swipe up opens family cards.

### D2 Knowledge family card

Front:

```text
family name
total item count
```

Back:

```text
processing/runs observations
review/validation requests
family metadata
```

Swipe up opens Knowledge Items.

### D3 Knowledge Item

Front:

```text
title
brief description
processing/governance observations as standardized icon circles
```

Candidate axes include:

```text
activation/review state
origin/source class
chunking observation
vector/index observation
```

These axes remain separate in data even when compressed into icons.

Back:

```text
file/title
date
source relation
downloadable PDF/Markdown representation
summary
provenance/version
full tags + add tag control
```

Knowledge item visual grammar matches Document/Evidence family grammar where appropriate, but Knowledge retains its own semantic family and scope.

## 11. Level E — Outils

### E1 category card

Front exposes counts in standardized circles:

```text
Skills
Functions
Workflows
Plugins
additional supported capability families
```

Back offers a Hermes capability-forging prompt.

The user may describe a desired capability; Hermes may propose whether the correct Capability Slot is a Skill, Function, Workflow, Plugin, Connector, MCP binding or another supported type.

```text
forged candidate != declared
!= validated
!= admitted
!= installed
!= enabled
!= activated for scope
```

Swipe up opens capability-type cards.

### E2 capability type

Front:

```text
SKILLS / FUNCTIONS / WORKFLOWS / ...
active count / total known count
```

Back:

```text
currently enabled/active projections
known activable/available candidates
```

Swipe up opens individual capability cards.

### E3 capability card

Front:

```text
name
version
one-line description
state
update-available observation
```

Active/selected capabilities may use gradient-filled fronts; inactive entries use the neutral/outlined state defined by the card skin system.

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
risk/limitations
rollback/suspend path
```

Bottom action may propose enable/disable/suspend depending on actual lifecycle state. Consequential effects route through Pantheon gates and a human Decision before native execution.

## 12. Runtime Hosts / Postes

`Outils` also contains registered/observed workstation/runtime-host cards.

A workstation is not a capability and is not a Pantheon runtime.

Suggested RuntimeHost observation:

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

A host card may expose models observed on that host.

Model distinctions:

```text
discovered != available
available != configured
configured != selected
selected != authorized for a task/scope
```

Pantheon displays and qualifies observations; the external runtime/host owner performs discovery and execution.

## 13. Pantheon god/role documentation cards

`Outils` may also expose the architecture-domain god/role definitions already documented in `docs/domain-packs/architecture/ROLE_FACETS.md`.

These are documentation/reference cards only.

Examples include:

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

Role Cards may show jurisdiction, facets, typical expressions, consultations, gates and limits.

```text
documented role != runtime agent
role card != installed capability
role selection != execution authority
```

They must not expose install/activate controls unless a distinct executable capability record exists and is governed separately.

## 14. CSS/component architecture

The visual implementation should avoid one CSS component per business entity.

Recommended layers:

```text
@layer tokens;
@layer base;
@layer card;
@layer themes;
@layer tags;
@layer states;
@layer motion;
@layer context;
@layer utilities;
```

Recommended file hierarchy:

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

Core selectors should be orthogonal:

```text
data-role="container | entity | conversation"
data-family="project | document | evidence | knowledge | capability | decision | runtime-host | role-reference"
data-face="front | back"
data-processing="idle | running | blocked | failed"
data-active="true | false"
data-review="..."
```

Subtype (`skill`, `workflow`, `email`, `sheet`, etc.) should not normally redefine layout.

### Standard indicator system

All icon/number circles share one primitive size, alignment and spacing.

```text
StatusOrb
MetricOrb
Property/TagOrb
```

The common indicator rail is fixed in the card anatomy rather than positioned independently by each card type.

### Visual family rules

Project:

```text
front: white, large Impact-style identity text, restrained project accent
back: white with ~1px project-color keyline
```

Document / Evidence / Knowledge:

```text
front: solid family color or family-specific governed skin
back: white with family-color border
```

Capability:

```text
front active: gradient fill
front inactive: neutral/outlined presentation
back: white with ~5px gradient border
```

Container cards remain simpler and use the family/container mark top-left instead of an index.

## 15. JavaScript modules

The implementation should progressively decompose the current large information-architecture renderer into reusable modules:

```text
card_renderer.js
spatial_navigation.js
context_resolver.js
card_context.js
tag_registry.js
hermes_dock.js
```

These modules are cockpit presentation/interaction code. They do not become canonical databases, approval engines, search engines or Hermes runtime components.

## 16. Data model direction

The Cockpit V2 should be driven by structured owner records and relations rather than page-specific JSON.

Key conceptual records:

```text
Project / Affaire
Person
Organization
ProjectParticipation / CompanyEngagement
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
CardComment / scoped Hermes answer projection
```

Relations should preserve one identity / many projections.

The data model may be implemented incrementally. This document does not by itself authorize database migrations.

## 17. Implementation sequence

Recommended implementation order:

```text
1. universal Card primitive + front/back + standardized indicator rail
2. spatial navigation engine
3. Context Resolver JS with _/#/@/* registry
4. Tag projection + tag picker against a bounded registry API
5. Project Card + ProjectFact/Tag projection
6. Document revision/representation/issues card contract
7. Décisions cross-object filtered projection
8. Knowledge hierarchy/card skin
9. Outils capability hierarchy
10. RuntimeHost/model observation cards
11. documented role-reference cards
12. scoped Hermes fixed dock + attached answer projections
```

The order deliberately separates UI scaffolding from owner database migrations and consequential runtime mutations.

## 18. Status matrix

```text
five-space product concept                    documented previously / refined here
spatial swipe navigation                      documented non-implemented
universal Card V2 grammar                     documented non-implemented
Context Resolver _/#/@/*                      documented non-implemented
Tag registry/assignment model                 documented non-implemented
ProjectFact extensibility                     documented non-implemented
Document revision/representation/issues model partially exists across current document contracts / V2 integration to implement
Décisions cross-object projection             documented non-implemented
Knowledge V2 visual hierarchy                 documented non-implemented
capability lifecycle backend                  implemented externally in pantheon-mvp
RuntimeHost/model observations                documented non-implemented
role facets                                   already documented candidate in ROLE_FACETS.md; UI reference projection non-implemented
fixed scoped Hermes card assistant            documented non-implemented
```

## 19. Forbidden collapses

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
```

The Cockpit may make the structured system simple to use; it must not make consequential distinctions disappear.