# Prompt — Composition Study v01

Status: working visual prompt — not governance doctrine.

## Purpose

Generate a reduced composition study for the Pantheon RPG visual system before attempting the full detailed poster.

This prompt tests:

- vertical hierarchy;
- spatial readability;
- four-strata structure;
- player journey;
- source / knowledge / memory / craft separation;
- Greek antique city identity;
- doctrine-safe visual metaphor.

It intentionally excludes most micro-details, full god roster, full tool armory, full domain frieze and long labels.

## Scope

This is not the final poster.

It is a layout validation image.

The image should look like a simplified but beautiful isometric RPG world map, with enough detail to evaluate composition, but not so much detail that the structure disappears.

## Main prompt

```text
Create a very tall vertical isometric pixel art composition study for Pantheon Next represented as a governed decision RPG world.

The image must look like a playable 16-bit / 32-bit strategic RPG map, not a corporate diagram, not a SaaS dashboard, not a software architecture chart. Use a Greek antique visual language: limestone, cut stone, terracotta roofs, columns, stoas, agoras, propylons, paved streets, terraces, gardens, ports and underground forges.

The goal is to test spatial structure and readability only. Keep the image cleaner and less crowded than a final poster. Use minimal labels, mostly blank parchment cartouches for later text overlay.

The poster is a vertical cutaway with four clear strata.

Top stratum: Cieux des Possibles. Show floating islands with a few oracle temples, astrolabes, mirrors, celestial pools and constellations. This layer should feel like a place of scenarios, variants and possible paths. Add only a few small advisor figures. They must not look like rulers or controllers.

Middle outer stratum: Monde Extérieur. Around the city, show an explorable landscape with sea, source boats, forests, rivers, mountains, ruins, marshes, roads, bridges and fields. Add light fog-of-war in some zones. The landscape should clearly sit outside the city.

On one side, show source boats arriving at an antique harbor. The boats must stop at the docks and never enter the city. Use only four readable source boats for this study: small web rowboat, official state galley, merchant SaaS ship, social network corsair. The visual rule must be obvious: external sources stay outside.

Between boats and city, show Quais de Vérification: stone docks, scribes, guards, open crates, scroll inspection tables and seals. The docks are the threshold. Sources are inspected here before they can support work.

Outside the city but near the docks, show Champs de Knowledge as cultivated fields of documents, orchards of references, small rural libraries and synthesis mills. These fields must remain clearly outside the city. They may connect to the city through controlled roads, not direct uncontrolled streams.

Central stratum: Cité de la Mémoire. Make this the dominant visual focus. It must be a Greek antique civic city, not a medieval castle. No crenellations, no fantasy fortress. Use a central Pantheon palace with columns and fronton to represent system memory. Around it, create four separated project districts. Separate districts with streams, gardens, low walls, controlled bridges and porticoes. Each district should contain a small square and a few houses. The hierarchy should be legible: palace = system memory, district = project memory, square = session, house = discussion or local memory, bridge = controlled exchange.

Place the player as a small RPG hero in three key moments: at the docks bringing sources, near the council asking for help, and at a validation gate reviewing a sealed deliverable. The player must clearly be active and central.

Near the central city, show a small Conseil des Dieux as an open circular Greek agora. Include only a few companion sprites for the composition study: Athena, Themis, Argos, Hephaistos, Hermes, Mnemosyne. They are helpers, not rulers. They face the player or the task, not a control room.

Bottom stratum: Ateliers Souterrains. Show a cutaway underground world beneath the city with forges, workbenches, scribe press, map table, image chamber, tool racks, small data crystals and delivery chests. It must look like craft workshops, not backend infrastructure, not a server room. Show one simplified craft chain: source crate, orientation map, tool, forge, proof, sealed deliverable.

At the lower center, show a validation gate. A sealed deliverable moves from the workshop toward one specific project district through a controlled path. Do not show the deliverable entering the whole city or all districts. The message must be visually clear: only validated content joins the right memory area.

Use a subtle RPG HUD around the player with simple bars or icons for clarity, sources, confidence, risk and validation. Keep it discreet and game-like.

Overall composition: readable in three seconds. The viewer should immediately understand: player chooses, sources are checked, knowledge stays outside, memory is a Greek city, workshops craft deliverables, validation controls what remains.

Art direction: tall vertical isometric pixel art, 16-bit / 32-bit strategic RPG, crisp tiles, detailed but not overloaded, dark blue night atmosphere, limestone, ochre, terracotta, olive green, copper, parchment, soft cyan, subtle violet, discreet gold highlights. Beautiful composition, clear hierarchy, no dense micro-labels.
```

## Shared negative prompt

Use `prompt-negative-v01.md`.

## What this prompt deliberately removes

To protect readability, this composition study does not include:

- all gods;
- all tools;
- all domains;
- all traps;
- all side quests;
- detailed loot system;
- long explanatory text;
- full portal list;
- dense dialogue bubbles.

These elements can return after the master spatial logic is validated.

## Review checklist

Accept the generated composition only if:

- the four strata are readable;
- the city is clearly Greek antique;
- the city is the visual center;
- source boats stop outside the city;
- verification docks are visible;
- knowledge fields remain outside the city;
- project districts are separated;
- workshops look like craft, not backend;
- gods look like helpers, not controllers;
- the player remains the decision-maker;
- validation controls the final memory update;
- the result is cleaner than the full master poster prompt.

Reject the composition if:

- it looks like a medieval fortress;
- it looks like a corporate dashboard;
- it looks like a technical stack diagram;
- boats enter the city;
- knowledge fields appear inside the memory city;
- the gods dominate the player;
- the underground looks like a server room;
- the final deliverable updates all memory indiscriminately.
