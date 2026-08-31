# Mutation review: canonizing an Entity relation

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Change

- Added: `ai_logs/2026/Q3/2026-08-31-mutation-review-entity-relation-canonization.md`.
- Updated: three inventory verdicts for `entity_relations.py`; the discovery
  signal made transitive after review; seven further entry points declared and
  one of them reviewed; enumerated total 85 → 92; unreviewed ceiling 28 → 31;
  discovery floor 84 → 91.
- Removed: nothing.

## Why

`canonize_relation`, `reject_relation` and `retire_relation` were three of the
thirteen entry points the widened discovery net found in the previous batch.
Canonization is the act the doctrine names, so it went first.

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

All three `none`.

## Three layers, and what they actually guarantee

This is the most layered guard in the codebase.

```text
route     separate endpoint from the Hermes proposal route;
          actor_kind="human" passed as a literal; editor key; human actor
module    _actor(..., proposing=False) accepts only "human", no default
database  agency_entity_relation_events_hermes_proposes_only
          CHECK (actor_kind = 'human' OR event_type = 'relation_proposed')
```

The Hermes-facing route exists and passes `actor_kind="hermes"` — and it can
only reach `propose_relation`. Proposing admits Hermes; canonizing, rejecting
and retiring do not.

**And none of the three verifies that the label is true.** A caller presenting
`human` passes all of them. What the constraint guarantees is narrower and worth
naming precisely: the audit trail can never contain the contradiction. No stored
row can say Hermes canonized a relation.

That is internal consistency of the record. It is real, it is the strongest form
this review has found, and it is not the same as knowing who acted.
`canonize_relation`'s docstring says "Hermes cannot reach this". What holds is
"no record can say Hermes reached this".

## The ladder this completes

Across six modules the same unverified label is defended at four different
strengths:

```text
agency_classification   a Python check on a defaulted label   a direct caller omits it
agency_information      a literal at the route                body-proof; module still trusts
execution_results       a trigger on the claim dispositions   a second Python caller cannot pass
entity_relations        a CHECK tying kind to event type      no row can contradict itself
```

The review has recorded the weak end repeatedly. Recording the strong end is
what makes the weak end a finding rather than a complaint: the repository knows
how to do this, in SQL, on the act it cares most about.

## Amendment: the widened net was still too narrow, then briefly too wide

Review caught the discovery signal added in the previous batch. It intersected
each function's calls with *private* helpers in its own module, and still missed
`create_scoped_issue` — the entry point of `POST /work/issues` — because that
one delegates to two *public* functions in another module. I had concluded it
was already declared from its absence in the undeclared list, without opening
the inventory. That is the same move the net was being corrected for.

Making the closure transitive over whole subtrees then caught every
`install_*_routes` and `create_app` in the package: eighteen wiring functions
that *define* route handlers calling writers rather than calling writers
themselves. Too narrow missed thirteen; naive-transitive added eighteen that
mean nothing.

The net that holds counts a function's own calls with nested definitions
excluded, and follows them to a fixpoint across modules. It finds seven more
real delegators:

```text
work_issue_scopes.create_scoped_issue      POST /work/issues
store.intake_document
apu_mapping_converter.convert_and_store
human_revision_upload.upload_revision
project_change_variants.select_variant_for_change_candidate
project_claim_candidates.create_claim_from_candidate
cli.main
```

`create_scoped_issue` is reviewed here — it composes two already-reviewed
functions into one transaction, requires exactly one primary scope and refuses
duplicate endpoints. The other six join the backlog.

## Also worth keeping

`_decide` is shared by all three. The source explains why: writing them once
keeps the optimistic lock, the replay check and the audit record identical
across canonizing, rejecting and retiring, "which is what a reader of the
history is entitled to assume". Retirement stamps `retired_by` and moves the
status rather than deleting the row, so a relation that was true stays readable
as having been true and withdrawn.

## Local distinctions

```text
checked label          != verified identity
consistent record      != true record
no row can say it      != it cannot happen
proposing              != canonizing
retired                != deleted
```
