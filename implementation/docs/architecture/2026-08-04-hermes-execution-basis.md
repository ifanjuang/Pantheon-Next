# Hermes execution basis

Date: 2026-08-04

Status: implementation note — non-authoritative.

## Verified overlap

Handoff submission and launch preparation use the same four immutable dimensions:

```text
requested_effect
task_contract_ref
context_pack_ref
preview_digest
```

They are represented internally by `HermesExecutionBasis`.

## Placement

The value object is dependency-free. It contains no PostgreSQL, FastAPI, Cockpit, adapter or runtime behavior.

`hermes_handoff_store` constructs the basis before persisting the immutable Handoff and creating its Work Issue.

`hermes_launch_context` reconstructs the admission and Handoff bases and requires their equality before consuming the already-admitted launch window.

## Authority retained elsewhere

The basis does not decide:

- whether the Work Issue is open or assigned to Hermes;
- whether a human admitted execution;
- whether the admission is current, expired, stale or revoked;
- whether a launch reservation may be created;
- whether an external runtime starts;
- whether a result is accepted or Evidence is admitted.

## Non-equivalences

```text
basis structurally valid != Work Issue valid
basis equality != execution admission
execution admission != launch reservation
launch reservation != runtime dispatch
runtime start != accepted result
runtime success != Evidence
```

This tranche centralizes an existing immutable identity. It does not add a governed concept, scheduler, queue, provider router, retry engine or approval mechanism.

## Follow-up

The running-context reader also verifies the same admission/Handoff dimensions together with the exact runtime run. It may consume this value object in a separate PR after its run-specific error and state contracts are preserved explicitly.
