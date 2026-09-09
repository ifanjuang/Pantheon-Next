# Context Stack

Status: candidate support doctrine — dynamic context-card stack and context sufficiency watch.
Boundary profile: candidate_support_note.

Runtime status: non-executable.

This document defines a governed model for composing, reviewing and adapting the visible context used by a professional cockpit, assistant surface or execution runtime.

It does not implement a UI, dashboard, context engine, retrieval engine, router, scheduler, queue, agent loop, context optimizer, automatic approval system, automatic memory promotion, Hermes skill, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action or external runtime behavior.

## Purpose

A professional question rarely needs the whole dossier, and it should not be answered from a single flat context blob.

A response about a site delay, a PLU question, a CCAP review, a visa EXE, a client-facing email or a memory proposal each needs a different set of contextual cards.

The Context Stack defines how Pantheon may govern that visible, task-bounded set of context cards without turning context into evidence, memory, doctrine or runtime state.

## Core rule

```text
Context prepares work.
Evidence supports review.
Approval legitimizes consequential change.
Memory preserves validated material.
```

A Context Stack is a dynamic set of context cards selected for a question, subject, dossier, task or workflow candidate.

It must make visible:

- which context is currently active;
- why each context card is needed;
- which scope each card belongs to;
- which context is missing, stale, excessive or mixed;
- which action is permitted, limited or blocked because of the context state.

## Relationship to Context Packs

`CONTEXT_PACKS.md` defines the governed bundle prepared for a target surface, assistant or runtime.

A Context Stack is the cockpit-facing composition model that may feed, justify or constrain a Context Pack.

```text
Context Stack  -> visible, dynamic, card-based context composition.
Context Pack   -> bounded context bundle prepared for a target tool or surface.
Evidence Pack  -> reviewable proof package after execution.
```

A Context Stack is not an Evidence Pack.

A Context Stack is not memory.

A Context Stack is not a hidden system prompt.

A Context Stack is not runtime state.

A Context Stack must not silently merge project context, agency practice, domain knowledge, user preference, retrieved material and doctrine.

## Context card families

A Context Stack may contain several context card families. The list is not fixed. It is selected according to the question and risk level.

Common families:

```text
Project Context
Subject Context
Phase Context
Location Context
Typology Context
Regulatory Context
Contractual Context
Technical Context
Document Context
Relationship Context
Temporal Context
Risk Context
Action Context
Memory Context
Transmission Context
```

### Project Context

Used to frame the dossier.

Typical fields:

```text
dossier
project alias
client or masked client reference
mission scope
phase
location
project typology
actors
known constraints
open subjects
key dates
```

### Subject Context

Used to frame the current issue or question.

Typical fields:

```text
subject
trigger
request or reproach
known facts
unknowns
related documents
related evidence
risk level
expected output
```

### Location Context

Used when geography changes the answer.

Typical fields:

```text
commune
address or masked reference
parcel reference when authorized
planning authority
heritage or protected perimeter signal
risk-zone signal
external source freshness
```

### Typology Context

Used when project type changes rules, methods or risk.

Typical fields:

```text
new build
renovation
extension
surlevation
change of destination
housing
ERP
workplace
heritage building
site condition
```

### Regulatory Context

Used when a question may depend on PLU, DTU, ERP, accessibility, fire safety, PPRI, ABF, ANC, servitudes, public APIs or another external rule.

Typical fields:

```text
applicable rule candidate
source reference
version or date
source status
freshness
scope of applicability
open verification point
```

### Contractual Context

Used when mission scope, market documents or responsibility may affect the answer.

Typical fields:

```text
mission phase
contract scope
excluded scope
CCAP / CCTP / AE references
validated documents
instruction chain
responsibility boundary
approval or delivery requirement
```

### Technical Context

Used when the answer depends on design, construction, structure, fluids, materials, details, support condition or site state.

Typical fields:

```text
plans
photos
site reports
BET notes
technical constraints
support condition
interfaces
uncertainties
source confidence
```

### Temporal Context

Used when dates, deadlines, prescription, purge, reception, site planning, index, version or chronology matter.

Typical fields:

