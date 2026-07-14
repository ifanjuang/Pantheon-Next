# Card Stack static prototypes

Status: illustrative prototype — documented non-implemented.
Boundary profile: candidate_support_note.
Owner: `docs/governance/CARD_STACK_MODEL.md`.

This directory contains static UX projections used to test the Card Stack grammar without creating a production cockpit, renderer, interaction engine, approval engine or Hermes command surface.

Files:

- `card-type-variations.html` — shared card anatomy with controlled variations by governed type;
- `mobile-work-scene.html` — answer-first mobile Work Scene with explicit compact cards and a single scene navigation.

## Prototype rules

```text
Card projection != governed object
Scene != exhaustive graph
Gate != Decision
Action Candidate != authorized action
recorded != current
UI affordance != Hermes command
```

The examples are deliberately static. Labels such as `Review`, `Inspect` or `Resolve` are displayed as non-interactive affordance examples, not working controls.

Color is never the sole status carrier. Type, status and consequence are written in text. The prototypes include visible focus treatment for the only real links: navigation between the two static examples.

## Scene rule

```text
Candidate Output
→ principal open Gate
→ strongest Evidence Candidate
→ compact Action Candidate and Source summaries
```

The Work Scene is complete enough for governed review. It is not an exhaustive graph or a stored workflow.

## Boundary

No production UI, state machine, schema, workflow engine, runtime command, OpenWebUI plugin, Hermes skill, approval engine, memory engine or external action is implemented here.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```