# Architecture Knowledge Registry Blueprint

Status: candidate support doctrine — blueprint for the architecture knowledge registry (documentation only).

This document is the Pantheon-side **blueprint** for how an architecture
practice's reusable knowledge is registered and governed. It resolves
arbitration item C ("Knowledge registry location") of
`docs/domain-packs/architecture/OS_RECONCILIATION.md`: the blueprint lives in
Pantheon; the runnable mapping lives outside Pantheon.

It is documentation only. It does not implement a registry runtime, ingestion
pipeline, OCR, vector index, embedding store, graph backend or external
connector. Entries it describes remain candidates until reviewed.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

An architecture practice reuses a body of knowledge across projects:
regulations, agency standards, typical construction details, lessons learned,
supplier and product data, and precedents. This blueprint describes how such
knowledge is **registered as governed entries** — with a source, an authority
level and a status — so it can be referenced without being silently treated as
truth.

## Placement: blueprint in Pantheon, mapping outside

- **Pantheon (this blueprint)** governs the vocabulary, the authority levels, the
  statuses and the boundary. It decides nothing automatically.
- **The runnable mapping** (ingestion, normalization, indexing, retrieval) lives
  outside Pantheon: non-executable templates under `templates/` and/or external
  adapters on the Hermes side. It produces candidates, never canonical truth.

This mirrors the doctrine of the whole repository: Pantheon governs, Hermes and
adapters execute, the proof constrains, the human decides.

## What the registry holds

Each registry entry is a governed knowledge item, not a fact. Candidate
categories:

- `regulation` — codes, norms, local urban rules (high authority when official).
- `agency_standard` — the practice's own conventions and templates.
- `construction_detail` — typical or proven details and assemblies.
- `lesson_learned` — post-project feedback, reserves, site observations.
- `supplier_product` — product and supplier data, technical sheets.
- `precedent` — prior projects or external references used by analogy.

Categories align with `docs/governance/KNOWLEDGE_TAXONOMY.md`; they extend it for
the architecture domain, they do not replace it.

## How entries map to the governance vocabulary

A registry entry reuses the existing axes and the proof register vocabulary
rather than inventing parallel ones:

- **source authority** uses `source_authority_level` (from `law_or_regulation`
  down to `model_interpretation_candidate`).
- **status** uses `proof_status` / `approval_state` from the architecture proof
  register.
- **scope** uses the shared scope vocabulary (project / agency_library /
  global_reference …).

So a regulation entry can carry strong authority, while a model-derived note
stays a low-authority candidate — the same ladder used everywhere else.

## Boundary

- No ingestion engine, OCR, vector or graph backend, embedding store, retrieval
  service or external connector is defined or implied here.
- The mapping that turns sources into registry entries is an adapter outside
  Pantheon; it outputs Task Contract in → Result Candidate + Evidence Pack
  Candidate out, through the chokepoint.
- Registry entries never auto-promote to canonical; promotion is a governed
  human decision, per use, like any other Pantheon canonization.

## Relationship to other documents

- `docs/governance/KNOWLEDGE_TAXONOMY.md` — the general knowledge taxonomy this
  blueprint specializes for architecture.
- `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md` — governed ingestion and
  memory boundary the runnable mapping must respect.
- `docs/domain-packs/architecture/AGENCY_DOMAIN_PACK.md` and
  `docs/governance/DOMAIN_PACK_SPEC.md` — the domain pack the registry serves.
- `docs/domain-packs/architecture/PROOF_REGISTER.md` — the proof vocabulary reused
  by registry entries.
- `docs/domain-packs/architecture/OS_RECONCILIATION.md` — arbitration item C that
  this blueprint resolves.

## Governance references

- docs/domain-packs/architecture/OS_RECONCILIATION.md
- docs/governance/KNOWLEDGE_TAXONOMY.md
- docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md
- docs/domain-packs/architecture/AGENCY_DOMAIN_PACK.md
- docs/domain-packs/architecture/PROOF_REGISTER.md
