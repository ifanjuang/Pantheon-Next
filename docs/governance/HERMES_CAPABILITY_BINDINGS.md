# Hermes Capability Bindings

Status: candidate support doctrine — product-specific optional binding registry.

Machine-checkable selection, activation and compatibility relations remain owned by the existing `CapabilityBinding`, `CapabilityActivation` and `CapabilityCompatibilityObservation` contracts.

This document answers one narrow question:

```text
When Hermes needs a capability that its native runtime does not already satisfy,
which external implementations are worth selecting or testing?
```

It does not install, activate, authorize or route providers.

## Core rule

```text
Hermes native capability sufficient
-> use it
-> no external binding required

capability gap demonstrated
-> select one primary external binding for that function
-> qualify it
-> activate only through existing governance
```

```text
reviewed != selected
selected != installed
installed != activated
activated != task-authorized
runtime success != Evidence
provider selected != Pantheon dependency
```

Pantheon should not add a product merely to make the architecture look complete.

## Binding posture

Use `unbound` whenever no external product is required or when the choice is user/profile specific.

Candidate status vocabulary remains:

```text
external_reference
watch
candidate
to_verify
preferred_candidate
fallback_candidate
rejected
superseded
```

Runtime status remains separate from candidate status.

## Current registry

| Capability slot | Current external-binding posture | Notes |
|---|---|---|
| `web_evidence_intake` | `xberg-io/crawlberg` preferred candidate | Public-web intake with provenance; browser/SSRF/antibot boundaries remain relevant. |
| `external_connector_gateway` | Nango candidate | Optional scoped API connector gateway; credentials and writes remain separately governed. |
| `observability` | Langfuse preferred candidate | Optional Hermes trace/cost/latency visibility; traces are not Evidence or approval. |
| `document_structural_analysis` | Docling preferred candidate | Existing bounded path; extraction is derivative, not source truth. |
| `document_source_management` | `unbound` | Core source/document owners and local/NAS intake do not require a DMS. Paperless is superseded as a target dependency. |
| `knowledge_retrieval_pipeline` | `unbound` | No canonical RAG framework is required. Hermes-native file/context access may be sufficient. |
| `external_runtime_memory` | `unbound` | Hermes native memory is a valid baseline. Hindsight is the currently recommended external provider because it has the strongest live qualification in this repository. |
| `structural_repo_analysis` | `Lum1104/Understand-Anything` candidate | Useful structural analysis; generated graph remains derivative. |
| `revit_local_adapter` | Pantheon Revit Gate local-plugin candidate | Local sandbox exception; model mutation remains consequential. |
| `agent_artifact_transfer` | `shehryarsaroya/agenttransfer` to verify | Optional transport/handoff capability; receipts are not proof. |
| `bounded_workflow_runtime` | no default binding | LangGraph remains a reference for a demonstrated stateful-workflow gap, not a second runtime. |
| `document_parsing_rag_ingestion` | no integrated-stack adoption | RAGFlow remains reference/watch only because its bundled agents/workflows/memory/UI duplicate replaceable responsibilities. |

## Native Hermes baseline

A valid deployment may keep these optional slots unbound.

Current Hermes provides native facilities including:

```text
project/context files
MEMORY.md / USER.md
session history/search
runtime tools and skills
```

These are Hermes runtime facilities. They are not Pantheon Knowledge, Evidence or Registre Probatoire state merely because they are available or persistent.

```text
native Hermes sufficient != missing architecture layer
```

## External runtime memory

The machine-checkable selection owner remains:

```text
catalog/bindings/external-runtime-memory-unbound.yaml
```

That record is deliberately `unbound`. No external-memory provider is required by Pantheon.

### Recommended external provider: Hindsight

When an external memory/retrieval capability is wanted, Hindsight is the current recommended reference because Pantheon-Next has demonstrated the most complete working path with it.

Observed/qualified evidence includes:

```text
Hindsight service                    = 0.9.1 in the qualified Synology campaign
hindsight-obsidian code/assets       = 0.2.1 qualification target
Hermes native Hindsight provider     = exercised
Hermes bounded Hindsight recall      = exercised
single-bank MCP read routing         = exercised
bank isolation                       = exercised
Obsidian/Markdown ingestion          = exercised
producer separation                  = exercised
source/path provenance on recall     = regression-tested
```

