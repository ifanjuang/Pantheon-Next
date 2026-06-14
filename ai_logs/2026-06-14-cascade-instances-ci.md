# AI Log — Validated register instances + CI cascade enforcement

Date: 2026-06-14

## Demande

« Pousse » : aller plus loin que les schémas et le doctor — un vrai dossier
d'instances `register_link` / `impact_review` (et `register_candidate`) validé
en CI par la règle de cascade.

## Action

- Dossier d'exemple `docs/examples/cascade_register/` : mini-dossier fictif et
  cohérent (reclassement ERP sous-sol) — deux `register_candidate` (déclencheur
  P-202, cible P-150), deux `register_link` (un élevé, un critique vers les
  issues de secours) et un `impact_review`. L'impact critique est en
  `critical_arbitration` ; aucun déclassement silencieux.
- `.github/scripts/check_register_instances.py` : contrôle read-only qui valide
  chaque instance contre son schéma, vérifie l'intégrité référentielle des
  `link_ids`, et applique la règle de cascade en réutilisant
  `evaluate_impact_review` du doctor `mcp-server` (source unique de la règle).
- Étape `Register instance + cascade rule validation` ajoutée à
  `.github/workflows/governance-ci.yml` (pip install jsonschema + pyyaml).
- Vérifié localement : 5 instances valides, `link_ids` résolus, règle satisfaite ;
  et échec attendu sur un cas critique déclassé en silence (test négatif).
- Indexé dans `docs/examples/README.md` ; CHANGELOG 0.1.54.

## Boundary

Lecture seule : le contrôle signale, cite, rapporte ; il n'édite, ne corrige ni
ne décide. Les instances enregistrent des propositions et des décisions humaines.
Aucun runtime, scheduler, file, routeur de fournisseur, moteur d'approbation,
promotion de mémoire ni résolution de cascade automatique.

## Related

- `docs/examples/cascade_register/`
- `.github/scripts/check_register_instances.py`
- `.github/workflows/governance-ci.yml`
- `mcp-server/pantheon_mcp/doctor.py`
- `schemas/register_link.schema.yaml`, `schemas/impact_review.schema.yaml`, `schemas/register_candidate.schema.yaml`

## Repo state

Implémenté : dossier d'instances validé + application de la règle de cascade en
CI (read-only). Aucune résolution automatique.
