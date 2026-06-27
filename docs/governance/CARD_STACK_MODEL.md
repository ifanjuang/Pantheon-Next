# Card Stack Model

Status: candidate support doctrine — review draft for card-based cockpit UX, scenes, navigation and gate visibility.

Review status: explicitly open for re-reading with Claude, ChatGPT and human arbitration.

Runtime status: non-executable.

This document is a working model. It is intentionally not final doctrine. It should remain easy to revise while the card UX, scenes, role cards, rites, competences, evidence handling and project navigation are tested conceptually.

It does not implement a UI, mobile app, Swiper component, dashboard, frontend route, card renderer, state machine, runtime, workflow engine, graph database, scheduler, queue, skill generator, competence engine, evidence engine, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill, connector or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon needs a cockpit UX that makes governance visible without turning governance into a technical maze.

The user should be able to understand:

```text
where they are;
which project and subject are active;
which workflow is being reviewed;
which cards were mobilized;
which evidence supports the result;
which competences were used or created;
which rites and roles intervened;
which gates block, allow or escalate;
what can be changed, promoted, refused or validated.
```

The model must be playful enough to use on mobile, but disciplined enough for professional work.

## Working thesis

```text
Cards are unique objects.
Scenes are filtered and ordered presentations.
The Workflow Scene is exhaustive for the cards used in a treatment.
The Evidence Scene is scoped by project and subject.
The Competence Scene is global, neutral and not project-owned.
The Constellation is the map used to change project and understand the graph.
Gates are the decision surfaces.
```

French working formula:

```text
Les cartes sont les objets.
Les scènes sont des présentations filtrées et ordonnées.
La scène Workflow est exhaustive sur les cartes utilisées.
La scène Evidence est cadrée par projet et sujet.
La scène Compétences est globale et neutre.
La constellation permet de changer de projet.
Les gates exposent le statut et les décisions.
```

## Non-finality rule

This document is deliberately written as a candidate.

It may be revised after:

```text
Claude review;
ChatGPT review;
professional UX walkthrough;
mobile prototype testing;
card count testing;
workflow example testing;
architecture-domain example testing.
```

No section of this document promotes a schema, runtime, UI, role, rite, competence, memory rule or implementation.

## Core separation

### Card

A Card is a unique governance or cockpit object.

Examples:

```text
Project Card
Subject Card
Workflow Card
Context Card
Connaissance Card
Guide de competence Card
Ressource de competence Card
Competence Card
Template Card
Document / Source Card
Evidence Card
Role / God Card
Rite Card
Lieu Card
Action Card
Gate Card
Trace Card
Memory / Register Card
Gap Card
Promotion Card
Constellation Card
```

A card may appear in several scenes, but it should not be duplicated as a different object merely because another scene displays it.

### Scene

A Scene is a filtered and ordered presentation of cards.

Examples:

```text
Workflow Scene
Evidence Scene
Competence Scene
Documents / Connaissances Scene
Gates Scene
Actions Scene
Memory / Trace Scene
Constellation Scene
```

A Scene is not a database table by itself.

A Scene is not a runtime workflow.

A Scene is not a separate copy of the cards.

### Deck

A Deck is the vertical sequence of cards currently visible inside a scene.

In a Workflow Scene, the deck is the narrative of the treatment.

In a Competence Scene, the deck may be the maturity column for a competence subject.

In an Evidence Scene, the deck may be the evidence stack for a project subject.

### Constellation

The Constellation is the global graph view.

It is used to:

```text
change project;
see subjects;
see gates;
see tensions;
see dependencies;
see hidden or filtered cards;
understand how project, subject, workflow, evidence, actions and competences relate.
```

The Constellation helps orientation.

It should not become the main decision surface. Gates remain the decision surfaces.

## Navigation model — candidate

### Project switching

Changing project should happen from the Constellation or another explicit project map.

This avoids overloading horizontal swipe with too many meanings.

### Project view

Inside a project, horizontal navigation should move between subjects of the same project.

```text
Subject A <-> Subject B <-> Subject C
```

### Subject view

Inside a subject, vertical navigation should move through the active scene deck.

For the Workflow Scene:

```text
Project compact card
↓
Subject card
↓
Workflow card
↓
Used cards in treatment order
```

