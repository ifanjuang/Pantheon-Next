# 2026-08-31 — chokepoint wiring and the three open pin decisions

## Objective

Take the two things the previous slices deliberately stopped short of: wire the Pantheon chokepoint into the application, and decide the three recorded pin lags.

## Exact repository state

```text
branch base = f16f6d60b6a1b80d57eae80b9dad400a9a0abed8
main        = 07b28ce4f56469f2824d0e250f3d100c78090fff
```

PR #877 was green on all nine checks before this slice.

---

## Part 1 — chokepoint wiring

### Order followed

The previous log stated the order that matters, and it was followed rather than shortened:

1. assembly test — `implementation/tests/test_policy_client_assembly.py`;
2. wiring — `cockpit_shell.create_cockpit_app`;
3. inventory and `WHAT_RUNS.md` updated to the new state.

Wiring before step 1 would have left the same silent-regression hole that produced the original state: `test_cockpit_shell.py` and `test_cockpit_composed.py` contained no occurrence of `policy`, so the factory could be changed in either direction with nothing reacting.

### Posture chosen

Enforcement defaults to `required`.

```text
MVP_POLICY_ENFORCEMENT = required | disabled   (default: required)
MVP_POLICY_API_URL     + MVP_POLICY_API_KEY    (both required to build a client)
```

`require_policy_client()` follows the file's existing dependency shape — `503` when unconfigured, exactly as `require_update_signing_secret` already does. The refusal is scoped to the consequential route: read-only projections keep serving with no decision point. A deployment that runs without a PDP must say `MVP_POLICY_ENFORCEMENT=disabled` by name.

```text
unconfigured != permitted
disabled by default != disabled by decision
```

A partial environment (URL without key) builds no client and refuses, rather than half-configuring one.

### Blast radius

Only two test files exercised the apply route. Both now state their posture rather than inheriting it:

- `test_update_apply_passes_only_exact_confirmed_effect` was given a real `StandInPolicyClient` and now asserts it reaches `apply_knowledge_update`. It turned from a test to appease into the test that proves the wiring: `observed["policy_client"]` did not exist before this branch.
- `test_expired_confirmation_maps_to_gone` covers error translation, not admission, and names the bypass.

### Inventory revisit point behaved as designed

`test_chokepoint_coverage_is_reported_honestly` was written to refuse a coverage claim while `HttpPolicyClient` had no instantiation. Wiring the client made the claim permissible, and the inventory now records `enforce_consequential` for `apply_knowledge_update`.

Its docstrings described the pre-wiring state and were rewritten rather than left to lie. The check was also strengthened to verify a claim in both directions: refused while no client can exist, and required to be backed by a real `enforce_consequential(` call plus a `required`-by-default application boundary.

Seven of eight entry points still record `gate: "none"`. That is the current honest state, not a defect list.

---

## Part 2 — the three pin decisions

### Validation mechanism

All six LiveSync labs (S1..S6) and the Hindsight labs (O1, O2, Q5) carry `implementation/qualification/external-pins.json` in their path filters, so moving the pins re-runs those qualifications against the new upstream on this change. Their result is the qualification; operational acceptance remains a separate human decision.

`implementation-hindsight-obsidian-hermes-o3-lab.yml` does **not** trigger on the registry. It is listed in `HISTORICAL_ACTIVE_PATHS` in the pins test. Noted, not changed here.

### Decisions

```text
self-hosted-livesync      1.0.18     -> 1.0.21   ref f5f7aab11f03f62c6946d2fa296c50bb5df5b2a4
self-hosted-livesync-cli  1.0.18-cli -> 1.0.21-cli   (derived)
hindsight                 0.9.1      -> 0.9.2
couchdb                   3.5.0      -> 3.5.2
```

The LiveSync commit was verified from two independent sources — the release page and the tag's commit feed — because the GitHub API is unreachable from this session and a wrong ref in the registry would be a serious error. The labs assert `git rev-parse HEAD` against it, so a wrong value fails loudly rather than silently.

The reason to move LiveSync was never the version number: 1.0.20 corrects settings-page behaviour under Obsidian 1.13, the release line pinned beside it as `obsidian-desktop`, so the previous pin qualified a combination whose upstream documented an interaction defect.

CouchDB moved with it because it backs that topology.

Moving `hindsight` closes the version lag **only**. It does not settle which lexical lane is authoritative on which corpus: 0.9.2's BM25 change overlaps the hand-written lexical fallback added to `implementation/mvp_vertical/retrieval.py` in #874, and Hindsight is not wired into that retrieval path. That remains a separate open design question, recorded as a note on the observation rather than quietly closed.

