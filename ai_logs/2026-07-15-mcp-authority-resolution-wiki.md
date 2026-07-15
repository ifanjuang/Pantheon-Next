# AI log — MCP authority resolution and governance wiki

Date: 2026-07-15

## Intent

Resolve MCP source authority through the decomposed authority indexes and give
Hermes an on-demand, traceable explanation of the governance structure.

## Changes

- added a pure read-only resolver shared by the MCP source map and current-tree
  authority coverage CI;
- implemented exact, directory and glob resolution, exact precedence,
  registered-sub-index discovery, source-row tracing and fail-closed conflict or
  missing outcomes;
- indexed the seven existing source-map documents that had no deliberate row,
  preserving their declared status and adding no runtime or promotion;
- added `explain_governance_structure`, a read-only navigation aid grouping the
  governed sources and explaining why each group exists;
- added unit and integration coverage for master, sub-index, grouped, missing,
  conflict and unregistered cases.

## Boundary

The structure guide is not a second source of truth. Authority remains in the
master index and its registered placement sub-indexes. The MCP reads and
explains; it does not execute, write, approve, schedule, route, install or
promote memory.

```text
OpenWebUI exposes.
Hermes executes.
Pantheon governs.
```
