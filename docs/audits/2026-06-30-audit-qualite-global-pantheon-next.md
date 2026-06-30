# Audit qualité global — Pantheon Next

Status: validation-only / audit trace — to verify. Lecture critique transversale du dépôt (gouvernance, code, schémas, docs MD/HTML, frontières doctrinales). Enregistre une position et des recommandations ; ne promeut rien, ne décide rien, n'altère aucune doctrine.

Date : 2026-06-30
Périmètre : `CLAUDE.md`, `docs/governance/` (177 MD), `mcp-server/`, `schemas/`, `tests/`, `.github/`, `templates/`, `examples/` + `docs/examples/`, `hermes/`, `base_metier/`, `legacy/`, `ai_logs/`, `docs/assets/` (HTML/JS).

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

---

## Synthèse exécutive

Le dépôt est **doctrinalement très propre dans son code** (aucun outil n'exécute, n'écrit ni ne sonde ; tout reste candidat) mais a accumulé une **dette documentaire** et une **dérive de frontière silencieuse**. La thèse centrale de cet audit :

> Pantheon est un projet **spécification-lourd / implémentation-légère** (≈ 20:1). La couche qui doit gouverner la complexité du runtime reproduit, en prose, la dérive de complexité qu'elle interdit au code — sans contrepoids exécutif qui la force à rester minimale.

Deux décisions structurantes restent à trancher par le mainteneur : **(a)** la frontière `dashboard/`, **(b)** le devenir de `base_metier/architecte/`. Une troisième, plus profonde, conditionne la trajectoire : **doctrine pure vs preuve par une tranche verticale exécutable**.

---

## 1. Cartographie

| Zone | Volume | Statut déclaré | Observation |
|---|---|---|---|
| Racine | 6 fichiers + dossiers | gouvernance | `VERSION=0.1.0` ≠ `CHANGELOG 0.1.57` |
| `docs/governance/` | **177 MD** (165 avec `Status:`) | 60 candidate, 26 documented-non-implemented, **17 obsolete** | Forte densité |
| `docs/assets/` | 18 Mo, 29 HTML | « visual support » | Contient un **prototype de cockpit** (proto JS, 56 fichiers) |
| `mcp-server/` | 14 tools, 24 tests | implementation candidate | Sain — mais excède la frontière déclarée |
| `schemas/` | 28 YAML + examples | initial schema baseline | Cohérent, double suite de tests |
| `hermes/profiles/` | 7 profils | candidate_only_template | OK |
| `base_metier/architecte/` | 42 fichiers, **2 scripts Python**, PDF | non indexé | **Hors doctrine** + risque licence |
| `legacy/` | **1,2 Mo binaire** (`.zip`) | historical reference | Pollution du tree |
| `examples/architecture/` | 3 cas | illustrative | **Doublonne `docs/examples/`** (18 cas) |
| `ai_logs/` | **481 fichiers**, 2,0 Mo | validation-only / trace | Aucune consolidation |
| `.github/` | 1 workflow, 8 scripts | actif | Liste obligatoire désync. du doctor |

---

## 2. Lecture à trois altitudes

### 2.1 Vue d'architecte dev
- **La doctrine grossit plus vite que son référent.** Coût marginal d'une idée ≈ 4-5 artefacts (MD + AUTHORITY_INDEX + MODULES + ai_log + schéma) à garder cohérents. Le chokepoint gouverne les effets runtime, **pas** la prolifération documentaire : c'est l'angle mort.
- **La pureté « governs, does not execute » est force et piège.** Le dépôt seul ne fait rien d'observable ; toute la valeur dépend de Hermes + OpenWebUI, absents du repo. Arbitre sans terrain.
- **Le `dashboard/` fantôme est un symptôme.** Module promis par `CLAUDE.md`, inexistant ; ses fonctions ont migré dans `mcp-server/` (6 `verify_*`) et `docs/assets/pantheon-control/` (proto JS). La doctrine décrit une architecture-cible que l'implémentation ne suit pas.

### 2.2 Vue d'utilisateur professionnel
- Le README est l'**excellent** artefact du repo — mais il **sur-signale** une maturité produit inexistante. Aucun chemin d'installation utilisable ; le cockpit est une maquette à données fictives ; `STATUS.md` dit honnêtement « partial ».
- Ironie : un projet dont la thèse est « réponse fluide ≠ réponse vraie » présente une **doc fluide qui sur-promet**.
- Ce qui rendrait le produit *réel* pour le pro (corpus métier, ingestion) est précisément la zone la plus hors-doctrine (`base_metier/`).

