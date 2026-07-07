# 2026-07-07 — Nettoyage gouvernance, passe B : absorption des clusters

## Intervention

Exécution de la passe B du plan de nettoyage approuvé : 13 documents satellites absorbés intégralement (verbatim, titres rétrogradés d'un niveau) dans leur document mère, puis supprimés. Le contenu n'est pas perdu : il vit dans la cible sous une section « Absorbed: … (2026-07-07) », et l'original reste dans l'historique git.

## Mapping des absorptions

| Source (supprimée) | Cible |
|---|---|
| `CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md` | `CARD_STACK_MODEL.md` |
| `CARD_STACK_ROLE_QUALITY_ALIGNMENT.md` | `CARD_STACK_MODEL.md` |
| `DATA_PLATFORM_INDEX.md` | `DATA_PLATFORM_ARCHITECTURE.md` |
| `DATA_PLATFORM_STATUS.md` | `DATA_PLATFORM_ARCHITECTURE.md` |
| `EXTERNAL_AGENTIC_INSPIRATIONS.md` | `EXTERNAL_TOOLS_POLICY.md` |
| `EXTERNAL_AI_OPTION_REVIEWS.md` | `EXTERNAL_TOOLS_POLICY.md` |
| `EXTERNAL_METHOD_REVIEWS.md` | `EXTERNAL_TOOLS_POLICY.md` |
| `EXTERNAL_REPO_INSPIRATIONS.md` | `EXTERNAL_TOOLS_POLICY.md` |
| `EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md` | `EXTERNAL_TOOLS_POLICY.md` |
| `HERMES_EVALUATION_AND_SIMULATION_LAYER.md` | `HERMES_INTEGRATION.md` |
| `HERMES_KANBAN_EXECUTION_PATTERNS.md` | `HERMES_INTEGRATION.md` |
| `HERMES_PAGE_AGENT_INTEGRATION.md` | `HERMES_INTEGRATION.md` |
| `OPENWEBUI_TEMPLATES.md` | `OPENWEBUI_INTEGRATION.md` |

## Références

Toutes les références repo-wide (docs, schémas, exemples, templates, profils Hermes, runbook) sont réécrites de la source vers la cible ; les listes YAML `governance_refs` sont dédoublonnées ; les lignes de sous-index devenues redondantes sont retirées.

## Écarts assumés par rapport au plan livré

- `_TEMPLATE_RITE.md` gardé (faux positif : son en-tête liste l'énumération des statuts possibles, dont « superseded »).
- `RAG_INGESTION_*.md` gardés tous deux (pas de document mère existant ; une fusion aurait créé un document neuf, hors périmètre mécanique).
- `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md` et `evidence_topology_antipatterns/ANTI_PATTERN_SUMMARY_ONLY_HANDOFF.md` reclassés hors fusion (le motif « HANDOFF » avait été pris pour une réconciliation) — intouchés.
- `AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` gardé : le master index le cite comme base constitutionnelle de la décomposition (#287).
- `.github/` volontairement intouché (les pushes de session modifiant les workflows suppriment le déclenchement CI ; une entrée obsolète inoffensive subsiste dans l'EXCLUDED de `check_axis_vocabulary.py` — à purger par le mainteneur avec le patch full-tree).

## Bilan

`docs/governance/` : 241 → 167 documents (−61 passe A, −13 passe B). Les ~68 documents ARBITRAGE restent intouchés sur décision du mainteneur ; leur triage est la prochaine passe possible.

## Vérification

8 scripts de guard verts en full-tree, guard « runtime phrases » vert, tests racine 12/12, tests mcp-server 122/122.

## Corrections de revue (PR #279)

Le mainteneur a corrigé lui-même les chemins de lecture du `README.md` de gouvernance et la ligne Data Platform de `STATUS.md` (commits `e390e23`, `bc91874`) ; cette passe complète avec le balayage systématique des doublons résiduels du réécriveur : `MODULES.md` (×2), `DATA_PLATFORM_ARCHITECTURE.md`, `RAG_INGESTION_PIPELINE.md`, `ROADMAP.md` (×2).

## Confirmations finales (demandées en revue)

- **Lignes ARBITRAGE : intouchées.** Aucun document classé ARBITRAGE dans le plan de triage n'a été supprimé, fusionné ou modifié par les passes A/B ni par ces corrections.
- **`schemas/` : touché uniquement pour des descriptions, des commentaires et des pointeurs `governance_refs`.**
- **Aucun champ de contrat de schéma ajouté, supprimé ou renommé ; enums intacts.**

