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

## Conceptual dimensions

The project can also be understood through four abstract dimensions.

These dimensions are philosophical and conceptual only. They are not runtime layers, not implementation modules, not APIs and not code boundaries.

They exist to explain how Pantheon Next structures space, continuity, transformation and visibility.

### Structure — Topos

Pantheon spatializes the system.

It defines:
- roles,
- boundaries,
- approvals,
- permissions,
- constraints,
- domains,
- allowed and forbidden transitions.

Topos represents the structured space in which governed actions are allowed to exist.

### Persistence — Chronos

Pantheon temporalizes the system.

It preserves continuity through:
- Evidence Packs,
- Task Contracts,
- revisions,
- approvals,
- memory candidates,
- audit trails,
- governance history.

Chronos represents persistence through time.

Pantheon does not only store information. It preserves responsibility, traceability and continuity.

### Transformation — Poiesis

Hermes Agent transforms the system.

It converts:
- requests into actions,
- context into outputs,
- analysis into operational artifacts,
- tasks into governed evidence.

Poiesis represents transformation and operational becoming.

Pantheon Next does not perform Poiesis itself.

### Manifestation — Aletheia

OpenWebUI manifests the system.

It exposes:
- results,
- validations,
- knowledge,
- Evidence Packs,
- reviews,
- human interactions.

Aletheia represents visibility and unveiling.

It is the dimension through which the system becomes interpretable and accessible to humans.

## Repository baseline

This repository is the clean Pantheon Next governance baseline extracted from the historical Pantheon OS repository. It is governance-first.

Historical runtime-oriented folders are not migrated by default. They must be classified before reuse.

For the authoritative state of every governance document and Hermes profile, see `docs/governance/STATUS.md`.

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
docs/governance/   canonical governance Markdown
hermes/profiles/   lightweight Hermes profile templates (candidate-only, not installed)
ai_logs/           AI intervention logs
legacy/            pointer to Pantheon-OS historical source
schemas/           declarative governance validation contracts
```

Planned but not implemented yet (tracked in `STATUS.md`): `operations/`, `tests/`, `docs/assets/`.

## Hermes profile doctrine

Hermes profiles under `hermes/profiles/` are lightweight templates only.

They are candidate-only execution profiles aligned with Pantheon Roles defined in `docs/governance/AGENTS.md`.

Pantheon Next does not install Hermes profiles, does not deploy them and does not execute them. A profile template never governs, never approves, never canonizes memory and never merges code.

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
