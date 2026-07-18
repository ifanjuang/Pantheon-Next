# Work Issue and delegated merge model

Date: 2026-07-18

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md` as a candidate support doctrine.
- Distinguished card notes, issue comments, Work Issues, Hermes runs, Change Proposals, review and merge.
- Defined issue-creation thresholds, orthogonal status axes and anti-proliferation rules.
- Allowed Hermes to create bounded child issues, propose discovered issues, create card candidates and update runtime-owned states through a controlled Pantheon adapter.
- Defined exact and conditional human delegation for merge.
- Clarified `AGENTS.md` so the forbidden act is self-authorized or unapproved merge, not execution of an exact governed delegation.
- Proposed a minimal PostgreSQL target model while preserving Hermes ownership of queues, workers, retries and scheduling.

## Why

A candidate-only return model is too passive for ordinary professional work. Hermes needs to report state, create follow-up work, create structured card candidates and apply a merge when the human explicitly delegates that exact effect. At the same time, runtime success must not become approval and Pantheon must not become the execution engine.

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

## Remaining work

- Review and merge the doctrine clarification.
- Decide the first implementation slice and protected-path schema review separately.
- Define controlled API transition rules and optimistic version checks.
- Implement any Hermes binding outside Pantheon runtime authority.
- Validate the compact mobile issue projection before production UI work.
