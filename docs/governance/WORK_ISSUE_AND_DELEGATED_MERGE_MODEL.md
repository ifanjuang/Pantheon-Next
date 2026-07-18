# Work Issue and Delegated Merge Model

Status: candidate support doctrine — documented non-implemented / to verify.

Date: 2026-07-18

This document defines the missing work-object boundary between cards, Hermes execution and governed change. It does not replace Task Contracts, Context Packs, approval doctrine or the existing card revision lifecycle.

It does not implement a PostgreSQL schema, API, issue tracker, queue, scheduler, Hermes Skill, OpenWebUI Function, worker, merge adapter, test or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human defines consequential authority.
```

## Minimal vocabulary

```text
Case / Affaire = professional scope
card = projection of current governed knowledge
note = information without expected treatment
Work Issue = bounded work to treat
issue comment = discussion about that work
Hermes run = external execution record
Change Proposal = proposed versioned change
merge = application of an authorized proposal
```

Cards remain optional. Work Issues and governed execution must work when no card is displayed.

## Notes, comments and Work Issues

A card note is an annotation. It implies no assignment, execution, completion or approval.

An issue comment clarifies or discusses a Work Issue. It does not change status by itself.

A Work Issue exists only when work deserves durable follow-up, assignment, separate discussion, later resumption, independent review or a visible blocker.

A note or comment may be explicitly promoted to a Work Issue Candidate. Actionable wording alone must not trigger promotion.

Do not create a Work Issue for every reasoning step, file read, source lookup, tool call or retry.

```text
note != Work Issue
comment != status change
request != authorization
Hermes returned != issue resolved
```

## Issue creation by Hermes

| Origin | Default treatment |
|---|---|
| explicit user request | create or continue one Work Issue |
| necessary child work inside authorized scope | Hermes may create a linked child issue |
| materially new discovered topic | attach an issue suggestion; do not open automatically |
| contradiction or blocker | mark the current issue waiting or blocked and preserve the reason |

A discovered topic becomes a Work Issue only after user confirmation or a previously admitted rule covering that exact class of follow-up.

## Minimal Work Issue

```yaml
work_issue:
  issue_id:
  case_ref:
  title:
  description:
  origin: human | hermes_child | promoted_suggestion
  parent_issue_ref:
  primary_card_ref:
  issue_type: research | verification | correction | drafting | decision | action
  priority:
  assigned_to:
  requested_effect: read_only | draft | internal_write | external_effect | canonical_effect
  status: open | in_progress | waiting | review | done | cancelled
  close_reason: answered | merged | duplicate | obsolete | rejected | impossible | cancelled
  task_contract_ref:
  context_pack_ref:
  created_by:
  created_at:
  updated_at:
```

Use one business status on the issue.

The Hermes technical state belongs to the Hermes run:

```text
not_started
running
returned
partial
failed
cancelled
unknown
```

The review state belongs to the Change Proposal:

```text
draft
pending_review
changes_requested
accepted
rejected
stale
```

The compact user vocabulary remains:

```text
À traiter
En cours
Besoin de vous
À relire
Bloqué
Terminé
```

A surface may derive `Bloqué` from an issue in `waiting` with a blocking reason. It need not create another stored issue state.

## Hermes writes

Hermes writes only through a controlled Pantheon adapter, never through direct PostgreSQL access.

Within an admitted Task Contract, Hermes may:

- create a necessary child Work Issue;
- attach an issue suggestion for newly discovered work;
- move an assigned issue to `in_progress`, `waiting` or `review`;
- create and update its Hermes run record;
- attach result, sources, Evidence Pack Candidate and trace references;
- create a card with `candidate` or `pending_review` status;
- prepare a Change Proposal against an exact base version;
- mark a resolution candidate;
- execute an exact or conditional merge after the required authority is recorded.

Pantheon validates actor, transition, scope, requested effect, base version and idempotency before persistence.

Hermes must not:

- self-authorize a consequential merge;
- broaden the mandate silently;
- treat runtime success as evidence or approval;
- close a sensitive issue merely because a run returned;
- overwrite a newer card version;
- bypass repository or external-system protections;
- use PostgreSQL as its queue.

## Cards created by Hermes

Hermes may create a durable card record without making it canonical.

| Result | Card posture |
|---|---|
| uncertain or weakly sourced knowledge | `candidate` |
| consequential professional fact or decision | `pending_review` |
| transient answer | remain on the issue; create no card |

Automatic activation is deferred. It may be introduced later only for observed, low-risk and reversible cases under an admitted Pantheon policy.

Every Hermes-created card records its originating issue, run, sources, Case scope and validation state.

```text
card_created != card_confirmed
runtime_return != governed_truth
```

## Change Proposal

A correction creates a Change Proposal instead of overwriting the card.

```yaml
change_proposal:
  proposal_id:
  issue_ref:
  target_object_ref:
  base_version:
  proposed_patch:
  change_summary:
  evidence_candidate_refs: []
  requested_effect:
  review_status:
  created_by:
  created_at:
