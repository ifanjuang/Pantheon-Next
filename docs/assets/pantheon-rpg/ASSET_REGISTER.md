# Pantheon RPG Asset Register

Status: visual asset registry — documentation only.

This file records the current visual JPG assets known in the repository and their intended README role.

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
player_01_fr.jpg
worldmap_01_fr.jpg
port_01_fr.jpg
citadel_01_fr.jpg
evidence_01_fr.jpg
livrables_01_fr.jpg
ui_hermes_pantheon_01_fr.jpg
before_after_01_fr.jpg
```

Language suffixes:

```text
_fr = French-labelled board
_en = English-labelled board
_bi = bilingual or mostly language-neutral board
```

Current repository note:

Some existing README-linked assets do not yet use the language suffix.

They should remain stable until a deliberate binary rename pass is performed.

## Current JPG assets verified by path

| Current path | README status | Intended board | Language status | Recommendation |
|---|---:|---|---|---|
| `docs/assets/pantheon-rpg/references/player_01.jpg` | integrated | Player — the professional decides | to verify visually; likely French or mixed | keep current README link until rename pass |
| `docs/assets/pantheon-rpg/references/worldmap_01.jpg` | integrated | Worldmap — outside information world | to verify visually; likely French or mixed | keep current README link until rename pass |
| `docs/assets/pantheon-rpg/references/port_01.jpg` | integrated | Port — controlled source intake | to verify visually; likely French or mixed | keep current README link until rename pass |
| `docs/assets/pantheon-rpg/references/citadel_01.jpg` | integrated | Citadel — governed dossier / memory city | to verify visually; likely French or mixed | keep current README link until rename pass |
| `docs/assets/pantheon-rpg/references/olympus_01.jpg` | integrated | Pantheon / roles of judgment | to verify visually; likely French or mixed | keep current README link until rename pass |
| `docs/assets/pantheon-rpg/references/player_02_fr.jpg` | not integrated | Player candidate / French-labelled iteration | French | keep as candidate; compare visually before replacing `player_01.jpg` |

## Missing target boards

These boards are part of the current public visual direction but are not currently verified as present:

| Target path | Board | Purpose |
|---|---|---|
| `docs/assets/pantheon-rpg/references/before_after_01_fr.jpg` | Avant / Après | show why Pantheon exists: raw AI versus governed dossier |
| `docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg` | UI / Hermes / Pantheon | explain who does what: cockpit, workshop, governance |
| `docs/assets/pantheon-rpg/references/evidence_01_fr.jpg` | Evidence | show hypotheses, contradictions, source review and proof discipline |
| `docs/assets/pantheon-rpg/references/livrables_01_fr.jpg` | Livrables | show candidate output production before validation |
| `docs/assets/pantheon-rpg/references/pantheon_governance_01_fr.jpg` | Pantheon governance | show configuration, validation, decision memory and audit posture |

## Former or obsolete paths observed in commit history

These paths were observed in recent commit history but are not current verified README assets:

```text
docs/assets/pantheon-rpg/references/worldmap_01_fr.jpg
docs/assets/pantheon-rpg/references/port_01_fr.jpg
docs/assets/pantheon-rpg/references/IMG_1413.jpeg
docs/assets/pantheon-rpg/references/ChatGPT Image 15 mai 2026, 19_06_06.png
```

Do not reintroduce raw camera or ChatGPT-export filenames in README.

Use stable board names instead.

## Recommended README sequence

Public-facing order:

```text
0. Avant / Après — De l’IA brute au dossier gouverné
1. Qui fait quoi ? — OpenWebUI / Hermes / Pantheon
2. Player — Le professionnel garde la main
3. Port — Les sources sont filtrées avant usage
4. Evidence — L’incertain devient visible
5. Livrables — Le résultat devient exploitable
6. Citadel — La mémoire est compartimentée
7. Pantheon — La stack devient méthode professionnelle
8. Worldmap — Le monde extérieur est riche mais incertain
```

Current README order may remain conservative until the missing boards exist.

## Visual audit status

This register currently verifies repository paths and README integration state.

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

Binary JPG rename should be done as a deliberate asset pass.

Before renaming:

- verify the image visually;
- decide whether it is README-ready, candidate or obsolete;
- preserve links or update README atomically;
- avoid broken image paths;
- add an AI log.

## Current recommendation

Keep the existing README image links stable for now.

Use this register to guide the next pass:

```text
1. visually compare player_01.jpg and player_02_fr.jpg;
2. decide whether player_02_fr.jpg replaces player_01.jpg;
3. produce missing before_after, ui/hermes/pantheon, evidence and livrables boards;
4. then rename final public assets with language suffixes;
5. update README once final paths exist.
```