### Scene switching

Scene switching should not be the main horizontal swipe if horizontal swipe is used for subjects.

Scene switching may be handled by:

```text
scene rail;
segmented control;
small tabs;
mode switch;
scene picker card;
constellation filter.
```

Candidate scene rail:

```text
Workflow | Evidence | Documents | Gates | Actions | Traces
```

Global or special scene:

```text
Competences
```

### Card interaction

```text
Tap
= open verso / detail.

Long press
= quick actions such as edit, promote, refuse, open gate, request source, mark obsolete, archive, merge.

Swipe vertical
= read sequence.

Swipe horizontal
= sibling subjects inside the same project, unless a specific screen defines otherwise.

Constellation button
= return to project/global graph.
```

## Scene model

## 1. Workflow Scene

The Workflow Scene is the complete narrative of a treatment.

It must show all cards actually mobilized by the workflow, including:

```text
Project
Subject
Workflow / Demarche
Context Stack
Context Cards
Documents / Sources used
Connaissances used
Competences used
Competences created on the flow
Guides / Ressources de competence when relevant
Templates used
Evidence created or relied on
Role / God Cards activated
Rite Cards invoked
Action Cards prepared
Gate Cards opened or closed
Trace Cards
Memory / Register Candidate Cards
Gap Cards
Promotion Cards
```

Important boundary:

```text
Workflow Scene is exhaustive for used cards.
It is not exhaustive for all cards in the project.
```

A card is included when it participates in the treatment.

A card is not included merely because it exists somewhere in the project or system.

### Workflow opening order

Recommended opening sequence:

```text
1. Project compact card
2. Subject card
3. Workflow card
4. Treatment cards in order
```

The primary Gate may remain visible as a badge, sticky status or compact strip while scrolling.

This avoids forcing Gate to be the third card in every workflow while keeping decision status visible.

### Workflow card purpose

The Workflow Card explains:

```text
what method is active;
why this method was selected;
which cards were mobilized;
which rites or roles were involved;
which gates bound the output;
which result candidate was produced;
which traces were preserved;
which promotions were suggested.
```

### Workflow closure

A Workflow Scene should close with explicit status, for example:

```text
draft_allowed
source_required
approval_required
transmission_blocked
memory_candidate_created
competence_candidate_proposed
task_split_required
closed_without_action
```

## 2. Evidence Scene

The Evidence Scene is project-scoped and subject-scoped.

Primary classification:

```text
Project
-> Subject
-> Assertion or value
-> Source / Evidence
-> Status
```

Evidence should not be treated as global by default. Evidence usually has a scope.

Example:

```text
Project: extension maison
Subject: surface taxable CERFA
Evidence: surface taxable candidate = 42.30 m2
Source: plans APD + calculation table
Status: candidate / to verify
Gate: not transmissible before validation
```

Evidence Scene should show:

```text
Evidence Cards for the subject
source chain
contradictions
missing evidence
doubt types
validated evidence
obsolete evidence
affected actions
affected gates
```

Horizontal navigation in Evidence Scene may follow sibling subjects of the active project.

## 3. Competence Scene

The Competence Scene is global and neutral.

A competence is not owned by a project.

```text
A competence may be used by a project.
A competence must not become project-specific by default.
```

The Competence Scene should be organized by competence subject horizontally and maturity vertically.

Candidate horizontal subjects:

```text
PDF / forms
APIs / open data
surfaces / calculations
web research
urbanism / rules
construction / chantier
documents / extraction
visualization / d3.js / three.js
communication
memory / capitalisation
```

Candidate vertical maturity:

```text
Durable competences
↓
Candidate competences
↓
On-the-flow competences
↓
Observed needs
↓
Competence gaps
↓
Blank new competence card
```

A Competence Card may list usage references to projects and workflows, but those usages do not make the competence project-owned.

### Competence created on the flow

When a workflow reveals a reusable ability, the Workflow Scene should surface a special card:

```text
Competence on the flow
```

It means:

```text
The treatment revealed a potential reusable competence.
It is not yet a validated competence.
It may be edited, refused, merged, kept as project-only note or promoted to Competence Candidate.
```

User actions:

