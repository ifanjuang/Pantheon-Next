# Work Issue and Delegated Merge Model

Status: candidate support doctrine — documented non-implemented / to verify.

Date: 2026-07-18

This document defines a minimal governed work model for notes, Work Issues, Hermes execution returns, card changes and delegated merge.

It does not implement a PostgreSQL schema, API, issue tracker, queue, scheduler, Hermes Skill, OpenWebUI Function, worker, merge adapter, GitHub integration, test or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human defines consequential authority.
```

## Purpose

Pantheon needs to distinguish knowledge from work without forcing the user to operate the Card Stack.

```text
Case / Affaire = professional scope
card = projection of current governed knowledge
note = information without expected treatment
Work Issue = bounded work to treat
issue comment = discussion about that work
Hermes run = external execution
Change Proposal = proposed versioned change
review = governed control
merge = application of an authorized proposal
```

Cards remain optional. Work Issues and governed execution must remain usable when no card is displayed.

## Core flow

```text
user request or discovered follow-up
-> Work Issue when durable follow-up is useful
-> bounded Task Contract + targeted Context Pack
-> Hermes execution
-> structured return
-> answer, card candidate, Change Proposal or linked Work Issue
-> policy check or human review
-> authorized merge
-> new governed version
```

## Notes, comments and Work Issues

A card note is an annotation. It does not imply assignment, execution, completion or approval.

An issue comment belongs to a Work Issue discussion. A comment may clarify scope, provide a source, record a question or explain a decision. It does not change issue status by itself.

A Work Issue is an independently addressable work object. It has an owner, scope, effect class, lifecycle and event history.

A note or comment may be explicitly promoted to a Work Issue Candidate. Pantheon and Hermes must not infer that promotion merely because the text sounds actionable.

```text
note != Work Issue
comment != status change
request != authorization
issue resolved != proposal merged
```

## When a Work Issue should exist

Create a Work Issue when the work deserves at least one of these:

- durable follow-up;
- assignment;
- separate discussion;
- later resumption;
- independent review;
- a consequential effect;
- a visible dependency or blocker.

Do not create a Work Issue for every reasoning step, file read, source lookup, tool call or retry inside one bounded task.

Hermes may create:

| Origin | Default posture | Treatment |
|---|---|---|
| explicit user request | `open` or `in_progress` | within the stated request |
| necessary child work | `open`, linked to its parent | may proceed when inside the authorized scope and effect ceiling |
| materially new discovered work | `proposed` | requires triage before widening scope |
| contradiction or blocker | `waiting_user` or `blocked` on the active issue; optional linked issue | preserve the reason and evidence gap |

A discovered topic should remain a return note when separate tracking adds no professional value.

## Minimal issue shape

```yaml
work_issue:
  issue_id:
  case_ref:
  title:
  description:
  origin: explicit_user | human_created | hermes_child | hermes_discovered | system_projection
  parent_issue_ref:
  related_card_refs: []
  issue_type: research | verification | correction | drafting | decision | action
  priority:
  assigned_to:
  requested_effect: read_only | draft | internal_write | external_effect | canonical_effect
  process_status:
  runtime_status:
  review_status:
  resolution:
  task_contract_ref:
  context_pack_ref:
  base_object_versions: {}
  created_by:
  created_at:
  updated_at:
```

## Orthogonal state axes

One overloaded status is insufficient. The model keeps separate axes while the user surface may show a simpler derived label.

### Process status

```text
proposed
open
triaged
in_progress
waiting_user
waiting_source
blocked
resolved
closed
cancelled
```

### Hermes runtime status

```text
not_requested
ready_for_handoff
running
returned
partial
failed
cancelled
unknown
```

### Review status

```text
not_required
pending
changes_requested
accepted
rejected
```

### Resolution

```text
answered
change_merged
duplicate
obsolete
rejected
cannot_resolve
cancelled
```

The compact user vocabulary may project these axes as:

```text
À traiter
En cours
Besoin de vous
À relire
Bloqué
Terminé
```

## Hermes write authority

Hermes may write through a governed Pantheon adapter. It must not connect directly to PostgreSQL.

Within an admitted Task Contract, Hermes may:

- create necessary child Work Issues;
- propose materially new discovered Work Issues;
- set runtime-owned states such as `running`, `returned`, `partial`, `failed` or `unknown`;
- request `waiting_user`, `waiting_source` or `blocked` with a visible reason;
- attach results, source references, Evidence Pack Candidates and trace references;
- create card records with an explicit candidate or review state;
- prepare Change Proposals against exact base versions;
- mark a resolution candidate;
- execute an exact or conditional merge after the required authority is recorded.

Pantheon validates the transition, actor, scope, effect ceiling, base version and idempotency key before persisting it.

Hermes must not:

- self-authorize a consequential merge;
- broaden a user mandate silently;
- treat runtime success as evidence or approval;
- close a sensitive issue merely because a run returned;
- overwrite a newer card version;
- bypass repository or external-system protections;
- use PostgreSQL as its runtime queue.

## Cards created by Hermes

Hermes may create a durable card record, but creation and canonical authority are separate.

| Result class | Initial card posture |
|---|---|
| uncertain or weakly sourced knowledge | `candidate` |
| consequential professional fact or decision | `pending_review` |
| low-risk internal projection covered by an admitted policy | may become `active` after Pantheon applies that policy |
| contradiction | candidate plus visible contradiction status |
| transient answer | remain on the Work Issue; create no card |

Every Hermes-created card records its originating issue, run, sources, creation time, base scope and validation status.

```text
card_created != card_confirmed
runtime_return != governed_truth
automatic_policy_application != Hermes self-approval
```

## Change Proposal and stale-result control

A correction does not overwrite a current card. It creates a Change Proposal containing:

```yaml
change_proposal:
  proposal_id:
  issue_ref:
  target_object_refs: []
  base_versions: {}
  proposed_patch:
  change_summary:
  evidence_candidate_refs: []
  requested_effect:
  review_status:
  merge_authority_ref:
  created_by:
  created_at:
