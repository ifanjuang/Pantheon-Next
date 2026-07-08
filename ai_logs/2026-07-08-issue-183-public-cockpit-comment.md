# 2026-07-08 — Issue #183 public cockpit wording comment

## Status

Validation-only trace.

This log records an explicit GitHub issue comment added to the existing landing refactor issue. It does not create doctrine, runtime behavior, approval, memory promotion, provider routing, scheduling, installation, update execution or external action beyond the recorded issue comment.

## External action performed

A comment was added to:

```text
https://github.com/ifanjuang/Pantheon-Next/issues/183
```

GitHub comment id:

```text
4918658715
```

## Why

`docs/index.html` still contains public landing labels such as `Cockpit`, while Pantheon Control is a static prototype and has now been clarified as `Maquette statique` in its own entry point.

Because `docs/index.html` is monolithic and broad hand-editing through a full-file replacement is riskier than the label change itself, the durable fix belongs in issue #183:

```text
Docs HTML refactor: landing index and shared components
```

## Comment content summary

The issue comment adds the requirement that the landing refactor must apply the cockpit wording rule from `docs/assets/README.md`:

```text
Preferred public labels:
- Maquette cockpit
- Maquette Pantheon Control
- Prototype statique

Avoid unqualified labels:
- Cockpit
- Control plane
- Dashboard live
- Services en ligne
- Connexions actives
```

unless the same visible block says that the state is declared, fictive, static or target behaviour.

## Boundary kept

The issue comment does not authorize:

```text
runtime
agent loop
scheduler
queue
provider router
MCP host gateway
plugin manager
installer
updater
automatic approval
automatic memory promotion
external sender
service control
account connection
external routing
```

## Result

The landing refactor issue now carries the public cockpit wording requirement without risking a brittle full-file patch of `docs/index.html`.
