# Pantheon Cockpit Information Architecture

Status: candidate support doctrine — documented non-implemented.

Boundary profile: candidate_support_note.

Decision date: 2026-07-23.

This document records the accepted candidate information architecture for the Pantheon-facing cockpit.

It specializes the product-level navigation described in `PANTHEON_COCKPIT_UX_SPEC.md`, the card and Scene grammar of `CARD_STACK_MODEL.md`, the human-review presentation of `DECISION_SURFACE_SPEC.md`, the skill states of `SKILL_LIFECYCLE.md`, and the external runtime boundary of `HERMES_INTEGRATION.md`.

It does not create a UI, chat engine, document store, knowledge base, Kanban engine, queue, scheduler, approval engine, skill builder, installer, plugin manager, MCP host, memory engine, provider router or execution runtime.

```text
OpenWebUI or another cockpit surface exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## 1. Purpose

The cockpit must give a professional user one understandable entry point without flattening projects, documents, knowledge, operational capabilities and consequential decisions into one undifferentiated chat.

The accepted first-level navigation is:

```text
Pantheon
Affaires
Connaissances
Outils
Décisions
```

No additional top-level `Documents`, `Kanban`, `Skills`, `Plugins`, `MCP`, `Runtime`, `Trace` or `Administration` tab is introduced in the default professional mode.

These concerns remain accessible as bounded projections under the five primary spaces.

## 2. Decision summary

### Accepted

```text
Pantheon
= contextual conversation with Hermes.

Affaires
= professional Cases, their documents, work, project knowledge and history.

Connaissances
= general reusable knowledge outside one specific Affaire.

Outils
= governed catalogue of skills, toolsets, plugins, MCP entries and other runtime resources.

Décisions
= human inbox for questions, validations, approvals and arbitrations that block or condition continuation.
```

### Placement decisions

```text
Documents live primarily behind an Affaire.

Project-specific knowledge lives behind its Affaire.

General reusable knowledge lives under Connaissances.

Kanban is a view of work under Affaires, with an optional cross-Affaire aggregate.

A pending human response appears in Décisions and may also project into the
conversation and the relevant Kanban card.

Skill construction is proposed from Pantheon or Outils, but follows the governed
skill lifecycle and never auto-installs or auto-activates.
```

### Rejected collapses

```text
conversation = authorization
document = knowledge
project knowledge = general knowledge
knowledge = evidence
tool available = tool authorized
skill generated = skill admitted
plugin installed = plugin approved
Kanban card = queue job
decision card = approval
Hermes waiting = Pantheon scheduler
```

## 3. Shared identity rule

One underlying governed object may appear in several spaces.

```text
one entity
many bounded projections
no identity duplication
```

Example:

```text
one Work Issue
├── conversation projection in Pantheon
├── Kanban projection in Affaires
├── blocking Decision projection in Décisions
└── Trace projection after resolution
```

The UI must not create four independent records for these four displays.

Every projection should retain a stable identifier and explicit links to its source object, Affaire, conversation, task or Work Issue, sources and decision state.

## 4. Pantheon

### 4.1 Role

`Pantheon` is the landing page and the default working surface.

It is a contextual conversation with Hermes, not a generic unscoped chat and not a technical administration dashboard.

The default flow is:

```text
select or confirm an Affaire
-> inspect the proposed context
-> add or remove documents and knowledge
-> speak with Hermes
-> review candidates, gaps and decisions in the conversation
```

### 4.2 Visible context

The conversation header or context drawer should expose:

```text
active Affaire
active conversation
Hermes profile
model binding summary
selected project documents
selected project knowledge
selected general knowledge
selected capabilities when materially relevant
open decisions
scope and data-sensitivity warnings
```

Technical implementation details remain collapsed unless they materially affect trust, availability, cost, scope or a required decision.

### 4.3 Context hierarchy

The default context hierarchy is:

```text
Affaire
├── declared project scope
├── project documents
├── project knowledge
├── prior scoped decisions
├── relevant Work Issues
└── scoped conversation history

