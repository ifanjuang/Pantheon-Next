# Work Issue and delegated merge model

Date: 2026-07-18

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md` as candidate support doctrine.
- Distinguished card notes, issue comments, Work Issues, Hermes runs, Change Proposals and merge.
- Reduced the issue lifecycle to one business status plus a close reason.
- Kept technical execution state on `hermes_runs` and review state on `change_proposals`.
- Allowed Hermes to create necessary child issues, attach discovered-work suggestions, create card candidates and update bounded states through a controlled adapter.
- Defined exact and conditional human delegation for merge using existing Task Contracts, User Decision Gates and material events.
- Clarified `AGENTS.md` so the forbidden act is self-authorized or unapproved merge, not execution of an exact governed delegation.
- Proposed only five missing PostgreSQL work tables and explicit anti-overengineering rules.

## Why

A candidate-only return model is too passive for ordinary professional work, while a general issue engine, policy service and multi-axis state machine would be premature. The reduced model supports real follow-up and delegated merge without making Pantheon a runtime or duplicating existing governance objects.

## Boundary

Protected paths touched: no.
Runtime impact: none.
Authority impact: candidate doctrine added; canonical Hermes merge wording clarified for exact governed delegation.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Local distinctions

```text
note != Work Issue
comment != status change
Hermes returned != issue resolved
card created != card confirmed
merge executed != merge self-authorized
PostgreSQL record != Hermes queue
documented contract != implemented feature
```

## Simplifications retained

```text
one issue business status
runtime state on Hermes run
review state on Change Proposal
resolution as close reason
discovered work as suggestion by default
no merge-authority service or table
no many-to-many issue/card relation before a real need
material events only
```

## Remaining work

- Review and merge the doctrine clarification.
- Decide the first implementation slice and protected-path schema review separately.
- Implement any Hermes binding outside Pantheon runtime authority.
- Validate the compact mobile issue projection before production UI work.
