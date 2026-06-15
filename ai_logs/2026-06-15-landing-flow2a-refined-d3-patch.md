# AI Log — Landing flow2a refined D3 patch

Date: 2026-06-15

## Trigger

Issue #131 — *Patch landing: replace flow2a with refined D3 entries/outputs/memory schema*.
The maintainer routed the work order to the ChatGPT/Codex track (`@codex apply this issue as a targeted patch`), but the Codex connector reported it needs a configured environment and applied nothing. The request was handed to the Claude track instead.

## Doctrine read

- `CLAUDE.md` (zones, protected paths, candidate rule)
- Issue #131 body and the `@codex` scope comment
- `docs/assets/pantheon-flow/entries-outputs-memory-d3.html` (the already-validated reference asset)

## Change

`docs/index.html`:

- Replaced only the `responsive("#flow2a", ...)` block with a refined rendering equivalent to `docs/assets/pantheon-flow/entries-outputs-memory-d3.html`, re-expressed through the landing's existing helpers (`responsive` / `mk` / `marks`): `a.box`, `a.T`, `a.Ln`, `a.P`, markers `ag` / `aa` / `agg`. The drop-shadow filter from the standalone asset was dropped to keep the landing's flat style.
- The inner dotted frame (`PÉRIMÈTRE DE TRAVAIL IA`) is narrower than the old `flow2a`, leaving visible side gutters for `refus → reprise` (left) and `remontée au corpus` (right).
- Corrected the doctrinal wording inside the diagram: `la décision humaine reste hors exécution` (not `hors cadre`); `PÉRIMÈTRE DE TRAVAIL IA` (not generic `CADRE`); `Résultat candidat qualifié`; `HUMAIN · ARBITRAGE`; `Action externe`; memory `candidate → canonique` at the Cerbère threshold.
- Updated the note under the diagram to match: `La décision humaine reste hors exécution` and `mémoire candidate puis canonique au seuil Cerbère`, avoiding any phrasing that puts Pantheon "hors cadre de décision" (Pantheon governs; the human arbitrates).

The other two diagrams (`#flow2b`, `#flow3`) and the simple `#dossierFlow` view are untouched.

## Boundary

Documentation / landing visual only.

No runtime, queue, scheduler, approval engine, memory engine, provider router, connector, external action, schema, test, dependency, platform, operation or Docker change. No protected path (`schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker, `.env`) touched.

## Repo state

Documented non implemented: the diagram visualizes the governance path; it does not execute it.

## Verification

- Modified inline script block syntax-checked with `node --check` → OK.
- Diff limited to:
  - `docs/index.html`
  - `ai_logs/2026-06-15-landing-flow2a-refined-d3-patch.md`
