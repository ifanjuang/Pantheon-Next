# AI log — Architectural Project Graph candidate orientation

Date: 2026-06-21
Repository: `ifanjuang/Pantheon-Next`

## Request

User asked to record the architectural project graph orientation on Git.

The request combines earlier discussion about:

- building anatomy / project knowledge graph;
- evidence graph;
- runtime memory graph;
- GraphRAG as candidate relation generator;
- buildingSMART / IFC as adapter, not central model;
- non-BIM sources such as PDF, JPG, sketches, renderings and photos;
- no duplication between building anatomy, evidence and memory;
- decision as firm latest status of an evidence object;
- unified graph view with project selector and toggles;
- color modes by topic, zone, decision date, trade, status or object type;
- visual grammar for memory, evidence and anatomy nodes.

## Files read before creation

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`

## Search performed

Searched repository for existing equivalent material using:

```text
architectural project graph anatomy evidence memory graph
```

No direct equivalent was found.

## Created

- `docs/governance/ARCHITECTURAL_PROJECT_GRAPH.md`

## Status

Candidate orientation.

Documented non-implemented.

## Boundary preserved

No protected path changed.

No schema changed.

No test changed.

No runtime created.

No graph database created.

No vector database created.

No IFC parser created.

No GraphRAG runtime created.

No memory engine created.

No approval engine created.

No evidence register write created.

No external action created.

## Important note

`AUTHORITY_INDEX.md` was read, but not updated in this pass because the connector response was truncated and a full-file rewrite would risk accidental loss of unrelated index content.

The created document itself declares its candidate status and non-implementation boundary.

A later safe index update should add:

```md
| `docs/governance/ARCHITECTURAL_PROJECT_GRAPH.md` | candidate support doctrine | documented non-implemented | Candidate orientation for a unified architecture project graph: building anatomy, evidence/status graph and runtime memory diagnostics; buildingSMART/IFC and GraphRAG are adapters/candidate generators, not authorities. No runtime. |
```

## Doctrine retained

```text
The building graph explains the project anatomy.
The evidence graph qualifies assertions and decisions.
The memory graph shows external runtime recall.
The status view records the latest governed state.
GraphRAG may propose.
IFC may structure.
Hermes may execute.
Pantheon governs.
The human decides.
```