The qualified reference topology is:

```text
Obsidian / Markdown
-> designated synchronization path
-> filesystem vault representation
-> hindsight-obsidian-sync
-> isolated Hindsight bank
-> bounded Hermes consumer
```

The later Q5 qualification also proved the important producer separation:

```text
Hermes file write
!= immediate Hindsight write

source Markdown change
-> designated hindsight-obsidian-sync reconcile
-> Hindsight materialization
-> Hermes recall with provenance
```

Therefore:

```text
Obsidian + Hindsight = qualified and recommended external reference composition
Obsidian + Hindsight != mandatory Pantheon stack
Hindsight recall != truth
Hindsight memory != Evidence
```

If an external stack is desired and no contrary user/deployment requirement exists, this qualified composition is the default recommendation because it is already demonstrated rather than merely hypothetical.

### Hermes-native alternative

An external provider is not required when native Hermes memory/context satisfies the user.

```text
Hermes native memory/context
= valid zero-extra-provider option
= external_runtime_memory remains unbound
```

This is not a downgrade of the Hindsight qualification. It is the simpler valid path for users who do not need the extra workspace/retrieval behavior.

### Other providers

Mnemosyne has historical proof of cross-session Hermes recall. Mem0, Honcho, OpenViking, Holographic, RetainDB, ByteRover, Supermemory and other providers may be reconsidered when they solve a demonstrated need better.

They are not parallel active recommendations.

```text
historically qualified != current default recommendation
new provider != new Pantheon subsystem
```

Detailed historical provider results remain in dated qualification logs/reference reviews rather than being promoted into permanent architecture.

## Workspace and retrieval

Pantheon does not define a mandatory note application or RAG topology.

A minimal deployment may use:

```text
Hermes project/context files
+ explicitly selected source files/folders
+ Hermes native memory/session search
```

A richer deployment may add a workspace/retrieval stack. The currently recommended qualified reference is:

```text
Obsidian / Markdown
-> Self-hosted LiveSync / CouchDB where synchronization is needed
-> filesystem vault mirror
-> hindsight-obsidian-sync
-> Hindsight
```

`OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` records that demonstrated composition and its remaining deployment-specific hardening gaps.

A replacement is acceptable when it preserves the same generic invariants:

```text
folder != governed identity
retrieval result != truth
sync success != approval
memory != Evidence
projection != persistence
```

## RAG posture

Pantheon does not require a canonical RAG framework.

```text
identified source / scope
-> optional retrieval implementation
-> candidate context with provenance
-> reasoning
-> Evidence only through the existing governed path
```

Embeddings, vector stores, rerankers, graphs and retrieval frameworks remain implementation choices. A task that can be satisfied by Hermes-native context or direct bounded source access does not need an extra RAG layer.

If advanced retrieval is required, Hindsight is currently the best-demonstrated external option in this repository; Haystack, LlamaIndex and selected LangChain components remain replaceable candidates rather than Pantheon dependencies.

## Document source management

Paperless no longer has a preferred binding role.

Existing source/document owners already preserve professional provenance and bounded local/NAS intake. A DMS may be selected later only for a concrete operational gap such as scanning intake, retention workflow or specialized version-management UX.

Any such DMS remains a replaceable backing/source adapter, never Pantheon classification, Knowledge or Evidence authority.

## Selection criteria

Select an external binding only when at least one concrete need exists:

- native Hermes capability is insufficient;
- required retrieval quality or scale is demonstrated;
- a specific external integration is needed;
- isolation, sharing or persistence requirements exceed native behavior;
- professional workflow requires a specialized replaceable adapter.

Prefer the candidate that:

- has current evidence in the repository;
- adds the least overlapping runtime surface;
- preserves provenance and scope;
- can be removed without migrating Pantheon governance state;
- fails closed around consequential operations.

## Replacement rule

An external binding may be replaced when another implementation satisfies the same capability contract better.

Replacement does not transfer authority and does not retroactively approve the new provider.

```text
provider implementation changes
!= Pantheon governance owner changes
```

## Final rule

```text
Use native Hermes when sufficient.
When an external workspace/retrieval/memory stack is wanted, prefer the already-qualified Obsidian + Hindsight composition unless another need justifies a different binding.
Keep every external provider optional and replaceable.
Pantheon governs the boundary, not the product choice.
```