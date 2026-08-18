# Landing rework — vertical diagrams, borrowed method, problem-first narrative

Date: 2026-08-17

Status: validation-only trace — editorial and illustration change, documented non-implemented.
Boundary profile: validation_only_trace.

Second pass on `docs/index.html` / `docs/index-en.html`, after the readability pass logged in `2026-08-17-landing-architecture-and-memories-readability.md`.

## Change

- Updated: every landing diagram redrawn on a portrait 400-unit canvas (`.diagram--vertical` / `.diagram-body.vertical`), so a phone reads them without horizontal scrolling. The former `min-width: 640px` horizontal canvases and the `:has(#agency-ai-title)` rect-override hack are gone.
- Updated: `docs/assets/diagrams/pantheon-system-map-fr.svg` and `-en.svg` redrawn vertically (viewBox `400×940`) with the same content — surfaces, direct path, assisted path, rules, authoritative server, human decision, projections.
- Added: `#bribes` / `#fragments` section — an AI does not guess, it completes from fragments; a diagram contrasts a fragmented input (reconstructed, confident, wrong in places) with an organised record (faithful, flags what is missing), plus four failure modes.
- Updated: `#pantheon` is now a positive introduction placed **after** the problem — Pantheon as a way of organising records and knowledge and passing them safely to the AI already in use, with four cards (see, cite, compartmentalise, hand over).
- Added: `#grammaire` / `#grammar` — the provenance of the vocabulary, which was previously implicit and made the mythology look anecdotal. Roles ← a college of magistracies (`GOVERNANCE_COLLEGE.md`); Rites ← recurring method moves (`rites/README.md`); Spaces ← record compartmentalisation and declared scopes (`SCOPE_ISOLATION.md`); the register ← the vocabulary of instructing a case file (`REGISTRE_PROBATOIRE_DIRECTION.md`).
- Updated: the roles named on the landing now match the canonical registry — Athena, Argos, Themis, Apollo, Hephaistos, Iris, Zeus (`AGENTS.md`) plus Mnemosyne as the continuity figure (`VISUAL_LANGUAGE.md`). The previous page named Hestia, Chronos and Ploutos, which no owner document defines. The Rite example now calls ARGOS, THEMIS and APOLLO, the roles `rites/CONCORDANCE_DES_SOURCES.md` actually lists.
- Updated: negative framings moved out of the discovery path. Section bodies state what Pantheon does; the boundary statements (not a model, not a regulation, not a guarantee of compliance) stay in the closing Responsibility and Transparency blocks.
- Added: `.lineage` and `.roles-grid` components; `.diagram--vertical` typography scale.
- Updated: the two memory cards carry the doctrine's own analogy — the architect's own recollection versus the project's file of exhibits.

## Why

Readers reported three things: the diagrams overflowed phone screens; the method was asserted without ever saying what it was derived from, which made Roles/Rites/Spaces read as decoration; and the page described Pantheon by what it is not before the reader had any reason to want it. The narrative now runs problem → why it goes wrong → what Pantheon is → how it is built.

Wording follows `EDITORIAL_LANGUAGE.md`: start from the practitioner's situation, use *cadrer*, avoid explaining the architecture first, avoid promising automatic proof.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — static HTML/CSS/SVG, no script.
Authority impact: none. The page reports the canonical role registry instead of names no owner document defines.
Schema/test/CI impact: none. `check_asset_references.py`, `check_no_local_cockpit.py`, `check_internal_links.py`, `check_index_coverage.py` re-run clean.
External action: none.
Memory behavior: none — described, not implemented.

## Local distinctions

```text
documented != implemented
borrowed vocabulary != borrowed authority
diagram != runtime topology
illustrative example != project record
```
