# Architecture Project Card Deck Composition

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document owns one architecture-domain projection rule for the Cockpit: keep the number of visible card families small, keep project use simple, and let rich professional content live in flexible Information cards rather than multiplying rigid object types.

```text
OpenWebUI / Cockpit exposes.
Hermes Agent executes bounded work and may edit permitted working content.
Pantheon Next governs consequential status, scope, approval and external effects.
The human decides.
```

This document does not create a runtime, workflow engine, approval engine, scheduler, queue, provider router, memory engine or source-of-truth replacement.

## 1. Core simplification

The architecture cockpit should not create separate visible card families for every professional concept.

```text
Project = affair anchor and current synthetic business information.
Information = flexible professional content and source-linked dossier material.
Contacts = one project-level grouped contact card.
Work = visible professional work structure and progress projection.
Decision = review/validation surface when Work requires human orientation or confirmation.
Tool = operational capability/runtime/connector projection.
```

A future Reference family may expose reusable competences, methods, roles, templates or rites, but it is not required for the first agency cockpit.

The following former candidate distinctions are intentionally not promoted as separate architecture-facing card families:

```text
Surface
Fact
Claim
Jalon
```

They may still exist as technical concepts elsewhere when an owner doctrine requires them, but the architecture cockpit should not force them into separate user-facing schemas.

## 2. Project card

The Project card is the affair anchor. It may directly carry concise current information useful to the agency, including for example:

```text
project identity
code
display name
client
address
phase
business status
budget
terrain/project/existing surface summaries
current footprint summary
parcel references
permit reference
selected project-specific summary fields
```

These values remain current business information. Their presence on the Project card does not make them proof, Evidence or an opposable regulatory conclusion.

```text
project display != Evidence
project value != source authority
project revision != approval state
```

The Project card also exposes its Information cards, Contacts card, Work cards and relevant Decisions.

## 3. Information card

Information is the principal flexible professional card family.

It can represent, without changing the base card contract:

```text
PLU / PLUi note
email
meeting report
internal note
contract
CCTP / CCAP
supplier document
technical study
received dossier
administrative document
regulatory analysis
question
hypothesis
professional synthesis
source-backed memo
other project information
```

### 3.1 General fields

An Information card should support at least:

```text
card_id
project_ref
title
category
source_type
source_ref optional
source_version optional
index optional
date optional
author
summary
details
status
limits / postures[]
tags[]
previous_ref optional
technical revision + audit metadata
```

`category` and `source_type` are distinct.

Example:

```text
category = PLU
source_type = PDF
```

or:

```text
category = compte_rendu
source_type = note
```

### 3.2 Index rule

The visible Information-card index changes only when the source/reference document changes in the professional sense.

Hermes edits to summary/details do not consume a new visible index.

```text
visible source index != technical revision
```

Technical revisions may be recorded internally for audit and concurrency without changing the professional index.

For draft notes without an external file, the owner contract must define what constitutes a new source/version boundary before automatic index changes are implemented.

### 3.3 Author

Use `author`, not `created_by`, for the professional author/issuer attribution shown to the user.

No user-facing `updated_by` field is required on the card.

Technical audit metadata may still exist behind the projection.

### 3.4 Working and acted states

The minimal user-facing status vocabulary is:

```text
brouillon
en_redaction
acte
```

A technical `superseded` state may exist internally where needed.

Hermes may directly improve permitted working content while the card is `brouillon` or `en_redaction`, for example:

```text
rewrite
clarify
summarize
detail
develop
restructure
```

`acte` is a consequential professional status. Hermes must not self-promote a working card to `acte`.

An acted card is not silently rewritten. A material new professional version is prepared separately and retains the prior acted state as reference.

### 3.5 Context rule for Hermes

While a newer working version exists, Hermes context should contain both:

```text
last acted Information card/version
+
current working Information card/version
```

Hermes must therefore be able to distinguish:

```text
what is acted
what is being drafted
what is assumed
what is proposed
```

This is context construction, not durable memory promotion.

## 4. Information limits / postures

Limits/postures are not tags.

Initial professional vocabulary:

```text
questionnement
hypothese
consultatif
obligatoire
contractuel
```

Several may apply when meaningful.

These are use qualifications. They do not silently collapse governance distinctions.

```text
contractuel != Evidence
acte != legally opposable by itself
obligatoire != automatically verified
hypothese != fact
```

