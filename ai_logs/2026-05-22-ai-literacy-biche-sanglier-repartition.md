# AI log — Biche / Sanglier repartition

Date: 2026-05-22

Scope:

- `docs/assets/ai-literacy/biche_scene_card.md`;
- `ai_logs/2026-05-22-ai-literacy-biche-sanglier-repartition.md`.

Type: documentation-only editorial correction.

## Change

Revised the Biche de Cerynie scene card to avoid overlap with the future Sanglier scene card.

The Biche had initially absorbed too much of the technical/contextual preparation layer, including context injection, RAG, sources, documents and skills.

The corrected repartition is now:

```text
Biche    = connaitre le modele / systeme que l'on sollicite.
Sanglier = cadrer le contexte, les pieces, le RAG, les sources et les skills a donner au systeme.
```

The Biche now focuses on:

- model and system predictability;
- typical behavior of the model;
- system instructions;
- generation parameters;
- simple vs tool-enabled mode;
- agentic mode or not;
- ability to act;
- degree of autonomy;
- expected status of the output.

Key retained formulas:

```text
Connaitre la machine qui ecoute.
Avant de demander, savoir quelle machine ecoute.
Le prompt formule. Le systeme transforme.
Une intention fragile ne se confie pas a une machine inconnue.
```

## Boundary

This is documentation only.

It does not add runtime behavior, agents, tools, workflow execution, provider routing, approval automation, memory promotion, OpenWebUI integration, Hermes integration or evidence automation.

The assets remain support material and must not be treated as canonical governance doctrine or implementation.

Doctrine preserved:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Limitation

The Sanglier scene card still needs to be created or refined to take over the contextual layer:

- raw dossier chaos;
- injected documents;
- RAG and retrieval settings;
- Knowledge Bases;
- source selection;
- skills relevant to the task;
- facts, hypotheses, risks, decisions, perimeter and exclusions.

No implementation claim is made.
