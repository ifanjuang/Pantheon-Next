# Card Stack static prototypes

Status: illustrative prototype — documented non-implemented.
Boundary profile: candidate_support_note.
Owner: `docs/governance/CARD_STACK_MODEL.md`.

This directory contains static UX projections used to test the Card Stack grammar without creating a production cockpit, renderer, interaction engine, approval engine or Hermes command surface.

Files:

- `VISUAL_LANGUAGE.md` — bounded visual-language guidance subordinate to `CARD_STACK_MODEL.md`;
- `visual-language.html` — accessible static demonstration of card anatomy, non-colour distinctions, status separation, navigation and local visual grouping;
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

The examples are deliberately static. Labels such as `Review`, `Inspect` or `Prepare action candidate` are review intents, not approvals, runtime commands or external effects.

Color is never the sole status carrier. Type, status, border pattern, structural marker and consequence are explicit in text. Real links and disclosure controls use semantic elements with visible keyboard focus.

## Shared visual grammar

```text
written kind
→ exact owner-defined status
→ title and scoped summary
→ consequence or risk
→ essential metadata
→ dominant relation
→ bounded review affordance
```

Compact cards use explicit reduced markup. They are not expanded cards hidden by clipping.

Human Decision cards separate:

```text
recorded
current
expiry
revocation
supersession
scope
```

## Navigation rule

```text
project selector or Constellation = global Project Space
primary tabs or rail = Scene
vertical order = Deck depth
horizontal group = siblings at the same level
tap or Enter = governed detail
bounded menu = review intent or Action Candidate preparation
```

Global and Scene navigation must not duplicate the same meaning.

## Scene rule

```text
Candidate Output
→ principal open Gate
→ strongest Evidence Candidate
→ compact Action Candidate and Source summaries
```

The Work Scene is complete enough for governed review. It is not an exhaustive graph or a stored workflow.

## Cluster boundary

`Cluster` is a local visual grouping construct only.

```text
Cluster != governance object
Cluster != graph node by default
Cluster != workflow
Cluster != authorization scope
```

## Boundary

No production UI, state machine, schema, workflow engine, runtime command, OpenWebUI plugin, Hermes skill, approval engine, memory engine or external action is implemented here.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```