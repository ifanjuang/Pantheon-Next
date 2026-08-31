# Mutation review: the Hermes execution boundary

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-hermes-execution-boundary.md`.
- Updated: seven inventory verdicts across `hermes_execution.py`,
  `hermes_handoff_store.py`, `hermes_launch_context.py`,
  `hermes_result_candidate.py` and `execution_results.py`; unreviewed ceiling
  30 → 23.
- Removed: nothing.

## Why

The remaining unreviewed entry points are spread one to three per module, so
this batch is grouped by responsibility rather than by file: everything on the
path from a handoff request to a stored result. It is the cluster the doctrine
cares about most — `implementation success != authorization`, and Hermes must
not approve, canonize or promote.

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

All seven `none`.

```text
hermes_handoff_store.submit_handoff
hermes_execution.revoke_admission
hermes_execution.record_external_runtime_start
hermes_launch_context.reserve_launch
hermes_result_candidate.create_result_candidate
execution_results.store_execution_result
execution_results.append_review_disposition
```

## Three controls this review had not seen before

### A guard enforced below Python

`append_review_disposition` refuses `accepted_for_claim` and
`selected_for_change_candidate` for a non-human reviewer — and so does
`validate_execution_result_review_disposition`, a trigger on the table.

That answers, concretely, the weakness recorded against
`agency_classification._validate_actor`: it was not a second layer because a
direct caller inherited its default. A trigger *is* a second layer, because a
second Python caller cannot route around it.

### Two keys, two sides, no overlap

```text
admit_handoff / revoke_admission        editor key + human actor
reserve_launch / runtime start / return Hermes key + Hermes actor
```

The name in the header is still unverified — sixth module, same story. But no
key can play both sides: Hermes cannot admit its own handoff, and a human editor
cannot forge the runtime callback. Authorization is separated even though
attribution is not.

### Code that states what it does not mean

`record_external_runtime_start` returns its own non-equivalences as data:

```text
runtime start recorded != Evidence
launch reservation     != dispatch
running                != task success
```

And `reserve_launch`'s docstring names the assumption a caller would otherwise
make: a replay of the same idempotency key returns the same immutable
reservation and is not permission to submit Hermes again.

## The digest chain, corrected

The first version of this record claimed `preview_digest` was taken from the
caller's preview and never recomputed from that preview's content anywhere in
the codebase. **That was wrong, and review caught it.**

`hermes_handoff_preview.build_preview` sets

```python
preview["preview_digest"] = _digest(preview)
```

over the preview it has just built. The sole production caller of
`submit_handoff` — `submit_hermes_handoff` — rebuilds the preview server-side
with `prepare(preview_body)` and passes that object; the client's
`expected_preview_digest` is only compared against it, to reject a stale scope
with 409. The client cannot supply the digest that gets stored.

What remains true is narrower, and is the shape this review has recorded
repeatedly: the protection is **route-borne, not module-borne**.
`submit_handoff` does not recompute the digest from the preview it is handed, so
a second caller added later would inherit none of it, while the chain every
downstream stage relies on — the immutable basis at admission, the re-derivation
in `get_execution_envelope` — would still read as anchored.

## How the wrong version happened

The claim rested on a `grep` for `preview_digest` truncated by `head -20`. The
assignment lives in `hermes_handoff_preview.py`, a file the batch never opened,
and it was below the cut.

That is the second time today a record asserted something from a search result
taken for the search itself; the first was an event-write count read off
`actor_kind=` matches. Both are the same move this review keeps recording
against the code, committed against the code by the review.

The original note still stands on its own terms, and is worth keeping: I nearly
wrote seven `none` verdicts without examining this link at all, on the module
whose other controls are the strongest in the codebase. Strength elsewhere is
not evidence about the link you did not read — and a truncated search is not a
reading.

## Local distinctions

```text
admitted read_only     != authorized consequential
runtime start recorded != Evidence
launch reservation     != dispatch
route-borne guard      != module-borne guard
truncated search       != reading
checked in Python      != checked below Python
```
