# 2026-07-05 — Purge de la dette de guards et passage de la CI en full-tree

## Intervention

Application des recommandations actionnables de l'audit du 2026-07-04 (même PR), sur instruction explicite du mainteneur.

## Changements

- 16 violations latentes de guards purgées (liens internes ×4, couverture d'index ×4, vocabulaire d'axes ×8) — détail dans `CHANGELOG.md` 0.1.61.
- Passage des guards en full-tree : **préparé, non appliqué** — les pushes touchant `.github/workflows/` depuis la session automatisée font que GitHub cesse de créer des runs CI pour la PR (permission `workflows` absente côté intégration). Le changement reste une action mainteneur (chemin protégé). Patch à appliquer sur `.github/workflows/governance-ci.yml` :

```diff
       - name: Governance doctor read-only checks
         shell: bash
-        env:
-          GOVERNANCE_BASE_REF: ${{ github.event.pull_request.base.sha || github.event.before }}
         run: |
           set -euo pipefail
           python3 .github/scripts/check_status_headers.py
           python3 .github/scripts/check_internal_links.py
           python3 .github/scripts/check_index_coverage.py
           python3 .github/scripts/check_axis_vocabulary.py
           python3 .github/scripts/check_no_truncation.py
-          python3 .github/scripts/check_no_net_truncation.py
+          GOVERNANCE_BASE_REF="${{ github.event.pull_request.base.sha || github.event.before }}" \
+            python3 .github/scripts/check_no_net_truncation.py
```

  Vérifié localement : les huit scripts passent en full-tree sur cet arbre.
- `VERSION`, `pyproject.toml`, `mcp-server/pyproject.toml` → 0.1.61 ; entrée CHANGELOG 0.1.61.
- Tag `v0.1.60` : **non poussé** — le remote refuse les pushes de tags depuis la session automatisée. Action mainteneur requise : `git tag -a v0.1.60 3375fcb && git push origin v0.1.60`, puis `v0.1.61` sur le commit de merge de la PR. `v0.1.59` non taggable rétroactivement (commit absent de la lignée réécrite).

## Nature et bornes

Chemins protégés touchés : `schemas/` (descriptions et commentaires uniquement — aucun champ ajouté/supprimé/renommé, enums intacts) et le workflow CI (portée des guards). Autorisation : demande explicite du mainteneur ; revue via PR #279. Aucun runtime, aucune promotion de mémoire, aucune approbation automatique.

## Vérification

Full-tree local : 8 scripts de guard verts, guard « runtime phrases » vert, tests racine 12/12, tests mcp-server 122/122.
