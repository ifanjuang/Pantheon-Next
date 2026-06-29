# Architecture Method Deck

Status: candidate support doctrine — architecture-domain Method Cards for governed AI use in agency workflows.

Runtime status: non-executable.

This document specializes `METHOD_CARD_MODEL.md` for architecture practice.

It does not implement a UI, renderer, workflow engine, method selector, source validator, RAG system, OCR pipeline, PDF tool, email sender, approval engine, memory engine, Hermes skill, connector, schema, test or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Architecture work is consequential because an AI error can become a wrong source, an implicit validation, a mission-scope expansion, a false proof, an unauthorized transmission or a professional commitment.

This deck turns generic Method Cards into professional cards that can be proposed by Roles during Runs.

```text
A method appears because a Role detects a tension.
It does not appear because it is intellectually interesting.
```

## Cockpit budget

A task should normally expose at most:

```text
1 primary method;
1 guardrail method;
1 verification method;
other methods stay in the trace unless they change proof, scope, cost, status, memory or action.
```

## Common fields

Each professional card should define:

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

## Core professional method cards

### source_admission

Purpose: prevent a received source from becoming trusted by default.

Likely roles: ARGOS, MAITRE, ATHENA.

Trigger: a document, mail, quote, plan, photo, CR, PLU extract, CERFA, report or notice enters the task.

Minimum output: source type, issuer, date, version, project scope, authority class, applicability, risk and recommended next step.

Evidence delta: qualifies_source, raises_question.

Scope delta: clarifies_scope.

Gate triggers: source supports a consequential claim, or source is outdated, partial, derived or contradicted.

Hermes profile hint: doc-intake, evidence-review.

Forbidden outputs: source validation, professional conclusion, external transmission, canonical memory.

### authority_qualification

Purpose: decide which source has candidate priority when sources conflict.

Likely roles: ARGOS, THEMIS, ZEUS.

Trigger: sources give different values, clauses, dates, amounts, statuses or decisions.

Minimum output: conflicting sources, conflicting values, relative authority, source retained as candidate, source downgraded, uncertainty, question if arbitration is required.

Evidence delta: resolves_conflict, changes_confidence, raises_question.

Scope delta: clarifies_scope.

Gate triggers: retained source affects payment, visa, reception, filing, client decision, enterprise instruction or memory promotion.

Hermes profile hint: evidence-review.

Forbidden outputs: final contractual interpretation, payment approval, source canonization, external instruction.

### assertion_mapping

Purpose: turn a candidate output into reviewable assertions.

Likely roles: ARGOS, ATHENA, MAITRE.

Trigger: a report, email, note, visa, form, analysis, CR entry or synthesis contains factual or professional claims.

Minimum output: assertion, source reference, source status, confidence, contradictions, risk if false, allowed reuse scope.

Evidence delta: adds_source, weakens_claim, changes_confidence.

Scope delta: clarifies_scope if assertions imply mission posture.

Gate triggers: unsourced assertion supports consequential output.

Hermes profile hint: evidence-review, governance-review.

Forbidden outputs: validated truth, final proof, external transmission.

### contractual_decomposition

Purpose: decompose a contractual issue into clauses, lots, amounts, inclusions, exclusions and required decisions.

Likely roles: THEMIS, MAITRE, ARGOS.

Trigger: quote, amendment, CCTP / CCAP clause, situation, invoice, claim, delay or scope dispute.

Minimum output: contract corpus, lot, clause reference, expected prestation, claimed prestation, included/excluded/changed/unclear status, financial implication, question or gate.

Evidence delta: adds_source, resolves_conflict, raises_question.

Scope delta: clarifies_scope, detects_out_of_scope, requires_mission_gate.

Gate triggers: avenant, client decision, enterprise instruction, payment validation, claim rejection, mission extension.

Hermes profile hint: architecture-domain, evidence-review, governance-review.