### 2.3 Vue de Pantheon lui-même
- **Fidèle dans le code**, infidèle à son esprit dans sa propre gestion :
  - `MODULES.md` dit « doit rester plus simple que le runtime qu'il gouverne » — invérifiable, probablement faux en volume cognitif.
  - Interdit la « auto-promoted memory », mais 60 candidats non datés traînent : **canonisation par fatigue**.
  - Distingue bien implémenté/documenté/partiel/obsolète **par doc**, jamais **au niveau système** : il manque la carte d'honnêteté globale.
- Question de fond : la gouvernance est-elle un *moyen* (protéger un produit) ou est-elle devenue la *fin* (produire de la doctrine élégante) ? La trajectoire penche vers la fin.

---

## 3. Problèmes & incohérences (priorisés)

### Bloquants (doctrine ↔ code)
1. **`dashboard/` promis, inexistant** ; fonctions absorbées par `mcp-server/` (`verify_install/observability/backup/exposure/update`, `load_verification_preset`) et `docs/assets/pantheon-control/`. La séparation déclarée n'est plus vraie.
2. **`base_metier/architecte/` exécutable et non indexé** : `skills/pdf_to_md/convert_pdf_to_md.py`, `skills/ingest_local_folder/ingest.py` ; absent d'`AUTHORITY_INDEX`/`MODULES` ; PDF de provenance non auditée (CCAG, MAF, Code construction) → **risque licence**.
3. **`legacy/Pantheon-OS-main.zip` (1,2 Mo)** versionné sans nécessité.

### Incohérences documentaires
4. **6 stubs obsolètes encore référencés** depuis les points d'entrée publics : `README.md:250`, `docs/governance/README.md:53,86,196` (famille `EVIDENCE_TOPOLOGY_*`).
5. **17 docs `obsolete`** dans `docs/governance/` (dont `EPISTEMIC_CONTROL`, `MODEL_ROUTING_POLICY`, `ROUTING_FOUNDATION`, `MEMORY_EVENT_SCHEMA`, `OPENWEBUI_PLUGIN_POLICY`…).
6. **`ROADMAP.md` (l. 373-382)** cite comme objectifs des stubs rétrogradés par `AUTHORITY_INDEX.md` (règle « index wins » → roadmap incohérente).
7. **`STATUS.md` stagnant** : daté 2026-06-20, posture « controlled bootstrap » inchangée depuis ≈ 7 semaines.
8. **Versionnement** : `VERSION=0.1.0` vs `CHANGELOG 0.1.57`, sans tags.
9. **Liste « fichiers obligatoires » désync.** : CI exige 25 fichiers, `doctor.py` 15, alors qu'il prétend « mirror the CI ».
10. **Regex `NEGATION` trop permissif** (`\bno\b` désamorce le garde anti-runtime → faux négatifs).
11. **Familles documentaires concurrentes** sans carte maîtresse (carte/deck, registre/mémoire/preuve, rôle/réflexe).
12. **`base_metier`/`examples` doublés** ; `EVIDENCE_TOPOLOGY.md` à 1957 l ; 3 docs « Pantheon Control » non hiérarchisés.
13. **Dépendance implicite** : `apu.py` importe `referencing`, absent de `mcp-server/pyproject.toml`.
14. **Bilinguisme asymétrique** : gouvernance EN, surfaces FR, vocabulaire hybride ; README EN/FR déphasés (368 vs 383 l).

### Ce qui fonctionne (à préserver)
- Invariant gouvernance ≠ exécution **tenu dans le code**.
- Triade schemas/examples/tests.
- CI doctrinale (phrases interdites + NEGATION) — rare et précieux.
- Autorité hiérarchique lisible ; `AUTHORITY_INDEX` arbitre les divergences.

---

## 4. Préconisations

Notation : **Effort** S(<½j)/M(1-3j)/L(>3j) · **Impact** ○ faible / ◐ moyen / ● fort