```text
key date
source date
deadline
phase date
document index date
chronology tension
staleness warning
```

### Risk Context

Used when the task may affect responsibility, cost, delay, insurance, safety, compliance, client relation, external transmission or memory.

Typical fields:

```text
risk family
risk severity
trigger
what may go wrong
safe fallback
approval requirement
blocked effect
```

### Action Context

Used when a draft, note, email, form, filing package, repository change, memory proposal or external communication is expected.

Typical fields:

```text
expected output
recipient or target
internal or external effect
allowed output status
forbidden output status
required evidence
approval ceiling
transmission state
```

## Context item status

Each context item should carry a status. A Context Card may mix items with different statuses, but it must not hide that mixture.

Recommended statuses:

```text
established
candidate
to_verify
missing
contradicted
obsolete
stale
out_of_scope
mixed_scope
excessive
sensitive
```

These are governance-readable signals.

They are not runtime commands.

## Context sufficiency

A Context Stack should answer what the current context is sufficient for.

Recommended sufficiency states:

```text
sufficient_for_orientation
sufficient_for_draft
sufficient_for_internal_review
insufficient_for_source_backed_claim
insufficient_for_external_action
insufficient_for_memory_promotion
insufficient_for_canonical_status
blocked_by_missing_context
blocked_by_scope_conflict
blocked_by_stale_context
```

Example:

```text
Context sufficient for draft: yes.
Context sufficient for external transmission: no.
Context sufficient for memory promotion: no.
```

## Context Stack Change Candidate

When the active context is not appropriate for the question or task, the system may surface a Context Stack Change Candidate.

It is a proposal, not execution.

Minimum shape:

```text
context_stack_change_candidate:
  id:
  origin:
  trigger:
  current_question:
  current_subject:
  current_stack:
  proposed_additions:
  proposed_removals:
  proposed_scope_limits:
  reason:
  risk_if_ignored:
  affected_outputs:
  affected_evidence_expectations:
  approval_or_gate_impact:
  ZEUS_status: accepted | refused | to_verify | to_arbitrate
  human_decision_required: true | false
  trace_refs:
```

Typical triggers:

```text
regulatory_claim_requested
external_transmission_requested
memory_promotion_requested
source_conflict_detected
scope_mixed
context_stale
target_referent_ambiguous
reasoning_dependency_unestablished
project_specific_fact_used_as_general
knowledge_needed_but_absent
technical_consequence_detected
contractual_risk_detected
question_changes_phase
workflow_advances
```

Typical changes:

```text
add_context_card
remove_context_card
limit_scope
split_context
request_source
open_decision_gate
block_external_action
allow_draft_only
create_capability_gap
```

## HESTIA — candidate context watch role

HESTIA is a candidate role for UX and context-watch purposes.

HESTIA is not yet promoted to the canonical role registry.

HESTIA does not validate sources.

HESTIA does not produce Evidence.

HESTIA does not approve, transmit, canonize, promote memory or execute work.

HESTIA watches the Context Stack and may propose Context Stack Change Candidates. Her candidate jurisdiction is the situated validity of the working context: the active Project/Case, phase, location, target referent or bounded target set, scope, relevance, freshness and sufficiency needed for the requested level of answer.

Useful bias:

```text
situated referent grounding, context sufficiency, context scope,
context relevance, context staleness and context overload
```

A referent may legitimately remain a bounded candidate set. HESTIA must not convert several plausible governed identities into one selected identity merely to make reasoning easier.

May propose:

```text
add missing context
remove irrelevant context
limit scope
mark mixed scope
mark a target referent unresolved
preserve a bounded target candidate set
request targeted clarification when target distinction materially affects the allowed answer
flag stale context
ask ATHENA which candidate dependencies or dimensions could materially change the reasoning
ask MNEMOSYNE whether prior naming, discussion or project history helps frame the referent
ask ARGOS to verify source state
ask THEMIS to review risk created by missing context
ask ZEUS to arbitrate sufficiency or blocking status
```

May challenge:

```text
answering from too little context
silently selecting one identity from several plausible candidates
treating a colloquial alias as a governed identity without support
loading the whole project to resolve a local referent
using project facts as general knowledge
using general knowledge without project fit
mixing agency preference with doctrine
using stale context as if current
loading too much dossier material without need
```

