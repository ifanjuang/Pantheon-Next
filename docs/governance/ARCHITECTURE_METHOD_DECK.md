# Architecture Method Deck

Status: candidate support doctrine — architecture-domain Method Cards for governed AI use in French architecture-agency workflows.

Runtime status: non-executable.

This document specializes `METHOD_CARD_MODEL.md` for architecture agency work.

It does not implement a UI, cockpit renderer, workflow engine, scheduler, queue, role executor, method selector, source validator, RAG system, OCR pipeline, PDF tool, email sender, approval engine, memory engine, Hermes skill, connector, schema, test or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Architecture work is consequential because a small AI error can become a wrong source, an implicit validation, a mission-scope expansion, a false proof, an unauthorized transmission or a professional commitment.

This deck turns generic Method Cards into professional cards that can be proposed by Roles during Runs.

Core rule:

```text
A method appears because a Role detects a tension.
It does not appear because it is intellectually interesting.
```

The visible cockpit should prefer professional method labels over raw reasoning labels.

```text
Show: mission_scope_guard
Do not show first: Hume / Chesterton / second-order thinking
```

Raw reasoning may remain inside the method card as internal support.

## Use model

A Run type may expose method affordances.

A Role proposes one when the task requires it.

```text
Run type
-> task
-> role detects tension
-> Method Proposal Candidate
-> bounded Hermes execution if needed
-> Result Candidate + Evidence Pack Candidate
-> Pantheon status / gate
-> human decision when consequential
```

Suggested cockpit budget:

```text
1 primary method;
1 guardrail method;
1 verification method;
other methods remain in the trace unless they change proof, scope, cost, status or action.
```

## Common fields

Each professional method card should define:

```text
id:
name:
purpose:
likely_roles:
trigger:
minimum_output:
evidence_delta:
scope_delta:
gate_triggers:
hermes_profile_hint:
forbidden_outputs:
stop_condition:
failure_modes:
visibility:
```

Allowed `evidence_delta` values:

```text
none;
adds_source;
qualifies_source;
resolves_conflict;
weakens_claim;
raises_question;
changes_confidence;
opens_gate.
```

Allowed `scope_delta` values:

```text
none;
clarifies_scope;
narrows_scope;
expands_candidate_scope;
detects_out_of_scope;
requires_mission_gate.
```

## Core professional method cards

### 1. source_admission

Purpose: prevent a received source from becoming trusted by default.

Likely Roles:

```text
ARGOS;
MAITRE;
ATHENA when preparing synthesis.
```

Trigger:

```text
new document, mail, quote, plan, photo, CR, PLU extract, CERFA, report, notice or dataset enters the task.
```

Minimum output:

```text
source type;
issuer / author;
date;
version / index;
project scope;
authority class;
applicability;
risk level;
recommended next step.
```

Evidence delta:

```text
qualifies_source;
raises_question if date, scope or issuer is uncertain.
```

Scope delta:

```text
clarifies_scope.
```

Gate triggers:

```text
source is used to support a consequential claim;
source is outdated, partial, commercial, derived or contradicted.
```

Hermes profile hint:

```text
doc-intake;
evidence-review.
```

Forbidden outputs:

```text
source validation;
professional conclusion;
external transmission;
canonical memory.
```

Stop condition:

```text
source is classified enough to decide whether analysis may proceed.
```

Failure modes:

```text
treating OCR, Markdown, summary or RAG chunk as equivalent to the signed source;
missing the source date or index;
using an example document as project authority.
```

### 2. authority_qualification

Purpose: decide which source has candidate priority when sources conflict.

Likely Roles:

```text
ARGOS;
THEMIS;
ZEUS if status arbitration is needed.
```

Trigger:

```text
two or more sources give different values, dates, clauses, amounts, statuses or decisions.
```

Minimum output:

```text
conflicting sources;
conflicting values;
relative authority;
source retained as candidate;
source rejected or downgraded;
remaining uncertainty;
question if arbitration is required.
```

