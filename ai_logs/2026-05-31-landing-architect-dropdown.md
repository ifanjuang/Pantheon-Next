# AI Log — Landing page: architect detail dropdown

Date: 2026-05-31

## Scope

Added a collapsible dropdown (`<details>`) under the "Pour votre métier" section
of `docs/index.html`, detailing the architect use cases from simple to most
committing.

## Changes made

Updated:

- `docs/index.html` (CSS for `.drop` / `.steps` / `.redlines`; an architect
  `<details>` block after the four-profession grid).

Added:

- `ai_logs/2026-05-31-landing-architect-dropdown.md`.

## Content

Six usage areas ranked by robustness, drawn from the user-provided
architecture deep-research document, each ending on the Pantheon decision/risk
point (the AI prepares; the professional decides and signs):

```text
Comptes rendus & synthèses               (simple)
Recherche & extraction dans les pièces   (simple)
Marchés, contrats & pièces entreprises   (intermédiaire)
Coordination du dossier CDE / BIM        (intermédiaire)
Analyse des offres & situations          (avancé)
Suivi de chantier instrumenté            (le plus engageant)
```

Plus a "lignes rouges" note: no crossing a mission boundary (no DAACT signature
without having directed the works, no attestation of an uncontrolled fact), no
emotion recognition or permanent site surveillance, and no contract / client
data / site photo transmitted without a frame (minimum necessary only).

## Discipline

- tool-agnostic: capabilities and risks only, no product names in the page body;
- editorial: avoided flagged terms ("opposable" -> "qui engage"; "vérité"
  avoided -> "affirmation"); no "safe AI" / "automatic" claims;
- faithful to doctrine: answering is not acting; source is not proof; the human
  decides.

## Verification

HTML tags balanced (`details` 1/1, `div` 47/47); no forbidden affirmative
phrase. `index.html` is not covered by the governance phrase scan.

## Explicit non-implementation

No runtime added. No files touched under `schemas/`, `tests/`, `hermes/`,
`operations/`, `pyproject.toml`, or `CLAUDE.md`.
