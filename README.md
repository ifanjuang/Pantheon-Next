# Pantheon Next

Pantheon Next est une couche de gouvernance déclarative pour systèmes agentiques.

Pantheon Next n’est pas un runtime, pas un agent, pas un orchestrateur autonome et pas un moteur d’exécution. Il définit l’autorité, les règles, les contrats, les preuves, les transitions autorisées, les approvals, les limites d’action et les conditions de mémoire que les runtimes externes doivent respecter.

La règle structurante du projet est simple :

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

Execution belongs to runtimes.

Authority belongs to Pantheon.

Pantheon Next sert à rendre les workflows agentiques gouvernables, traçables, auditables et maintenables.

## Repository baseline

This repository is the clean Pantheon Next governance baseline extracted from the historical Pantheon OS repository. It intentionally starts with governance documents, schemas, assets registry and AI intervention logs only.

Historical runtime-oriented folders are not migrated by default. They must be classified before reuse.

## Canonical primitives

```text
1. Workflow Event
2. Task Contract
3. Evidence Pack
4. Memory Candidate
5. Approval Policy
```

## Repository map

```text
docs/governance/  canonical governance Markdown
schemas/          machine-readable governance schemas and examples
ai_logs/          AI intervention logs
docs/assets/      diagram export registry
```

## Runtime boundary

Pantheon Next must not recreate:

```text
Execution Engine
Agent Runtime
Tool Runtime
LLM Provider Router
scheduler
message bus
queue
LangGraph central orchestrator
auto-promoted memory
self-evolution auto-merge
heavy dashboard
free plugin manager
automatic skill installer
```
