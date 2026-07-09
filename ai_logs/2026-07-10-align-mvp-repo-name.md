# 2026-07-10 — Align MVP binding repository name

Status: validation-only trace.

Boundary profile: validation_only_trace.

## What changed

Updated active governance documents to align the MVP binding with the published repository name:

```text
published repository: ifanjuang/pantheon-mvp
observed artifact: pantheon-mvp-vertical.bundle
```

Files updated:

```text
docs/governance/PANTHEON_MVP_VERTICAL_BINDING.md
docs/governance/WHAT_RUNS.md
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
```

## Why

The external repository was created/renamed as `ifanjuang/pantheon-mvp` after the original bundle review used the working name `pantheon-mvp-vertical`.

The docs now distinguish the reviewed bundle artifact from the published repository that should receive the bundle.

## Boundary

This change does not import, install, execute, activate, adopt or approve the external repository.

It does not validate CI, professional evidence, external send, memory promotion, provider routing, scheduling or runtime behavior.

## Current status

```text
repository_created: true
bundle_pushed: to_verify
ci_observed: to_verify
adoption: blocked pending P0 fixes and human approval
```
