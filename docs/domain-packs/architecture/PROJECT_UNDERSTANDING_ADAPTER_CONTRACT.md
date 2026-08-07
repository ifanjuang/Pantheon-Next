# Architecture Project Understanding — Adapter Contract

Status: candidate support doctrine — adapter binding for Architecture Project Understanding.

This document defines the **binding** an external adapter must respect to feed the
Architecture Project Understanding (APU) belief contract. The adapter (PDF/IFC/
image/Revit reader) is **runtime and lives outside Pantheon**; Pantheon governs
status, scope, evidence expectations, the correction gate and ontology feedback.

It is documentation only. It implements no reader, OCR, vision, extractor or
connector. It specializes the generic `BRIDGE_CONTRACT.md` /
`ADAPTERS_AND_BINDINGS.md` for the APU family.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## The interface

Every APU adapter is a function across the chokepoint:

```text
Task Contract in
→ adapter / runtime outside Pantheon
→ Result Candidate + Evidence Pack Candidate out
```

It never produces canonical truth. It produces candidates that a human reviews.

### Input (Task Contract)

```text
- one or more source artifacts (e.g. a vector PDF), with source id, index/date or explicit "unknown"
- an optional five-line program (see PROGRAM_AND_CONFORMANCE.md)
- the project scope for the run
- a run id
```

### Output (Result Candidate)

Objects conforming to `schemas/architecture-project-understanding/`:

- `stable_object` (kind `space`, `opening`, …) with `matches` proposed as
  `candidate` on the `cross_source` axis — identity is a probative candidate, not
  a fact;
- `attribute_claim` with `modality: observed` (or `proposed`), per-attribute
  provenance, and `certainty` on the **E0–E4** axis (the numeric score stays
  inside the adapter's derivation; only the band crosses the boundary);
- `object_relation`, `spatial_node` (a `zone` must carry `zone_type`),
  `object_identity` (aliases / source_refs);
- optionally a `program_delta` using only the review categories of
  PROGRAM_AND_CONFORMANCE.md / the #168 template — never a compliance verdict.

### Output (Evidence Pack Candidate)

`evidence` items with a locator (page+bbox, grid ref, element id) for every
important field, plus assumptions, uncertainties and missing pieces.

## Source-specific binding specializations

Source adapters may need stricter local contracts without changing this APU
chokepoint.

```text
REVIT_LOCAL_ADAPTER.md
-> owns local Revit context, capability exposure, preflight and model execution.

DRAWING_TAKEOFF_LOCAL_ADAPTER.md
-> owns the candidate local PDF/drawing measurement binding, including scale,
   quantity, marked-output, withheld/refusal and offline-packaging posture.
```

These are sibling source bindings. A drawing-takeoff engine must not become a
Revit dependency merely because both can report quantities, and neither source's
native identity becomes `stable_object_id`.

```text
PDF measurement != Revit observation
source agreement != reviewed identity match
quantity agreement != accepted project quantity
```

Hermes may compare results from several admitted bindings, but cross-source
matching remains candidate material routed through the existing APU review path.

## Hard constraints (the MUSTs)

1. Everything is `candidate`. No adapter canonizes; canonization is a governed
   human act.
2. The adapter never grants `regulatory_claim`; that use is opened only by the
   gate (L5).
3. Per-attribute provenance is mandatory (L3): each important field carries an
   evidence locator or an explicit absence reason.
4. Certainty crosses the boundary only as the E0–E4 band (decision A).
5. The adapter outputs `observed` / `proposed`, never `required` (intent belongs
   to the program).
6. The adapter does not mutate the source. Human corrections are governed
   `human_override`s, not adapter writes.
7. The adapter runs outside Pantheon; it imports Pantheon schemas and templates,
   and Pantheon never imports the adapter (one-way dependency).

## Reference shapes

- Output envelope and acceptance gates: `templates/architecture_vertical_mvp/`.
- A schema-conformant worked example: `docs/examples/architecture_project_understanding_dossier/`.
- Referential-integrity expectations: `.github/scripts/check_apu_referential_integrity.py`.

## Governance references

- docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
- docs/domain-packs/architecture/DRAWING_TAKEOFF_LOCAL_ADAPTER.md
- docs/governance/REVIT_LOCAL_ADAPTER.md
- docs/governance/PROGRAM_AND_CONFORMANCE.md
- docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md
- docs/governance/BRIDGE_CONTRACT.md
- docs/governance/ADAPTERS_AND_BINDINGS.md
- docs/governance/EVIDENCE_PACK.md
- docs/governance/TASK_CONTRACTS.md
