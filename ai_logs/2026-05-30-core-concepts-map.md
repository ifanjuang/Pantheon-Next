# AI Log — Core Concepts Map

Date: 2026-05-30

## Context

The user identified that Pantheon Next now has enough doctrine layers and should consolidate before adding new external references.

The risk was doctrine sprawl: many coherent documents existed, but the relationships between Task Contracts, Context Packs, Evidence Packs, approvals, memory, roles, rites, domains, skills, modules, Effective Policy, OpenWebUI Templates and external references needed a stable navigation map.

## Action

Created:

```text
docs/governance/CORE_CONCEPTS_MAP.md
```

Updated:

```text
README.md
docs/governance/README.md
docs/governance/STATUS.md
CHANGELOG.md
```

## Doctrine added

`CORE_CONCEPTS_MAP.md` provides:

- one-line doctrine for the core flow;
- minimal dossier flow;
- object map;
- authority ladder;
- execution ladder;
- role and rite map;
- domain and skill map;
- module and Effective Policy map;
- OpenWebUI map;
- Hermes map;
- User Decision Gate map;
- external reference map;
- high-risk shortcut list;
- stable reading path.

Central rule:

```text
Every concept has one job.
Every promotion requires governance.
Every external action requires a boundary.
Every unresolved tension must remain visible.
```

## Boundary preserved

This intervention did not implement:

- schema;
- runtime model;
- workflow engine;
- module registry;
- plugin manager;
- approval engine;
- memory engine;
- OpenWebUI UI;
- Hermes integration;
- tests;
- operations tooling;
- automatic approval;
- automatic memory promotion.

## Status impact

Pantheon Next now has a compact doctrine navigation map to reduce sprawl while preserving:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The map should be read before adding new conceptual layers or external reference reviews.