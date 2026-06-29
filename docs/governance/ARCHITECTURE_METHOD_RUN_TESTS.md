# Architecture Method Run Tests

Status: candidate support examples — architecture-domain run tests for Method Cards, Hermes handoff and cockpit display.

Runtime status: non-executable.

This document tests whether Method Cards, Hermes handoff discipline and the Card Stack cockpit grammar are usable in real architecture-agency situations.

It does not implement a workflow engine, Hermes skill, UI, schema, approval engine, memory engine, connector, scheduler, queue or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next must not increase the number of things to see.

It must reduce confused decisions.

These run tests verify whether Pantheon can transform a professional request into a controlled decision surface.

Core questions:

```text
Is it true?
Is it sourced?
Is it inside our mission scope?
Can it leave the cockpit?
```

A run test does not prove that the UI works.

It tests whether the governance grammar is usable.

## What this document tests

Each test verifies:

```text
the user intent;
the professional risk;
the expected candidate output;
the forbidden final effects;
the failure signal;
the role that detects the tension;
the method proposed;
the Hermes handoff boundary;
the returned candidate;
the visible cockpit cards;
the gate;
the expected human decision.
```

## Core operating model

```text
User request
-> Run opened
-> Task created
-> Responsible Role assigned
-> Initial method or method affordance selected
-> Hermes executes bounded task
-> Result Candidate returned
-> Evidence / scope / confidence threshold checked
-> If weak: Role proposes Method Proposal Candidate
-> Pantheon qualifies effect
-> Hermes may rerun bounded task
-> Gate opens if consequential
-> Human decides
```

Hermes is never the professional responsible role.

```text
Role observes.
Method structures.
Competence produces.
Hermes executes.
Evidence supports.
Gate authorizes or blocks.
Human decides.
```

## Failure taxonomy

Pantheon should not rerun Hermes with a vague instruction such as `do better`.

It must first classify the failure.

| Failure type | Typical signal | Method family |
|---|---|---|
| source_missing | required document absent | source_admission |
| source_weak | source exists but is partial, stale or unclear | source_admission / probative_review |
| source_conflict | two sources contradict each other | authority_qualification |
| claim_unsourced | assertion has no support | assertion_mapping / probative_review |
| contract_scope_unclear | prestation unclear against CCTP / CCAP / AE | contractual_decomposition |
| site_observation_weak | photo or note cannot support a CR point | site_observation_review |
| quote_or_payment_risk | amount, scope or receivability unclear | quote_variation_review |
| field_as_claim_weak | CERFA field filled without sufficient support | cerfa_field_claim_review |
| scope_risk | wording may exceed mission | mission_scope_guard |
| external_action_risk | draft may be sent, filed or transmitted | external_commitment_guard |
| task_too_broad | task cannot be executed cleanly | decomposition / HEPHAISTOS |
| bad_framing | question produces bad or trivial answer | problem_repositioning / METIS |
| output_too_vague | candidate is not actionable | constrained_generation / synthesis review |
| memory_risk | candidate may be promoted too early | memory_promotion_gate |

## Method selection rule

A Role does not choose a method because it is intellectually interesting.

A Role proposes a method because it detects a tension inside its jurisdiction.

```text
ARGOS chooses by proof.
THEMIS chooses by scope and responsibility.
ATHENA chooses by clarity and synthesis.
HEPHAISTOS chooses by decomposition and execution feasibility.
METIS chooses by reframing and oblique movement.
ZEUS chooses by threshold and arbitration.
```

## Handoff levels

Pantheon should distinguish the proposal from the executable instruction.

### Handoff Candidate

```text
why rerun?
which role proposes it?
which method is proposed?
what failure does it address?
what gain is expected?
what cost or density does it add?
what is forbidden?
does it change proof, scope, memory or external action?
does it require Zeus or human gate?
```

### Executable Hermes Handoff

```text
Task Contract
+ Context Pack
+ Method Card or Method Proposal Candidate
+ allowed sources
+ allowed outputs
+ forbidden outputs
+ approval ceiling
+ stop condition
-> Hermes execution
-> Result Candidate + Evidence Pack Candidate + Trace References
```

Hermes may execute the bounded work.

Hermes may not convert method success into proof, approval, memory or external action.

## Visibility budget

The cockpit should default to:

```text
answer-first;
evidence-on-demand;
gate-always-visible.
```

A task should normally expose no more than:

