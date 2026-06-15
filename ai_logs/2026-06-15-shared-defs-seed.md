# AI Log — Shared definitions seed

Date: 2026-06-15

## Context

After PR #126 merged the D3 module manifest and claim-status reconciliation, a follow-up shared vocabulary factoring was requested.

A previous attempt to wire `$ref` consumers directly was abandoned because local reference resolver test changes were blocked by the connector and would risk a red CI.

## Change made

Added a deliberately narrow seed:

- `schemas/shared_defs.schema.yaml`
- `schemas/README.md` index entry and D3 note

The seed defines only `scope_type`.

No existing schema consumes `shared_defs.schema.yaml` in this pass.

## Boundary

Implemented: schema vocabulary seed only.

Not implemented:

- `$ref` consumers;
- local schema resolver tests;
- runtime;
- database;
- queue;
- scheduler;
- approval engine;
- memory engine;
- OpenWebUI integration;
- Hermes skill;
- external action.

## Decision status

Decision Zeus: Accepted as a safe seed, pending PR review.

Repository state: documented / schema seed implemented, not wired.
