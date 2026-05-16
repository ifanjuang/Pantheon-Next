# AI Log — README front door and visual reading path refactor

Date: 2026-05-16

## Scope

Refactored the main English and French README files so the repository front door is clearer, shorter and more explicit about Pantheon Next's current status.

A second pass added a visual reading path using the intended RPG boards:

- Player;
- Worldmap;
- Port;
- Citadel;
- Evidence;
- Livrables;
- Pantheon.

## Files changed

- `README.md`
- `README.fr.md`
- `ai_logs/2026-05-16-readme-frontdoor-refactor.md`

## Why

The previous README contained useful product framing, but it mixed several layers:

- public product introduction;
- governance doctrine;
- narrative city-game explanation;
- integration posture;
- roadmap and implementation status;
- external channel framing.

That made the first read heavier than necessary and increased the risk that target capabilities could be mistaken for implemented runtime behavior.

The visual layer also needed a clearer reader path. A single citadel image was not enough to explain the journey from user intent to external information, governed intake, evidence, deliverables and Pantheon roles.

## Changes

The README structure now emphasizes:

- current repository status at the top;
- Pantheon Next as a governance and documentation layer;
- the central boundary: `OpenWebUI exposes. Hermes Agent executes. Pantheon Next governs.`;
- what the repository is and is not;
- the three-surface operating model;
- the professional loop from user request to approved output or Memory Candidate;
- core governance objects;
- Pantheon Roles as governance viewpoints, not autonomous agents;
- the separation between source, knowledge, context, evidence and memory;
- everyday tools as governed entry points, not automatic truth sources;
- implementation status and absent areas;
- key governance entry points.

The visual reading path now follows the user journey:

```text
Player
→ Worldmap
→ Port
→ Citadel
→ Evidence
→ Livrables
→ Pantheon
```

Existing images are embedded where present:

- `docs/assets/pantheon-rpg/references/player_01.jpg`;
- `docs/assets/pantheon-rpg/references/worldmap_01.jpg`;
- `docs/assets/pantheon-rpg/references/port_01.jpg`;
- `docs/assets/pantheon-rpg/references/citadel_01.jpg`;
- `docs/assets/pantheon-rpg/references/olympus_01.jpg`;
- and their French equivalents.

Missing boards are marked as images to produce instead of being embedded as broken links:

- `docs/assets/pantheon-rpg/references/evidence_01.jpg`;
- `docs/assets/pantheon-rpg/references/livrables_01.jpg`;
- `docs/assets/pantheon-rpg/references/evidence_01_fr.jpg`;
- `docs/assets/pantheon-rpg/references/livrables_01_fr.jpg`.

The French README was kept aligned with the English README.

## Boundary check

This is documentation-only.

No runtime was introduced.

No endpoint was introduced.

No provider router was introduced.

No scheduler, queue, message bus, LangGraph runtime, plugin manager, tool runtime, automatic skill installer or automatic memory promotion mechanism was introduced.

No claim was made that OpenWebUI integration, Hermes runtime integration, generated Evidence Packs, Memory Candidate UI, schemas, tests, operations tooling or deployment stack are implemented.

The missing Evidence and Livrables boards are explicitly marked as images to produce, not existing assets.

## Risks and limitations

- The README still references target governed entry points. These remain target or future surfaces unless separately implemented in the external execution layer.
- `STATUS.md` remains the authority for current repository state.
- Some governance files still have stub or contradictory status and must be reconciled separately.
- This pass did not modify protected areas such as `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md`.

## Status

Implemented as a documentation refactor.

Implementation claims remain intentionally conservative.
