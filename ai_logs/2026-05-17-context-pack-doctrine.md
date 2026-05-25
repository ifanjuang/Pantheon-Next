# AI Log — Context Pack Doctrine Integration

Date: 2026-05-17

## Context

The user asked whether the Claude-oriented `CLAUDE.md` pattern could inspire Pantheon Next beyond Claude Code.

The conclusion was that the valuable abstraction is not `CLAUDE.md` itself, but a governed context package that can be adapted to multiple assistants, cockpit surfaces and external runtimes.

## Action

Created:

```text
docs/governance/CONTEXT_PACKS.md
```

Updated:

```text
docs/governance/README.md
docs/governance/STATUS.md
CHANGELOG.md
```

## Doctrine added

A Context Pack is now defined as a scoped, governed context bundle prepared for:

- Claude Code;
- ChatGPT;
- OpenWebUI;
- Hermes Agent;
- external assistants;
- human reviewers.

A Context Pack prepares action.

It is not:

- Canonical Memory;
- Evidence Pack;
- approval;
- doctrine by itself;
- runtime state;
- system prompt authority;
- hidden task launcher;
- substitute for a Task Contract.

## Central rule

```text
Context prepares action.
Evidence supports review.
Approval legitimizes change.
Memory preserves what was validated.
```

## Adapter doctrine

Tool-specific surfaces are adapters, not canonical doctrine.

Examples:

```text
CLAUDE.md
ChatGPT project instructions
OpenWebUI system prompts
OpenWebUI folders
Hermes profile notes
Hermes Task Contract appendices
human checklists
```

If an adapter conflicts with active Pantheon doctrine, Pantheon doctrine wins.

## Boundary impact

This prevents the Claude Code memory/instruction pattern from creating parallel Pantheon memory.

It also prevents assistant-specific files from becoming stronger than governance documents.

The doctrine keeps the central separation:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Explicitly not implemented

This intervention did not implement:

- Context Pack runtime;
- automatic Context Pack generator;
- automatic Context Pack importer;
- hidden prompt authority;
- Context Pack executor;
- automatic context-to-memory promotion;
- Claude Code runtime integration;
- OpenWebUI runtime integration;
- Hermes runtime integration;
- schemas;
- tests;
- operations tooling.

## Status impact

`CONTEXT_PACKS.md` is now active governance doctrine.

`docs/governance/README.md`, `docs/governance/STATUS.md` and `CHANGELOG.md` now reference the Context Pack boundary.

## Next logical step

The next useful step is to reconcile schema fields against the active Markdown doctrine, including Context Pack relationships, but `schemas/` remains protected and requires explicit confirmation before modification.
