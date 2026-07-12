# Première démonstration complète de la boucle gouvernée (blocs 1-3)

Date: 2026-07-10

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: cette trace de la première exécution de bout en bout des neuf étapes de `MVP_GOVERNED_TASK_LOOP.md`, réalisée dans le dépôt externe (arbitrage Option A) sur le dossier fictif `devis_reprise`, contre une instance pgvector 0.6.0 réelle.
- Updated: ancrage de vérification externe ajouté le 2026-07-12.
- Removed: rien.

## Why

Les critères d'acceptation de la spec exigent : « Demonstration produces an ai_logs/ entry ». La démonstration a eu lieu ; voici son enregistrement.

Résultat rapporté du run historique : 2 décisions enregistrées, dont 1 `request_revision`, 1 Register Candidate en attente d'admission au Registre Probatoire, 0 action externe (`external_action_authorized: false` constitutif). La trace de session rapporte 17/17 tests d'acceptation au moment du premier run, puis 24/24 après les correctifs P0 de `PANTHEON_MVP_VERTICAL_BINDING.md`.

Le SHA exact du premier run 17/17 n'est pas récupérable avec certitude depuis cette trace seule. Il n'est donc pas reconstruit ni affirmé rétrospectivement.

## External verification anchor

Une vérification ultérieure du dépôt externe est précisément épinglée :

```text
external_repository: ifanjuang/pantheon-mvp
external_commit: 28d7846a3edc9a9f533b873c5ac49e67cec2ca48
external_workflow: Pantheon MVP CI
external_workflow_run: 29201089740
external_workflow_run_number: 31
external_workflow_conclusion: success
observed_at: 2026-07-12
```

Cet ancrage confirme l'état vérifié du dépôt externe à ce commit. Il ne prétend pas être le SHA historique exact du premier run 17/17.

```text
historical_report != current_verification_anchor
workflow_success != professional_evidence
```

Refus couverts par le démonstrateur et ses tests : fuite de périmètre, question hors périmètre, `external_send`, décision signée par une identité système, et rétention sans autorisation explicite. Les objets sont validés contre le schéma vendored du dépôt externe.

Incident instructif : la règle append-only des Decision Records a intercepté un bug réel de collision d'identifiants pour deux décisions dans la même seconde. La correction a introduit un horodatage à la microseconde et des identifiants distincts.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none — l'exécution a eu lieu dans le dépôt externe, hors de Pantheon Next.
Authority impact: none.
Schema/test/CI impact in Pantheon Next: none.
External action: none.
Memory behavior: none — le Register Candidate produit attend l'admission ; rien n'est promu.

## Local distinctions

```text
demonstration_ran != binding_adopted
workflow_green != professional_evidence
register_candidate != admitted_memory
gate_exercised != gate_generalized
external_repo_verified != Pantheon_activation
```