Evidence delta:

```text
resolves_conflict;
changes_confidence;
raises_question if no source clearly prevails.
```

Scope delta:

```text
clarifies_scope.
```

Gate triggers:

```text
retained source affects payment, visa, reception, filing, client decision, enterprise instruction or memory promotion.
```

Hermes profile hint:

```text
evidence-review.
```

Forbidden outputs:

```text
final legal interpretation;
payment approval;
source canonization;
external instruction.
```

Stop condition:

```text
source precedence is proposed or a question is raised.
```

Failure modes:

```text
choosing the newest source even if it has lower authority;
trusting derived extraction over original document;
ignoring signed amendments.
```

### 3. assertion_mapping

Purpose: turn a candidate output into reviewable assertions.

Likely Roles:

```text
ARGOS;
ATHENA;
MAITRE.
```

Trigger:

```text
candidate report, email, note, visa, form, analysis, CR entry or synthesis contains factual or professional claims.
```

Minimum output:

```text
assertion;
source reference;
source status;
confidence;
contradictions;
risk if false;
allowed reuse scope.
```

Evidence delta:

```text
adds_source;
weakens_claim;
changes_confidence.
```

Scope delta:

```text
none by default;
clarifies_scope if assertions imply mission posture.
```

Gate triggers:

```text
an unsourced assertion supports consequential output.
```

Hermes profile hint:

```text
evidence-review;
governance-review.
```

Forbidden outputs:

```text
validated truth;
final proof;
external transmission.
```

Stop condition:

```text
important assertions are sourced, marked weak or escalated.
```

Failure modes:

```text
checking only explicit numbers and missing implicit commitments;
turning every minor sentence into bureaucracy;
not distinguishing style claims from factual claims.
```

### 4. contractual_decomposition

Purpose: decompose a contractual issue into clauses, lots, amounts, inclusions, exclusions and required decisions.

Likely Roles:

```text
THEMIS;
MAITRE;
ARGOS.
```

Trigger:

```text
quote, amendment, CCTP / CCAP clause, situation, invoice, claim, delay or scope dispute.
```

Minimum output:

```text
contract corpus used;
lot concerned;
clause or document reference;
prestation expected;
prestation claimed;
included / excluded / changed / unclear;
financial implication;
question or gate.
```

Evidence delta:

```text
adds_source;
resolves_conflict;
raises_question.
```

Scope delta:

```text
clarifies_scope;
detects_out_of_scope;
requires_mission_gate if agency posture may change.
```

Gate triggers:

```text
avenant;
client decision;
enterprise instruction;
payment validation;
claim rejection;
mission extension.
```

Hermes profile hint:

```text
architecture-domain;
evidence-review;
governance-review.
```

Forbidden outputs:

```text
final contractual decision;
order to enterprise;
financial approval;
legal advice framed as final.
```

Stop condition:

```text
contractual classification is candidate and reviewable.
```

Failure modes:

```text
reading contract in isolation from approved changes;
forgetting mission scope;
using generic public-market assumptions in private contracts without basis.
```

### 5. mission_scope_guard

Purpose: detect wording or action that may exceed the agency's mission or imply responsibility.

Likely Roles:

```text
THEMIS;
MAITRE;
ZEUS when gate is triggered.
```

Trigger:

```text
draft includes validate, approve, order, confirm, accept, guarantee, certify, fault, responsibility, payment, conformity, visa, OPC or insurance implications.
```

Minimum output:

```text
engaging wording or action;
possible implied commitment;
mission boundary concerned;
risk level;
safer formulation candidate;
gate required or not.
```

Evidence delta:

```text
weakens_claim;
opens_gate if output is consequential.
```

Scope delta:

```text
detects_out_of_scope;
requires_mission_gate.
```

Gate triggers:

```text
external transmission;
visa;
client validation;
enterprise instruction;
fault recognition;
mission extension;
insurance-related statement.
```

