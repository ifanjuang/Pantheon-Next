# AI log — landing detailed iterative D3 diagram

Date: 2026-06-03

## Scope

Added a second, more detailed D3 diagram to `docs/index.html`, placed lower on the
page (new section `#detail`). The first dossier-flow diagram is kept as the simple,
pedagogical view; the new one shows the real governed, iterative cycle.

## Changes

- New section `Pour aller plus loin — Le même chemin, vu en détail : un cycle qui itère.`
- New D3 diagram `#flowDetail` (second inline script), rendered into a dark canvas
  inside a horizontally scrollable container (`.diagram.scroll`) so the dense schema
  stays legible on phones (scroll rather than shrink).
- HTML legend (`.dlegend`) for loops, node nature and honesty status (responsive).
- Added a `Détail` link in the top navigation.
- The diagram encodes only what the governance Markdown already states:
  - Corpus is the matter at the top (fed by web sources and internal connections),
    filtered by `Contexte` before the engine;
  - `Travail IA` shows the Governance College as judgment roles (not autonomous
    agents) producing candidates under Task Contract: MÈTIS, ATHENA, ARGOS,
    HÉPHAÏSTOS, THÉMIS, APOLLON, IRIS, with ZEUS arbitrating;
  - workflow authority modes `off → … → durable` ("never automatic by birth");
  - skills shown explicitly as `documenté · NON IMPLÉMENTÉ` (SKILL_LIFECYCLE.md stub);
  - Evidence Pack as auditable proof; candidate result; human decision gate;
  - two validated outputs: Action (transmitted, leaves the frame) and Memory
    (candidate → CERBÈRE/CHARON threshold → canonical);
  - four iteration loops: internal bounded (ZEUS → MÈTIS), quality/proof
    insufficient → corpus, human refusal → corpus, validated memory → back to base.

## Sources of truth consulted

`GOVERNANCE_COLLEGE.md`, `USER_DECISION_GATE.md`, `REQUEST_LIFECYCLE.md`,
`DATA_PLATFORM_ARCHITECTURE.md`, `DOCUMENT_INTELLIGENCE.md`, `MEMORY.md`,
`WORKFLOW_LIFECYCLE.md`, `SKILL_LIFECYCLE.md`, `EVIDENCE_PACK.md`,
`hermes/profiles/*` souls.

## Doctrine impact

No doctrine change. The diagram is a documentation surface that reflects existing
governance Markdown.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Repo state

Documented, non-implemented. The diagram describes governance; it implements no
runtime. Skills are labelled non-implemented to stay honest.

## Risk

Low. Modified only `docs/index.html` and this AI log. Both inline D3 scripts are
guarded (`typeof d3`, `svg.empty()`) and degrade to a no-op when the CDN is blocked.
The diagram script was rendered in a headless DOM (jsdom + d3) to verify output.

## Follow-up

Review rendered GitHub Pages output on desktop and phone. Optionally add a true
mobile stacked reflow of the detailed diagram if horizontal scroll proves awkward.
