# Cartographie d'intégration — Pantheon Next / MCP / MVP — 2026-07-23

Statut : audit externe, validation-only. Cette cartographie ne crée aucune doctrine, n'installe rien et n'approuve rien ; elle constate l'état des trois zones et nomme les manques.

Périmètre observé :

- `ifanjuang/Pantheon-Next` — checkout local, branche `claude/pantheon-repos-audit-s46afb` issue de `main` (`e2ad457`).
- `mcp-server/` — module Python interne à Pantheon Next (c'est le « pantheon-mcp » désigné dans la demande ; **il n'existe pas de dépôt GitHub `pantheon-mcp` distinct** — `list_repos` ne renvoie que `Pantheon-Next` et `pantheon-mvp`).
- `ifanjuang/pantheon-mvp` — checkout local, `main` (`ff7edba`).

Vocabulaire de statut employé (aligné sur `docs/governance/WHAT_RUNS.md`) : **implémenté** · **partiel / à vérifier** · **documenté non-implémenté** · **candidat** · **volontairement absent** · **externe**.

---

## 1. Clarification du périmètre : « trois dépôts » = deux dépôts + un module

La demande parle de trois dépôts. La réalité de l'arborescence et de `list_repos` :

| Nom demandé | Réalité | Rôle doctrinal |
|---|---|---|
| `pantheon-next` | dépôt GitHub `ifanjuang/Pantheon-Next` | noyau de gouvernance (pur, ne dépend de rien) |
| `pantheon-mcp` | **module `mcp-server/` à l'intérieur de Pantheon Next**, seule distribution Python du dépôt | surface de politique / validation en lecture seule ; point de connexion vers Hermes et OpenWebUI |
| `pantheon-mvp` | dépôt GitHub `ifanjuang/pantheon-mvp` | candidat exécutable externe : cockpit + boucle verticale gouvernée |

Conséquence pour l'intégration : la frontière « noyau ↔ MCP » est **interne** (monorepo, dépendance à sens unique) ; la frontière « Next ↔ MVP » est **inter-dépôts** (consommation vendorée, épinglée, report-only).

---

## 2. Vue d'ensemble par zone

| Zone | Nature dominante | Ce qui tourne réellement |
|---|---|---|
| Noyau Pantheon Next | ~97 % documentation + artefacts déclaratifs (doctrine, schémas, templates, fixtures, exemples, logs) | validation structurelle (schémas + tests + guards CI) |
| `mcp-server/` | ~3 % code Python **read-only** | service de politique transport-neutre (stdio MCP + projection HTTP interne), CLIs de vérification |
| `pantheon-mvp` | code exécutable (Python + JS cockpit) | boucle verticale gouvernée end-to-end, en **candidat / non adopté** |

Les trois zones sont **structurellement cohérentes** avec la doctrine affichée (« OpenWebUI expose / Hermes exécute / Pantheon gouverne ») : aucune ne recrée de runtime autonome, de scheduler, de file d'attente, de routeur de providers ou de moteur d'approbation.

---

## 3. Cartographie capacité par capacité

### 3.1 Noyau de gouvernance (Pantheon Next)

