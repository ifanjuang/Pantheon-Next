# Architecture Project Understanding — Belief Contract

Status: candidate doctrine — architecture-domain project understanding contract (v0.1).

This document defines a candidate **belief contract** for understanding an
architecture project from heterogeneous sources.

It is documentation only.

It does not implement a SQL schema, migration, Postgres/PostGIS table, object
storage, pgvector index, provenance graph runtime, OCR, vision model, PDF/IFC
reader, Revit plugin, MCP server, queue, scheduler, diff engine, OpenWebUI
action, Hermes skill, connector, approval engine or memory engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

In abstract form:

```text
The exposure surface exposes.
The execution runtime executes.
Pantheon governs.
The proof constrains.
The human decides.
```

## Purpose

Architecture practice does not need a plan reader. It needs a governed
understanding of the project that can ingest heterogeneous sources (Revit, IFC,
vector PDF, scanned PDF, JPG, sections, elevations, details, BET drawings),
reconstruct what is known about the project, and expose **what is read,
measured, estimated, missing, contradictory and what must be arbitrated** —
without ever claiming truth on its own.

This is not a database to be filled. It is a **proof engine**: a system of
beliefs carrying their provenance, which degrades gracefully and stays
auditable.

## Placement (non-negotiable)

| Layer | Role | Hosts this contract? |
| --- | --- | --- |
| Pantheon Next | governs: vocabulary, status, proof, canonization rules, limits | **Yes** — this contract + schemas |
| Hermes | orchestrates: selects readers, runs modules | no |
| Adapters (`ifj-*`) | execute: Revit / IFC / PDF / image, OCR, vision, diff | no |
| Project Understanding Base | stores sources, candidates, proofs, decisions (PostGIS/JSONB) | no |
| OpenWebUI | visualizes, corrects, queries, validates | no |

No extraction runtime, OCR, vision, Revit plugin or executable MCP server
enters this repository — including under any `labs/` folder. Only **data
examples** (candidate YAML) are admitted here. The runtime lives in separate
bounded repositories (`ifj-revit-spatial-bridge`, `ifj-pdf-plan-reader`,
`ifj-ifc-spatial-reader`, `ifj-image-plan-reader`).

## Invariant principle — five laws

These laws prevail over every other part of the contract.

- **L1 — No source produces truth.** Every adapter produces `candidate`.
  Canonization is a governed human act.
- **L2 — Certainty is computed, not declared.** `certainty_score` and
  `tolerance` are *outputs* of a derivation graph, never inputs.
- **L3 — Provenance is per attribute, not per object.** A stable object has a
  source *per field*.
- **L4 — A contradiction is held, not resolved.** The system keeps the
  competing claims and routes to the source policy and the human.
- **L5 — The right to ground a regulatory conclusion is an approved use, never a
  model output.** It travels only through the `regulatory_claim` use type,
  opened by the gate.

## Core objects (minimal noyau)

The initial contract defines **only** the nine objects below. Everything else
(technical assemblies, interfaces/details, checks, coordination issues) is an
extension that plugs into this core and is specified later (see §"Out of scope").

Each object has a validation schema under
`schemas/architecture-project-understanding/`.

### 1. `stable_object` — project identity

Persistent identity across indices and sources. The **match is itself a
probative candidate**, not a fact. The revision diff (Lot 4) runs only on
matches that are `confirmed_by_human` or explicitly presumed.

### 2. `attribute_claim` — the elementary datum

Replaces flat measurements. Each attribute of an object is a claim carrying its
source, derivation and allowed use. There is **no** `can_support_regulatory_claim`
boolean: the regulatory right is a `use_type` in `allowed_use`, opened only by the
gate (L5).

### 3. `calibration` — the upstream foundation

Every measurement depends on a registration into a shared frame, **gated and
multi-witness**. While witnesses diverge beyond threshold, **no derived
measurement may exceed `to_verify`** (mapped to `requires_more_evidence`).
Recognized frames: `PIXEL`, `PAGE`, `MODEL_LOCAL`, `PROJECT`, `GEO_NGF`.
Orientation (true/project/drawing north) and altimetry (project zero / NGF) are
frames, not separate graphs.

### 4. `derivation` — provenance DAG + uncertainty propagation

Makes inference auditable and certainty computable (L2). A conclusion's
`certainty_score` is `<= min` of its premises; a path tolerance composes its
segment tolerances.

### 5. `evidence` — localized proof

`{source, locator}` where locator is a page+bbox, ElementId, grid ref or IFC
GUID. Reuses the proof-register `evidence_ref` / `anchor` shape.

### 6. `doubt` — active, drives an acquisition backlog

