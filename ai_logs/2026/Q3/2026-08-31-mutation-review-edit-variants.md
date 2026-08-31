# Mutation review: the A/B edit variant review

Date: 2026-08-31
Zone: `implementation/`
Scope: the four unreviewed mutation entry points in
`implementation/mvp_vertical/knowledge_edit_variants.py`, plus a rewritten
rationale for one entry already recorded.

## Verdicts

| entry point | regime |
| --- | --- |
| `create_variant_request` | `none` |
| `project_execution_result_variant` | `none` |
| `select_variant` | `none` |
| `reject_request` | `none` |
| `apply_selected_variant` | `none` — reasoning rewritten |

No ceiling for required gates moves. That is deliberate and explained below.

## The module already closes two of the defects recorded against `knowledge.py`

This is the useful finding, and it runs the opposite way to the rest of the
review.

`create_variant_request` writes into the same `knowledge_edit_requests` table as
`knowledge.create_edit_request`. Its INSERT sets `replacement_markdown` to a
literal NULL and the status to a literal `'queued_for_hermes'`. The caller
cannot ask for anything else. The shortcut recorded against the other creation
path — supply the replacement, land on `proposed`, skip Hermes — is structurally
impossible here.

`project_execution_result_variant` refuses any request whose status is outside
`{queued_for_hermes, proposed}`. That is precisely the status guard
`knowledge.complete_edit_request` lacks, so a rejected request cannot receive a
projected variant.

Both defects have a fix already written in this repository, one module away.

## The rejection is still reversible, and the selection survives it

Traced end to end:

```text
create_variant_request        status queued_for_hermes
project_..._variant           status proposed
select_variant                selected_variant_id set, status still proposed
reject_request                status rejected, selection NOT cleared
complete_edit_request         status proposed  (version still matches base)
apply_selected_variant        proposed + intact selection -> applies
```

The applied text is the variant the human selected, not the later proposal, so
the effect is not a substitution — it is the application of an edit that was
refused.

`reject_request` is otherwise sound: status-guarded, locked, reasoned,
idempotent, and it writes the refusal as an event. Its verdict is `none` and the
reversal is recorded against it anyway, so that the reversal is findable from the
function that is meant to be terminal.

## Why `apply_selected_variant` is not a second gate requirement

Its recorded reasoning said the request had already selected the variant. The
chain above falsifies that, exactly as the same premise was falsified for
`apply_edit_request`.

But `apply_selected_variant` delegates the Knowledge mutation to
`knowledge.apply_edit_request`, which is already recorded as
`gate_required_not_wired`. Wiring the chokepoint there covers this path too.
Recording it twice would overstate how many places have to be wired, which is the
opposite failure to the one this review keeps finding and no better.

One caveat is recorded rather than waved past: this function commits its own
`replacement_markdown` write in a separate transaction before delegating, so that
write would survive a refusal downstream.

## Attribution, third form

`select_variant`, `reject_request` and `apply_selected_variant` all record an
actor, and the record is real — `selected_by`, an `actor` column on
`knowledge_edit_review_events`, an idempotency key, an event per decision. Both
halves of it are unverified:

- `actor` is the `X-Pantheon-Human-Actor` header value, non-empty and nothing
  more;
- `actor_kind` is a literal written at the call site. There are four
  `_insert_event` sites — one `"system"` for the projection, three `"human"` for
  selection, rejection and application.

Amended on review. That was first recorded as six event writes, five `"human"`
and one `"system"`, which counted `actor_kind=` matches in the file rather than
reading what each call was to: two of the six are arguments to
`knowledge.apply_edit_request`, not event writes. Six literals, four of them in
the audit log. The finding is unchanged — every one is a constant — but the
count was asserted from a grep pattern instead of from the call sites, which is
the same move this review keeps recording against the code.

So the column records the kind the code path intends, never the kind of the
caller observed. Across four modules the same header now has four fates:

```text
agency_classification     asserted, persisted as updated_by
agency_information        asserted, required, then discarded
knowledge                 a body field, persisted verbatim
knowledge_edit_variants   asserted, persisted; the kind is a literal
```

## What this batch did not change

No behaviour. Four verdicts, one rewritten rationale, and one ceiling moved:
unreviewed 40 → 36.
