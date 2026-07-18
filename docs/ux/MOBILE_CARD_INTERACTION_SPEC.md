# Mobile Card Interaction Specification

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines a mobile interaction grammar for the existing Card Stack model. It does not introduce a new ontology, runtime, workflow engine, scheduler, queue, approval engine, memory engine, plugin manager or execution authority.

```text
OpenWebUI exposes and animates.
Pantheon Next governs.
Hermes Agent executes authorized handoffs.
The human decides consequential matters.
```

If this document conflicts with an owner document, the owner document wins.

## 1. Relationship to the Card Stack model

The definitions in `docs/governance/CARD_STACK_MODEL.md` remain authoritative:

```text
Card
= stable cockpit projection of one identifiable governed entity or record.

Scene
= filtered and ordered presentation of Cards for one review purpose.

Deck
= reading and depth order inside a Scene.

Constellation
= global relation view and project-switching surface.
```

This specification adds a mobile projection concept:

```text
Mobile Focus Card
= the Card currently projected as the primary full-viewport object inside a Scene.
```

A Mobile Focus Card is not a new governed object and does not duplicate the identity of the underlying entity.

## 2. Core interaction doctrine

```text
One focused Card occupies one mobile viewport.
The normal reading model does not rely on page scrolling.
Navigation gestures express bounded UI intent.
No gesture directly authorizes or performs a consequential action.
```

Long or materially distinct content should normally become:

- another Card;
- a bounded detail projection;
- a source excerpt;
- or a controlled opening of the original.

Accessible overflow remains permitted when required by viewport size, localization, text enlargement, assistive technology or system UI constraints.

## 3. Universal mobile grammar

```text
Swipe left / right
= browse comparable Cards in the current Scene.

Tap on a visible Door
= open the relation or bounded detail represented by that Door.

Swipe down
= return to the previous navigation context.

Swipe up
= open the Tactical Overlay without changing the active object.

Hold
= open the Action Deck.
```

Every gesture must have a visible, accessible alternative.

```text
Swipe left / right
↔ previous / next controls when required.

Tap Door
↔ explicit labelled control.

Swipe down
↔ visible back control.

Swipe up
↔ visible context control.

Hold
↔ visible Actions control.
```

## 4. Horizontal browsing

Horizontal movement is reserved for comparable Cards in the same bounded Scene.

Examples:

```text
Source 2 of 8
Decision 1 of 3
Capability binding 4 of 6
```

Requirements:

- the neighboring Card must be previewed during drag;
- the active axis must lock early;
- the transition must require a deliberate distance or velocity threshold;
- incomplete movement must return to the current Card;
- a gesture must never perform approval, rejection, deletion, sending, installation, activation or execution.

## 5. Doors

A Door is a presentation affordance derived from an existing governed relation or bounded projection rule.

```text
existing relation or permitted projection
→ Door calculation
→ visible Door
```

A Door is not by default:

- a PostgreSQL governance object;
- a new relation;
- an authorization;
- an execution request;
- a task instruction.

A Door should expose enough information to make its destination predictable:

- human-readable label;
- target family or purpose;
- count where relevant;
- exact status when consequential;
- warning or unresolved condition where relevant.

Examples:

```text
Sources · 8
Contradictions · 2 open
Decision required
Hermes result available
Original document
```

Door prioritization must be bounded by the current Scene purpose. The interface must not attempt to expose the complete graph on one Card.

## 6. Navigation path and return

Mobile navigation uses the current navigation path, not an assumed ontological parent.

```text
Project
→ subject
→ Source
→ Evidence Candidate
```

Swipe down or the visible back control removes the current navigation layer and restores the exact preceding context.

The navigation path may be retained as session state. Session restoration does not convert an unconfirmed choice into a Decision, approval, handoff or durable governed record.

## 7. Tactical Overlay

Swipe up opens a temporary Tactical Overlay above the active Focus Card.

The overlay does not replace the current object and must preserve the user's position.

The first implementation is limited to:

1. current navigation path;
2. position inside the current Scene;
3. critical governed statuses;
4. open Gates and contradictions;
5. relevant Hermes activity;
6. prioritized nearby navigation targets.

The Tactical Overlay must not become a hidden general dashboard, administration console, runtime controller, complete memory browser or complete graph explorer.

The overlay may provide navigation shortcuts, but selecting a shortcut remains an explicit navigation intent and never an authorization.

## 8. Action Deck

Hold or the visible Actions control opens the same contextual Action Deck.

The Action Deck must distinguish at least three effect families.

### 8.1 Local or session effects

Examples:

- select a Door;
- adjust presentation;
- retain a local navigation preference;
- pin a Card for the current review.

These do not become governed truth merely because the interface stores them.

### 8.2 Pantheon-governed writes

Examples:

- propose a relation;
- signal a contradiction;
- create or update a candidate qualification;
- open a Gate;
- record a human Decision within scope;
- propose memory or register material.

These operations must preserve identity, actor, scope, status, provenance and applicable Gate requirements.

### 8.3 Hermes handoff candidates

