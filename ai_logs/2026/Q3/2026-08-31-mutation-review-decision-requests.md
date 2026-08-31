# Mutation review: the Decision Request inbox

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-decision-requests.md`.
- Updated: three inventory verdicts for `decision_requests.py`; unreviewed
  ceiling 36 → 33; required-gate ceiling 7 → 8.
- Removed: nothing.

## Why

The three `decision_requests.py` mutation entry points were unreviewed, and one
of them writes the decision record the whole governed loop exists to produce.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — no executable behaviour changes.
Authority impact: none — the verdicts are review records, not approvals.
Schema/test/CI impact: the inventory test's ceilings move; no schema or workflow
changes.
External action: none.
Memory behavior: none.
Zone: `implementation/`
Scope: the three unreviewed mutation entry points in
`implementation/mvp_vertical/decision_requests.py`.

## Verdicts

| entry point | regime |
| --- | --- |
| `create_request` | `none` |
| `cancel_request` | `none` |
| `resolve_request` | `gate_required_not_wired` |

## This module already has the concept the review has been asking for

Five batches have now recorded the same gap in different clothing: authorization
is verified, attribution is asserted. The question left open for the owner was
whether governed mutation routes should take an authenticated principal.

`decision_requests` answers it, and it answered it before this review started.
`resolve_request` requires `identity_assurance`, which is `declared` or
`authenticated`, and refuses the pairing that would make the field decorative:

```python
if identity_assurance == "authenticated":
    if not isinstance(authenticated_principal, dict): raise
    if not authenticated_principal.get("user_id") or not authenticated_principal.get("identity_provider"): raise
elif authenticated_principal is not None:
    raise  # declared assurance cannot carry a principal
```

The distinction is modelled, mandatory, and persisted on the decision record
itself. That is the shape the other four modules are missing.

## And the caller chooses which one describes itself

`ResolveDecisionRequestBody` carries `identity_assurance` and
`authenticated_principal`. The route forwards the body with `**values` and
supplies `decided_by` from the `X-Pantheon-Human-Actor` header.

So the party that asserts the name also selects the assurance level describing
that assertion, and supplies the principal said to back it. The validation is
that a dict has two non-empty keys. Nothing authenticates anything.

A row in `agency_decision_records` can therefore read
`identity_assurance: authenticated`, with a principal and an identity provider,
on a decision that nothing authenticated. The default is `declared`, which is
honest; it is the upgrade that costs nothing.

The `mvp_governed_loop_objects` contract validates the decision projection, and
that validation constrains the value of the field, not its truth — the same
distinction as `schema conformance != professional approval`, one level down.

## Why this is the gate requirement and the other two are not

`resolve_request` writes `approve`, `refuse`, `request_revision` or
`request_more_evidence` against a candidate digest. It is the decision the whole
governed loop exists to record. Its concurrency and idempotency are the most
careful in the codebase — locked read, status check, `expected_revision` repeated
in the UPDATE's WHERE clause, unique decision identity, event replay keyed on the
payload digest, and the record and the status transition in one transaction.

None of that is the problem. What the record says about who decided is.

`create_request` asks for a decision rather than taking one, and writes `status`
as a literal `'pending'` in its INSERT — the same shape `create_variant_request`
uses and `knowledge.create_edit_request` does not, so no caller can create a
request that arrives already resolved. `cancel_request` withdraws a pending
request, insists on a rationale, and records the actor.

## What this batch did not change

No behaviour. Three verdicts and two ceilings moved: unreviewed 36 → 33,
required-gate 7 → 8.

## Local distinctions

```text
models the distinction != sources the distinction
assurance level        != assurance
validates the value    != validates its truth
careful write          != trustworthy record
```
