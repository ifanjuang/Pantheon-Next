# 2026-07-23 — Cockpit information architecture

Status: validation-only intervention trace.
Boundary profile: validation_only_trace.

## Human decision

The maintainer selected the following candidate first-level Cockpit navigation:

```text
Pantheon
Affaires
Connaissances
Outils
Décisions
```

The accepted placement is:

- `Pantheon` is the landing page and contextual conversation with Hermes;
- `Affaires` owns professional Cases, their documents, Work Issues, Kanban projections and project-scoped knowledge;
- `Connaissances` owns general reusable knowledge;
- `Outils` exposes typed resource cards for skills, Hermes toolsets, plugins, MCP entries, connectors, models and profiles;
- `Décisions` exposes human questions, validations, approvals and arbitrations, including items that block Hermes continuation.

Kanban remains a view under `Affaires`, not a top-level runtime, queue or scheduler. One Work Issue or Decision may appear in conversation, Kanban and the Decisions inbox without identity duplication.

The maintainer also requested a governed skill-construction affordance. Hermes may prepare Skill Proposal Candidates from conversations, documents, repositories, existing skills, templates or repeated task-local patterns. Generation, declaration, validation, admission, installation, activation and task authorization remain distinct.

## Change

Added `docs/governance/PANTHEON_COCKPIT_INFORMATION_ARCHITECTURE.md` as candidate support doctrine.

The document specializes existing owners without replacing them:

- `PANTHEON_COCKPIT_UX_SPEC.md` for product UX;
- `CARD_STACK_MODEL.md` for Card and Scene grammar;
- `DECISION_SURFACE_SPEC.md` for decision review;
- `SKILL_LIFECYCLE.md` for skill states and gates;
- `HERMES_INTEGRATION.md` for execution boundaries.

## Status

```text
implemented:
  - documentation file
  - explicit dated human decision trace

documented non-implemented:
  - accepted five-space navigation
  - contextual Hermes landing page
  - Affaire/document/project-knowledge hierarchy
  - general Knowledge space
  - Outils resource catalogue
  - Decisions inbox
  - Decision/Kanban/Work Issue coupling
  - governed skill builder

to verify:
  - reconciliation with the external pantheon-mvp cockpit
  - exact OpenWebUI exposure
  - runtime inventory and mutation adapter
  - identity, scope and continuation contracts
```

## Responsibility allocation

```text
Pantheon governs status, scope, provenance, gates and consequential decisions.
Hermes executes conversation, skills, tools, plugins, MCP calls and bounded continuations.
OpenWebUI or another cockpit surface exposes the five spaces and their cards.
The human approves consequential changes and professional conclusions.
```

## Boundary

```text
navigation != runtime
Kanban != queue
Decision card != approval engine
skill proposal != installed skill
installed != activated
human response != observed execution
```

No UI, runtime, scheduler, queue, installer, plugin manager, MCP host, approval engine, memory engine, external action or protected-path change is introduced.
