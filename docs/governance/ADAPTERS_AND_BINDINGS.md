# Adapters and Bindings

Status: active support doctrine — blueprint-in-Pantheon and adapter-outside model for tool-specific configuration.

This document defines where tool-specific configuration lives and how it stays adapted to Pantheon without coupling Pantheon to any tool.

This document is part of the bindings and adapters exception. Because its subject is binding to specific tools, it may name selected or candidate products where the generic doctrine body would not. The bindings-registry rule and this exception are defined in `MODULAR_DOMAIN_REORIENTATION.md`.

It does not implement a configuration, a runtime-client component, a Hermes skill, a Langfuse project, a runtime, a bridge or any executable artifact.

Runtime/client/authority placement is inherited from `HERMES_INTEGRATION.md`: runtime clients are optional and replaceable interaction surfaces, Hermes Agent is the selected external execution runtime and PEP, Pantheon Cockpit is the governed projection surface, and Pantheon retains PDP/governance responsibility.

## Purpose

Using the strengths of Hermes, an optional compatible runtime client, Langfuse or any other tool requires real, runnable configuration. That configuration must not live inside Pantheon, but it must stay adapted to Pantheon.

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
- **Adapter (outside Pantheon):** the actual selected runtime-client component if any, the actual Hermes skill, the actual Langfuse project configuration. These are running things, adapted to Pantheon by conforming to its blueprints.

Pantheon defines the port. The adapter is what plugs into it.

## Kernel and adapters split

Pantheon has a stable kernel and a replaceable adapter layer.

```text
Kernel:   tool-agnostic doctrine, contracts, statuses, evidence, approvals,
          memory, scope and placement rules.
Adapter:  tool-specific projection, configuration, version compatibility and
          runtime capability mapping.
```

The kernel changes only when the abstract governance model changes.

An adapter changes when a bound tool changes its surfaces, permissions, runtime affordances, channels, memory behavior, profile model, skill system or automation features.

A tool update must not drag product-specific vocabulary into the framework body. It is handled as an adapter review unless it proves that the existing abstract model is insufficient.

| Change type | Lives in | Rule |
|---|---|---|
| New governance distinction | Pantheon kernel | update doctrine only if the distinction is tool-agnostic |
| New Hermes skill, profile, channel, subagent or blueprint feature | Hermes adapter / integration note | map to existing Task Contract, Evidence Pack, approval, memory and scope rules |
| New runtime-client action, template, form or interaction affordance | runtime-client adapter | expose runtime interaction only; do not create authority |
| New Pantheon Cockpit card or governed decision projection | Pantheon Cockpit implementation / projection contract | project governed state only; projection is not persistence or approval |
| New observability or trace capability | observability adapter | trace support only; not Evidence Pack or approval |
| New external tool connector | connector adapter | classify external effect, approval need, idempotency and scope |

The practical test is:

```text
Can the core rule be written without naming the tool?
```

If yes, it belongs in the kernel. If no, it belongs in a binding, adapter or reference review.

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

For example, a Hermes adapter is adapted when a new runtime feature such as background subagents, image editing, messaging channels, automation blueprints or memory batch operations is mapped to the existing Pantheon effects model before use. The feature may become powerful execution; it does not become proof, approval, memory or external-action authority.

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

## Version-change discipline

A bound tool update is classified before any adaptation work starts.

```text
version_change_review:
  tool:
  version:
  changed_surface:
  new_runtime_power:
  new_external_effect:
  new_memory_behavior:
  new_profile_or_skill_behavior:
  existing_kernel_rule:
  adapter_change_required:
  kernel_change_required: false by default
  status: accepted | refused | to_verify | to_arbitrate
```

Default decision:

```text
Tool update -> adapter review.
Kernel update -> only if the abstract governance model is missing a rule.
```

This prevents every Hermes, selected runtime-client, Langfuse or connector release from rewriting Pantheon doctrine while still allowing each tool to express its full power behind the governed boundary.

## Relationship to existing structure

```text
templates/                  -> blueprints in Pantheon, non-executable.
bindings registry           -> current selected/candidate bindings in
                               MODULAR_DOMAIN_REORIENTATION.md.
adapters (outside Pantheon) -> the real configurations that conform to the blueprints.
```

The `templates/` directory is the blueprint layer. The bindings registry maps abstract roles to current selected or candidate tools without making an optional client mandatory. Adapters are the built configurations that realize a blueprint for a specific tool, and they live outside this repository.

## Boundary phrase

```text
The kernel governs without depending on the tool.
The blueprint lives in Pantheon.
The adapter lives in the tool.
The dependency always points to Pantheon.
The validated remains.
```