```text
edit
complete
promote to competence candidate
merge with existing competence
refuse
mark as project-only case note
```

Promotion criteria:

```text
general enough to reuse;
not dependent on one project;
bounded;
testable;
linked to guides/resources;
clear inputs and outputs;
clear risks;
clear gates;
not already covered by an existing competence.
```

### Blank competence card

The Competence Scene should include a blank card for proposing a new competence.

Initial paths:

```text
from idea;
from wiki / guide;
from documentation;
from workflow;
from gap;
from existing competence;
from repeated manual work.
```

Initial status:

```text
observed_need
```

or, if sufficiently structured:

```text
competence_candidate
```

## 4. Documents / Connaissances Scene

This scene should distinguish Documents and Connaissances.

```text
Document / Source
= file, link, plan, email, notice, page, PDF, image, table, API response, retrieved item.

Connaissance
= professional, regulatory, contractual, agency, project or dossier knowledge extracted, qualified or structured.
```

A document may feed a connaissance.

A connaissance may support Evidence when selected for an assertion or value.

This scene may contain both project-specific and general material, but they must be marked:

```text
project connaissance
professional / metier connaissance
agency connaissance
external source
competence resource
```

Important distinction:

```text
Competence guides and resources are not metier connaissance unless they state professional, regulatory, contractual or project content.
```

## 5. Gates Scene

The Gates Scene shows decision surfaces.

It may be scoped to:

```text
project
subject
workflow
action
memory proposal
competence promotion
external transmission
```

It should show:

```text
current status;
what is allowed;
what is blocked;
why;
which roles signaled;
which evidence is missing;
which approval is required;
which options the user has;
which next procedure ZEUS selected or recommends.
```

Gate cards should not decide truth.

They expose status and procedure.

## 6. Actions Scene

The Actions Scene shows candidate or completed outputs.

Examples:

```text
mail candidate
PDF filled candidate
form prepared candidate
table generated
note drafted
schema generated
patch candidate
external message
file classification
```

Each Action Card must classify effect:

```text
internal draft
candidate artifact
internal state change
external effect
canonical effect refused as runtime work
```

External effect requires approval.

## 7. Memory / Trace Scene

The Memory / Trace Scene separates trace from memory.

```text
Trace
= what happened, was consulted, produced, modified, blocked or decided.

Memory / Register Candidate
= what may remain after validation.
```

This scene may show:

```text
Trace Cards
Memory Candidate Cards
Register Cards
Archive Cards
Promotion Cards
Revocation Cards
Obsolete Cards
```

A workflow should show its trace and any memory or promotion candidate it created.

## 8. Constellation Scene

The Constellation Scene is the graph view.

It should support:

```text
change project;
select subject;
see project-level gates;
see subject clusters;
see evidence/action dependencies;
see competence usages;
see memory candidates;
see conflicts;
see filtered-out cards;
understand relations.
```

It is an overview and navigation surface.

It is not the main decision surface.

## Card recto / verso rule

The card front must be simple.

The card back must be detailed.

```text
Recto
= read in two seconds.

Verso
= understand, verify, relate, audit or act.
```

The verso should not repeat the recto except for the card name or a small persistent title.

### Universal front fields — candidate

Most card fronts should expose no more than seven visible pieces of information.

Candidate universal front:

```text
title
family
type or subtype
scope
status
main signal / risk / value
linked gate or next step
```

This is not a rigid schema. Some families need fewer fields.

### Universal back fields — candidate

The card back may include:

```text
details
relations
sources or traces
role / rite / gate links
action links
history
review notes
promotion options
edit controls
```

The exact fields depend on card family.

## Card family display table — candidate