May block or escalate only as a governance signal:

```text
context_insufficient_for_external_action
context_insufficient_for_memory_promotion
context_scope_conflict
context_stale_for_regulatory_claim
context_overloaded
target_referent_materially_ambiguous
```

HESTIA does not decide by herself which possible context dimension is materially consequential to the substantive reasoning. ATHENA may propose those reasoning dependencies; HESTIA watches whether the corresponding situation, referent and context are sufficiently established for the intended answer status.

```text
referent candidate set != merged identity
context available != context relevant
context relevant != context sufficient
context sufficient != source true
```

Final arbitration remains with ZEUS.

The human decides when a User Decision Gate is required.

## Role relationship

Context watch does not replace existing roles.

```text
ATHENA structures the task, hypotheses, reasoning dependencies and candidate projections.
ARGOS challenges source state and provenance.
MNEMOSYNE challenges stale/superseded prior state and may expose relevant naming/history.
THEMIS challenges risk, liability and approval boundaries.
APOLLO challenges clarity and delivery readiness.
HEPHAISTOS prepares artifact candidates.
IRIS challenges transmission conditions.
ZEUS arbitrates status and next procedure.
HESTIA, if adopted, watches situated referent, context sufficiency and scope.
```

If HESTIA reveals a missing source, ARGOS should review source sufficiency.

If HESTIA reveals a stale or historically ambiguous designation, MNEMOSYNE may frame the relevant prior state or naming context without turning memory into truth.

If HESTIA reveals a risk-bearing gap, THEMIS should review consequence.

If HESTIA reveals no safe procedure, ZEUS should arbitrate or escalate to the user.

### Reasoning-context loop

For a situated professional question, context sufficiency and reasoning may legitimately form a short bounded loop without becoming a router, graph engine or autonomous agent loop:

```text
ATHENA
  -> propose explicit hypotheses and the bounded dimensions that could materially change the answer

CONTEXT STACK / HESTIA candidate
  -> expose whether the corresponding Project, referent, typology, location, technical,
     regulatory, contractual or actor context is established, missing, stale or ambiguous

ARGOS / MNEMOSYNE when needed
  -> verify source state or frame relevant prior state/history through admitted routes

ATHENA
  -> resume candidate consequence / risk / scenario / solution projection with the now-bounded context

THEMIS when triggered
  -> challenge responsibility, competence, policy or applicability boundaries

ZEUS only when needed
  -> arbitrate status or procedure if competing paths remain materially unresolved
```

This loop does not require every role on every request. It should stop as soon as the context is sufficient for the intended answer status or the remaining uncertainty is explicitly carried.

```text
candidate reasoning dependency != established project fact
projection != persistence
possible risk != established non-compliance
possible solution != design decision
successful retrieval != Evidence
```

## Proportional activation

The full Context Stack should not appear for every question.

Use the minimum effective context required by:

```text
question type
subject type
phase
risk
external effect
memory impact
source dependency
scope breadth
```

Examples:

| Question type | Likely minimum Context Stack |
|---|---|
| simple reformulation | Subject Context + Action Context |
| client-facing email | Subject Context + Relationship Context + Risk Context + Action Context |
| PLU question | Project Context + Location Context + Typology Context + Regulatory Context |
| DTU / technical issue | Subject Context + Technical Context + Document Context + Risk Context |
| CCAP / contract issue | Project Context + Contractual Context + Document Context + Risk Context |
| visa EXE | Phase Context + Technical Context + Contractual Context + Document Context + Action Context |
| situated object / change-impact question | Subject Context + Project Context + Technical Context, then only the relation/regulatory/history cards materially required |
| memory proposal | Subject Context + Evidence Context + Scope Context + Memory Context |
| external transmission | Action Context + Transmission Context + Risk Context + Approval Context |

## Architecture examples

### Client-facing response about hedge, claustra and privacy

Initial stack:

```text
Subject Context
Action Context
```

HESTIA candidate signal:

```text
The question may depend on project history, ANC/SPANC constraints, PLU/clôture rules, client validation, relation risk and external transmission.
```

