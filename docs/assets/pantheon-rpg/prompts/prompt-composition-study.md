# Prompt — Composition Study

Status: working visual prompt — not governance doctrine.

Document revision: 1.

## Purpose

Validate the global vertical composition before generating the dense Pantheon RPG poster.

This study must test:

- the four-strata vertical cutaway;
- the source boundary;
- the memory city hierarchy;
- the underground workshop layer;
- the final human validation gate;
- readability at poster scale and mobile crop scale.

## Scope

This prompt is intentionally reduced.

It does not attempt to render all gods, all tools, all quests or all domain villages.

It focuses on spatial hierarchy and doctrine-safe metaphor.

## Main prompt

```text
Create a very tall vertical isometric pixel art composition study for Pantheon Next, designed like a playable strategic RPG world map.

The image must be divided into four clearly readable horizontal strata stacked vertically:

1. the Cieux des Possibles at the top,
2. the Monde Extérieur and source routes around the upper middle,
3. the Cité de la Mémoire at the center,
4. the Ateliers Souterrains below the city.

At the very top, create a simple Greek stone title platform with a large empty title area and a small player character looking toward the world below.

In the Cieux des Possibles, show only three floating oracle islands connected by light bridges. Use one observatory, one mirror temple and one celestial pool. Show a few companion god silhouettes as advisors, never rulers.

In the Monde Extérieur, create a wide explorable landscape with sea, cliffs, forest, river, mountain, ruins and a rural knowledge field. Keep some zones under fog-of-war.

On the sea, show five source boats that stop outside the city: a small web-page rowboat, a social-network corsair ship, an open-data fishing boat, a SaaS merchant ship and an official institutional galley. The ships must remain outside the city.

Between the boats and the city, create the Quais de Vérification with stone docks, scribes, inspected crates, scrolls, seals and guarded gates. Make the boundary visually obvious: external sources are checked before entering governed work.

Beside the docks but outside the city, create the Champs de Knowledge as patchwork fields of documents, orchards of references, a small norm village, a public-data village and a synthesis mill. Knowledge remains outside the memory city.

At the center, create the Cité de la Mémoire as a large Greek antique civic city with limestone buildings, columns, terracotta roofs, porticoes, gardens, stairs, streams and bridges. No medieval castle.

Inside the city, place a central Pantheon palace and four separated project districts. Each project district must have its own gate, square, houses and archive. Districts communicate only through controlled bridges. The city hierarchy must be visible: city equals governed memory, palace equals system memory, district equals project memory, square equals work session, house equals local discussion, bridge equals controlled exchange.

Show the player entering one project district, reviewing a sealed document and walking toward a decision gate.

Around the city, place only three simple RPG traps: a fog marsh for missing context, a treasure-chest mimic for false proof and an old-version ghost in ruins.

Below the city, create the Ateliers Souterrains as craft workshops carved into rock. Show a forge, cartography room, document workshop, tool armory and sealed deliverable workshop. The underground must look artisanal and antique, never like a server room or software backend.

At the bottom, show the final human validation gate. The player chooses between validate, correct, reject and save. A sealed deliverable may move only toward the correct project district after validation.

Use a controlled Greek-antique palette: limestone, terracotta, olive green, deep blue, ochre, copper, parchment, soft cyan and muted violet. Crisp isometric pixel art, readable silhouettes, strong vertical hierarchy, minimal text, empty parchment spaces for later labels.

The image must communicate a simple doctrine: sources stay outside, knowledge supports work, memory is scoped, tools craft candidates, the player decides, only validated content becomes durable memory.
```

## Shared negative prompt

Use `prompt-negative.md`.

## Composition requirements

The first candidate should be judged on:

```text
vertical hierarchy
source boundary readability
city hierarchy readability
project separation
human decision visibility
underground craft metaphor
absence of backend imagery
```

## Mobile crop requirement

The composition must remain understandable when viewed as three sequential mobile crops:

```text
top crop: possibilities + source world
a center crop: verification docks + memory city
a bottom crop: underground workshops + validation gate
```

## Known risks

### Too much visual detail

If the image becomes decorative rather than readable, remove secondary islands, villages and workshop tools.

### Medieval drift

Reject any castle, fortress, knight or feudal imagery.

### Runtime drift

Reject any server room, control center, autonomous robot or hidden machine deciding for the player.

### Memory drift

Reject any direct stream from source boats or knowledge fields into the central palace.

## Review checklist

- are the four strata obvious?
- do source boats stop outside the city?
- are the verification docks visible?
- are knowledge fields outside the city?
- is the city Greek antique?
- are project districts separated?
- is the player active?
- are underground workshops artisanal?
- is validation human?
- does the deliverable return only to the correct project district?
