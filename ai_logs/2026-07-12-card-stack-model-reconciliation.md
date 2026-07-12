# Card Stack Model reconciliation

Date: 2026-07-12
Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

`docs/governance/CARD_STACK_MODEL.md` was reduced and reconciled against the current owner documents.

The previous draft mixed cockpit grammar, object model, lifecycle vocabulary, project architecture, detailed walkthroughs and quasi-data specifications across more than one thousand lines. It also contained two alignment notes absorbed verbatim during an earlier governance cleanup.

The first reduction pass was intentionally reverted to draft posture after review showed that deliberate truncation acknowledgment did not prove semantic completeness. A second section-by-section audit then preserved the unique rules from those absorbed notes in compact owner-aligned sections.

## Corrections applied

- Card is a stable cockpit projection of one identifiable governed entity or record.
- Scene remains a filtered ordered presentation; Deck remains vertical reading depth inside a Scene.
- `Pantheon project` is replaced with `Governance Reference Space`.
- project-level `Run` usage is removed; `Run` remains reserved for runtime execution instances.
- Work is a bounded review projection rather than an exhaustive graph.
- primary navigation is reduced to Work, Evidence, Assets, Decisions, Trace and a separate Reference Space.
- Constellation is a global mode, not a peer project Scene.
- Gate and Decision remain distinct.
- status values are owner-defined and only projected by cards.
- `recorded != admitted_memory` is replaced by Register-aligned distinctions.
- long press prepares bounded intents or candidates and cannot directly merge, archive, approve, send, install, activate or promote memory.
- the Current Decision Resolver is upstream of the Card Stack.
- UI intent cannot silently become Hermes execution.

## Preserved unique material

The semantic reduction audit retained the unique substance of the absorbed alignment sections:

```text
knowledge-corpus alignment
→ Source / reusable knowledge / Evidence / Register separation

role-quality alignment
→ visibility threshold, non-agent boundary and compact role-quality projection

workflow examples
→ answer-first default and minimum first-prototype set

card inflation guidance
→ field-versus-sub-card rule and core invariants
```

Detailed legacy walkthroughs remain recoverable from repository history. They were not retained in the compact model because they are examples rather than owner doctrine.

## Classification

```text
implemented:
- revised documentation;
- explicit semantic reduction audit;
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
Run != governance treatment
record_present != Register Entry
UI_intent != runtime_command
CI_green != doctrine_promotion
merged != promoted
```