Proposed additions:

```text
Project Context
Location Context
Regulatory Context
Technical Context
Contractual Context
Relationship Context
Risk Context
Transmission Context
```

Possible ZEUS status:

```text
allow_draft_only
block_external_action_pending_source_review
```

### Visa EXE coordination question

Initial stack:

```text
Subject Context
Document Context
```

Proposed additions:

```text
Phase Context
Technical Context
Contractual Context
Risk Context
Action Context
```

Reason:

```text
A visa response may depend on mission scope, plan indices, technical interfaces and whether the answer could be read as synthesis or approval.
```

Possible ZEUS status:

```text
source_required
approval_required_before_external_response
```

### PLU-based question

Initial stack:

```text
Subject Context
```

Proposed additions:

```text
Location Context
Typology Context
Regulatory Context
Knowledge references
```

Reason:

```text
A planning answer may change with commune, zone, document version, typology and project scope.
```

Possible ZEUS status:

```text
insufficient_for_source_backed_claim until dated source and zone are verified
```

### Situated project referent and consequence question

Examples include `cette porte doit être réglée` from a photo, `quel meuble est prévu dans la salle de bain enfant ?` when plans say `SDB A` / `SDB B`, or `si on décale la porte du bureau 1, est-ce que cela fonctionne ?`.

The minimum handling is not a global project traversal:

```text
human designation / photo / local question
-> bounded referent candidate(s) from admitted project context
-> preserve several candidates if the designation is not yet determining
-> ATHENA identifies only the consequence dimensions that could materially change the answer
-> add only the corresponding context cards
-> clarify the referent only when the distinction changes the permitted conclusion
```

For the office-door example, an evacuation-distance or ERP dependency may justify Regulatory/Typology Context; a known BET or prior opinion may justify Project/Document/Memory Context. Those cards are added because the reasoning exposes a dependency, not because every architectural question loads every available dossier fact.

## UX projection

The cockpit may display the Context Stack as cards.

Allowed display behavior:

```text
show active context cards
show missing context
show context sufficiency
show scope and status badges
show why a context card was added
show Context Stack Change Candidates
show ZEUS status
request user decision when required
```

Forbidden display behavior:

```text
hide scope mixing
show context as proof
show a retrieved source as validated evidence
silently promote context into memory
silently expand across projects
silently authorize external action
```

A useful card header should expose:

```text
Context family
Scope
Status
Freshness
Risk if wrong
Sufficiency impact
Next check
```

## Boundaries

A Context Stack must not:

```text
execute work
route tools
schedule retrieval
decide source truth
replace Evidence Pack
replace Task Contract
replace User Decision Gate
promote memory
authorize external action
become a hidden prompt dump
become a runtime state store
```

If the context is insufficient, the safe result is one of:

```text
ask for source
mark limitation
allow draft only
open User Decision Gate
create Capability Gap
block external action
```

## Minimal checklist

Before using a Context Stack for consequential work, verify:

```text
1. The question is stated.
2. The active subject is identified.
3. The project referent or bounded candidate set is visible when the question is situated.
4. Scope is visible.
5. Project-specific and general material are separated.
6. Missing context is marked.
7. Stale or non-dated context is marked.
8. Source-dependent claims point to sources or Evidence expectations.
9. The expected output status is visible.
10. Any external effect is blocked unless approval path exists.
11. Any memory effect remains candidate until validation.
```

## Status and next review

This document is candidate support doctrine.

It should be reviewed against:

```text
CONTEXT_PACKS.md
SCOPE_ISOLATION.md
GOVERNANCE_COLLEGE.md
USER_DECISION_GATE.md
DOSSIER_SITUATION_INTAKE.md
PANTHEON_COCKPIT_UX_SPEC.md
```

Open questions:

```text
Should HESTIA become a canonical Pantheon Role, or remain a cockpit-facing context-watch label?
Should situated referent grounding remain a HESTIA quality if HESTIA is promoted, or stay a shared clarification function?
Should Context Stack Change Candidate receive a schema later?
Should Context Card families be standardized in the architecture domain pack first?
How much of this belongs in cockpit UX versus general doctrine?
```
