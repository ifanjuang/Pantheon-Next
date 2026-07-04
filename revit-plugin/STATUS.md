# Revit Plugin Status

Status date: 2026-07-04

Repository state: skeleton / documented non-implemented.

## Current state

```text
Implemented: no.
Documented non-implemented: yes.
Partial: skeleton only.
To verify: future Revit 2027 add-in scaffold.
Obsolete: no.
```

## What exists

```text
README boundary
architecture note
consolidated execution model
knowledge source policy
Python/snippet policy
context pack contract candidate
action log contract candidate
sample JSON / JSONL
placeholder source tree
```

## What does not exist

```text
No Revit add-in.
No .addin manifest.
No C# project.
No compiled DLL.
No loaded Revit command.
No local relay.
No MCP server.
No tests.
No CI.
No model modification.
No production runtime.
```

## Target runtime, later

```text
Revit 2027
C#
.NET 10
local Revit API execution
Revit-controlled handler for writes
named transactions for write_light actions
local JSONL action logs
```

## Safety boundary

A future implementation must keep these non-negotiables visible:

```text
active document name visible before action
async request handling, but Revit-controlled writes
named transaction for write_light effects
local action log
affected ElementIds where available
warning level and reversibility level
preflight before write
stop / disable Hermes control
no delete in first prototype
no save/sync in first prototype
no unreviewed generated snippet promotion
```

## Indexing note

`AUTHORITY_INDEX.md` and `WHAT_RUNS.md` are not modified in this branch.

This folder should be indexed after the authority/decomposition work clarifies the expected placement, or before merge if reviewers require it.
