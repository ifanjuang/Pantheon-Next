# Architecture Vertical MVP Slice — PDF → rooms + doors → program delta → human correction

Status: support template — candidate-only vertical slice, documented non-implemented.

This template materializes the first real test slice for Architecture Project Understanding. It is not doctrine promotion, not a runtime, not an adapter, not a schema migration and not an extraction implementation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The purpose is deliberately narrow: stop enriching the ontology and confront the v0.1 belief contract with one real project.

## Decision carried by this slice

Doctrine is frozen for this topic while the slice runs.

No new project-understanding objects, enums or schema families should be added for this slice. Existing objects and schemas are treated as v0.1 hypotheses, explicitly revisable by the first adapter feedback.

The slice may discover that the current ontology is wrong, too broad, too rigid or missing a practical relation. That finding is a review result. It must not be silently converted into a new object before the slice has been reviewed.

## MVP scope

One project. One PDF plan source. One five-line program. One human correction pass.

```text
PDF plan source
→ rooms / spaces + doors / openings candidate extraction
→ comparison against a five-line program
→ human correction sheet
→ review: what broke, what held, what the ontology must change
```

### In scope

- vector PDF first;
- one plan set or one bounded plan sheet;
- rooms / spaces visible on plan;
- doors / openings visible on plan;
- room labels, room numbers, approximate areas when visible or measurable;
- door identifiers when visible;
- door-to-room relations: `opens_to`, `located_in`, `separated_by` when supportable;
- evidence locator per extracted attribute: page, bbox/grid/anchor, source revision;
- five-line program comparison;
- human correction and review of extraction mistakes.

### Out of scope

- materials, assemblies, facades, wet-room details and interfaces;
- regulatory conclusions;
- fire-rating conclusions;
- PMR or code compliance assertions;
- scan/OCR-heavy plan reading as first target;
- IFC/Revit reconciliation;
- automatic canonization;
- schema promotion;
- database design;
- runtime implementation inside Pantheon.

## Required input package

The slice starts only when the following are present:

```text
1. Source PDF
2. Source version / date / index, or explicit "unknown"
3. Project scope for this run
4. Five-line program
5. Human reviewer identity or role
```

The five-line program must stay plain and small. Example:

```text
- 1 entrance / circulation sequence
- 1 kitchen
- 1 living room
- 2 bedrooms
- 1 bathroom with WC
```

## Output envelope

The external adapter or execution runtime returns only:

```text
Task Contract in
→ adapter / runtime outside Pantheon
→ Result Candidate + Evidence Pack Candidate out
```

The Result Candidate is not a truth. The Evidence Pack Candidate is not proof until reviewed. Human correction does not rewrite the PDF source; it creates a governed correction layer.

## Candidate objects allowed in the slice

Use the existing v0.1 hypotheses only:

```text
spatial_node
object_identity
object_relation
property_set
property_claim
attribute_claim
calibration
derivation
evidence
human_override
```

No new object may be added during extraction. When the slice needs a missing concept, record it under `ontology_feedback`, not as a new schema field.

## Minimal extraction targets

For each room / space candidate:

```text
stable_id
node_kind: room | space | circulation | unknown
current_display_name
human_ref, if visible
source_refs
area_claim, if visible or derivable
confidence representation used
provenance locator per attribute
uncertainties
```

For each door / opening candidate:

```text
stable_id
object_kind: door | opening | unknown
current_display_name
human_ref, if visible
source_refs
relation candidates: opens_to / separated_by / located_in
width_claim, if visible or derivable
swing_direction, if visible and useful
confidence representation used
provenance locator per attribute
uncertainties
```

## Program delta categories

The comparison against the five-line program must use only these categories:

```text
matched
missing_in_plan
extra_in_plan
ambiguous_match
dimension_or_area_to_verify
relation_to_verify
source_insufficient
```

No category means compliance. They are review states only.

## Human correction gate

The human correction pass must answer four questions:

```text
1. What did the adapter read correctly?
2. What did it miss?
3. What did it invent or over-read?
4. Which ontology assumption failed or survived?
```

Corrections must be recorded as `human_override` or `correction_candidate`, never as direct source mutation.

## Acceptance gates

The slice is successful only if all gates below are reviewable:

| Gate | Requirement |
|---|---|
| G0 — corpus admitted | The PDF and five-line program are present and scoped. |
| G1 — extraction visible | Rooms and doors are output as candidates, not truth. |
| G2 — attribute provenance | Every important field has a locator or explicit absence reason. |
| G3 — program delta | The five-line program produces matched/missing/extra/ambiguous/to-verify items. |
| G4 — correction loop | Human corrections are captured without mutating the source. |
| G5 — ontology feedback | Failures are classified as schema debt, adapter weakness or source insufficiency. |
| G6 — status discipline | No result is called implemented, canonical, compliant or validated by extraction alone. |

## Debt explicitly attached to this slice

The following debt must be paid before the current schemas can be treated as a real foundation:

```text
1. Factor duplicated $defs.
2. Add referential-integrity controls for ids and refs.
3. Decide between certainty_score and E0–E4; do not keep two competing certainty systems.
4. Confirm whether confidence is numeric derivation output, evidence-status axis, or display-level translation.
5. Verify that zone_type is required when node_kind is zone.
```

Until then, the repository state is:

```text
Project Understanding v0.1: documented non-implemented.
Schemas: implemented as validation artifacts, but hypothesis-level for this slice.
Adapter feedback: expected to revise them.
```

## Definition of done

The vertical slice is done when one real project produces:

```text
- one source inventory;
- one five-line program;
- one rooms/doors Result Candidate;
- one Evidence Pack Candidate with locators;
- one program delta;
- one human correction sheet;
- one ontology feedback note;
- one Zeus decision: accepted / refused / to verify / to arbitrate.
```

The outcome is not a better doctrine document. The outcome is a tested boundary between project understanding, proof, adapter execution and human correction.
