# AI Log — Adapters and bindings

Date: 2026-05-31

## Scope

Recorded the blueprint-in-Pantheon and adapter-outside model so that tool-specific
templates and configurations (OpenWebUI, Hermes, Langfuse and others) can be adapted
to Pantheon without coupling Pantheon to any tool.

This follows the modular domain reorientation and answers a practical question:
where do tool-specific configurations live, and how do they stay adapted to Pantheon?

## Files changed

Added:

- `docs/governance/ADAPTERS_AND_BINDINGS.md`;
- `ai_logs/2026-05-31-adapters-and-bindings.md`.

Updated:

- `CHANGELOG.md`.

## Why the change was made

Using a tool's strengths requires real, runnable configuration. That configuration
must not live inside Pantheon, but it must stay adapted to Pantheon.

The document fixes the two halves of a capability — blueprint in Pantheon, adapter
outside — and the four disciplines that keep adapters healthy: dependency direction
toward Pantheon, conformance not duplication, stated target version, single source
of truth.

## Governance boundary

The document is support doctrine.

It does not implement a configuration, an OpenWebUI Function, a Hermes skill, a
Langfuse project, a runtime, a bridge or any executable artifact.

It confirms that adapted configurations belong outside Pantheon, in the tool's own
repository or a dedicated adapters repository, never inside Pantheon.

## Key doctrine preserved

```text
The blueprint lives in Pantheon.
The adapter lives in the tool.
The dependency always points to Pantheon.
The validated remains.
```

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```
