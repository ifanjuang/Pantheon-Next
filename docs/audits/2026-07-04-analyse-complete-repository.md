# Analyse complète du dépôt Pantheon Next — 2026-07-04

Statut : audit externe, validation-only. Cette analyse ne crée aucune doctrine et n'approuve rien ; elle constate.

Périmètre : état de `origin/main` au commit `3375fcb` (« docs: correct authority index decomposition plan »), historique CI GitHub Actions des 30 derniers runs, exécution locale complète des suites de tests et des guards de gouvernance.

---

## 1. Vue d'ensemble factuelle

| Mesure | Valeur |
|---|---|
| Fichiers versionnés (hors `.git`) | 1 416 |
| Documents Markdown sous `docs/governance/` | 226 (dont 37 `reference_reviews/`) |
| Fichiers Python | 63 (~2 823 lignes pour le paquet `pantheon_mcp`) |
| Fichiers YAML (schémas, exemples, templates, fixtures) | 193 |
| Entrées `ai_logs/` | 559 |
| Taille du pack git | ~60 Mo (dont ~16 Mo d'images `docs/assets/pantheon-rpg/`, 1,2 Mo `legacy/Pantheon-OS-main.zip`) |
| Version déclarée | 0.1.60 — alignée entre `VERSION`, `CHANGELOG.md`, `pyproject.toml` racine et `mcp-server/pyproject.toml` |
| Tags git sur le remote | **0** |
| PR ouvertes | 0 |

Nature du dépôt : ~97 % de documentation et d'artefacts déclaratifs, ~3 % de code exécutable (le module `mcp-server/`, en lecture seule). C'est conforme à la doctrine affichée (« governance-first »), mais la proportion mérite d'être nommée : le produit décrit (intégration OpenWebUI/Hermes, cockpit, packs métier opérants) n'existe pas encore en dehors de sa description — ce que `WHAT_RUNS.md` reconnaît d'ailleurs honnêtement.

## 2. Ce qui est vérifié et solide

- **Les tests passent.** Suite racine : 12/12. Suite `mcp-server` : 122/122 (après installation de l'extra `mcp`). Les schémas ont des exemples valides et des tests négatifs (signature d'étape incomplète, enum invalide, etc.).
- **Le code respecte ses bornes.** Audit du paquet `pantheon_mcp` : aucun `subprocess`, aucun accès réseau, aucune écriture de fichier. `server.py` n'expose que des primitives de lecture/validation/classification, et chaque docstring d'outil restate le refus d'agir. Les CLI ne font qu'imprimer des verdicts. La revendication « read-only » est tenue dans le code.
- **Les profils Hermes sont bornés dans les deux sens** : `allowed_outputs` (candidats) et `forbidden_outputs` (approbation finale, merge direct, envoi externe, mutation de source de vérité).
- **L'outillage de gouvernance est inhabituellement soigné** : 9 scripts de guard (en-têtes de statut, liens internes, couverture d'index, vocabulaire d'axes, anti-troncature, instances de registre, tranche verticale, intégrité référentielle APU) plus un guard anti-« phrases runtime » avec gestion de la négation. Peu de dépôts de cette taille ont un contrôle de cohérence documentaire automatisé de ce niveau.
- **L'honnêteté de statut est structurée** : `STATUS.md`, `AUTHORITY_INDEX.md`, `MODULES.md`, `WHAT_RUNS.md` forment une hiérarchie explicite avec règles de préséance en cas de désaccord. `WHAT_RUNS.md` distingue « runs / static prototype / documented non-implemented / voluntarily absent » — c'est rare et c'est la vraie originalité du dépôt.
- **La doctrine est cohérente avec elle-même** : la frontière « le noyau ne dépend de rien, mcp-server et l'exposition dépendent du noyau » est respectée dans l'arborescence observée.

## 3. Constats critiques (par gravité décroissante)

### 3.1 La pratique de développement contredit la discipline déclarée

Sur les **30 derniers runs CI de `main` (2026-07-03 21:27 → 2026-07-04 22:30), 29 sont en échec et 1 en succès** (le dernier commit). Échantillon d'échec (`1a62747`) : les **deux** jobs cassés — le guard « Governance files do not suggest Pantheon executes » et les tests `mcp-server`. Le dépôt a donc passé l'essentiel de la journée avec sa propre CI rouge, réparée en fin de séquence.

S'y ajoutent :

- **0 PR ouverte** et un flux visible de commits directs sur `main`, alors que `STATUS.md` et `WHAT_RUNS.md` déclarent des chemins protégés (`schemas/`, `tests/`, `mcp-server/`, CI) exigeant « explicit review » ;
- une **lignée antérieure de `main`** (tête `380af11`, 2026-06-29) divergente de la lignée actuelle (50 commits d'un côté, 94 de l'autre), contenant des commits `test no`, `test forbidden`, `chore: remove accidental temp file` — ce qui indique une réécriture (force-push) de la branche par défaut et des essais de guard commités directement sur `main`.

Pour un projet dont la thèse centrale est la discipline de décision et la trace probatoire, c'est la contradiction la plus sérieuse : la gouvernance décrite s'applique au contenu, pas encore au processus de développement lui-même.

### 3.2 L'invariant de release est violé sur son quatrième terme

L'entrée CHANGELOG 0.1.59 pose l'invariant `VERSION = tête du CHANGELOG = pyproject = tag git` et affirme : « A `v0.1.59` tag is created on the merge commit to make the invariant real ». Or `git ls-remote --tags origin` renvoie **zéro tag**. Les trois premiers termes sont alignés (0.1.60 partout) ; le tag revendiqué n'existe pas. Une affirmation factuelle fausse dans le CHANGELOG d'un projet d'« honnêteté de statut » doit être corrigée en priorité (créer les tags ou rectifier l'entrée).

