# Pantheon RPG Visual System Status

Status date: 2026-05-15

This file tracks the working state of the Pantheon RPG visual system.

It is a documentation status note.

It is not governance doctrine and does not claim implementation.

## Current posture

Status: visual system scaffolded; planche 2 design direction accepted; binary export identified and documented; repository PNG drop pending binary-capable upload path.

The directory now contains:

```text
docs/assets/pantheon-rpg/
  README.md
  STATUS.md
  prompts/
    README.md
    prompt-composition-study-v01.md
    prompt-master-poster-v01.md
    prompt-city-memory-v01.md
    prompt-negative-v01.md
  iterations/
    README.md
  exports/
    README.md
    pantheon-rpg-city-memory-v01.provenance.md
  references/
    README.md
```

The final PNG binary is not yet committed to this directory.

## Current export candidate

The accepted planche 2 candidate has been identified and recorded in provenance.

```text
Local generated file: /mnt/data/isometric_map_of_a_medieval_city_complex.png
Planned repository path: docs/assets/pantheon-rpg/exports/pantheon-rpg-city-memory-v01.png
Format: PNG
Dimensions: 1448 x 1086 px
Size: 3,448,189 bytes
SHA256: 7200154131d9e071700975c8d71769cabefc997ea4ecbbbe927d274c32bed80e
```

## Implemented in documentation

### Concept and roadmap

- `README.md` defines the visual system concept, strata, metaphor rules, risks, acceptance criteria and development roadmap.

### Prompt workspace

- `prompts/README.md` defines the prompt workspace and naming rules.
- `prompts/prompt-composition-study-v01.md` defines the first reduced composition study prompt.
- `prompts/prompt-master-poster-v01.md` defines the first full master poster prompt.
- `prompts/prompt-city-memory-v01.md` defines the accepted visual direction for planche 2, the governed memory city.
- `prompts/prompt-negative-v01.md` defines shared visual and doctrine drift exclusions.

### Image lifecycle folders

- `iterations/README.md` defines how to store work-in-progress and rejected image candidates.
- `exports/README.md` defines how to store validated final assets.
- `exports/pantheon-rpg-city-memory-v01.provenance.md` records the accepted planche 2 visual direction, candidate metadata and pending binary export location.
- `references/README.md` defines how to store non-confidential visual references and notes.

## Accepted visual direction

### Planche 2 — Governed Memory City

Status: accepted design direction; export candidate identified.

The board currently documents:

- a standalone planche 2, not a full stacked poster;
- an isometric Mediterranean / Greek-antique visual language;
- a city scale close to the selected reference map, with smaller buildings and more natural context;
- direct function labels near buildings and zones instead of a large separate legend panel;
- hierarchy by proximity: port, palace, temple, production quarter, project-memory quarters and peripheral knowledge/template landscape;
- `Palace of System Memory` as core validated memory;
- `Temple of Invocation` for calling companions and roles;
- `Pantheon of Manifests` for order, rules and priorities;
- `Project Memory` quarters as scoped project memory areas;
- `Port of External Sources` and `Quays & Docks` as external source intake;
- `Knowledge Pastures` as living knowledge;
- `Templates & Documents Fields` as reusable models and document grounds;
- `Library of Logic & Methods` as methods and reasoning support;
- `Portico of Proof` as evidence and validation layer;
- `Forge of Skills`, `Armory of Skills`, `Workflow Atelier` and `Context Atelier` as the production / capability district;
- `House of Deliverables`, `Theater of Communication` and `Pigeonry of Messages` as output and transmission functions;
- `Road of Possibilities` as an extra-muros exploration direction.

## Not implemented

No binary image file has been committed to the repository yet.

No root `README.md` integration has been performed.

No runtime, workflow, scheduler, provider router, tool runtime, asset generation pipeline or automatic memory mechanism has been introduced.

## Phase status

| Phase | Name | Status |
|---|---|---|
| 0 | Concept lock | Partially complete |
| 1 | Master composition | In progress |
| 2 | Cieux des Possibles | To do |
| 3 | Monde Extérieur and source routes | To do |
| 4 | Quais de Vérification and knowledge fields | To do |
| 5 | Cité de la Mémoire | Accepted direction for planche 2; export candidate documented |
| 6 | Conseil des Dieux | To do |
| 7 | Portals, domains, quests and side quests | To do |
| 8 | Ateliers Souterrains | To do |
| 9 | Final validation and save | To do |
| 10 | Image generation and iteration | In progress |
| 11 | Asset drop | Provenance updated; PNG binary pending |
| 12 | Repository README integration | Deferred |

## Next action

Commit the binary PNG at the planned export path when a binary-capable repository upload path is available:

```text
docs/assets/pantheon-rpg/exports/pantheon-rpg-city-memory-v01.png
```

After the PNG is committed, update `exports/pantheon-rpg-city-memory-v01.provenance.md` to `Review status: accepted export committed`.

Then move to the next board.

Recommended next board options:

1. `Monde des Possibles` — upper exploration map and professional domains.
2. `Ateliers / Fondations` — underground support, manifests, skill forging and deliverables.
3. `Quais & Sources` — maritime source intake and verification logic.

## Review risks

### Typography risk

Generated image typography may require manual correction before final publication.

### Doctrine drift risk

Reject any image where gods, oracles, workshops or foundations appear to govern autonomously.

The player / human validation model must remain central in the broader poster series.

### Memory confusion risk

Reject any image where source intake, knowledge fields or templates flow directly into system memory without validation and scoping.
