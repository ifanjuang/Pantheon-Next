# 2026-07-10 — WHAT_RUNS entry for MVP Vertical binding

Status: validation-only trace.

Boundary profile: validation_only_trace.

## What changed

Updated:

```text
docs/governance/WHAT_RUNS.md
```

The runtime-status map now includes the Pantheon MVP Vertical binding as:

```text
documented non-implemented / external executable candidate
```

## Why

PR #333 classified the external `pantheon-mvp-vertical` bundle as a candidate binding for `governed_task_loop_block_1`.

PR #335 then cleaned up the one-shot reference review after the binding distillate landed.

`WHAT_RUNS.md` now reflects the current status explicitly: the binding is documented and governed by Pantheon as a candidate, but it is not imported, installed, executed, activated or adopted by Pantheon.

## Boundary

This change does not create runtime behavior.

It does not install the external repo, execute the bundle, approve adoption, approve activation, validate evidence, send externally, schedule, route providers or promote memory.

## Current adoption status

```text
adoption:
  blocked pending P0 fixes.

P0 fixes:
  Task Contract schema alignment
  canonical path-boundary checks
  fixture-specific runner labelling
  related tests
```