### 3.3 Les guards sont verts par construction, pas parce que l'arbre est propre

Les scripts de guard sont volontairement limités au diff (`GOVERNANCE_BASE_REF`, politique de baseline du 2026-06-11). Exécutés en full-tree sur `3375fcb`, trois échouent. La purge complète (réalisée à la suite de cet audit, même PR) a traité **16 violations latentes** :

- `check_internal_links` : 4 — deux références vers des documents jamais créés (`reference_reviews/COGNICORE_RUNTIME_REVIEW.md` → `COGNICORE_HERMES_ADAPTER_CANDIDATE.md` ; `reference_reviews/PYTHIA_GOVERNANCE_STATE_REVIEW.md` → `GOVERNANCE_STATE_VIEW.md`) et deux noms de branches `docs/...` pris pour des chemins dans `OPEN_BRANCH_LANDING_PLAN.md` ;
- `check_index_coverage` : 4 candidats non indexés dans `AUTHORITY_INDEX.md` (`MISSING_INFORMATION_DISCIPLINE.md`, `WORKFLOW_DEPTH_POLICY.md`, `CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md`, `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`) ;
- `check_axis_vocabulary` : 8 occurrences — champs `confidence:` non marqués legacy (`role_signal`, `evidence_pack`, leurs exemples, les exemples de topologie) et deux `approval_impact:` mêlant l'axe C à un contexte d'approbation.

Note de méthode : la première mesure de cet audit annonçait « 6 violations » — les sorties des scripts avaient été tronquées à la lecture et les scripts dédupliquent par texte de ligne. Le décompte complet, établi pendant la purge, est de 16.

### 3.4 La production doctrinale dépasse la capacité de promotion

`AUTHORITY_INDEX.md` compte 106 entrées, dont la grande majorité en classe *candidate* (≈65 marquées candidates pour une poignée de canoniques). Le dépôt contient en outre **10 documents « méta »** consacrés à sa propre réconciliation (`*_RECONCILIATION.md`, `REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`, `AUTHORITY_INDEX_DECOMPOSITION_PLAN.md`, `CONCEPTUAL_STABILIZATION.md`, etc.). Le pipeline candidat → revue → promotion est massivement engorgé en amont : on écrit des candidats plus vite qu'on ne les juge, puis on écrit des documents pour gérer l'encombrement. À 226 documents de gouvernance pour un contributeur, le coût marginal de cohérence de chaque nouveau document croît — les trois échecs de guard latents et la file de candidats non indexés en sont les symptômes mesurables.

