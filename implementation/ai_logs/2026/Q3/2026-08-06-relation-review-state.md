# Relations gain a review state; Hermes may propose

Date: 2026-08-06
Scope: `mvp_vertical/sql/015_entity_relations.sql`, `entity_relations.py`, `entity_relation_api.py`
Axes: E4 certainty, V4 verification, K3 consequence, C2 approval (human decision, recorded)

## What was decided

Two human decisions, this date.

**A relation is not canonical when it is written.** Every other family in this
repository has a candidate path — Change Candidate, Knowledge edit, Source
admission, Hermes result. Relations were the exception: `agency_entity_relations`
had no status column, so a relation was true the instant a human typed it, and
Hermes could not suggest one at all. It now passes through
`proposed -> canonical -> retired`, or `proposed -> rejected`.

**Hermes may propose.** That is the only act it is admitted to. Canonizing,
rejecting and retiring stay human. The gate is in the schema as well as in the
module:

```sql
CHECK (actor_kind = 'human' OR event_type = 'relation_proposed')
```

so a caller that bypasses `entity_relations.py` still cannot record Hermes
canonizing anything.

**The endpoint vocabulary opens; `relation_type` stays closed.** Endpoints accept
every project-scoped type the plan names, reusing the vocabulary
`016_work_issue_scopes.sql` already established rather than inventing a second
one. A tranche that introduces an owner adds an arm to
`resolve_agency_entity_relation_project` — a `CREATE OR REPLACE`, so no table
lock and no constraint migration. Tranches D through G would otherwise each have
migrated the same CHECK, four serialization points on one file between two agents
working in parallel.

The doctrinal control is on the *meaning*, not on the endpoint: the four canonical
relation types remain the only permitted values. An endpoint whose owner table
does not exist yet is refused by the resolver, by name — one enforcement point
instead of two kept in sync.

## The bug the backfill probe found

Adding a status column to a populated table means backfilling it, and the backfill
is the dangerous half.

The scope guard installed by the *previous* version of this migration accepts
exactly one UPDATE shape — active to retired, advancing the revision. A backfill
is neither: it is a row keeping its meaning and gaining a column. So the migration
died here:

```text
psycopg.errors.RaiseException: Entity relation update must be one
active-to-retired transition
```

on **every installation that already held a relation**, at the next boot. No
existing test could see it. Every local database was empty, so the backfill
touched no rows and the trigger never fired — the same blindness that hid the
guard-marker regression in `005_change_candidate_review.sql`.

The fix drops the stale trigger before the backfill; the guarded `CREATE TRIGGER`
further down restores the new one, and the file runs in one transaction, so no
writer ever sees the table unguarded.

## Backfill mapping

```text
retired_at IS NULL   -> canonical
retired_at IS NOT NULL -> retired
```

Nothing becomes a proposal retroactively. Under the old rules an unretired
relation was canonical — that is what its author asserted. Backfilling it to
`proposed` would claim a human review that never happened, which is the one
mapping that would be a lie.

## Status

- implemented: status column and state machine, the Hermes proposal gate in
  schema and module, `propose_relation` / `canonize_relation` / `reject_relation`
  / `retire_relation`, the widened endpoint vocabulary and resolver, the widened
  uniqueness predicate so a refusal frees the edge.
- implemented: `POST /hermes/entity-relations`, guarded by the Hermes key. Hermes
  reaches relations through it and through nothing else.
- implemented: `tests/test_entity_relation_migration.py`, which applies the
  previously shipped migration to a throwaway database, writes an active and a
  retired relation through it, and only then applies the migration under test.
  Verified to reproduce the boot failure above when the fix is removed.
- full suite `1205 passed`, no skips.

## Open

`EntityRelationDecisionBody.expected_revision` lost its `le=1` bound, which was a
two-state assumption. There is no upper bound now; a relation advances at most
twice, so one could be reinstated, but the value is checked against the row under
lock either way.

## Boundary

```text
proposed  != canonical
propose   != decide
Hermes    != author of truth
rejected  != deleted
open vocabulary != open meaning
```

No relation type was added. Nothing here approves, admits Evidence, promotes
memory or authorizes a task.
