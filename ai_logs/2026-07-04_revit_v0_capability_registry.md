# AI Log — Revit V0 Capability Registry Slice

Date: 2026-07-04

Repository: `ifanjuang/Pantheon-Next`

## Context

After PR #272 merged the Revit Free Exploration V0 posture, the next step was to narrow the wide field of possible Revit actions into a buildable first capability registry slice.

The user confirmed moving forward with a V0 registry that keeps the plugin permissive in spirit, but technically grounded in reliable primitives:

```text
Context Pack
Selection Intelligence
Spatial Queries
Method Candidate
Preview / Sandbox
Action Log
```

## Change made

Updated:

```text
docs/governance/PANTHEON_REVIT_GATE.md
```

Added section:

```text
V0 initial capability registry slice
```

The section defines:

- effect vocabulary: `read_only`, `candidate_only`, `write_light`, `write_model`, `export`, `log`, `blocked_v0`;
- difficulty vocabulary: `low`, `medium`, `high`, `research`;
- a core V0 registry of buildable first-slice tools;
- a visible-but-not-first-build table for model-writing and high-risk capabilities;
- the first complete scenario to prove the product spine.

## Product spine recorded

```text
see -> understand -> show -> propose -> act lightly -> log
```

This is the recommended first prototype loop before geometry-writing capabilities are promoted into the sandbox surface.

## Repo state

```text
Documented non-implemented.
```

No plugin code, Revit add-in, MCP server, schema, test, Docker file, operations file or protected path was changed.

## Decision classification

```text
Accepté:
- Add a compact V0 capability registry slice.
- Keep first build focused on context, selection, spatial primitives, method choice, light write and log.
- Keep risky/model-writing tools visible but not first-build.

Refusé:
- Treating the registry as implementation.
- Presenting wall-profile edit, curtain wall generation, delete, save, sync or arbitrary generated code as first-build tools.

À vérifier:
- Actual Revit API feasibility of each high/research tool.
- Which first writable action should be prototyped after TextNote/DetailLine.
- Whether `write_parameter_selected` should be limited to review parameters only in the first build.

À arbitrer:
- Whether the registry should later become a separate capability passport file or remain embedded in `PANTHEON_REVIT_GATE.md`.
```

## Notion

The GitHub repository remains canonical. Notion should be updated if a PR is opened from this branch.