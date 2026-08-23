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
- schema conformance remains distinct from approval, Evidence and authorization.

## Non-equivalences

```text
generated build copy != second authority
schema conformance != professional approval
runtime success != Evidence
repository co-location != authority transfer
```
