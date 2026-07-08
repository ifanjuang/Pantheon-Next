# 2026-07-08 — Réparation des guards après les 13 commits MVP directs sur main

## Intervention

Sur demande du mainteneur (« Vérifie ce qu'a fait chatgpt » puis « Vas-y ») : audit des 13 commits poussés directement sur main (82f1e42..5af0b09, préparation du bloc 1 du vertical) et réparation des casses. 8 de ces 13 pushes avaient une CI rouge ; main était rouge au moment de l'audit.

## Constats d'audit

- Fond solide et cohérent avec `MVP_GOVERNED_TASK_LOOP.md` : fixtures ordonnées de la boucle (nominale, sous-ensemble schéma, cas d'échec délibéré), design de validateur, invariants, plan de validation, schéma candidat des cinq objets, cinq ai_logs.
- Casses : 12 en-têtes `Status:` hors vocabulaire (11 fixture + 1 reference_reviews), 1 candidat non indexé, schéma sans `x-boundary` ni exemple ni test (convention #37), vocabulaire de clés du narratif (`object:`/`id:`) divergent du schéma (`object_type:`/`object_id:`).
- Le double fichier fixture (narratif complet vs sous-ensemble schéma) est un design délibéré documenté dans `SCHEMA_ALIGNMENT.md` — conservé.

## Réparations

- 12 en-têtes `Status:` normalisés vers les familles acceptées (« candidate support note — … », « active support index — … ») ; descripteurs d'origine conservés.
- Ligne d'index pour `POSTGRES_PROPERTY_GRAPH_CAPABILITY.md` + **ligne groupée** pour `docs/governance/examples/mvp_vertical_fixture/`.
- Clés du narratif `fixture.yaml` harmonisées (`object_type:`, `object_id:`) — contenu inchangé.
- Schéma : bloc `x-boundary` ajouté, `governance_refs` doté d'un `default` (pointeurs seuls), exemple `schemas/examples/mvp_governed_loop_objects.example.yaml` (le task_contract du sous-ensemble schéma, déjà valide), câblage dans `tests/test_governance_schemas.py` et `tests/test_schema_examples.py`. Chemins protégés touchés via PR revue — aucun champ de validation ajouté/supprimé/renommé, enums intacts, `additionalProperties` inchangé.

## Vérification

8 scripts de guard verts en full-tree, guard « runtime phrases » vert, tests racine 12/12 (le schéma MVP est désormais sous le filet), tests mcp-server 122/122, exemple validé contre le schéma.

## Correction post-revue (Codex, PR #311)

`CAPABILITY_CANDIDATE_DISTILLATES.md` : « active support index » surclassait l'autorité du répertoire `reference_reviews/` (external reference / support review, non-doctrinal sauf distillation). Reclassé « support review index » — famille acceptée par le guard et conforme au placement du sous-index des références externes.

