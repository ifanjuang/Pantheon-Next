# Card Stack type variations

Status: illustrative prototype — documented non-implemented.
Boundary profile: candidate_support_note.

This folder contains a static visual candidate derived from `docs/governance/CARD_STACK_MODEL.md`.

It explores one shared card anatomy with controlled variations for:

- Context;
- Source;
- Evidence Candidate;
- Candidate Output;
- Action Candidate;
- Gate;
- Human Decision;
- Trace;
- reusable Reference.

## Design rule

```text
same anatomy
+ same interaction grammar
+ controlled type variation
!= one unrelated design per card family
```

Variation may use:

- accent hue;
- border weight;
- typography emphasis;
- information density;
- icon or glyph;
- consequence indicator.

Variation must not alter:

- underlying status ownership;
- interaction meaning;
- Gate and Decision separation;
- evidence semantics;
- authorization semantics;
- runtime boundaries.

Color is never the sole status carrier.

## Boundary

The HTML is a static prototype only. It introduces no production UI, renderer, state machine, design-system package, schema, workflow engine, runtime command, approval engine, memory engine or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```
