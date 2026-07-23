# Assets Registry

Status: active support index — documentation assets only.

This directory indexes visual and explanatory assets used to make Pantheon Next understandable.

It is not runtime.

It is not a source of truth by itself.

It does not implement OpenWebUI, Hermes, OCR, vision, Notion sync, workflow execution, Registre Probatoire storage, approval, scheduling or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The Registre Probatoire proves.
The human decides.
```

## Current assets

| Asset | Purpose | Status |
|---|---|---|
| [`pantheon-map/`](pantheon-map/) | Interactive ecosystem map: surface, governance, execution, evidence and Registre Probatoire. | Visual support; documentation only. |
| [`workflow-under-hood/`](workflow-under-hood/) | Architecture workflow-under-the-hood explainer: situation intake, workflow candidate, OCR / vision / plan review, evidence gaps and user gate. | Visual support; documentation only. |
| [`pantheon-control/`](pantheon-control/) | Static Pantheon Control dashboard mockup for modules, services, IA, skills, proofs and files. | Visual support; documentation only. |
| [`card-stack/`](card-stack/) | Static Card Stack type variations and answer-first mobile Work Scene derived from `CARD_STACK_MODEL.md`. | Illustrative prototype; documented non-implemented; no executable controls. |
| [External MVP cockpit demo](https://ifanjuang.github.io/pantheon-mvp/) | Public no-network synthetic-data demonstration using the actual `pantheon-mvp` cockpit assets. Source observed at [`7f3faf74afd59a07a9ab6026360881eb374df905`](https://github.com/ifanjuang/pantheon-mvp/tree/7f3faf74afd59a07a9ab6026360881eb374df905); direct path after static publication: `/pantheon-mvp/mvp_vertical/cockpit/demo.html`. | Implemented externally and publicly targeted; linked only; not copied, installed, served or activated by Pantheon Next. Public deployment remains to verify independently. |
| [`pantheon-flow/entrees-sorties-memoire-d3.html`](pantheon-flow/entrees-sorties-memoire-d3.html) | D3.js explanatory flow for entries, context minimization, IA workflow, candidate result, human decision, external action and governed memory. | Visual support; documentation only. |
| [`pantheon-rpg/`](pantheon-rpg/) | Narrative / illustrative material for before-after and responsibility path visuals. | Visual support; documentation only. |

## Use rule

Assets may explain:

- responsibility boundaries;
- workflow phases;
- role viewpoints;
- evidence and register distinctions;
- candidate outputs;
- review gates;
- user decision points.

Assets must not imply that a feature is implemented when it is only documented.

If an asset shows a button, flow, module, connector, AI action or workflow, it must remain clear whether that element is:

```text
implemented
documented non-implemented
candidate
validation-only
external reference
voluntarily absent
refused
```

## Public landing and cockpit wording

Public pages must not present `pantheon-control/` as a live cockpit or control plane.

Preferred public labels:

```text
Maquette cockpit
Maquette Pantheon Control
Prototype statique
```

Avoid unqualified labels such as:

```text
Cockpit
Control plane
Dashboard live
Services en ligne
Connexions actives
```

unless the same visible block makes clear that the state is declared, fictive, static or a target behaviour.

`docs/index.html` is still a monolithic landing page. Do not hand-edit it broadly for wording cleanup. Extract or refactor shared labels/components first, then align its public cockpit links with this rule.

## Registre and memory wording

Visual assets should avoid using `memory` as the bottom source-of-truth layer.

Preferred distinction:

```text
Hermes memory = runtime recall without authority.
Registre Probatoire = governed evidence register that may be cited after validation.
```

Notion, databases or cockpit views may mirror or expose records.

They do not become probative by display.

## Workflow visual rule

When showing a professional workflow, prefer this simple surface path:

```text
Question
→ Dossier Situation Brief
→ Sources
→ Analysis
→ Impacts
→ Questions
→ Human decision
```

And this under-the-hood path:

```text
Dossier Situation Intake
→ Workflow Candidate
→ role review
→ Zeus procedural arbitration
→ governed execution handoff
→ Hermes execution
→ Result Candidate + Evidence Pack Candidate
→ review / approval / rejection
```

## Anti-runtime reminder

This directory holds documentation assets only.

It contains no runtime resources, deployment artifacts, generated runtime configuration, approval engine, memory engine or external-action component.
