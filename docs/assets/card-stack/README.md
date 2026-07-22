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

## External implementation example

The implemented cards-first frontend is owned by the external `ifanjuang/pantheon-mvp` candidate, not by this directory.

Pinned observation:

```text
repository: ifanjuang/pantheon-mvp
commit: 4ee41a845ec51db3118a584db0411a300450ccbd
demo source: mvp_vertical/cockpit/demo.html
runtime path when the external MVP is served: /cockpit/demo.html
```

Links:

- [static no-network demo source](https://github.com/ifanjuang/pantheon-mvp/blob/4ee41a845ec51db3118a584db0411a300450ccbd/mvp_vertical/cockpit/demo.html);
- [actual cockpit CSS and JavaScript assets](https://github.com/ifanjuang/pantheon-mvp/tree/4ee41a845ec51db3118a584db0411a300450ccbd/mvp_vertical/cockpit).

The external demo loads the real MVP `styles/index.css`, `app.js`, `resources.js`, `effects.js` and `knowledge_updates.js`, then injects synthetic fixtures through `demo.js`. Network access is disabled before those scripts run.

Pantheon Next does not copy, serve or activate these assets. This repository keeps only the link and governance classification.

```text
linked implementation != local runtime
same frontend assets != same operational status
demo loaded != installed or healthy
demo button != authorized effect
```

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