| Card family | Recto simple | Verso detail, without repeating recto |
|---|---|---|
| Project / Affaire | project name; phase; location; typology; global status; next milestone; global risk | actors; mission; contractual scope; key dates; authorizations; known constraints; open subjects; dependencies; linked workflows; project-level gates |
| Subject / Situation | subject; active question; urgency; status; risk; active workflow; main gate | request origin; exact formulation; known facts; unknowns; assumptions; tensions; linked cards; roles; rites; expected output; scope limits |
| Workflow | workflow name; subject; status; method; number of used cards; main gate; result candidate | selection reason; full used-card sequence; involved roles; invoked rites; evidence relied on; competences used/created; actions; traces; closure status; promotion suggestions |
| Context Stack | active question; context sufficiency; active context count; main missing context; HESTIA status; linked gate | active context cards; reasons for inclusion; missing context; stale context; oversized context; project/general/agency scope; sufficiency by output type; change candidates |
| Context | context family; scope; status; main gap; risk if wrong; sufficient for what | context data; origin; freshness; ambiguities; exclusions; conflicts; reason for activation; impact on evidence/action/gate |
| Connaissance | name; domain; status; scope; main source; freshness; confidence | detailed content; rule or project fact; full source; version; date; applicability; limits; contradictions; linked assertions/evidence; validation status |
| Guide de competence | guide name; linked competence; method covered; status; maturity; update signal | method steps; anti-usages; prerequisites; linked resources; examples; minimum tests; limits; review date; possible runtime projection |
| Ressource de competence | name; format; linked competence; status; source; date; freshness | link or file; version; license; author; intended use; not authoritative for; state; dependencies; update policy |
| Competence | name; what it can do; status; inputs; candidate outputs; main risk; output gate | what it cannot do; guides; resources; templates; required tools; possible Hermes projection; tests; limits; evidence expectations; approval ceiling; fallback; use cases |
| Hermes Skill | skill name; projected competence; runtime status; available or not; risk; last test | skill folder; dependencies; commands; tools; inputs/outputs; runtime limits; traces; known errors; activation status; Task Contract compatibility |
| Tool / Connector | tool name; type; availability; possible action; risk; required authorization | auth; permissions; exposed data; limits; logs; errors; scopes; costs; dependencies; compliance; external effects; linked competences |
| Template | name; output type; scope; status; used by; misuse risk | expected fields; required fields; forbidden fields; variables; tone; structure; fictional example; limits; usage conditions; external-output gate; version history |
| Document / Source | title; type; version/index; date; author; status; reliability signal | useful excerpts; provenance; transmission chain; pages; links; contradictions; freshness; linked connaissances/evidence; uncertain zones; derived pieces |
| Evidence | assertion or value; status; confidence; main source; contradiction flag; action impact; linked gate | detailed sources; citations; calculation method; direct/indirect support; assumptions; confidence scale when used; contradictions; limits; validator; scope; history |
| Action | candidate action; type; recipient; internal/external effect; status; ZEUS gate; approval required | linked artifact; transmission conditions; required evidence; risks; versions; attachments; channel; logs; rollback; next steps; approval trace |
| Gate / ZEUS | gate object; status; allowed; blocked; main reason; expected decision | role positions; missing evidence; options; recommended procedure; approval level; impact on action/memory/transmission; preserved dissent; human decision requirement |
| Role / God | role; active facet; signal; status; block or alert; concerned gate | mandate; useful bias; risk if excessive; detailed analysis; what it sees; what it may miss; proposals; objections; recommended rites; relations to other roles |
| Rite | rite name; reason; mode; involved roles; status; expected output | trigger; anti-trigger; sequence; budget; closure criteria; revealed tensions; retained results; ZEUS final status; evidence expectations; reason for another rite if proposed |
| Lieu | place name; UX function; hosted families; dominant role; frequent gate | present cards; navigation; neighboring cards; place usage; confusion risks; available views; display rules; possible thresholds/transitions |
| Trace | event; date; origin; type; status; impact | event detail; before/after; author; tool; file; commit; link; justification; relations; effect on evidence/action/gate/memory |
| Memory / Register | remembered or candidate item; scope; status; sensitivity; validation state | origin source; reason to preserve; duration; anonymization; project/agency/general level; revocation; obsolescence; linked evidence; promotion decision |
| Gap / Manque | identified gap; type; what it blocks; priority; detector role; linked gate | description; context; missing competence/source/tool; impact; workaround; expected decision; proposed creation path |
| Promotion | item to promote; target type; origin; status; why it may be durable; decision needed | source workflow; supporting examples; generality test; risks; merge candidates; required review; proposed target card; refusal path |
| Constellation | central subject; visible card count; tensions; main gate; next action | full graph; typed links; dependencies; ascendants/descendants; conflicts; alternate paths; filters; hidden cards; composition justification |

