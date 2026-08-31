# Mutation review: the Work Issue lifecycle — and a hole in the net

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-work-issue-lifecycle.md`.
- Updated: a third discovery signal in
  `implementation/tests/test_consequential_mutation_inventory.py`, which found
  13 previously invisible entry points; nine verdicts across `work_issues.py`
  and `work_issue_scopes.py`; enumerated total 72 → 85; unreviewed ceiling
  23 → 28; discovery floor 70 → 84.
- Removed: nothing.

## Why

The Work Issue row is what the whole Hermes execution boundary reads: batch
nine established that `admit_handoff` refuses anything but a `read_only`
`requested_effect` on an open issue assigned to Hermes. Reading the module that
writes that row was the obvious next batch. It turned into something else.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — the discovery signal is test-side; no executable
behaviour changes.
Authority impact: none — the verdicts are review records, not approvals.
Schema/test/CI impact: the inventory test gains a third discovery signal and
moves two bounds; no schema or workflow changes.
External action: none.
Memory behavior: none.

## The finding: the instrument was under-counting

While reading `work_issues.py` I looked for `transition_issue` in the inventory
and it was not there. Nor were twelve others.

Discovery recognised a public function two ways: a name beginning with `apply`,
`admit`, `promote`, `approve` or `commit`, or a literal SQL write in its own
body. Neither sees a public function that delegates its write to a private
helper in the same module — a normal shape in this codebase.

```text
work_issues.transition_issue          the only general status move
work_issues.close_issue               the only path to done
entity_relations.canonize_relation    canonization, by name
entity_relations.reject_relation      entity_relations.retire_relation
source_intake.exclude_source          restore_source, link_project,
                                      unlink_project, update_metadata,
                                      suggest_projects
hermes_runtime_return.record_external_runtime_return
apu_cross_family.create_decision_request
```

The miss was not random. It fell on functions whose names are verbs of
consequence — closing, canonizing, excluding, transitioning.

A third signal now catches them: a public function that calls a private
same-module helper whose body writes.

### Why the guard could not have caught itself

Two tests guarded discovery. One asserts every discovered entry point is
declared; the other that discovery is not vacuous. Both passed throughout.
Neither can fail for something the net never saw.

The control verified its output and never its coverage. That is the same
failure this inventory exists to record, committed by the inventory — and it is
the seventh distinct instance in this review, this time in the instrument
rather than in a verdict.

## The nine verdicts, all `none`

The lifecycle module is strong, and specifically strong in the way the doctrine
needs.

`record_hermes_return` is the clearest statement in the codebase of what Hermes
may not do. The caller names an outcome; the resulting issue status is looked up
in `RETURN_TO_ISSUE_STATUS`, whose entire range is `review` and `waiting`.
**Hermes cannot name `done`, because it never names a status at all.**

`start_hermes_run` copies `requested_effect` from `issue["requested_effect"]`
rather than accepting it — so the bound on what a run may do comes from the
governed row, not from whoever starts it.

`close_issue` holds `to_status="done"` and `actor_kind="human"` as literals in
its body, and `ALLOWED_TRANSITIONS` permits `done` only out of `review`.

`transition_issue` is the exception worth naming: it takes both `to_status` and
`actor_kind` from its caller. Its sole production route passes literals behind
the editor key and a human actor, and the state machine bounds the rest — but it
is route-borne, not module-borne, for the seventh time in this review.

## Two more guards below Python

```text
work_issues.requested_effect      CHECK constraint on five permitted effects
work_issue_scope_links            DELETE refused: retain and retire instead
work_issue_scope endpoints        trigger rejects an unknown project or decision
```

The first is load-bearing for the Hermes boundary: `admit_handoff` reads that
column, and this module never validates it. The constraint that bounds external
execution is enforced in SQL.

## Local distinctions

```text
verified output        != verified coverage
delegates its write    != performs no write
names an outcome       != names a status
route-borne guard      != module-borne guard
enumerated             != discovered
```
