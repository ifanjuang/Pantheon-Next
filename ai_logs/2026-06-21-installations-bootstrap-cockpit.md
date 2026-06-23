# AI log — Installations & bootstrap cockpit page

Date: 2026-06-21
Repository: `ifanjuang/Pantheon-Next`

## Request

User asked to continue development after documenting the bootstrap dependency ladder for a machine or NAS starting from nothing installed.

## Created

- `docs/assets/pantheon-control/installations.html`
- `docs/assets/pantheon-control/installations-data.js`
- `docs/assets/pantheon-control/installations-ui.js`

## Updated

- `docs/assets/pantheon-control/nav.js`

## Result

Added a cockpit page named `Installations & bootstrap` under Infrastructure.

The page displays:

- bootstrap layers L0 to L8;
- dependencies;
- current mock status;
- execution owner;
- Pantheon role;
- next action;
- recommended NAS / compute profiles;
- possible installation states;
- candidate request log.

## Boundary preserved

No protected path changed.
No operational configuration file created.
No executable script created.
No package created.
No system service created.
No network rule created.
No runtime service created.
No Portainer, OpenWebUI, Hermes, queue, scheduler, memory engine, vector database, GraphRAG runtime, LangGraph runtime, Langflow runtime or connector gateway was created.

## Doctrine retained

```text
Before Hermes exists, Pantheon cannot ask Hermes to install Hermes.
Bootstrap must be human-readable and runtime-independent.
This cockpit page prepares candidate steps only.
It does not install anything.
```
