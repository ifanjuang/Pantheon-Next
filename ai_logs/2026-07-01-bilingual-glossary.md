# AI log — single bilingual glossary EN ↔ FR (B-6)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-6 (accepted, target-driven): internal governance stays EN-dominant,
professional-facing surfaces (README, landing, cockpit, architecture domain pack)
are FR, and there is **one** shared FR/EN glossary rather than a duplicated set of
177 translated docs.

## Change

- `docs/governance/GLOSSARY.md` gains a `## Bilingual terms (EN ↔ FR)` section:
  the language-direction rule (governance EN / surfaces FR) plus a ~23-row table
  mapping the core doctrine and professional-surface terms to their FR working
  form (Chokepoint / Point de contrôle, Evidence Pack / Dossier de preuves,
  Guardrail / Garde-fou, Read-only verification / Vérification en lecture seule,
  the E/V/K/C axes, etc.). Placed in the existing canonical glossary rather than a
  new file, to stay the single vocabulary owner (anti-sprawl, B-5).

## Deferred / not done here

- Formalizing the language policy in `EDITORIAL_LANGUAGE.md` (B-6.3) and the
  FR surfaces themselves (README/landing/cockpit) are separate follow-ups; the
  direction rule is stated at the head of the new glossary section in the meantime.

## Boundary

Documentation / vocabulary only. No doctrine altered — the table records existing
terms with their FR equivalents; it promotes nothing and adds no runtime, schema,
test or `mcp-server/` change. Governance runtime-phrase guard stays green.
