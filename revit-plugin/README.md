# Revit Local Adapter Reference Skeleton

Status: non-executable reference skeleton — documented non-implemented.

Canonical boundary: `../docs/governance/REVIT_LOCAL_ADAPTER.md`.

This directory is a reference layout for a future external Revit add-in. It is not the Pantheon governance kernel and it does not currently contain a compiling add-in, `.addin` manifest, Revit command, relay, MCP server, installer or runnable integration.

```text
Pantheon Next governs contracts and status.
Hermes may orchestrate an admitted task.
The external Revit add-in executes inside Revit.
Cockpit exposes preflight and review.
The human decides consequential effects.
```

## Code-hosting boundary

Production add-in code should live in a dedicated implementation repository. This skeleton may illustrate contracts and fixtures only. Its presence does not adopt a binding or authorize this repository to become a runtime, installer or plugin manager.

## Current reference content

```text
revit-plugin/
  README.md
  STATUS.md
  docs/
    ARCHITECTURE.md
    EXECUTION_MODEL.md
    KNOWLEDGE_SOURCE_POLICY.md
    PYTHON_AND_GENERATED_SNIPPETS.md
    CONTEXT_PACK_CONTRACT.md
    ACTION_LOG_CONTRACT.md
  src/.gitkeep
  tools/python/README.md
  samples/
    context-pack.example.json
    action-log.example.jsonl
```

## Implementation metadata

The currently reviewed prototype target may be Autodesk Revit 2027 with C# and .NET 10. Product and runtime versions are binding metadata; they are not part of the architecture identity.

## First admissible proof

```text
read the active document and view
read the explicit selection
produce a bounded Context Pack candidate
return a local technical trace
refuse stale or out-of-scope work
```

Any writable proof requires a named Revit transaction, exact Task Contract correlation, human authorization, changed-element journaling and a demonstrated rollback or manual-reversal posture.

```text
compiled != installed
loaded != activated
transaction_success != accepted_result
runtime_success != Evidence
```
