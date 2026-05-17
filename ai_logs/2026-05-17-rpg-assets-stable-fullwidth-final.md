# AI Log — RPG assets stable names and full-width README layout

Date: 2026-05-17

## Scope

Completed the Pantheon RPG asset rename and README presentation pass.

The README now uses stable semantic image paths and displays the RPG boards vertically with:

```text
title
full-width image
description
asset path
```

## Files affected

- `README.md`
- `docs/assets/pantheon-rpg/ASSET_REGISTER.md`
- `docs/assets/pantheon-rpg/RENAME_ASSETS.md`
- `docs/assets/pantheon-rpg/references/*.jpg`
- `ai_logs/2026-05-17-rpg-assets-stable-fullwidth-final.md`

## Final stable board paths

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

## Former raw paths removed from public references

The repository search no longer returns references to:

```text
IMG_1452.jpeg
IMG_1448.jpeg
IMG_1446.jpeg
IMG_1451.jpeg
IMG_1450.jpeg
IMG_1457.jpeg
IMG_1449.jpeg
IMG_1455.jpeg
IMG_1454.jpeg
```

## README layout

The previous two-column table layout was replaced by a full-width image layout.

Reason:

- better visual impact;
- better mobile readability;
- clearer sequence for non-technical readers;
- title and description no longer compete with the image.

## Boundary check

This intervention is asset hygiene and README presentation only.

It does not implement:

- runtime behavior;
- OpenWebUI integration;
- Hermes integration;
- Evidence Pack generation;
- memory promotion;
- provider routing;
- plugin management;
- execution tooling.

## Remaining visual task

The missing board remains:

```text
docs/assets/pantheon-rpg/references/livrables_01_fr.jpg
```

Optional later work:

```text
*_en.jpg
*_bi.jpg
```
