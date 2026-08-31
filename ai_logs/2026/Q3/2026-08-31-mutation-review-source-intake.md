# Mutation review: Source intake

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-source-intake.md`.
- Updated: six inventory verdicts for `source_intake.py`; unreviewed ceiling
  31 → 25.
- Removed: nothing.

## Why

Six of the entry points the widened discovery net found were in
`source_intake.py`, all delegating to one private `_mutate` helper. They are
where material enters consideration, so they sit directly against
`retrieved data != truth`.

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

All six `none`: `update_metadata`, `suggest_projects`, `link_project`,
`unlink_project`, `exclude_source`, `restore_source`.

None of them admits Evidence, approves anything or reaches outside. They set
which Project a Source belongs to, what is recorded about it, and whether it is
in or out of consideration.

## One helper, six callers, and a double concurrency check

`_mutate` carries everything: `_validate_actor`, an idempotency replay keyed on
the payload digest, a locked read comparing `expected_revision`, and then an
UPDATE that repeats the revision in its own WHERE clause and asserts
`rowcount == 1`. A race that slips past the first check still cannot write —
the same shape as `agency_information.update_working_information`, and the
opposite of the projection race recorded in the eighth batch.

`actor_kind` is required on all six, with **no default**, and Hermes is refused
by name with its own `SourceGovernanceGateRequired`. Still a caller-supplied
label — seventh module, same axis — but a caller cannot inherit it by omission.

## Three structural choices worth recording

**A suggestion removes a link by being written.** This record first claimed the
opposite — that `suggest_projects` writes to its own column and never touches
`project_id` or `project_link_status`. Review corrected it. The assignment dict
is on the same line as the call:

```python
assignments={"candidate_project_refs": normalized,
             "project_link_status": "suggested",
             "project_id": None}
```

Suggesting on an already-linked Source therefore unlinks it, and nothing refuses
that or asks for it. The regime stays `none` — the effect is the same class as
`unlink_project`, recorded separately — but it is a state transition no caller
requested, and whether `suggest_projects` should refuse a linked Source or
preserve its link is the owner's to decide.

I wrote the claim from the function's name and purpose without reading the
assignment beside it, then headlined the batch with it. Eighth instance of this
review's own recurring failure, and the most direct: a property asserted from
what the code is for rather than from what it does.

**Restoring does not re-link.** `restore_source` returns an excluded Source to
`unassigned` with a null project, not to whatever project it had before. The
link is a human act that has to be made again.

**`checksum` is named for what it is.** `update_metadata` validates a supplied
checksum as a SHA-256 digest by length and alphabet — a format check, not a
verification: nothing recomputes it from the bytes. The field records what the
intaker asserted, and it is called `checksum` rather than something claiming the
verification did not happen. Twice this review has recorded the opposite — a
field named for a conclusion holding only an assertion — so the honest naming is
worth noting where it appears.

## Local distinctions

```text
suggestion        != link
suggesting        != leaving the link alone
excluded          != deleted
restored          != re-linked
format valid      != verified
required label    != verified identity
```
