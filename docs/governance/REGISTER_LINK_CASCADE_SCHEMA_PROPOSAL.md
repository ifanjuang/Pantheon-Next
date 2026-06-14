# Register Link & Cascade — schema proposal

Status: validation-only proposal — documented non-implemented. Protected-path change: requires explicit approval before any edit under `schemas/` or `tests/`.

This note specifies two candidate schemas that formalize the **dependency, impact and cascade** model already described in prose by [`EVIDENCE_MEMORY_CANONICALIZATION.md`](EVIDENCE_MEMORY_CANONICALIZATION.md) (sections *Dependency model*, *Impact review*, *Conflict model*) and sequenced by [`EVIDENCE_MEMORY_DEV_PLAN.md`](EVIDENCE_MEMORY_DEV_PLAN.md) (Layer 1 `memory_links`, `impact_reviews`). It turns the prose into a machine-checkable contract so that links between Registre Probatoire entries — and the cascade they trigger — can be validated rather than improvised.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Certainty stays on the `E0–E4` axis owned by [`GLOSSARY.md`](GLOSSARY.md); approval stays on `C0–C5` owned by [`APPROVALS.md`](APPROVALS.md). This proposal adds relation and impact metadata around [`register_candidate.schema.yaml`](../../schemas/register_candidate.schema.yaml); it does not change that schema.

## Boundary

This document changes no protected path. It edits no file under `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml`, Docker or `.env`. The schemas below are printed inside a governance note for review; they are not executable schema files.

These schemas are validation contracts only. They do not introduce a runtime, an autonomous loop, a provider router, a scheduler, a message queue, a hidden workflow runtime or automatic memory promotion. They record proposed relations and proposed consequences; they decide nothing and downgrade nothing. No impacted entry changes status without a recorded human decision at the gate. Critical impacts must never be silently downgraded.

## Why

Today a Registre Probatoire entry can only express one relation: `supersedes_candidate_id`. The doctrine, however, requires typed links (`depends_on`, `impacts`, `conflicts_with`…) and a cascade: when a base condition changes, dependent entries must be reviewed, not silently kept or silently dropped.

A concrete case from the architecture domain:

```text
The geotechnical study imposes deep foundations.
→ this validates one entry (foundation type)
→ and must reopen review of the seismic structural assumption,
  the cost estimate and the schedule that depended on it.
```

Without a link schema, that cascade lives only in someone's head (or, today, only as a visual hint in the dashboard mockup). This proposal gives it a contract.

## Object A — Register Link

A typed, directed relation from one register entry/candidate to another.

```yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: Pantheon Next Register Link
description: >-
  Governance schema for a typed, directed relation between two Registre
  Probatoire entries or Register Candidates. Validation metadata only;
  it records a relation, it does not execute or promote anything.
type: object
required:
  - link_id
  - from_id
  - to_id
  - relation
  - created_at
  - created_by
properties:
  link_id: { type: string, pattern: "^[a-z0-9._-]+$" }
  from_id: { type: string, minLength: 1 }   # subject register entry / candidate id
  to_id:   { type: string, minLength: 1 }   # related register entry / candidate id
  relation:
    type: string
    enum:
      - depends_on
      - impacts
      - valid_if
      - invalid_if
      - supersedes
      - superseded_by
      - derived_from
      - conflicts_with
      - supports
      - requires_arbitration
  dependency_type:
    type: string
    description: Optional qualifier for depends_on / impacts relations.
    enum:
      - program_dependency
      - technical_dependency
      - budget_dependency
      - planning_dependency
      - contractual_dependency
      - regulatory_dependency
      - client_preference_dependency
      - assumption_dependency
  impact_level:
    type: string
    enum: [none, low, medium, high, critical]
    default: none
  revalidation_required: { type: boolean, default: false }
  revalidation_reason: { type: [string, "null"] }
  scope:
    type: object
    required: [scope_type, scope_id]
    properties:
      scope_type:
        type: string
        enum: [session, task, dossier, project, domain, user, organization, repository, governance, system]
      scope_id: { type: string, minLength: 1 }
      scope_label: { type: string }
    additionalProperties: false
  created_at: { type: string, format: date-time }
  created_by: { type: string }
  note: { type: [string, "null"] }
  governance_refs:
    type: array
    items: { type: string }
    default:
      - docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md
      - docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md
      - docs/governance/GLOSSARY.md
additionalProperties: false
x-boundary:
  runtime_execution: false
  autonomous_loop: false
  provider_routing: false
  scheduler: false
  queue_system: false
  memory_promotion: false
  automatic_canonization: false
  automatic_cascade_resolution: false
```

## Object B — Impact Review

A cascade record opened when a triggering entry changes. It lists the impacted entries and the **proposed** consequence for each. Resolution is a recorded human decision; the schema records, it does not mutate the targets.

```yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: Pantheon Next Impact Review
description: >-
  Governance schema for a cascade impact review opened when a triggering
  register entry changes. Records proposed consequences and human decisions;
  it promotes, downgrades and archives nothing on its own.
type: object
required:
  - impact_review_id
  - trigger_id
  - trigger_change
  - created_at
  - impacted
  - status
properties:
  impact_review_id: { type: string, pattern: "^[a-z0-9._-]+$" }
  trigger_id: { type: string, minLength: 1 }     # entry whose change opened the review
  trigger_change:
    type: string
    enum: [created, validated, superseded, revoked, archived, updated]
  created_at: { type: string, format: date-time }
  created_by: { type: string }
  required_approval:
    type: string
    enum: [C0, C1, C2, C3, C4, C5]
  impacted:
    type: array
    minItems: 1
    items:
      type: object
      required: [target_id, impact_status]
      properties:
        target_id: { type: string, minLength: 1 }
        relation:
          type: string
          enum: [depends_on, impacts, valid_if, invalid_if, conflicts_with, derived_from]
        impact_status:
          type: string
          enum:
            - unaffected
            - impact_detected
            - obsolete_probable
            - revalidate
            - update_proposed
            - critical_arbitration
            - supersede
            - archive
            - revoke
            - resolved
        severity:
          type: string
          enum: [none, low, medium, high, critical]
          default: none
        recommended_action: { type: [string, "null"] }
        decision:
          type: string
          enum: [pending, accepted, refused, deferred]
          default: pending
        decided_by: { type: [string, "null"] }
        decided_at: { type: [string, "null"], format: date-time }
      additionalProperties: false
  status:
    type: string
    enum: [open, in_review, resolved, deferred]
  governance_refs:
    type: array
    items: { type: string }
    default:
      - docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md
      - docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md
additionalProperties: false
x-boundary:
  runtime_execution: false
  autonomous_loop: false
  provider_routing: false
  scheduler: false
  queue_system: false
  memory_promotion: false
  automatic_canonization: false
  automatic_cascade_resolution: false
```

## Cascade rule (declarative)

The rule is a validation contract, not an engine:

```text
1. When a trigger entry's status changes to validated, superseded, revoked
   or archived, an Impact Review should be opened that lists every entry
   linked by `impacts`, or by the inverse of `depends_on`, plus any
   `conflicts_with` neighbour.
2. Each impacted target receives an impact_status and a severity.
3. A target with severity = critical must take impact_status
   critical_arbitration and route to the governance path. It must never be
   silently downgraded.
4. No target changes its own status until the Impact Review records a human
   decision (accepted / refused / deferred) at the gate.
5. The Impact Review is resolved only when every impacted target has a
   recorded decision.
```

Critical impact areas (from the canonicalization note) include structure, safety, budget, planning / contract, urbanism, insurance, professional liability and agency doctrine.

## Relation to the dashboard mockup

The Pantheon Control mockup already renders this model, with simulated data:

```text
register_link            → the "Conséquences en cascade" zone on a Preuve card
impact_review            → the "À valider" panel + the cascade declassification
trigger_change=validated → validating P-202 reopens P-150 as "À revoir"
impacted[].decision      → the Valider / Refuser buttons in the gate panel
```

The mockup is the read-only surface; this schema is the contract the surface and the validator would share. The mockup decides nothing — the gate does — which matches `decision: pending` until a human resolves it.

## Worked example — client asks to fit out the basement (ERP)

```text
trigger_id:     P-202  (basement fit-out requested)
trigger_change: validated
impacted:
  - target_id: P-150  relation: impacts  impact_status: supersede
    severity: high     recommended_action: "Recompute ERP classification"
    decision: pending
  - target_id: ev.desenfumage  relation: depends_on  impact_status: revalidate
    severity: high     decision: pending
  - target_id: ev.issues       relation: depends_on  impact_status: revalidate
    severity: critical recommended_action: "Route to governance path"
    decision: pending
status: open
```

No status of P-150, `ev.desenfumage` or `ev.issues` changes until each line carries a recorded decision.

## Files affected (apply only after approval)

Paths are written relative to their directory so this proposal does not claim
that the not-yet-created schema files exist.

```text
ADD   register_link.schema.yaml          (under schemas/)
ADD   impact_review.schema.yaml          (under schemas/)
ADD   register_link.example.yaml         (under schemas/examples/)
ADD   impact_review.example.yaml         (under schemas/examples/)
EDIT  README.md                          (under schemas/, the listing)
EDIT  test_schema_examples.py            (under tests/, example/schema pairs)
EDIT  test_governance_schemas.py         (under tests/, schema -> example mapping)
```

## Approval checklist

```text
[ ] confirm the relation vocabulary matches EVIDENCE_MEMORY_CANONICALIZATION.md
[ ] confirm impact_status vocabulary (10 values) is the canonical set, not UI-only
[ ] confirm the cascade rule stays declarative (no engine, no auto-resolution)
[ ] confirm critical impacts can never be silently downgraded
[ ] authorize the protected-path edits under schemas/ and tests/
[ ] after approval: add the two schemas + examples, update README and the two
    tests, run the schema tests, add a CHANGELOG entry and an ai_logs trace
```

## Current repo state

Documented non-implemented. No protected path changed. The schemas are added only after explicit approval of this proposal.
