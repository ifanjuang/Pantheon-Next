# Pantheon RPG Prompts

Status: working prompt workspace — not governance doctrine.

This directory stores image-generation prompts and visual briefing notes for the Pantheon RPG visual system.

Prompts are design artifacts. They do not define implementation, runtime behavior, governance authority or canonical doctrine.

## Naming convention

Current prompt identities are responsibility-based and stable:

```text
prompt-composition-study.md
prompt-master-poster.md
prompt-city-memory.md
prompt-source-world.md
prompt-underground-workshops.md
prompt-council-gods.md
prompt-negative.md
```

A prompt revision belongs inside the document metadata and Git history. It does not create a permanent generation-named path.

## Prompt file structure

Each prompt should include:

- document revision;
- purpose;
- scope;
- composition intent;
- required visual elements;
- forbidden visual drift;
- negative prompt;
- known risks;
- review checklist.

## Current prompt set

```text
prompt-composition-study.md
prompt-master-poster.md
prompt-city-memory.md
prompt-negative.md
```

## Recommended usage order

1. Use `prompt-composition-study.md` to validate the four-strata spatial structure and readability.
2. Use `prompt-master-poster.md` only after the reduced composition is accepted.
3. Use secondary board prompts after master composition review.

The first priority is to stabilize the visual map before adding all micro-details.

## Prompt roles

### Composition study

A reduced layout prompt for testing the vertical map, source boundaries, memory city, underground craft layer and final validation logic.

### Master poster

A dense complete-poster prompt for testing the full visual world after the composition study has clarified the spatial hierarchy.

### Negative prompt

A shared exclusion prompt preventing drift toward medieval fantasy, SaaS dashboards, technical stack diagrams, backend imagery or autonomous runtime metaphors.
