# Evidence Topology Examples

Status: fictional examples — educational support for the active Evidence Topology contract.

These examples illustrate `docs/governance/EVIDENCE_TOPOLOGY.md` and the optional topology fields already present in the current Task Contract and Evidence Pack schemas.

They are not runtime prompts, professional advice, approval or authority.

```text
Hermes clients may expose runtime interaction.
Hermes Agent executes externally under Task Contract.
Pantheon Cockpit may expose governed topology/Evidence state.
Pantheon Next governs consequential status.
```

## Purpose

The examples show how to select and record a reasoning topology before external execution without treating orchestration as authority.

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

## Included examples

| File | Topology | Purpose |
|---|---|---|
| [`task_contract_single_primary_reasoning_context.yaml`](task_contract_single_primary_reasoning_context.yaml) | `single_primary_reasoning_context` | Fictitious enterprise ticket where Jira, code, XML config and design notes must be connected in one consolidated reasoning context. |
| [`task_contract_fanout_extract_then_single_synthesis.yaml`](task_contract_fanout_extract_then_single_synthesis.yaml) | `fanout_extract_then_single_synthesis` | Fictitious professional dossier where several sources can be extracted in parallel, but final reasoning remains consolidated. |
| [`task_contract_persistent_role_team_handoff.yaml`](task_contract_persistent_role_team_handoff.yaml) | `persistent_role_team_handoff` | Fictitious staged workflow where runtime continuity is useful but handoffs remain artifact-bound and gated. |
| [`evidence_pack_topology_examples.yaml`](evidence_pack_topology_examples.yaml) | Evidence Pack examples | Fictitious Evidence Packs showing Evidence Items, Handoff Artifacts, topology records and approval gaps. |

## Reading rule

Preserve these distinctions:

```text
source != Evidence
retrieval != truth
worker output != conclusion
handoff != approval
team chat != Evidence Pack
runtime role memory != governed memory
runtime state != Pantheon persistence
```

## Current contract status

The example concepts are backed by active optional fields in:

- `schemas/task_contract.schema.yaml` — `reasoning_topology`;
- `schemas/evidence_pack.schema.yaml` — `evidence_items`, `handoff_artifacts`, `reasoning_topology_record`.

Schema validation proves conformance to those shapes. It does not prove Evidence sufficiency, professional correctness, runtime adoption or approval.

## Not implemented by these examples

The examples do not themselves implement:

- execution or Hermes dispatch;
- a LangGraph/swarm runtime;
- agent-to-agent messaging;
- client/Cockpit UI;
- memory promotion;
- approval automation.

They are bounded fixtures for doctrine, schema validation and review.
