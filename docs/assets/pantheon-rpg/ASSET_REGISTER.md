# Pantheon RPG Asset Register

Status: visual asset registry — documentation only.

This file records the current visual JPG/JPEG assets known in the repository and their intended README role.

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

Examples:

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

Language suffixes:

```text
_fr = French-labelled board
_en = English-labelled board
_bi = bilingual or mostly language-neutral board
```

Current repository note:

Several assets were dropped with raw camera/export filenames such as `IMG_1446.jpeg`.

They are now classified below.

Binary files should be physically renamed only during a deliberate binary asset pass.

Until that pass, README links may reference current paths to avoid broken images, while public headings use stable board names.

## Current README-ready French boards

These assets have been identified by the user and may be used in the README with their current paths.

| Current path | Target stable name | README role | Language status | User identification | Recommendation |
|---|---|---|---|---|---|
| `docs/assets/pantheon-rpg/references/IMG_1452.jpeg` | `before_after_01_fr.jpg` | 00 — Avant / Après | French | avant / après, second version, better | use as manifesto board |
| `docs/assets/pantheon-rpg/references/IMG_1448.jpeg` | `ui_hermes_pantheon_01_fr.jpg` | 01 — Qui fait quoi ? | French | qui fait quoi | use to explain OpenWebUI / Hermes / Pantheon |
| `docs/assets/pantheon-rpg/references/IMG_1446.jpeg` | `player_journey_01_fr.jpg` | 02 — Parcours joueur | French | parcours joueur entre requêtes et livrable | use as player journey board |
| `docs/assets/pantheon-rpg/references/IMG_1451.jpeg` | `port_01_fr.jpg` | 03 — Port | French | port | use as current source-intake board |
| `docs/assets/pantheon-rpg/references/IMG_1450.jpeg` | `evidence_01_fr.jpg` | 04 — Evidence / atelier des preuves | French | evidence atelier | use as current evidence board |
| `docs/assets/pantheon-rpg/references/IMG_1457.jpeg` | `citadel_01_fr.jpg` | 05 — Citadelle | French | citadelle | use as citadel board |
| `docs/assets/pantheon-rpg/references/IMG_1449.jpeg` | `memory_compartment_01_fr.jpg` | 06 — Compartimentage mémoire | French | compartimentage de la mémoire | use as memory compartment board |
| `docs/assets/pantheon-rpg/references/IMG_1455.jpeg` | `pantheon_system_summary_01_fr.jpg` | 07 — Résumé système Pantheon | French | résumé système Pantheon | use as global system summary board |
| `docs/assets/pantheon-rpg/references/IMG_1454.jpeg` | `worldmap_ai_internet_01_fr.jpg` | 08 — Worldmap IA / Internet | French | world map avec côté IA et côté Internet | use as outside-world board |

## Current legacy README-linked assets

These assets were already linked in the README before the new French board mapping.

They should remain in the repository unless deliberately archived.

| Current path | Former README status | Intended board | Language status | Recommendation |
|---|---:|---|---|---|
| `docs/assets/pantheon-rpg/references/player_01.jpg` | integrated | Player — the professional decides | to verify visually; likely French or mixed | legacy; superseded for README by `IMG_1446.jpeg` |
| `docs/assets/pantheon-rpg/references/worldmap_01.jpg` | integrated | Worldmap — outside information world | to verify visually; likely French or mixed | legacy; may be superseded by `IMG_1454.jpeg` |
| `docs/assets/pantheon-rpg/references/port_01.jpg` | integrated | Port — controlled source intake | to verify visually; likely French or mixed | legacy; superseded for README by `IMG_1451.jpeg` |
| `docs/assets/pantheon-rpg/references/citadel_01.jpg` | integrated | Citadel — governed dossier / memory city | to verify visually; likely French or mixed | legacy; superseded for README by `IMG_1457.jpeg` and `IMG_1449.jpeg` |
| `docs/assets/pantheon-rpg/references/olympus_01.jpg` | integrated | Pantheon / roles of judgment | to verify visually; likely French or mixed | legacy; may be superseded by `IMG_1455.jpeg` |
| `docs/assets/pantheon-rpg/references/player_02_fr.jpg` | not integrated | Player candidate / French-labelled iteration | French | keep as alternate player candidate |

## Missing or not yet identified target boards

These boards remain useful but are not yet mapped to a verified current file:

| Target path | Board | Purpose |
|---|---|---|
| `docs/assets/pantheon-rpg/references/livrables_01_fr.jpg` | Livrables | show candidate output production before validation |
| `docs/assets/pantheon-rpg/references/pantheon_governance_01_fr.jpg` | Pantheon governance | show configuration, validation, decision memory and audit posture if distinct from system summary |

## Former or obsolete paths observed in commit history

These paths were observed in recent commit history but are not current verified README-ready assets:

```text
docs/assets/pantheon-rpg/references/worldmap_01_fr.jpg
docs/assets/pantheon-rpg/references/port_01_fr.jpg
docs/assets/pantheon-rpg/references/IMG_1413.jpeg
docs/assets/pantheon-rpg/references/ChatGPT Image 15 mai 2026, 19_06_06.png
```

Do not reintroduce raw camera or ChatGPT-export filenames as public naming convention.

If README uses temporary raw paths, keep public section titles stable and schedule a binary rename pass.

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

This register currently verifies repository paths, user-provided board identification and README integration state.

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

Binary JPG/JPEG rename should be done as a deliberate asset pass.

Before renaming:

- verify the image visually;
- decide whether it is README-ready, candidate or obsolete;
- preserve links or update README atomically;
- avoid broken image paths;
- add an AI log.

## Current recommendation

Use the current `IMG_*.jpeg` paths in README only as a temporary safe integration layer.

Next pass:

```text
1. perform binary rename/copy to target stable names;
2. update README paths from IMG_*.jpeg to stable names;
3. archive or keep legacy images as alternates;
4. add missing livrables board;
5. optionally create English-labelled or bilingual variants.
```