### P1 — Contrepoids à la doctrine
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 1.1 | **Règle du référent** : `candidate → active` exige un consommateur exécutable (schéma+test+appel mcp-server) **ou** un exemple end-to-end. Inscrire dans `AUTHORITY_INDEX.md`. | S | ● |
| 1.2 | **Budget de complexité** : plafond de docs `candidate` ouverts ; au-delà, fermer/fusionner avant d'ajouter. | S | ◐ |
| 1.3 | **`Created:` obligatoire** sur tout candidat + péremption (>90j → arbitrage). | M | ● |
| 1.4 | **`WHAT_RUNS.md`** : une page, deux colonnes « tourne réellement » / « promesse ». | S | ● |

### P2 — Aligner les frontières de modules
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 2.1 | Trancher B-1, puis **mettre `CLAUDE.md` en accord**. | S | ● |
| 2.2 | Reclasser `docs/assets/pantheon-control/` (prototype de module, pas asset). | M | ◐ |
| 2.3 | Indexer **toutes** les zones dans `AUTHORITY_INDEX.md`. | S | ◐ |

### P3 — Prouver la boucle (tranche verticale)
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 3.1 | Faire tourner `architecture_devis_reprise` de bout en bout (OpenWebUI → Hermes → mcp-server → Evidence Pack → gate). | L | ● |
| 3.2 | Runbook reproductible dans `operations/`. | M | ● |
| 3.3 | Sortie réelle capturée en **fixture de test**. | M | ◐ |

### P4 — `base_metier/architecte/`
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 4.1 | Décider B-2 + **audit licence** des PDF. | M | ● |
| 4.2 | Sortir les binaires du Git (`.gitignore` + manifestes reconstructibles). | S | ◐ |
| 4.3 | Si conservé : scripts Python déplacés côté `hermes/`. | M | ◐ |

### P5 — Hygiène documentaire
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 5.1 | Corriger liens vers 6 stubs obsolètes (`README.md:250`, `docs/governance/README.md:53,86,196`). | S | ◐ |
| 5.2 | Archiver les 17 docs `obsolete` sous `docs/governance/_archive/`. | S | ◐ |
| 5.3 | Réaligner `ROADMAP.md` (l. 373-382) sur `AUTHORITY_INDEX.md`. | S | ◐ |
| 5.4 | Mettre `STATUS.md` à jour + revue datée récurrente. | S | ◐ |
| 5.5 | Carte maîtresse dans `CORE_CONCEPTS_MAP.md` (doc maître/déclinaisons/obsolètes par famille). | M | ● |
| 5.6 | Découper `EVIDENCE_TOPOLOGY.md` (1957 l) + sommaire. | M | ◐ |
| 5.7 | Hiérarchiser les 3 docs « Pantheon Control ». | S | ○ |

### P6 — Hygiène code / CI
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 6.1 | **Liste unique** de fichiers obligatoires (YAML) consommée par CI + `doctor.py`. | M | ◐ |
| 6.2 | Resserrer le regex `NEGATION` (contraindre `\bno\b`). | S | ◐ |
| 6.3 | Déclarer `referencing>=0.30` dans `mcp-server/pyproject.toml`. | S | ○ |
| 6.4 | Trancher `VERSION` (B-7). | S | ○ |
| 6.5 | Retirer `legacy/Pantheon-OS-main.zip` du tree. | S | ◐ |
| 6.6 | `ai_logs/INDEX.md` généré + archivage trimestriel. | M | ○ |

### P7 — Crédibilité produit
| # | Préconisation | Effort | Impact |
|---|---|---|---|
| 7.1 | Bandeau d'état franc en tête de README (« méthode + maquettes ; pas encore installable »). | S | ● |
| 7.2 | Index HTML **EN** miroir de `docs/index.html`. | M | ○ |
| 7.3 | Politique linguistique formelle dans `EDITORIAL_LANGUAGE.md`. | S | ○ |

---

## 5. Arbitrages (décisions du mainteneur) — avec recommandation

### B-1 · Frontière `dashboard/` vs `mcp-server/`
- (A) Créer un vrai module `dashboard/` (fidèle, mais double la maintenance).
- (B) Fusionner dans `mcp-server/` (« policy + verification surface ») + réécrire `CLAUDE.md` (économe, reflète le réel).
- (C) Statu quo + note transitoire.