```text
one primary method;
one guardrail method;
one verification method;
one main gate;
two or three critical proofs or gaps.
```

Everything else belongs in the verso, trace or constellation.

## Visibility levels

| Level | Display | Use when |
|---|---|---|
| trace only | hidden in history | method was used but did not change the task |
| field | visible line on task | method structures normal work |
| chip | compact marker | method helps explain the task |
| sub-card | visible card | method is proposed, contested, failed, repeated or changes output |
| gate | decision surface | method reveals a consequential threshold |

## Gate rule

Gate is required before:

```text
external transmission;
client validation;
enterprise instruction;
visa;
administrative filing;
payment;
reception;
reserve lifting;
canonical memory;
mission extension;
fault recognition.
```

A gate is not an alert.

A gate blocks a threshold until decision.

## Test Case A — Chantiers, compte rendu de visite

### Run Test Contract

```text
Use case:
CR chantier

User intent:
Preparer un compte rendu exploitable a partir de notes, photos et precedent CR.

Professional risk:
Une observation faible devient une affirmation formelle.

Expected candidate:
Draft CR + uncertain points + draft email.

Forbidden final effects:
send email;
issue instruction;
create reserve;
canonical memory;
client or enterprise commitment.

Main gates:
external transmission;
professional assertion;
reserve / responsibility.

Success condition:
The user can decide: send / correct / ask source / block.
```

### User request

```text
Prepare le compte rendu de chantier a partir de mes notes, photos et du precedent CR.
```

### Initial task chain

| Step | Task | Responsible role | Method | Competence | Runtime | Visibility |
|---:|---|---|---|---|---|---|
| 1 | Qualify inputs | ARGOS | source_admission | document intake | Hermes | chip |
| 2 | Compare previous CR | ARGOS | site_observation_review | CR comparison | Hermes | field |
| 3 | Classify points | ATHENA | assertion_mapping | synthesis | Hermes | field |
| 4 | Draft CR | ATHENA | constrained_generation | professional drafting | Hermes | field |
| 5 | Check mission wording | THEMIS | mission_scope_guard | responsibility boundary | Hermes | sub-card if risky |
| 6 | Prepare draft email | ATHENA / MAITRE | external_commitment_guard | draft production | Hermes | gate |
| 7 | Decide transmission | ZEUS / human | gate_review | decision | none until approved | gate |

### Thresholds

```text
source identified;
photo dated or uncertainty marked;
location confirmed or gap opened;
previous CR checked;
new / maintained / closed status assigned;
no enterprise instruction implied;
external send blocked until gate.
```

### Failure signal

```text
A photo is used to describe a defect, but the location is uncertain.
```

### Method Proposal Candidate

```yaml
proposingRole: ARGOS
detectedProblem: visual evidence too weak to support a CR assertion
failedThreshold: source / location confidence
currentMethod: assertion_mapping
proposedMethod: site_observation_review
expectedGain: avoid turning weak visual interpretation into formal chantier point
evidenceDelta: weakens_claim
scopeDelta: none
gateRequired: true before CR transmission
status: proposed
```

### Executable Hermes Handoff

```text
Task Contract:
Review the disputed chantier observation.

Context Pack:
photo, previous CR point, site notes, lot concerned, date if available.

Method Card:
site_observation_review

Allowed outputs:
observation candidate;
uncertainty;
required missing source;
wording candidate with reserve.

Forbidden outputs:
final technical diagnosis;
formal enterprise instruction;
reserve issuance;
external email.
```

### Returned candidate

```text
Result Candidate:
The photo may concern the stair landing, but location is not confirmed.

Evidence Pack Candidate:
photo reference;
previous CR reference if any;
uncertainty: location not confirmed.

Next action:
ask for another angle or mark the observation as uncertain.
```

### Cockpit display

Default visible layer:

```text
Draft CR candidate.
Main gate: external transmission.
Critical gap: photo not localized.
Method chip: site_observation_review.
Next action: ask source / correct / block send.
```

Method sub-card if unresolved:

```text
Method:
site_observation_review

Proposed by:
ARGOS

Reason:
visual evidence insufficient for CR assertion

Allowed:
observation candidate with reserve

Forbidden:
enterprise instruction / reserve / send
```

Gate card:

```text
Gate:
external transmission

Decision:
send / correct / ask for source / keep draft

Reason:
CR may create professional record and external effect.
```

### Bad path

```text
Photo interpreted as confirmed defect.
Draft CR sent.
Observation becomes formal record.
```

