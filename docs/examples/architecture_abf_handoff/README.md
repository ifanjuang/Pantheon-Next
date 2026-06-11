# Example — Architecture / Urbanisme — Governed Handoff for ABF / mairie reply

Status: fictional professional example — educational support only.

This example shows how Pantheon frames a sensitive architecture / urbanisme task before an execution runtime prepares a draft.

It is not legal advice, planning advice, administrative advice or architectural validation. It does not replace the architect's judgment, site knowledge, client instruction, planning authority position, ABF consultation or professional liability review.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Scenario

A mairie sends a request for complementary material on a facade change in a protected or heritage-sensitive context.

The practitioner asks:

```text
Prepare a reply to the mairie and ABF about the requested facade documents.
```

A raw assistant may produce a fluent answer that sounds ready to send. That is unsafe because the task may touch:

- regulatory interpretation;
- scope of the submitted works;
- completeness of administrative exhibits;
- ABF-facing wording;
- client and project responsibility;
- external transmission.

Pantheon must separate drafting from sending, evidence from proof and runtime success from governance approval.

## Intake classification

```text
request_type: professional external communication preparation
professional_domain: architecture_urbanisme
consequence: high
external_effect_possible: yes
status: Task Contract required
```

The task is not a simple writing request. It is a candidate external communication under professional responsibility.

## Task Contract excerpt

```yaml
task_contract:
  id: TC-ARCH-ABF-REPLY-001
  intent: "Prepare a draft reply to the mairie / ABF request for complementary facade material."
  scope:
    included:
      - fictional project facade change
      - received mairie request
      - supplied project notice
      - supplied facade photographs
      - supplied planning extracts
    excluded:
      - other client dossiers
      - legal opinion on appeal strategy
      - unsupported conclusion that ABF approval is acquired
      - direct filing or sending
  allowed_outputs:
    - internal issue note
    - draft email candidate
    - evidence pack candidate
    - unresolved questions list
  forbidden_outputs:
    - sent email
    - administrative filing
    - final regulatory conclusion without source
    - Registre Probatoire entry
  approval:
    required_before_external_effect: true
    minimum_gate: User Decision Gate
  register_rules:
    default: no Register Candidate unless a scoped, sourced and approved project fact is extracted
```

## Context Pack excerpt

```yaml
context_pack:
  id: CP-ARCH-ABF-REPLY-001
  purpose: "Give the execution runtime only the material needed to prepare a draft reply."
  scope:
    type: dossier
    label: "Fictional facade change dossier"
  included_sources:
    - mairie_request_2026-06-11.pdf
    - notice_architecturale_candidate.md
    - facade_photos_contact_sheet.pdf
    - planning_extract_candidate.pdf
  excluded_sources:
    - unrelated client emails
    - prior project notes not cited in the mairie request
  assumptions:
    - "The protected-context status is treated as user-provided until verified in a source."
    - "The exact ABF position is not assumed unless present in the request."
  open_questions:
    - "Which exhibits are actually missing?"
    - "Is the recipient service confirmed?"
    - "Should the reply be only a draft or also a filing instruction?"
  evidence_expectations:
    - cite every regulatory or procedural claim
    - list missing exhibits instead of pretending completeness
    - keep ABF position distinct from mairie instruction
```

## Decision Gate

```yaml
decision_gate:
  id: DG-ARCH-ABF-REPLY-001
  conflict: "The user wants a reply, but sending or filing would create an external administrative effect."
  options:
    - prepare_draft_only
    - prepare_internal_issue_note_only
    - ask_for_missing_sources
    - send_directly
  selected_option: prepare_draft_only
  rejected_options:
    send_directly: "External effect requires explicit professional approval."
  status: approved_for_draft_only
```

## Governed execution handoff

This is the bounded object passed to the execution runtime. It is not an execution graph and does not make Pantheon run the work.

