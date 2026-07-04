# Revit Plugin — Pantheon Revit Gate 2027

Status: skeleton / documented non-implemented.

Repository state: implementation artifact candidate — external adapter prototype, not Pantheon kernel doctrine.

This folder is reserved for a future local Revit 2027 adapter prototype.

It does not currently contain a compiling Revit add-in, `.addin` manifest, Revit command, local relay, MCP server, test harness or runnable integration.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
Revit executes locally.
```

## Boundary

`revit-plugin/` is not the Pantheon governance kernel.

It must not redefine doctrine, authority classes, approval rules, memory rules, evidence rules or scope rules.

It may later implement a local Revit adapter that consumes governed contracts and produces traceable local Revit effects.

```text
Pantheon governs the contract and status.
Hermes may call the adapter.
The Revit plugin executes inside Revit.
The human validates consequential actions.
```

## Target

```text
Target product: Autodesk Revit 2027
Target add-in runtime: C# / .NET 10
Primary API surface: Revit API inside Revit context
Optional later adapter: MCP wrapper or local relay
```

## Current skeleton

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

## Runtime rule

No runtime is implemented yet.

A future implementation must not claim to be operational until at least one Revit 2027 add-in compiles, loads in Revit, exposes a visible command and writes a local trace.

## Core model

```text
C# / .NET 10 = future Revit add-in core
Python = support tooling only
Generated snippets = candidate references only
Hermes = external caller / task-state orchestrator
Pantheon = governance of status, proof, scope, approval and memory
```

## First intended loop

```text
see -> understand -> show -> propose -> act lightly -> log
```

The first real prototype should prove only a small loop:

```text
1. Read active Revit document and active view.
2. Read selection.
3. Capture a context pack.
4. Optionally create a sandbox/review view.
5. Optionally create a TextNote or DetailLine.
6. Write a local action log.
```

## Explicit non-goals for the first prototype

```text
No MEP.
No HVAC.
No structure.
No save/sync.
No deletion.
No broad model rewrite.
No production model automation.
No unreviewed generated snippet promotion.
```

## Relationship with Pantheon docs

The governing and planning documents remain in `docs/governance/` until the repository authority/decomposition work decides a better placement.

Relevant current documents include:

```text
docs/governance/PANTHEON_REVIT_GATE.md
docs/governance/PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md
docs/governance/PANTHEON_REVIT_GATE_2027_PROTOTYPE_PLAN.md
```

This folder must stay aligned with those documents.
