# AI Log — Cascade follow-ups (rule check, link reference, mockup wiring)

Date: 2026-06-14

## Demande

Après l’ajout des schémas `register_link` / `impact_review`, traiter les trois
suites proposées : (1) un doctor check read-only qui valide les instances et
applique « critique jamais déclassé en silence » ; (2) câbler la maquette sur
ces schémas ; (3) étendre `register_candidate` pour référencer ses liens.

## Action

1. **Doctor check** — `mcp-server/pantheon_mcp/doctor.py` :
   - `evaluate_impact_review(data)` : fonction pure, règle déclarative
     (critique ⇒ `critical_arbitration` ; review `resolved` ⇒ décision
     enregistrée par cible) ;
   - `check_cascade_rule(root)` : scanne `schemas/examples` et `docs/examples`,
     valide chaque `impact_review` contre le schéma (si jsonschema dispo) puis
     applique la règle ; ajouté à `run_all`. Imports yaml/jsonschema gardés.
   - Tests : `mcp-server/tests/test_cascade_doctor.py` (5) ; suite module
     toujours verte (21 au total hors tests exigeant le SDK `mcp`).

2. **Maquette** — `docs/assets/pantheon-control/` : la page Preuves parle le
   vocabulaire des schémas. Chaque preuve porte des liens au format
   `register_link` (relation, to_id, dependency_type, impact_level). Valider
   construit un objet `impact_review` et applique la règle à l’écran : une cible
   critique passe en « Arbitrage requis », jamais un déclassement silencieux.

3. **Schéma** — `schemas/register_candidate.schema.yaml` gagne `link_ids`
   (références optionnelles vers `register_link`) ; l’exemple le démontre.

CHANGELOG 0.1.53.

## Boundary

Le doctor signale, cite et rapporte ; il n’édite, ne corrige ni ne décide. Les
schémas et la maquette enregistrent des propositions et des décisions humaines.
Aucun runtime, scheduler, file, routeur de fournisseur, moteur d’approbation,
promotion de mémoire ni résolution de cascade automatique.

## Related

- `mcp-server/pantheon_mcp/doctor.py`, `mcp-server/tests/test_cascade_doctor.py`
- `schemas/register_link.schema.yaml`, `schemas/impact_review.schema.yaml`
- `schemas/register_candidate.schema.yaml`
- `docs/governance/REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md`

## Repo state

Implémenté : schémas de validation + doctor check read-only + maquette alignée.
Aucune résolution de cascade automatique.
