# Policy chokepoint wiring convergence — 2026-08-31

Status: validation / intervention trace — not doctrine.

## Baseline

Current `main` after #877:

```text
aaf9b95261f71492d7d7e7787ce50d9278f6d368
```

#877 established the consequential-mutation inventory, MCP read-only annotations and external-pin freshness observation. It did not wire a policy client into an application path.

## Objective

Port only the chokepoint-wiring decision previously mixed into #881, without moving external pins or importing the LiveSync retry/lab changes.

## Observed state

- `policy_gate.enforce_consequential` is implemented and exercised by module tests.
- `HttpPolicyClient` exists, but before this change the Cockpit application factory did not assemble it.
- the Knowledge UPDATE apply route could therefore reach its owner-specific local guards without a configured Pantheon policy decision point.
- #877's widened inventory currently enumerates 72 mutation entry points; 64 remain explicitly unreviewed. This change claims central-gate coverage for one reviewed entry point only.
- #881 recorded a local end-to-end observation of the exact `HttpPolicyClient -> enforce_consequential -> pantheon-policy-api` path in both refusal and allow directions. That observation is retained as an observation, not deployment truth.

## Change

- assemble `HttpPolicyClient` from `MVP_POLICY_API_URL` + `MVP_POLICY_API_KEY` in the Cockpit factory;
- default `MVP_POLICY_ENFORCEMENT` to `required`;
- refuse the Knowledge UPDATE apply route with `503` when the decision point is unconfigured;
- permit an explicit `disabled` posture only when named by configuration;
- pass the resolved policy client into `knowledge_update.apply_knowledge_update`;
- update the mutation inventory from `optional` to `enforce_consequential` for that exact path;
- retain a repeatable read-only round-trip observer;
- update `WHAT_RUNS.md` to say one entry point is wired and the remaining mutation surface is not yet centrally covered.

## Deliberate non-change

No external qualification pin, deployment lock, LiveSync workflow, retry helper, Evidence admission rule, approval rule, source identity, persistence owner or Hermes runtime is changed.

```text
local guard != authorization gate
gate configured != decision validated
gate answered != effect performed
one path wired != mutation surface closed
local observation != deployed enforcement
```

## Verification

This touches protected implementation/tests and must complete repository PR CI before merge. The earlier mixed #881 branch is evidence for the behavior but is not reused as an authority source; this branch is reconstructed from current `main`.
