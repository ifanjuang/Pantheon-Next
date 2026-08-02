# Pantheon RPG Visual Roadmap

Status: visual production guidance — documentation only.

This roadmap organizes future Pantheon RPG boards into a clearer production sequence.

It does not define implementation, runtime behavior, agents, connectors, generated Evidence Packs or memory automation.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Strategic answer

Some boards should be decomposed.

Some should be simplified.

Some need more detail.

The rule is simple:

```text
Decompose flows.
Simplify concepts.
Enrich only governance-bearing details.
```

A board that explains a passage, intake, review, validation or memory transition should be decomposed.

A board that explains a mental model, a role family or the outside world should remain simple and iconic.

## Production priorities

| Priority | Board | Action | Why |
|---|---|---|---|
| P0 | Legend | Add | Stabilizes the whole visual grammar. |
| P1 | Citadel | Decompose | It is the main product metaphor. |
| P1 | Port | Decompose | It explains everyday tools and external sources. |
| P2 | Player | Refine | It anchors human authority and professional responsibility. |
| P2 | World map | Simplify | It explains instability, not every possible risk. |
| P3 | Olympus | Simplify | It must not suggest autonomous agents. |
| P3 | README previews | Review | Ensure every image answers its local section. |

## Phase 0 — Freeze existing references

Goal: preserve the current visual family.

Actions:

- keep current `references/` images as historical reference exports;
- avoid overwriting existing boards unless intentionally replacing them;
- use new filenames for new explorations;
- keep French and English variants when the board contains labels;
- document every accepted visual improvement in this folder.

Suggested status:

```text
Current images = reference baseline.
New images = iterative candidates.
Accepted images = README-ready exports.
```

## Phase 1 — Add the shared legend

Goal: make the whole visual system readable.

Create:

- `legend_symbols_01.jpg`;
- `legend_symbols_01_fr.jpg`.

The legend should define reusable symbols for:

- dossier;
- raw source;
- hypothesis;
- evidence;
- Evidence Pack;
- Task Contract;
- Output Candidate;
- Register Candidate;
- Registre Probatoire entry;
- validation;
- rejection;
- external channel;
- human decision.

Acceptance criteria:

- readable at README width;
- simple grid layout;
- no runtime implication;
- reusable symbols across every later board.

## Phase 2 — Rebuild the citadel as a system board

Goal: make the main product image immediately understandable.

Create:

- `citadel_system_01.jpg`;
- `citadel_system_01_fr.jpg`.

The image should show the complete governed dossier path:

```text
Professional dossier
→ Source gate
→ Temporary / candidate zone
→ Evidence hall
→ Validation chamber
→ Canonical archive
```

Key corrections:

- visible route from user to validation;
- clear controlled gates;
- inner archive for validated memory;
- outer candidate zone for unvalidated material;
- evidence area visibly distinct from memory;
- small professional player visible, not dominant.

Acceptance criteria:

- a reader understands the workflow without reading a long caption;
- memory promotion is visibly gated;
- evidence does not look like automatic truth;
- the city feels organized but not bureaucratic.

## Phase 3 — Decompose the citadel

Goal: explain the core governance mechanisms without overcrowding one board.

Create:

- `citadel_gate_01.jpg` / `citadel_gate_01_fr.jpg`;
- `citadel_evidence_01.jpg` / `citadel_evidence_01_fr.jpg`;
- `citadel_memory_01.jpg` / `citadel_memory_01_fr.jpg`.

### Citadel gate

Explains:

- source intake;
- provenance tagging;
- scope filtering;
- temporary holding;
- rejection.

### Evidence hall

Explains:

- selected sources;
- visible assumptions;
- preserved contradictions;
- Evidence Pack assembly;
- review readiness.

### Memory archive

Explains:

- Working Context is temporary;
- Register Candidate is not a Registre Probatoire entry;
- Registre Probatoire entry is sealed, scoped and validated;
- memory does not promote itself.

## Phase 4 — Decompose the port

Goal: make external tools pragmatically understandable.

Create:

- `port_control_01.jpg` / `port_control_01_fr.jpg`;
- `port_filtering_01.jpg` / `port_filtering_01_fr.jpg`;
- `port_channels_01.jpg` / `port_channels_01_fr.jpg`.

The port should answer the professional question:

```text
My information is already in Gmail, Drive, Notion, Trello, WhatsApp, Telegram, PDFs and the web.
How does Pantheon keep control?
```

Key corrections:

- external tools must appear as channels;
- channels must not look like truth sources;
- every incoming flow should pass through a controlled gate;
- rejected or temporary material must be visible;
- evidence-bound material should be sealed or tagged.

Acceptance criteria:

- the board makes practical sense for non-technical professionals;
- it does not imply built-in runtime connectors unless documented elsewhere;
- it shows governed intake, not automatic ingestion.

## Phase 5 — Simplify the world map

Goal: explain why the outside information world needs method.

Create:

- `worldmap_02.jpg`;
- `worldmap_02_fr.jpg`.

The world map should not become a fantasy encyclopedia.

It should show a limited number of functional regions:

- weak sources forest;
- obsolete ruins;
- contradiction marsh;
- norms mountain;
- open web sea;
- signal lighthouse;
- route to Pantheon.

Acceptance criteria:

- fewer but stronger labels;
- clear route toward governed intake;
- useful and risky information coexist;
- no overload of monsters, icons or lore.

## Phase 6 — Simplify Olympus

Goal: clarify cognitive roles without suggesting autonomous agents.

Create:

- `olympus_roles_01.jpg`;
- `olympus_roles_01_fr.jpg`.

Olympus should be a council map, not an agent swarm.

Role families:

- structure and plan;
- verify and prove;
- evaluate risk;
- arbitrate;
- formulate;
- transmit;
- produce implementation candidates.

Acceptance criteria:

- roles are clearly grouped;
- no battle or magic domination;
- no figure appears to self-authorize or decide alone;
- a visible note states that these are cognitive roles, not autonomous runtime agents.

## Phase 7 — Refine the player board

Goal: make the user recognizable as a professional.

Create:

- `player_professional_01.jpg`;
- `player_professional_01_fr.jpg`.

Corrections:

- character remains small at RPG scale;
- character carries a dossier, plans, sources or contracts;
- posture is calm, responsible and professional;
- the image shows paths toward sources, evidence, validation and memory;
- avoid warrior-centered fantasy framing.

Acceptance criteria:

- user understands they remain responsible;
- AI appears as assistance, not replacement;
- Pantheon appears as method, not game world.

## Phase 8 — README integration pass

Goal: keep the README visual and readable.

Actions:

- use the citadel system board near the top;
- place the world map near the AI/source-risk explanation;
- place the player near the human responsibility section;
- place Olympus near operating doctrine;
- place the port near everyday tools;
- add the legend only if it clarifies, not if it overloads.

Acceptance criteria:

- each image explains the section where it appears;
- no late image gallery unless used as an archive;
- every visual block is understandable in three seconds;
- captions do not compensate for unclear images.

## Phase 9 — Bilingual export policy

Goal: keep French and English usable without duplicating visual effort unnecessarily.

Rules:

- create unlabeled or low-label images when possible;
- create `_fr` variants only when labels appear inside the image;
- keep filenames stable;
- do not mix French and English labels inside the same export;
- README English should reference English exports;
- README French should reference `_fr` exports.

Recommended naming:

```text
<board>_<variant>_<index>.jpg
<board>_<variant>_<index>_fr.jpg
```

Examples:

```text
citadel_system_01.jpg
citadel_system_01_fr.jpg
port_control_01.jpg
port_control_01_fr.jpg
```

## Final acceptance checklist

Before a board becomes README-ready, verify:

- it supports the Pantheon doctrine;
- it does not imply Pantheon is a runtime;
- it does not imply OpenWebUI canonizes memory;
- it does not imply Hermes approves or bypasses validation;
- it keeps tools as governed channels;
- it keeps memory promotion gated;
- it shows human decision where needed;
- it remains readable at README preview size;
- it matches the existing antique fantasy RPG visual family;
- it has a clear reason to exist.

## Current recommended sequence

```text
1. legend_symbols_01
2. citadel_system_01
3. port_control_01
4. player_professional_01
5. worldmap_02
6. olympus_roles_01
7. citadel_gate_01
8. citadel_evidence_01
9. citadel_memory_01
10. port_filtering_01
11. port_channels_01
```

This sequence stabilizes the grammar first, then the main product promise, then the practical external-tool story.
