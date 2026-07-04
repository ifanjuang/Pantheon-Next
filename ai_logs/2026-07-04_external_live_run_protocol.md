# AI log — external live run protocol

Date: 2026-07-04

## Scope

Prepared issue #273 by adding a validation-only protocol for the first external OpenWebUI to Hermes test.

## File added

```text
docs/examples/vertical_devis_reprise/EXTERNAL_LIVE_RUN_PROTOCOL.md
```

## Summary

The new protocol records:

- required environment notes;
- minimum request fields;
- expected candidate return shape;
- expected evidence candidate shape;
- read-only verification commands;
- pass/fail classifications;
- post-test note template for issue #273.

## Decision

Accepted:

- prepare the external test;
- keep the test as validation-only example material;
- use the fictional `architecture_devis_reprise` slice;
- keep human decision separate from technical success.

Refused:

- no repository runtime;
- no repository service;
- no automatic approval;
- no memory promotion;
- no sending action.

## Tool limitation

A follow-up edit to `RUNBOOK.md` was attempted to link the protocol, but the tool safety layer blocked that update. Issue #273 now links the protocol file instead.

## Repo state

- Documentation protocol: implemented.
- Protected paths touched: none.
