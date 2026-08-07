# Agent Plugins interoperability

Status: candidate external-interoperability review — documented, not implemented, installed, activated or task-authorized.
Boundary profile: external_reference_review.
Reviewed specification: Agent Plugins 1.0.0 Working Draft.
Reviewed Hermes target: Hermes Agent 0.20.0, as already recorded by `HERMES_RUNTIME_SURFACE_REVIEW.md`.

## Purpose

This document classifies the Agent Plugins specification against Pantheon Next's existing governance and Hermes boundaries.

It does not create a Pantheon plugin format, plugin manager, installer, runtime, registry, package resolver, MCP runtime, skill runtime or approval mechanism.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The objective is convergence: reuse a portable external package format where it fits, while keeping Pantheon concepts authoritative and tool-agnostic.

## Reviewed upstream contract

Upstream source reviewed on 2026-08-07:

```text
specification: https://agent-plugins.org/specification
spec_version: 1.0.0
status: Working Draft
portable_manifest: plugin.json
portable_component_types:
  - Agent Skills under skills/*/SKILL.md
  - MCP servers declared in mcp.json
```

The normative specification defines a `Client` as the tool that discovers, installs, loads and executes plugin components. Agent Skills remain governed by the Agent Skills specification; Agent Plugins only defines their fixed discovery location. MCP wire behavior remains governed by MCP; Agent Plugins defines the portable `mcp.json` configuration that a client maps into its native configuration.

This places the Agent Plugins client responsibility in the execution/runtime layer, not in Pantheon governance.

## Canonical placement

```text
Agent Plugin package
        |
        v
external portable packaging
        |
        v
Hermes-side client / installer / translator candidate
        |
        v
existing Pantheon capability and binding governance
        |
        v
OpenWebUI / Cockpit exposure and human decision
```

Pantheon must not become an Agent Plugins conformant runtime merely to govern packages that another runtime can consume.

The existing responsibility split remains sufficient:

```text
Agent Plugins -> describes and packages portable runtime components
Hermes        -> discovers / installs / maps / loads / executes runtime components
Pantheon      -> governs eligibility, scope, binding legitimacy, approval and Evidence status
OpenWebUI     -> exposes state, warnings and decision surfaces
human         -> decides consequential effects
```

## Mapping to existing Pantheon concepts

Agent Plugins introduces no missing Pantheon authority object.

| Agent Plugins surface | Pantheon interpretation | Required posture |
|---|---|---|
| plugin package | external capability package candidate | preserve source, version and observed package identity; no automatic adoption |
| `plugin.json` | external package metadata | metadata only; never a Capability Passport or authorization record |
| `skills/*/SKILL.md` | runtime skill candidates | Hermes-side skill surface; consequential use remains bounded by Task Contract and scope |
| `mcp.json` | portable MCP binding declaration | candidate runtime bindings; tool availability does not authorize use |
| MCP server entry | candidate concrete binding | qualify exact effects, target, permissions and failure posture before consequential use |
| client extension namespace | client-specific runtime metadata | keep outside Pantheon kernel unless a tool-agnostic governance distinction is demonstrated |
| `PLUGIN_ROOT` | runtime package location | runtime state only; not Pantheon memory or provenance by itself |
| `PLUGIN_DATA` | client-managed persistent runtime data | runtime state only; never canonical memory, Evidence or approval state |

The preferred convergence path is therefore:

```text
plugin.json / skills / mcp.json
        -> external observation
        -> candidate capability bindings
        -> existing Capability Slot / passport / Task Contract machinery
        -> governed execution handoff
        -> Result Candidate / Evidence Pack Candidate
```

No `PantheonPlugin`, `PantheonPluginManifest` or parallel plugin lifecycle is justified by the reviewed specification.

## Required non-equivalences

```text
plugin discovered != plugin adopted
plugin installed != capability approved
manifest valid != package trusted
skill present != skill authorized
MCP server declared != MCP server selected
MCP server reachable != MCP tool authorized
binding selected != dependency adopted
runtime scan passed != safe for professional data
runtime success != Evidence
PLUGIN_DATA persisted != Pantheon memory
client extension present != Pantheon authority
```

These are applications of existing Pantheon invariants, not new kernel rules.

## Manifest boundary

Agent Plugins 1.0.0 uses a closed root `plugin.json` schema. Client-specific metadata belongs under namespaced `extensions`; unknown root fields must not acquire semantics.

Pantheon governance fields therefore must not be added to the portable root manifest.

Forbidden convergence pattern:

```text
plugin.json
  approved: true
  pantheon_scope: ...
  evidence_level: ...
  authorization: ...
```

Preferred pattern:

```text
portable plugin metadata
        +
separate Pantheon-side observation / qualification / binding records
```

A future Pantheon-specific Agent Plugins extension namespace is not required by the current need. It should be introduced only if a concrete client-side interoperability requirement cannot be represented through existing Pantheon records without duplicating authority into the package.

## Security boundary

Agent Plugins constrains package-relative paths to the plugin root, but the specification explicitly does not sandbox plugin subprocesses or runtime-supplied paths.

For Pantheon this means:

