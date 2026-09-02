# Routing acting an Information version through the chokepoint

Date: 2026-09-02

Status: implemented — `act_working_information` now routes through
`enforce_consequential`. Fifth and last of the five entries the
consequential-mutation inventory recorded as `gate_required_not_wired`;
the pending ceiling moves 1 → 0.
Boundary profile: bounded_implementation_change.

## Change

- Added: `agency_information.AgencyInformationGateRefused`,
  `agency_information.AgencyInformationGatePolicyUnavailable`,
  `agency_information._digest`; `human_decision_ref` on
  `InformationActBody`; `tests/test_agency_information_act_gate.py`.
- Updated: `act_working_information` gained `actor: str` (required —
  see Why), `policy_client`, `decision_payload`, `required_ceiling`
  parameters; `install_agency_data_routes` gained a `require_policy_client`
  parameter and the `act_information` route now depends on it, forwarding
  the real actor identity it already resolved but previously discarded;
  `cockpit_shell.py`'s call to `install_agency_data_routes` passes its
  existing `require_policy_client`; the inventory's entry moves off
  `gate_required_not_wired`; the pending ceiling 1 → 0; five direct test
  call sites (`test_agency_information.py` ×3, `test_ifja_field_journeys.py`,
  `test_hermes_scoped_context.py`) now pass an explicit `actor`.
- Removed: nothing.

## Why

Unlike the other four entries in this batch, this one was not missing a
guard — `act_working_information` already compared `actor_kind` before
allowing the act, already locked the row, already checked the version was
still working, already compared `expected_revision`. What it lacked was
narrower and harder to see locally: nothing recorded *who* acted the
version. `agency_information_cards` has no actor column. The route
(`act_information` in `agency_data_api.py`) already resolved a real
identity from the `X-Pantheon-Actor` header, through `require_agency_actor`
— and discarded it as `_actor`, an unused parameter, because the function
underneath had nowhere to put it.

The inventory's own finding named both halves of this precisely: "the
effect is a change to canonical agency state, and nothing records who
performed it." The first half is why the effect qualifies for the
chokepoint at all; the second half is specifically what the chokepoint's
decision record now fixes — not by adding a database column, but by
making the acting identity part of the decision that has to exist before
the write can proceed.

## What the gate binds to, and what it still does not verify

Scope is the parent Project, read off the working row
(`working["project_id"]`). The object reference is
`agency_information:{information_id}`. The digest covers the working
row's content fields — everything except `status`, `acted_at`,
`revision` and `updated_at`, which are exactly the fields this act
changes — so a decision taken over one draft cannot be replayed against
a different draft under the same `information_id`/`expected_revision`,
and the same content cannot be acted twice under two different decisions
without each being independently bound to it.

This does not verify the content itself is fit to become the acted
version of the series — no more than `store_reviewed_dossier`'s digest
verifies its `review_ref` names a review that happened. It closes a
narrower, specific gap: that a decision to act *this* version cannot be
silently stretched to cover a different one.

## Where the enforcement actually lives

Same fail-closed composition as the rest of this series:
`act_working_information` accepts an optional `policy_client` and only
gates when one is supplied; `agency_data_api.install_agency_data_routes`
now takes `require_policy_client` as a parameter rather than resolving
its own, because `cockpit_shell.py` already owns and tests that
resolution (`MVP_POLICY_API_URL`, `MVP_POLICY_API_KEY`,
`MVP_POLICY_ENFORCEMENT`) for every other route it composes — this is
the one entry point in this batch reached only through
`cockpit_shell.create_cockpit_app`, never through the narrower
`cockpit_api.create_app` on its own, so there was no reason to duplicate
that resolution the way `cockpit_api.py` had to for the Knowledge routes
in the prior PR.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: acting an Information version now fails closed on the
only production route when no decision point is configured. The five
existing direct test callers, none of which pass a `policy_client`, are
unaffected beyond the now-required `actor` argument.
Authority impact: this is the point. Superseding the canonical acted
Information for a series — the row `card_scope` and
`hermes_scoped_context` read — now routes through the governance check,
bound to the exact content being promoted, with the acting identity
recorded in the decision rather than nowhere.
Schema/test/CI impact: no schema change — `agency_information_cards`
still has no actor column, deliberately; the acting identity is
governance-record state, not application state. One test module added.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests   1303 passed, 386 skipped
tests/                  595 passed
```

The six new tests in `test_agency_information_act_gate.py` skip locally
(no reachable PostgreSQL in this execution environment, same as every
DB-dependent test in this batch); they were read by hand against the
gate placement rather than left unverified. GitHub CI runs the pgvector
integration lane and is the authoritative execution check.

## Local distinctions

```text
guard on what the module can check locally != guard on who the caller is
acted_at recorded                          != who acted it recorded
digest binds content to an identifier      != digest verifies the content is right
```
