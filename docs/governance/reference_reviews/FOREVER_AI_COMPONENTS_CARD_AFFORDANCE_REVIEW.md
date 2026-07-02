# Forever AI Components — Card Affordance Review

Status: external reference / candidate distillation — UX inspiration only.

Review date: 2026-07-02

Source reviewed:

```text
https://github.com/isas1/forever-ai-components
https://raw.githubusercontent.com/isas1/forever-ai-components/main/agents.json
https://raw.githubusercontent.com/isas1/forever-ai-components/main/infinite/facets.json
```

This document reviews `isas1/forever-ai-components` as an external inspiration for the Pantheon card cockpit.

It does not import the repository, add a dependency, create a component registry, create a UI renderer, create a Swiper integration, modify the dashboard, create an OpenWebUI Function, create a Hermes skill, create a runtime, create a state machine, create a schema, create a database, create an approval engine or change `CARD_STACK_MODEL.md` by itself.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Why this reference is useful

Forever AI Components frames its components as a structured design knowledge base for AI coding agents. Its useful pattern is not the visual style itself.

The useful pattern is:

```text
registry -> facets -> retrieval -> selected component -> embedded adaptation guidance -> output rationale
```

Pantheon should not copy the visual library directly. Pantheon can reuse the registry logic to make cockpit cards more playful, manipulable and context-sensitive without weakening governance boundaries.

## Accepted distillation

Accepted:

```text
A Pantheon card may be playful, tactile and engaging.
A Pantheon card may use visual affordances to help orientation, comparison, learning and decision quality.
A Pantheon card should carry machine-readable guidance about when it is useful, when it must not be used, which actions are possible and which actions remain forbidden.
A Pantheon card stack may be selected by situation, not by a fixed page menu.
External visual component registries may inspire rendering patterns when filtered through Pantheon placement rules.
```

Candidate Pantheon translation:

```text
Forever component registry
-> Pantheon card affordance registry

UI intent
-> professional situation

component facets
-> governance facets

component metadata
-> card affordance metadata

retrieve component
-> expose the minimal legitimate affordance

rendering quality gate
-> governance and status quality gate
```

## Refused distillation

Refused:

```text
Forever is not a Pantheon dependency.
A visual component is not a governance object.
A component registry is not an approval registry.
A motion effect is not status.
A card animation is not evidence.
A component selection is not role arbitration.
A visual affordance is not authorization.
A rendered card is not a truth source.
A card stack is not a workflow runtime.
A draggable gesture is not execution.
```

The exposure surface may render a card. It must not redefine what the card means.

## Core candidate idea: governed affordance

A governed affordance is a possibility of interaction made visible because the current status, scope, evidence state, risk level and approval requirement allow that interaction.

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

The cockpit should therefore be playful in manipulation and strict in consequence.

```text
Playful does not mean permissive.
Ludique ne veut pas dire permissif.
```

## Playful governance

Pantheon should not look like a cold administrative back office. It should feel like a living decision table: cards can be opened, flipped, compared, dragged, pinned, promoted as candidates, sent to a gate, attached to evidence or parked in a trace.

Playfulness is allowed when it improves:

```text
orientation;
attention;
comparison;
learning;
review quality;
decision quality;
mobile manipulation;
understanding of status;
understanding of risk.
```

Playfulness is forbidden when it:

```text
hides status;
weakens evidence hierarchy;
hides risk;
makes an unavailable action feel available;
turns a candidate into a validated object visually;
turns a role/god card into an agent character;
turns a rite into a workflow runner;
turns an action candidate into an executed action;
turns a memory candidate into canonical memory.
```

## Suggested card-affordance metadata

This is a candidate shape only, not a schema.

```yaml
card_affordance:
  id:
  card_family: project | subject | run | task | document | connaissance | evidence | decision | record | competence | method | role | rite | constellation
  surface_role: orient | compare | inspect | decide | block | trace | learn | prepare
  governance_meaning:
  use_when:
  avoid_when:
  status_axes:
    process_status:
    governance_status:
    evidence_state:
    risk_axis:
    approval_level:
  allowed_interactions:
    tap:
    long_press:
    swipe_horizontal:
    swipe_vertical:
    drag_targets:
  forbidden_interactions:
  gate_required:
  evidence_required:
  memory_behavior:
  external_effect_behavior:
  visual_discipline:
    density:
    motion:
    reduced_motion_required: true
    mobile_primary: true
    status_must_remain_visible: true
  failure_modes:
```

The field is deliberately called `card_affordance`, not `component`, because the governed possibility matters more than the visual object.

## Governance facets

Forever filters components by facets such as role, technique, style, motion, interaction, accessibility, performance and labels. Pantheon should filter card affordances by governance facets first.