Hermes profile hint:

```text
governance-review.
```

Forbidden outputs:

```text
legal conclusion;
final responsibility decision;
external send;
canonical memory.
```

Stop condition:

```text
risk is removed, reformulated or sent to gate.
```

Failure modes:

```text
blocking harmless wording;
rewriting so cautiously that the message becomes unusable;
failing to distinguish draft preparation from transmission.
```

### 6. external_commitment_guard

Purpose: separate a prepared candidate from an action that affects outside parties.

Likely Roles:

```text
ZEUS;
THEMIS;
MAITRE.
```

Trigger:

```text
send email, file dossier, deposit form, publish CR, issue visa, notify enterprise, update external tracker, request payment or transmit document.
```

Minimum output:

```text
external action candidate;
recipient or affected party;
object of transmission;
approval required;
evidence required;
idempotency / duplicate risk;
allowed action state: draft only / ready for approval / blocked.
```

Evidence delta:

```text
opens_gate.
```

Scope delta:

```text
requires_mission_gate if professional commitment is possible.
```

Gate triggers:

```text
any external effect.
```

Hermes profile hint:

```text
governance-review;
repo-maintainer or connector-side profile only when bounded by explicit approval.
```

Forbidden outputs:

```text
automatic send;
automatic filing;
automatic merge;
automatic memory promotion.
```

Stop condition:

```text
external effect is blocked, approved, or converted back to draft-only.
```

Failure modes:

```text
treating a Gmail draft as a sent answer;
assuming user review equals external approval;
repeating an action without idempotency.
```

### 7. probative_review

Purpose: check whether an output is sufficiently supported for its intended effect.

Likely Roles:

```text
ARGOS;
ZEUS;
MAITRE.
```

Trigger:

```text
output may be used to justify decision, memory, transmission, payment, visa, reception, claim or professional advice.
```

Minimum output:

```text
claims reviewed;
sources checked;
missing evidence;
contradictions;
confidence;
allowed reuse scope;
remaining questions.
```

Evidence delta:

```text
changes_confidence;
weakens_claim;
opens_gate if support is insufficient.
```

Scope delta:

```text
none by default;
clarifies_scope if use context is limited.
```

Gate triggers:

```text
proof gap affects consequential output.
```

Hermes profile hint:

```text
evidence-review.
```

Forbidden outputs:

```text
proof validation;
Registre Probatoire entry;
external approval.
```

Stop condition:

```text
candidate support is sufficient for internal use, or gate/question is opened.
```

Failure modes:

```text
infinite verification;
checking citations without checking source authority;
collapsing confidence into truth.
```

### 8. phase_gate_review

Purpose: prevent phase progress from being treated as validated state without evidence and authorized decision.

Likely Roles:

```text
ZEUS;
MAITRE;
THEMIS.
```

Trigger:

```text
APS, APD, DP/PC, PRO, DCE, ACT, EXE/VISA, DET, AOR, DOE, GPA or archive state is about to change.
```

Minimum output:

```text
phase concerned;
expected deliverables;
evidence available;
evidence missing;
actor who may validate;
status: candidate / ready_for_review / blocked / validated externally.
```

Evidence delta:

```text
adds_source;
changes_confidence;
opens_gate.
```

Scope delta:

```text
clarifies_scope.
```

Gate triggers:

```text
phase state changes;
filed package;
client approval;
consultation launch;
visa issued;
reception pronounced;
reserves lifted.
```

Hermes profile hint:

```text
architecture-domain;
governance-review.
```

Forbidden outputs:

```text
phase validation;
filing;
client approval record;
canonical memory promotion.
```

Stop condition:

```text
phase state is classified and missing validation is visible.
```

Failure modes:

```text
confusing task completion with phase approval;
using incomplete evidence pack;
forgetting that contract-specific gates may differ.
```

### 9. site_observation_review

Purpose: qualify site observations from notes, photos, CR history or conversations before they become report points.