```yaml
governed_execution_handoff:
  handoff_id: EH-ARCH-ABF-REPLY-001
  linked_task_contract: TC-ARCH-ABF-REPLY-001
  linked_context_pack: CP-ARCH-ABF-REPLY-001
  decision_gate: DG-ARCH-ABF-REPLY-001
  approval_ref: null
  scope:
    type: dossier
    label: "Fictional facade change dossier"
  target_runtime: execution_runtime
  requested_effect: internal_state_change
  action_family: draft_external_reply_candidate
  target:
    kind: draft_email_candidate
    ref: mairie_abf_reply_draft
  allowed_inputs:
    - linked_context_pack
    - linked_task_contract
  forbidden_effects:
    - send_email
    - file_administrative_document
    - update_Registre_Probatoire_entry
    - state_that_ABF_approval_is_acquired_without_source
  expected_result_candidate:
    - internal_issue_note
    - draft_email_candidate
    - unresolved_questions
  expected_evidence_pack_candidate:
    - sources_used
    - assumptions
    - unsupported_claims
    - contradictions_or_gaps
    - approval_needed_before_send
  outcome_observation_expected: true
  idempotency_key: TC-ARCH-ABF-REPLY-001::draft_only::v1
  trace_refs:
    - TC-ARCH-ABF-REPLY-001
    - CP-ARCH-ABF-REPLY-001
    - DG-ARCH-ABF-REPLY-001
```

## Expected runtime return

```yaml
runtime_return:
  handoff_delivery_status: sent
  runtime_task_status: success
  governance_result_status: candidate
  result_candidate:
    type: draft_email_candidate
    status: candidate_to_review
    external_effect: false
  evidence_pack_candidate:
    sources_used:
      - mairie_request_2026-06-11.pdf
      - notice_architecturale_candidate.md
    assumptions:
      - "ABF-facing context requires source confirmation."
    gaps:
      - "Exact list of missing exhibits must be checked against the mairie request."
      - "Recipient and filing channel are not confirmed."
    approval_needed_before_send: true
  outcome_observation_candidate:
    draft_created: true
    email_sent: false
    filing_done: false
    register_changed: false
```

## Candidate internal issue note

```text
The reply may be prepared as a draft only.

The dossier should not state that the facade proposal is accepted or that ABF agreement is acquired unless a dated source says so. The draft should identify the requested exhibits, distinguish already supplied material from missing material and preserve any uncertainty around the protected-context status.

Before sending, the architect must verify the recipient, the exhibit list, the current planning source and the exact administrative effect of the reply.
```

## Candidate draft email

```text
Subject: Complementary material — facade change dossier [PROJECT REF]

Bonjour,

Nous faisons suite à votre demande de pièces complémentaires relative au dossier de modification de façade.

À ce stade, nous préparons les éléments suivants pour répondre à votre demande :

1. les vues de façade mises à jour ;
2. les photographies de l'existant ;
3. la notice précisant les matériaux et teintes envisagés ;
4. les éléments nécessaires à la bonne lecture du projet dans son contexte.

Avant transmission définitive, nous vérifions la concordance entre la liste des pièces demandées et les documents déjà produits afin d'éviter tout écart de périmètre.

Cette réponse ne préjuge pas de l'instruction du dossier ni de la position finale des services consultés.

Cordialement,
[ARCHITECT]
```

## What Pantheon prevents

This example matters because the dangerous failure is not only hallucination. The dangerous failure is a clean professional message treated as safe to transmit when its sources, scope and approval are still incomplete.

Pantheon prevents:

- draft treated as sent;
- runtime success treated as professional validation;
- source gap hidden by fluent wording;
- ABF / mairie position inferred without source;
- administrative filing without explicit approval;
- project fact promoted into the Registre Probatoire without review.

## Final reading

```text
The execution runtime may draft the reply.
Pantheon governs whether the reply is bounded, sourced, reviewable and blocked before external effect.
The professional decides whether anything leaves the office.
```