### A deployment target was already ahead of its qualification

`test_ubuntu_node_bootstrap_contract.py` caught a second consumer of the LiveSync ref: `deployment/ubuntu/release.env`. Aligning it surfaced something the bump did not cause.

The release lock already carried a **newer Hindsight image than the registry pinned**. The existing guard asserted the CouchDB image and the LiveSync ref against the registry, but neither the Hindsight image nor the LiveSync CLI image — so the deployment target had drifted ahead of the qualification meant to justify it, unobserved.

That is the same class of gap as the chokepoint, in the other direction, and the guard was extended to cover both. Verified to bite by moving the release image ahead of the pin and watching the test fail.

```text
deployment target != qualified artifact
```

The extended guard reads every version from the registry and restates none, so it cannot itself drift.

---

## Guard that fired twice during this work

`test_active_qualification_code_does_not_duplicate_current_pin_literals` rejected this work twice, and was right both times:

- in the previous slice, for a pin version quoted in the freshness tool's docstring;
- here, for a version quoted in the comment explaining the deployment drift — a version that had just *become* a current pin through the bump.

Both were reworded to quote nothing. A check whose own text restates the values it audits is the first thing to go stale.

## Validation

```text
tests/                  554 passed
mcp-server/tests        229 passed
implementation/tests   1251 passed, 352 skipped (no local PostgreSQL)
.github/scripts         23/23 OK
pin freshness           exit 0 — no pin actionable
```

## Boundary

```text
gate wired != gate observed end to end
configuration present != decision point reached
pin moved != qualification passed
lab green != operational acceptance
deployment target != qualified artifact
one entry point covered != eight
```

## Next admissible step

The S1..S6 and O1/O2/Q5 results on this change are the first real signal on the moved pins. A red lab is the answer, not a defect to route around.

Seven mutation entry points still record `gate: "none"`. Each is a separate review: the inventory makes them enumerable, it does not make them equivalent. `admit_handoff` and `apply_authorized_write_command` carry the strongest local chains and are the natural next candidates.

A real policy decision point observed end to end remains unproven. Configuration present is not a decision point reached.

---

## Addendum — the decision point was observed, and it did not need a deployment

The section above listed "a real policy decision point observed end to end" as unproven, and the plan sized it at two days, mostly deployment. That was wrong: it took twenty minutes and no deployment at all.

`pantheon-policy-api` was started as a local process against this checkout, and the exact production path — `HttpPolicyClient` into `enforce_consequential` — was driven against it.

```text
/livez   alive
/readyz  ready, repository accessible, "ready != safe; healthy != authorized"
protected route without a key  ->  401
```

Both directions were recorded, because only the pair is informative:

```text
without gate signals  ->  refused, blocked_pending_task_contract
                          missing: reviewed_task_contract_ref, evidence_pack_candidate_ref
with gate signals     ->  allowed, eligible_with_gate_signals_unverified
```

The refusal proves the gate is not permissive by default. The allow proves the round-trip completes. Neither performed any effect.

### The allowing disposition is bounded, and says so

`eligible_with_gate_signals_unverified`, with `gate_signal_validation_performed: false`. The decision point allowed the effect *and* reported that the gate references it was handed were never validated — they are caller-asserted strings. That is this repository's own distinction, enforced by the service rather than only written down:

```text
provided gate reference != validated decision
eligible != approved
gate answered != effect performed
```

### The request contract, recorded because it cost several attempts

None of this is obvious from the client side, and each was established by a refusal rather than by reading:

- `request.scope` is an object with `scope_type` and `scope_id`. A scope string is silently treated as absent and yields `blocked_pending_scope`.
- Gate references live in `gate_signals`, a sibling of `request` — not inside it. Placing them in `request` changes nothing and the same refusal repeats.
- `decision.expires_at` is an RFC 3339 string. An epoch integer is rejected with "not a valid timestamp".

One false alarm is worth recording too: `/policy/decisions:validate` appeared missing from the service because it is registered through a table and `add_api_route` rather than an `@app.post` decorator. It exists. A grep for decorators is not an inventory of routes.

### What this changes

`WHAT_RUNS.md` no longer lists the round-trip as unproven. `implementation/tools/observe_policy_round_trip.py` makes the observation repeatable rather than anecdotal: it exercises both directions, prints the verdicts, and exits non-zero only when the decision point fails to answer — a refusal is a successful observation.

What remains unproven is different and smaller: a decision point observed in a real deployment rather than a local process, and the seven other mutation entry points reviewed one by one.

```text
local process != deployment
observation repeatable != observation adopted
```
