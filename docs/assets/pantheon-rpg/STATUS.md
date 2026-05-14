# Pantheon RPG Visual System Status

Status date: 2026-05-14

This file tracks the working state of the Pantheon RPG visual system.

It is a documentation status note.

It is not governance doctrine and does not claim implementation.

## Current posture

Status: conceptual visual system scaffolded; composition-study prompt ready.

The directory now contains:

```text
docs/assets/pantheon-rpg/
  README.md
  STATUS.md
  prompts/
    README.md
    prompt-composition-study-v01.md
    prompt-master-poster-v01.md
    prompt-negative-v01.md
  iterations/
    README.md
  exports/
    README.md
  references/
    README.md
```

## Implemented in documentation

### Concept and roadmap

- `README.md` defines the visual system concept, strata, metaphor rules, risks, acceptance criteria and development roadmap.

### Prompt workspace

- `prompts/README.md` defines the prompt workspace and naming rules.
- `prompts/prompt-composition-study-v01.md` defines the first reduced composition study prompt.
- `prompts/prompt-master-poster-v01.md` defines the first full master poster prompt.
- `prompts/prompt-negative-v01.md` defines shared visual and doctrine drift exclusions.

### Image lifecycle folders

- `iterations/README.md` defines how to store work-in-progress and rejected image candidates.
- `exports/README.md` defines how to store validated final assets.
- `references/README.md` defines how to store non-confidential visual references and notes.

## Not implemented

No image has been generated or added.

No final visual asset has been validated.

No root `README.md` integration has been performed.

No runtime, workflow, scheduler, provider router, tool runtime, asset generation pipeline or automatic memory mechanism has been introduced.

## Phase status

| Phase | Name | Status |
|---|---|---|
| 0 | Concept lock | Partially complete |
| 1 | Master composition | In progress — composition study prompt ready |
| 2 | Cieux des Possibles | To do |
| 3 | Monde Extérieur and source routes | To do |
| 4 | Quais de Vérification and knowledge fields | To do |
| 5 | Cité de la Mémoire | To do |
| 6 | Conseil des Dieux | To do |
| 7 | Portals, domains, quests and side quests | To do |
| 8 | Ateliers Souterrains | To do |
| 9 | Final validation and save | To do |
| 10 | Image generation and iteration | To do |
| 11 | Asset drop | To do |
| 12 | Repository README integration | Deferred |

## Next action

Use `prompts/prompt-composition-study-v01.md` to generate a reduced layout candidate.

The candidate should be reviewed before using the dense master poster prompt.

## Review risks

### Overload risk

The master prompt contains the whole world. If the first result is unreadable, the visual system should split into four boards.

### Typography risk

Generated image typography will likely be imperfect. Final text should be overlaid manually after visual validation.

### Doctrine drift risk

Reject any image where gods, oracles or workshops appear to govern autonomously.

The player must remain the decision-maker.

### Memory confusion risk

Reject any image where boats, knowledge fields or portals flow directly into the memory palace without docks, validation or project scoping.
