# Card Stack Model

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines how governed objects are selectively exposed in a card-based cockpit. It does not define a new ontology, lifecycle vocabulary, runtime, workflow engine, approval engine or memory engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## Purpose

The Card Stack makes governance understandable on desktop and mobile without turning Pantheon into the engine.

It must let a user see, at the appropriate level of detail:

```text
where they are;
which Case, project and subject are active;
what treatment or review instance is being examined;
which sources and evidence candidates matter;
which gaps, gates and decisions remain open;
which action candidates exist;
what has been executed, retained, refused or superseded.
```

The Card Stack does not decide what exists. Owner documents and governed records do.

```text
The Card Stack defines exposure.
It does not define truth, authorization, execution or durable memory.
```

## Jurisdiction

```text
PANTHEON_GRAPH_MODEL
= generic grammar for governed nodes and relations

GOVERNANCE_OBJECT_RELATIONSHIP_MAP
= cross-domain responsibility map

CARD_STACK_MODEL
= bounded cockpit projection grammar

DECISION_SURFACE_SPEC
= decision-review specialization
```

If this document conflicts with an owner document, the owner document wins.

The Card Stack does not own the lifecycle or schema of:

```text
Case
Situation
Task Contract
Capability
Binding
Source
Derived Representation Candidate
Evidence Pack Candidate
Gate
Decision
Register Candidate
Register Entry
InstallationCandidate
HandoffDecision
ExecutionResultCandidate
HealthObservation
```

## Core definitions

```text
Governed entity or record
= underlying object with identity, scope, status and relations.

Card
= stable cockpit projection of one identifiable governed entity or record.

Scene
= filtered and ordered presentation of cards for one review purpose.

Deck
= vertical reading and depth order inside a Scene.

Constellation
= global relation view and project-switching surface.
```

One underlying entity may appear in several Scenes without becoming several entities.

```text
one entity
many bounded presentations
no identity duplication
```

A lifecycle state is not a card family. A relation is not automatically a card. A field becomes a visible sub-card only when it materially changes review or decision.

## Field-versus-sub-card rule

```text
Field when normal.
Sub-card when it blocks, fails, conflicts, repeats,
is newly proposed, changes scope or requires arbitration.
```

| Element | Default projection | Visible sub-card when |
|---|---|---|
| Role or symbolic quality | reference or field | conflict, handoff, missing expertise or arbitration |
| Method | reference | contested, changed, failed or consequential |
| Competence | reference | missing, proposed, repeatedly productive or failed |
| Rite | reference | a proof, mission, transmission or memory boundary is triggered |
| Risk | field | it blocks or raises the required decision level |
| Scope | field | it changes permitted use, responsibility or output |
| Action | Action Candidate | a consequential effect is proposed |
| Gate | Gate card | a consequential threshold is open |
| Decision | Decision card | a human determination has been recorded or is required |

Roles, gods, methods, competences and rites are references or bounded projections. They are not activated agents or hidden executors.

## Reference Space and Project Space

Pantheon Next is not modelled as a client project.

```text
Governance Reference Space
→ doctrine
→ controlled vocabulary
→ roles and symbolic qualities
→ methods
→ competences
→ rites
→ templates and guides
→ reusable documentary knowledge

Project Space
→ Cases and Situations
→ subjects and scopes
→ treatments or review instances
→ Task Contracts
→ project sources
→ candidate outputs
→ evidence candidates
→ gates and decisions
→ traces and governed records
```

`Run` remains reserved for a runtime execution instance. A professional or governance sequence shown in the cockpit is a `Treatment`, `Review Instance`, `Approach` or another owner-defined governance object.

Reusable references may be mobilized by a project without becoming project-owned truth.

## Primary cockpit views

Keep the first navigation level small.

### Work

Purpose: understand what is being produced and reviewed.

Typical projections:

```text
Case
Situation
Treatment or Review Instance
Task Contract
Task or review item
candidate output
open blocker
next governed action
```

The Work Scene is a bounded review projection. It is not the complete graph and is not required to display every mobilized reference simultaneously.

### Evidence