## Roles / gods in cards

A Role / God Card should appear in a workflow only when the role is active, mandatory or has produced a useful signal.

Roles should not appear as decorative characters.

UX compression rule:

```text
Gods are review facets.
Rites are methods.
Places are views.
Invocations are signals.
ZEUS is procedural status.
The human decides.
```

## Rites in cards

Rites may appear in Workflow Scene when invoked, proposed, blocked or closed.

Rites must remain bounded procedures.

A rite may reveal the need for another rite, but should not trigger it by itself. Any second rite requires ZEUS status and an explicit reason.

## Places in cards

Places are UX orientation zones.

Candidate places:

```text
Contexte — Le Foyer
Sources — Les Archives
Risque — Le Tribunal
Production — L'Atelier / La Forge
Debat — L'Agora
Transmission — Le Pont / Le Sas
Decision — Le Seuil / Le Trone
```

Places do not create new authority.

They help the user understand where a card belongs.

## Competence neutrality rule

Competences are global and neutral by default.

```text
Competence identity is not project-specific.
Competence usage may be project-specific.
```

A competence may list projects, subjects or workflows where it was used.

Those usages are trace and feedback, not ownership.

## Evidence scope rule

Evidence is scoped.

Default evidence scope:

```text
project -> subject -> assertion/value
```

Evidence may support broader memory only through explicit review and promotion.

## Promotion model — candidate

Workflows may produce promotion candidates:

```text
Competence Candidate
Template Candidate
Connaissance Candidate
Memory Candidate
Guide Candidate
Resource Candidate
Rite Candidate
```

A promotion candidate should expose:

```text
origin workflow;
reason for promotion;
why it may be reusable;
what must be reviewed;
risk if promoted incorrectly;
merge/refuse/project-only options;
ZEUS status;
human decision requirement when needed.
```

Promotion must not be automatic.

## Complexity budget — candidate

This budget is provisional and should be tested.

```text
Workflow Scene:
  show all used cards, but group or collapse low-impact cards if the deck becomes unreadable.

Card front:
  no more than 7 visible pieces of information.

Gate card:
  no more than 6 visible facets on front.

Rite card:
  no more than 5 visible steps on front.

Role card:
  one active facet on front; details on back.

Constellation:
  overview only, not the main decision surface.
```

If a Workflow Scene becomes too long, safe compression options:

```text
group trace cards;
group low-risk documents;
collapse repeated role signals;
show promotion candidates as a closing cluster;
keep gate, evidence and action cards visible.
```

## Open review questions

These questions are intentionally left open for future review:

```text
1. Should the term Scene replace Game in all UX doctrine?
2. Should horizontal swipe always mean sibling subjects, or can special scenes override it?
3. Should Workflow Scene include every Trace Card or a grouped Trace cluster by default?
4. Should Competence Scene be accessible globally only, or also as a project-side overlay?
5. Should Places stay pure UX labels, or receive a candidate governance note?
6. Should the card family table become a template later?
7. Should CARD_STACK_MODEL.md stay candidate until a mobile prototype validates the navigation?
8. Should competence promotion receive a dedicated Competence Promotion Gate document?
9. Should evidence cards in Workflow Scene be duplicated visually from Evidence Scene or referenced as cards from the same object graph?
10. Should the first card in Workflow Scene always be Project compact, or should it be hidden when project context is obvious?
```

## Review notes for Claude / ChatGPT / human arbitration

Reviewers should classify suggestions as:

```text
Accepted
Refused
To verify
To arbitrate
Non applicable
```

Review focus:

```text
Does this model stay simple enough for mobile use?
Does it preserve the distinction between project-scoped evidence and global competences?
Does it prevent competences from becoming project-specific by accident?
Does Workflow Scene show enough to understand the treatment without becoming unreadable?
Does the constellation remain navigation, not decision authority?
Does the model preserve gates as decision surfaces?
Does it avoid creating runtime behavior by vocabulary alone?
```

## Boundary

This document is a UX/governance candidate.

It creates no runtime, no UI, no schema, no database, no tool call, no connector, no skill, no approval engine and no memory engine.

Any implementation must be handled later in the appropriate exposure surface or execution runtime, under the existing placement doctrine.