Forbidden outputs: final contractual decision, order to enterprise, financial approval.

### mission_scope_guard

Purpose: detect wording or action that may exceed mission scope or imply responsibility.

Likely roles: THEMIS, MAITRE, ZEUS.

Trigger: validate, approve, order, confirm, accept, guarantee, certify, fault, responsibility, payment, conformity, visa, OPC or insurance implication.

Minimum output: engaging wording or action, possible commitment, mission boundary, risk, safer formulation candidate, gate required or not.

Evidence delta: weakens_claim, opens_gate.

Scope delta: detects_out_of_scope, requires_mission_gate.

Gate triggers: external transmission, visa, client validation, enterprise instruction, fault recognition, mission extension, insurance-related statement.

Hermes profile hint: governance-review.

Forbidden outputs: responsibility decision, external send, canonical memory.

### external_commitment_guard

Purpose: separate a prepared candidate from an action that affects outside parties.

Likely roles: ZEUS, THEMIS, MAITRE.

Trigger: send email, file dossier, deposit form, publish CR, issue visa, notify enterprise, update external tracker or request payment.

Minimum output: action candidate, recipient, object of transmission, approval required, evidence required, duplicate risk, action state.

Evidence delta: opens_gate.

Scope delta: requires_mission_gate if professional commitment is possible.

Gate triggers: any external effect.

Hermes profile hint: governance-review.

Forbidden outputs: automatic send, automatic filing, automatic merge, automatic memory promotion.

### probative_review

Purpose: check whether an output is sufficiently supported for its intended effect.

Likely roles: ARGOS, ZEUS, MAITRE.

Trigger: output may justify decision, memory, transmission, payment, visa, reception, claim or professional advice.

Minimum output: claims reviewed, sources checked, missing evidence, contradictions, confidence, allowed reuse scope, remaining questions.

Evidence delta: changes_confidence, weakens_claim, opens_gate.

Scope delta: clarifies_scope if use context is limited.

Gate triggers: proof gap affects consequential output.

Hermes profile hint: evidence-review.

Forbidden outputs: proof validation, Registre Probatoire entry, external approval.

### phase_gate_review

Purpose: prevent phase progress from being treated as validated state without evidence and authorized decision.

Likely roles: ZEUS, MAITRE, THEMIS.

Trigger: APS, APD, DP/PC, PRO, DCE, ACT, EXE/VISA, DET, AOR, DOE, GPA or archive state changes.

Minimum output: phase, expected deliverables, available evidence, missing evidence, actor who may validate, status candidate/ready/blocked/validated externally.

Evidence delta: adds_source, changes_confidence, opens_gate.

Scope delta: clarifies_scope.

Gate triggers: phase state changes, filed package, client approval, consultation launch, visa, reception, reserve lifting.

Hermes profile hint: architecture-domain, governance-review.

Forbidden outputs: phase validation, filing, client approval record, canonical memory promotion.

### site_observation_review

Purpose: qualify site observations before they become report points.

Likely roles: ARGOS, ATHENA, MAITRE.

Trigger: photo, site note, oral report, enterprise message or repeated observation may enter a CR or reserve list.

Minimum output: observation, location, date/source, lot, previous CR link, status, severity, recommended wording, question if weak.

Evidence delta: adds_source, weakens_claim, raises_question.

Scope delta: clarifies_scope if observation implies instruction.

Gate triggers: reservation, formal notice, enterprise instruction, responsibility implication.

Hermes profile hint: doc-intake, evidence-review, architecture-domain.

Forbidden outputs: final technical diagnosis, enterprise order, formal reserve issuance without gate.

### quote_variation_review

Purpose: review additional, modified or disputed quotations without silent approval.

Likely roles: THEMIS, ARGOS, MAITRE, ATHENA.

Trigger: complementary quote, variante, moins-value, plus-value, revised estimate or enterprise claim.

