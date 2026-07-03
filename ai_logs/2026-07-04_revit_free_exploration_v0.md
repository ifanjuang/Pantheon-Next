# AI Log — Revit Free Exploration V0

Date: 2026-07-04

Repository: `ifanjuang/Pantheon-Next`

## Context

A Revit architecture plugin discussion clarified the preferred V0 posture:

```text
V0 should remain permissive to discover real architectural uses.
Regulation should come later from observed usage.
The initial scope is architecture only: no MEP, no HVAC, no structure.
Offline/local operation is preferred.
Hermes may orchestrate and call the plugin.
Pantheon should not become the runtime.
```

Existing repository material already contained Revit framing:

- `docs/governance/PANTHEON_REVIT_GATE.md`
- `docs/governance/PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md`

So the intervention updated the existing main framing document instead of creating a duplicate Revit dossier.

## Change made

Updated:

```text
docs/governance/PANTHEON_REVIT_GATE.md
```

The update records:

- `V0 Free Exploration Mode` as accepted sandbox/exploration orientation;
- architecture-only scope;
- offline/local-first posture;
- Hermes orchestration with plugin execution outside Pantheon;
- MCP as optional adapter, not authority;
- broad capability registry direction;
- visual context pack direction;
- method-first modeling for sketches, detail lines, façade profiles and curtain-wall composition;
- async analysis allowed, but committed Revit changes remain local Revit transactions;
- minimal non-negotiable traces: document name, named transaction, local log, affected elements, stop/disable control.

## Repo state

```text
Documented non-implemented.
```

No plugin code, Revit add-in, MCP server, schema, test, Docker file, operations file or protected path was changed.

## Decision classification

```text
Accepté:
- V0 permissive / sandbox exploration posture.
- Architecture-only scope.
- Offline/local-first assumption.
- Broad capability catalogue visible in plugin settings.
- Traceability from the first writable prototype.

Refusé:
- Treating the plugin as implemented.
- Making Pantheon the Revit runtime.
- Treating MCP as authority.
- Extending V0 to MEP, HVAC or structure.

À vérifier:
- Actual Revit API feasibility per capability family.
- Target Revit version(s).
- Local API vs MCP-first sequence.
- Minimum useful log/action-report format.
- Whether deletion stays blocked even in sandbox.

À arbitrer:
- First writable action to prototype.
- Final plugin name.
- Exact V0 capability registry fields.
```

## Notion

The GitHub repository remains canonical. Notion dashboard maintenance was not performed in this intervention.