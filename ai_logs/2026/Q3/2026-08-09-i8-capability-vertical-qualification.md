# I8 — representative Capability vertical qualification

Date: 2026-08-09
Parent: #620
Issue: #642

## Objective

Qualify the merged I2–I7 Capability governance model on one existing chain without adding another owner.

## Selected vertical

The existing Docling/document-analysis records already span the governance responsibilities required by I8:

```text
document_structural_analysis Capability Slot
-> example.portable-skill.read Capability Passport
-> immutable content_digest
-> capability_binding_document_analysis_docling
-> project-scoped CapabilityActivation
-> existing Task Contract / Execution Admission seam in pantheon-mvp
-> exact-release CapabilityCompatibilityObservation
-> existing non-authoritative Tool Card projection in pantheon-mvp
```

No new Capability, registry, runtime binding manager or projection owner is introduced.

## Cross-repository executable seams retained

### Pantheon-Next

I8 cross-validates the already merged Passport, Binding, Activation and CompatibilityObservation records and schemas. The deterministic corpus tests exact identity continuity and adversarial replacement/state combinations.

### pantheon-mvp

Existing executable owners are intentionally reused rather than mirrored here:

- `mvp_vertical/hermes_execution.py` remains the sole Execution Admission / task-run legitimacy seam;
- `tests/test_hermes_execution.py` proves human admission is immutable/bounded, does not start the runtime, becomes stale when its governed Work Issue changes and is consumed once by an external run;
- `mvp_vertical/cockpit/projection/tool_governance_projection.js` remains projection-only;
- `tests/test_cockpit_tool_cards.py` proves exact binding/release/activation/compatibility axes remain distinct and that the UI cannot infer authorization.

I8 therefore does not copy a Docling governance row into the static MVP tool catalogue. A UI fixture may project the exact fields, but projection presence remains non-authoritative.

## Adversarial matrix

The I8 corpus covers:

1. exact baseline continuity;
2. release/content-digest drift;
3. binding replacement without activation/observation inheritance;
4. installed/healthy runtime facts without admission;
5. healthy + compatible while safety remains not qualified;
6. project activation while task authorization remains absent;
7. stale compatibility observation;
8. explicit unbound/unavailable binding;
9. UI projection with no authorization effect.

## Governing result

```text
binding selected != dependency adopted
release changed != prior observation valid
binding replaced != activation inherited
installed/available != admitted
healthy != compatible
compatible != safe
activated != task authorized
Execution Admission != Capability activation
runtime success != Evidence
UI projected != authorization
H source qualification != I task authorization
```

## Boundary with H

The representative chain uses document analysis because its records already exist, but I8 does not re-run or redefine document/PDF/image source qualification. Any `source_qualification_ref` remains optional provenance into H-owned qualification. I only qualifies Capability governance continuity around the exact implementation/binding.

## Exit posture

I8 is complete only after the deterministic corpus is green on the exact PR head and the existing MVP admission/projection seams remain unchanged. I9 may then audit duplicate owners, stale doctrine and cross-repository contract drift.
