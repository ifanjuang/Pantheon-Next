# Card Stack Model reconciliation

Date: 2026-07-12
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

`docs/governance/CARD_STACK_MODEL.md` was reduced and reconciled against the current owner documents.

The previous draft mixed cockpit grammar, object model, lifecycle vocabulary, project architecture, detailed walkthroughs and quasi-data specifications across more than one thousand lines.

The revised document keeps the useful UX grammar while removing competing ownership.

## Corrections applied

- Card is defined as a stable cockpit projection of one identifiable governed entity or record.
- Scene remains a filtered ordered presentation; Deck remains vertical reading depth inside a Scene.
- `Pantheon project` is replaced with `Governance Reference Space`.
- the Work Scene is a bounded review projection rather than an exhaustive graph;
- primary navigation is reduced to Work, Evidence, Assets, Decisions, Trace and a separate Reference Space;
- Constellation is a global mode, not a peer project Scene;
- Gate and Decision remain distinct;
- status values are owner-defined and only projected by cards;
- Evidence Candidate and accepted evidence are not collapsed;
- long press prepares bounded intents or candidates and cannot directly merge, archive, approve, send, install, activate or promote memory;
- the Current Decision Resolver is upstream of the Card Stack;
- UI intent cannot silently become Hermes execution;
- owner-document and non-equivalence boundaries are explicit.

## Classification

```text
implemented:
- revised documentation;
- this validation trace.

partial:
- existing static and read-only prototype surfaces.

documented non-implemented:
- production Card Stack UI;
- Scene/Deck state implementation;
- authenticated decision surface;
- current-decision projection;
- live Hermes handoff integration.

promotion:
- not requested.
```

## Boundary

No UI, renderer, graph runtime, workflow engine, scheduler, queue, approval engine, memory engine, Hermes skill, connector, external action or lifecycle migration is introduced.

## Local distinctions

```text
card_projection != object_ownership
scene != workflow
deck != scene_sequence
Gate != Decision
UI_intent != runtime_command
CI_green != doctrine_promotion
merged != promoted
```
