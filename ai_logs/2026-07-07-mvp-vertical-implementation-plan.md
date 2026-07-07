# 2026-07-07 — Plan d'implémentation du vertical MVP

## Intervention

Sur demande du mainteneur (« Prépare le plan ») : plan d'implémentation séquencé du vertical `mvp-governed-task-loop`, adossé à la spec `docs/governance/MVP_GOVERNED_TASK_LOOP.md` (PR #297). Document : `docs/governance/MVP_VERTICAL_IMPLEMENTATION_PLAN.md`.

## Structure

Trois blocs : (1) exécution bornée Hermès + pgvector → candidats, avec frontière de retrieval appliquée en SQL avant le ranking ; (2) capture/contrat et affichage/décision côté OpenWebUI (Function candidate, quatre actions) ; (3) Decision Records et Register Candidate autorisé. Critères d'acceptation par bloc, mappés sur ceux de la spec. Décision bloquante unique : l'arbitrage d'hébergement du code exécutable (`HERMES_CODE_HOSTING_BOUNDARY.md`, hypothèse Option A — dépôt frère).

## Nature et bornes

Documentation uniquement : aucun runtime, scheduler, queue, provider router, plugin manager, promotion de mémoire automatique ni approbation automatique ; `schemas/`, `tests/`, CI et `mcp-server/` intouchés ; lignes ARBITRAGE intouchées. Tout l'exécutable décrit vit côté Hermès, hors du noyau de gouvernance.
