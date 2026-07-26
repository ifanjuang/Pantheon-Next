# 2026-07-26 — Tool Card model and Hermes provenance

Status: validation-only intervention trace.

## Decision recorded

A dedicated candidate Tool Card grammar is added for cockpit representation of tools, skills, plugins, functions, MCP bindings and adjacent runtime capabilities.

The change records the following design decisions:

```text
1. Tool cards require a detailed operational description, not only name/icon/status.
2. Tool/card data is expected to be data-driven rather than hard-coded in React.
3. Hermes-native inventory remains owned by Hermes.
4. Skills discovered from Hermes-managed files/manifests are classified as hermes_dynamic_skill.
5. Pantheon may add catalogue candidates independently as pantheon_catalog entries.
6. Dynamic discovery, installation, health, approval and activation remain separate state axes.
7. Catalogue presence is not an install instruction.
8. Runtime observation is not governance approval.
```

## Initial catalogue additions

The candidate Tool Card document records explicit placement for:

```text
LangChain
LangGraph
LangFlow
LangSmith
```

They are catalogue candidates / references only. No installation, dependency adoption, runtime activation or provider routing is introduced.

## Boundary classification

```text
exposed_by: cockpit / OpenWebUI projection where applicable
executed_by: Hermes or another explicitly adopted external runtime
owned operationally by: native runtime / upstream tool
Pantheon governs: classification, scope, evidence, approval, lifecycle and activation decisions
human approves: adoption and consequential activation/update where applicable
forbidden: treating discovery, install, health, trace or catalogue presence as approval/evidence
```

## Repository effect

```text
new_candidate_document: docs/governance/TOOL_CARD_MODEL.md
authority_index_updated: docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
protected_paths_touched: no
runtime_changed: no
schema_changed: no
implementation_status: documented non-implemented
```

This log is a dated human-requested design trace. It does not by itself promote the candidate document to canonical doctrine.
