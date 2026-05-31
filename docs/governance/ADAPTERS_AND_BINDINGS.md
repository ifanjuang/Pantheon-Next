# Adapters and Bindings

Status: active support doctrine — blueprint-in-Pantheon and adapter-outside model for tool-specific configuration.

This document defines where tool-specific configuration lives and how it stays adapted to Pantheon without coupling Pantheon to any tool.

It does not implement a configuration, an OpenWebUI Function, a Hermes skill, a Langfuse project, a runtime, a bridge or any executable artifact.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Using the strengths of OpenWebUI, Hermes, Langfuse or any other tool requires real, runnable configuration. That configuration must not live inside Pantheon, but it must stay adapted to Pantheon.

This document answers one question:

```text
Where do tool-specific templates and configurations live, and how do they stay adapted to Pantheon?
```

## The two halves

A capability has two halves that must not be confused.

```text
Blueprint  -> lives in Pantheon as a non-executable template or rule.
Adapter    -> lives outside Pantheon as the real, runnable configuration.
```

- **Blueprint (in Pantheon):** the manifest shape, the envelope, the contract shapes, the domain-pack rules and the non-executable templates under `templates/`. These are plans, not running things.
- **Adapter (outside Pantheon):** the actual OpenWebUI Function, the actual Hermes skill, the actual Langfuse project configuration. These are running things, adapted to Pantheon by conforming to its blueprints.

Pantheon defines the port. The adapter is what plugs into it.

## Why adapters live outside

Pantheon must not hold runtime or executable configuration. The prohibitions in `CLAUDE.md` constrain the Pantheon repository.

Therefore the real configuration belongs in the tool's own repository or in a dedicated adapters repository, never in Pantheon.

Having adapted configurations outside Pantheon is the correct way to use a tool's power while staying governed. It is not a boundary violation; it is the boundary working as intended.

## What "adapted to Pantheon" means

An adapter is adapted to Pantheon when:

```text
it declares a manifest conformant to the Pantheon manifest shape;
it speaks the envelope (Task Contract in, candidate plus Evidence Pack out);
it carries Pantheon governance identifiers where relevant;
it targets a stated version of the Pantheon contract or manifest.
```

For example, a Langfuse adapter is adapted when its trace metadata carries `task_contract_id`, `evidence_pack_id` and candidate status, so traces are linkable to governance artifacts. The trace never becomes an Evidence Pack.

## The four disciplines

```text
1. Dependency direction: adapters depend on Pantheon contracts, never the reverse.
   Pantheon never references a specific tool configuration.
2. Conformance, not duplication: an adapter references the manifest and envelope;
   it does not restate the rules. Domain rules stay in the Pantheon domain pack.
3. Stated target version: each adapter declares which Pantheon contract or manifest
   version it targets, so contract bumps reveal which adapters need updating.
4. Single source of truth: the rule lives once in Pantheon; the configuration lives
   per tool outside. Different things, so no duplication, as long as the adapter
   references rather than restates.
```

## Relationship to existing structure

```text
templates/                 -> blueprints in Pantheon, non-executable.
bindings registry          -> the only place a tool is named, in
                              MODULAR_DOMAIN_REORIENTATION.md.
adapters (outside Pantheon) -> the real configurations that conform to the blueprints.
```

The `templates/` directory is the blueprint layer. The bindings registry maps abstract roles to current tools. Adapters are the built configurations that realize a blueprint for a specific tool, and they live outside this repository.

## Boundary phrase

```text
The blueprint lives in Pantheon.
The adapter lives in the tool.
The dependency always points to Pantheon.
The validated remains.
```
