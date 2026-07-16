# AI log — Hermes dashboard operator language and demo fixture repair

Date: 2026-07-16  
Scope: public Hermes Modules preview and the installable Pantheon Modules dashboard plugin.

## Request

Review the mobile preview for comprehensibility and repair the misleading partial-live state before merging.

## Findings

- The demo SDK requested the fixture one directory above the page because the relative URL was written as if it resolved from the script file. Browser `fetch()` resolves from the document URL.
- The plugin could not distinguish the synthetic public harness from a live Hermes dashboard.
- Night-operation cards exposed internal enum values, native job identifiers and Cron expressions before explaining the operator-visible state.

## Changes

- Load `hermes-modules-demo.json` from the page directory and mark the SDK as `mode: "demo"`.
- Render `DÉMO` or `ERREUR DÉMO` independently from live status.
- Present a French operational summary, human-readable states, schedules and risks.
- Fold job names, Cron syntax, observed profile and timestamps into `Détails techniques`.
- Keep the public renderer byte-for-byte identical to the installable Hermes plugin and bump demo asset cache keys.
- Add regression coverage for the fixture URL, demo mode and operator-facing language.

## Boundary

No operation is activated by this change. The public fixture remains synthetic, all mutations remain disabled, and every example Cron job remains paused.

## Follow-up: compact card disclosure

The operation cards now keep only their decision summary visible by default. A controlled `Afficher les détails / Masquer les détails` button toggles the state grid, activation contract, technical data and current native action controls through `hidden` and `aria-expanded`. The page owns the expanded operation identifier, so opening one card closes the previous card. No action or governance boundary changed.
