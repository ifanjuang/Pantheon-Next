# Pantheon Next

Pantheon Next est une couche de gouvernance déclarative pour systèmes agentiques.

Pantheon Next peut aussi se lire comme une cité-jeu des décisions fiables : une cité antique gouvernée, construite au cœur d’un monde de possibles.

L’utilisateur n’est pas spectateur. Il est le joueur.

Il entre dans la cité avec une intention, des sources, un dossier, un problème ou une décision à préparer. Il choisit une quête, convoque des compagnons, explore des connaissances, fabrique un livrable, vérifie les preuves, puis décide ce qui peut rejoindre la mémoire.

```text
L’IA ouvre les possibles.
Pantheon les organise.
L’humain décide.
Le validé reste.
```

Cette métaphore est narrative et pédagogique.

Elle n’est pas un modèle d’exécution.

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
1. Role
2. Policy
3. Contract
4. Evidence
5. Approval
6. Context
7. Memory Candidate
```

Workflow Manifests and Skill Manifests may exist as governed declarations, but they are not runtime primitives.

## Repository map

```text
docs/governance/   canonical governance Markdown, narrative and visual doctrine
hermes/profiles/   lightweight Hermes profile templates (candidate-only, not installed)
ai_logs/           AI intervention logs
legacy/            pointer to Pantheon-OS historical source
schemas/           declarative governance validation contracts
docs/assets/       assets registry stub, not yet migrated
```

Planned but not implemented yet (tracked in `STATUS.md`): `operations/`, `tests/`.

## Narrative and visual layer

The narrative layer is documented in:

- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`.

These documents explain the city-game metaphor and its visual grammar.

They do not introduce runtime behavior.

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