| Capacité | Statut | Preuve / emplacement | Manque pour « pleinement fonctionnel » |
|---|---|---|---|
| Doctrine + honnêteté de statut (STATUS / WHAT_RUNS / AUTHORITY_INDEX / MODULES) | **implémenté** | `docs/governance/`, hiérarchie de préséance explicite | — (c'est l'actif le plus mûr) |
| Schémas de validation (capability passport, task contract, evidence pack, APU, proof register, mvp governed loop, work issue slice…) | **implémenté** | `schemas/*.schema.yaml` + exemples valides + tests négatifs | Couverture métier au-delà de l'architecture reste à étendre |
| Guards de cohérence documentaire (en-têtes de statut, couverture d'index, anti-« phrases runtime », intégrité APU…) | **implémenté** | `.github/scripts/`, `.github/workflows/` | — |
| Templates Hermes / OpenWebUI (déclaratifs, sans adaptateur exécutable) | **candidat** | `templates/hermes/`, `templates/openwebui/` | Ce sont des gabarits ; aucun n'est installé côté runtime |
| Profils Hermes (`zeus`, `athena`, `apollo`, `argos`, `hephaistos`, `iris`, `themis` + `_base`) | **candidat** | `hermes/profiles/` avec `allowed_outputs` / `forbidden_outputs` | Templates de profils, pas d'exécution installée |
| Packs métier architecte (base_metier, domain-packs, exemples fictifs) | **partiel / à vérifier** | `base_metier/architecte/`, `docs/domain-packs/` | Méthode cadrée mais ne valide/exécute rien par elle-même |
| Déploiement policy-API (`Dockerfile.policy-api`, `compose.policy-api.yaml`) | **candidat / non activé** | racine du dépôt | Image ≠ installation ; réseau interne durci mais jamais déployé |
| Adaptateur Revit (`revit-plugin/`) | **documenté non-implémenté / squelette** | `revit-plugin/` | Add-in C#/.NET à écrire |
| Trace d'intervention (`ai_logs/`) | **implémenté (trace)** | `ai_logs/<année>/Q<n>/` | — |

### 3.2 Surface de politique / validation (`mcp-server/`)

Toutes les capacités ci-dessous sont **read-only et sans effet de bord** — vérifié dans le code (`pantheon_mcp/` : aucun `subprocess`, aucun accès réseau, aucune écriture). Le service transport-neutre `PantheonPolicyService` (`service.py`) est appelé identiquement par le transport stdio MCP (`server.py`) et par la projection HTTP (`http_api.py`).

| Capacité | Statut | Outil / module |
|---|---|---|
| Carte des sources + résolution d'autorité (exact/groupe/glob, fail-closed en `conflict`) | **implémenté** | `list_sources`, `source_map.py`, `authority_index.py` |
| Lecture de doctrine + wiki de structure | **implémenté** | `read_doctrine`, `explain_governance_structure` |
| Catalogue de consultation honnête (implémenté / partiel / non-implémenté) | **implémenté** | `get_consultation_catalog`, `consultation.py` |
| Explication de placement d'architecture | **implémenté** | `explain_architecture` |
| Qualification d'un statut de capacité **fourni** (axes listed/detected/installed/configured/enabled/reachable/health + gouvernance/usage/update/rollback) | **implémenté (qualification seule)** | `get_capability_status` — ne sonde aucun runtime |
| Validation de capability passport | **implémenté** | `validate_passport`, `passports.py` |
| Classification K0–K4 / V0–V4 / C0–C5 + gates | **implémenté** | `classify_request`, `policy.py` |
| Refus d'action externe (bloqué par défaut + chemin de légitimation) | **implémenté** | `check_external_action` |
| Doctor read-only fail-closed (fichiers obligatoires, langage runtime, règle cascade, instance de registre, tranche verticale, worklist vocabulaire) | **implémenté** | `run_doctor_checks`, `doctor.py` |
| Validation de dossier APU (schémas + posture de gate) | **implémenté** | `validate_apu_dossier`, `apu.py` + CLI |
| Vérifications `verify_*` à partir d'**évidence fournie** : install, observability, backup, exposure, update | **implémenté (verdict comme donnée)** | `install.py`, `observability.py`, `backup.py`, `exposure.py`, `update.py` + CLIs |
| Lecture de preset de vérification → plan | **implémenté** | `load_verification_preset`, `presets.py` |
| Projection HTTP interne authentifiée (classify, preflight, external-action, context-pack, routes legacy compat) | **implémenté (candidat)** | `http_api.py`, `http_middleware.py` |
| Récupération de connaissance privée + service d'identité/permission scopée | **absent** | noté explicitement dans `mcp-server/README.md` |
| Inventaire runtime Hermes / probe live | **volontairement absent** | le MCP ne sonde jamais ; l'inventaire vient du plugin Hermes |

Tests : suite `mcp-server/tests/` étendue (parité cockpit/backup/exposure/observability/update, fail-closed, e2e vertical). À exécuter après `pip install "mcp-server/.[test]"`.

### 3.3 Candidat exécutable (`pantheon-mvp`)

Boucle verticale gouvernée, **implémentée et testée en externe, non adoptée** (`GOVERNANCE_STATUS.md` : gate 8 « approbation humaine » = OPEN).

| Capacité | Statut | Module |
|---|---|---|
| Task Contract validé contre schéma vendoré au chargement | **implémenté (candidat)** | `contract.py` |
| Ingestion bornée + récupération scopée (Block 1) | **implémenté (candidat)** | `store.py`, `documents.py`, `embedder.py` |
| Seam de rédaction + flags consultatifs (Block 2, Drafter injectable) | **implémenté (candidat)** | `runner.py`, `drafting.py` (slot LLM = Drafter côté Hermes, jamais routé ici) |
| Register candidate + rétention B1 (Block 3) | **implémenté (candidat)** | `register.py` |
| Persistance Work Issues | **implémenté (candidat)** | `work_issues.py`, `work_issue_read.py`, `sql/001_work_issues.sql` |
| Extraction Docling + intake NAS incrémental strict | **implémenté (candidat) / à vérifier en réel** | `documents.py`, tests `test_docling_documents`, `test_nas_intake` |
| Publication Knowledge versionnée `generated_unreviewed` + gate UPDATE signé | **implémenté (candidat)** | `knowledge.py`, `knowledge_update.py`, `signer.py` |
| Cockpit cards-first (HTML/CSS/JS) | **implémenté (candidat)** | `mvp_vertical/cockpit/` |
| API cockpit + shell | **implémenté (candidat)** | `cockpit_api.py`, `cockpit_shell.py` |
| Éditeur mobile Markdown offline (PWA) | **implémenté (candidat) / non installé** | `mvp_vertical/mobile_editor/` |
| Prévisualisations proposition-seule : effet, site-manifest, navigation | **implémenté (candidat)** | `effect_preview.py`, `effect_guard.py`, `site_manifest_preview.py`, `site_navigation_profile.py` |
| Profils de ressources | **implémenté (candidat)** | `resource_profiles.py` |
| Stand-in de gate terminal (≠ cockpit OpenWebUI) | **implémenté (stand-in déclaré)** | `terminal_gate_standin.py` |
| Stand-in runner (≠ Hermes Agent) | **implémenté (stand-in déclaré)** | `runner.py` |
| Tool OpenWebUI « Document Cards » read-only | **candidat / non installé** | `openwebui/pantheon_document_cards.py` |
| Identité pgvector / digests décision-récupération | **implémenté (candidat)** | tests `test_pgvector_identity`, `test_decision_record` |

---

## 4. Points de connexion entre les trois projets

```text
                 (vendoring épinglé, sens unique, report-only)
   Pantheon Next  ────────────────────────────────────────────►  pantheon-mvp
   (schemas/)          UPSTREAM_COMMIT + check_schema_drift.py     (vendor/pantheon/)

   Pantheon Next  ◄───── consulte ─────  Hermes Agent  ─────► exécute (hors Pantheon)
   (mcp-server/)      MCP stdio / HTTP        (externe)

   OpenWebUI  ─── expose ───►  cockpit MVP / Document Cards  (candidat, non installé)
```

| # | Connexion | Statut | Artefact concret |
|---|---|---|---|
| C1 | **Next → MVP : schémas vendorés** (seul lien inter-dépôts réellement câblé) | **implémenté** | `mvp_vertical/vendor/pantheon/` : 3 schémas verbatim + 1 vocabulaire dérivé ; épinglé par `UPSTREAM_COMMIT` ; dérive surveillée par `tools/check_schema_drift.py` (workflow `schema-drift.yml`, report-only). Re-vendoring = `tools/revendor.sh`, décision revue. Contrat : `docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md`. |
| C2 | **Hermes → MCP (consultation)** : preflight, classification, préparation de candidats | **documenté non-implémenté** (côté runtime) | Fragment de config `templates/hermes/connection/pantheon_policy_mcp.template.yaml` ; contrat `mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md`. Le serveur existe ; **aucun artefact ne prouve qu'un Hermes vivant le charge**. |
| C3 | **Hermes → MCP (HTTP policy/preflight)** en tant que Policy Enforcement Point | **documenté non-implémenté** | `mcp-server/docs/HTTP_API_CONTRACT.md` (fail-closed) + `templates/hermes/connection/pantheon_policy_http.template.yaml`. L'API renvoie de la donnée ; **rien ne prouve qu'un Hermes appelle et obéit**. |
| C4 | **Plugin dashboard Hermes → MCP** : produit l'inventaire live, le MCP le qualifie via l'enveloppe d'observation | **candidat / inactif ici** | `templates/hermes/dashboard-plugins/pantheon-modules/` (données synthétiques en preview ; pas de backend Pantheon). |
| C5 | **OpenWebUI → cockpit MVP / Document Cards** | **candidat / non installé** | `pantheon-mvp/openwebui/pantheon_document_cards.py`, `cockpit_api.py` ; côté Next, gabarits `templates/openwebui/`. |
| C6 | **Next observe MVP** (réconciliation, pas dépendance) | **implémenté (observation)** | `docs/governance/PANTHEON_MVP_COCKPIT_RECONCILIATION.md` (épingle `pantheon-mvp#44`), `PANTHEON_MVP_VERTICAL_BINDING.md`. Observation seule : Next n'importe ni n'exécute le MVP. |
| C7 | **Délibération multi-modèles (MoA)** Hermes | **documenté non-implémenté / désactivé** | `templates/hermes/connection/pantheon_deliberation_moa.template.yaml`, handoffs délibération. Aucune config installée ni exécutée. |

**Incohérence de synchronisation relevée (C1).** Deux références de commit vendoré divergent :

- `pantheon-mvp/GOVERNANCE_STATUS.md` cite `UPSTREAM_COMMIT 782afb474dec572e63d2c944007e1cf5bab37a09` ;
- le fichier réel `mvp_vertical/vendor/pantheon/UPSTREAM_COMMIT` contient `f8bc3bde142d1e105b7c9a966d8e0d62b39918c4`.

Le texte de gouvernance est **en retard sur le pin réel**. À réconcilier (documentation vers code) lors d'un prochain re-vendoring revu. Ce n'est pas une dérive structurelle de schéma (que `check_schema_drift.py` couvre), mais une dérive documentaire non couverte par le contrôleur.

---

## 5. Éléments manquants pour une plateforme Pantheon pleinement fonctionnelle

Classés par ce qui bloque l'activation end-to-end. Aucun de ces manques n'est un « trou à combler en silence » : plusieurs sont **volontairement absents** par doctrine et resteront externes.

### 5.1 Chaînon d'exécution vivant (le manque central)

- **Liaison Hermes réelle + Policy Enforcement Point actif.** Aujourd'hui le contrat existe (C2/C3) mais **aucun artefact ne prouve qu'un conteneur Hermes appelle le MCP/HTTP et obéit au verdict**. C'est la pièce qui transforme « gouvernance décrite » en « gouvernance appliquée ».
- **Installation OpenWebUI réelle** des functions/tools/pipes (les gabarits de Next et le tool Document Cards du MVP sont des candidats non installés).

### 5.2 Couche de déploiement (absente des deux dépôts publics)

- **Dépôt/couche de déploiement privé** : révisions épinglées, Compose/Portainer, reverse-proxy, montages de stockage, backup/health/rollback, références de secrets. `NEXT_MVP_REPOSITORY_PLACEMENT.md` la décrit ; elle **n'existe pas encore**. `Dockerfile.policy-api` + `compose.policy-api.yaml` en sont un candidat non activé.
- **Aucun tag/release Git** sur les remotes : les checkpoints de changelog ne sont pas des releases publiées.

### 5.3 Services de plateforme non encore présents

- **Backend mémoire / Registre Probatoire persistant** (Mem0/Memvid ou équivalent gouverné) : la promotion mémoire est **volontairement absente** du noyau ; il manque le backend externe gouverné qui la porterait sous gate humain.
- **Service d'identité / permission / scope** : noté « absent » dans `mcp-server/README.md`. Sans lui, l'enforcement scopé par utilisateur/projet n'est pas réalisable.
- **Accès aux sources privées / récupération de connaissance privée** : absent du MCP (le MVP le simule via stand-ins et fixtures fictives).
- **Déploiement réel Docling / pgvector / intake NAS** : le code MVP existe et passe ses tests, mais sur stand-ins et corpus fictifs — pas de preuve d'un déploiement live.

### 5.4 Décisions de gouvernance encore ouvertes

- **Gate 8 (approbation humaine d'activation du MVP)** : OPEN. Les gates 1–7 ont une évidence *candidate*, pas une adoption.
- **Réconciliation du pin vendoré** (§4) : dérive documentaire à corriger.
- **Extension des packs métier** au-delà de l'architecture, si la plateforme vise d'autres domaines.

### 5.5 Volontairement absents (à ne pas « compléter » sans décision de doctrine)

`WHAT_RUNS.md` les liste : runtime d'exécution interne Pantheon, boucle d'agent cachée, moteur d'approbation autonome, promotion mémoire automatique, scheduler, file d'attente, routeur de providers, marketplace de plugins, envoyeur externe automatique, gateway de connecteurs non restreint, ERP, runtime de plateforme de données de production. Toute proposition les réintroduisant doit être classée conflit de doctrine ou adaptateur/runtime explicitement externe.

---

## 6. Synthèse

- **Le noyau de gouvernance et le module MCP sont solides et tiennent leurs bornes** (read-only vérifié dans le code, honnêteté de statut structurée, guards CI inhabituellement soignés).
- **Le candidat MVP prouve la « cage » de gouvernance end-to-end** en externe, mais reste candidat / non adopté par choix (gate humain ouvert).
- **Un seul lien inter-dépôts est réellement câblé** : le vendoring épinglé des schémas Next → MVP, avec surveillance de dérive report-only (une petite dérive documentaire de pin à corriger).
- **Ce qui manque pour une plateforme pleinement fonctionnelle est essentiellement l'exécution vivante et sa couche de déploiement** : une liaison Hermes réelle qui applique le verdict de politique, une installation OpenWebUI réelle, une couche de déploiement privée, et les services de plateforme externes (mémoire gouvernée, identité/scope, sources privées) — le tout sous décision humaine explicite.

La plateforme est aujourd'hui **une gouvernance complète et vérifiable, en attente de son runtime d'exécution gouverné et de sa couche de déploiement**. C'est cohérent avec la doctrine : Pantheon gouverne, il ne devient pas le runtime.
