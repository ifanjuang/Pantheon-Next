# Dossier Situation Intake

Status: active support doctrine — intake object for ambiguous professional requests — documented non-implemented.
Boundary profile: active_support_doctrine.

This document defines a governed intake function used before a professional Approach or Workflow Candidate is forged, executed or presented as ready.

It does not create a new Pantheon Role.

Runtime/client boundary: see `HERMES_INTEGRATION.md`. This intake produces candidate material only; Registre admission and consequential human decision remain separately governed.

## Terminology note

`Case / Affaire` is the controlled system term for the professional unit.

This document keeps `Dossier Situation Intake` as a legacy/public-facing label because the file and existing references already use it. Inside the doctrine, `dossier` must not be read as a file folder, Corpus or storage directory.

```text
Case / Affaire = professional unit.
Situation = concrete question or tension.
Corpus = document set.
Folder / dossier fichier = storage directory only.
```

## Why this exists

Professional requests often arrive as incomplete language:

```text
What are the impacts?
Can you answer the client?
Prepare the notice.
Check this new document.
```

The danger is that the system may answer the sentence instead of the professional situation.

A governed intake step prevents that collapse.

It builds a short `Dossier Situation Brief` before an Approach or Workflow Candidate is proposed.

## Canonical rule

```text
Clarify the situation before forging the workflow.
```

The intake function does not decide.

It prepares the minimum shared understanding needed for Athena to structure the work, Hephaistos to forge an artifact candidate and Zeus to arbitrate the procedure.

## Role placement

`Dossier Situation Intake` is a function, not a role.

It is produced through role viewpoints:

| Viewpoint | Contribution |
|---|---|
| IRIS | clarifies the user's wording and reformulates the real request in plain professional language |
| ATHENA | structures the request into a treatable problem and identifies the likely Approach or Workflow Candidate family |
| ARGOS | lists required sources, versions, provenance, geography and evidence gaps |
| THEMIS | identifies risk, tension, approval boundary, liability or external-effect risk |
| APOLLO | checks completeness, usability and delivery readiness of the brief |
| ZEUS | arbitrates the status and next procedure when ambiguity, conflict or tension remains |
| HEPHAISTOS | may later forge the workflow or artifact candidate; it does not define the intake authority |

IRIS clarifies.

ATHENA structures.

ARGOS situates the proof.

THEMIS qualifies tension.

ZEUS arbitrates status.

HEPHAISTOS builds only after the situation is sufficiently bounded.

## Dossier Situation Brief

Minimum shape:

```text
dossier_situation_brief:
  request:
    raw_user_request:
    clarified_request:
    requested_output:
    requested_effect:
  project_identity:
    official_name:
    aliases:
    address:
    commune:
    parcel_refs:
    project_type:
  phase:
    user_says:
    contract_phase:
    operational_phase:
    contradiction:
  geography_and_rules:
    jurisdiction:
    PLU_zone:
    ABF_or_heritage:
    ERP_context:
    known_constraints:
  sources:
    received_now:
    required:
    available:
    missing:
    superseded_or_uncertain:
  versions:
    latest_plan_known:
    latest_notice_known:
    incoming_document_index:
    version_conflicts:
  contract_scope:
    mission_reference:
    in_scope:
    out_of_scope:
    unclear:
  relation_context:
    client_tension:
    mairie_tension:
    ABF_or_authority_tension:
    contractor_tension:
    insurer_or_claim_context:
  risk_triggers:
    safety:
    cost:
    schedule:
    external_commitment:
    professional_liability:
  memory_and_register:
    runtime_memory_relevant:
    registre_entries_required:
    contradictions:
  blocking_questions:
  non_blocking_questions:
  recommended_next_status:
```

The shape above is documentary.

It is not an executable schema.

Any schema addition under `schemas/` requires a dedicated protected-path review.

The identifier `dossier_situation_brief` is retained as a compatibility name. New explanatory text should read it as a Case/Situation brief.

## Status vocabulary

The brief may recommend a next status:

| Status | Meaning |
|---|---|
| `ready_for_workflow_candidate` | enough information exists to forge a Workflow Candidate |
| `pending_clarification` | user wording or project target is ambiguous |
| `pending_source` | a required source, version or proof element is missing |
| `pending_contract_scope` | the mission boundary is unclear |
| `risk_review_required` | risk or tension requires Themis review before work continues |
| `zeus_arbitration_required` | conflicting candidate paths or statuses require arbitration |
| `blocked` | continuing would produce a false truth, external effect, wrong memory or unauthorized action |

## Example — unclear architecture request

User request:

```text
The client sent a new structural note with changed effectif. What are the impacts?
```

IRIS clarification:

```text
The user wants an internal impact review from a client email and attached document.
The likely topic is ERP / fire-safety coordination, not only structure.
```

Athena structure:

```text
Approach family: incoming document impact review.
Likely Workflow Candidate: assisted impact review with draft-only outputs.
Likely outputs: impact matrix, annotated PDF, questions, draft-only reply.
```

Argos evidence needs:

```text
email source
attachment index
latest plans
previous notice
contract / mission reference
Registre Probatoire entries for effectif and last approved assumptions
```

Themis risk flags:

```text
changed effectif
possible fire-safety consequence
stair / circulation consequence
contract scope unclear
client-facing answer could become external commitment
```

Zeus procedure:

```text
status: ready_for_workflow_candidate
mode: assisted
external_action: blocked
registre_mutation: blocked
user_decision_gate: required before transmission
```

## Boundary

The intake function may create a brief candidate.

It must not:

- answer the substantive question as final;
- send, publish or transmit;
- validate an ERP, fire-safety, legal, contractual or insurance position;
- mutate the Registre Probatoire;
- promote runtime memory;
- hide missing sources;
- forge a durable workflow without validation.

The output remains candidate material until the required governance path is complete.