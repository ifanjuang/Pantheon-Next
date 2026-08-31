# The agency_classification cluster, and two attribution mechanisms

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Objective

Review the five unreviewed mutation points in `agency_classification.py`. Chosen
by module rather than by entry, so the production callers are read once for five
verdicts instead of five times.

## The five

```text
create_category               none
update_category               none
archive_category              none
assign_category               none
retire_category_assignment    none
```

Classification is not a professional act: it approves nothing, admits no Evidence
and reaches nothing external. Hermes is refused at two independent layers — the
route rejects the Hermes bearer key outright and returns 503 if the editor and
Hermes keys are configured identically, and `_validate_actor` accepts only
`human` or `system`. `actor_kind` is a literal at every call site, so a request
body cannot set it. Update, archive and retirement carry `expected_revision`
optimistic concurrency and refuse an already-terminal row.

## What tracing composition surfaced

The commitment after the previous batch was to read what a guard composes to
rather than what it is named. Applied here it produced a finding larger than the
five entries.

```text
principal.principal_ref     35 sites   an authenticated principal context
X-Pantheon-Human-Actor      19 route dependencies across 8 modules
```

`require_human_actor` is named like an authentication check. It composes to:
read the `X-Pantheon-Human-Actor` header, require it non-empty. Nothing ties the
named human to a governed principal, or to the party presenting the bearer key.
And the value is persisted into governed rows — `archive_category` writes
`updated_by = %s` from it.

So on those routes **the authorization is verified and the attribution is
asserted**. Anyone holding the editor key can name any human as the author of a
governed write.

This is the third instance in this session of the same failure shape, and the one
with the widest reach:

```text
review_ref                            looked like a reference to a review
"refuses to revoke access.manage"     looked like protection of the administrator
require_human_actor                   looks like authentication
```

## Why this is not a gate requirement

The chokepoint decides whether an effect may happen. It would not repair
attribution. The remedy is binding the actor to an authenticated identity — the
`human_access` principal context already exists and is used at 35 sites — which
is a behavioural change and not a review record's to make.

Recorded as a module-level finding rather than folded into five guard regimes,
for the same reason the human-access lockout was: a defect that spans routes is
not a property of any one entry point.

## Boundary

Protected paths touched: `implementation/tests/` — one inventory file.
Runtime impact: none.
Authority impact: none. All five verdicts are proposals for arbitration.
Schema/test/CI impact: unreviewed ceiling 53 → 48.
External action: none.
Memory behavior: none.

## Local distinctions

```text
authorization verified != attribution verified
named guard            != composed guard
classification         != professional effect
module finding         != entry guard regime
```

## Next decision

Whether the header-asserted actor should be replaced by the authenticated
principal context on those 19 route dependencies. Until it is, `updated_by` on
those tables records a claim rather than an identity.
