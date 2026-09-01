# Haystack bounded retrieval qualification

Status: qualification lab for Pantheon issue #908. Not installed, selected, activated or adopted by default.

## Purpose

Exercise Haystack only as a replaceable implementation behind the existing `knowledge_retrieval_pipeline` Capability Slot.

Pantheon must resolve access, currentness and exact source identity before the adapter receives any material. The provider is a projection and ranking surface only.

```text
Pantheon access/currentness/source owners
        -> exact RetrievalScopeResolution
        -> this lab adapter
        -> Haystack projection + BM25 retrieval
        -> provider-neutral candidates with exact provenance
        -> runtime consumer
```

## Qualification target

Canonical pin: `implementation/qualification/external-pins.json`.

At creation of this slice:

```text
package: haystack-ai
version: 3.1.0
upstream repository: deepset-ai/haystack
release commit: 859a6eb3ac4d0bd33f069bab57fb041e3434a353
```

The release pin is qualification input, not deployment truth.

## What this slice proves

- material outside a fresh Pantheon `RetrievalScopeResolution` is rejected before projection;
- provider retrieval is filtered by exact dossier/source ref/digest/version identity;
- provider responses are post-validated against the exact resolved identity and fail closed on mismatch;
- a poisoned provider store cannot widen the accepted corpus;
- replacing a source revision removes the prior projection for this binding instance;
- deleting/revoking all resolved sources reconciles the projection to empty;
- returned candidates preserve `document_id`, `document_version_id`, dossier, source ref, digest, source version, purpose and currentness basis references;
- returned objects are provider-neutral and carry no Evidence-admission or effect-authorization claim;
- `HAYSTACK_UNSAFE_DESERIALIZATION` is refused when enabled.

## Deliberate limitations

This first slice uses only Haystack core `InMemoryDocumentStore` + `InMemoryBM25Retriever`.

It does **not** qualify:

- production persistence or restart recovery;
- embeddings, vector retrieval or reranking;
- Google Drive, NAS or Obsidian ingestion;
- Hindsight integration or documentary dual-ingestion;
- Haystack Agent, AgentTool, Hayhooks, MCP or serialized pipeline execution;
- a production Hermes transport/API binding;
- retrieval-quality superiority over Pantheon's current native hybrid path;
- a preferred or activated Haystack binding.

The `binding_instance_id` used by the adapter is operational projection identity only. It is not a Pantheon Project, dossier, Source, CapabilityBinding or authorization identity.

## Security posture

Haystack 3.1.0 exposes `HAYSTACK_UNSAFE_DESERIALIZATION` as a process-wide switch that disables deserialization protections when set to a supported truthy value. This lab explicitly refuses that posture.

```text
provider row != Pantheon Source
provider score != Evidence quality
provider filter success != authorization
retrieval success != truth
projection != persistence
lab present != binding selected
```

## Next decision

A green lab closes only the first synthetic boundary slice. The next step is to review its measured behavior and decide whether a second slice is justified. Native retrieval remaining sufficient is a valid outcome and leaves `knowledge_retrieval_pipeline` unbound.