Hermes may propose a posture change, but it must not autonomously make consequential transitions such as:

```text
consultatif -> contractuel
hypothese -> obligatoire
```

when that transition changes professional reliance or responsibility.

## 5. Tags

All card families may use a common Tag Registry.

Tags are lightweight transverse professional classification and navigation metadata, for example:

```text
re2020
maison-individuelle
logement
tertiaire
ecole
erp
zone-naturelle
structure
electricite
dce
cctp
ccap
chantier
urbanisme
```

A tag registry entry should minimally support:

```text
slug
title
description
icon_key    # intended Radix icon mapping
color       # semantic presentation token
```

Hermes may primarily manage ordinary tag assignment and may propose/add missing vocabulary under the registry policy.

Hermes should prefer an existing canonical tag before creating a near-duplicate.

Tags are never governance shortcuts.

```text
tag != status
tag != limit/posture
tag != approval
tag != Evidence
tag != safety qualification
```

## 6. Status and limit visual language

Status and limit/posture registries are distinct from the Tag Registry.

On the card recto:

```text
status + limits
= icon only
= circular colored background/border treatment
= aligned horizontally at top right
```

On the card verso the same status/limit semantics may remain compact, with accessible labels/tooltips available to avoid icon-only ambiguity.

The server/owner schema determines allowed status transitions. CSS appearance does not authorize a transition.

## 7. Contacts card

A Project exposes one Contacts card containing several contacts grouped by project-use category.

Typical groups:

```text
maitrise_ouvrage
architecte / equipe_maitrise_oeuvre
bureau_etudes
bureau_controle
ssi
autres_intervenants
entreprises_travaux
```

The first agency cockpit does not require a visible Participation card per person or company.

A simple contact entry may contain:

```text
name
company optional
role optional
email optional
phone optional
address optional
notes optional
source optional
```

Hermes may populate or update project contact information from user-provided material or an explicitly permitted external source such as Google Contacts.

This simplification accepts that project-local contact snapshots may duplicate a person across projects. A future canonical directory may be introduced separately if the operational value justifies the added relation model.

## 8. Work card

A Work card represents the visible structure of professional work.

It may show:

```text
objective
current professional work state
steps / milestones
responsibilities mobilized
role/god references
skills
functions
approved tools/bindings used or expected
linked Information card(s)
expected result
```

The Work card may look like a workflow to the user, but Pantheon does not become the workflow runtime.

```text
Work card = visible governed work projection
Work card != scheduler
Work card != queue
Work card != orchestration engine
```

Hermes executes only bounded admitted work through its external runtime.

The Cockpit displays the professional sequence and current state.

No hidden chain-of-thought is stored or exposed. Visible steps are explicit professional objectives, checkpoints and reviewable actions only.

## 9. Work to Information production

A Work card does not change entity type into an Information card.

Instead:

```text
Work card
  -> produces
Information card
```

Examples:

```text
Prepare meeting report
  -> meeting-report Information card
  -> optional PDF source when exported

Prepare email
  -> email Information card / delivery-ready draft

Analyse PLU
  -> PLU analysis Information card
```

The completed Work card may remain available as trace/history while the produced Information card becomes the useful professional artifact.

## 10. Decision card

A Decision surface appears when Work requires human orientation, validation or final confirmation.

Typical sequence:

```text
Work
 -> human choice required
 -> Decision surface
 -> human selects/validates
 -> Work continues or completes
```

or:

```text
Work complete
 -> final review Decision
 -> human validation
 -> final Information artifact / external handoff candidate
```

The visual Decision family may render agency choices and Pantheon governance review with a consistent UX, but underlying governed objects remain distinct.

```text
Agency professional choice != Pantheon governance Decision
Gate != Decision
Decision recorded != external action performed
```

Hermes may prepare options, sources, concise rationale and recommendations. Hermes does not self-record the consequential human decision.

## 11. Tool card

The Tool family may visually group:

```text
Capability
Binding
Runtime Host
Connector
External service
```

The underlying statuses remain separate.

```text
installed != approved
healthy != safe
update_available != update_authorized
binding_selected != dependency_adopted
installed != activated
```

Hermes may observe and report operational state where authorized. Pantheon governs consequential posture. The human approves installation/update/activation where required.

## 12. Common recto card shell

