# Boundary profiles dedup pass

Date: 2026-07-08

Status: validation-only trace — documented non-implemented.

## Context

After reducing repeated use of the architecture slogan, the next visible repetition was the long non-runtime disclaimer pattern:

```text
no runtime
no approval engine
no memory promotion
no scheduler
no queue
no provider router
no external action
```

The pattern is necessary, but repeating it everywhere makes documents harder to read and easier to drift.

## Change

Added:

```text
docs/governance/BOUNDARY_PROFILES.md
```

Updated:

```text
CONTRIBUTING.md
templates/README.md
docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md
```

## Decision

Use boundary profiles to reduce repeated boilerplate.

Boundary profiles do not reduce responsibility and do not hide consequential effects.

If a document changes runtime status, protected paths, external action, memory behavior, approval behavior or tool installation/update status, it must still name the specific boundary.

## First applied profile

`templates/README.md` now uses:

```text
Boundary profile: non_executable_template.
```

and expresses the concrete separation with:

```text
exposed_by
executed_by
governed_by
approved_by
forbidden
```

## Boundary

This change is documentation-only.

It does not add or modify:

```text
schemas/
tests/
CI workflows
runtime code
OpenWebUI Functions, Pipes, Filters or Actions
Hermes skills or contracts
approval engine
memory promotion
scheduler
queue
provider router
external action authorization
```

## Preserved distinctions

```text
boundary_profile != authorization
template != implementation
schema_valid != approved
runtime_success != evidence
trace != doctrine
```
