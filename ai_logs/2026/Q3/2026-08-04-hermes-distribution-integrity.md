# 2026-08-04 — Hermes distribution integrity contract

Status: candidate declarative contract change; no runtime or activation effect.

## Context

The first Hermes distribution lock recorded repository refs and component paths, but component digests were optional and the external runtime version could be expressed as a range. The operational lock also cannot truthfully contain the final commit SHA of the repository that contains it.

## Change

The distribution contract revision is raised to `2` and now requires:

- an exact Hermes semantic version target;
- an explicit runtime artifact digest field, nullable only while the lock is candidate or otherwise unobserved;
- `digest_mode` and `content_digest` for every declared component;
- a required artifact-integrity acceptance check;
- deterministic file and directory digest semantics.

Repository refs remain provenance anchors. Exact component identity is established by content digests.

## Boundary

```text
source revision recorded != final self-containing commit
component digest matched != component installed
runtime version reviewed != runtime artifact observed
artifact observed != binding activated
acceptance passed != task authorized
```

No installer, updater, runtime, scheduler, queue, provider router, plugin manager, memory promotion, approval or Evidence admission is introduced.
