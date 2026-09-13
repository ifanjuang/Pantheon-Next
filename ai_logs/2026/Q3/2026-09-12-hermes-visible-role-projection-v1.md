# AI log — Hermes visible Role projection v1

Date: 2026-09-12
Status: implementation intervention — presentation foundation only.

## Observation

Live `/v1/runs` tests showed that the installed activity skill influenced final
wording but did not reliably emit canonical Role labels. The
`pantheon-governed` profile exposed no meaningful interim events before the
final response. Its base `SOUL.md` also discouraged process narration without a
specific exception for bounded observable milestones.

## Change

- versioned `pantheon-activity-projection` under `templates/hermes/skills/`;
- added a managed `pantheon-governed` SOUL supplement requiring compact,
  role-labelled observable milestones for non-trivial governed work;
- added an idempotent Ubuntu configurator with backup and optional restart;
- added structural tests;
- reconciled `ROLE_DIALOGUE_TRACE.md` with canonical Roles and the partial v1
  implementation state.

## Boundary

This first slice formats output already produced by Hermes. It does not add a
`role.stage` SSE event, persist Role Signals, implement the Cockpit dialogue
view, expose private chain-of-thought, create agents or grant authority.

```text
ordered streamed labels != durable event stream
visible Role != autonomous agent
projection != persistence
runtime output != Evidence
```

## Live acceptance

The updated template and SOUL supplement were installed into the external
`pantheon-governed` profile with pre-change copies retained beside the profile.
Hermes Agent `0.21.1` was restarted and returned healthy.

Observed runs through `/p/pantheon-governed/v1/runs`:

- `run_dde8400914ca4480b41b3bc8502725cf`: a concise technical question stayed
  quiet and returned no unnecessary Role sequence;
- `run_3c697d95271840dc84e78efd18916a1a`: a non-trivial architecture comparison
  automatically exposed `Athena · Plan / structuration`, an observed
  `Hermes · Milestone initial`, and `Zeus · Statut` without the caller naming
  the skill or prescribing those labels.

The `/events` stream emitted a keepalive but no separate material Role milestone
before completion. V1 therefore qualifies ordered role-labelled response
projection only. Structured progressive runtime events and Cockpit persistence
remain unimplemented.

Some numerical thresholds and duration estimates in the model return were not
source-backed. They remain unverified candidate content and are not acceptance
evidence for the architectural recommendation. The acceptance concerns only the
visible projection contract.
