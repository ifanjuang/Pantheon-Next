# 2026-07-08 — Arbitrage d'hébergement du code exécutable : Option A

## Décision

Décision humaine explicite du mainteneur (2026-07-08, en session) : **Option A** de `docs/governance/HERMES_CODE_HOSTING_BOUNDARY.md`. Le code exécutable du vertical MVP (runner Hermès, ingestion, configuration du store pgvector) vit dans un dépôt frère `pantheon-mvp-vertical`. Pantheon-Next conserve uniquement les artefacts read-only : doctrine, schémas, fixtures, validateurs, traces.

## Portée et bornes

- La frontière une-direction de `CLAUDE.md` est préservée : le dépôt frère consomme la doctrine et le plan de policy (`mcp-server/`) ; rien d'exécutable ne remonte ici.
- Le premier fichier exécutable de runtime proposé dans Pantheon-Next rouvrirait l'arbitrage (il n'hérite pas de celui-ci).
- Référent B-5 : cette entrée datée constitue la décision enregistrée.

## Suite immédiate

Bloc 1 du plan (`MVP_VERTICAL_IMPLEMENTATION_PLAN.md`) : ingestion bornée aux sources déclarées du Task Contract, retrieval scopé en SQL avant ranking, runner produisant Result Candidate + Evidence Pack Candidate, validées par `scripts/validate_mvp_fixture.py`.
