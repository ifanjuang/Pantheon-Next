# Program & Conformance

Status: candidate doctrine — program-as-source and conformance extension of the
Architecture Project Understanding belief contract (v0.1).

This document extends `PROJECT_UNDERSTANDING.md`. It is documentation
only and adds no runtime: no extraction, OCR, vision, solver, scheduler or
conformance engine. It defines vocabulary and validation contracts; deviations
and program changes are governed candidates, decided by the human gate.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A project can be born partially or with no drawing at all — from a client program
alone (number of rooms, required connections, target areas), or from a document
platform such as Kroqi. The program is the highest-authority source of **intent**.
This extension lets the system:

- ingest a program as a typed, layered, versioned source of intent;
- express prescriptive requirements (areas, heights, connections, counts,
  classifications, attributes);
- classify spaces, openings, boundaries and groups under several coexisting
  schemes (housing typology, fire/ERP, medical/ISO, activity, façade, doors…);
- group spaces into composite identities (a T2, a duplex, a lift shaft) that span
  several levels and carry their own requirements;
- detect the **deviation** between a drawn version and the program, and resolve it
  in either direction — amend the design, amend the program, or record a waiver.

## The modality axis (core addition)

The elementary datum gains a modality so intent and state are distinguishable:

```text
claim_modality: required | proposed | observed | as_built
```

- program → `required` (intent);
- drawing / model → `observed` or `proposed` (state);
- deviation = `required` with no matching `observed`, or `observed` contradicting
  `required`.

Without modality, an `attribute_claim` cannot say whether 0.83 m is a measurement
or a demand. Modality lives on `attribute_claim` and on `classification`.

## Program as a typed, layered, versioned source

A `program` is a high-authority source (`operation_contract` /
`approved_client_decision`). Several programs coexist: general orientations and
specific requirements, and different typologies on a mixed project.

- `program_type`: `housing | medical | office | erp | education | hospitality | industrial | mixed | other`
- `program_layer`: `general_orientation | specific_requirement`
- versioning uses documentary time (program v1 → v2 is a `version_event`).

**Email-triggered change.** A received email is a `source_artifact` / `evidence`
that produces a `program_change` candidate routed through the chokepoint — never
applied automatically. The same governance as `human_override`, applied to intent.

## Requirements (prescriptive claims)

A `requirement` is a prescriptive claim from a program. Families:

- **quantitative**: `area_min` / `area_max` / `area_target`, `ceiling_height_min`
  / `ceiling_height_target`, `dimension_min`;
- **relational**: `must_connect`, `must_be_adjacent`, `must_have_access_to`;
- **count**: `count` (spaces of a function) and `group_count` (units of a
  typology, e.g. eight T2);
- **classificatory / attribute**: a target must carry a classification or an
  attribute value (e.g. a bedroom door must be sliding and acoustic).

A requirement targets a `stable_object`, a `space_function`, a `space_group`, or a
classification value over a scope.

## Classification (multi-scheme, extensible)

A space, opening, boundary or group may carry several classifications at once,
each a candidate with provenance and modality. Rather than one hard-coded
taxonomy, schemes are **registered** (`classification_scheme`) and extensible.

Starter registry (each a scheme; values illustrative, extensible):

- `housing_typology`: studio, T1, T2, T3, T4, T5, simplex, duplex, PLAI, PLUS,
  PLS, accessible, adaptable.
- `room_function`: sejour, cuisine, chambre, sdb, wc, degagement, cellier,
  local_technique, hall, circulation, local_velo, local_om.
- `activity`: sleeping, wet_room, cooking, storage, technical, working.
- `fire_erp`: ERP types (J, L, M, N, O, P, R, S, T, U) and categories (1 to 5);
  habitation families (1, 2, 3A, 3B, 4); Euroclasses reaction (A1 to F) and
  resistance ratings (REI / EI).
- `medical`: zones 1 to 4, soins, bloc, chambre; cleanroom `iso_cleanroom`
  (ISO 14644 classes 1 to 9).
- `acoustic`: sensitive / sleeping room, required isolation.
- `accessibility`: PMR circulation, accessible-unit quota.
- `facade_system`: curtain_wall, ventilated_cladding, masonry, other.
- `door_property`: operation (swing, sliding, folding, pivot, automatic),
  acoustic rating, fire rating.

A regulatory classification (ERP category, fire rating, PMR lift) feeding a
conclusion is granted only through the `regulatory_claim` use type (L5). The
program *demands* a class; it does not *prove* conformity.

## Composite identities and multi-level objects

A `space_group` is a `stable_object` of kind `group` that aggregates members,
carries its own requirements and classifications, can nest (building → floor →
unit → room), and may span several levels.

The genuinely new structural concept is **vertical identity**: duplexes, lift
shafts, stairwells, ducts and curtain walls cross several `levels` and reappear on
several plans/sections. Two additions support it:

- `spans_levels` on `stable_object` and `space_group`;
- a third matching axis on `stable_object.matches`: in addition to cross-index and
  cross-source, **cross-level** (the lift shaft on the ground-floor plan and on the
  first-floor plan are the same object).

Vertical connections are typed: `stair | lift | ramp | shaft_duct`.

## Per-kind attribute vocabulary

Attributes are controlled-but-extensible per object kind, each value an
`attribute_claim` with modality and provenance:

- `space`: `area`, `clear_height`, `function`.
- `opening`: `operation` (swing / sliding / folding / pivot / automatic),
  `acoustic_rating`, `fire_rating`, `clear_width`, `clear_height`, `thermal`.
- `boundary`: `facade_system`, `acoustic_rating`, `fire_rating`, `thermal`.

## Deviation and bidirectional resolution

A `deviation` records a gap between a requirement and the observed state. Kinds:
`missing_space`, `missing_connection`, `count_short`, `count_excess`,
`area_below_min`, `area_above_max`, `ceiling_height_below_min`,
`wrong_classification`, `wrong_attribute`, `missing_attribute`.

Resolution is a human decision, never automatic, and works in both directions:

- `amend_design` — the design changes in the next index;
- `amend_program` — the program is modified (a `program_change` candidate);
- `accept_deviation` — a recorded waiver with authority and justification.

## Governance invariants (in addition to the core)

1. `program_change` is never auto-applied; it is a candidate through the gate.
2. Classifications and requirements carry provenance and modality like any claim.
3. A regulatory classification grounds a conclusion only via `regulatory_claim`.
4. A deviation is never resolved by the system; the gate chooses the direction.
5. `accept_deviation` is an explicit waiver, recorded — not a silent pass.

## Governance references

- docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
- docs/domain-packs/architecture/PROOF_REGISTER.md
- docs/governance/APPROVALS.md
- docs/governance/GLOSSARY.md
- schemas/architecture-project-understanding/shared.schema.yaml