```

If a target changed after the recorded base version, the proposal becomes `stale` or requires rebase and review. Hermes must not silently apply it.

The detailed card revision lifecycle remains in:

```text
docs/assets/pantheon-control/card_revision_proposal_lifecycle.md
```

## Delegated merge

A merge is an execution effect, not a judgment authority. Hermes may perform it when Pantheon can resolve an authorization for the exact target and effect.

Supported modes:

| Mode | Meaning |
|---|---|
| manual | Hermes prepares; the human applies |
| exact delegation | the human authorizes one identified proposal or pull request |
| conditional delegation | the human authorizes merge only if named checks and constraints pass |

A conditional delegation should record:

```yaml
merge_authority:
  authority_id:
  granted_by:
  target_ref:
  allowed_head_ref:
  allowed_base_ref:
  allowed_effect:
  required_checks: []
  conflict_policy: block
  stale_policy: block
  expiry:
  single_use: true
  granted_at:
```

Example:

```text
Verify this proposal and merge it if required checks pass,
the target has not changed and there is no unresolved conflict.
```

If a condition fails, Hermes returns `blocked`, `changes_requested` or `waiting_user`. It does not reinterpret the instruction.

A merge authorization is scoped and non-transitive. Permission to merge one proposal does not authorize future merges, related issues, external transmissions or canonical decisions outside that proposal.

Repository branch protection and external-system permissions still apply.

## PostgreSQL target model

PostgreSQL is the governed record target, not the Hermes execution engine.

Minimal candidate tables:

```text
cases
cards
card_versions
card_notes
work_issues
issue_comments
issue_events
hermes_runs
change_proposals
```

A separate relation table such as `issue_card_links` is justified only when one issue-to-many-card or many-issue-to-one-card relations are required operationally.

`issue_events` is append-only for material transitions:

```text
created
triaged
assigned
status_changed
handoff_sent
runtime_returned
review_requested
authority_granted
merge_applied
resolved
closed
cancelled
```

The current state remains directly queryable on the main object. Pantheon does not need to rebuild every issue from its complete event history for ordinary display.

Browser and Hermes writes go through controlled APIs or adapters. Neither receives unrestricted database credentials.

## Context efficiency

Hermes receives a task-specific Context Pack rather than an entire Case database or document corpus.

The pack should contain only:

- the resolved Case scope when required;
- the active Work Issue and relevant comments;
- pertinent cards and their versions;
- current decisions and contradictions;
- required source references;
- requested effect and approval ceiling;
- expected output and stop conditions.

This minimizes latency, token use, cross-Case contamination and stale-context risk.

## Card Stack projection

The Card Stack exposes work without becoming the work database.

A card face may show only compact indicators such as:

```text
3 issues open
1 Hermes run in progress
1 proposal to review
```

The issue thread, comments, evidence and event history belong in a detail surface. Card navigation must not trigger hidden execution.

## Optimization rules

1. Cards remain optional.
2. Create Work Issues only for independently useful follow-up.
3. Create cards only for durable structured knowledge.
4. Keep internal state precise and user-facing state compact.
5. Send targeted Context Packs, not whole Cases.
6. Store current state directly and material history append-only.
7. Allow reversible low-risk writes under admitted policy.
8. Require exact authority for consequential or external effects.
9. Block stale proposals instead of overwriting newer versions.
10. Keep queues, workers, retries and scheduling in Hermes.

## Non-equivalence rules

```text
card != underlying object schema
note != Work Issue
comment != status change
Hermes returned != issue resolved
issue resolved != issue closed
issue closed != proposal merged
card created != card confirmed
merge executed != merge self-authorized
authorization granted != conditions satisfied
PostgreSQL record != Hermes queue
documented contract != implemented feature
```

## Implementation order

Recommended first operational slice:

1. Work Issue, comment and append-only material event storage;
2. controlled Pantheon API with transition validation and optimistic version checks;
3. targeted Context Pack and Hermes handoff record;
4. normalized Hermes return and runtime-owned issue states;
5. card candidate creation and Change Proposal;
6. exact and conditional delegated merge;
7. compact Card Stack projections.

Any schema, test, runtime, protected-path or external integration change requires a separate implementation review.

## Final rule

```text
The card exposes current knowledge.
The Work Issue organizes treatment.
Hermes executes within scope.
Pantheon validates writes and authority.
The human defines consequential permission.
Merge applies only an authorized, current and checked proposal.
```
