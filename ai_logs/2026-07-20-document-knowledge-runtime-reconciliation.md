# Reconcile the external Document to Knowledge runtime

Date: 2026-07-20

Status: validation-only trace — external candidate observed / not adopted.
Boundary profile: validation_only_trace.

## Change

- Reconciled the runtime-status spine to Pantheon Next contract PR #422 and external `pantheon-mvp` PR #41.
- Recorded external squash commit `af5ce4b552db8de1a90b53fdb40b810074dbc4dc` and PostgreSQL/pgvector workflow run `29764430187`.
- Replaced obsolete claims that Knowledge publication and mobile offline editing were absent.
- Preserved the distinction between a tested external implementation and installation, activation, adoption or production use.

## Why

The external adapter now validates the vendored Document → Knowledge contract, freezes source/chunk provenance, publishes versioned `generated_unreviewed` Knowledge and exposes a conflict-safe mobile editor candidate. Leaving the status spine at the earlier Document Card commit would make the repository materially stale.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none in Pantheon Next; an external implementation is observed only.
Authority impact: none; Knowledge remains neither Evidence, governed memory nor doctrine.
Schema/test/CI impact: no new artifact in this reconciliation; external run `29764430187` reported `155 passed`.
External action: GitHub repository reconciliation only; no installation, credential use, live Hermes connection or real dossier access.
Memory behavior: none.

## Local distinctions

```text
external implementation observed != binding adopted
PWA committed != mobile deployment authorized
queued_for_hermes != live Hermes proposal
generated_unreviewed != reviewed
test pass != professional validation
```
