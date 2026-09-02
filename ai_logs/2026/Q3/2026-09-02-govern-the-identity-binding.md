# Governing the act that makes an external identity a governed principal

Date: 2026-09-02

Status: implemented — the chokepoint on `bind_oidc_identity`, with a local
provisioning path. Governance reconciliation stated, not assumed.
Boundary profile: bounded_implementation_change.

## Change

- Added: `human_access.binding_digest`; `BindingRefused` and
  `BindingPolicyUnavailable`; the `bind-oidc-identity` CLI subcommand;
  `tests/test_human_identity_binding_gate.py`.
- Updated: `bind_oidc_identity` routes through `enforce_consequential` when a
  decision point is supplied; the inventory entry moves from
  `gate_required_not_wired` to `enforce_consequential`; the coverage-claim test
  now asks the gate closure rather than the module text; the pending ceiling
  6 → 5; the inventory's founding paragraph, which had gone stale.
- Removed: nothing.

## Why

`bind_oidc_identity` writes `human_oidc_bindings`. `resolve_principal_context`
resolves every authenticated request against that table, so the row this
function writes is the root of trust for the whole principal regime — the
eighteen routes behind `require_principal`, `require_access`, and every grant
those checks consult.

It was recorded as needing the chokepoint. Reading it in order to wire it found
what the entry had not said: **it had no production caller at all.** Seven test
modules call it and nothing else does. No route, no CLI command. In a live
deployment the table could only be populated by writing to the database
directly, or the entire principal regime answers `403 PrincipalNotBound` to
everyone.

## The reconciliation, stated rather than assumed

The obvious design is a route requiring an authenticated principal holding a
dedicated grant. The repository has already refused it, in writing, in the
schema.

`033_human_project_access_management.sql`:

```text
project.access.manage is a technical project-scoped administration capability.
It does not encode professional role, approval, Decision, Evidence or IdP
invitation authority. Remote B4 routes deliberately cannot delegate this
action; it remains a locally provisioned bootstrap capability.
```

Two things follow, and neither is this module's opinion:

- the action that would be the natural authorizer explicitly does not carry IdP
  invitation authority;
- the repository already accepts that a capability of this class is provisioned
  locally rather than through a remote route.

The grant table could not express the permission in any case.
`human_resource_grants.project_id` is `NOT NULL REFERENCES agency_projects`, and
the action vocabulary is a CHECK. Every grant is project-scoped. A
project-scoped grant minting a system-wide identity would be an escalation: the
manager of one small project could bind an identity usable everywhere.

So the authority for a binding is not a grant. It is the chokepoint.

## What the gate binds to

`enforce_consequential` runs before the write, with an expectation whose
`expected_digest` is `binding_digest(principal_ref, issuer, subject,
valid_until)`. The decision must cover **this exact binding**, not name it —
the `apu_write_preparation.append_authorization` shape this review recommended
everywhere else, applied to the act that most needs it.

The scope is `{"scope_type": "human_principal", "scope_id": principal_ref}`. A
binding is not project-scoped, and borrowing a project scope to satisfy a
convention would have been a small lie in the one place that cannot afford one.

The request declares `external_effect: False` and `writes_state: True`: a
binding sends nothing outward and writes governed state.

## Where the enforcement actually lives

`policy_client` is an optional parameter here, exactly the shape this inventory
was created to record as unenforced. Optionality in the module is not the
defect; a composition point that never supplies it is.

So the enforcement is at the composition point, on the same arrangement
`cockpit_shell` already uses: the CLI refuses to open a database connection
unless a decision point is configured, or `MVP_POLICY_ENFORCEMENT=disabled` is
declared **by name**. Disabling the gate is an explicit act with a spelling, not
an omission.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: a binding made without a decision point now fails closed on the
only production path. Existing callers that pass no `policy_client` — all of
them tests — are unchanged.
Authority impact: this is the point. The act that admits an external identity
now routes through the governance check, and the decision is bound to the exact
binding. It confers no access by itself: a bound principal still holds no grant.
Schema/test/CI impact: no schema change; one test module added.
External action: none.
Memory behavior: none.

## Two findings about the record itself

**The founding paragraph had gone stale.** The inventory opens by stating that
`policy_client` had no non-test caller and `HttpPolicyClient` was never
instantiated outside tests. That was true on 2026-08-31 and false on 2026-09-01,
when `4d3e99c3` wired the client into `cockpit_shell.create_app` behind a
fail-closed `require_policy_client`. Three passes over the entries missed it,
because every pass was reading entry points and none was reading the premise.
A record rots at its premises as readily as at its rows.

**The coverage claim was checked at module granularity.** It asked whether the
module contained the string `enforce_consequential(` — the same polarity error
`#928` repaired on the pending side, standing on the covered side. A module can
gate one function and leave its neighbour ungated. It now asks `_gate_closure`,
the walk that already existed.

## Local distinctions

```text
identity verified      != identity admitted
authenticated          != authorized
grant project-scoped   != permission system-wide
optional parameter     != unenforced gate
premise of a record    != checked by its tests
module contains a call != this function reaches it
```
