# Hermes governed memory posture — 2026-08-04

Status: completed governance clarification candidate. No Hermes configuration, memory file, toolset, profile or runtime was modified.

## Objective

Close the ambiguity between disabling an external Hermes memory provider and disabling every runtime-memory input that can affect a Pantheon-admitted run.

## Upstream fact checked

Hermes Agent 0.20.0 exposes profile-local memory status with separate values for:

```text
external provider
built-in MEMORY.md injection
built-in USER.md profile injection
memory tool
```

The OpenAI-compatible API also supports opt-in long-term memory scoping through `X-Hermes-Session-Key`.

`hermes memory off` changes the external provider selection. It does not by itself disable the three built-in memory surfaces.

## Existing Pantheon state

The merged runtime-mode doctrine already required:

```text
external provider off
automatic recall/write forbidden
hidden OpenWebUI memory/RAG forbidden
```

It did not yet state the built-in memory injection, user profile, memory tool or session-memory-key requirements explicitly.

## Decision

A `pantheon-governed` profile is qualified only when all axes are observed:

```text
external_provider: off
built_in_memory_injection: off
built_in_user_profile_injection: off
memory_tool: off
session_memory_key: absent
```

Stored `MEMORY.md` or `USER.md` files may remain inside the isolated profile, but they must not enter the prompt, retrieval path or memory tool during governed work.

Any unknown or active axis keeps the profile `not_qualified` and produces a Capability Gap.

## Observer consequence

The current MVP observer reads `/v1/capabilities` and `/v1/toolsets`. Those surfaces cannot prove the complete memory posture.

Therefore:

```text
observer_contract_change_required: true
```

A later MVP extension must consume an explicit read-only profile-memory observation. It must not infer built-in injection state from tool absence, read arbitrary host files or mutate Hermes configuration.

## Files changed

```text
docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md
docs/governance/HERMES_RUNTIME_GOVERNANCE.md
hermes/profiles/README.md
hermes/profiles/PROFILE_CONSTITUTION.md
hermes/profiles/_base/base-soul-rules.md
tests/test_hermes_ecosystem_adaptability.py
```

## Non-effects

```text
no runtime
no profile creation
no memory deletion
no memory-provider selection
no tool activation
no OpenWebUI configuration
no distribution-lock change
no task authorization
```
