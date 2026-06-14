# AI Log — Register-instance validation promoted into the doctor

Date: 2026-06-14

## Demande

« Continue le dev. »

## Constat

Le doctor `mcp-server` ne mirroitait que partiellement la CI : `check_cascade_rule`
ne validait que les instances `impact_review`. La validation complète d'un dossier
Registre Probatoire (schémas des trois types + intégrité référentielle des
`link_ids` + règle de cascade) vivait uniquement dans le script CI
`.github/scripts/check_register_instances.py`. La doctrine veut une source unique
de la règle et un doctor qui répond « les checks sont-ils verts ? » sans lancer la CI.

## Action

- `mcp-server/pantheon_mcp/doctor.py` : ajout de `check_register_instances`
  (read-only). Pour chaque instance sous `docs/examples/cascade_register/`, valide
  contre le schéma correspondant (`register_candidate`, `register_link`,
  `impact_review`), vérifie l'intégrité référentielle des `link_ids`, et applique
  la règle de cascade via `evaluate_impact_review`. Ajouté à `run_all`. Dégrade
  proprement si PyYAML/jsonschema absent.
- `.github/scripts/check_register_instances.py` : réécrit pour importer et exécuter
  `check_register_instances` depuis le doctor — plus de réimplémentation. Le doctor
  devient la source unique ; la CI le miroite.
- `mcp-server/tests/test_cascade_doctor.py` : 3 tests ajoutés (dossier cohérent,
  présence dans `run_all`, référence `link_ids` inconnue signalée). 8 tests passent.
- Nettoyage : suppression de `tmp_should_not_create.txt`, artefact de test
  accidentellement committé puis mergé (ni gouvernance, ni schéma, ni doc).
- CHANGELOG 0.1.55.

## Vérifié

- `python -m pytest` (mcp-server) : 8 passés.
- `python .github/scripts/check_register_instances.py` : « 5 register instance(s)
  valid; link_ids resolve; cascade rule satisfied. »
- Tests racine `tests/` : 7 passés.

## Boundary

Lecture seule : le doctor signale, cite, rapporte ; il n'édite, ne corrige ni ne
décide. Aucun runtime, scheduler, file, routeur de fournisseur, moteur
d'approbation, promotion de mémoire ni résolution de cascade automatique.

## Related

- `mcp-server/pantheon_mcp/doctor.py`
- `.github/scripts/check_register_instances.py`
- `mcp-server/tests/test_cascade_doctor.py`
- `docs/examples/cascade_register/`
- `schemas/register_candidate.schema.yaml`, `schemas/register_link.schema.yaml`, `schemas/impact_review.schema.yaml`

## Repo state

Implémenté : validation complète des instances Registre Probatoire dans le doctor
(source unique), miroitée par la CI. Aucune résolution automatique.
