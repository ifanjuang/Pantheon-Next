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

Both are recorded `none`.

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
