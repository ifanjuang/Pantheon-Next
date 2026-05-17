# Pantheon RPG Asset Rename Plan

Status: executed — historical asset hygiene note.

This file records the completed safe binary rename pass for Pantheon RPG README assets.

The README now uses stable semantic asset names.

The former raw `IMG_*.jpeg` filenames should not be reintroduced as public README paths.

## Why this exists

Binary image renaming must be done with Git-safe binary operations such as `git mv` or Git tree blob reuse.

Do not rewrite binary JPG/JPEG files through a text-only API.

Do not copy base64 manually unless the binary integrity is verified.

## Executed mapping

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

## Current stable paths

```text
docs/assets/pantheon-rpg/references/before_after_01_fr.jpg
docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg
docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg
docs/assets/pantheon-rpg/references/port_01_fr.jpg
docs/assets/pantheon-rpg/references/evidence_01_fr.jpg
docs/assets/pantheon-rpg/references/citadel_01_fr.jpg
docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg
docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg
docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg
```

## README display rule

The README displays these boards vertically:

```text
title
full-width image
description
asset path
```

This is intentional.

The previous two-column table layout was removed because full-width images are more readable on GitHub and mobile.

## Future additions

Missing target board:

```text
docs/assets/pantheon-rpg/references/livrables_01_fr.jpg
```

Optional future variants:

```text
*_en.jpg
*_bi.jpg
```

## Boundary check

This pass did not modify:

- governance doctrine;
- runtime code;
- schemas;
- operations;
- tests;
- OpenWebUI integration;
- Hermes integration.

It was an asset hygiene and README presentation pass only.