All visible card families should use one stable DOM/CSS hierarchy as far as possible.

```text
CARD
├── HEADER
│   ├── IDENTITY
│   │   ├── TYPE / CATEGORY
│   │   └── INDEX + DATE
│   └── STATES
│       ├── STATUS ICON
│       └── LIMIT ICON(S)
├── BODY
│   └── family-specific primary content
└── FOOTER
    └── TAG ICONS
```

Recto placement rule:

```text
top left     = type/category, then index/date underneath
top right    = status + limit icons, horizontally aligned right
center       = primary content
bottom right = tags as icons only, vertically anchored to the bottom
```

Recto tag rendering:

```text
icon only
circular visual treatment
color comes from Tag Registry
border/background created with CSS
accessible title/tooltip retained
```

The tag circle is presentation only. It must not be encoded as a separate bitmap asset.

## 13. Common verso card shell

The verso keeps the same identity/context but prioritizes detailed review.

```text
CARD BACK
├── HEADER
│   ├── IDENTITY / INDEX / DATE
│   └── STATES
├── BODY
│   └── detailed family-specific content
└── FOOTER
    ├── ACTIONS
    └── TAG LABELS
```

Verso placement rule:

```text
top          = stable identity + status/limits
center       = detailed content and useful provenance
bottom left  = context-permitted actions
bottom left, bottom row = tag labels
```

Actions and tags share the footer vertically rather than overlapping.

Recommended order:

```text
actions
then tags anchored to the bottom edge
```

Verso tags render as text labels with rectangular colored background and no rounded-pill treatment.

## 14. Contextual actions

The card shell exposes only actions permitted by the current owner policy/context.

Examples:

```text
working Information card
 -> Ask Hermes to improve / detail / develop / restructure

Hermes candidate requiring review
 -> Refuse / Accept

Decision surface
 -> Refuse / Validate selected option

acted Information card
 -> prepare next working version
```

The browser must not infer authorization from the existence of a button.

```text
button visible != action authorized
UI intent != runtime command
```

The server/Pantheon boundary remains responsible for consequential checks.

## 15. Notion projection

Notion should remain a simplified current-state collaborative projection.

Default direction:

```text
Project
 -> current useful project information

Contacts
 -> current useful project contacts where desired

Information
 -> current acted/final useful information only

Work
 -> optional human-facing work summaries only

Decision
 -> final useful professional decision only
```

Do not project by default:

```text
technical revisions
archived card versions
Hermes working candidates
rejected candidates
runtime traces
internal diffs
governance-only operational observations
```

Notion remains a projection and does not acquire authority merely because it is editable.

## 16. Implementation posture

```text
implemented:
- existing Cockpit V2 cards-first prototype and flip/navigation mechanics in pantheon-mvp;
- Agency Data current read projections;
- existing append/revision and bounded governance seams owned elsewhere.

partial:
- current card CSS already uses a three-row face shell compatible with HEADER / BODY / FOOTER;
- tags already support icon/color projection fields in the structured interface;
- current project participant collection can act as the transition seam toward a single grouped Contacts card.

documented non-implemented:
- this simplified six-family architecture UX;
- unified Information card contract;
- source-index rule;
- acted + working dual-context resolver behavior;
- grouped project Contacts card as the only contact card;
- tag/status/limit registries driving the final renderer;
- recto/verso placement rules in this document;
- contextual Hermes edit actions on Information cards.

obsolete candidate direction for the architecture cockpit:
- forcing Surface / Fact / Claim / Jalon into separate visible card families;
- treating every project participant as a required visible card.

forbidden:
- automatic approval;
- Hermes self-promotion to consequential acted/contractual/approved states;
- hidden execution from a card click;
- tag assignment that fabricates approval, Evidence, safety or authorization;
- Pantheon becoming the Work runtime.
```

`schemas/project_claim.schema.yaml` may remain temporarily as historical/candidate compatibility material, but this document no longer treats `Project Claim` as the required architecture cockpit composition seam. Its retention, deprecation or deletion should be handled in a separate schema-cleanup change after implementation review.

## 17. Promotion condition

This document remains candidate support doctrine.

Implementation, indexing, passing CI or merging this file does not promote it to active doctrine. Promotion requires explicit human decision after practical Cockpit testing and confirmation that the simplified model preserves the necessary governance distinctions without burdening agency use.
