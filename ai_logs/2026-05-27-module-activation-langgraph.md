# AI Log — Module Activation and LangGraph Boundary

Date: 2026-05-27

## Context

The user asked to keep Pantheon modular for future UI controls that can activate or deactivate modules.

The user then refined the requirement:

```text
detect if LangGraph is enabled;
if so, apply some rules by default;
other rules remain activable.
```

## Action

Created:

```text
docs/governance/MODULE_ACTIVATION.md
docs/governance/reference_reviews/README.md
docs/governance/reference_reviews/LANGGRAPH.md
hermes/profiles/_base/LANGGRAPH_RUNTIME_CANDIDATE.md
```

Updated:

```text
docs/governance/README.md
docs/governance/STATUS.md
docs/governance/ROADMAP.md
CHANGELOG.md
```

## Doctrine added

Module activation now separates:

```text
capability detection
→ governance activation
→ task authorization
```

Core rule:

```text
Detected does not mean enabled.
Enabled does not mean authorized for a task.
Authorized for a task does not mean sovereign.
```

`MODULE_ACTIVATION.md` defines:

- detection records;
- activation records;
- task authorization records;
- status vocabulary;
- activation scopes;
- mandatory rules;
- optional rules;
- Effective Policy examples;
- future UI control boundaries;
- LangGraph as the first example of a Hermes runtime candidate.

## LangGraph posture

LangGraph is documented as:

```text
Pantheon   -> reference review and governance boundary only
Hermes     -> optional runtime candidate only, if task-authorized
OpenWebUI  -> cockpit exposure only, not runtime authority
```

LangGraph may be detected in Hermes, but detection does not authorize use.

If LangGraph is enabled, mandatory Pantheon rules apply automatically.

Optional capabilities such as checkpoint resume, streaming status, human interrupts or limited retry may be toggled by governed scope.

## Explicitly not implemented

This intervention did not implement:

- LangGraph runtime;
- LangGraph installation;
- LangGraph OpenWebUI Function, Pipe, Tool or Pipeline;
- module UI;
- module registry runtime;
- module Effective Policy engine;
- automatic module detection monitor;
- automatic module activation;
- plugin manager;
- skill installer;
- provider router;
- scheduler;
- queue;
- automatic approval;
- automatic memory promotion;
- schemas;
- tests;
- operations tooling.

## Risk notes

Main risk: module activation vocabulary could be mistaken for a plugin manager or runtime policy engine.

Mitigation: `MODULE_ACTIVATION.md`, `STATUS.md`, `ROADMAP.md` and `CHANGELOG.md` explicitly state that this is support doctrine only.

Second risk: Effective Policy examples could be mistaken for executable enforcement.

Mitigation: Effective Policy is defined as a governance artifact, not a runtime engine.

Third risk: LangGraph runtime candidate documentation could be mistaken for installation approval.

Mitigation: LangGraph remains Hermes candidate only, not installed, not enabled by default and not a Pantheon runtime.

## Status impact

Pantheon Next now has a modular activation vocabulary for future UI work while preserving the core doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon detects capabilities to apply policy.

It does not detect capabilities to execute them.