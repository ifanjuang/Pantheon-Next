# Note de travail — Piste ChatGPT : optimisations du dépôt Pantheon Next

Date : 2026-06-10.
Statut : ordre de travail (work order) — préparé pour la piste ChatGPT du mainteneur.
Trace : cette note est aussi un journal d'intervention IA (analyse + préparation de handoff, aucun changement de doctrine).

La note ci-dessous est autonome : elle peut être collée telle quelle dans une session ChatGPT ayant accès au dépôt `ifanjuang/Pantheon-Next`.

---

## CONTEXTE (à lire avant tout travail)

Pantheon Next est un dépôt de **gouvernance pure** pour le travail professionnel assisté par IA. Doctrine immuable :

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Le dépôt contient ~143 documents Markdown de gouvernance (`docs/governance/`), 8 schémas YAML de validation (`schemas/`), 2 tests read-only (`tests/`), des templates non exécutables (`templates/`), des profils Hermès candidats (`hermes/`), et un CI (`.github/workflows/governance-ci.yml`).

Avant de commencer, lire obligatoirement :

1. `CLAUDE.md` (règles du dépôt, zones, frontières) ;
2. `docs/governance/GLOSSARY.md` (les 4 axes : E0–E4 certitude probante, V0–V4 vérification de réponse, K0–K4 conséquence, C0–C5 plafond d'approbation) ;
3. `docs/governance/AUTHORITY_INDEX.md`, `STATUS.md`, `TARGET_ARCHITECTURE.md` ;
4. `ai_logs/README.md` (règles du journal).

## RÈGLES ABSOLUES (non négociables)

1. **Chemins protégés — ne JAMAIS modifier sans approbation explicite du mainteneur** : `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml`, fichiers Docker, fichiers `.env`. Pour ces chemins, produire une **proposition validation-only** (le contenu imprimé dans une note de gouvernance, jamais en fichier exécutable) — modèle : `docs/governance/REGISTRE_PROBATOIRE_SCHEMA_PROPOSAL.md` (E6).
2. **Aucun runtime** : pas de scheduler, queue, agent, promotion mémoire, approbation automatique. Tout script ajouté est **read-only** (il lit et signale, il n'écrit ni ne corrige).
3. **Tout reste candidat** jusqu'à revue : ne jamais auto-déclarer un nouveau document « active doctrine ». Statut d'entrée : `candidate / to verify` ou `validation-only`.
4. **Une PR par lot**, en **draft**, branche dédiée, sans toucher d'autres lots. Ne pas éditer `AUTHORITY_INDEX.md` / `MODULES.md` / `STATUS.md` dans les PRs de contenu (voir Lot 4).
5. **Chaque intervention ajoute une entrée `ai_logs/`** (`YYYY-MM-DD-sujet.md`) : intent, travail effectué, frontière respectée, état du dépôt.
6. **Vocabulaire** : « Registre Probatoire » / « Register Candidate » (jamais « Canonical Memory » réintroduit) ; le CI le vérifie. Ne jamais utiliser C0–C5 pour la conséquence (c'est l'axe K).
7. Distinguer toujours : implemented / documented but not implemented / partial / obsolete / to verify.

## ORDRE ET DÉPENDANCES

```text
Lot 1 (CI checks)      → indépendant, à faire en premier
Lot 2 (déduplication)  → après Lot 1 (les checks protègent la refonte)
Lot 3 (axes partagés)  → APRÈS E6 uniquement (E6 est déjà en cours sur la
                          piste ChatGPT, PR #87) ; ne pas mener en parallèle
Lot 4 (process PR)     → indépendant, rapide
Lot 5 (digest machine) → après Lot 1 (réutilise le parseur d'en-têtes)
```

**Coordination E6** : la piste ChatGPT travaille déjà sur E6 (rename
`memory_candidate` → `register_candidate`, PR #87). Cette note ne couvre PAS
E6 ; ne pas le dupliquer ici. Le Lot 3 démarre seulement quand E6 est approuvé
et appliqué, et son fichier d'axes proposé doit référencer le schéma renommé
(`register_candidate`), pas l'ancien nom.

---

## LOT 1 — Étendre le CI de gouvernance (checks read-only)

**Objectif** : transformer les conventions manuelles en vérifications automatiques. C'est la Phase 4 (« Doctor ») de `docs/governance/ROADMAP.md`.

**Emplacement** : scripts Python sans dépendance externe (stdlib uniquement) sous `.github/scripts/` ; appel depuis `.github/workflows/governance-ci.yml` (étendre le job existant, ne pas le remplacer).

**Checks à implémenter** (chacun : liste les violations avec chemin + ligne, exit 1 si violation, exit 0 sinon ; mode `--list` pour rapport) :

1. `check_status_headers.py` — tout fichier `docs/governance/**/*.md` (hors `README.md`) doit déclarer dans ses 10 premières lignes une ligne `Status:` dont la valeur contient l'un de : `canonical`, `active doctrine`, `active support`, `support`, `candidate`, `validation-only`, `reference`, `stub`, `obsolete`, `example`. Dresser d'abord l'inventaire réel des formulations existantes et proposer la liste normalisée dans la PR (ne pas inventer une taxonomie nouvelle : reprendre celle d'`AUTHORITY_INDEX.md`).
2. `check_internal_links.py` — tout chemin relatif référencé dans un Markdown de gouvernance (liens `[..](..)` et mentions de chemins `docs/...`, `schemas/...`, `templates/...` dans le texte et les blocs ```text```) doit exister dans le dépôt. Tolérance : liste d'exclusions explicite en tête de script pour les chemins volontairement futurs (ex. `mcp-server/`, `dashboard/`), chaque exclusion commentée.
3. `check_index_coverage.py` — tout document déclarant `Status: candidate` doit avoir une ligne dans `AUTHORITY_INDEX.md`. Signaler aussi l'inverse : entrées d'index pointant vers des fichiers supprimés.
4. `check_axis_vocabulary.py` — garde des axes : signaler (a) `C0`–`C4`/`C5` utilisés comme niveau de *conséquence* (motifs type `consequence.*C[0-5]`, `C[0-5]_` suivis d'un mot de conséquence) ; (b) tout nouveau champ `confidence:` dans un YAML (le champ canonique est `certainty`, axe E) ; (c) `K[0-4]` utilisé comme plafond d'approbation. Calibrer sur le corpus actuel : le check doit passer sur `main` (mettre les violations héritées en liste d'exception datée, à purger).

**Critères d'acceptation** : CI vert sur `main` ; chaque check documenté en tête de fichier (quoi, pourquoi, comment exclure) ; aucun check ne modifie de fichier ; entrée `ai_logs/` ; PR draft intitulée `ci: read-only governance checks (status headers, links, index coverage, axes)`.

**Ne pas faire** : pas d'auto-fix, pas de dépendance pip ajoutée à `pyproject.toml` (protégé), pas de hook git imposé.

## LOT 2 — Déduplication des blocs de frontière + consolidation

**Objectif** : réduire la masse sans perdre le sens.

1. **`docs/governance/BOUNDARY_STANDARD.md`** (nouveau, `Status: candidate`) : un document unique listant les effets interdits standard (runtime, scheduler, queue, approval engine, memory engine, provider router, connector gateway, external action…) avec la phrase de référence courte à utiliser ailleurs, par ex. : `Boundary: standard non-implementation boundary applies — see BOUNDARY_STANDARD.md.`
2. **Remplacement mécanique prudent** : dans les documents où le bloc « does not implement … » est strictement le bloc standard, le remplacer par la ligne de référence. Si un document a des interdits *spécifiques* en plus, garder uniquement les spécifiques + la ligne de référence. Faire cela par paquets de ~15 fichiers maximum par PR pour rester relisible. Compter et annoncer les lignes économisées dans chaque PR.
3. **Consolidation `EVIDENCE_TOPOLOGY_*`** : fusionner les ~5–8 fichiers `EVIDENCE_TOPOLOGY_*.md` en un seul `EVIDENCE_TOPOLOGY.md` (sections = anciens fichiers), avec table de correspondance ancienne→nouvelle en tête. Les anciens fichiers deviennent des renvois d'une ligne (« moved to ») ou sont supprimés si le Lot 1.2 confirme qu'aucun lien n'est cassé. Les `evidence_topology_antipatterns/` restent où ils sont.
4. **Stubs « migration pending »** : inventorier tous les documents marqués stub/migration pending (ex. `EPISTEMIC_CONTROL.md`, `MODEL_ROUTING_POLICY.md`, `ROUTING_FOUNDATION.md`, `SKILL_LIFECYCLE.md`, etc.). Pour chacun proposer dans une note unique : migrer / marquer `obsolete` / fusionner. **Ne pas supprimer** sans décision du mainteneur — livrer la note de décision (une ligne par stub, recommandation argumentée en 1 phrase).

**Critères d'acceptation** : CI du Lot 1 vert après chaque PR ; aucun changement de sens (déduplication ≠ réécriture) ; le mainteneur peut relire chaque PR en < 15 min.

## LOT 3 — Vocabulaire d'axes partagé (proposition seulement, chemin protégé)

**Objectif** : une seule source machine-lisible pour E0–E4 / V0–V4 / K0–K4 / C0–C5.

**Livrable** : `docs/governance/SHARED_AXES_PROPOSAL.md` (`Status: validation-only proposal`), sur le modèle d'E6, contenant :

1. le futur fichier `schemas/shared_axes.yaml` **imprimé dans la note** (définitions + libellés des 4 axes, source : GLOSSARY) ;
2. la liste exacte des schémas existants à faire pointer dessus (et comment : `$ref` ou enum recopié avec commentaire de source) ;
3. l'impact sur le schéma issu d'E6 (`register_candidate`, PR #87 — déjà en cours sur la piste ChatGPT : s'appuyer sur son résultat, ne pas le refaire) et sur les schémas de la PR #35 (leurs `consequence_level` C0–C5 doivent migrer vers l'axe K) ;
4. une checklist d'approbation pour le mainteneur.

**Interdit** : créer ou modifier quoi que ce soit sous `schemas/` ou `tests/` dans ce lot.

## LOT 4 — Hygiène des PRs

1. **`.github/PULL_REQUEST_TEMPLATE.md`** (nouveau) avec sections : Summary / Boundary (chemins protégés touchés ? non-implémentation ?) / Statut déclaré des nouveaux docs / Entrée `ai_logs/` ajoutée ? / Index : « cette PR ne touche pas AUTHORITY_INDEX, MODULES, STATUS » (case à cocher).
2. **Règle d'indexation séparée** : ajouter une courte section « Indexing rule » à `docs/governance/AUTHORITY_INDEX.md` (ou note dédiée si le mainteneur préfère) : les PRs de contenu n'éditent pas les 3 index ; une PR de réindexation par lot suit, guidée par le check 1.3 du Lot 1 qui liste ce qui manque.

## LOT 5 — Digest machine-lisible de la gouvernance

**Objectif** : un index YAML généré, consommable par Hermès / le futur `mcp-server/` / le mainteneur. Correspond à la Phase 1 (« canonical source map ») de `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` (PR #75).

1. `.github/scripts/build_governance_digest.py` (read-only sur les docs ; écrit uniquement le digest) : parcourt `docs/governance/**/*.md`, extrait : chemin, titre (premier `#`), `Status:`, première phrase de résumé, axes mentionnés (E/V/K/C), `governance_refs` détectés.
2. Sortie : `docs/governance/GOVERNANCE_DIGEST.yaml` avec en-tête `# GENERATED — do not edit; regenerate with .github/scripts/build_governance_digest.py`.
3. Job CI qui vérifie que le digest commité est à jour (régénère et diff ; échec si divergence).

**Critère** : le digest est exact, régénérable, et ne porte **aucune autorité** propre (le statut vient des docs ; le digest est une projection — l'écrire dans son en-tête).

---

## CONVENTIONS COMMUNES À TOUS LES LOTS

- Branches : `chatgpt/lot1-ci-checks`, `chatgpt/lot2-boundary-dedup`, etc.
- PRs en **draft**, titre préfixé `ci:` / `docs:` selon le lot, corps avec section Boundary explicite.
- Une entrée `ai_logs/` par PR.
- Pas d'entrée `CHANGELOG.md` sans accord (rotation récente ; conflits fréquents).
- En cas de doute entre deux interprétations : poser la question dans la PR, ne pas trancher.

## DÉFINITION DE « TERMINÉ »

```text
Lot 1 : CI vert sur main avec les 4 checks actifs.
Lot 2 : BOUNDARY_STANDARD mergé, ≥ 1 vague de déduplication mergée,
        EVIDENCE_TOPOLOGY consolidé, note de décision stubs livrée.
Lot 3 : proposition SHARED_AXES livrée avec checklist d'approbation.
Lot 4 : template PR en place, règle d'indexation documentée.
Lot 5 : digest généré + vérifié par le CI.
```

---

## Frontière de cette note

Cette note est un ordre de travail et une trace. Elle ne change aucune doctrine, ne promeut aucun candidat, ne touche aucun chemin protégé. Tout livrable décrit ci-dessus reste candidat jusqu'à revue par le mainteneur.
