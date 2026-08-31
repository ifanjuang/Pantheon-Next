# Mutation review: the Information Card projection

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-information-projection.md`.
- Updated: three inventory verdicts for `information_projection.py`; unreviewed
  ceiling 33 → 30.
- Removed: nothing.

## Why

The three `information_projection.py` mutation entry points were unreviewed.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — no executable behaviour changes.
Authority impact: none — the verdicts are review records, not approvals.
Schema/test/CI impact: the inventory test's unreviewed ceiling moves; no schema
or workflow changes.
External action: none.
Memory behavior: none.

## Verdicts

| entry point | regime |
| --- | --- |
| `add_document_link` | `none` |
| `remove_document_link` | `none` |
| `update_projection_metadata` | `none` |

All three for the same reason: `projection != persistence` and
`projection != governed identity`. Linking a Document to an Information card,
unlinking it, or editing dates and media types changes what the card is backed
by and how it is shown, not what it says or who may act on it.

## The guards

`actor_kind` reaches all three from `require_human_writer`, a dependency
returning a literal that refuses a Hermes key with 403 — the same body-proof
shape as `agency_information`. None of the three defaults it. Each takes
`expected_revision` under a row lock and is idempotent on a payload digest, and
each writes an event carrying the resulting snapshot.

`add_document_link` verifies that both endpoints exist before writing.
`remove_document_link` asserts `rowcount == 1`, so unlinking something that was
not linked is an error rather than a silent success — the event log cannot
record a removal that removed nothing.

## Two things worth naming, one in each direction

### `observed_version` and `observed_digest` are unverified, and say so

Both are caller-supplied and never checked against the Document. That is the
same structure as several findings in this review — except the fields are named
for what they are. They record what the linker observed, not a validated fact,
and nothing downstream reads them as authority. Twice already this review has
recorded the opposite: a field named for a conclusion holding only an assertion.

### The event type is derived from the write, not predicted before it

`add_document_link` is an upsert. It returns `(xmax = 0)` and chooses
`document_link_added` or `document_link_updated` from that value, so the record
describes what the statement actually did. The comment in the source says a
previous version reported a creation for a role change, leaving the append-only
history describing a link creation that never happened.

That is the inverse of the failure this review keeps finding, fixed deliberately
and explained where the fix lives. Worth recording, because a review that only
collects defects gives a false picture of the codebase it is reviewing.

## Attribution

Fifth form, and unremarkable after the previous four: `actor` is the
`X-Pantheon-Actor` header value, required by the route and — unlike
`agency_information`, which discards it — persisted into the projection event
log.

## Local distinctions

```text
projection             != persistence
projection             != governed identity
observed value         != validated value
derived from the write != asserted beside it
```