```

If the target changed after `base_version`, the proposal becomes `stale` and must be rebased or reviewed. Hermes must not overwrite the newer version.

Detailed revision, diff and archive rules remain in:

```text
docs/assets/pantheon-control/card_revision_proposal_lifecycle.md
```

## Delegated merge

A merge is an execution effect, not judgment authority.

The first implementation needs only three modes:

| Mode | Meaning |
|---|---|
| manual | Hermes prepares; the human applies |
| exact | the human authorizes one identified proposal or pull request |
| conditional | the human authorizes it only if named checks pass |

Do not introduce a separate merge-authority service or table in the first slice.

Record the delegation in the existing Task Contract or User Decision Gate and append a material `merge_authorized` event containing:

```text
author
target
allowed head and base
required checks
conflict policy
stale policy
expiry when relevant
single-use posture
```

If a condition fails, Hermes returns `waiting` or `changes_requested`. It does not reinterpret the instruction.

Authorization is scoped and non-transitive. Repository protections and external permissions still apply.

```text
merge executed != merge self-authorized
authorization recorded != conditions satisfied
```

## Minimal PostgreSQL target

The first candidate storage slice contains only the missing work objects:

```text
work_issues
issue_comments
hermes_runs
change_proposals
issue_events
```

Cards, card versions and notes connect to their existing or separately reviewed storage model.

Start with `case_ref`, one optional `primary_card_ref` and one optional `parent_issue_ref`. Add a many-to-many issue/card relation only after a real operational case requires it.

The current state stays directly queryable. `issue_events` records only material events:

```text
issue_created
status_changed
hermes_started
hermes_returned
review_requested
merge_authorized
merge_applied
issue_closed
```

Raw tool calls, reasoning steps, retries and reads remain in Hermes runtime logs. PostgreSQL is the governed record target, not the Hermes execution engine.

## Targeted Context Pack

Hermes receives only the task-relevant context:

- resolved Case scope when required;
- current Work Issue and useful comments;
- pertinent cards and exact versions;
- current decisions and contradictions;
- required source references;
- requested effect and approval ceiling;
- expected output and stop conditions.

Do not send an entire Case database or document corpus by default.

## Card Stack projection

The Card Stack exposes work without owning it. A card face may show only:

```text
3 issues open
1 Hermes run in progress
1 proposal to review
```

Issue discussion, evidence and history belong in a detail surface. Card navigation must not trigger hidden execution.

## Anti-overengineering rules

1. Create an object only when it has a distinct identity and lifecycle.
2. Prefer a field over a new object.
3. Prefer a derived display state over a duplicated stored state.
4. Require real professional cases before adding generic relations.
5. Keep issue creation explicit except for necessary in-scope child work.
6. Create cards only for durable structured knowledge.
7. Reuse Task Contracts, Context Packs, gates and revision doctrine.
8. Store material history, not every runtime operation.
9. Block stale writes instead of building automatic conflict resolution.
10. Keep queues, workers, retries and scheduling in Hermes.

Before adding a feature, ask:

```text
Does it solve at least three real professional situations?
Can it be a field?
Can it be derived?
Can it be added later without a difficult migration?
```

If it lacks real cases and can be derived or deferred, do not add it.

## First implementation slice

1. Work Issue, comment and material event storage;
2. controlled transitions and optimistic version checks;
3. targeted Context Pack and Hermes run record;
4. normalized Hermes return;
5. card candidate and Change Proposal;
6. exact and conditional delegated merge;
7. compact Card Stack indicators.

Any schema, API, test, runtime, protected-path or external integration change requires a separate implementation review.

## Final rule

```text
The card exposes current knowledge.
The Work Issue organizes treatment.
Hermes executes within scope.
Pantheon validates writes and authority.
Merge applies only an authorized, current and checked proposal.
```
