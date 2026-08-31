# The two live human-access mutation points

Date: 2026-08-31

Status: validation-only trace — governance review record, no runtime change.
Boundary profile: validation_only_trace.

## Objective

Review `grant_access` and `revoke_grant`, the two mutation points in
`human_access.py` that production actually reaches. The module's other four were
recorded in the previous batch; these two are what decide who may act.

## What their production callers add

Both are reached only through `human_access_api.py`, and the route contributes
more than the function does:

```text
require_principal                     the caller is an authenticated principal
require_project_access_manager        and already holds project.access.manage
granted_by = principal.principal_ref  taken from the session, not the request body
REMOTE_MANAGEABLE_ACTIONS             project.access.manage cannot be delegated
document grant                        target must already hold project.read
revoke                                project.access.manage cannot be stripped
```

`grant_access` is recorded `none`. `revoke_grant` was too, and that was wrong —
see the amendment below.

## Why not escalated, stated deliberately

The reflex after the `store_reviewed_dossier` correction is to escalate every
authorization-shaped path. That would be the wrong lesson from being wrong.

The distinguishing fact is that the actor here is **verified rather than
asserted**. `granted_by` comes from the authenticated session, and the caller
must already hold `project.access.manage`, checked against the database.
`store_reviewed_dossier` failed on exactly the opposite: a `review_ref` that
nothing verifies. The route also caps escalation by refusing to delegate the
manage right at all, and the codebase names the effect
`technical_project_access_granted` — *technical*, distinguished by its own author
from a professional one.

Cleared on the chain, not on the category.

```text
verified actor != asserted reference
technical access != professional effect
corrected once != escalate everything
```

## The finding is neither of them

`project.access.manage` is required by both routes, excluded from what they may
delegate, and refused for revocation. **No production path creates it.** The only
way it comes to exist is a direct `grant_access` call, which nothing outside the
tests makes.

So the delegation chain is well guarded and its root is established nowhere in
this repository. That is a larger question than either entry's guard regime, and
it is recorded rather than folded into one.

## Boundary

Protected paths touched: `implementation/tests/` — one inventory file.
Runtime impact: none.
Authority impact: none. Both verdicts are proposals for arbitration.
Schema/test/CI impact: ceiling 55 → 53.
External action: none.
Memory behavior: none.

## Next decision

Where the first `project.access.manage` grant is supposed to come from. Until
that is answered, the access surface is either seeded by hand outside any
governed path, or not seeded at all — and the second is what the symbol layer
currently observes.


## Amendment, 2026-08-31 — the revocation guard was narrower than asserted

`revoke_grant` was recorded `none`, with a guard list stating that the route
"refuses to revoke project.access.manage, so the administrator cannot be
stripped", and reasoning that "the one escalation it could enable — stripping the
project administrator — is refused by the route outright."

A review caught that this is false, and it is false in the guard list itself, not
only in the prose.

```text
require_project_access_manager  ->  require_project_read      (project.read)
                                ->  require_access            (project.access.manage)

revoke route refuses            ->  grant["action"] == "project.access.manage"
                                    and nothing else
```

`project.read` is remotely grantable, and the revoke route carries no
`REMOTE_MANAGEABLE_ACTIONS` restriction at all. So one manager can revoke another
manager's paired `project.read` grant. The victim keeps the `project.access.manage`
row and fails every management endpoint, because the read check runs first.

An administrator lockout reachable by an ordinary manager, through a route that
needs no special access, is consequential. Reclassified as
`gate_required_not_wired`; the regime's ceiling moves 2 → 3.

The durable remedy is a code fix — protect a manager's paired read grant, or make
revocation refuse any grant the target needs in order to manage. That is a
behavioural change and not this record's to make.

## What this says about the previous entry, and what it does not

The `grant_access` verdict is unaffected: its guard against escalation is the
route refusing to *delegate* the manage right, which is real and direct. The
error here was the mirror-image guard on revocation, which only looks symmetric.

Twice in two batches a verdict has been corrected by review, and both times the
error was the same shape: a guard asserted from what a check is named rather than
from what it composes to. `review_ref` looked like a reference to a review.
"refuses to revoke project.access.manage" looked like protection of the
administrator. Neither survived reading the next call down.

```text
named guard      != composed guard
refuses directly != refuses indirectly
symmetric-looking != symmetric
```
