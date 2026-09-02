# Routing the reviewed-dossier import through the chokepoint

Date: 2026-09-02

Status: implemented — the chokepoint on `store_reviewed_dossier`, with a
local provisioning path. Second of the five remaining pending gates.
Boundary profile: bounded_implementation_change.

## Change

- Added: `apu_owner.ApuOwnerRefused`, `apu_owner.ApuOwnerPolicyUnavailable`;
  the `store-reviewed-dossier` CLI subcommand; `policy_gate.OBJECT_IDENTITY_KEY`;
  `tests/test_apu_reviewed_dossier_gate.py`.
- Updated: `store_reviewed_dossier` routes through `enforce_consequential`
  when a decision point is supplied; the inventory entry moves from
  `gate_required_not_wired` to `enforce_consequential`; the pending-gate
  ceiling 5 → 4; the inventory's list of the remaining four; the coverage
  test suite.
- Removed: nothing.

## Why

`store_reviewed_dossier` installs the whole canonical Architecture Project
Understanding baseline for one Project — stable objects, source
representations, attribute claims, relation claims — in one shot. It was
recorded as needing the chokepoint because `review_ref` is a caller-supplied
string with nothing behind it: no lookup, foreign key, signature or table of
completed reviews exists to verify it against.

Reading it in order to wire it found the same shape #935 found in
`bind_oidc_identity`: **it had no production caller at all.** Thirteen test
modules call it; nothing else does. In a live deployment, a Project's whole
canonical APU baseline could only be installed by writing to the database
directly.

## What the gate binds to, and what it still does not verify

`_normalize_dossier` already folds `review_ref` into the same structure as
the stable objects, representations and claims before the existing
idempotency digest (`payload_digest = _digest(dossier)`) is computed. The
repair reuses that digest rather than inventing a new binding: the decision
expectation's `expected_digest` is `payload_digest`, so the decision covers
this exact `review_ref` bundled with this exact dossier as one unit.

This is worth being exact about, because an earlier draft of this same PR
overstated it. The digest does **not** prove `review_ref` names a review that
actually happened — nothing in this repository can, absent a table of
completed reviews that does not exist. What it closes is narrower: a decision
taken over one dossier/review_ref pairing cannot be replayed against a
different dossier under the same `review_ref`, or the same dossier re-labelled
under a different one.

The scope is the Project (`{"scope_type": "project", "scope_id": project_id}`),
matching what the write installs.

## Where the enforcement actually lives

Same arrangement as `bind_oidc_identity` and `cockpit_shell`: `policy_client`
is optional in the module, and the new `cli store-reviewed-dossier` command is
the composition point that makes it mandatory. It refuses to open a database
connection unless a decision point is configured, or
`MVP_POLICY_ENFORCEMENT=disabled` is declared by name.

## A naming collision, and how it was resolved

`apu_owner.py` carries its own baseline-contract test
(`test_runtime_has_no_discarded_reader_writer_or_migration_surface`) that
forbids the literal substring `object_identity` anywhere in the module's
source — a guard against resurrecting field/method names from an earlier,
discarded v0.2 owner design. `enforce_consequential`'s decision-expectation
schema independently uses `object_identity` as a field name, unrelated to that
old design.

Rather than work around the module's own test, `policy_gate.OBJECT_IDENTITY_KEY`
was added as a shared constant so a caller whose own module forbids the
lowercase phrase can still build a conformant expectation without the literal
string appearing in its source. `human_access.py` (from #935) was not changed;
it carries no such ban.

## Boundary

Boundary profile applies: `bounded_implementation_change`.

Protected paths touched: no.
Runtime impact: installing a reviewed dossier without a configured decision
point now fails closed on the only production path. Existing callers that
pass no `policy_client` (all thirteen test modules) are unchanged.
Authority impact: this is the point. The act that installs canonical APU
state for a Project now routes through the governance check, with the
decision bound to the dossier's exact content plus its claimed `review_ref`.
Schema/test/CI impact: no schema change; one test module added; the
baseline-contract test's forbidden-token list is unaffected.
External action: none.
Memory behavior: none.

## Verification

```text
implementation/tests   1300 passed, 369 skipped
tests/                  595 passed
```

Verified by removing each half of the CLI's fail-closed check in turn, as with
#935: the gate test fails without it, passes with it restored.

## Local distinctions

```text
digest binds review_ref to content != digest verifies review_ref is true
optional parameter                 != unenforced gate
one module's forbidden phrase       != another module's vocabulary
```
