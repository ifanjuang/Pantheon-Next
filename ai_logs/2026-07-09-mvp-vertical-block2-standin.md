# 2026-07-09 — MVP Vertical Block 2 stand-in clarification

Status: validation-only trace — documented non-implemented.

Boundary profile: validation_only_trace.

## What changed

Updated the existing MVP vertical distillate:

```text
docs/governance/PANTHEON_MVP_VERTICAL_BINDING.md
```

Updated the runtime-adapter authority sub-index row:

```text
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
```

The update records the reported Block 2 follow-up: terminal decision gate, four review choices, signed decision trace, system-signer refusal and reported 12/12 local tests.

A later correction points the published repository target to:

```text
ifanjuang/pantheon-mvp
```

The original bundle name remains `pantheon-mvp-vertical.bundle`.

## Why

The external vertical slice is still a candidate binding, but the explanatory status needed tightening after the Block 2 handoff.

The key clarification is that the deterministic runner occupies the Hermes seat only as a stand-in, while the terminal gate occupies the OpenWebUI seat only as a stand-in.

This prevents a future reader from treating the external repo as the final Hermes implementation or a live OpenWebUI cockpit.

The GitHub repository now exists, but executable MVP content was not verified through the connector. Repository existence must not be read as executable content push, CI verification, adoption or activation.

## Boundary

This change does not import, install, execute, activate, approve, send, schedule, route providers, validate evidence or promote memory.

It documents a reported external artifact status and a repository-target correction only.

## Preserved distinctions

```text
stand_in_runner != Hermes Agent
terminal_gate != OpenWebUI cockpit
twelve_tests_reported != twelve_tests_currently_verified_by_pantheon
repository_exists != executable_content_pushed
runtime_success != evidence
result_candidate != approved_result
external_repo != Pantheon runtime
```

## Required external follow-up

Before adoption or activation, the external repository still needs:

```text
executable content push to ifanjuang/pantheon-mvp
P0 schema alignment
P0 source path boundary proof
P0 stand-in naming or explicit headers
P0 gate decision semantics review
visible external CI after push
human approval for adoption
```

## Status

```text
implemented in Pantheon Next:
  documentation clarification only.

published external repository observed:
  ifanjuang/pantheon-mvp exists, but executable MVP content is not verified here.

reported externally:
  Block 2 decision gate and 12/12 tests.

not verified here:
  executable content pushed to pantheon-mvp, CI result, concrete Block 2 diff, test coverage.

adoption:
  still blocked pending content push, P0 fixes and human approval.
```
