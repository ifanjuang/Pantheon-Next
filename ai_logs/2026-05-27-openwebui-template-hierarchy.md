# AI Log — OpenWebUI Template Hierarchy

Date: 2026-05-27

## Context

The user chose to continue with OpenWebUI templates after the module activation doctrine.

The user explicitly requested hierarchical dependencies:

```text
some modules should disable whole branches of functionality when disabled
```

## Action

Created:

```text
docs/governance/OPENWEBUI_TEMPLATES.md
```

Updated:

```text
docs/governance/README.md
docs/governance/STATUS.md
docs/governance/ROADMAP.md
CHANGELOG.md
```

## Doctrine added

`OPENWEBUI_TEMPLATES.md` defines future cockpit template semantics for:

- parent-child dependency hierarchy;
- disabled-parent behavior;
- dependency state vocabulary;
- dependency records;
- mandatory blockers;
- degraded mode;
- UI control rules;
- OpenWebUI extension warning;
- Native Mode boundary;
- LangGraph run status exposure;
- Human Interrupt exposure;
- Capability Gap exposure.

Core rule:

```text
A disabled parent must make its children visibly unavailable.
A visible child must never imply its parent is satisfied.
```

## Hierarchy added

The documented parent surfaces are:

```text
Task Contract Surface
Knowledge and Source Surface
Evidence Surface
Decision Surface
Memory Surface
Module Control Surface
Runtime Candidate Surface
```

These surfaces define what child templates are blocked, degraded or unavailable when a parent is disabled.

## Boundary impact

This is support doctrine only.

It does not implement:

- OpenWebUI templates;
- OpenWebUI Functions;
- OpenWebUI Tools;
- OpenWebUI Pipes;
- OpenWebUI Filters;
- OpenWebUI Actions;
- OpenWebUI Pipelines;
- OpenWebUI native-mode governance runtime;
- module UI;
- module registry runtime;
- dependency graph runtime;
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

Main risk: dependency hierarchy could be mistaken for executable policy enforcement.

Mitigation: the document states that dependency blocking is cockpit visibility doctrine, not runtime enforcement.

Second risk: OpenWebUI template doctrine could be mistaken for OpenWebUI plugin or Function implementation.

Mitigation: the document explicitly states that templates come before thin actions, and runtime must not live inside OpenWebUI by default.

Third risk: Native Mode could become global agentic execution for Pantheon.

Mitigation: the document requires scoped task, declared tools, declared memory rule, declared evidence requirement and approval ceiling.

## Status impact

Pantheon Next now has a doctrine layer for future OpenWebUI cockpit templates and dependency blocking while preserving:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

OpenWebUI templates make governance visible.

They do not make governance true.