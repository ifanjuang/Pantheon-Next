# AI Log — Réorganisation multi-pages du mockup Pantheon Control

Date: 2026-06-13

## Demande

Revue cohérence / UX du mockup Dashboard envoyé en PR #115
(`docs/assets/pantheon_control_dashboard_mockup.html`) et décision : tout
changer, réorganiser, ou laisser rodé. Choix retenu après revue : **réorganiser
et décomposer en plusieurs pages**.

## Diagnostic du mockup #115

À garder : bandeau de règles (`Installed ≠ Authorized`, …) et double statut
runtime/gouvernance par stack.

Problèmes de cohérence (doctrine) :

- **Violation** : l’Evidence Inbox mutait l’état sur place
  (`Promouvoir/Questionner/Déclasser/Archiver`). CLAUDE.md exige un candidat
  d’édition via le chokepoint et le User Decision Gate, jamais d’écriture
  directe.
- **Catalogue** avec états `Installable` + bouton `Gate` : frôle l’installeur /
  orchestrateur, interdits par la frontière.
- **Tests** avec `Run all` : laisse croire que le dashboard exécute, alors que
  les doctor checks read-only vivent dans `mcp-server/`.
- **Taxonomie** divergente de `EVIDENCE_MEMORY_DEV_PLAN.md` (§ Dashboard impact).

Problèmes UX : SPA monolithique sans état de nav actif, régression du drawer
mobile (présent en v15), panneau « Détail / activité » ambigu, sémantique
couleur devinée par sous-chaîne, mélange FR/EN.

## Action

Nouveau prototype statique multi-pages sous `docs/assets/pantheon-control/` :

- coquille partagée (`nav.js`, `style.css`) : barre, drawer responsive, bandeau
  de règles, état de nav actif ;
- 7 pages alignées sur la taxonomie documentée : Accueil/Liveness, Services
  installés, IA & Agents, Connexions, Base & Mémoire, Evidence → Mémoire,
  Surveillance ;
- Evidence → Mémoire **propose-only** : les actions préparent un candidat routé
  vers le gate, le statut affiché ne change pas ;
- Connexions en diagnostic lecture seule + « Préparer candidat » ;
- Surveillance **affiche** les doctor checks du `mcp-server` (n’exécute pas) +
  journal d’audit append-only ;
- réconcilie les deux directions (infra de #115 + Evidence→Mémoire de la v15)
  comme facettes d’un même cockpit.

## Boundary

Documenté non implémenté. HTML/CSS/JS statique uniquement, données mock. Aucun
runtime, accès base, promotion mémoire, sync backend, intégration OpenWebUI,
exécution Hermes, gate d’approbation ni migration de schéma.

## Related

- PR #115 — mockup mono-page d’origine
- `ai_logs/2026-06-06-dashboard-v15-evidence-memory.md`
- `docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md`
- issue #68

## Repo state

Partiel / documenté non implémenté.