Likely Roles:

```text
ARGOS;
ATHENA;
MAITRE.
```

Trigger:

```text
photo, site note, oral report, enterprise message or repeated observation may enter a CR or reserve list.
```

Minimum output:

```text
observation;
location;
date / source;
related lot;
previous CR link;
status: new / maintained / closed / uncertain;
severity;
recommended CR wording;
question if location or fact is weak.
```

Evidence delta:

```text
adds_source;
weakens_claim if visual evidence is insufficient;
raises_question.
```

Scope delta:

```text
none by default;
clarifies_scope if observation implies instruction.
```

Gate triggers:

```text
reservation;
formal notice;
enterprise instruction;
responsibility implication.
```

Hermes profile hint:

```text
doc-intake;
evidence-review;
architecture-domain.
```

Forbidden outputs:

```text
technical diagnosis as final;
enterprise order;
formal reserve issuance without gate.
```

Stop condition:

```text
observation is candidate, supported, downgraded or turned into a question.
```

Failure modes:

```text
over-interpreting an image;
missing date or location;
closing a point contradicted by latest evidence.
```

### 10. quote_variation_review

Purpose: review additional, modified or disputed quotations without silent approval.

Likely Roles:

```text
THEMIS;
ARGOS;
MAITRE;
ATHENA for synthesis.
```

Trigger:

```text
complementary quote, variante, moins-value, plus-value, revised estimate or enterprise claim.
```

Minimum output:

```text
quote identity;
lot;
amount;
object;
contractual basis;
technical basis;
financial coherence;
missing detail;
status: receivable_candidate / not_receivable_candidate / to_justify / to_arbitrate.
```

Evidence delta:

```text
adds_source;
resolves_conflict;
raises_question;
changes_confidence.
```

Scope delta:

```text
clarifies_scope;
detects_out_of_scope;
requires_mission_gate if agency recommendation may engage.
```

Gate triggers:

```text
client recommendation;
avenant;
order;
payment;
refusal.
```

Hermes profile hint:

```text
architecture-domain;
evidence-review;
governance-review.
```

Forbidden outputs:

```text
approval;
enterprise instruction;
client decision;
final financial validation.
```

Stop condition:

```text
quotation posture is candidate and next decision is visible.
```

Failure modes:

```text
checking price without checking contract;
checking contract without checking site change;
forgetting approved client requests.
```

### 11. visa_commitment_review

Purpose: review EXE / VISA wording and status before it can imply validation beyond the intended professional posture.

Likely Roles:

```text
THEMIS;
MAITRE;
ZEUS.
```

Trigger:

```text
EXE document, technical detail, product sheet, method statement, shop drawing or note is prepared for visa or comment.
```

Minimum output:

```text
document identity;
issuer;
index;
object;
review perimeter;
comments;
reserved points;
wording risk;
visa status candidate;
gate required.
```

Evidence delta:

```text
adds_source;
weakens_claim;
opens_gate.
```

Scope delta:

```text
clarifies_scope;
requires_mission_gate.
```

Gate triggers:

```text
visa issuance;
acceptance-like wording;
technical conformity statement;
responsibility shift.
```

Hermes profile hint:

```text
architecture-domain;
governance-review.
```

Forbidden outputs:

```text
final visa;
technical guarantee;
enterprise instruction;
external send.
```

Stop condition:

```text
candidate review is ready for human visa decision or blocked.
```

Failure modes:

```text
validating performance not checked;
using too broad wording;
ignoring BET responsibility or required external expertise.
```

### 12. reception_risk_review

Purpose: identify the evidence, reservations and responsibility posture before reception or reserve lifting.

Likely Roles:

```text
ZEUS;
THEMIS;
ARGOS;
MAITRE.
```

Trigger:

```text
OPR, reception, reserve list, reserve lifting, GPA issue or handover.
```

Minimum output:

