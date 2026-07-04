# AI Log — Revit Plugin Skeleton

Date: 2026-07-04

Repository: `ifanjuang/Pantheon-Next`

## Context

The user decided that a future Revit plugin may live under:

```text
Pantheon-Next/revit-plugin/
```

The user then clarified several architectural requirements:

```text
C# / .NET 10 = future Revit 2027 add-in core.
Python = support tooling only.
Generated snippets = candidate references only.
All modifications should be asynchronous at request level.
Actual Revit writes must remain Revit-controlled and transactional.
Hermes may expose broad capabilities, with warning levels and validation friction.
Hermes must track requested, running, blocked, failed, retried and finalized work.
Blockers should be generic task states, not exhaustive case documentation.
Official Revit docs may be vectorized as a Hermes reference skill.
```

## Change made

Created a skeleton-only `revit-plugin/` folder with consolidated boundary documentation, sample contracts and placeholders.

Added final skeleton files:

```text
revit-plugin/README.md
revit-plugin/STATUS.md
revit-plugin/docs/ARCHITECTURE.md
revit-plugin/docs/EXECUTION_MODEL.md
revit-plugin/docs/KNOWLEDGE_SOURCE_POLICY.md
revit-plugin/docs/PYTHON_AND_GENERATED_SNIPPETS.md
revit-plugin/docs/CONTEXT_PACK_CONTRACT.md
revit-plugin/docs/ACTION_LOG_CONTRACT.md
revit-plugin/tools/python/README.md
revit-plugin/src/.gitkeep
revit-plugin/samples/context-pack.example.json
revit-plugin/samples/action-log.example.jsonl
```

## Repo state

```text
Skeleton / documented non-implemented.
```

No compiling Revit add-in, `.addin` manifest, C# project, local relay, MCP server, tests, schemas, Docker file, operations file or production runtime was added.

## Consolidated model

```text
Task
Action
Dependency
Blocker
WarningLevel
ReversibilityLevel
ValidationState
ResultState
ActionLog
```

## Decision classification

```text
Accepté:
- A `revit-plugin/` folder may exist in Pantheon-Next as an isolated implementation artifact candidate.
- It must remain clearly separated from Pantheon kernel doctrine.
- C# / .NET 10 remains the future plugin core.
- Python is support tooling only.
- Generated snippets are candidate references only.
- Hermes may expose broad capabilities, but visibility does not mean execution.
- Warning levels and reversibility levels determine friction.
- Blocking conditions should be represented generically rather than exhaustively mapped.
- A future Hermes Revit Reference skill may use official vectorized docs.

Refusé:
- Treating `revit-plugin/` as Pantheon governance kernel.
- Claiming implementation before a Revit add-in compiles and loads.
- Treating runtime possibility as governance permission.
- Treating retrieval as proof or approval.
- Silent execution of consequential Revit changes.
- Silent escalation from one method to a riskier method.
- Exhaustive case mapping as doctrine.

À vérifier:
- Whether `revit-plugin/` needs immediate `AUTHORITY_INDEX.md` and `WHAT_RUNS.md` rows.
- Exact Revit 2027 C#/.NET 10 scaffold.
- Where task state lives first: plugin-side, Hermes-side or both.
- Whether the vectorized Revit reference corpus lives only in Hermes local storage.

À arbitrer:
- Whether the first code PR should add `.sln`/`.csproj` or only C# source stubs.
- Whether local relay starts with HTTP, WebSocket, named pipe or stdio.
- Default warning levels for first tools.
```

## Boundary note

`AUTHORITY_INDEX.md` and `WHAT_RUNS.md` were not modified in this branch. Any authority/runtime-status row for `revit-plugin/` should be handled in a follow-up or added before merge if review requires it.