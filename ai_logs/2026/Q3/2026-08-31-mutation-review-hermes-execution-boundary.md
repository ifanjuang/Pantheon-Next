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

## The finding: the first link of the digest chain is asserted

`preview_digest` is taken from the caller's preview in `submit_handoff` and
**never recomputed from that preview's content**, anywhere in the codebase.

Everything downstream compares it: the immutable basis at admission, the
re-derivation in `get_execution_envelope`, `expected_preview_digest` at the
handoff API. So it is a genuine seal against drift *between* stages — and the
value it seals was supplied rather than computed.

Recorded rather than escalated. The effect of `submit_handoff` is a request, and
the admission it can reach is bounded to `read_only` work on an open Work Issue
whose Task Contract and Context Pack must already match the handoff's. The
constraint that does the work there is the governed Work Issue row, not the
digest.

I nearly wrote seven `none` verdicts without checking this one, on a module
whose other controls are the strongest in the codebase. Strength elsewhere is
not evidence about the link you did not read.

## Local distinctions

```text
admitted read_only     != authorized consequential
runtime start recorded != Evidence
launch reservation     != dispatch
compared digest        != computed digest
checked in Python      != checked below Python
```
