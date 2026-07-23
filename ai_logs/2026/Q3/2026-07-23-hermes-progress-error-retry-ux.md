# 2026-07-23 — Hermes progress, error, diagnosis and bounded retry UX

Status: validation-only intervention trace.

## Request

The maintainer requested that Cockpit cards show a percentage instead of only `en cours` when Hermes exposes measurable progress, display an explicit error when processing fails, and clarify whether Hermes may automatically investigate and retry failures.

## Decision recorded

A transverse candidate specification was added:

- `docs/governance/HERMES_PROGRESS_ERROR_RETRY_UX.md`.

The candidate decision is:

```text
Hermes-reported measurable progress
-> display percentage + real unit

no measurable progress
-> display current step or indeterminate state

failure
-> display explicit error + partial successes + diagnosis posture + retry posture
```

Hermes may automatically diagnose errors and retry only under a bounded, pre-authorized policy.

Typical automatic retries are limited to transient, idempotent or safely resumable failures such as timeouts, temporary network failures, rate limits, interrupted transfers or resumable indexing.

Hermes may not automatically:

- switch to an unapproved binding or model;
- move from local to remote execution;
- send data to a new provider;
- install or update a dependency;
- change system configuration;
- expand scope;
- weaken validation;
- alter validated content;
- mark a recovered runtime output professionally valid.

## Non-equivalence rules

```text
error detected != root cause confirmed
root cause proposed != remediation authorized
retry attempted != problem corrected
fallback available != fallback authorized
runtime recovered != output validated
```

## Repository effect

Documentation only.

No Cockpit component, Hermes Skill, polling service, callback receiver, retry worker, queue, scheduler, provider fallback, configuration mutation, runtime installation or automatic approval is implemented.