Candidate governance facets:

```yaml
risk_level: low | medium | high | critical
effect_type: none | truth | memory | external_action | doctrine | approval
evidence_state: absent | weak | sufficient | strong | contradicted
governance_status: candidate | to_verify | gate_open | validated | refused | out_of_scope
process_status: waiting | processing | success | error
authority_surface: user | role | college | zeus | human
scope: task | dossier | project | domain | organization
reversibility: reversible | costly | irreversible
visibility: private | project | client_facing | external
approval_level: C0 | C1 | C2 | C3 | C4 | C5
motion_level: none | subtle | expressive | blocked
mobile_posture: primary | secondary | desktop_only
```

Visual facets may exist, but they must be downstream of governance facets.

## Gesture discipline

Gestures may be playful only if their effect is bounded.

```text
Tap
-> read / flip / inspect.

Long press
-> open quick actions, never auto-validate.

Swipe horizontal
-> sibling card or branch at same level.

Swipe vertical
-> deck depth / hierarchy.

Drag to Zeus
-> request arbitration, not validation.

Drag to Evidence
-> attach or request evidence, not prove.

Drag to Memory
-> create or review memory candidate, not canonize.

Drag to Action
-> prepare an action candidate, not execute.
```

Rule:

```text
The gesture proposes.
The gate constrains.
The human decides.
The trace preserves.
```

## Card personalities without role confusion

The cards may have visual character, but not autonomous character.

Allowed:

```text
Evidence card feels like a proof object.
Gate card feels like a threshold.
Competence card feels like a reusable tool.
Rite card feels procedural.
Role card feels like an expressed review quality.
Trace card feels stable and archived.
```

Forbidden:

```text
Zeus as autonomous agent.
Athena as chatbot persona.
Hermes as authority.
Rite as executable workflow.
Competence as automatically installed skill.
Evidence as proof without source and status.
```

## Rendering adapter boundary

External visual libraries may inspire rendering, but only at the rendering layer.

```text
Pantheon owns card meaning.
CARD_STACK_MODEL.md owns card-stack grammar.
This reference review proposes card-affordance distillation.
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

## Candidate stack behavior

A situation should retrieve the smallest useful card stack, not display the whole cockpit.

Example: external client transmission.

```text
Situation: draft message may commit the professional externally.
Stack:
  context card;
  result candidate card;
  evidence card;
  risk card;
  action candidate card;
  gate Zeus / user decision card;
  trace card.
Landing view:
  draft output + main gate + top evidence.
Full deck:
  available on demand.
```

Example: competence-on-the-flow.

```text
Situation: repeated useful maneuver appears during a task.
Stack:
  need / gap card;
  competence candidate card;
  examples card;
  test / failure-mode card;
  promotion gate card;
  trace card.
Forbidden:
  automatic promotion to durable competence.
```

## Compatibility with existing doctrine

This review must remain compatible with:

```text
docs/governance/CARD_STACK_MODEL.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/DOMAIN_PACK_SPEC.md
docs/governance/DECISION_SURFACE_SPEC.md
docs/governance/CARD_STACK_ROLE_QUALITY_ALIGNMENT.md
```

It reinforces the existing boundary that the exposure surface may show, warn, label, collect decisions, display Evidence Packs and open gates, but must not become governance authority or automatic approval surface.

## Decision classification

Accepted:

```text
Use Forever as an external inspiration for registry, facets, retrieval protocol, embedded adaptation metadata and quality gates.
Use the phrase governed affordance for card interactions made visible by status, evidence, risk, scope and approval.
Keep the card cockpit playful, tactile and engaging.
```

Refused:

```text
No dependency adoption.
No component import.
No runtime or UI implementation.
No status change based on rendering.
No role/god card as agent character.
No action by gesture alone.
```

To verify:

```text
Whether this distillation should later be folded into CARD_STACK_MODEL.md.
Whether a separate CARD_AFFORDANCE_REGISTRY_SPEC.md is useful or too much doctrine sprawl.
Whether the prototype should test three visual affordance levels: sober, playful, ceremonial.
Whether gesture semantics need a dedicated mobile prototype before promotion.
```

To arbitrate:

```text
Whether the card-affordance metadata belongs in CARD_STACK_MODEL.md, DECISION_SURFACE_SPEC.md, an adapter document, or a future schema only after validation.
Whether playful governance should become a named sub-section of CARD_STACK_MODEL.md.
```

## Boundary

This file is a reference review and candidate distillation only.

It creates no UI, no renderer, no component dependency, no schema, no state machine, no database, no OpenWebUI extension, no Hermes skill, no approval engine, no memory engine, no runtime and no external action.

The validated remains.
