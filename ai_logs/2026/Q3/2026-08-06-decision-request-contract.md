# Decision Request contract

Date: 2026-08-06
Status: contract candidate implemented in schema, persistence pending.

## Observed state

Pantheon already owns the immutable `decision_record` contract in
`mvp_governed_loop_objects.schema.yaml`. The current MVP Cockpit still projects a
WorkIssue in review as if that projection were a Decision and mutates the
WorkIssue directly through validate/refuse routes. This conflicts with the
accepted information architecture:

```text
Decision Request / Gate != Decision
Decision != WorkIssue projection
```

A Decision has its own recorded human identity. A WorkIssue may be blocked by
one unresolved Decision Request, but the request and the task remain distinct.

## Decision

Add a `DecisionRequest` Gate contract for the human attention inbox. It carries:

```text
question and user-facing type
response mode and bounded options when applicable
candidate reference and digest
Project and WorkIssue links when applicable
sources, evidence gaps and blocked action
required owner, surface, priority and optimistic revision
```

Resolving a request must create a separate existing `decision_record`; it does
not transform the request into a Decision. A global view and a Project view show
the same request identity.

At most one pending blocking request may target one WorkIssue. Non-blocking
preference requests may coexist when the external Task Contract allows a safe
fallback.

## Resolution boundaries

```text
request pending != human decision
request visible != approval
Decision recorded != runtime resumed
Decision recorded != WorkIssue transitioned
Decision recorded != action executed
Action executed != result validated
```

A continuation, revised Task Contract or manual step is prepared separately and
must retain the Decision reference. No scheduler, queue or hidden resume path is
introduced.

The four canonical `decision_value` outcomes remain owned by the existing
`decision_record` contract. Option and free-text responses are recorded in the
Decision consequences while the canonical decision value describes the reviewed
candidate posture.