Why it fails:

```text
source weak;
location not confirmed;
external effect;
possible enterprise implication.
```

Corrected path:

```text
site_observation_review;
uncertainty marked;
source request opened;
send gate blocked.
```

### Pantheon succeeded if

```text
no weak visual source became proof;
the uncertainty is visible;
the CR remains draft until gate;
the user has one clear next decision.
```

### Pantheon failed if

```text
the observation is stated as fact;
the send action is available without gate;
the method appears as decoration but does not change the output;
the user sees too many cards and misses the gate.
```

## Test Case B — Devis complementaire

### Run Test Contract

```text
Use case:
Devis complementaire

User intent:
Analyser le devis et preparer une reponse au maitre d'ouvrage.

Professional risk:
A draft answer becomes implicit validation, payment advice or enterprise instruction.

Expected candidate:
Candidate opinion + draft MOA email.

Forbidden final effects:
approve quote;
recommend payment as final;
send email;
instruct enterprise;
create amendment as validated.

Main gates:
client transmission;
financial advice;
mission boundary;
external commitment.

Success condition:
The user can decide: send / correct / ask decomposition / ask client / block.
```

### User request

```text
Analyse ce devis complementaire et prepare une reponse au maitre d'ouvrage.
```

### Initial task chain

| Step | Task | Responsible role | Method | Competence | Runtime | Visibility |
|---:|---|---|---|---|---|---|
| 1 | Qualify quote | ARGOS | source_admission | quote intake | Hermes | chip |
| 2 | Check contract corpus | ARGOS | authority_qualification | document review | Hermes | sub-card if conflict |
| 3 | Analyze contractual scope | THEMIS | contractual_decomposition | CCTP / CCAP review | Hermes | field |
| 4 | Check technical cause | ATHENA | diagnostic_cause_analysis | technical coherence | Hermes | field |
| 5 | Check amount | ATHENA | quote_variation_review | price review | Hermes | sub-card if amount risk |
| 6 | Review proof | ARGOS | probative_review | evidence packaging | Hermes | chip / sub-card |
| 7 | Check mission wording | THEMIS | mission_scope_guard | responsibility boundary | Hermes | sub-card if risky |
| 8 | Draft MOA email | ATHENA / MAITRE | constrained_generation | professional drafting | Hermes | field |
| 9 | Decide transmission | ZEUS / human | external_commitment_guard | decision gate | none until approved | gate |

### Thresholds

```text
quote identified;
date and issuer known;
contract corpus available or gap opened;
claim mapped to CCTP / CCAP / amendment;
technical cause separated from contractual entitlement;
financial implication isolated;
wording does not imply validation;
client transmission gated.
```

### Failure signal A — source contradiction

```text
The quote amount differs from a payment situation or prior signed amendment.
```

### Method Proposal Candidate A

```yaml
proposingRole: ARGOS
detectedProblem: quote amount conflicts with payment situation or amendment
failedThreshold: source precedence
currentMethod: contractual_decomposition
proposedMethod: authority_qualification
expectedGain: identify which source may be used as candidate priority
evidenceDelta: resolves_conflict
scopeDelta: clarifies_scope
gateRequired: false internally, true before recommendation
status: proposed
```

### Executable Hermes Handoff A

```text
Task Contract:
Compare conflicting financial sources.

Context Pack:
quote, situation, amendment, relevant emails.

Method Card:
authority_qualification

Allowed outputs:
conflict table;
candidate source priority;
remaining uncertainty;
question if arbitration required.

Forbidden outputs:
payment approval;
quote validation;
client recommendation;
enterprise instruction.
```

### Returned candidate A

```text
Result Candidate:
The quote and situation conflict. The signed amendment has higher candidate authority, but the object does not fully match.

Evidence Pack Candidate:
quote reference;
situation reference;
amendment reference;
conflict summary.

Next action:
ask enterprise for decomposition or submit to human arbitration.
```

### Failure signal B — risky wording

Draft says:

```text
Nous validons ce devis complementaire.
```

### Method Proposal Candidate B

```yaml
proposingRole: THEMIS
detectedProblem: wording may imply agency approval
failedThreshold: mission scope / external commitment
currentMethod: constrained_generation
proposedMethod: mission_scope_guard
expectedGain: produce safer wording candidate
evidenceDelta: weakens_claim
scopeDelta: requires_mission_gate
externalActionDelta: opens_gate
gateRequired: true before send
status: needs_human_gate
```

