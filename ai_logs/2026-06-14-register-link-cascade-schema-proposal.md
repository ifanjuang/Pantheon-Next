# AI Log — Register Link & Cascade schema proposal

Date: 2026-06-14

## Demande

Après la maquette dashboard (cascade rendue à l’écran sur la page Preuves),
formaliser le « vrai schéma de liens entre preuves (depends_on / impacts) côté
gouvernance pour piloter ces cascades » — c’est-à-dire passer de la prose et de
l’UI à un contrat machine-checkable.

## Constat

- `schemas/register_candidate.schema.yaml` n’exprime qu’une relation :
  `supersedes_candidate_id`.
- Le modèle dépendances / impacts / cascade est richement décrit en prose dans
  `EVIDENCE_MEMORY_CANONICALIZATION.md` (Dependency model, Impact review,
  Conflict model) et séquencé par `EVIDENCE_MEMORY_DEV_PLAN.md` (Layer 1
  `memory_links`, `impact_reviews`), mais aucun schéma ne le porte.
- `schemas/` et `tests/` sont des chemins protégés : la convention du dépôt
  (cf. `REGISTRE_PROBATOIRE_SCHEMA_PROPOSAL.md`) est d’écrire d’abord une note de
  proposition, puis d’appliquer après approbation explicite.

## Action

Ajout de `docs/governance/REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md` :

- schéma candidat **A — `register_link`** : relation typée et dirigée entre
  deux entrées/candidats (depends_on, impacts, valid_if, invalid_if, supersedes,
  superseded_by, derived_from, conflicts_with, supports, requires_arbitration),
  avec `dependency_type`, `impact_level`, revalidation et scope ;
- schéma candidat **B — `impact_review`** : cascade ouverte quand une entrée
  déclencheuse change ; liste des cibles impactées avec `impact_status`,
  `severity`, action recommandée et **décision humaine** par cible ;
- **règle de cascade déclarative** : critique = arbitrage obligatoire, jamais de
  déclassement silencieux ; aucune cible ne change de statut sans décision
  enregistrée au gate ;
- correspondance explicite avec la maquette (zone « cascade », panneau « À
  valider ») et exemple ERP (sous-sol → reclassement P-150).

Indexé dans `AUTHORITY_INDEX.md` (validation-only). Aucun chemin protégé touché.

## Boundary

Documenté non implémenté. Aucune édition sous `schemas/`, `tests/`,
`operations/`, `platform/`, Docker ou `.env`. Schémas imprimés dans la note pour
revue, non exécutables. Pas de runtime, scheduler, file, routeur de fournisseur
ni promotion de mémoire ; contrat de validation seulement.

## Related

- `docs/governance/REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md`
- `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md`
- `docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md`
- `schemas/register_candidate.schema.yaml`
- issue #68

## Application (après approbation)

Approbation explicite reçue → schémas appliqués :

- ajout de `schemas/register_link.schema.yaml` et `schemas/impact_review.schema.yaml` ;
- ajout des exemples `schemas/examples/register_link.example.yaml` et
  `schemas/examples/impact_review.example.yaml` ;
- mise à jour de `schemas/README.md` et des deux tests
  (`tests/test_schema_examples.py`, `tests/test_governance_schemas.py`) ;
- 7 tests de schémas passent localement ; entrée CHANGELOG 0.1.52.

## Repo state

Implémenté comme schémas de validation (contrats déclaratifs ; aucun runtime,
aucune résolution de cascade automatique).
