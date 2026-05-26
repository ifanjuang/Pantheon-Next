# README Simplification — Less AI, More Professional, More Communication

Date: 2026-05-18

## Scope

Editorial restructuring of both public READMEs for clarity, professional positioning and reader adherence.

Files changed:

- `README.md`;
- `README.fr.md`.

No doctrine document, schema, profile or governance file was modified.

## Goal

The owner asked to simplify the explanation, improve adherence for non-technical professional readers, and shift the tone to be less AI-centric, more professional and more communication-oriented.

## Changes

- Length reduced from 522 to 251 lines per file (about 52% shorter).
- Visible sections reduced from 18 to 7: *Who this is for*, *What you get*, *How a dossier flows*, *Six honest distinctions*, *Cloud or local*, *See it on real dossiers*, *One formula*.
- The six overlapping "X ≠ Y" sections (risk, source-not-proof, draft-not-deliverable, memory, what-is-not, role-agreement) were merged into a single "Six honest distinctions" block.
- The internal doctrine (`OpenWebUI exposes / Hermes executes / Pantheon governs`), the seven Pantheon Roles, the vocabulary table, the compartmentalized-memory block and "What Pantheon is not" were moved into a collapsible "Under the hood" section, so the top of the page leads with professional value, not internal architecture. This aligns the README with `EDITORIAL_LANGUAGE` guidance to start from professional risk and consequence before technical architecture.
- Tone shifted: the hero now positions Pantheon Next as "a control method for professional dossiers" rather than "help to use AI safely". Explicit mentions of "AI" dropped from roughly twenty to three; the engine is framed as a tool, the professional as the accountable party.
- Added two adherence levers absent before: a "Who this is for" line and a benefit-led "What you get" block (nothing leaves by accident, audit-ready trail, trustworthy memory).
- The collapsible table of contents was removed; with seven sections it is no longer needed.

## Images

Only `before_after_01_fr.jpg` is kept in the visible flow. The README no longer references `port_01_fr.jpg`, `livrables_01_fr.jpg`, `memory_compartment_01_fr.jpg` or `pantheon_system_summary_01_fr.jpg`, because the sections they anchored were merged or collapsed. The image files remain in `docs/assets/` and can be re-added if desired.

## Doctrine boundary

- No runtime, integration, schema, test, operations or platform change.
- The internal doctrine wording is preserved verbatim inside "Under the hood".
- The seven canonical Pantheon Roles and HEPHAISTOS spelling are unchanged.
- No claim of implementation beyond the status banner and the "Project status and structure" section, both preserved.

## Symmetry

`README.md` and `README.fr.md` are structurally identical: 251 lines each, 7 visible sections each, same section order, same links and the same single image.

## Verification

- All relative links resolve.
- The one image reference resolves.
- EN and FR section counts match.

## Risks and limitations

- This is an editorial change; wording is a matter of taste and the owner may want further tuning of the hero copy.
- Four narrative images are no longer surfaced in the README; if their visibility matters for the public page, a short gallery could be reintroduced under a collapsible block.
- `CHANGELOG.md` was not updated; a release note can be added in a separate reconciliation pass.
