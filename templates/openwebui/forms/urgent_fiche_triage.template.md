# Urgent Fiche Triage Template

Status: non-executable OpenWebUI form template candidate.

This template supports `docs/governance/URGENT_REVIEW_TRIAGE.md`.

It is a capture and display shape only.

It does not implement a form, queue, scheduler, notification, priority engine, approval, memory promotion, OpenWebUI Action, Hermes skill or external action.

```text
Template does not mean implementation.
Urgent is a claim until qualified.
```

## Fiche

```text
title:
matter_or_project:
origin:
received_at:
created_by:
```

## Urgency claim

```text
why_marked_urgent:
risk_if_not_handled:
deadline_or_trigger:
blocker_status:
```

## Evidence

```text
evidence_or_source:
source_type:
source_date:
source_version:
missing_evidence:
```

## Decision need

```text
decision_needed:
decision_owner:
approval_level_if_known:
external_effect_possible: yes | no | unknown
```

## Triage classification

```text
urgency_class:
  immediate_blocker | decision_needed_today | evidence_needed | production_needed | awaiting_external_response | unclear_or_duplicate | not_urgent

consequence_level:
  C0_administrative | C1_internal | C2_project_progress | C3_client_commitment | C4_contractual_financial | C5_liability_safety_regulatory

deadline_class:
  today | tomorrow | this_week | before_meeting | before_site_visit | before_submission | before_signature | before_payment | before_work_continues | no_deadline_found

status:
  urgent_claim_unqualified | urgent_blocker | urgent_today | urgent_this_week | evidence_needed | decision_needed | production_needed | awaiting_external_response | deferred | resolved | obsolete | duplicate | not_urgent
```

## Next action

```text
next_action:
assigned_role_or_owner:
not_before:
not_after:
requires_detail_before_yes: yes | no
requires_user_decision_gate: yes | no
```

## Boundary

```text
This fiche does not approve action.
This fiche does not send, file, issue, validate, merge or promote memory.
Any external effect requires its own governed approval path.
```
