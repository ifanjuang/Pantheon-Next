# Append-only logs could not be ordered by their own timestamp

Date: 2026-08-06
Scope: eight append-only event tables
Axes: E4 certainty, V4 verification, K2 consequence, C0 approval (defect correction, no vocabulary or authority change)

## The defect

`occurred_at` defaulted to `CURRENT_TIMESTAMP`, which in PostgreSQL is the
**transaction start time**, not the statement time. Every event written inside one
transaction therefore carries the same `occurred_at`, to the microsecond.

Three read paths order by it:

```text
work_issues.py:555                  ORDER BY occurred_at, event_id
knowledge.py:667                    ORDER BY occurred_at, event_id
agency_change_candidate_review.py   ORDER BY occurred_at, event_id
apu_mapping_reviews.py              ORDER BY occurred_at, review_id
```

The tiebreak is a random UUID in every case, so when the discriminator is constant
the visible order of the history is arbitrary.

`work_issues.record_hermes_return` makes this concrete: it writes `status_changed`,
`hermes_returned` and `review_requested` in one transaction, all three carrying the
**same `expected_version`** — so `resulting_version` cannot separate them either.
Reproduced before the fix:

```text
AssertionError: three events written in one transaction share an occurred_at:
['2026-08-06T11:48:17.970908+00:00',
 '2026-08-06T11:48:17.970908+00:00',
 '2026-08-06T11:48:17.970908+00:00']
```

An append-only log whose order is arbitrary is not an audit trail. Nothing was
lost or mis-written; what was unavailable is the sequence.

## What changed

`clock_timestamp()` on eight `occurred_at` columns — it advances per statement, so
the write order is recoverable. `013`–`016` already used it; this brings the rest
into line.

```text
issue_events                          001_work_issues.sql
agency_project_events                 002_agency_data.sql
agency_change_candidate_events        002_agency_data.sql
agency_source_events                  009_source_intake_admission.sql
execution_result_review_dispositions  010_execution_results.sql
apu_mapping_review_events             011_apu_mapping_reviews.sql
hermes_execution_admission_events     hermes/005_admission_lifecycle.sql
knowledge_events                      store.DDL
```

Each is applied twice over: directly in the `CREATE TABLE`, so fresh databases are
born correct, and through a catalog-guarded `ALTER COLUMN ... SET DEFAULT` for
databases that already exist. `CREATE TABLE IF NOT EXISTS` never revisits an
existing table, which is why the guarded half is required and why `store.DDL`
needed one too.

Every guard keys on `column_default LIKE '%clock_timestamp%'` — a value the
migration **adds**, never one shared with the definition it replaces.

## How the eighth was found

The first seven came from reading the migration files. The eighth,
`knowledge_events`, is defined in `store.DDL` rather than in any numbered
migration, and a file-by-file reading missed it.

It was caught by extending
`test_guarded_migrations_reach_their_target_schema_on_a_fresh_database` to query
the **catalog** for any `occurred_at` whose default is not `clock_timestamp()`,
rather than checking a list of tables. The derived form found on its first run what
the enumerated form would have kept missing, and it covers tables added later
without anyone remembering to update it.

## Status

- implemented: the eight defaults, fresh and guarded.
- implemented: `test_events_written_in_one_transaction_are_orderable`, which
  reproduces the three-event case and asserts distinct, increasing, correctly
  ordered timestamps. Verified to fail before the change.
- implemented: the catalog-derived assertion in the fresh-database migration test.
- verified: a throwaway database applying `store.DDL` plus the Work Issue and
  Hermes chains reaches `clock_timestamp()` on all three of its event logs.
- full suite `1193 passed`, no skips.

## Boundary

```text
event order    != event content
timestamp fix  != new vocabulary
audit trail    != approval
```

No event type, actor rule, approval level or authority was changed.