Minimum output: quote identity, lot, amount, object, contractual basis, technical basis, financial coherence, missing detail, candidate status.

Evidence delta: adds_source, resolves_conflict, raises_question, changes_confidence.

Scope delta: clarifies_scope, detects_out_of_scope, requires_mission_gate.

Gate triggers: client recommendation, avenant, order, payment, refusal.

Hermes profile hint: architecture-domain, evidence-review, governance-review.

Forbidden outputs: approval, enterprise instruction, client decision, final financial validation.

### visa_commitment_review

Purpose: review EXE / VISA wording and status before it can imply validation beyond the intended posture.

Likely roles: THEMIS, MAITRE, ZEUS.

Trigger: EXE document, technical detail, product sheet, method statement, shop drawing or note is prepared for visa or comment.

Minimum output: document identity, issuer, index, object, review perimeter, comments, reserved points, wording risk, visa status candidate, gate required.

Evidence delta: adds_source, weakens_claim, opens_gate.

Scope delta: clarifies_scope, requires_mission_gate.

Gate triggers: visa issuance, acceptance-like wording, technical conformity statement, responsibility shift.

Hermes profile hint: architecture-domain, governance-review.

Forbidden outputs: final visa, technical guarantee, enterprise instruction, external send.

### reception_risk_review

Purpose: identify evidence, reservations and responsibility posture before reception or reserve lifting.

Likely roles: ZEUS, THEMIS, ARGOS, MAITRE.

Trigger: OPR, reception, reserve list, reserve lifting, GPA issue or handover.

Minimum output: works/lot, observed state, evidence, reserve candidate, severity, responsible party candidate, missing confirmation, implication, gate required.

Evidence delta: adds_source, weakens_claim, opens_gate.

Scope delta: clarifies_scope, requires_mission_gate.

Gate triggers: reception, reserve omitted, reserve lifted, GPA issue closed, formal statement sent.

Hermes profile hint: evidence-review, governance-review, architecture-domain.

Forbidden outputs: pronouncing reception, lifting reserve, recognizing fault, external notification without approval.

### cerfa_field_claim_review

Purpose: treat each sensitive form field as a claim requiring source, confidence and review status.

Likely roles: ARGOS, ATHENA, MAITRE, ZEUS.

Trigger: CERFA, DP/PC field, surface, parcel, address, applicant identity, work description or regulatory checkbox.

Minimum output: field, value candidate, source, confidence, contradiction, comment, missing information, review requirement.

Evidence delta: adds_source, raises_question, changes_confidence, opens_gate.

Scope delta: clarifies_scope.

Gate triggers: administrative filing, client signature, external transmission.

Hermes profile hint: doc-intake, architecture-domain, evidence-review.

Forbidden outputs: filing, signature-ready claim without review, canonical project data mutation.

### constrained_generation

Purpose: generate drafts or creative variants while preserving source, mission, style and forbidden-effect constraints.

Likely roles: ATHENA, METIS, HEPHAISTOS, THEMIS.

Trigger: draft email, notice, CR wording, client explanation, design variants, image prompts, synthesis or presentation text.

Minimum output: constraints used, forbidden elements, source dependence, style/tone, draft candidate, review points, external-action status.

Evidence delta: none by default; raises_question if the draft introduces unsupported claims.

Scope delta: detects_out_of_scope if generation overstates mission or authority.

Gate triggers: external use, professional assertion, change of project position.

Hermes profile hint: architecture-domain, governance-review if external.

Forbidden outputs: external send, final approved wording, unsupported factual assertion, mission expansion.

## Relationship with reasoning modes

Raw reasoning modes remain governed by `REASONING_MODES_LIBRARY.md`.

This deck translates some of them into professional method cards suitable for cockpit visibility.

## Core invariant

```text
Architecture Method Cards guide professional AI work.
They produce candidates, questions and gates.
They do not validate, approve, send, remember or execute.
```

The validated remains.
