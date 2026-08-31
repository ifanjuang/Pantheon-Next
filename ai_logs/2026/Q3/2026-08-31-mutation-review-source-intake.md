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

**A suggestion cannot become a link by being written.** `suggest_projects`
writes to its own column and never touches `project_id` or
`project_link_status`. `retrieved data != truth`, kept in the table shape rather
than in a rule someone has to remember.

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
excluded          != deleted
restored          != re-linked
format valid      != verified
required label    != verified identity
```
