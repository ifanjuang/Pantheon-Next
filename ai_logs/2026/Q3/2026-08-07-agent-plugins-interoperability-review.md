# Agent Plugins interoperability review

Date: 2026-08-07
Status: documented external-interoperability review; no runtime, installation, activation or authorization effect.
Scope: `docs/governance/AGENT_PLUGINS_INTEROPERABILITY.md`.

## Objective

Evaluate Agent Plugins 1.0.0 against the current Pantheon Next / Hermes boundary without introducing a parallel plugin abstraction or runtime responsibility.

## Repository state checked

The review started from `Pantheon-Next/main` at:

```text
0da3cffcda288a26f62cf2e01b7358268ce054c1
```

Relevant existing doctrine was checked before the change, including:

```text
CLAUDE.md
CAPABILITY_PLACEMENT.md
HERMES_INTEGRATION.md
HERMES_RUNTIME_SURFACE_REVIEW.md
EXTERNAL_TOOL_PLACEMENT_REGISTER.md
```

The current Hermes runtime review already targets Hermes Agent 0.20.0 and already classifies MCP and plugin surfaces as replaceable execution bindings. It concludes that no Pantheon kernel change or run-binding change is required for the reviewed 0.20.0 surface.

No existing Agent Plugins-specific review, branch or package-format implementation was found.

## External state checked

Agent Plugins specification observed on 2026-08-07:

```text
version: 1.0.0
status: Working Draft
manifest: plugin.json
component types: Agent Skills + MCP servers
skill location: skills/*/SKILL.md
MCP location: mcp.json
client responsibility: discover / install / load / execute plugin components
```

The specification keeps Agent Skills under the Agent Skills standard and MCP wire semantics under MCP. Agent Plugins standardizes packaging and portable MCP configuration; it does not define Pantheon-style approval, Evidence, memory promotion or task authorization.

A separate upstream compatibility signal was also observed: Microsoft APM documents an experimental Hermes target that deploys Agent Skills to Hermes skill locations and compiles MCP server configuration into Hermes's native `mcp_servers` block. This supports keeping translation outside Pantheon, but does not prove native Hermes Agent Plugins support and does not imply APM adoption.

## Decision

Add one bounded interoperability review rather than a new Pantheon plugin model.

```text
Agent Plugins -> external portable package format
Hermes / external translator -> client-side mapping and execution
Pantheon -> existing capability, scope, approval and Evidence governance
OpenWebUI / Cockpit -> exposure and human decision
```

No new `PantheonPlugin`, plugin registry, installer, schema, Capability Slot type or authorization state is introduced.

The review explicitly preserves:

```text
plugin installed != capability approved
manifest valid != package trusted
MCP declared != MCP authorized
binding selected != dependency adopted
runtime success != Evidence
PLUGIN_DATA persisted != Pantheon memory
```

## Plan result

Completed:

- verified the current repository and Hermes 0.20.0 review state;
- verified the upstream Agent Plugins 1.0.0 Working Draft contract;
- checked that the need is covered by existing Pantheon capability/binding concepts;
- documented the external-format placement and failure/security boundaries;
- defined the condition under which a future adapter would actually become justified;
- defined a synthetic future acceptance test without implementing it.

Not performed by design:

- no Pantheon schema change;
- no `pantheon-mvp` change;
- no Hermes package installation;
- no plugin manager or adapter implementation;
- no Agent Plugins package creation;
- no synthetic runtime acceptance run;
- no adoption of Microsoft APM or another translator.

## Conclusion

The architectural question is closed for the current evidence: Agent Plugins is accepted with constraints as an external interoperability format candidate. A custom adapter remains unjustified until a real Hermes mapping gap is demonstrated.
