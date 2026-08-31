# Mutation review: the Knowledge edit chain

Date: 2026-08-31
Zone: `implementation/`
Scope: the four unreviewed mutation entry points in `implementation/mvp_vertical/knowledge.py`,
plus one correction to a verdict already recorded.

## Why this batch differs from the earlier ones

The nine entry points reviewed first were chosen because nothing in production
reached them. These four are the opposite: each is behind a route that a key
holder can call today, and three of the four take the fields that carry the
claim as body parameters.

## What was read

For each entry point: the function, its route in `cockpit_api.py`, the route's
dependency guard, the request body model, and — this is where the batch turned —
the other functions that write the state the entry point reads.

## Verdicts

| entry point | regime |
| --- | --- |
| `revise_knowledge` | `none` |
| `create_edit_request` | `none` |
| `publish_knowledge` | `gate_required_not_wired` |
| `complete_edit_request` | `gate_required_not_wired` |
| `apply_edit_request` | `gate_required_not_wired` (corrected from `none`) |

## Three findings

### 1. `review_status="reviewed"` is a caller assertion

`POST /documents/{document_id}/knowledge` is guarded by `require_editor_key`, a
bearer-token comparison, and forwards the body with `**body.model_dump()`.
`PublishKnowledgeBody` exposes `created_by`, `actor_kind` — which permits
`hermes` — and `review_status`, which permits `reviewed`. `publish_knowledge`
checks each against a set of permitted strings and nothing else.

A holder of the editor key can publish a Knowledge item that already reads as
professionally reviewed, attributed to anyone, produced by anything. The
repository states `schema conformance != professional approval`; membership in
`REVIEW_STATUSES` is precisely the conformance being taken for the approval.

### 2. A human rejection is reversible by the party it rejected

`knowledge_edit_variants.reject_request` moves an edit request to `rejected` and
records a human rejection event with `knowledge_mutated: False`. Because the
rejection does not revise the Knowledge item, the item's version still equals the
request's `base_version`.

`complete_edit_request` guards no status. Given that same `request_id` and the
Hermes key, it writes a new `replacement_markdown` and computes the status from
the version comparison alone — which still matches — so the request returns to
`proposed`. The editor-keyed apply route then applies it. Nothing beside the
original rejection event records that this happened.

An already-applied request is safe from the same move, but only by accident: the
apply incremented the version, so the comparison sends it to `conflict` instead.

### 3. The retirement of direct revision is a property of the route

`PUT /knowledge/{knowledge_id}` raises 410 with "direct Knowledge revision is
retired; use the project-scoped signed update preview/apply routes".

`create_edit_request` accepts `replacement_markdown` on creation. When it is
present the request is written as `proposed` rather than `queued_for_hermes` —
Hermes is not involved at all. `POST /edit-requests/{request_id}/apply`, guarded
by the same editor key, then calls `apply_edit_request`, which calls
`revise_knowledge`.

One key, three calls, arbitrary replacement text into a governed Knowledge item,
with no signature, no confirmation phrase, no project scope, and no second party.
The signed chain in `knowledge_update.py` is real and unchanged; it is simply not
the only way in.

## The correction, and the shape it makes four of

`apply_edit_request` was recorded `none` with the reasoning that "the request
status already carries the decision". Findings 2 and 3 are two independent ways
to write that status with no decision behind it. The transactional audit and the
concurrency checks in that function are real; what is not real is the decision
they are recorded against.

That is the fourth verdict in this review to be corrected, and all four have the
same shape:

```text
review_ref                     read as a reference to a review
"cannot revoke access.manage"  read as protection of the administrator
_validate_actor                read as a refusal of Hermes
status == "proposed"           read as a decision already taken
```

None was a slip; each was written after reading the function, and each was wrong
one call away from where the reading stopped. The question that finds them is not
"what does this check" but "who controls each input", asked of every link
including the ones that look settled.

## What this batch did not change

No behaviour. This is a review record: five inventory verdicts, the reasoning for
each, and two ceilings moved deliberately — unreviewed 48 → 44, required-gate
3 → 6. The three findings are recorded, not fixed; fixing them changes live
routes and is the owner's call.
