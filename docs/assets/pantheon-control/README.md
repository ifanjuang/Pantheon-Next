# Pantheon Control — mockup multi-pages

Statut : **documenté non implémenté**. Prototype HTML statique uniquement.

Réorganisation du mockup mono-page de la PR #115
(`docs/assets/pantheon_control_dashboard_mockup.html`) en plusieurs pages, à la
demande de revue cohérence / UX.

## Pourquoi cette version

- **Découpage en pages** au lieu d’un seul SPA `show()/hide()`, avec coquille
  partagée (barre + drawer mobile + bandeau de règles) et état de nav actif.
- **Correction doctrinale majeure** : l’Evidence Inbox d’origine mutait l’état
  directement (`Promouvoir/Questionner/…`). Ici, chaque action **prépare un
  candidat** routé vers le chokepoint / User Decision Gate — jamais d’écriture
  directe. Le dashboard ne décide rien ; le gate décide.
- **Connexions** recadrées en diagnostic lecture seule + « Préparer candidat »
  (ni installeur, ni orchestrateur).
- **Surveillance** : le dashboard **affiche** les doctor checks read-only du
  `mcp-server` ; il ne les exécute pas.
- **Taxonomie** alignée sur `docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md`
  (§ Dashboard impact) plutôt que la taxonomie ad hoc de #115.

## Pages

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil / Liveness + file de travail du jour |
| `services.html` | Services installés (runtime vs gouvernance) |
| `agents.html` | IA & Agents (Ollama + Hermes candidate-only) |
| `connections.html` | Connexions / catalogue diagnostic |
| `base-memory.html` | Base & Mémoire (canon vs projections) |
| `evidence.html` | Evidence → Mémoire (propose-only + file d’impact) |
| `surveillance.html` | Doctor checks affichés + journal d’audit |

## Fichiers partagés

- `style.css` — thème commun, chips à ton explicite, drawer responsive.
- `data.js` — données mock (aucune réelle, aucun effet runtime).
- `nav.js` — coquille, navigation, `mountPage()`.

## Hors périmètre

Aucune intégration runtime, Docker, schéma, test, endpoint backend, installation
réelle ni promotion de preuve réelle.