Optional additions
├── selected general knowledge
├── selected guide or template
└── explicitly mobilized operational capability
```

General knowledge is never attached silently merely because it is semantically similar.

Cross-Affaire content requires explicit selection or a declared governed relation.

### 4.4 Context selection

Each selectable context item should expose:

```text
name
type
origin
scope
version or date
status
why it is suggested
whether it is currently selected
```

Selections should be reversible before execution.

A suggested item is not automatically admitted into the active context.

```text
suggested != selected
selected != relied upon
relied upon != evidence
```

### 4.5 Conversation outputs

Hermes may return:

```text
answer candidate
draft candidate
document candidate
knowledge candidate
evidence candidate
capability gap
action candidate
decision request
runtime trace reference
```

A fluent response does not hide a missing source, unresolved contradiction, scope conflict or consequential action.

### 4.6 Conversation-integrated decisions

When Hermes cannot legitimately continue without a human response, the conversation shows a Decision card inline.

The same Decision appears in `Décisions`.

The card must state:

```text
what Hermes needs
why continuation is blocked or conditional
which Affaire and Work Issue are affected
the options or requested information
the consequence of each option
the sources or gaps
the next safe action
```

Resolving the card may allow an external runtime continuation, but the card itself does not resume a hidden Pantheon workflow.

## 5. Affaires

### 5.1 Role

`Affaires` is the professional dossier and work space.

An Affaire is the primary container for project-specific material.

Typical contents:

```text
overview
documents
work and Kanban
project knowledge
conversations
decisions
participants and scope
history and trace
```

### 5.2 Affaire list

The list should support:

```text
active
recent
waiting for me
at risk
archived
```

The user may switch Affaires without collapsing their conversations, sources, Work Issues or decisions.

### 5.3 Documents

Documents live under their Affaire by default.

Document families may include:

```text
source document
received document
working document
derived representation
generated draft
reviewed version
validated professional deliverable
superseded version
archived document
```

The UI must distinguish the original source from its extracted, OCR, Markdown, chunked, summarized or transformed representations.

```text
source document != derived representation
derived representation != reviewed knowledge
generated draft != validated deliverable
```

### 5.4 Project knowledge

Project knowledge is knowledge whose legitimate scope is one Affaire or one declared group of Affaires.

Examples:

```text
client decision for Lieurey
selected material for Mannevillette
contractual scope for Trouville
project-specific interpretation under review
```

It remains behind the Affaire unless a separate generalization proposal is reviewed.

### 5.5 Work and Kanban

Kanban is a view of governed work, not a new runtime.

Recommended professional columns:

```text
À traiter
En cours
En attente de décision
En attente externe
À valider
Terminé
```

Optional additional states may be shown only when backed by the owner Work Issue or task vocabulary.

A card may include:

```text
title
Affaire
current status
responsible human or runtime
linked conversation
linked sources
open decisions
blocker
last observation
next governed action
```

### 5.6 Waiting for a human decision

When Hermes reaches an unresolved human boundary:

```text
Work Issue in progress
-> Decision Candidate created
-> Work Issue projects as En attente de décision
-> Decision appears in Décisions
-> conversation shows the same Decision
```

After a human answer:

```text
Decision recorded
-> linked Work Issue becomes eligible for continuation
-> external runtime receives a bounded continuation or new Task Contract
-> Work Issue observation is refreshed
```

Pantheon does not schedule, queue or secretly resume the work by itself.

### 5.7 Global Kanban

A cross-Affaire Kanban may exist as a filtered aggregate inside `Affaires`.

It must preserve the original Affaire and Work Issue identities.

It is a view, not a separate work database.

## 6. Connaissances

### 6.1 Role

`Connaissances` contains general reusable knowledge that is not owned by one Affaire.

Typical categories:

```text
professional doctrine
regulation
construction methods
materials
agency methods
CCTP references
urban planning references
templates and guides
validated reusable lessons
```

### 6.2 Project versus general knowledge

```text
Project choice in Lieurey
= project knowledge under the Lieurey Affaire.

