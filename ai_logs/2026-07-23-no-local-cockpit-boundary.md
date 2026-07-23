# 2026-07-23 — No-local-cockpit boundary guard

Status: validation-only intervention trace.
Boundary profile: validation_only_trace.

## Change

The canonical repository description now reflects the merged placement decision: the executable cockpit belongs to `ifanjuang/pantheon-mvp`, while `docs/assets/pantheon-control/` is an orientation point plus a closed inventory of validation-support artifacts.

A read-only repository check now verifies:

- no root `dashboard/` module exists;
- retired local product paths remain absent;
- the Pantheon Control directory contains only the explicitly retained inventory;
- the orientation page loads no script, stylesheet, iframe, embed or object resource;
- the orientation page states the external `pantheon-mvp` and non-runtime boundary.

The root test suite runs the check against the actual repository tree and covers representative refusal cases.

## Boundary

The check reads files and returns a process verdict. It does not inspect a live runtime, contact `pantheon-mvp`, install anything, execute Hermes, approve an output or authorize professional use.

```text
allowlisted validation artifact != cockpit product
absence of local cockpit != external deployment proof
CI success != runtime safety
orientation link != adoption or activation
```

## Protected paths

This intervention updates canonical repository instructions and adds a root test. It was explicitly authorized as the narrowed completion of issue #452.
