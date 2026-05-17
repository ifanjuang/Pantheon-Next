# AI Log — Pantheon RPG asset rename plan

Date: 2026-05-17

## Scope

Added a safe local rename plan for Pantheon RPG binary image assets.

The README already points to the correct user-identified image boards, but those files currently use temporary raw names such as `IMG_1452.jpeg`.

This intervention documents how to rename them with `git mv` into stable semantic names without rewriting or corrupting JPEG binaries.

## Files changed

- `docs/assets/pantheon-rpg/RENAME_ASSETS.md`
- `docs/assets/pantheon-rpg/references/README.md`
- `ai_logs/2026-05-17-rpg-asset-rename-plan.md`

## Why

The available repository write path is safe for text files but not ideal for binary JPEG copy/rename.

Rather than risk corrupting image files by rewriting binary content through a text-oriented API, the rename has been formalized as a local Git plan.

## Rename targets

```text
IMG_1452.jpeg → before_after_01_fr.jpg
IMG_1448.jpeg → ui_hermes_pantheon_01_fr.jpg
IMG_1446.jpeg → player_journey_01_fr.jpg
IMG_1451.jpeg → port_01_fr.jpg
IMG_1450.jpeg → evidence_01_fr.jpg
IMG_1457.jpeg → citadel_01_fr.jpg
IMG_1449.jpeg → memory_compartment_01_fr.jpg
IMG_1455.jpeg → pantheon_system_summary_01_fr.jpg
IMG_1454.jpeg → worldmap_ai_internet_01_fr.jpg
```

## Added guidance

`RENAME_ASSETS.md` includes:

- `git mv` commands;
- README path replacements;
- one-shot Python text replacement helper;
- verification script for missing or suspiciously small images;
- suggested commit message;
- boundary check.

## Boundary check

This intervention is asset hygiene documentation only.

It does not implement:

- runtime behavior;
- OpenWebUI integration;
- Hermes integration;
- Evidence Pack generation;
- memory promotion;
- provider routing;
- plugin management;
- execution tooling.

## Status

Rename plan documented.

Physical binary rename not executed in this pass.
