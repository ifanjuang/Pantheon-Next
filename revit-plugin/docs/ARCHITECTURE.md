# Revit Plugin Architecture

Status: planning note — documented non-implemented.

This note describes the intended adapter shape. It does not implement the plugin.

## Target split

```text
Pantheon governance docs
  -> capability status, scope, proof, approval and boundaries

Hermes Agent
  -> external caller and operational task-state orchestrator

Revit Plugin
  -> local Revit 2027 adapter running inside Revit

Revit API
  -> actual local model read/write surface
```

## First architecture target

```text
Revit 2027 Add-in
  -> Ribbon command
  -> Context reader
  -> View capture service
  -> Light writer service
  -> Transaction runner
  -> Local action log
  -> Optional relay endpoint
```

## First proof loop

```text
User opens a local RVT.
User selects one architectural element or opens a relevant view.
User clicks a Revit command.
Plugin captures a context pack.
Hermes receives or simulates a response.
Plugin previews or writes a light review artifact.
Plugin logs the action.
```

## Future C# layout

Candidate project layout:

```text
src/Pantheon.RevitGate2027/
  Addin/
  Commands/
  Context/
  Actions/
  Logging/
  Relay/
  Serialization/
```

No project files are created in the skeleton PR.

## C# responsibility

```text
load inside Revit;
call Revit API safely;
respect Revit UI/API context;
run named transactions;
write local traces;
block or elevate dangerous operations in early prototypes.
```

## Execution model

The detailed execution posture is consolidated in:

```text
revit-plugin/docs/EXECUTION_MODEL.md
```

It covers:

```text
async request handling;
Revit-controlled writes;
warning levels;
reversibility levels;
task and action state;
blockers and dependencies;
non-blocking user dialogue;
controlled retry loops;
finalization.
```

## Knowledge model

The source policy is consolidated in:

```text
revit-plugin/docs/KNOWLEDGE_SOURCE_POLICY.md
```

A future Hermes Revit Reference skill may retrieve official and candidate references, but retrieval produces method candidates, not permission to modify Revit.

## Python position

The Python and snippet policy is consolidated in:

```text
revit-plugin/docs/PYTHON_AND_GENERATED_SNIPPETS.md
```

Python remains support tooling only.

## MCP position, later

MCP may become an adapter wrapper after local primitives exist.

```text
MCP is transport / interface.
MCP is not authority.
MCP does not approve Revit actions.
MCP does not replace local Revit transaction discipline.
```

## First excluded operations

```text
delete element
purge unused
save model
sync model
broad model rewrite
load families automatically
modify central/workshared state
```
