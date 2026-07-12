# Card Stack type variations

Status: illustrative prototype — documented non-implemented.
Boundary profile: candidate_support_note.

This folder contains static visual candidates derived from `docs/governance/CARD_STACK_MODEL.md`.

Files:

- `card-type-variations.html` — shared anatomy with controlled variations by governed type;
- `mobile-work-scene.html` — answer-first mobile Work Scene showing real Deck order.

The prototypes cover:

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

## Scene rule

```text
Candidate Output first
→ main open Gate
→ strongest supporting or contradicting Evidence
→ lower-priority Action Candidates and Sources
```

The Scene is complete enough for governed review. It is not an exhaustive graph.

## Boundary

The HTML files are static prototypes only. They introduce no production UI, renderer, state machine, design-system package, schema, workflow engine, runtime command, approval engine, memory engine or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```
