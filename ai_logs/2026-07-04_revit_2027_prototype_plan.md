# AI Log — Revit 2027 Prototype Plan

Date: 2026-07-04

Repository: `ifanjuang/Pantheon-Next`

## Context

After the Revit V0 capability registry was merged, the user clarified the target version:

```text
Pour 2027
```

External verification showed that Autodesk Revit 2027 documentation exists, that Revit 2027 surfaces a Revit Public MCP Server as Tech Preview, and that Revit 2027 migrates add-ins to .NET 10.

## Change made

Added:

```text
docs/governance/PANTHEON_REVIT_GATE_2027_PROTOTYPE_PLAN.md
```

The document records a documentation-only Revit 2027 prototype plan:

- target version: Revit 2027;
- runtime assumption: .NET 10;
- MCP: relevant external signal but not first dependency;
- first proof loop: `see -> understand -> show -> propose -> act lightly -> log`;
- first tools: context pack, selection, visible elements, active view capture, sandbox/review view, TextNote, DetailLine, action report;
- excluded from the prototype: MEP, HVAC, structure, save/sync, deletion, arbitrary generated code execution, family edits, wall profile edits and curtain-wall generation.

## Repo state

```text
Documented non-implemented.
```

No plugin code, Revit add-in, MCP server, schema, test, Docker file, operations file or protected path was changed.

## Decision classification

```text
Accepté:
- Target the first prototype at Revit 2027.
- Treat .NET 10 as the add-in runtime assumption.
- Keep MCP as adapter/transport, not authority.
- Keep the first proof loop small and review-oriented.

Refusé:
- Treating the plan as implementation.
- Promoting Revit Public MCP Server Tech Preview as the core architecture.
- Adding code or protected-path changes in this step.

À vérifier:
- Exact Revit 2027 SDK / add-in scaffold details.
- Preferred local relay: localhost HTTP, WebSocket, named pipe or stdio.
- First UI surface: ribbon command, dockable panel or modeless WPF panel.

À arbitrer:
- Where the actual plugin code will live.
- Which first write_light action should be prototyped first.
```

## Notion

The GitHub repository remains canonical. Notion should be updated if a PR is opened from this branch.