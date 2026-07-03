# Forever AI Components — Card Affordance Review

Status: external reference / candidate distillation — UX inspiration only.

Review date: 2026-07-03

Source reviewed:

```text
https://github.com/isas1/forever-ai-components
```

This document reviews `isas1/forever-ai-components` as an external inspiration for the Pantheon card cockpit.

It does not import the repository, add a dependency, create a component registry, create a UI renderer, create a Swiper integration, modify the dashboard, create an OpenWebUI Function, create a Hermes skill, create a runtime, create a state machine, create a schema, create a database, create an approval engine or change `CARD_STACK_MODEL.md` by itself.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Useful pattern

The useful pattern is not the visual style itself.

The useful pattern is:

```text
registry -> facets -> retrieval -> selected component -> embedded adaptation guidance -> output rationale
```

Pantheon should not copy the visual library directly. Pantheon may reuse the registry logic to make cockpit cards more playful, manipulable and context-sensitive without weakening governance boundaries.

## Candidate distillation

Candidate phrase:

```text
governed affordance
```

A governed affordance is a visible possibility of interaction made available because the current status, scope, evidence state, risk level and approval requirement allow that interaction.

```text
The card exposes an affordance.
The stack organizes attention.
The gate constrains consequence.
Pantheon governs meaning.
The renderer only renders.
```

French working formula:

```text
La carte expose une possibilité.
Le stack organise l'attention.
Le gate contraint la conséquence.
Pantheon gouverne le sens.
Le rendu ne fait qu'afficher.
```

The cockpit may be playful in manipulation and strict in consequence.

```text
Playful does not mean permissive.
Ludique ne veut pas dire permissif.
```

## Accepted

```text
Forever AI Components may inspire registry logic, facets, retrieval protocol, embedded adaptation metadata and quality gates.
Pantheon may translate that into governed card affordances.
Cards may be playful, tactile and engaging when this improves orientation, comparison, learning, review quality or decision quality.
A card stack may be selected by situation rather than by a fixed page menu.
```

## Refused

```text
Forever is not a Pantheon dependency.
A visual component is not a governance object.
A component registry is not an approval registry.
A motion effect is not status.
+A card animation is not evidence.
A component selection is not role arbitration.
A visual affordance is not authorization.
A rendered card is not a truth source.
A card stack is not a workflow runtime.
A gesture is not execution.
```

## Gesture discipline

Gestures may be playful only if their effect is bounded.

```text
Tap -> read / flip / inspect.
Long press -> open quick actions, never auto-validate.
Swipe horizontal -> sibling card or branch at same level.
Swipe vertical -> deck depth / hierarchy.
Drag to Zeus -> request arbitration, not validation.
Drag to Evidence -> attach or request evidence, not prove.
Drag to Memory -> create or review memory candidate, not canonize.
Drag to Action -> prepare an action candidate, not execute.
```

Rule:

```text
The gesture proposes.
The gate constrains.
The human decides.
The trace preserves.
```

## Rendering adapter boundary

External visual libraries may inspire rendering, but only at the rendering layer.

```text
Pantheon owns card meaning.
CARD_STACK_MODEL.md owns card-stack grammar.
This review proposes card-affordance distillation.
The exposure surface owns rendering.
External UI libraries may inspire component appearance.
Hermes may prepare candidates under Task Contract.
Zeus / the human decide consequential status.
```

Any future adapter to a visual component registry must obey:

```text
1. No external registry is a source of doctrine.
2. No component metadata overrides Pantheon status.
3. No animation hides the status, gate or evidence state.
4. No visual affordance exposes a forbidden action.
5. Components are pinned by commit or vendored if used in a prototype.
6. Reduced motion handling is mandatory.
7. Mobile touch fallback is mandatory.
8. Cheap / accessible / mobile-ready components are preferred.
```

## To verify

```text
Whether this distillation should later be folded into CARD_STACK_MODEL.md.
Whether a separate CARD_AFFORDANCE_REGISTRY_SPEC.md would be useful or too much doctrine sprawl.
Whether the prototype should test three visual affordance levels: sober, playful, ceremonial.
Whether gesture semantics need mobile testing before promotion.
```

## To arbitrate

```text
Whether card-affordance metadata belongs in CARD_STACK_MODEL.md, DECISION_SURFACE_SPEC.md, an adapter document, or a future schema after validation.
Whether playful governance should become a named subsection of CARD_STACK_MODEL.md.
```

## Boundary

This file is a reference review and candidate distillation only.

It creates no UI, no renderer, no component dependency, no schema, no state machine, no database, no OpenWebUI extension, no Hermes skill, no approval engine, no memory engine, no runtime and no external action.

The validated remains.
