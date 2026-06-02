# AI log — architecture target workflow synthesis PR

Date: 2026-06-03

## Scope

Created branch `docs/workflow-cible-examples` and added:

- `docs/governance/ARCHITECTURE_TARGET_WORKFLOWS.md`

The branch also starts from the previously added workflow examples and D3 assets:

- `docs/examples/architecture_cerfa_workflow/README.md`
- `docs/examples/architecture_invoice_visa_workflow/README.md`
- `docs/examples/architecture_site_photo_review_workflow/README.md`
- `docs/assets/pantheon-workflows/architecture_cerfa_rag_spine_d3.html`
- `docs/assets/pantheon-workflows/architecture_invoice_visa_spine_d3.html`
- `docs/assets/pantheon-workflows/architecture_site_photo_review_spine_d3.html`

## Purpose

Consolidate user-provided architecture agency examples into a candidate target workflow model.

The synthesis describes:

- OpenWebUI as the visible cockpit/interface;
- Hermes Agent as the execution workshop;
- Pantheon Next as the governance frame;
- target goals for architecture workflows;
- milestones M0-M7 for progressive delivery;
- composable workflow atoms;
- primitive workflows;
- composition rules;
- candidate connector families;
- candidate skills and tools;
- common quality gates;
- feedback loops;
- trace and memory decision;
- links to the three example workflows.

## Updates in this PR

Added sections to `ARCHITECTURE_TARGET_WORKFLOWS.md` for:

- target goals;
- implementation milestones;
- reusable workflow atoms;
- primitive workflows;
- composition rules.

The intent is to avoid treating rich examples as monolithic agents. Workflows should be decomposed into independently testable atoms and small reusable primitives that compose through the Task Contract / Result Candidate / Evidence Pack Candidate envelope.

## Primitive workflow additions

Added three primitive workflows:

1. Information collection workflow — classify the information type first, then select source families before retrieval.
2. Form filling workflow — identify form version and fields, map fields to sources, fill only certain fields and comment uncertain fields.
3. Comment and annotation workflow — make comments first-class outputs attached to fields, pages, plan zones or photo areas.

## Doctrine impact

No doctrine change.

The document remains candidate support material and explicitly says it does not implement a runtime, connector, OpenWebUI action, Hermes skill, Gmail sender, Telegram listener, WhatsApp integration, form filler, image analyzer, PDF exporter or memory engine.

## Repo state

Documented, non-implemented.

## Risk

Medium-low editorial risk: it names many tool families and future capabilities, so the document keeps them in a candidate integration/synthesis layer rather than generic doctrine.

## Follow-up

Review wording on candidate connectors and capabilities to ensure no implied implementation promise.

Review whether milestones M0-M7 and primitive workflows should remain in this candidate synthesis or move into a later roadmap / implementation planning document after arbitration.