```text
package containment != process sandbox
valid stdio command != safe command
valid remote MCP URL != approved external destination
configured header != secret mechanism
transport supported != transport authorized
```

Agent Plugins v1 also does not define portable OAuth configuration or portable credential-reference fields. Credential discovery, storage and authorization remain client responsibilities.

Therefore secrets, credentials, network exposure, subprocess sandboxing, installation integrity, update policy and rollback remain Hermes/deployment concerns governed by existing Pantheon eligibility and external-effect rules; they must not be absorbed into `plugin.json`.

## Failure isolation

The specification deliberately separates failure boundaries: an invalid skill can be skipped while other components continue; an invalid MCP server entry can be rejected without invalidating unrelated servers; an absent component location is not itself a plugin error.

Pantheon should preserve that granularity rather than projecting a single coarse `plugin healthy` state.

Preferred observation shape is conceptual, not a new canonical schema:

```text
package_observed
manifest_valid
skills:
  valid / invalid / unavailable
mcp_servers:
  valid / invalid / unreachable / unauthorized
capability_gaps
```

A package-level health label must not collapse component validity, runtime reachability, security qualification, governance approval and task authorization.

## Hermes 0.20.0 fit

`HERMES_RUNTIME_SURFACE_REVIEW.md` already reviews Hermes Agent 0.20.0 and classifies MCP and plugin surfaces as replaceable execution bindings. It also concludes:

```text
kernel_change_required: false
run_binding_change_required: false
```

That existing conclusion remains valid for Agent Plugins.

Hermes already has first-class skill and MCP management surfaces. The upstream Microsoft APM project also documents an experimental Hermes target that deploys Agent Skills into Hermes skill locations and writes MCP servers into Hermes `mcp_servers` configuration. This is evidence that portable-to-Hermes translation can remain outside Pantheon; it is not evidence that Agent Plugins itself is natively supported by Hermes or that APM is adopted.

Observed external compatibility evidence therefore supports this sequence:

```text
1. do not change Pantheon kernel;
2. do not create a Pantheon plugin manager;
3. prefer an external Agent Plugins -> Hermes mapping when needed;
4. qualify the resulting Hermes skill/MCP binding through existing Pantheon governance;
5. require a real-instance observation before claiming operational compatibility.
```

## Adapter decision

Current decision:

```text
agent_plugins_specification: 1.0.0-working-draft
placement: external interoperability format candidate
pantheon_kernel_change_required: false
pantheon_schema_change_required: false
pantheon_plugin_registry_required: false
pantheon_installer_required: false
hermes_runtime_adapter_required: not demonstrated
external_translation_or_client_support: candidate / to verify
real_instance_observation_required: true
installation_effect: none
activation_effect: none
task_authorization_effect: none
```

An Agent Plugins-specific adapter becomes justified only if a real package cannot be represented by Hermes's existing Agent Skills and MCP configuration surfaces without losing a material capability or provenance distinction.

Until such a gap is demonstrated, adding an adapter would be speculative duplication.

## Minimum future acceptance test

Before claiming that Agent Plugins is operationally consumable in the Pantheon/Hermes stack, use one synthetic package containing one harmless Agent Skill and one read-only MCP server, then verify:

1. the exact package source, version and digest are recorded;
2. the manifest and component schemas validate at the pinned Agent Plugins version;
3. the skill maps to Hermes without changing Pantheon doctrine or schemas;
4. the MCP server maps to Hermes without embedding credentials in package metadata;
5. Hermes exposes only the expected read-only tools;
6. Pantheon still requires the existing Task Contract / capability admission path for consequential use;
7. component failure remains isolated and visible as a Capability Gap;
8. runtime output returns as candidate output / candidate evidence only;
9. uninstall or rollback removes runtime availability without mutating Pantheon canonical state.

Synthetic acceptance is deliberately postponed until an actual Agent Plugins-to-Hermes client or translator is selected. No custom adapter should be written merely to make this test possible.

## Decision

Accepted with constraints as an external interoperability format candidate.

Accepted:

```text
portable packaging concept
Agent Skills reuse
portable MCP configuration concept
failure isolation
client-owned runtime translation
```

Refused:

```text
Agent Plugins as Pantheon runtime
Agent Plugins as Pantheon governance authority
Pantheon-owned plugin installer or plugin manager
root plugin.json governance fields
automatic capability adoption from package presence
automatic authorization from installation or health
```

To verify:

```text
native Hermes 0.20.0 Agent Plugins package support
candidate external translator/client behavior
one synthetic package acceptance run
supply-chain and rollback posture of the selected client
```

## Relationship to existing doctrine

This review specializes but does not override:

- `CAPABILITY_PLACEMENT.md`;
- `ADAPTERS_AND_BINDINGS.md`;
- `HERMES_INTEGRATION.md`;
- `HERMES_RUNTIME_SURFACE_REVIEW.md`;
- `EXTERNAL_TOOL_PLACEMENT_REGISTER.md`;
- `EXTERNAL_TOOLS_POLICY.md`.

If any statement here conflicts with those authorities, the existing canonical governance documents win.