Purpose: assess support, contradiction, provenance and unresolved gaps.

Typical projections:

```text
assertion or claim
original Source
Derived Representation Candidate
Evidence Pack Candidate
gap
contradiction
reliance status
```

A simplified public label such as `Preuve` must not hide the exact underlying status.

### Assets

Purpose: access project sources and reusable reference material without confusing them with proof.

Typical projections:

```text
original document
source connection
project asset
derived representation
reusable documentary knowledge
template
guide
competence reference
method reference
```

### Decisions

Purpose: expose questions, gates, reviews, arbitrations and human decisions.

```text
Gate
= consequential threshold or control condition.

Decision
= explicit human determination within a declared scope.
```

A Gate may remain open, blocked or satisfied without a final Decision record. A Decision may resolve one or more Gates only within its stated scope.

### Trace

Purpose: show what occurred and what was retained without treating logs as proof.

Typical projections:

```text
runtime trace
retrieval trace
Decision Record
Register Candidate
Register Entry
supersession
revocation
obsolescence
```

### Reference Space

A separate global surface exposes reusable material:

```text
Competences
Methods
Templates and guides
Roles and symbolic qualities
Rites
Doctrine
Reusable documentary knowledge
```

The Constellation is a global mode, not another peer Scene in every project.

## Source, knowledge, evidence and Register separation

The cockpit must preserve the following distinctions:

| Object | Meaning | Project-owned by default? |
|---|---|---|
| Source | Raw, received, retrieved or observed material. | Depends on source. |
| Reusable documentary knowledge | Qualified professional or regulatory material reusable across Cases. | No. |
| Context | Minimum situated material used for the current task or review. | Scoped to the Case or Situation. |
| Evidence | Status-qualified support or contradiction for a scoped Assertion. | Scoped to the Assertion and use. |
| Register Candidate | Proposed durable retention after review. | Scoped until decided. |
| Register Entry | Human-approved durable governed retention. | Scoped and versioned. |
| Competence | Reusable governed ability. | No. |
| Guide or Resource | Material supporting a Competence. | No. |
| Template | Reusable output form. | No. |

```text
Source != Evidence
Reusable knowledge != Evidence
Evidence != Register Entry
Record present != durable promotion
```

A reusable knowledge item may support a project Assertion only through a scoped Evidence projection that keeps the original source, authority, freshness and limitations visible.

Example:

```text
PLU corpus or qualified rule note
→ reusable documentary knowledge
→ scoped excerpt used for one project Assertion
→ Evidence Candidate
→ Gate or Human Decision
→ optional Register Candidate
```

Project-specific emails, plans, photographs, quotations and reports remain Sources or project Assets. They do not become reusable knowledge merely because they were ingested or displayed.

## Role-quality visibility

A Role or God card represents a governance guardian, not an activated agent.

A role quality becomes visible only when it changes at least one of:

```text
status;
risk;
wording;
evidence requirement;
missing information;
next safe action;
consultation;
rite request;
arbitration;
gate.
```

If a quality only decorates, comments or restates the obvious, it remains hidden.

A compact role-quality projection may show:

```text
role and jurisdiction;
visible quality expression;
reason for visibility;
warning, tactic, consultation or Gate request;
impact on status, evidence, wording or action;
linked Gate or next review action.
```

```text
role quality expression != agent invocation
warning != Decision
consultation trace != hidden chain-of-thought
Gate request != Gate completion
```

## Navigation grammar

One gesture should keep one stable meaning.

```text
Constellation or project selector
= change Project Space.

Rail or tabs
= change primary cockpit view.

Vertical
= read or descend the Deck.

Horizontal
= move between sibling cards or branches at the current level.

Tap
= open governed detail or recto/verso view.

Long press
= open a bounded action menu or prepare an Action Candidate.
```

Horizontal navigation does not generically mean `alternative`; siblings may be tasks, sources, evidence candidates, decisions or branches.

A long press must not directly archive, merge, approve, send, install, activate or promote memory.

Permitted generic outcomes include:

```text
open details;
copy reference;
request source;
request review;
prepare Action Candidate;
open relevant Gate.
```

