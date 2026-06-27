# AI Log — Card Stack Model candidate

Date: 2026-06-27

## Change

Created `docs/governance/CARD_STACK_MODEL.md` as candidate support doctrine and explicit review draft.

Updated:

- `docs/governance/README.md` — added `CARD_STACK_MODEL.md` to the short read path, core bootstrap path, conceptual read path and a new `Card stack and cockpit UX model` section.

## Model captured

The new document formalizes a reversible candidate model for cockpit cards and scenes:

```text
Cards are unique objects.
Scenes are filtered and ordered presentations.
The Workflow Scene is exhaustive for the cards used in a treatment.
The Evidence Scene is scoped by project and subject.
The Competence Scene is global, neutral and not project-owned.
The Constellation is the map used to change project and understand the graph.
Gates are the decision surfaces.
```

It also documents:

- project -> subject -> workflow navigation;
- Workflow Scene as a complete narrative of cards actually mobilized;
- Evidence Scene as project/subject-scoped;
- Competence Scene as global and neutral, organized by competence subject and maturity;
- competence-on-the-flow and promotion candidates;
- recto/verso card display rules;
- card family display table;
- roles/gods, rites and places as UX-visible cards without creating agents/runtime;
- complexity budget;
- open review questions for Claude / ChatGPT / human arbitration.

## Boundary

Documentation only.

No UI, mobile app, Swiper component, dashboard, frontend route, card renderer, state machine, runtime, workflow engine, graph database, scheduler, queue, skill generator, competence engine, evidence engine, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill, connector or external action was implemented.

No protected paths were modified.

## Authority Index note

`docs/governance/AUTHORITY_INDEX.md` was not modified in this pass.

Reason: the available write tool replaces the full file. Because the file is large and the fetched output was truncated, a full replacement would have risked accidental line loss. The document should be indexed in a follow-up pass when the full file can be safely patched or replaced.

Repo state for `CARD_STACK_MODEL.md` is therefore documented candidate, visible in README, but Authority Index indexing remains a follow-up action.

## Repo state

Documented non-implemented.

## Follow-up

- Review with Claude and ChatGPT.
- Decide whether `Scene` replaces `Game` in UX doctrine.
- Decide whether horizontal swipe is always sibling subjects.
- Decide whether Workflow Scene groups traces by default.
- Decide whether Competence Scene is global-only or also appears as an overlay from project workflows.
- Index `CARD_STACK_MODEL.md` in `AUTHORITY_INDEX.md` once the full file can be safely patched.
- Formalize Card Stack Model further only after conceptual review.