### Executable Hermes Handoff B

```text
Task Contract:
Rewrite the response without implying validation, instruction or approval.

Method Card:
mission_scope_guard

Allowed outputs:
safer wording candidate;
risky terms removed;
remaining approval gap.

Forbidden outputs:
final approval;
client decision;
enterprise instruction;
email sending.
```

### Returned candidate B

```text
Result Candidate:
A ce stade, ce devis appelle une verification complementaire au regard des pieces du marche et des elements transmis. Sous reserve de decision de la maitrise d'ouvrage, les points suivants restent a confirmer...

Evidence Pack Candidate:
quote reference;
contract references;
missing decomposition if required;
prior client decision if any.

Gate:
human approval before sending.
```

### Cockpit display

Default visible layer:

```text
Candidate opinion.
Amount / scope conflict.
Mission-scope warning.
MOA transmission gate.
Next action: ask decomposition / correct wording / send after gate / block.
```

Method sub-card:

```text
Method:
mission_scope_guard

Proposed by:
THEMIS

Reason:
wording may imply agency approval

Allowed:
safer wording candidate

Forbidden:
send / approve / instruct
```

Gate card:

```text
Gate:
MOA transmission

Decision:
send / correct / ask for evidence / block

Reason:
external effect and possible professional commitment.
```

### Bad path

```text
Hermes writes `devis valide`.
Draft email sent.
Client and enterprise may treat it as approval.
```

Why it fails:

```text
implicit approval;
possible financial commitment;
mission-scope risk;
external effect not gated.
```

Corrected path:

```text
mission_scope_guard;
safer wording candidate;
external_commitment_guard;
human gate.
```

### Pantheon succeeded if

```text
the quote remains candidate until decision;
the source conflict is visible;
the risky wording is removed;
the user has a clear decision surface;
the send action is blocked until gate.
```

### Pantheon failed if

```text
the draft uses approval language;
Hermes recommends payment as final;
the evidence gap is hidden;
the gate is buried in details.
```

## Test Case C — CERFA / depot administratif

### Run Test Contract

```text
Use case:
CERFA / administrative filing

User intent:
Preparer le CERFA pour depot DP/PC.

Professional risk:
A weak field value becomes a signed administrative claim.

Expected candidate:
Completed form candidate + uncertain fields list.

Forbidden final effects:
file application;
mark signature-ready;
mutate canonical project data;
claim administrative certainty without source.

Main gates:
filing;
client signature;
professional claim;
phase transition.

Success condition:
The user can decide: file / correct / request missing value / block.
```

### User request

```text
Prepare le CERFA pour le depot de DP/PC.
```

### Initial task chain

| Step | Task | Responsible role | Method | Competence | Runtime | Visibility |
|---:|---|---|---|---|---|---|
| 1 | Identify form version | ARGOS | source_admission | form intake | Hermes | chip |
| 2 | Extract project data | ARGOS | assertion_mapping | project data extraction | Hermes | field |
| 3 | Fill sensitive fields | ATHENA | cerfa_field_claim_review | form drafting | Hermes | field / sub-card |
| 4 | Check surfaces | ARGOS | probative_review | surface verification | Hermes | sub-card if weak |
| 5 | Check filing boundary | THEMIS | external_commitment_guard | filing boundary | Hermes | gate |
| 6 | Decide filing | ZEUS / human | phase_gate_review | filing gate | none until approved | gate |

### Thresholds

```text
correct form version;
project identity source known;
parcel and address sourced;
surface value supported by calculation or marked uncertain;
regulatory checkboxes sourced;
uncertain fields listed;
filing blocked until gate.
```

### Failure signal

```text
A surface field is filled from a plan label, but the calculation source is missing.
```

### Method Proposal Candidate

```yaml
proposingRole: ARGOS
detectedProblem: administrative field is insufficiently supported
failedThreshold: field-as-claim proof
currentMethod: cerfa_field_claim_review
proposedMethod: probative_review
expectedGain: distinguish candidate value from filing-ready value
evidenceDelta: raises_question
scopeDelta: none
externalActionDelta: opens_gate before filing
gateRequired: true before filing
status: needs_human_gate
```

### Executable Hermes Handoff

```text
Task Contract:
Review sensitive CERFA fields as claims.

Method Card:
cerfa_field_claim_review

Allowed outputs:
field value candidate;
source reference;
confidence;
contradiction;
missing information;
review requirement.

Forbidden outputs:
filing;
signature-ready claim;
canonical project data mutation.
```

