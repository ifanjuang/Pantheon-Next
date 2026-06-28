# AI Log — Card Stack Navigation and Methods

Date: 2026-06-28

Actor: ChatGPT

## Context

Human arbitration corrected the mobile navigation model:

```text
vertical axis = ascend / descend hierarchy
horizontal axis = sibling cards
```

A verification also found that `CARD_STACK_MODEL.md` still missed Method / Reasoning cards as task-level fields and sub-cards, despite the new Method Card model and Architecture Method Deck.

## Change made

Updated `docs/governance/CARD_STACK_MODEL.md` to:

- add `Methods / Reasoning` to the Pantheon reference project;
- state that tasks mobilize roles, methods, competences, rites, documents, evidences and decisions;
- define Method in Pantheon vs Method in a task;
- add Method to visible sub-card rules;
- add method references and Method Proposal Candidates to Task Cards;
- add a dedicated `Method inside a task` section;
- add method-triggered spawned cards;
- change navigation to:
  - Up -> ascend hierarchy;
  - Down -> descend hierarchy;
  - Left -> previous sibling card;
  - Right -> next sibling card.

## Boundary preserved

Documentation only.

No schema, test, runtime, UI, renderer, state machine, workflow engine, method selector, reasoning engine, approval engine, memory engine, Hermes skill, connector, platform file, operations file, Docker file, environment file or external action was added.

## Repo state

Documented non-implemented.

Note: the branch is currently diverged from `main` and must be reconciled before merge.

## Decision status

Accepted:

- vertical navigation for hierarchy;
- horizontal navigation for sibling cards;
- methods as task fields, Method Proposal Candidates and visible sub-cards when they carry process state.

To verify:

- reconcile branch with current `main` before merge;
- test whether the method sub-card model creates too much UI density on mobile.
