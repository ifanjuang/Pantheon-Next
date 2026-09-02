# Removing a flag that promised a guard, and a lookup that discarded its key

Date: 2026-09-02

Status: implemented — two bounded repairs in the candidate implementation.
Boundary profile: bounded_implementation_change.

## Change

- Added: `_selection_row_by_id` in `project_change_variants.py`.
- Updated: `store.ingest` loses the unused `replace_dossier` parameter and both
  call sites; `select_variant_for_change_candidate` looks its selection
  disposition up by id; three inventory entries, one of which was wrong.
- Removed: `_selection_row`, replaced by the id lookup.

## Why

Both were found by reading the last twenty-one mutation entry points, recorded
there, and left for a decision rather than fixed inside a review commit.

**`replace_dossier`** was accepted by `store.ingest`, documented as retained for
API compatibility, and referenced zero times in the body — while both callers
passed `replace_dossier=False`. A reader at either call site would conclude the
dossier was protected from replacement. It was, but by the `DELETE` scoped to
one `source_digest`, not by that flag.

**The replay lookup** read:

```python
_selection_row(conn, replayed["source_review_disposition_id"] and selection_key)
```

`_selection_row` matched on `idempotency_key`. So the expression tested the
stored disposition id, discarded it, and passed this call's key instead —
correct only when a replay reuses the original key. `_candidate_for_source`
matches on `source_result_id`, so a second call for the same result under a
different key reached this branch and raised *variant selection disposition was
not retained* about a disposition that exists. The falsy branch reached the same
error through `idempotency_key = NULL`.

## The entry that had already believed the flag

This is the part worth recording.

The `store.intake_document` entry, written in the same batch and the same file,
read: *"It then delegates with exactly one source and `replace_dossier=False`,
which is what keeps a single-document intake from clearing the dossier it lands
in."*

That guarantee was taken from the flag's name at the call site. The next entry
read `ingest` itself and found the parameter unused. So the inventory shipped
carrying both the finding and the belief the finding falsifies — the exact
failure shape the whole review exists to record, committed inside the record,
on the same day, by the same reading.

Nothing caught it. The consistency test added in #928 covers pending gates; both
of these are `none`. A record can be internally contradictory and every test
still passes.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: `ingest` no longer accepts a keyword it ignored — a caller
passing it now fails loudly instead of being quietly misled. The replay branch
of variant selection returns the disposition instead of raising.
Authority impact: none. Neither change alters who may act or what is admitted.
Schema/test/CI impact: no schema change.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests   1294 passed, 361 skipped
tests/                  593 passed
```

The replay branch is exercised against PostgreSQL in the `tests` job; this
container has no pgvector, so those skip locally.

## Local distinctions

```text
parameter accepted     != parameter honoured
flag named at a call   != guarantee at the callee
record contains finding != record free of what it falsifies
tests pass             != record is consistent
```
