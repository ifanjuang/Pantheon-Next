# Canonical contract direct consumption

Date: 2026-08-23
Status: implementation convergence trace; not doctrine.

## Objective

Remove the cross-repository schema-vendoring path made redundant by the monorepo consolidation.

## Result

- repository checkouts consume Pantheon contracts directly from root `schemas/`;
- built wheels stage the complete schema tree as an exact generated, Git-ignored payload;
- packaged schema bytes are verified against the build manifest before use;
- dirty checkouts do not claim `HEAD` as the exact source commit for changed schema bytes;
- the decision vocabulary is read directly from `$defs.decision_value.enum`;
- committed vendor snapshots, source sidecars, pin files, revendor helpers and schema-drift workflow are removed;
- runtime consumers that still reconstructed `vendor/pantheon` paths were converted to `pantheon_contracts` and a permanent regression guard now refuses their reintroduction;
- historical tests for Decision Request, Navigation Registry, Tag Registry and document currentness now verify the canonical root contract and its non-authoritative semantics instead of deleted vendor sidecars or fixed upstream pins;
- schema conformance remains distinct from approval, Evidence and authorization.

## CI finding during convergence

The full PostgreSQL suite was intentionally kept strict. After the runtime consumers were converted, it exposed eight remaining failures caused only by tests that still opened deleted files under `mvp_vertical/vendor/pantheon`. Those tests were converged to the canonical contract registry; no runtime behavior, schema vocabulary, PostgreSQL migration or authority rule was relaxed to make the suite pass.

A temporary self-removing workflow was used only to perform the exact mechanical rewrites on the branch because the large currentness test could not be safely patched through a partial file update. Its final tree contains no additional workflow.

## Non-equivalences

```text
generated build copy != second authority
schema conformance != professional approval
runtime success != Evidence
repository co-location != authority transfer
```
