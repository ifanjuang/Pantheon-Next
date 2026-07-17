# MCP consultation contract and bounded architecture explanations

Date: 2026-07-15

Status: implemented read-only / partial — validation-only trace.
Boundary profile: validation_only_trace.

## Change

- Added a transport-neutral `pantheon.consultation.v1` response contract with
  repository version and per-source content fingerprints.
- Added MCP tools for an honest consultation catalog, allowlisted architecture
  explanations and qualification of caller-provided capability-status candidates.
- Rebased on the native Hermes dashboard merges and aligned qualification with
  its nine state axes. The external dashboard plugin remains the observation
  producer; the MCP performs no duplicate inventory or probe.
- Expanded the governed MCP source map for architecture, capability, control,
  Hermes, OpenWebUI, knowledge, memory, retrieval and runtime-status sources.
- Fixed authority labeling so the MCP reads the master authority index plus only
  the sub-indexes registered by that master.
- Added focused tests and aligned MCP, Hermes-integration and repository-status
  documentation.
- Extended the native Hermes MCP candidate allowlist with the three bounded
  consultation tools while preserving disabled resources, prompts and sampling.

## Why

Hermes and other MCP clients need a shared, citeable explanation of where a
component belongs and why. Pantheon Control also needs status axes that do not
collapse listing, detection, installation, configuration, enablement,
reachability, health, governance and task use. The same pure logic can
later be projected by a bounded HTTP adapter without claiming that such an API,
MCP-side runtime inventory or private knowledge retrieval exists today.

## Evidence

```text
focused consultation tests: 11 passed
full MCP unittest suite: 157 passed
real MCP stdio list/call consultation smoke test: passed
root pytest suite: 33 passed
Governance Doctor: pass; 6/6 checks and 552/552 items evaluated and passed
status headers, internal links, index coverage, axis vocabulary: passed
register, vertical-slice, APU, catalog and handoff guards: passed
packaging contract (non-distributable root / MCP metadata / VERSION / CHANGELOG):
0.1.62, passed
runtime probe performed by new tools: no
HTTP API implemented: no
remote MCP implemented: no
knowledge / Mem0 / Memvid retrieval implemented: no
```

## Boundary

Protected paths touched: yes (`mcp-server/`, `mcp-server/tests/`, packaging metadata).
Runtime impact: read-only stdio MCP tool surface only.
Authority impact: none; projections cite sources and retain their declared status.
Schema/test/CI impact: focused tests added; no schema or CI change.
External action: none.
Memory behavior: none.

## Local distinctions

```text
connected != consulted
consulted != obeyed
reported status != runtime probe
listed != installed
configured != enabled
governance_eligible != task_authorized
installed != approved
retrieved != evidence
transport contract != HTTP service
qualified candidate != authorized capability
```
