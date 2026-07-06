# Card Stack Hardening Note

Status: candidate support note — documented non-implemented.

Related issue: #293.

Applies to: `docs/governance/CARD_STACK_MODEL.md`.

Runtime status: non-executable.

This note refines `CARD_STACK_MODEL.md` without replacing it. It is a hardening note for card inflation, place/scene separation, context/evidence boundaries and competence-resource projections.

It does not implement a UI, renderer, route, state machine, schema, test, approval engine, memory engine, OpenWebUI plugin, Hermes skill, connector or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## 1. Do not replace the current backbone

The current backbone remains valid:

```text
Project -> Scene -> Deck -> Card / sub-card
```

The subject remains a scope label, not a navigation level.

The Workflow Scene remains exhaustive for the cards mobilized in a treatment.

The Evidence Scene remains scoped by project and subject.

Competence and Method scenes remain global and neutral.

The Constellation remains an orientation view, not the main decision surface.

Gates remain decision surfaces.

## 2. Lieu / Scene / Deck / Card

`CARD_STACK_MODEL.md` already distinguishes scenes, decks, cards and constellation. The cockpit also needs a stable mental-location layer.

Recommended distinction:

```text
Lieu       = stable cockpit workspace.
Scene      = active view inside a lieu.
Deck       = vertical reading / depth order inside a scene.
Card       = governed entity.
Sub-card   = incident, blocker, proposal, repeated signal or visible tension.
```

A `Lieu` is not a runtime container.

A `Lieu` is not a module.

A `Lieu` is not a project.

A `Lieu` is the user-facing workspace that answers:

```text
Where am I working?
```

Suggested mapping:

| Lieu | Scenes | Function |
|---|---|---|
| Atelier | Workflow, Actions, Draft Output | produce and review candidate work |
| Agora | Gates, Arbitrages, Contradictions, Questions ouvertes | expose tensions and decisions |
| Bibliothèque | Documents, Connaissances, Guides, Ressources, Templates | find reusable and source material without making it proof |
| Registre | Traces, Memory Candidates, Register Entries | see what was kept, refused, validated or superseded |
| Constellation | Projects, dependencies, tensions, major links | orient globally without deciding |

This prevents the cockpit from collapsing into a flat list of scenes.

## 3. Cardinal card-versus-field rule

A card does not appear because a concept exists.

A card appears because a concept changes the conduct of the case.

```text
Field if normal.
Visible card or sub-card if it orients, works, blocks, fails, repeats,
is newly proposed, changes scope, changes evidence, changes action,
or requires arbitration.
```

Examples:

| Object | Normal state | Visible card / sub-card trigger |
|---|---|---|
| Role | field on Task Card | role conflict, blocker, handoff, useful dissent |
| Method | method reference | proposed, contested, failed, repeated, changes proof/scope/action |
| Competence | competence reference | missing, failed, proposed on the flow, productive output requested |
| Rite | rite reference | proof gap, mission limit, responsibility issue, pre-transmission check |
| Template | template reference | inappropriate, dangerous, contested, creates misleading output |
| Resource | resource reference | stale, authoritative ambiguity, missing version, license/scope issue |
| Context | context field | missing, stale, mixed scope, excessive or blocks the output |
| Gate | badge | blocks truth, memory, external action or professional commitment |
| Action | field or badge | candidate effect becomes ready, blocked, consequential or external |

Core UX sentence:

```text
The card is not a documentary sheet.
The card is a governed conduct unit.
It appears when something must be seen, decided, verified, blocked, linked or transmitted.
```

## 4. Role / God cards remain exceptional

There should be no Role / God card by default.

A role card appears only when a judgment tension becomes useful to see.

```text
ATHENA normal structuring -> field.
ARGOS normal source review -> field.
THEMIS normal risk review -> field.
APOLLO normal clarity review -> field.
IRIS normal transmission formatting -> field.
HEPHAISTOS normal artifact preparation -> field.
ZEUS normal status badge -> gate or arbitration field.
```

Visible role-quality cards are justified only when the role changes the treatment:

```text
ARGOS detects a source gap.
THEMIS blocks external transmission.
APOLLO flags delivery unreadiness.
IRIS identifies recipient over-disclosure.
HEPHAISTOS detects unsafe fabrication conditions.
ZEUS arbitrates unresolved status or procedure.
```

This preserves the Governance College boundary: roles are separated review responsibilities, not autonomous agents.

## 5. Guide / Ressource / Template cards

`COMPETENCE_MODEL.md` separates competence vocabulary. The card stack should project that separation without turning library material into proof.

Recommended projection:

| Card | Meaning | Must not become |
|---|---|---|
| Connaissance Card | professional, regulatory, contractual, project or dossier knowledge | skill, template, evidence by itself |
| Guide Card | method for learning or applying a competence | validated method by itself |
| Ressource Card | documentation, example, link, snapshot, distillation, dataset or snippet | proof by itself |
| Template Card | reusable form for producing a candidate output | validated content |
| Competence Card | governed reusable ability to produce candidates | runtime skill or approval |
| Evidence Card | support for a specific assertion | general context or memory by itself |
| Action Card | prepared effect | authorized external action |
| Gate Card | decision surface or blocker | execution engine |

Forbidden collapses:

```text
Template filled ≠ truth.
Guide used ≠ method validated.
Resource found ≠ proof.
Competence executed ≠ approved result.
Evidence candidate ≠ proof.
Action prepared ≠ external action authorized.
Gate visible ≠ decision taken.
```

## 6. Context Card is not Evidence Card

`CONTEXT_STACK.md` projects naturally into the Card Stack, but it must not become a parallel proof model.

Recommended distinction:

```text
Context Card = why the work can be framed in this perimeter.
Evidence Card = why an assertion can be reviewed.
Gate Card = why a decision is possible or blocked.
```

A Context Card may say:

```text
This is the active project, phase, location, typology, risk and expected output.
```

It must not say:

```text
This claim is proven.
This source is validated.
This output may be sent.
This fact may enter memory.
```

Context prepares work.

Evidence supports review.

Approval legitimizes consequential change.

Memory preserves validated material.

## 7. Three views of one card

A card should not try to show everything in one face.

Recommended invariant:

```text
Recto = quick comprehension.
Verso = governed detail.
Constellation = relations.
```

Recto answers:

```text
What is it?
Which scope?
Which status?
Which risk?
What blocks or continues?
```

Verso answers:

```text
Why?
With which sources?
Which links?
Which history?
Which limits?
Which possible actions?
```

Constellation answers:

```text
What is it linked to?
What does it affect?
Which gate blocks what?
Which evidence supports what?
```

The recto must remain a five-second read.

The verso must remain reviewable.

The constellation must remain an orientation and impact view, not a decision engine.

## 8. Workflow scene remains answer-first

The Workflow Scene may be exhaustive for a treatment, but it should not display the whole dossier by default.

Default landing should remain:

```text
Draft Output + main Gate + top Evidence.
```

The full deck remains available on demand.

Comprehensiveness is available.

Comprehensiveness is not the landing screen.

## 9. Non-goals

This note does not authorize:

```text
schema creation;
UI implementation;
renderer creation;
state-machine creation;
OpenWebUI plugin behavior;
Hermes skill behavior;
connector behavior;
automatic approval;
automatic memory promotion;
one card per concept;
one card per god;
replacement of CARD_STACK_MODEL.md;
replacement of PANTHEON_COCKPIT_UX_SPEC.md;
replacement of CONTEXT_STACK.md;
replacement of COMPETENCE_MODEL.md.
```

## 10. Patch guidance for CARD_STACK_MODEL.md

A later direct patch to `CARD_STACK_MODEL.md` should be small:

1. Add `Lieu / Scene / Deck / Card` after the hard rule.
2. Move or reinforce the card-versus-field rule before card-family enumeration.
3. Add `Guide / Ressource / Template Cards` near card families.
4. Add `Context Card is not Evidence Card` near relationships with other documents.
5. Keep the existing navigation backbone.

No protected path should be touched.

## Final rule

```text
Pantheon does not win by showing more cards.
Pantheon wins by showing the card that changes the conduct of the case.
```