General zinc-roof design principles
= general knowledge under Connaissances.
```

The UI should make this scope visible.

### 6.3 Generalization path

Hermes may propose that a project-specific item is reusable.

The path is:

```text
project knowledge
-> Generalization Candidate
-> scope and source review
-> contradiction and sensitivity review
-> human decision
-> new versioned general knowledge candidate
```

The original project item remains linked and unchanged.

Generalization is not copying without provenance and is not automatic memory promotion.

### 6.4 Knowledge selection in Pantheon

General knowledge may be selected for a conversation from the `Pantheon` context drawer.

The UI should show:

```text
scope
authority or review status
source provenance
version
known limitations
reason for mobilization
```

Selection is explicit when the material can materially influence a professional conclusion.

## 7. Outils

### 7.1 Role

`Outils` is the user-facing catalogue of operational resources available to or proposed for Hermes.

The public label may be simple, but the internal resource type remains explicit.

Primary categories:

```text
Skills
Outils Hermes / Toolsets
Plugins
MCP
Connecteurs
Modèles et profils
```

The first implementation may expose only the categories that have reliable inventory data.

### 7.2 Common Resource Card

A common card may show:

```text
name
resource type
description
source and version
installation status
configuration status
technical activation status
governance authorization status
scope activation status
health observation
update signal
risk summary
dependencies
last observation
next required decision
rollback or suspension path
```

The card is a projection. It does not execute an operation.

### 7.3 Skill cards

A skill card may provide:

```text
read content
view provenance
view declared purpose and limits
view required tools
test in a bounded context
compare versions
propose a revision
suspend for a profile or scope
propose activation
propose generalization from a conversation
```

### 7.4 Toolset cards

A toolset card may provide:

```text
view the exposed tool family
view provider or backend
view required environment posture
view profile scope
test availability
propose enable or suspend
view consequential effects
```

The UI must not imply that every underlying Python function can be governed independently when Hermes only exposes a toolset-level control.

### 7.5 Plugin cards

A plugin card must expose the larger execution surface:

```text
repository and pinned revision
manifest
tools registered
hooks registered
commands registered
providers or backends registered
secrets required
host-control surface
network access
data access
installation status
enabled status
restart requirement
rollback path
```

Third-party plugin installation is a sensitive code-adoption event.

### 7.6 MCP cards

An MCP card should distinguish:

```text
server declared
server installed or externally present
authentication configured
connection reachable
server enabled
tools discovered
tools authorized by scope
health observed
last test
```

```text
MCP connected != MCP tools authorized
```

### 7.7 Read and change actions

Read-only actions may include:

```text
list
inspect
read content
view manifest
view status
view diff
view health observation
view update signal
```

Change candidates may include:

```text
install
adopt
configure
enable
suspend
update
rollback
remove
replace
```

Every change resolves to the relevant gate and external adapter.

The preferred reversible action is `suspend`, not `remove`.

## 8. Governed skill construction

### 8.1 Entry points

The cockpit may propose `Créer un skill` from:

```text
Pantheon conversation
Outils / Skills
a document
a repository
an existing skill
a blank guided template
a repeated task-local pattern observed by Hermes
```

### 8.2 Proposal, not automatic creation

Hermes may prepare a Skill Proposal Candidate.

Minimum candidate content:

```text
proposed name
bounded purpose
source material
originating Affaire and conversation when applicable
expected inputs
expected outputs
forbidden outputs
required tools or connectors
risk class
evidence expectation
approval ceiling
memory impact
scope
failure modes
tests
provenance and version
```

The first durable output is a reviewable draft, not an installed skill.

### 8.3 Builder path

```text
capture source and purpose
-> generate or edit Skill Proposal Candidate
-> inspect full content
-> inspect required operational capabilities
-> run bounded tests
-> record failures and limitations
-> declare manifest and passport
-> validate structure
-> admission review
-> install through Hermes when approved
-> keep disabled or scope-limited
-> activate separately
```

This path composes `SKILL_LIFECYCLE.md`; it does not replace it.

### 8.4 Conversation-derived skill

When a conversation contains a useful repeated method, Hermes may show:

```text
This method may be reusable.
Prepare a Skill Proposal Candidate?
```

The proposal must retain links to:

```text
originating conversation
originating Affaire
source documents
human corrections
known failed variants
final retained method
```

No private project fact should be generalized into a reusable skill without scope and confidentiality review.

### 8.5 Repository-derived skill

When a repo is supplied:

```text
repository observed
-> candidate skill paths identified
-> exact revision pinned
-> content inspected
-> provenance recorded
-> security and dependency review
-> install proposal
```

A repository URL is not an installation instruction.

### 8.6 Non-equivalences

```text
generated != declared
declared != validated
validated != admitted
admitted != installed
installed != enabled
enabled != task-authorized
successful test != professional validation
```

## 9. Décisions

### 9.1 Role

`Décisions` is the human attention and decision inbox.

It contains consequential or blocking items that require a human determination.

Primary user-facing types:

```text
Question
Validation
Approbation
Arbitrage
```

These labels specialize existing Gate and Decision objects; they do not create a new approval ontology.

### 9.2 Question

Hermes needs missing information or confirmation before it can proceed safely.

Examples:

```text
Which document version applies?
Which recipient is intended?
Is this assumption correct?
What is the mission scope?
```

### 9.3 Validation

A candidate output requires professional review.

Examples:

```text
draft document
analysis candidate
knowledge publication candidate
proposed task completion
```

Validation of a draft does not necessarily authorize transmission, memory promotion or canonical admission.

### 9.4 Approbation

A consequential effect requires explicit authorization.

Examples:

```text
install or activate a capability
send externally
modify an external system
update a runtime
promote knowledge or memory
apply a destructive change
```

### 9.5 Arbitrage

Several legitimate options, interpretations or priorities require a human choice.

The options must show their consequences and unresolved evidence.

### 9.6 Decision card

A Decision card should contain:

```text
decision type
question
status
priority or urgency
Affaire
linked Work Issue or task
linked conversation
linked source or document
blocked action
candidate options
recommendation candidate when present
evidence and gaps
scope
required decision owner
created time
age
next safe action
```

### 9.7 Views

Recommended views:

```text
À décider
À valider
Approbations
Décisions prises
```

A combined default inbox may group them by urgency and Affaire.

### 9.8 Resolution and continuation

A human response produces a Decision record or an explicitly scoped captured determination.

It may authorize a bounded handoff or continuation.

It does not directly prove that execution occurred.

```text
decision recorded != action executed
action executed != result validated
```

The resulting runtime observation returns separately.

## 10. Kanban and Decision coupling

### 10.1 State coupling

A Work Issue can be shown in `En attente de décision` when at least one unresolved Decision blocks its declared next step.

The relation should be explicit:

```text
decision_blocks_work_issue
```

The decision may remain non-blocking when it requests preference but the Task Contract allows a safe fallback.

### 10.2 No hidden queue

The Kanban does not dispatch Hermes jobs.

The Decisions inbox does not resume jobs.

A separately admitted runtime or adapter performs execution and continuation.

### 10.3 Continuation contract

After a decision, the system should prepare one of:

```text
bounded continuation instruction
revised Task Contract
new Task Contract
manual human step
refusal or closure
```

The continuation should retain:

```text
decision reference
original Work Issue
scope
allowed effects
forbidden effects
idempotency expectation
expected result candidate
expected evidence candidate
```

## 11. Cross-space navigation

Required deep links include:

```text
Pantheon conversation -> Affaire
Pantheon context item -> document or knowledge detail
Pantheon decision card -> Décisions
Affaire Work Issue -> linked conversation
Affaire Work Issue -> blocking Decision
Affaire document -> derived representations
Connaissance -> source Affaire or source document
Outil card -> tests, decisions and affected profiles
Décision -> conversation, Work Issue, sources and outcome observation
```

Back navigation must restore the prior Scene and active context without silently changing the selected Affaire.

## 12. Notifications and attention

The default cockpit should prioritize:

```text
decisions waiting for the user
work blocked by the user
new validation candidates
critical capability degradation
scope or source conflicts
```

A notification is a signal, not a decision and not a job.

## 13. Responsibility allocation

### Pantheon governs

```text
identity
scope
status
provenance
evidence expectation
decision requirement
approval ceiling
installation proposal
activation authorization
update authorization
rollback visibility
knowledge generalization
memory consequence
external-action legitimacy
```

### Hermes executes

```text
conversation runtime
skill loading
tool calls
plugin execution
MCP calls
bounded tests
external adapter operations
task continuation under contract
```

### OpenWebUI or the cockpit exposes

```text
conversation
context selection
Affaires
documents
knowledge
resource cards
Kanban projections
Decision cards
status and trace projections
```

### The human decides

```text
scope clarification
professional validation
arbitration
capability adoption
installation and activation
consequential external action
knowledge generalization
memory promotion
update and rollback
```

### Forbidden

```text
automatic capability installation
automatic plugin activation
automatic skill admission
automatic generalization
automatic professional validation
automatic external transmission
automatic memory promotion
Pantheon-owned scheduler or queue
hidden cross-Affaire context
```

## 14. Candidate implementation sequence

This sequence is planning guidance, not authorization.

### Phase 1 — read-only IA

```text
Pantheon conversation shell
Affaire selector
explicit context drawer
Affaires list and document cards
general Knowledge list
Outils inventory cards
Décisions read-only inbox
Kanban read-only projection
```

### Phase 2 — reversible proposals

```text
context selection
create Decision Candidate
suspend proposal
skill proposal drafting
bounded test proposal
decision capture
```

### Phase 3 — approved external adapter actions

```text
Hermes skill enable or suspend
toolset enable or suspend
plugin enable or suspend
MCP enable or suspend
skill installation into quarantine
bounded task continuation
```

Each operation remains externally executed and post-observed.

### Phase 4 — controlled skill builder

```text
conversation-derived proposal
repo-derived proposal
manifest/passport preparation
test records
admission decision
separate installation and activation gates
```

## 15. Acceptance criteria

The candidate architecture is correctly implemented only when:

```text
the top-level navigation has exactly the five accepted professional spaces;
Pantheon opens as a contextual Hermes conversation;
an Affaire owns its project documents and project knowledge;
general knowledge remains separately scoped;
Outils preserves the real resource type behind common cards;
a Decision can appear in conversation, Décisions and Kanban without identity duplication;
a Work Issue can be visibly blocked by a Decision;
resolving a Decision does not falsely claim execution;
skill creation produces a proposal before installation;
installation and activation are separate;
no cockpit component becomes a scheduler, queue, plugin manager or approval engine;
all runtime changes are applied by Hermes or another admitted external adapter;
all consequential actions remain human-gated.
```

## 16. Repository status

```text
information architecture:
  candidate support doctrine
  documented non-implemented

