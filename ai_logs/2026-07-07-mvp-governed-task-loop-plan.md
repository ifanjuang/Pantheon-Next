# 2026-07-07 — Plan MVP : mvp-governed-task-loop

## Intervention

Sur demande du mainteneur : documentation d'une première boucle gouvernée complète et minimale entre OpenWebUI, Hermès et pgvector — `docs/governance/MVP_GOVERNED_TASK_LOOP.md` plus quatre formes d'objets illustratives sous `docs/governance/examples/`. PR courte et dédiée.

## Nature et bornes

Documentation uniquement. Aucun runtime, scheduler, queue, provider router, plugin manager, promotion de mémoire automatique ni approbation automatique n'est ajouté ; la boucle compose la doctrine existante (Task Contract, Evidence Pack, User Decision Gate, Registre Probatoire) sans nouvelle règle. `schemas/` volontairement intouché (instruction explicite : pas de modification avant relecture) ; les YAML d'exemples sont non normatifs. Les 46+ lignes ARBITRAGE du plan de nettoyage restent intouchées.

## Choix d'adaptation

- Le terme « MemoryCandidate » de la demande est projeté sur le vocabulaire courant **Register Candidate** (GLOSSARY ; « Memory Candidate » est un terme retiré, bloqué par le guard anti-régression). Les noms de fichiers demandés sont conservés tels quels ; la prose utilise le terme courant avec note de correspondance.
- Scénario de référence : `architecture_devis_reprise` (le cas porteur du dépôt), pour que la démonstration future parte d'un dossier déjà documenté.
- Le document est indexé comme candidat dans `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` (règle de couverture des sous-index).

## Critère de réussite

La boucle est démontrée quand un dossier réel passe les neuf étapes avec au moins un refus ou une révision au gate (le gate doit être exercé), un Decision Record par décision, et au plus un Register Candidate créé sur autorisation explicite. La démonstration produit une entrée `ai_logs/` ; toute promotion reste une décision revue séparée.
