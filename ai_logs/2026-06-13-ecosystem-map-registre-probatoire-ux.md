# AI log — Ecosystem map realigned around Registre Probatoire

Date: 2026-06-13.

## Request

The maintainer asked for a deeper correction of the ecosystem HTML map and related examples so users feel why Pantheon governance is necessary.

Specific points:

- stop showing `memory` as the bottom layer of the ecosystem;
- use `Registre Probatoire` / evidence register vocabulary instead;
- avoid pie-chart / camembert composition;
- use narrower rectangles so lateral and return arrows remain legible;
- add a professional example where Hermes runtime memory conflicts with the Registre Probatoire before a project decision email can be sent;
- consider Notion synchronization without making Notion the probative authority.

## Canonical sources checked

Read path and related active material were checked before the edit:

- `docs/governance/STATUS.md`;
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`;
- `docs/governance/CAPABILITY_PLACEMENT.md`;
- `docs/governance/DOMAIN_PACK_SPEC.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/REGISTRE_PROBATOIRE_DIRECTION.md`;
- `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md`;
- `docs/governance/DATA_PLATFORM_RECONCILIATION.md`;
- recent PRs #107, #116 and #117 for Registre schema state, mcp-server CI, and dashboard UX doctrine.

## Changes made

- Replaced `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html` with a rectangular layered ecosystem map:
  - Surface;
  - Law / Gate;
  - Execution;
  - Proof / Registre.
- Replaced the bottom `Mémoire` object with `Registre Probatoire — ce qui peut être cité`.
- Added `Mémoire Hermes — rappel sans autorité` as a separate execution-runtime object.
- Added Notion / database view as optional synchronized cockpit, not source of truth.
- Added a visible refused shortcut: `Hermes memory -> client commitment`.
- Updated `docs/assets/pantheon-map/README.md` to reflect Registre Probatoire vocabulary and the new boundary.
- Added `docs/examples/architecture_decision_memory_vs_registre/README.md` as a fictional architecture decision example.
- Updated `docs/examples/README.md` to index the new example and include it in the reading path.

## Decision posture

Accepted:

- `Memory` at the bottom of the ecosystem map was misleading.
- The governed durable object is the Registre Probatoire.
- Runtime memory may recall but must not be cited for consequential decisions.
- Notion can be a synchronized view or cockpit, but not probative authority by default.

Refused:

- Pie / camembert ecosystem composition.
- Direct `memory -> action` shortcuts.
- Treating Notion rows, database rows or runtime memory as proof by themselves.

To verify:

- Root README and older visual / dashboard assets may still contain educational wording around `memory` that should be swept separately if the maintainer wants a corpus-wide public-facing UX pass.
- Pantheon Control mockup labels `Base & Mémoire` / `Evidence → Mémoire` may need a follow-up vocabulary pass because PR #117 deliberately used that taxonomy before this request.

## Boundary

Documentation and visual asset update only.

No schema, test, mcp-server, operation, platform, Docker, environment file, runtime, Notion integration, database synchronization, approval engine, Registre storage or external-action implementation was added.

Repo state: documented non-implemented.
