# Hermes execution basis

Date: 2026-08-04

Status: implementation note — non-authoritative.

## Verified overlap

Handoff submission, execution-envelope projection, launch preparation and running-context access use the same four immutable dimensions:

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

`hermes_execution.get_execution_envelope` requires the persisted Handoff and admission bases to match before applying the separate `ready_for_external_runtime` gate. It continues to return `runtime_instruction=None` and `dispatch_requested=False`.

`hermes_launch_context` reconstructs the admission and Handoff bases and requires their equality before consuming the already-admitted launch window.

`hermes_scoped_context` reconstructs the same admission and Handoff bases before separately requiring the exact run, `running` state, read-only effect and matching run references.

## Authority retained elsewhere

The basis does not decide:

- whether the Work Issue is open or assigned to Hermes;
- whether a human admitted execution;
- whether the admission is current, expired, stale or revoked;
- whether an execution envelope is consumable;
- whether a launch reservation may be created;
- whether an external runtime starts or remains running;
- whether an entity belongs to the admitted Context Pack;
- whether a result is accepted or Evidence is admitted.

## Non-equivalences

```text
basis structurally valid != Work Issue valid
basis equality != execution admission
execution admission != consumable envelope
execution envelope != dispatch
execution admission != launch reservation
launch reservation != runtime dispatch
basis equality != running run
running run != accepted result
runtime success != Evidence
```

This tranche centralizes an existing immutable identity. It does not add a governed concept, scheduler, queue, provider router, retry engine or approval mechanism.

## Follow-up

The human admission transaction still copies the same immutable dimensions from the Handoff while separately validating the Work Issue and its state. It may construct the basis explicitly in a separate PR if the existing admission-specific error messages and digest remain unchanged.
