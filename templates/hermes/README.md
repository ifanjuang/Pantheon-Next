# Hermes Templates

Status: external Hermes integration templates — inactive in Pantheon Next.

This directory contains candidate templates for future Hermes execution handoffs, returns and skill candidates.

They are not installed Hermes profiles, skills, tools or toolsets. The
pre-built browser bundle under `dashboard-plugins/pantheon-modules/` is an
installable Hermes dashboard-only plugin template; it executes only after an
external operator installs and enables it in Hermes.

Nothing in this directory executes inside Pantheon Next by its presence here.

## Placement

Hermes may execute under Task Contract and return candidates.

Hermes must not approve, canonize memory, mutate doctrine, merge directly or bypass approvals.

## First template classes

```text
connection/ candidate fragments for external Hermes configuration
dashboard-plugins/ installable external Hermes dashboard extensions
handoffs/   future Task Contract and Context Pack input envelopes
returns/    future candidate return envelopes
skills/     future skill candidate declarations
```

## Pantheon Modules dashboard plugin

`dashboard-plugins/pantheon-modules/` reads the native Hermes memory, MCP and
plugin inventories and presents their states without collapsing operational
enablement into governance activation or task authorization.

It includes explicitly confirmed Hermes-native controls for ready memory
providers, reviewed MCP catalog entries and installed plugins. It has no
Pantheon backend and retains no credentials. See its local `README.md` for the
review-first install sequence and the Mem0, n8n, LangGraph and Memvid
placements.

## Pantheon policy/wiki MCP connection

`connection/pantheon_policy_mcp.template.yaml` is a native Hermes Agent
`~/.hermes/config.yaml` fragment, aligned with the upstream `mcp_servers`
schema documented on 2026-07-15.

It deliberately exposes only the three read-only navigation tools needed for
the on-demand governance wiki:

```text
list_sources
read_doctrine
explain_governance_structure
```

The fragment is not installed, activated or approved by its presence here. An
external operator must install the `mcp-server/` distribution, mount the
Pantheon checkout read-only, adapt the absolute executable path, merge the
fragment into the real Hermes config and verify discovery. Sampling and MCP
resource/prompt wrappers are disabled; parallel calls are allowed because the
three included tools are read-only.

## Loop candidate templates

Loop candidate templates apply `docs/governance/LOOP_GOVERNANCE_MODEL.md` to Hermes-side handoffs and returns.

```text
handoffs/loop_contract_candidate.json
returns/loop_result_candidate.json
```

They are governance-readable examples, not executable schemas.

Runnable loop mechanics, retry state, queues, checkpoints and tool calls remain in Hermes or another execution runtime.

Pantheon governs admissibility, scope, evidence, blockers, gates and status.

## Rule

Hermes done does not mean Pantheon validated.
