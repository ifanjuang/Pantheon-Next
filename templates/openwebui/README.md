# OpenWebUI Templates

Status: non-executable cockpit template scaffold.

This directory contains candidate templates for future OpenWebUI cockpit surfaces.

They are not OpenWebUI Functions (Pipes, Filters, Actions, Event functions), Tools or Pipelines.

They are not installable plugins.

## Placement

OpenWebUI may expose:

```text
Task Contracts
Context Packs
Evidence Pack Candidates
Register Candidates
approval prompts
User Decision Gates
Capability Gaps
candidate status labels
```

OpenWebUI must not govern, execute, canonize memory, route providers or bypass approvals.

## Template classes and their OpenWebUI primitive (reference: OpenWebUI 0.10.2)

Some classes map to a native OpenWebUI primitive; others are Pantheon cockpit
concepts realized *through* a native primitive (OpenWebUI has no such primitive by
that name). Nothing here is installable.

```text
actions/         -> Action function            (native; thin toolbar action)
filters/         -> Filter function            (native; inlet/outlet display/status)
events/          -> Event function             (native, 0.10.x; read-only audit feed)
model_profiles/  -> a model connection/config  (NOT a native primitive; a cockpit profile
                                                 realized via an OpenAI-compatible connection)
forms/           -> an Action or a Tool         (NOT a native primitive; a governed input
                                                 surface realized via a native primitive)
```

The connection to the Hermes runtime is an OpenAI-compatible provider (see
`templates/hermes/connection/`). Skills consumed by Hermes use the `agentskills.io`
`SKILL.md` standard (see `templates/hermes/skills/`).

## Rule

A cockpit template may expose a decision surface.

It must not decide by itself.