Examples:

- analyze a document;
- query a connector;
- test a candidate binding;
- export a bounded result;
- prepare an external action.

The Action Deck may create an Action Candidate or prepare a handoff. Hermes executes only an explicitly authorized handoff.

```text
PostgreSQL row present
!= execution instruction

handoff selected
!= dependency adopted

runtime success
!= evidence
```

Each consequential action must expose before confirmation:

- intended effect;
- scope;
- target;
- externality;
- Gate state;
- required approver;
- rollback or reversibility where applicable.

## 9. Feedback and motion semantics

Motion communicates navigation and state; it does not redefine governance.

Recommended semantics:

```text
horizontal translation
= browse comparable Cards

forward depth transition
= enter a Door

layer withdrawal
= return to previous context

overlay rise
= inspect tactical context

bottom panel rise
= inspect available actions
```

Feedback must reflect the exact state achieved.

```text
request prepared
!= request authorized

request authorized
!= execution started

execution completed
!= result trusted

result available
!= evidence retained

healthy
!= safe

update available
!= update authorized
```

Animations, haptics and sound must never imply approval, safety, proof or completion when only an intermediate status has been reached.

## 10. Discoverability and accessibility

The gesture system must be learnable without requiring a manual.

Requirements:

- contextual first-use guidance;
- visible alternatives to all custom gestures;
- support for keyboard, switch, assistive and reduced-motion interaction where applicable;
- no reliance on color alone;
- no essential information available only through haptics;
- no consequential action available only through Hold;
- no gesture triggered from an interactive child control unless that control explicitly owns it.

The interface must respect reduced-motion preferences and provide equivalent state changes without spatial animation.

## 11. Gesture conflict rules

Swipe down is available only when:

- a prior navigation context exists;
- no modal, drawer or Tactical Overlay currently owns the gesture;
- the gesture starts from a non-interactive region or designated handle;
- vertical intent is established beyond the axis-lock threshold.

Swipe up is available only when:

- the Tactical Overlay is permitted for the current projection;
- no child control or system interaction owns the gesture;
- the current viewport can preserve the active Card context.

Horizontal browsing must not activate while the user is manipulating text selection, a control, media, an embedded source viewer or an accessibility element.

## 12. Projection boundaries

### Pantheon governs

- which Cards and Doors may be exposed;
- exact governed statuses;
- Gates, Decisions, scope and authorization state;
- whether an Action Candidate or handoff is admissible;
- traceability of consequential writes.

### Hermes executes

- authorized bounded handoffs;
- connector or capability operations;
- runtime work outside Pantheon.

Hermes does not infer authorization from UI position, a gesture, a Door, a selected binding or a database row alone.

### OpenWebUI exposes

- Mobile Focus Cards;
- Scenes and horizontal browsing;
- Doors;
- Tactical Overlay;
- Action Deck;
- motion, haptic and accessibility feedback;
- exact statuses supplied by Pantheon and Hermes projections.

OpenWebUI does not decide truth, approval, adoption, activation or evidence status.

### The human approves

- consequential external actions;
- scoped Decisions;
- installation or activation when required;
- adoption of dependencies or bindings when required;
- promotion into durable memory or registers when required;
- exceptions and risk acceptance.

### Forbidden

Pantheon must not become:

- runtime;
- scheduler;
- queue;
- provider router;
- MCP host;
- plugin manager;
- generic installer;
- memory engine;
- automatic approval engine.

## 13. Candidate prototype journeys

The first prototype should test at least these journeys:

```text
Project
→ subject
→ Source
→ Evidence Candidate
```

```text
Project
→ Gate
→ Decision Surface
```

```text
Capability Slot
→ candidate Hermes binding
→ installation status
→ Health Observation
→ update state
→ activation candidate
→ Pantheon Gates
```

```text
Action Candidate
→ Gate
→ human Decision
→ Authorized Handoff
→ Hermes execution
→ Execution Result Candidate
```

## 14. Prototype acceptance criteria

The candidate grammar should not be promoted until tests show that users can reliably:

- distinguish horizontal browsing from entering a Door;
- predict Door destinations before opening them;
- understand swipe down as return through the current path;
- discover the Tactical Overlay;
- discover the visible Actions control without being taught Hold first;
- distinguish local effects, governed writes and Hermes handoffs;
- identify exact status without relying on animation or color;
- recover from incomplete or accidental gestures;
- use the critical flows with reduced motion and accessibility alternatives.

## 15. Current status

```text
Card Stack doctrine
= documented non-implemented

Mobile Focus Card
= documented candidate

Horizontal browsing
= documented candidate, prototype required

Door interaction
= documented candidate, prototype required

Swipe-down return
= documented candidate, usability verification required

Tactical Overlay
= documented candidate, prototype required

Action Deck
= documented candidate, prototype required

Motion and haptics
= documented principles only

Runtime implementation
= not implemented by this document
```

This specification governs a candidate interaction projection only. It creates no schema, UI implementation, runtime behavior, background task, installation, activation, approval or external action.