# 2026-07-26 — Tool Card contract and Hermes provenance

Status: validation-only intervention trace.

## Decision recorded

Pantheon Next keeps only the governance contract for Tool Cards. The concrete catalogue, cockpit card data/projection and Hermes/runtime inventory reconciliation implementation belong in `pantheon-mvp`.

The decision preserves:

```text
1. Tool cards need an operational description, not only name/icon/status.
2. Hermes-native inventory remains owned by Hermes.
3. Hermes-managed dynamic skills are normalized as hermes_dynamic_skill observations.
4. Pantheon may add independent pantheon_catalog candidates.
5. discovery != installation != health != approval != activation.
6. catalogue presence != install instruction.
7. runtime observation != governance approval.
8. Pantheon Next does not own the executable Tool Card store or UI.
```

## Current capability context

The merged `knowledge_retrieval_pipeline` doctrine remains a tool-agnostic Capability Slot. Haystack is a candidate only; LlamaIndex and LangChain remain comparison/watch bindings. This Tool Card contract does not select, install or activate any of them.

## Boundary classification

```text
Pantheon Next: governance contract, status distinctions, Capability Slot doctrine, evidence/scope/approval rules
pantheon-mvp: executable catalogue and cockpit card projection
Hermes: native discovery and execution mechanics
OpenWebUI/Cockpit: exposure surface
human: consequential adoption, installation, activation, update and use decisions
```

No runtime, dependency adoption, installation, activation or provider routing is introduced by this documentation.
