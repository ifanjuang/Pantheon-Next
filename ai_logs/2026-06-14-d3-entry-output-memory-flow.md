# AI log — D3 entry/output/memory flow visual

Date: 2026-06-14

## Request

Improve the HTML diagram for entries, outputs and memory. The inner frame should be narrower so lateral arrows remain visible. Produce an improved D3.js version in the repository.

## Doctrine read

Read before modification:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MODULES.md`
- `docs/governance/VISUAL_LANGUAGE.md`
- `docs/assets/README.md`

Relevant boundaries kept:

- Pantheon governs; it does not execute.
- Visual assets are documentation support only.
- A workflow result remains a candidate until human arbitration.
- Memory wording must not imply that runtime memory is a source of truth.

## Repository discussion checked

Checked recent repository activity and relevant dashboard/asset work:

- PR #119, merged: usage-focused Pantheon Control redesign.
- PR #117, merged: multi-page Pantheon Control mockup.
- PR #127, open: PaddleOCR dashboard install candidate, with an index coverage review comment.
- PR #116, open: CI for MCP-server module tests.

No active discussion was found that directly conflicts with adding a visual support asset under `docs/assets/`.

## Changes

Created:

- `docs/assets/pantheon-flow/entrees-sorties-memoire-d3.html`

Updated:

- `docs/assets/README.md`
- `ai_logs/2026-06-14-d3-entry-output-memory-flow.md`

Correction after diff review:

- Restored the tail of `docs/assets/README.md` after detecting that the first index update had unintentionally shortened the workflow visual rule and removed the anti-runtime reminder.

## Design decisions

Accepted:

- Narrower inner dotted frame to create clear left/right gutters for loop arrows.
- D3-generated SVG, responsive desktop/mobile layout.
- Doctrine-consistent wording: `Résultat candidat qualifié`, `HUMAIN · ARBITRAGE`, `Action externe`, `Mémoire gouvernée`.
- Side loops separated visually: `refus → reprise` and `canonique → corpus futur`.

Refused:

- Treating the diagram as implementation evidence.
- Showing memory as an unqualified source-of-truth layer.
- Implying that the workflow validates, sends or memorizes by itself.

To verify:

- Visual rendering on the live Pages site after rebuild.
- Whether the embedded `docs/index.html` diagram should later be replaced directly by this standalone D3 asset.

## Repository state

Documented non-implemented.

This is a static visual support asset. It does not add runtime behavior, approval, memory promotion, external action, connector, backend, schema or test.
