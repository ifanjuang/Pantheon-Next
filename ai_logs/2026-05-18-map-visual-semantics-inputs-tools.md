# AI Log — Map visual semantics for inputs and tools

Date: 2026-05-18

## Scope

Updated the interactive Pantheon map visual semantics after review of mobile readability and category hierarchy.

## Files changed

- `docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html`
- `ai_logs/2026-05-18-map-visual-semantics-inputs-tools.md`

## Summary

Applied a clearer visual code:

- user-facing inputs and concrete incoming material now use opaque white backgrounds:
  - User;
  - Request;
  - Project dossier;
  - Documents;
  - WhatsApp;
  - Telegram;
  - Human decision.
- OpenWebUI and Hermes remain black with white text.
- Pantheon and Memory Gateway use a distinct ivory/white governance style.
- external tools and connectors use colored backgrounds:
  - MCP;
  - Google Workspace / G Suite;
  - Notion;
  - Trello.
- intermediate objects remain transparent-style:
  - Knowledge;
  - Entry;
  - Context Pack;
  - Evidence Pack;
  - Skills;
  - Web / watch;
  - Memory Candidate.
- validated memory remains green.
- forbidden paths remain red.

Added WhatsApp and Telegram as user communication inputs.

Replaced the generic `Google / Notion / Trello` node with distinct nodes so each external tool can be read and styled separately.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

MCP remains primarily attached to Hermes as an execution-side connector layer.

Pantheon governs permissions, scope, evidence, approvals and memory.

No runtime, provider routing, scheduler, queue, hidden workflow engine, automatic approval, automatic memory promotion or skill installation was added.