Consequential effects remain gated.

## Card contract

Every card has a compact recto and a reviewable detail view.

### Recto

```text
title;
underlying object kind;
scope;
owner-defined status projection;
risk or consequence indicator;
one-line summary;
next review action;
Gate indicator where relevant.
```

### Detail view

```text
identity and definition;
source or origin;
exact status axes and their owner;
main typed relations;
provenance and evidence references;
open contradictions or gaps;
history and supersession;
permitted candidate actions;
limits and non-equivalences.
```

The Card Stack must not invent a parallel lifecycle vocabulary. It displays status axes owned by the underlying object, schema or doctrine.

## Status projection

Process, governance, authorization, evidence and operational posture remain independent.

Illustrative axes may include:

```text
process posture;
governance maturity;
authorization posture;
evidence posture;
operational posture;
update posture.
```

Exact values remain owner-defined.

```text
process_success != governance_validation
governance_validation != execution
runtime_success != evidence
healthy != safe
approved != activated
record_present != Register Entry
Register Candidate != Register Entry
```

No card-level aggregate score may silently collapse these axes.

## Typed relations

Cards expose only the relations needed for the current review.

Common relation projections include:

```text
parent;
scoped_to;
derived_from;
supported_by;
contradicted_by;
produces;
blocks;
resolved_by;
supersedes;
observes;
proposes_action.
```

The Graph Model remains owner of generic relation grammar. The Card Stack controls visual selection, ordering and density only.

Recto shows at most the dominant relation. Detail view shows useful bounded relations. Constellation may show a broader graph projection.

## Answer-first default

Comprehensiveness must remain available, but it must not be the default landing screen.

The default Work view should prioritize:

```text
main candidate output;
main open Gate;
top supporting or contradicting Evidence;
next permitted action;
current scope and unresolved gap.
```

The complete Deck, secondary sources, role-quality expressions, traces and reference material remain available on demand.

```text
complete enough for governed review != exhaustive graph
answer_first != hidden evidence
```

## Governed interaction chain

A UI interaction must not become an implicit runtime command.

```text
user interaction
→ bounded UI intent
→ candidate object or review request
→ Gate and Human Decision when consequential
→ exact authorized handoff
→ external execution by Hermes Agent or another approved runtime
→ result and observation returned as candidates
```

Forbidden shortcut:

```text
card click
→ hidden execution
```

Pantheon governs the underlying scope, status, evidence, decision and authorization. OpenWebUI exposes bounded card projections. Hermes Agent executes only an explicit, scoped and currently authorized handoff.

## Current Decision Resolver boundary

A future Current Decision Resolver is upstream from the cockpit.

```text
Decision Records
+ scope
+ time
+ supersession
+ revocation
+ expiration
→ read-only current-decision projection
→ Card Stack display
```

The Card Stack must not calculate, infer or own the applicable decision. It only displays the resolver output and supporting reasons.

```text
UI projection != decision engine
resolver_output != execution
current_approval != perpetual_permission
```

## Minimum first prototype

The first practical cockpit test must not implement every card family.

Minimum bounded set:

```text
Context or scope projection;
Treatment or Review Instance projection;
Document or Source card;
Evidence Candidate card;
Role-quality card only when consequential;
Candidate Output card;
Action Candidate card;
Gate card;
Decision card when present;
Trace card.
```

Success criterion:

```text
The user can see what was used,
what remains uncertain,
what candidate output was produced,
what action is still only candidate,
which Gate remains open,
and what the human must decide.
```

## Mobile constraints

The default mobile surface should prioritize:

```text
current Case and scope;
main candidate output;
main supporting or contradicting source;
open Gate;
required human Decision;
next permitted action.
```

Detailed traces, secondary relations and reference material remain accessible on demand.

A Scene should be complete enough for governed review, not exhaustive of the complete relation graph.

## Responsibility allocation

