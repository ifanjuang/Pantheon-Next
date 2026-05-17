# Pantheon RPG Asset Register

Status: visual asset registry — documentation only.

This file records Pantheon RPG visual assets used or considered for README and documentation.

It is not governance doctrine.

It is not implementation.

It does not claim that a visual board implements a capability.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Registry rule

Visual assets are communication supports.

They must not imply:

- autonomous runtime;
- hidden workflow execution;
- automatic memory promotion;
- OpenWebUI as source of truth;
- Hermes as approval authority;
- Pantheon as execution engine.

## Naming convention

Preferred pattern:

```text
<board_slug>_<version>_<lang>.<ext>
```

Language suffixes:

```text
_fr = French-labelled board
_en = English-labelled board
_bi = bilingual or mostly language-neutral board
```

## Current README-ready French boards

These assets are the current stable public board files.

| Current stable path | README role | Language status | User identification | Recommendation |
|---|---|---|---|---|
| `docs/assets/pantheon-rpg/references/before_after_01_fr.jpg` | 00 — Avant / Après | French | avant / après, second version, better | use as manifesto board |
| `docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg` | 01 — Qui fait quoi ? | French | qui fait quoi | use to explain OpenWebUI / Hermes / Pantheon |
| `docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg` | 02 — Parcours joueur | French | parcours joueur entre requêtes et livrable | use as player journey board |
| `docs/assets/pantheon-rpg/references/port_01_fr.jpg` | 03 — Port | French | port | use as current source-intake board |
| `docs/assets/pantheon-rpg/references/evidence_01_fr.jpg` | 04 — Evidence / atelier des preuves | French | evidence atelier | use as current evidence board |
| `docs/assets/pantheon-rpg/references/citadel_01_fr.jpg` | 05 — Citadelle | French | citadelle | use as citadel board |
| `docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg` | 06 — Compartimentage mémoire | French | compartimentage de la mémoire | use as memory compartment board |
| `docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg` | 07 — Résumé système Pantheon | French | résumé système Pantheon | use as global system summary board |
| `docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg` | 08 — Worldmap IA / Internet | French | world map avec côté IA et côté Internet | use as outside-world board |

## Rename history

These raw files were mapped to stable names:

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

Do not reintroduce raw camera or ChatGPT-export filenames as public README paths.

## Current legacy assets

These assets existed before the new French board mapping.

They should remain in the repository unless deliberately archived.

| Current path | Former README status | Intended board | Language status | Recommendation |
|---|---:|---|---|---|
| `docs/assets/pantheon-rpg/references/player_01.jpg` | previously integrated | Player — the professional decides | to verify visually; likely French or mixed | legacy; superseded for README by `player_journey_01_fr.jpg` |
| `docs/assets/pantheon-rpg/references/worldmap_01.jpg` | previously integrated | Worldmap — outside information world | to verify visually; likely French or mixed | legacy; superseded by `worldmap_ai_internet_01_fr.jpg` |
| `docs/assets/pantheon-rpg/references/port_01.jpg` | previously integrated | Port — controlled source intake | to verify visually; likely French or mixed | legacy; superseded by `port_01_fr.jpg` |
| `docs/assets/pantheon-rpg/references/citadel_01.jpg` | previously integrated | Citadel — governed dossier / memory city | to verify visually; likely French or mixed | legacy; superseded by `citadel_01_fr.jpg` and `memory_compartment_01_fr.jpg` |
| `docs/assets/pantheon-rpg/references/olympus_01.jpg` | previously integrated | Pantheon / roles of judgment | to verify visually; likely French or mixed | legacy; may be superseded by `pantheon_system_summary_01_fr.jpg` |
| `docs/assets/pantheon-rpg/references/player_02_fr.jpg` | not integrated | Player candidate / French-labelled iteration | French | keep as alternate player candidate |

## Missing or not yet identified target boards

| Target path | Board | Purpose |
|---|---|---|
| `docs/assets/pantheon-rpg/references/livrables_01_fr.jpg` | Livrables | show candidate output production before validation |
| `docs/assets/pantheon-rpg/references/pantheon_governance_01_fr.jpg` | Pantheon governance | show configuration, validation, decision memory and audit posture if distinct from system summary |

## Former or obsolete paths observed in commit history

These paths were observed in recent commit history but are not current README-ready assets:

```text
docs/assets/pantheon-rpg/references/worldmap_01_fr.jpg
docs/assets/pantheon-rpg/references/port_01_fr.jpg
docs/assets/pantheon-rpg/references/IMG_1413.jpeg
docs/assets/pantheon-rpg/references/ChatGPT Image 15 mai 2026, 19_06_06.png
```

## Recommended README sequence

Public-facing order:

```text
0. Avant / Après — De l’IA brute au dossier gouverné
1. Qui fait quoi ? — OpenWebUI / Hermes / Pantheon
2. Parcours joueur — de la requête au livrable
3. Port — les sources sont filtrées avant usage
4. Evidence — l’incertain devient visible
5. Citadelle — la ville du dossier gouverné
6. Mémoire — la mémoire est compartimentée
7. Pantheon — résumé système et gouvernance
8. Worldmap — monde IA et monde Internet
9. Livrables — candidate outputs before transmission, to produce
```

## Visual audit status

This register verifies repository paths, user-provided board identification and README integration state.

It does not claim full visual quality review of every image.

A full visual audit should still check:

- strict isometry;
- readability at README width;
- label language;
- presence of the professional user;
- gods as assistants, not decision-makers;
- no runtime implication;
- no memory auto-promotion implication;
- no confusion between source, evidence and memory.

## Binary rename rule

Binary JPG/JPEG rename should be done through Git-safe binary operations such as `git mv` or Git tree blob reuse.

Do not rewrite binary images through text-only APIs.

## Current recommendation

Next pass:

```text
1. add missing livrables board;
2. optionally create English-labelled or bilingual variants;
3. optionally archive superseded legacy images after visual review.
```
