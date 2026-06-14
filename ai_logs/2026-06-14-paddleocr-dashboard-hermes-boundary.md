# AI Log — PaddleOCR dashboard-installable / Hermes-managed boundary

Date: 2026-06-14

## Context

The user reviewed `PaddlePaddle/PaddleOCR` as a possible OCR / document intelligence capability for Pantheon Next.

Initial direction was to create a short placement note and then define a benchmark. The user refined the boundary:

```text
Juste la possibilité de l’installer dans dashboard et laisser hermes gérer.
```

This means the change should not introduce a dedicated heavy PaddleOCR doctrine note, a Pantheon dependency, or a Pantheon-owned OCR module.

## Repository reading

The active governance documents were reviewed before the change:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Relevant existing doctrine confirmed:

- Pantheon Next is governance-first and not an execution runtime.
- The exposure surface exposes.
- The execution runtime executes.
- Pantheon governs.
- Document extraction and OCR belong in the execution runtime or deterministic preparation layer.
- Pantheon governs status, evidence, approval, scope and memory, not the extraction engine.

Related repository material checked:

- `docs/governance/DOCUMENT_INTELLIGENCE.md`
- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`
- Issue #33, which already covers governed document intelligence.
- Issue #90, which warns against adding new reference fiches during backlog sequencing.

## Decision

Accepted with constraints:

```text
PaddleOCR may be represented as a dashboard-installable Hermes-managed capability candidate.
```

Refused:

```text
PaddleOCR as Pantheon dependency.
PaddleOCR as Pantheon doctrine core.
PaddleOCR as proof engine.
PaddleOCR output as validated truth.
A dedicated standalone PaddleOCR doctrine note at this stage.
```

To verify:

```text
Actual Hermes installation path.
OCR quality on architecture documents.
Table extraction reliability.
Version/hash/provenance capture.
Failure and confidence reporting.
```

To arbitrate later:

```text
Whether PaddleOCR becomes one option among several document extraction backends, or the default local OCR backend for Hermes.
```

## Change made

Updated:

- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`

Added PaddleOCR as:

```text
dashboard-installable, Hermes-managed document extraction candidate; no Pantheon dependency.
```

The note states that the dashboard may expose:

```text
install via Hermes;
configure;
check health;
view logs;
run benchmark;
show capability gap when unavailable.
```

Hermes may install and run PaddleOCR, but outputs remain:

```text
Document Source
-> Extraction Candidate
-> Fragment Candidate
-> Evidence Pack Candidate
```

## Benchmark orientation

Minimum benchmark before operational use:

```text
CERFA;
mairie arrêté;
devis;
chantier compte rendu;
tableau de surfaces.
```

Benchmark result remains `Candidate / to verify` until reviewed.

## Boundary state

Documented non implemented.

No runtime, dashboard implementation, Hermes skill, installer, connector, schema, test, Docker, operations file or dependency was added.

## Process note

This was applied directly to `main` because the change was limited to an allowed governance Markdown register and AI log. The repo issue #41 preference for PR-based work remains noted for larger or structural changes.