| Concern | Pantheon Next | Hermes Agent | OpenWebUI | Human |
|---|---|---|---|---|
| Object and relation status | governs and records | reports candidates and observations | exposes bounded projections | reviews consequential status |
| Execution | does not execute | executes explicit bounded handoff | does not execute through display alone | authorizes where required |
| Evidence | governs criteria and reliance status | returns sources and candidates | exposes provenance and gaps | decides sufficiency and reliance |
| Gates and Decisions | governs thresholds and records | does not self-approve | exposes review surface | decides consequential outcomes |
| Memory | governs promotion boundary | may propose candidates | exposes retention status | approves durable promotion |
| External action | governs scope and authorization | performs only after authorization | exposes candidate and decision | authorizes consequence |

## Owner-document map

| Area | Owner document(s) |
|---|---|
| Controlled terminology | `TERMINOLOGY_BOUNDARIES.md`, `CORE_CONCEPTS_MAP.md` |
| Case and Task Contract | `CORE_CONCEPTS_MAP.md`, `TASK_CONTRACTS.md` |
| Capability and placement | `UNIFORM_CAPABILITY_GOVERNANCE.md`, `CAPABILITY_PLACEMENT.md` |
| Bindings | `ADAPTERS_AND_BINDINGS.md` |
| Generic relations | `PANTHEON_GRAPH_MODEL.md` |
| Cross-domain responsibilities | `GOVERNANCE_OBJECT_RELATIONSHIP_MAP.md` |
| Sources and derivatives | `RAW_DERIVED_GOVERNED_RECORDS.md`, `DOCUMENT_INTELLIGENCE.md` |
| Knowledge, competence and resources | `TERMINOLOGY_BOUNDARIES.md`, `COMPETENCE_MODEL.md`, `KNOWLEDGE_TAXONOMY.md` |
| Evidence | `EVIDENCE_PACK.md`, `EVIDENCE_TOPOLOGY.md` |
| Gates and approvals | `APPROVALS.md`, `USER_DECISION_GATE.md` |
| Memory and scope | `MEMORY.md`, `SCOPE_ISOLATION.md` |
| Decision review specialization | `DECISION_SURFACE_SPEC.md` |
| Roles and symbolic college | `AGENTS.md`, `GOVERNANCE_COLLEGE.md` |

## Semantic reduction audit

The prior long document contained two absorbed alignment sections. Their unique rules are retained here as follows:

| Former material | Retained location |
|---|---|
| source / Connaissance / Evidence / Register separation | `Source, knowledge, evidence and Register separation` |
| non-project reusable documentary corpus | `Reference Space`, `Assets`, and separation table |
| role-quality visibility and non-agent boundary | `Role-quality visibility` |
| gesture boundaries | `Navigation grammar` |
| answer-first landing | `Answer-first default` |
| minimal first test card set | `Minimum first prototype` |
| card inflation warning | `Field-versus-sub-card rule` and Core invariants |

Detailed legacy walkthroughs and card field examples remain recoverable from repository history and the reconciliation log. They are examples, not owner doctrine, and are not repeated in the compact model.

## Core invariants

```text
card != underlying object schema
scene != workflow
scene != complete graph
deck != sequence of scenes
constellation != graph runtime
role card != agent invocation
rite card != executable workflow
method selected != reasoning validated
source != evidence
reusable knowledge != evidence
Evidence Pack Candidate != professional proof
Gate != Decision
Decision recorded != action performed
long_press != authorization
card_visible != scope_authorized
UI intent != runtime command
runtime_success != evidence
record_present != Register Entry
merged_document != promoted_doctrine
```

## Implementation status

```text
implemented:
- this documentation model;
- static prototypes elsewhere in the repository.

partial:
- bounded read-only projections in existing verification surfaces.

documented non-implemented:
- production Card Stack renderer;
- Scene and Deck state model;
- Constellation interaction;
- authenticated Decision surface integration;
- current-decision projection;
- live Hermes handoff integration.

forbidden by this document:
- hidden execution from card interaction;
- automatic approval;
- automatic memory promotion;
- Card Stack-owned status or decision engine.
```

## Promotion condition

This document remains candidate support doctrine.

Indexing, CI success, a prototype or merge does not promote it. Promotion requires explicit human decision after owner-document review and practical cockpit testing.
