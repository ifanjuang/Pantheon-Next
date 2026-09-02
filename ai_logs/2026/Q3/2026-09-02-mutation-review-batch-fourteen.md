# Reading ten of the twenty-one remaining mutation entry points

Date: 2026-09-02

Status: validation-only trace — governance record extension, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-09-02-mutation-review-batch-fourteen.md`.
- Updated: ten entries from `unreviewed` to `none` with their reasoning; an
  addendum on the already-reviewed `canonize_relation`; unreviewed ceiling
  21 → 11; the read count 71 → 81.
- Removed: nothing.

## Why

The backlog was the last piece of the mutation-entry-point review still
standing. The ten read here are the ones a route can reach today, plus the two
that sit on the Hermes and APU boundaries.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — this changes a test module and a log.
Authority impact: none — verdicts are review records, not approvals.
Schema/test/CI impact: one ceiling lowered; no schema or workflow change.
External action: none.
Memory behavior: none.

## What the batch found

All ten are `none`. None of them needed the chokepoint, and saying that is only
worth something alongside what each one does not check.

**`hermes_runtime_return.record_external_runtime_return`** is the strongest
intake in the inventory, and reading it changed what "strongest" means here.
`_run_for_admission` joins on the admission, not just the run id, so a run from
another admission is refused rather than merely absent. The outcome/payload
correspondence is checked in both directions. `_validate_candidate_sources`
bounds what comes back by what went out: Hermes cannot cite a source it was not
given. Against that, one guard is narrower than its name — the Work Issue
version check is conditional on the run still being `running`.

**`contradictory_review_store.persist_candidate`** carries a guard shape found
nowhere else: an authority ceiling. It reads the report's own `authority` block
and refuses to store it unless `is_evidence`, `is_approval`, `is_zeus_closure`
and `is_task_authorization` are each exactly `False`. `memory != Evidence`
enforced where the row is written, not asserted in a name.

**`source_intake.relate_contained_source`** is stronger below Python than in it:
the self-containment its Python refuses is refused again by a CHECK constraint,
where a second caller cannot route around it. What neither layer refuses is a
cycle.

**`agency_change_candidates.reject_project_candidate`** sits one rung down that
same ladder. Its `actor_kind` is a literal `'human'`, but the events table only
CHECKs the vocabulary `(human, hermes, system)`. Where `entity_relations` can
say no stored row contradicts the doctrine, this module can only say no current
caller does.

## The finding that came back to an entry already reviewed

`propose_relation` validates its endpoints' *type* and never their existence,
and no foreign key can help because the ids are polymorphic. Following that
into `canonize_relation` — the act the doctrine names — showed it does not check
existence either. So an edge between two ids that name nothing can be canonized.

The existing `canonize_relation` entry recorded the actor axis at length and
said nothing about this. It was not wrong; it was incomplete. A reader of a
governance record cannot tell those apart, which is the case for reading an
entry point rather than reading its verdict.

## The finding about composition

`request_project_candidate_revision` opens with `ensure_schema(conn)`, whose
body is a migration followed by `conn.commit()`. Three functions call
`ensure_schema` inline and this is the only one that mutates — the only write
path in `mvp_vertical` that begins by committing.

Under the current routes it is harmless: `with_connection` hands out a fresh
connection per request with nothing in flight. What it costs is composition. The
function cannot be called inside a larger transaction without committing
whatever that transaction had open — the property
`apu_cross_family.create_decision_request` depends on for its own.

## What remains

Eleven entry points, in `agency_data`, `store.ingest`, `cli.main`,
`project_documents`, `human_revision_upload`, `project_change_variants`,
`project_claim_candidates`, `storage_retention`,
`document_revision_discussion` and `agency_change_candidates`.

## Local distinctions

```text
guard in Python        != guard below Python
vocabulary CHECK       != doctrine CHECK
type checked           != existence checked
entry not wrong        != entry complete
harmless here          != composable anywhere
```
