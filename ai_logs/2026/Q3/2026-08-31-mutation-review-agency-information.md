# Mutation review: the Agency Information series

Date: 2026-08-31
Zone: `implementation/`
Scope: the four unreviewed mutation entry points in
`implementation/mvp_vertical/agency_information.py`.

## What was read

Each function; its route in `agency_data_api.py`; the route's dependencies as
they are actually wired in `cockpit_shell.py`; and the table the effect lands in.

## Verdicts

| entry point | regime |
| --- | --- |
| `create_information` | `none` |
| `derive_working_version` | `none` |
| `update_working_information` | `none` |
| `act_working_information` | `gate_required_not_wired` |

## The route guards here are the strongest in the review so far

Worth recording, because most of this review has been corrections.

`actor_kind` reaches all four functions from `require_human_agency_writer`, a
dependency returning a literal. No request body can influence it. That dependency
refuses a Hermes key with 403, and returns 503 if the editor and Hermes keys are
configured identically. `update_working_information` gates `actor_kind="hermes"`
behind a `hermes_admitted` flag that no route passes, so Hermes editing is
refused unconditionally in production rather than by configuration.

Three of the four take `actor_kind` with **no default**, so a future direct
caller has to state its claim instead of inheriting one. That is precisely the
defect corrected in the classification cluster, avoided here.

`update_working_information` checks concurrency twice: the locked read compares
`expected_revision`, and the UPDATE repeats the revision in its WHERE clause and
asserts `rowcount == 1`. A race that slips past the first check still cannot
write.

## Amendment: one of the strengths above was not there

Review caught a claim in the first version of this record. It said
`create_information`'s field allowlist was "derived from the schema rather than
written out twice". Neither half was true.

The set passed to `_schema_values` is seventeen names spelled out at the call
site, duplicating the keys of the dict immediately above it. `_schema_values`
forwards whatever allowlist its caller hands it to
`normalize_declared_fields`, which validates against the field registry — not
against any declared view. A `create` view exists in the Information schema and
today matches the handwritten set exactly, minus `project_id`, which is a path
parameter rather than a body field. Nothing holds the two in step.

`update_working_information` next door genuinely does derive its allowlist,
through `_editable_fields()` and the `edit` view. The two paths differ in kind,
and the reading above collapsed them because `_schema_values` sounds like the
derivation it is not.

That is the same failure this review keeps recording, committed once more inside
the batch that praises the module for avoiding it: a guard described by what it
resembles rather than by what it composes to. The fix — derive the create
allowlist from the `create` view, adding `project_id` — is a behaviour change and
is left to the owner, like every other finding in this series.

## Two things that do not hold

### `derive_working_version` defaults `actor_kind` to `"human"`

The one entry point in this module where a future direct caller passes the check
by omission. Named rather than filed as a defect: the route is correct today and
the effect is a draft.

### The actor is required and discarded

All four routes declare `_actor: str = Depends(require_actor)`, which resolves to
`require_agency_actor` — read `X-Pantheon-Actor`, refuse the request with 422 if
it is missing or blank, return it stripped.

None of the four uses the value. The parameter is named `_actor` and never read.
`agency_information_cards` has no actor column — no `updated_by`, no `acted_by`.

So the header is enforced as though it mattered and stored nowhere. This is the
converse of the finding in the classification cluster, and the pair is worth
stating together:

```text
agency_classification   X-Pantheon-Human-Actor   asserted, and persisted as updated_by
agency_information      X-Pantheon-Actor         asserted, required, and discarded
```

Both dependencies are named `require_..._actor`. In one the record is a claim; in
the other there is no record.

## Why `act_working_information` is the one gate requirement

It supersedes the currently acted version of a governed Information series and
installs a new one, in a single transaction. The acted row is what `card_scope`
and `hermes_scoped_context` read, so this is the module's professional act, not
a working edit.

The module states that gravity itself — "only a human may act an Information
version" — and enforces it by comparing a string its caller passed. The route
passes it correctly today. Two things make it a gate requirement regardless: the
effect is a change to canonical agency state, and nothing records who performed
it. `acted_at` is written; the acting party is not.

## What this batch did not change

No behaviour. Four verdicts with their reasoning, and two ceilings moved
deliberately: unreviewed 44 → 40, required-gate 6 → 7. The findings are recorded,
not fixed — adding an actor column to a governed table is a schema decision and
the owner's to take.