→ **Reco : (B) court terme, (A) à terme.** Les `verify_*` sont read-only et n'exigent pas un module séparé : reconnais-le dans `CLAUDE.md`. Garde (A) comme cible quand le dashboard aura un vrai front. Ne crée pas un module vide pour respecter une frontière de papier.

### B-2 · Sort de `base_metier/architecte/`
- (A) Extraire dans un dépôt séparé côté Hermes.
- (B) Garder + indexer, scripts déplacés côté `hermes/`.
- (C) Supprimer.

→ **Reco : (A), précédé d'un audit licence immédiat.** C'est la zone que la doctrine pousse hors de Pantheon **et** celle qui porte le risque juridique. La sortir résout les deux. À défaut de bande passante : (B) transitoire, mais indexer et dé-versionner les binaires sans attendre.

### B-3 · Doctrine pure vs preuve exécutable (arbitrage majeur)
- (A) Rester un layer de gouvernance pur.
- (B) Livrer une tranche verticale exécutable sans renier la doctrine (Pantheon reste PDP).
- (C) Pivoter vers un produit intégré.

→ **Reco : (B), franchement.** La doctrine n'a de valeur qu'en gouvernant quelque chose qui tourne. Une boucle réelle réancre les 177 docs. (A) mène au monument documentaire ; (C) jette le différenciateur ; (B) garde l'intégrité **et** crée la preuve.

### B-4 · Domaine architecture : monorepo vs extraction
- (A) `docs/domain-packs/architecture/` (déplacer les 28 `ARCHITECTURE_*`).
- (B) Dépôt séparé.
- (C) Statu quo.

→ **Reco : (A) maintenant, (B) au 2ᵉ domaine.** Un sous-dossier donne le signal cœur ≠ pack sans la lourdeur multi-repo. Réévaluer à l'apparition d'un domaine juridique/médical.

### B-5 · Volume doctrinal : geler/élaguer vs continuer
- (A) Gel + élagage (moratoire).
- (B) Continuer au rythme actuel.
- (C) Élagage ciblé sans gel.

→ **Reco : (C), disciplinée par la règle du référent (1.1).** Un gel total est irréaliste ; le rythme actuel mène au monument. (C) + référent = la doctrine ne grandit que là où elle s'arrime à de l'exécutable.

### B-6 · Bilinguisme
- (A) Tout EN, surfaces FR.
- (B) Bilingue intégral (déphasage garanti).
- (C) Cible-driven : gouvernance EN, surfaces pro FR, glossaire bilingue unique.

→ **Reco : (C).** Ne pas tout dédoubler. Concentrer l'effort bilingue sur les surfaces que le pro voit (README, landing, cockpit), pas sur 177 docs internes.

### B-7 · `VERSION` vs `CHANGELOG`
- (A) Synchroniser `VERSION` au CHANGELOG + tags.
- (B) Supprimer `VERSION`, CHANGELOG fait foi.

→ **Reco : (A), avec tag automatisé.** Le doctor exige déjà `VERSION` ; en faire une vérité tenue (tag = version = tête du CHANGELOG) restaure un repère de maturité honnête à coût quasi nul.

### B-8 · `ai_logs/` (481 fichiers)
- (A) Tout garder à plat.
- (B) Archiver par trimestre + INDEX généré.
- (C) Élaguer.

→ **Reco : (B).** Préserver la traçabilité (force de Pantheon), restaurer la lisibilité.

---

## 6. Ordre d'attaque conseillé

1. **Trancher B-1, B-2, B-3** — les trois bifurcations structurantes ; tout en découle.
2. **Quick wins hygiène** : P5.1-5.4, P6.2-6.5, P7.1 (≈ ½ journée, fort gain de cohérence).
3. **P1** (règle du référent + `WHAT_RUNS.md`) — le garde-fou anti-dérive.
4. **P3** (tranche verticale) — le chantier qui change la nature du projet.

---

## Boundary note

Document d'audit. Il enregistre une lecture critique et des recommandations ; il ne crée aucune doctrine, ne promeut aucun candidat, ne modifie ni `schemas/`, ni `tests/`, ni `mcp-server/`, ni aucun chemin protégé. Toute préconisation ci-dessus reste un **candidat** soumis à revue humaine et à la User Decision Gate. La gouvernance décide ; l'humain décide.
