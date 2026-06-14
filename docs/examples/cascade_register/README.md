# Dossier d'instances — cascade Registre Probatoire (exemple)

Exemple fictif et validé : un mini-dossier d'architecture qui exerce les
schémas `register_candidate`, `register_link` et `impact_review`, et la règle
de cascade.

Scénario : le client demande d'aménager le sous-sol en cours de projet (ERP).
Valider cette preuve a des conséquences en cascade — la classification ERP est
déclassée, et les issues de secours partent en arbitrage (critique, jamais
déclassé en silence).

## Fichiers

| Fichier | Schéma | Rôle |
|---|---|---|
| `candidate.p-202.yaml` | `register_candidate` | Aménagement du sous-sol (déclencheur) |
| `candidate.p-150.yaml` | `register_candidate` | Classification ERP actuelle (cible) |
| `link.p202-impacts-p150.yaml` | `register_link` | P-202 impacte P-150 (réglementaire, élevé) |
| `link.p202-impacts-issues.yaml` | `register_link` | P-202 impacte les issues de secours (critique) |
| `impact_review.erp-basement.yaml` | `impact_review` | La cascade ouverte à la validation de P-202 |

## Validation

`.github/scripts/check_register_instances.py` valide chaque fichier contre son
schéma, vérifie l'intégrité des `link_ids` et applique la règle de cascade
(critique ⇒ `critical_arbitration` ; review `resolved` ⇒ décision par cible).
Il réutilise `evaluate_impact_review` du doctor `mcp-server`, source unique de
la règle. Lecture seule : il signale, il ne décide pas.

Statut : exemple — documenté non implémenté (données fictives).
