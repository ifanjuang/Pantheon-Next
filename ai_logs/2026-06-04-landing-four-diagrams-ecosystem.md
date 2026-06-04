# AI log — landing four-diagram set, decision outside the frame, ecosystem view

Date: 2026-06-04

## Scope

Reworked the landing diagrams in `docs/index.html` after design review, and made
the "risks" section sell the upside instead of fear.

## Changes

- **Schema 1 (`#dossierFlow`), revised, desktop + mobile reflow:**
  - The Pantheon frame now **defines the corpus** and no longer encloses the
    human **Decision** — the decision sits **outside the frame** (the human
    decides; Pantheon governs).
  - **Memory** is placed left of the **Corpus**, with a Memory→Corpus link
    ("enrichit"), a Decision→Memory arrow ("le validé devient mémoire"), and a
    Result→Corpus return ("reprise").
- **Detailed views split into three accordion diagrams** under "Architecture
  détaillée" (collapsed by default to keep the landing light):
  - `#flow2a` — **Entrées · sorties · mémoire**: corpus defined by the frame and
    fed at each step (canonical memory, external sources, knowledge base,
    templates); decision outside the frame; validated → memory at the CERBÈRE
    threshold → back to corpus. "Travail IA" renamed **"Workflow IA"**. No CHARON
    mention here.
  - `#flow2b` — **Rôles · workflows · skills**: the Governance College roles and
    functions, bounded iteration (ZEUS → MÈTIS), workflow authority modes
    (off → durable), and **skills presented as the capabilities of Hermes agents**
    (OCR, extraction, comparison, drafting, classification) governed as
    *candidates* — no "non implémenté" stamp, an honest "candidate / governed
    lifecycle" framing instead.
  - `#flow3` — **L'écosystème**: OpenWebUI (cockpit, exposes), Hermes Agent
    (runtime, executes — explained), cloud models in option (ChatGPT/Claude/
    Gemini) or local via Ollama, governed channels/tools (WhatsApp, Telegram,
    Notion, Office, Drive, Agenda), optional LangChain/LangGraph orchestration on
    the Hermes side (never a Pantheon runtime), and Pantheon + memory kept LOCAL
    on an internal server, exchanging Task Contract ↓ / Evidence Pack ↑.
- **"Risks" section reframed** from three red risk cards to three green "Atout"
  cards (positive value), with a more inviting heading.
- All three detailed SVGs render in a horizontally scrollable container so the
  dense schemas stay legible on phones.

## Doctrine fidelity

No doctrine change. Everything maps to existing governance Markdown
(`GOVERNANCE_COLLEGE`, `USER_DECISION_GATE`, `REQUEST_LIFECYCLE`,
`DATA_PLATFORM_ARCHITECTURE`, `DOCUMENT_INTELLIGENCE`, `MEMORY`,
`WORKFLOW_LIFECYCLE`, `SKILL_LIFECYCLE`, `EVIDENCE_PACK`, `OPENWEBUI_INTEGRATION`,
`HERMES_INTEGRATION`, `EXTERNAL_RUNTIME_OPTIONS`, `NANGO_HERMES_CONNECTOR_GATEWAY`,
`LOCAL_INSTALLATION_AND_CHANNELS`). The ecosystem view keeps the boundary explicit:
OpenWebUI exposes, Hermes executes, Pantheon governs; external runtimes and the
provider/model layer live on the Hermes side, never inside Pantheon.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Repo state

Documented, non-implemented. These are documentation surfaces; no runtime added.

## Risk

Low. Modified only `docs/index.html` and this AI log. All four inline D3 scripts
are guarded (`typeof d3`, `svg.empty()`) and degrade to a no-op when the CDN is
blocked. All four diagrams were rendered in a headless DOM (jsdom + d3) to confirm
they draw (44 / 69 / 80 / 74 elements) before merge.

## Follow-up

Review rendered GitHub Pages output on desktop and phone. Possible later: a true
mobile reflow for the detailed diagrams instead of horizontal scroll.
