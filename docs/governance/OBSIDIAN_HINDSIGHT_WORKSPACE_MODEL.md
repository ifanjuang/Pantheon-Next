# Obsidian / Hindsight Reference Implementation

Status: qualified reference implementation profile — not a Pantheon architecture owner, dependency or mandatory binding.

Authority note: generic memory selection remains owned by `HERMES_CAPABILITY_BINDINGS.md` and the machine-checkable `catalog/bindings/external-runtime-memory-unbound.yaml`. Generic source, Knowledge, Evidence and Project identities remain owned by their existing Pantheon contracts.

Qualification record: Pantheon-Next #655, #659, #660, #714 and merged qualification slices including #703, #725 and #726.

## Purpose

Record one tested workspace / synchronization / retrieval composition without turning those products into Pantheon prerequisites.

```text
Obsidian / Markdown
-> Self-hosted LiveSync / CouchDB
-> filesystem vault mirror
-> hindsight-obsidian-sync
-> Hindsight
-> bounded Hermes consumers
```

This composition is useful because it has real qualification evidence. It is not the only valid composition.

A user may instead use Hermes-native context/files/memory only, another note workspace, another synchronization mechanism, another retrieval engine or another memory provider when the same boundaries are preserved.

## Responsibility split

```text
Markdown workspace
= human-authored working material

synchronization transport
= convergence between representations

filesystem mirror
= synchronized file representation

Hindsight
= derived retrieval / associative memory in this reference profile

Hermes
= runtime consumption, reasoning and candidate generation

Pantheon
= governed identity, provenance, Evidence, authorization and durable professional status
```

```text
workspace != governed Project
folder != governed identity
sync success != professional approval
retrieved != truth
memory != Evidence
```

## Qualified observations

The repository has demonstrated, with bounded synthetic qualification:

- Self-hosted LiveSync CLI materialization through CouchDB into a filesystem vault;
- create/edit/rename/delete convergence in the qualified headless daemon composition;
- Hermes filesystem read/create/anchored-patch compatibility against a bounded vault;
- Hermes-originated file changes converging through LiveSync in the synthetic Q3 path;
- `hindsight-obsidian-sync` as a separate producer from Hermes runtime writes;
- Hindsight recall through Hermes with source/path provenance in the Q5 separation test;
- Hindsight bank isolation and bounded read surfaces in the #655 qualification campaign.

These observations prove compatibility for the tested revisions only.

```text
qualification proof != production adoption
runtime success != authorization
bank isolation != access control
```

## Current reference topology

The qualified IFJA reference used trust-domain banks rather than one bank per project:

```text
ifja-agency
ifja-projects
ifja-sandbox
```

Project/folder tags were used for narrower retrieval scope.

That topology is a provider-specific implementation choice, not a Pantheon identity model.

```text
bank != Project
folder/tag != Pantheon scope authority
```

Other providers may express isolation through namespaces, collections, tenants, stores or different mechanisms.

## Source rule

Original professional material keeps its existing source identity.

Examples:

```text
PDF -> source/document owner
email -> source/message owner
photo -> source/image owner
model -> source representation owner
Markdown note -> workspace source note when intentionally authored
```

Hindsight in this reference implementation is a derivative index/memory, not the canonical store for professional source bytes.

## Retrieval rule

Retrieval should remain bounded by the active task/source scope.

The reference Hindsight profile used strict bank/tag/folder constraints to prevent silent cross-project widening. A replacement retrieval engine must preserve the same behavioral invariant even if its API is different.

```text
specific target
-> bounded retrieval inside authorized scope
-> explicit widening only when requested/authorized
```

## Producer rule

The qualified durable-workspace path separates file mutation from Hindsight ingestion:

```text
Hermes or human edits source Markdown
!= direct durable Hindsight write

source Markdown
-> designated ingestion producer
-> derived Hindsight state
```

The Q5 qualification specifically demonstrated that Hermes file writes did not appear in Hindsight until the designated `hindsight-obsidian-sync` reconcile step ran.

That separation is useful, but Pantheon does not require this exact producer implementation. A replacement stack must merely avoid ambiguous concurrent authorities.

## Hermes-native alternative

No external workspace/retrieval stack is required when Hermes-native facilities are sufficient.

Current Hermes can use:

```text
project/context files
explicit file/folder references
MEMORY.md / USER.md
session history/search
```

Those facilities remain Hermes runtime state/context. They do not become Pantheon Evidence or governed Knowledge automatically.

## Hindsight posture

Hindsight is currently a strong qualified/recommended optional provider because the repository contains real integration tests for it.

It is not mandatory.

The `external_runtime_memory` Capability Binding remains `unbound` unless a separate selection decision changes it. Hermes native memory can remain the only runtime memory.

If Hindsight is selected for both document/workspace retrieval and runtime memory, the two responsibilities must remain scoped distinctly rather than being collapsed merely because one product can serve both.

## Security and production gaps

Historical qualification observed limitations including unauthenticated Hindsight API/MCP exposure on the tested LAN path. #659 retains the hardening/operational qualification work for that specific deployment.

Those gaps matter only when this reference implementation is selected. They are not Pantheon-wide infrastructure requirements.

## Replacement rule

A replacement workspace, sync layer, retrieval engine or memory provider is acceptable when it preserves the relevant contracts:

```text
source provenance remains visible
scope does not silently widen
runtime state does not become Evidence
a provider write does not become authorization
projection does not become persistence
folder/provider namespace does not become governed identity
```

Do not reproduce Obsidian/Hindsight-specific bank, tag or folder conventions in generic Pantheon contracts.

## Final classification

```text
Obsidian                 = recommended optional workspace example
Self-hosted LiveSync     = qualified optional synchronization example
CouchDB                  = synchronization state in that example
hindsight-obsidian-sync  = qualified optional ingestion example
Hindsight                = qualified/recommended optional retrieval/memory provider
Hermes native facilities = valid zero-extra-provider alternative
Pantheon                 = provider-agnostic governance boundary
```

This file records a tested composition. It does not define the Pantheon stack.