Pantheon landing conversation:
  external cockpit candidate / to implement

Affaires and documents:
  partially represented in the external pantheon-mvp candidate
  exact accepted navigation not implemented

general Knowledge space:
  partially represented in the external pantheon-mvp candidate
  scope split to verify

Outils resource catalogue:
  candidate
  partial Hermes inventory exists externally
  governed mutation adapter not implemented

Décisions inbox:
  candidate
  Decision surface documented
  cross-surface Work Issue coupling not implemented

Kanban coupling:
  documented non-implemented
  must not be treated as a queue

governed skill builder:
  documented non-implemented
```

## 17. Exit and promotion criterion

This document remains candidate support doctrine until one of the following reviewed outcomes occurs:

```text
merge its stable navigation rules into PANTHEON_COCKPIT_UX_SPEC.md and CARD_STACK_MODEL.md;
adopt it as the named owner for cockpit information architecture;
replace it with an implemented external cockpit specification pinned to a reviewed commit;
or refuse it and record the replacement decision.
```

Promotion requires a referent under `AUTHORITY_INDEX.md`, such as an explicit human decision record, a reviewed end-to-end prototype, tests, or a read-only conformance surface.

## Final rule

```text
Pantheon is where the professional speaks with Hermes in a chosen context.
Affaires hold project work and documents.
Connaissances hold reusable general knowledge.
Outils expose governed operational resources.
Décisions expose what requires the human.
Hermes executes.
The human decides.
```