A doubt carries **what would resolve it** and **what it blocks**. Prioritization
= number of checks unblocked / effort. A doubt is not decorative; it produces a
question and document-request backlog.

### 7. `contradiction` — governed object (L4)

Holds the competing claims, links their evidence, may carry a `policy_hint`, and
is `pending_human`. Never auto-resolved.

### 8. `human_override` — correction loop without write

A human correction never mutates the source. It is a higher-authority,
versioned layer that future re-extractions respect. Authority `human_decision`
sits at the top of the project source policy.

### 9. `canonization` — rite per use, not a boolean (L1, L5)

Canonical *for internal review* is not canonical *for contractual action*.
Promotion always answers: canonical **for which use, approved by which role, in
which scope** — expressed through the existing `approval_state` / `allowed_use`.

## Three time axes (never to be confused)

| Axis | Meaning | Carrier |
| --- | --- | --- |
| Documentary time | index A -> B -> C | `version_event` (existing) |
| Project / phasing time | existing -> demolished -> built | `change` on stable objects |
| Knowledge-validity time | a fact confirmed at APD invalidated by a PRO change | `validity` on `attribute_claim` |

An object "disappeared from an index" (alert) is not an object "demolished by
design" (intended).

## Responsibility axis (maîtrise d'œuvre)

Every risk/check carries a responsibility boundary, plugged into the existing
handoff logic (`docs/examples/architecture_abf_handoff`). Example:
`responsibility_boundary: [architect, bet_structure]`,
`handoff_expected: detail_or_arbitrage`. This is where governance meets real MOE
liability — the differentiator over BIM tools.

## Aligned vocabulary (no duplication)

This contract **extends** `schemas/architecture-proof-register/` and
`schemas/shared_axes.schema.yaml`; it does not create parallel enums.

- **Status** reuses `proof_status` (`candidate`, `contradictory_evidence`,
  `authority_too_low`, `requires_more_evidence`, `accepted_as_support`,
  `rejected`, `obsolete`, `superseded`, …). The flat
  `raw/extracted/.../canonical_active` ladder is **abandoned** in favor of
  `proof_status` + `approval_state`.
- **Source authority** reuses `source_authority_level`
  (`signed_market_document` … `model_interpretation_candidate`). The per-project
  `source_policy` orders these levels; `human_decision` always prevails.
- **Use** reuses `allowed_use` / `forbidden_use`, **plus** the new
  `regulatory_claim` use type — the sole vehicle of the regulatory right (L5).

## Governance invariants (the MUSTs)

1. No adapter writes `canonical`. (L1)
2. `confidence` / `tolerance` are never hand-entered. (L2)
3. Per-attribute provenance is mandatory. (L3)
4. No contradiction is resolved by the system. (L4)
5. `regulatory_claim` is opened only by the gate. (L5)
6. Divergent calibration caps derived measurements at `requires_more_evidence`.
7. Diff is conditioned on confirmed matches.
8. Every human correction routes through the chokepoint (`human_override`),
   never a direct write on the source.

## Out of scope (later extensions)

Plugged onto the core, **specified later**: `technical_assembly`
(materials/layers/faces/performances), `interface_detail` (reservations,
rainwater, waterproofing), `requirement_check` (IDS-style), `issue_coordination`
(BCF-style). The contract does not freeze a material vocabulary before a spatial
graph runs.

## Evaluation (from day one)

A few ground-truth projects plus an extraction error rate **per source type**
(vector PDF != scan != JPG). Without a regression harness, `confidence` is mere
self-declaration.

## Inspiration, not copy

IFC / IfcOpenShell (objects, relations, properties, quantities, `IfcDiff`), IDS
(information requirements), BCF (coordination issues), ISO 19650 (document
management), BHoM (software-agnostic AEC object + adapters), Speckle (versioned
objects + connectors), Topologic (topological/path graphs). Inspire the runtime
side; do not import their schemas into this governance core.

## Contract definition of done

> Architecture Project Understanding turns heterogeneous sources into beliefs
> with provenance: stable object -> per-field sourced attributes ->
> calibration/derivation -> evidence/doubt/contradiction -> override/canonization
> per use. It exposes what is read, measured, estimated, missing, contradictory
> and what must be arbitrated. Pantheon governs · Hermes orchestrates · the
> adapters execute · the proof constrains · the human decides.

## Governance references

- docs/governance/ARCHITECTURE_PROOF_REGISTER.md
- docs/governance/ARCHITECTURE_INDEX_EFFECT_MATRIX.md
- docs/governance/EVIDENCE_PACK.md
- docs/governance/ANSWER_VERIFICATION_GATE.md
- docs/governance/APPROVALS.md
- docs/governance/GLOSSARY.md
- schemas/shared_axes.schema.yaml
- schemas/architecture-proof-register/
