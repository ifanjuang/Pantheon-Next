# 2026-07-28 — Revit Local Adapter V0 boundary

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## What changed

Added a documentation-only V0 boundary for the future local Revit adapter.

Files added:

```text
docs/governance/REVIT_LOCAL_ADAPTER_V0.md
ai_logs/2026/Q3/2026-07-28-revit-local-adapter-v0.md
```

Files updated:

```text
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
docs/governance/WHAT_RUNS.md
```

## Why

The repository already classified `revit_local_adapter` as a candidate capability slot in `HERMES_CAPABILITY_BINDINGS.md`, but it did not yet have a focused Revit boundary document for the plugin V0.

The new document clarifies:

```text
Pantheon governs status, scope, evidence posture, approvals and forbidden effects.
Hermes may orchestrate bounded work externally under Task Contract.
Revit executes locally through a future controlled plugin.
OpenWebUI exposes status, previews, gaps and decision gates.
The human decides consequential effects.
```

## Boundary

This intervention is documentation-only.

It does not:

```text
create a Revit plugin
add a C#/.NET project
add a Revit API dependency
add a Hermes skill
add an OpenWebUI action
add a transaction runner
add an installer
add an updater
add tests or schemas
modify protected paths
execute Revit
approve adoption
approve activation
authorize real-project use
authorize save/sync/delete/purge
promote memory or Registre Probatoire entries
```

## Key doctrine added

The V0 boundary introduces simple Revit warning levels:

```text
W0 — read / observation
W1 — proposal / preview
W2 — light reversible write
W3 — model modification with dependencies
W4 — destructive or difficult to reverse
W5 — generated code or uncontrolled execution
```

V0 allows W0/W1 framing only. W2 remains blocked until sandbox approval and tests exist. W3/W4/W5 are refused for V0.

The document also defines the expected local transaction naming pattern for future mutations:

```text
PantheonGate:<task_id>:<action_id>:<short_effect>
```

This is a future rule for a local plugin implementation, not current executable behavior.

## Status classification

```text
implemented in Pantheon Next:
  documentation only.

documented non-implemented:
  Revit Local Adapter V0 boundary, index placement and status-map clarification.

not implemented:
  Revit add-in, C# project, Revit API package, local IPC, transaction runner,
  installer, updater, OpenWebUI action, Hermes skill or real Revit execution.

to verify later:
  sibling repository, Revit version/API target, W0/W1 implementation,
  preflight shape, action log shape, transaction refusal behavior and activation gates.
```

## Local distinctions preserved

```text
documented != implemented
capability_slot != installed_capability
Revit plugin visible != Revit plugin approved
preflight_pass != action_authorized
transaction_success != governance_approval
action_log != Evidence Pack
Evidence Pack Candidate != validated evidence
human_review_needed != human_approval_granted
```
