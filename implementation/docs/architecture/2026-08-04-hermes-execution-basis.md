# Hermes execution basis

Date: 2026-08-04

Status: implementation note — non-authoritative.

## Verified overlap

Handoff submission, launch preparation and running-context access use the same four immutable dimensions:

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

`hermes_scoped_context` reconstructs the same admission and Handoff bases before separately requiring the exact run, `running` state, read-only effect and matching run references.

## Authority retained elsewhere

The basis does not decide:

- whether the Work Issue is open or assigned to Hermes;
- whether a human admitted execution;
- whether the admission is current, expired, stale or revoked;
- whether a launch reservation may be created;
- whether an external runtime starts or remains running;
- whether an entity belongs to the admitted Context Pack;
- whether a result is accepted or Evidence is admitted.

## Non-equivalences

```text
basis structurally valid != Work Issue valid
basis equality != execution admission
execution admission != launch reservation
launch reservation != runtime dispatch
basis equality != running run
running run != accepted result
runtime success != Evidence
```

This tranche centralizes an existing immutable identity. It does not add a governed concept, scheduler, queue, provider router, retry engine or approval mechanism.

## Follow-up

The execution envelope also compares the immutable Handoff and admission dimensions. It may consume this value object in a separate PR after preserving its envelope-specific conflict messages and projection contract.
