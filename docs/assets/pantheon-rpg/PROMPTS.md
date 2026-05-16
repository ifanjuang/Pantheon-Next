# Pantheon RPG Visual Prompts

Status: visual production guidance — documentation only.

This document collects prompt patterns for future Pantheon RPG visual boards.

It does not define implementation, runtime behavior, agents, connectors, generated Evidence Packs or memory automation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Prompt doctrine

The prompt should not ask for generic fantasy art.

It should ask for a professional governance map expressed through antique heroic fantasy RPG isometry.

The result must feel like a readable system board, not a poster, battle scene, dashboard or lore illustration.

## Shared visual style

Use this base style for all boards.

```text
High-resolution isometric ancient fantasy RPG management-map illustration.
Orthographic isometric view, no horizon, no perspective vanishing point, no sky.
Dark elegant background, refined Mediterranean antique fantasy mood, stone, bronze, parchment, torchlight, marble, muted earth tones.
Video-game board logic, small readable characters, buildings aligned to isometric diagonals, organic but structured layout.
Professional, strategic, calm, noble, not childish, not cartoonish, not cyberpunk.
Readable at README width.
```

## Negative prompt

Use or adapt this negative block.

```text
No photorealism.
No modern SaaS dashboard.
No cyberpunk interface.
No sci-fi holograms.
No robots deciding.
No autonomous agent army.
No giant hero portrait.
No oversized weapons.
No battle scene.
No excessive fantasy decoration.
No cluttered unreadable labels.
No vertical or horizontal non-isometric walls facing the image frame.
No perspective horizon.
No text-heavy UI.
No implication that tools, agents or memory act without human validation.
```

## Shared symbol grammar

Use the same symbols across all boards.

| Concept | Visual symbol |
|---|---|
| Professional dossier | Bound folder, sealed chest or rolled plans |
| Raw Source | Unsealed scroll, open crate or loose parchment |
| Source Reference | Tagged scroll with small provenance marker |
| Hypothesis | Translucent or dotted scroll |
| Evidence Item | Sealed stone tablet or stamped parchment |
| Evidence Pack | Bundle of sealed tablets and scrolls |
| Task Contract | Framed mission tablet |
| Output Candidate | Draft parchment on review table |
| Memory Candidate | Grey chest outside inner archive |
| Canonical Memory | Sealed archive chest inside inner citadel |
| Validation | Wax seal or stamped bronze mark |
| Rejection | Returned cargo, crossed mark or closed gate |
| External channel | Ship, cart, messenger bird, courier or signal tower |
| Human decision | Hand applying seal or professional at validation table |

## Label rules

Each image should contain 5 to 7 main labels maximum.

Labels should use reader-facing vocabulary:

```text
Sources
Filtrage
Hypothèses
Preuves
Validation
Mémoire candidate
Mémoire validée
```

Avoid technical labels inside the image unless the image is explicitly for internal doctrine.

Prefer:

```text
Preuves
```

over:

```text
Evidence Pack
```

Prefer:

```text
Mémoire validée
```

over:

```text
Canonical Memory
```

The README or surrounding documentation may introduce the technical vocabulary.

## Master board prompt

Use this for a full system image.

```text
Create a high-resolution isometric ancient fantasy RPG management-map illustration for Pantheon Next.

Theme: the governed citadel of professional dossiers.

The image must show a professional user arriving with a sensitive dossier, sources entering through controlled gates, a temporary candidate zone, an evidence hall, a validation chamber and sealed canonical archives inside an inner citadel.

The composition must explain the workflow:
Dossier arrives → sources are filtered → assumptions remain visible → evidence is assembled → human validation happens → only validated information can enter memory.

The tone must be antique heroic fantasy, refined Mediterranean RPG, professional and strategic. No cyberpunk, no dashboard, no modern SaaS interface.

Use small RPG-scale characters, isometric roads, diagonal buildings, controlled gates, archives, review tables, seals, parchment, stone tablets and bronze markers.

Make the board readable at README size.

Include only these labels:
Sources, Filtrage, Hypothèses, Preuves, Validation, Mémoire candidate, Mémoire validée.
```

## Citadel prompts

### `citadel_system_01`

```text
Create an isometric ancient fantasy RPG board showing Pantheon as a governed citadel around a professional dossier.

Show a clear path from a professional user carrying a dossier to a controlled source gate, temporary candidate area, evidence hall, validation chamber and sealed inner archives.

The citadel must feel organized but alive: courtyards, terraces, archives, gates, review tables, parchment bundles, bronze seals, small officials and small professional characters.

The key idea: nothing becomes truth or memory without review and validation.

Keep labels minimal and readable.
```

### `citadel_gate_01`

