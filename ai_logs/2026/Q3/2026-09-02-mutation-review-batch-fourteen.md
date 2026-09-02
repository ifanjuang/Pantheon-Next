# Reading the last twenty-one mutation entry points

Date: 2026-09-02

Status: validation-only trace — governance record extension, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-09-02-mutation-review-batch-fourteen.md`.
- Updated: twenty-one entries from `unreviewed` to `none` with their
  reasoning; an addendum on the already-reviewed `canonize_relation`; the
  unreviewed ceiling from 21 to 0, which turns that test from a bound on a
  backlog into a rule; the read count 71 → 92.
- Removed: nothing.

## Why

The backlog was the last piece of the mutation-entry-point review still
standing. It is now empty: all ninety-two enumerated entry points have been read
individually.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — this changes a test module and a log.
Authority impact: none — verdicts are review records, not approvals.
Schema/test/CI impact: the unreviewed ceiling becomes 0, so a new mutation
entry point must be reviewed when it is added rather than admitted to a
backlog; no schema or workflow change.
External action: none.
Memory behavior: none.

## What the batch found

All twenty-one are `none`. None of them needed the chokepoint, and saying that
is only worth something alongside what each one does not check.

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

## The second half

**`storage_retention.retain_document_version`** verifies the bytes against the
digest recorded on the version *before* it stores anything, and derives the
Storage Object's identity from that digest. It is the direct counter-example to
`source_intake.create_source`, where a checksum is optional and only its shape
is checked. It also takes no locks at all: every write is
`ON CONFLICT DO NOTHING` followed by a read-back that must equal what was
intended — sound precisely because identity is the content.

**`project_claim_candidates.create_claim_from_candidate`** and
**`project_change_variants.select_variant_for_change_candidate`** both lock
first and read the decision under the lock, and both say why in a comment
beside the code. The APU application path had the same problem to solve and had
to be repaired for it this morning. Same repository, same class of problem,
already solved correctly twice.

**`human_revision_upload.upload_revision`** is the only entry point in the
inventory that authorizes a named principal rather than a shared key: three
`require_access` checks, then a scope check. It re-runs all three after
conversion and retention, with the reason written down — access revoked during a
long conversion should stop professional admission without erasing intake stages
that already happened. That is the opposite decision from the APU repair, where
the window between the check and the act was closed with a lock. Both are right;
the difference is what each window costs.

## Two findings worth more than their size

**A parameter that asserts a guard its function does not have.**
`store.ingest` accepts `replace_dossier`, documents it as retained for API
compatibility, and references it zero times in the body — while both callers
pass `replace_dossier=False`. A reader at either call site would conclude the
dossier is protected from replacement. It is, but by the digest-scoped DELETE,
not by that flag. This is the shape the whole review has been cataloguing,
reduced to its smallest form.

**A lookup that discards the value that would make it correct.**
`select_variant_for_change_candidate`, on its replay branch, calls
`_selection_row(conn, replayed["source_review_disposition_id"] and
selection_key)`. `_selection_row` matches on `idempotency_key`, so the
expression tests the stored disposition id, throws it away, and passes this
call's key instead — correct only when a replay reuses the original key. Since
`_candidate_for_source` matches on `source_result_id`, a second call with a
different key reaches this branch and raises *variant selection disposition was
not retained* about a disposition that exists.

## What the whole review leaves standing

Six entry points recorded as `gate_required_not_wired`, each bound to the
absence it claims. Everything else is `none`, with its reasoning and its
findings written beside it. Nothing is enumerated-but-unread.

## Local distinctions

```text
guard in Python        != guard below Python
vocabulary CHECK       != doctrine CHECK
type checked           != existence checked
entry not wrong        != entry complete
harmless here          != composable anywhere
parameter accepted     != parameter honoured
enumerated             != read
```