### Returned candidate

```text
Result Candidate:
Surface field remains candidate. Source is plan label only. Calculation confirmation missing.

Evidence Pack Candidate:
plan reference;
extracted label;
missing calculation;
uncertainty level.

Gate:
required before filing.
```

### Cockpit display

Default visible layer:

```text
CERFA candidate.
Surface field uncertainty.
Filing gate.
Next action: confirm calculation / correct / block filing.
```

Visible method sub-card:

```text
Method:
cerfa_field_claim_review

Proposed by:
ARGOS

Reason:
administrative field is a professional claim

Allowed:
candidate field value with uncertainty

Forbidden:
filing / signature-ready output
```

Gate card:

```text
Gate:
administrative filing

Decision:
file / correct / request missing value / block

Reason:
external administrative effect.
```

### Bad path

```text
Surface copied from plan label.
Form marked ready.
Filing prepared as final.
```

Why it fails:

```text
field-as-claim unsupported;
administrative effect;
possible professional responsibility;
gate missing.
```

Corrected path:

```text
cerfa_field_claim_review;
probative_review;
uncertainty marked;
filing gate blocked.
```

### Pantheon succeeded if

```text
uncertain fields are visible;
candidate values are not treated as filing-ready;
filing is blocked until human gate;
the user has a clear list of missing confirmations.
```

### Pantheon failed if

```text
field values look final without source;
Hermes silently fills missing data;
the filing button is available without gate;
uncertainty appears only in trace.
```

## Raw reasoning modes appendix

Raw modes stay behind professional Method Cards unless they change the task trajectory.

| Use case | Raw mode | Professional wrapper | Purpose |
|---|---|---|---|
| Devis complementaire | Hitchens | probative_review | burden of proof for enterprise claim |
| Devis complementaire | Occam / Chatton | diagnostic_cause_analysis | simplest sufficient cause without deleting necessary hypothesis |
| Devis complementaire | Sagan | quote_variation_review | stronger proof for high financial impact |
| CR chantier | abduction | site_observation_review | infer possible explanation without claiming certainty |
| CR chantier | premortem | reception_risk_review | avoid closing a point too early |
| CERFA | assertion mapping | cerfa_field_claim_review | treat every sensitive field as claim |
| Design / ambiguous request | Deleuze / false problem | problem_repositioning | detect wrong framing |
| Drafting / client explanation | via negativa | constrained_generation | remove unsafe wording before adding prose |

Visibility rule:

```text
raw mode invisible by default;
chip if useful to explain the method;
sub-card only if it changes the conclusion, gate, scope or proof path.
```

## Minimal future data shape

This is not a schema.

It is a future test shape.

```yaml
run_test:
  id:
  use_case:
  user_request:
  professional_risk:
  expected_candidate:
  forbidden_effects:
  thresholds:
  initial_task_chain:
    - task:
      responsible_role:
      method:
      competence:
      runtime:
      visibility:
  failure_signals:
    - signal:
      failed_threshold:
      detecting_role:
      proposed_method:
      evidence_delta:
      scope_delta:
      gate_required:
  handoff_candidate:
    reason:
    expected_gain:
    expected_cost:
    forbidden_effects:
  executable_handoff:
    task_contract:
    context_pack:
    method_card:
    allowed_outputs:
    forbidden_outputs:
    stop_condition:
  returned_candidate:
    result_candidate:
    evidence_pack_candidate:
    next_action:
  cockpit_display:
    default_visible:
    method_subcard:
    gate_card:
  success_conditions:
  failure_conditions:
```

## Cross-test success criteria

Pantheon succeeds if:

```text
the user sees one clear decision surface;
weak sources do not become proof;
drafts do not become external actions;
methods do not become validation;
Hermes never acts outside the handoff;
gates are visible before consequential effects;
the trace explains why the task was rerun.
```

## Cross-test failure criteria

Pantheon fails if:

```text
too many cards hide the gate;
Hermes reruns without bounded contract;
the method is visible but useless;
raw reasoning modes dominate the UX;
a draft implies approval;
a source conflict is hidden;
an external action is available before gate;
candidate memory is promoted without evidence.
```

## Final invariant

```text
A run test exists to prove that Pantheon reduces professional confusion.

It does not prove that the runtime works.
It does not validate the UI.
It does not authorize execution.
It does not create doctrine by itself.
```

The validated remains.