```text
Create an isometric close-up of the citadel gate where sources enter Pantheon.

Show incoming scrolls, PDFs as parchment bundles, emails as messenger birds, web sources as carts, and files as sealed crates.

Show a controlled gate with inspectors, provenance tags, temporary holding area and rejected-source path.

The gate must communicate filtering, scope control and source review.
```

### `citadel_evidence_01`

```text
Create an isometric evidence hall inside the Pantheon citadel.

Show selected sources laid on review tables, linked to sealed evidence tablets, visible assumptions, contradictions preserved on side tables, and a final Evidence Pack as a sealed bundle.

The image must show that evidence supports review but does not approve itself.
```

### `citadel_memory_01`

```text
Create an isometric cutaway of Pantheon memory areas.

Show temporary working context as loose parchments, Memory Candidates as grey chests outside the inner archive, and Canonical Memory as sealed chests inside a protected archive.

Add a validation seal gate between Memory Candidate and Canonical Memory.

The image must show that memory does not promote itself.
```

## Port prompts

### `port_control_01`

```text
Create an isometric ancient port connected to the Pantheon citadel.

The port represents governed external entry points: email, web, Drive, Notion, Trello, WhatsApp, Telegram, local files and APIs.

Show ships, carts, messenger birds and signal towers bringing sources to customs docks.

Show inspection gates, filtering booths, anonymization checkpoint, temporary warehouse, rejected cargo path and controlled route to the citadel.

The key idea: tools are channels, not truth.
```

### `port_filtering_01`

```text
Create an isometric close-up of a documentary customs checkpoint in an ancient fantasy port.

Incoming documents and messages are sorted into: allowed source reference, temporary material, evidence candidate and rejected material.

Use stamps, tags, sealed crates, grey holding areas and a clear route toward the governed citadel.

The image must show filtering and rejection as normal professional actions.
```

### `port_channels_01`

```text
Create an isometric port map showing multiple external channels as distinct docks.

Each dock should represent one channel without modern UI screenshots: Gmail as messenger birds, Drive as archive crates, Notion/Trello as task boards on carts, WhatsApp/Telegram as courier scrolls, web search as lighthouse and ships, local files as sealed boxes.

All docks must lead to a common controlled intake gate.

Do not show these channels as canonical memory.
```

## World map prompt

### `worldmap_02`

```text
Create an isometric antique fantasy RPG world map representing the unstable outside information world around Pantheon.

Show functional biomes: weak sources forest, obsolete ruins, contradiction marsh, norms mountain, open web sea, signal lighthouse and route toward the governed citadel.

The world must feel useful and dangerous, not evil. It contains discoveries, sources, noise, old information and contradictions.

The goal is to show why professionals need a method to cross this world without confusing signal, source, evidence and memory.

Keep the map less crowded than a fantasy adventure poster.
```

## Olympus prompt

### `olympus_roles_01`

```text
Create an isometric ancient council scene representing governed cognitive roles in Pantheon.

The scene must show roles of judgment, not autonomous agents.

Group figures by function: structure and plan, verify and prove, evaluate risk, arbitrate, formulate, transmit, produce implementation candidates.

Use small readable figures, calm council posture, tablets, scrolls and seals.

Do not show battle, magic domination, independent agents, or gods acting without human validation.

Include a clear visual note: roles of judgment, not autonomous agents.
```

## Player prompt

### `player_professional_01`

```text
Create an isometric ancient heroic fantasy RPG scene showing the professional user as the player of Pantheon Next.

The user stands before the governed citadel with a real dossier: plans, contracts, notes, sources, constraints and a decision to prepare.

The character is small, professional and calm, not a warrior hero. They carry a satchel, rolled plans, sealed documents and a validation seal.

Show several isometric paths ahead: source review, evidence, validation, memory.

The key idea: Pantheon structures the path, AI accelerates selected tasks, responsibility remains human.
```

## Legend prompt

### `legend_symbols_01`

```text
Create a clean isometric legend board for Pantheon Next visual language.

Dark elegant background. Antique fantasy RPG icons arranged in a clear grid.

Show and label the core symbols:
Dossier, Raw Source, Hypothesis, Evidence, Evidence Pack, Task Contract, Output Candidate, Memory Candidate, Canonical Memory, Validation, Rejection, External Channel, Human Decision.

Each symbol must be visually distinct and reusable across future boards.

Keep the board simple, precise and readable.
```

## Output checklist

Before accepting an image, verify:

- it is isometric without horizon or perspective effect;
- the professional dossier is visible;
- the flow is understandable without reading long text;
- the image does not imply autonomous runtime;
- tools are channels, not truth;
- memory is not automatic;
- the human decision remains visible;
- labels are short and readable;
- the color palette remains coherent with the existing Pantheon RPG boards;
- it works at README preview size.
