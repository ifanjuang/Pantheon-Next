# AI log — Bootstrap installation ladder candidate

Date: 2026-06-21
Repository: `ifanjuang/Pantheon-Next`

## Request

User asked whether Pantheon should use Hermes resources to facilitate module installation, while noting that at initial cold start Hermes, OpenWebUI, Portainer and Docker may not be available yet. User requested an A-to-Z dependency view.

## Search performed

```text
bootstrap installation ladder cold start installer hermes openwebui portainer docker
```

No equivalent document was found.

## Created

- `docs/governance/BOOTSTRAP_INSTALLATION_LADDER.md`

## Decision

Decision Zeus: Accepté as candidate orientation.

The core resolution is that Pantheon cannot rely on Hermes before Hermes exists.

## Covered

- cold-start dependency loop;
- human and physical baseline;
- bootstrap medium;
- base system capability;
- service substrate;
- minimal static cockpit or docs before OpenWebUI;
- Hermes installation candidate;
- exposure surface candidate;
- runtime modules and services;
- admission and per-task authorization;
- manual-first, bootstrap artifact, vendor package and admin workstation modes;
- NAS-first recommendation;
- redirection before runtime;
- health check ladder;
- cockpit representation.

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
The first installer is human, vendor tooling or a separately approved bootstrap artifact.
Hermes executes only after it exists and is authorized.
Pantheon prepares, classifies, checks and records status.
The human decides each escalation.
```