### 3.5 Hygiène du dépôt

- `legacy/Pantheon-OS-main.zip` (1,2 Mo) : une archive binaire opaque dans l'historique git — non auditable, gonfle le clone ; un tag/release sur le dépôt historique ou un sous-module ferait mieux.
- ~16 Mo d'images sous `docs/assets/pantheon-rpg/` (+ JPEG de 832 Ko à la racine des assets) : pack git ~60 Mo pour un dépôt de texte ; candidates à Git LFS ou à une compression.
- `ai_logs/` : 559 fichiers plats. La trace est une exigence de `CLAUDE.md`, mais sans index généré ni archivage par période, elle devient inexploitable (le script `generate_ai_logs_index.py` existe — son produit n'est pas visible).
- Suite racine vs CI : la CI exécute les tests `mcp-server` via `unittest discover` et les tests racine via les scripts de guard ; localement tout passe, mais l'installation du module échoue silencieusement si l'environnement a des paquets Debian en conflit (constaté avec PyJWT) — un `constraints`/venv documenté dans `mcp-server/README.md` éviterait le faux négatif.

## 4. Appréciation d'ensemble

Le dépôt est **cohérent, honnête sur son propre état, et son unique module de code est propre, testé et fidèle à ses bornes**. Ce sont des qualités réelles et peu communes.

Le risque principal n'est pas l'incohérence, c'est **l'auto-référence** : la majorité de l'énergie visible des dernières semaines (CHANGELOG 0.1.53 → 0.1.60, méta-documents, guards de vocabulaire) est consacrée à gouverner le dépôt qui décrit la gouvernance. Pendant ce temps, l'intégration réelle avec Hermes et OpenWebUI — le point où la doctrine rencontrerait un utilisateur — reste « documented non-implemented ». Le deuxième risque est le **processus** : CI rouge 29/30 sur la journée, commits directs sur `main`, réécriture d'historique, tag de release revendiqué mais absent — autant d'écarts entre la discipline prêchée et la discipline pratiquée.

## 5. Recommandations priorisées

1. **Rendre l'invariant de release vrai** : créer `v0.1.60` (et rétroactivement `v0.1.59` si souhaité) ou corriger l'entrée CHANGELOG 0.1.59. Coût : minutes.
2. **Appliquer la discipline PR à soi-même** : même en solo, passer par des branches + PR pour `main`, avec la CI comme gate de merge (branch protection), au lieu de pousser puis réparer. C'est l'alignement le moins cher entre doctrine et pratique.
3. **Purger les violations latentes** (liens, index, vocabulaire d'axes) puis retirer le mode diff-scopé des guards. — *Fait dans cette même PR : 16 violations traitées, guards passés en full-tree (sauf net-truncation, diff par nature).*
4. **Geler temporairement la production de candidats** : traiter la file (promouvoir, fusionner ou clore les ~65 candidats), réduire les 10 méta-documents à un seul document de réconciliation vivant.
5. **Alléger l'historique** : sortir `legacy/Pantheon-OS-main.zip` et les images lourdes vers une release ou LFS.
6. **Prochain incrément de valeur** : une tranche verticale réellement branchée (le serveur MCP consommé par un Hermes/OpenWebUI réel sur le cas `architecture_devis_reprise`), plutôt qu'un document de plus — c'est le seul test qui validera ou invalidera la doctrine.

---

Méthode : lecture de `CLAUDE.md`, `README.md`, `STATUS.md`, `AUTHORITY_INDEX.md`, `WHAT_RUNS.md`, `MODULES.md` (partiel) ; exécution locale de `pytest tests/` (12 OK), `unittest discover mcp-server/tests` (122 OK) et des 9 scripts `.github/scripts/` en full-tree ; grep de bornes sur `pantheon_mcp` (subprocess/réseau/écriture : néant) ; interrogation de l'API GitHub Actions (30 runs) et de `git ls-remote --tags`.
