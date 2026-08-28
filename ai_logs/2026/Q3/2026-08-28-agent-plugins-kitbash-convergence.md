# Agent Plugins / Kitbash convergence — 2026-08-28

## Objective

Revalidate issue #673 and the active Agent Plugins interoperability owner against current repository and upstream state, then avoid introducing a compiler/runtime dependency unless a distinct multi-client responsibility is demonstrated.

## Repository state

Slice base: Pantheon-Next `main` at `66f387c027f5a0334686674f381ef14a4bb04f86`.

Observed current repository facts:

- `docs/governance/AGENT_PLUGINS_INTEROPERABILITY.md` still described Agent Plugins 1.0.0 as a Working Draft and assigned exposure/decision responsibility to OpenWebUI.
- current architecture instead separates Hermes Web/dashboard runtime interaction, Hermes Agent execution, Pantheon Cockpit governed projection and Pantheon Next authority.
- the repository already has an executable candidate Agent Plugin package seam under `implementation/mvp_vertical/agent_plugin_package.py`; its existence does not establish installation, adoption or external-runtime support.
- no open issue other than #673 demonstrates a concrete requirement to compile one Skill source into several agent-client formats.
- #673 itself requires testing Kitbash only if a concrete multi-agent need exists and explicitly allows closure without adoption when native Agent Skills / Agent Plugins paths suffice.

## Upstream revalidation

Revalidated 2026-08-28:

- Agent Plugins specification remains version `1.0.0` but its current status is `Published`, not `Working Draft`.
- current Hermes upstream exposes first-class Skills, MCP and plugin surfaces.
- current Kitbash upstream remains a multi-target compiler and supports an opt-in Agent Plugins v1 target.

These facts support interoperability as an external format while weakening, not strengthening, the case for a Pantheon-specific compiler/adapter.

## Convergence decision

```text
Agent Plugins = accepted external interoperability format
Hermes native Skill/MCP/plugin surfaces = preferred runtime-side path
Kitbash = useful optional external tooling, not selected
Pantheon Kitbash adapter = not justified
Pantheon plugin manager = refused
```

No distinct multi-client compilation responsibility is currently demonstrated. Therefore introducing Kitbash now would add a dependency and a parallel transformation path for an unproven need.

## Preserved boundaries

```text
plugin discovered != plugin adopted
plugin installed != capability approved
compiled != authorized
portable package emitted != plugin adopted
MCP declared != MCP tool authorized
provider selected != authority transfer
runtime success != Evidence
projection != persistence
```

## Changes

- update `AGENT_PLUGINS_INTEROPERABILITY.md` to the published Agent Plugins 1.0.0 state;
- remove active OpenWebUI ownership from that review;
- make the Hermes 0.20.0 observation explicitly historical rather than a current runtime claim;
- record current native Hermes Skills/MCP/plugins as runtime-side surfaces without claiming Agent Plugins conformance;
- document Kitbash as optional need-driven tooling rather than a selected binding;
- extend the existing OpenWebUI retirement regression test to protect this active owner.

## Finish criteria

- Governance CI / Architecture Audit / Obsolete Authority checks green on exact PR head;
- no review finding left unresolved;
- #673 closed without adoption after merge, with reopening/re-evaluation only if a concrete multi-client portability requirement appears.
