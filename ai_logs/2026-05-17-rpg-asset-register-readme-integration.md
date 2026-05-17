# AI Log — Pantheon RPG asset register and README integration

Date: 2026-05-17

## Scope

Reviewed and classified current Pantheon RPG JPG/JPEG assets for README use.

Created and updated an asset register.

Updated the README visual reading path to use the user-identified French board images currently present in `docs/assets/pantheon-rpg/references/`.

## Files changed

- `docs/assets/pantheon-rpg/ASSET_REGISTER.md`
- `docs/assets/pantheon-rpg/references/README.md`
- `README.md`
- `ai_logs/2026-05-17-rpg-asset-register-readme-integration.md`

## User-provided asset identification

The user identified the following raw image files:

```text
IMG_1446.jpeg → parcours joueur entre requêtes et livrable
IMG_1448.jpeg → qui fait quoi
IMG_1449.jpeg → compartimentage de la mémoire
IMG_1450.jpeg → evidence atelier
IMG_1451.jpeg → port
IMG_1452.jpeg → avant / après, second version, better
IMG_1454.jpeg → world map with AI side and Internet side
IMG_1455.jpeg → résumé système Pantheon
IMG_1457.jpeg → citadelle
```

## Asset register changes

`ASSET_REGISTER.md` now records:

- current raw paths;
- target stable names;
- README roles;
- language status;
- user identification;
- recommendation for each board;
- legacy README-linked assets;
- missing Livrables board;
- binary rename rule.

Current target stable names:

```text
before_after_01_fr.jpg
ui_hermes_pantheon_01_fr.jpg
player_journey_01_fr.jpg
port_01_fr.jpg
evidence_01_fr.jpg
citadel_01_fr.jpg
memory_compartment_01_fr.jpg
pantheon_system_summary_01_fr.jpg
worldmap_ai_internet_01_fr.jpg
livrables_01_fr.jpg
```

## README changes

The README visual reading path now uses the current identified image files:

```text
IMG_1452.jpeg → Avant / Après
IMG_1448.jpeg → Qui fait quoi ?
IMG_1446.jpeg → Parcours joueur
IMG_1451.jpeg → Port
IMG_1450.jpeg → Evidence
IMG_1457.jpeg → Citadel
IMG_1449.jpeg → Memory compartmentalization
IMG_1455.jpeg → Pantheon system summary
IMG_1454.jpeg → Worldmap AI / Internet
```

`livrables_01_fr.jpg` remains marked as image to produce.

## Boundary check

This intervention is visual documentation and README integration only.

It does not implement:

- runtime behavior;
- OpenWebUI integration;
- Hermes integration;
- Evidence Pack generation;
- memory promotion;
- provider routing;
- plugin management;
- execution tooling.

## Binary rename status

Physical binary renaming was not performed in this pass.

Reason: the available write path was reliable for text updates, while binary copy/rename should be done as a deliberate asset pass to avoid broken image links or corrupted binaries.

The README currently references the existing `IMG_*.jpeg` files as a temporary safe integration layer.

Next recommended pass:

```text
1. copy or rename binary assets to their stable target names;
2. update README image paths from IMG_*.jpeg to stable names;
3. keep or archive legacy assets intentionally;
4. add the missing Livrables board;
5. optionally create English-labelled or bilingual variants.
```

## Status

Implemented as documentation and README integration.

No runtime implementation.
