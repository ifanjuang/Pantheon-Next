# Pantheon RPG Visual Corrections

Status: visual production guidance — documentation only.

This document guides future corrections of the Pantheon RPG reference boards.

It does not define implementation, runtime behavior, agents, connectors, generated Evidence Packs or memory automation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core decision

Yes, some boards should be decomposed.

Not all.

Decompose a board when it explains a workflow, a boundary or a controlled passage.

Simplify a board when it explains a concept, a role family or a mental model.

Add detail only when the detail carries governance meaning.

Remove detail when it is only decorative.

## Treatment matrix

| Board | Current role | Direction |
|---|---|---|
| Citadel | Main metaphor for governed dossiers | Decompose and enrich |
| Port | External flows and governed entry points | Decompose and enrich |
| World map | Unstable outside information world | Simplify and make functional |
| Olympus | Cognitive roles and doctrine boundary | Simplify and constrain |
| Player | Professional user and responsibility | Professionalize and simplify |
| Legend | Shared visual grammar | Add |

## Global correction rules

One board should answer one professional question.

Do not ask a single image to explain the entire system unless it is explicitly the master map.

Prioritize:

- readable flows;
- visible thresholds;
- clear temporary, candidate and validated zones;
- repeated symbols;
- small number of labels;
- stable isometric grid;
- professional dossier logic.

Avoid:

- pure fantasy decoration;
- too many characters;
- autonomous-agent impression;
- dashboard-like UI;
- photorealistic style;
- text-heavy labels inside the image;
- details that do not explain governance.

## Citadel

Intent: the core product image.

Treatment: decompose and enrich.

The citadel should show the controlled transformation of a professional dossier.

Add:

- a visible user path;
- a source gate;
- a temporary/candidate zone;
- an evidence hall;
- a validation chamber;
- sealed canonical archives;
- a clear inner perimeter for approved memory;
- a clear outer perimeter for unreviewed material.

Suggested decomposition:

- `citadel_system_01.jpg`: complete governed dossier map;
- `citadel_gate_01.jpg`: source intake and filtering;
- `citadel_evidence_01.jpg`: Evidence Pack and review trace;
- `citadel_memory_01.jpg`: Register Candidate versus Registre Probatoire entry.

Cut:

- generic monumental buildings;
- unreadable ornamental streets;
- unclear fantasy structures with no governance role.

## Port

Intent: external channels under control.

Treatment: decompose and enrich.

The port should behave like a documentary customs zone.

Add:

- incoming ships or carts for email, web, files, APIs, messengers;
- inspection gate;
- anonymization/filtering checkpoint;
- temporary warehouse;
- rejected cargo path;
- evidence cargo with seal;
- controlled route to the citadel.

Suggested decomposition:

- `port_control_01.jpg`: governed intake from external channels;
- `port_filtering_01.jpg`: filtering, anonymization, rejection;
- `port_channels_01.jpg`: Gmail, Drive, Notion, Trello, WhatsApp, web and local files as channels.

Cut:

- open decorative docks with no control point;
- implied automatic connector truth;
- any visual suggesting tools are a Registre Probatoire entry.

## World map

Intent: the outside information environment.

Treatment: simplify.

The world map should explain instability, not overload the reader.

Add functional biomes:

- weak sources forest;
- obsolete ruins;
- contradiction marsh;
- norms and rules mountain;
- open web sea;
- signal lighthouse;
- route to Pantheon.

Keep:

- a wide sense of possible knowledge;
- useful discoveries and risks together;
- clear route toward governed intake.

Cut:

- excessive fantasy quest details;
- monsters or icons that distract from the source/evidence problem;
- too many labels.

## Olympus

Intent: governed cognitive roles.

Treatment: simplify and constrain.

Olympus must never suggest autonomous runtime agents.

It should show a council of functions, not independent agents acting alone.

Group roles by function:

- structure and plan;
- verify and prove;
- evaluate risk;
- arbitrate;
- formulate;
- transmit;
- produce implementation candidates.

Add a visible disclaimer in surrounding documentation:

- roles of judgment;
- not autonomous agents;
- not runtime;
- not authority.

Cut:

- battle scenes;
- overpowered gods;
- excessive character lore;
- anything implying self-governing agents.

## Player

Intent: professional user remains responsible.

Treatment: professionalize and simplify.

The player should be a professional carrying a dossier, not only a heroic fantasy character.

Add:

- folder, plans, contract roll, tablet, notebook or sealed source pack;
- decision seal;
- path choices;
- small scale relative to the system;
- posture of responsibility, not combat.

Cut:

- oversized weapons;
- warrior fantasy dominance;
- portrait-like hero framing;
- anything that hides the dossier.

## Shared legend to add

A dedicated legend board should stabilize the whole system.

Suggested files:

- `legend_symbols_01.jpg`;
- `legend_symbols_01_fr.jpg`.

Symbols:

- Dossier: bound folder or sealed chest;
- Raw source: unsealed scroll;
- Hypothesis: dotted or translucent scroll;
- Evidence: sealed tablet;
- Validation: visible seal;
- Register Candidate: grey chest;
- Registre Probatoire entry: sealed archive inside inner citadel;
- Rejection: returned cargo or crossed mark;
- Task Contract: framed mission tablet;
- Evidence Pack: bundle of sealed sources;
- External channel: ship, cart or messenger;
- Human decision: hand seal or council mark.

## README acceptance criteria

At README width, each image must answer its local section in under three seconds.

The reader should understand:

- what enters;
- what is checked;
- what is temporary;
- what becomes evidence;
- what requires validation;
- what can become memory;
- who decides.

If an image needs a long paragraph to be understood, simplify it.