```text
works / lot concerned;
observed state;
evidence;
reserve candidate;
severity;
responsible party candidate;
missing confirmation;
reception implication;
gate required.
```

Evidence delta:

```text
adds_source;
weakens_claim;
opens_gate.
```

Scope delta:

```text
clarifies_scope;
requires_mission_gate if wording engages agency or client decision.
```

Gate triggers:

```text
reception pronounced;
reserve omitted;
reserve lifted;
GPA issue closed;
formal statement sent.
```

Hermes profile hint:

```text
evidence-review;
governance-review;
architecture-domain.
```

Forbidden outputs:

```text
pronouncing reception;
lifting reserve;
recognizing fault;
external notification without approval.
```

Stop condition:

```text
risk posture is candidate and human decision is isolated.
```

Failure modes:

```text
forgetting unresolved prior CR point;
confusing observation with contractual reserve;
closing a reserve without evidence.
```

### 13. cerfa_field_claim_review

Purpose: treat each sensitive form field as a claim requiring source, confidence and review status.

Likely Roles:

```text
ARGOS;
ATHENA;
MAITRE;
ZEUS if filing is near.
```

Trigger:

```text
CERFA, administrative form, DP/PC field, surface, parcel, address, applicant identity, work description or regulatory checkbox.
```

Minimum output:

```text
field;
value candidate;
source;
confidence;
contradiction;
comment;
missing information;
review requirement.
```

Evidence delta:

```text
adds_source;
raises_question;
changes_confidence;
opens_gate if filing is near.
```

Scope delta:

```text
clarifies_scope.
```

Gate triggers:

```text
administrative filing;
client signature;
external transmission.
```

Hermes profile hint:

```text
doc-intake;
architecture-domain;
evidence-review.
```

Forbidden outputs:

```text
filing;
signature-ready claim without review;
canonical project data mutation.
```

Stop condition:

```text
field is filled as candidate, commented, left blank or escalated.
```

Failure modes:

```text
using obsolete form version;
selecting between conflicting addresses silently;
using plan label when calculation disagrees.
```

### 14. constrained_generation

Purpose: generate useful drafts or creative variants while preserving source, mission, style and forbidden-effect constraints.

Likely Roles:

```text
ATHENA;
METIS;
HEPHAESTOS when production sequence matters;
THEMIS for guarded wording.
```

Trigger:

```text
draft email, notice, CR wording, client explanation, design variants, image prompts, synthesis or presentation text.
```

Minimum output:

```text
constraints used;
forbidden elements;
source dependence;
style / tone;
draft candidate;
points requiring review;
external-action status.
```

Evidence delta:

```text
none by default;
raises_question if draft introduces unsupported claim.
```

Scope delta:

```text
none by default;
detects_out_of_scope if generation overstates mission or authority.
```

Gate triggers:

```text
draft is intended for external use;
draft contains professional assertion;
draft changes project position.
```

Hermes profile hint:

```text
architecture-domain;
governance-review if external.
```

Forbidden outputs:

```text
external send;
final approved wording;
unsupported factual assertion;
mission expansion.
```

Stop condition:

```text
candidate draft exists with review points and forbidden effects respected.
```

Failure modes:

```text
clean prose hiding weak proof;
over-stylization;
creative drift from mission constraints.
```

## Anti-patterns

The deck must avoid method inflation.

```text
Do not activate a method because it sounds clever.
Do not expose runtime patterns as professional authority.
Do not use caution methods to block all production.
Do not use creative methods to escape proof.
Do not treat method success as proof or approval.
```

## Relationship with `METHOD_CARD_MODEL.md`

`METHOD_CARD_MODEL.md` defines the generic grammar.

This document defines architecture-domain cards using that grammar.

If a future machine-checkable schema is needed, it must be proposed separately and reviewed under protected-path rules before touching `schemas/`.

## Core invariant

```text
Architecture Method Cards guide professional AI work.
They produce candidates and gates.
They do not validate, approve, send, remember or execute.
```

The validated remains.
