# 2026-06-30 — Audit qualité global du dépôt

## Quoi
Ajout de `docs/audits/2026-06-30-audit-qualite-global-pantheon-next.md` : lecture critique transversale du dépôt (gouvernance, code, schémas, docs MD/HTML, frontières doctrinales), assortie de préconisations (P1–P7) et d'arbitrages (B-1 à B-8) avec recommandations.

## Pourquoi
Demande du mainteneur : analyse qualitative complète, liste de problèmes / incohérences / redondances, et arbitrages avec recommandations, vus aussi sous l'angle architecte-dev, utilisateur professionnel et doctrine Pantheon.

## Portée
- Document d'audit uniquement (`docs/audits/`).
- Aucune doctrine créée ni promue ; aucun candidat promu.
- Aucune modification de `schemas/`, `tests/`, `mcp-server/`, `pyproject.toml` ni d'un chemin protégé.
- Toutes les préconisations restent des candidats soumis à revue humaine et à la User Decision Gate.

## Risques / limites
- Lecture d'opinion : les arbitrages B-1 à B-8 engagent des décisions de mainteneur, non tranchées ici.
- Les constats de risque licence (`base_metier/architecte/`) et de dérive de frontière (`dashboard/`) demandent une vérification humaine avant action.
- Aucune correction appliquée : l'audit constate, il ne corrige pas.
