# Refreshing a governance record the code had left behind

Date: 2026-09-02

Status: validation-only trace — governance record refresh, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-09-02-mutation-inventory-refresh.md`; an
  `evidence` field on every `gate_required_not_wired` entry; and
  `test_a_pending_gate_still_points_at_the_code_that_needs_it`.
- Updated: three verdicts from `gate_required_not_wired` to `none` after their
  gaps were repaired; three Information projection entries and the
  `suggest_projects` entry, whose recorded defects were fixed; required-gate
  ceiling 9 → 6.
- Removed: nothing.

## Why

The mutation inventory went stale within a day of being written.

Five findings it recorded were repaired in `main` between 2026-08-31 and
2026-09-01 — the manager lockout (2f9fcfbd), the self-asserted `verified` Claim
status (b201a019), the self-chosen identity assurance (#916), the implicit
unlink in `suggest_projects` (2222a020) and the projection first-write race
(552e67e7). **None of those commits touched the inventory.**

So the record read three gates as open that were closed, and described two
defects that no longer existed, while every test in the file passed.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — this changes a test module and a log; no executable
behaviour changes.
Authority impact: none — the verdicts are review records, not approvals.
Schema/test/CI impact: the inventory test gains one check and lowers one
ceiling; no schema or workflow changes.
External action: none.
Memory behavior: none.

## Why the existing tests could not catch it

They check that every discovered entry point is **declared**, and that a
declared entry names a guard regime and a reason. Nothing checks that the reason
is still true. A verdict, once written, was permanent until someone re-read it.

That is precisely the failure the inventory exists to record — a record
describing a state its subject has left — committed by the inventory itself. It
joins the list the review has been keeping, and it is the first entry on that
list that is structural rather than an error of reading.

## The repair, and why this shape

Each `gate_required_not_wired` entry now carries an `evidence` field: a literal
fragment of the module that makes the gate pending.

```text
act_working_information   raise InformationGateRequired("only a human may act …")
store_reviewed_dossier        review_ref: str,
bind_oidc_identity        def bind_oidc_identity(
apply_edit_request        if request["status"] != "proposed" or …
complete_edit_request     def complete_edit_request(
publish_knowledge         if family not in FAMILIES or review_status not in …
```

Repair the code and the fragment goes; the test then asks for the verdict to be
revisited rather than letting it rot.

This is deliberately the pattern the review recommended everywhere else, and the
one `apu_write_preparation.append_authorization` already uses: **bind the record
to the content it describes, not to a name.** Having spent thirteen batches
recording where the repository does not do that, the inventory had no business
not doing it either.

Verified by breaking it: renaming `bind_oidc_identity` makes the test fail with
the entry named and the missing fragment quoted; restoring the name makes it
pass.

## The cost, accepted

A fragment can move for a reason unrelated to the gate — a rename, a
reformatting — and the test will then fail for nothing. That is the intended
trade: a false alarm asks a question, and a stale governance record answers one
wrongly.

## Local distinctions

```text
declared             != still true
verdict written      != verdict valid
passes its own tests != describes its subject
bound to a name      != bound to a content
```
