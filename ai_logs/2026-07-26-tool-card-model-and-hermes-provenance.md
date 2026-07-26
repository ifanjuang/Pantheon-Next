# 2026-07-26 — Tool Card contract and Hermes provenance

Status: validation-only intervention trace.

## Decision recorded

Pantheon Next keeps only the governance contract for Tool Cards. The concrete catalogue, card data model, cockpit code and Hermes inventory reconciliation implementation belong in the external `pantheon-mvp` repository.

The decision preserves:

```text
1. Tool cards require a detailed operational description, not only name/icon/status.
2. Hermes-native inventory remains owned by Hermes.
3. Skills discovered from Hermes-managed files/manifests are classified as hermes_dynamic_skill after adapter normalization.
4. Pantheon may add catalogue candidates independently as pantheon_catalog entries.
5. Dynamic discovery, installation, health, approval and activation remain separate state axes.
6. Catalogue presence is not an install instruction.
7. Runtime observation is not governance approval.
8. Pantheon Next does not own the executable Tool Card store or UI implementation.
```

## LangChain ecosystem

Capability placement remains in `HERMES_CAPABILITY_BINDINGS.md`. The concrete cockpit catalogue records for LangChain, LangGraph, LangFlow and LangSmith are delegated to `pantheon-mvp`.

No installation, dependency adoption, runtime activation or provider routing is introduced by the Next documentation.

## Boundary classification

```text
Pantheon Next: governance contract, status distinctions, Capability Slot doctrine, evidence/scope/approval rules
pantheon-mvp: executable catalogue and cockpit card projection
Hermes: native skill/tool/plugin/MCP/workflow discovery and execution mechanics
OpenWebUI/cockpit: exposure surface
human: consequential adoption, installation, activation, update and use decisions
```

## Repository effect

```text
candidate_document: docs/governance/TOOL_CARD_MODEL.md
authority_index_updated: docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
protected_paths_touched: no
runtime_changed: no
schema_changed: no
implementation_status_in_next: documented non-implemented
implementation_owner: external pantheon-mvp
```

This log is a dated human-requested design trace. It does not by itself promote the candidate document to canonical doctrine.
