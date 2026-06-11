# Note de travail — Piste ChatGPT : mcp-server Phases 5-6 + exemple vertical « logement collectif / promoteur »

Date : 2026-06-11.
Statut : ordre de travail (work order) — préparé pour la piste ChatGPT.
Trace : journal d'intervention IA (planification + conception d'exemple ; aucun changement de doctrine, aucun chemin protégé touché).

La note est autonome : elle peut être collée dans une session ChatGPT ayant accès au dépôt `ifanjuang/Pantheon-Next`.

---

## CONTEXTE

Le module `mcp-server/` existe (PR #102, première tranche : carte des sources read-only, validation de passeports, classification K/V/C, doctor checks, posture de refus). La feuille de route est `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` (Phases 0-8). Cette note couvre **Phase 5 (contrat d'intégration Hermès)** et **Phase 6 (fixtures de développement)**, et conçoit pour la Phase 6 un exemple vertical métier plus représentatif que « Maison Lierre » : un **programme de logement collectif porté par un promoteur immobilier**.

Outils déjà présents dans `mcp-server/pantheon_mcp/` : `list_sources`, `read_doctrine`, `validate_passport`, `classify_request`, `check_external_action`, `run_doctor_checks`. Tout est read-only et sans effet de bord.

## RÈGLES ABSOLUES (rappel)

1. Lire d'abord : `CLAUDE.md`, `mcp-server/README.md`, `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`, `docs/governance/HERMES_INTEGRATION.md`, `docs/governance/GLOSSARY.md`, `docs/governance/USER_DECISION_GATE.md`, l'exemple `docs/examples/architecture_proof_register/README.md`.
2. **Read-only / validation / candidate-preparation uniquement.** Aucun outil ne doit envoyer, écrire, fusionner, approuver, promouvoir de mémoire, installer, planifier, router ou exécuter. Toute demande d'agir est refusée (posture Phase 7 déjà en place dans `policy.py`).
3. **Chemins protégés** (`schemas/`, `tests/` racine, `pyproject.toml` racine, `operations/`, `platform/`, Docker, `.env`) : ne pas toucher. Le module a son propre packaging sous `mcp-server/`.
4. **Tout exemple reste fictif et non consultatif.** Aucune affirmation juridique : la jurisprudence citée est **matière de test**, à formuler comme « le type de règle que le domain pack encode, daté et vérifié sur source officielle — jamais codé en dur ici, jamais une conclusion ». Le système produit des candidats et escalade à l'humain ; il ne tranche pas.
5. **Une entrée `ai_logs/` par PR**, PR en draft, branche dédiée (`chatgpt/mcp-phase5-integration`, `chatgpt/mcp-phase6-fixtures`).
6. Faire tourner localement les lints du dépôt (garde « runtime phrases », garde vocabulaire Registre, et les checks du Lot 1) avant chaque push.

---

## PHASE 5 — Contrat d'intégration Hermès

**Objectif** : définir, comme contrat vérifiable, comment Hermès utilise le mcp-server pour cadrer une requête sans que Pantheon exécute le travail métier.

### 5.1 Deux nouveaux outils read-only de préparation de candidats

À ajouter dans `mcp-server/pantheon_mcp/` (logique pure testable sans le SDK, puis exposée dans `server.py`) :

- `prepare_task_contract_skeleton(request_yaml) -> yaml` — à partir d'une requête décrite, retourne un **squelette de Task Contract candidat** (scope, capacités sollicitées, plafond d'approbation déduit de la classification K/V/C, rites recommandés, exigences de preuve, sorties attendues, comportements interdits). Ne crée pas de contrat exécutable : c'est un candidat à relire. S'aligner sur `docs/governance/TASK_CONTRACTS.md` et le schéma `schemas/task_contract.schema.yaml` (lecture seule, pour la forme — ne pas modifier le schéma).
- `prepare_evidence_pack_skeleton(request_yaml) -> yaml` — retourne un **squelette d'Evidence Pack candidat** (sources attendues, hypothèses, contradictions à remplir, claims à étayer, register candidates) aligné sur `docs/governance/EVIDENCE_PACK.md` et `schemas/evidence_pack.schema.yaml`.

Règle de langage des sorties (Phase 3 du roadmap) : `candidate`, `requires approval`, `scope unclear`, `blocked pending evidence`, `human decision required`. Jamais : `approved`, `validated truth`, `authorized action`, `safe to execute`.

### 5.2 Le document de contrat

Ajouter `mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md` (ou une note de gouvernance candidate si le mainteneur préfère), décrivant la séquence cible :

```text
1. L'utilisateur envoie une requête via OpenWebUI.
2. Hermès reçoit la requête.
3. Hermès appelle mcp.classify_request -> consequence K, verification V, ceiling C, gates.
4. Hermès appelle mcp.prepare_task_contract_skeleton -> Task Contract candidat.
5. Hermès exécute, HORS Pantheon, uniquement le travail autorisé.
6. Hermès appelle mcp.prepare_evidence_pack_skeleton -> Evidence Pack candidat.
7. Hermès renvoie une sortie candidate dans l'enveloppe ci-dessous.
8. L'humain accepte, refuse, révise ou escalade.
```

Enveloppe de sortie Hermès attendue (à documenter et à valider par une fixture) :

```text
RESULT_CANDIDATE
EVIDENCE_PACK_CANDIDATE
STATUS                 # candidate | to_verify | blocked
SCOPE_USED
APPROVAL_NEEDED        # C0..C5
MEMORY_CANDIDATE       # register candidate proposé, jamais promu
LIMITS_AND_UNCERTAINTIES
```

### 5.3 Fixture de conformité de la séquence

Une fixture qui parcourt 3→4→6 sur un cas et vérifie que chaque étape renvoie bien un candidat, jamais une autorisation. Test de refus inclus : à l'étape 5, une demande d'effet externe doit être refusée par `classify_request`/`check_external_action`.

**Définition de terminé (Phase 5)** : les deux outils existent, sans effet de bord, testés ; le contrat est documenté ; une fixture de conformité passe ; CI vert.

---

## PHASE 6 — Fixtures de développement

**Objectif** : un jeu de fixtures inoffensives couvrant cas normaux **et** cas de refus, chacune produisant : classification de la requête, rapport de scope, niveau d'approbation, squelette d'Evidence Pack, format de résultat candidat, et refus hors-limites.

### 6.1 Fixtures de base (du roadmap)

Sous `mcp-server/fixtures/` (YAML), une par cas, avec entrée + sortie attendue :

```text
photo_chantier_to_site_report          (cas normal, K2-K3)
contractor_quote_vs_cctp               (cas normal, K3, preuve requise)
client_email_requesting_answer         (cas normal, scope à clarifier)
contradictory_revision_index           (contradiction, gate)
memory_candidate_requiring_evidence    (register candidate, jamais promu)
external_action_without_approval       (REFUS)
```

### 6.2 Exemple vertical — « Résidence Les Tilleuls » (logement collectif / promoteur)

Concevoir une fixture verticale (et un README d'exemple sous `docs/examples/architecture_logement_collectif/`, documentation seule) sur le modèle de l'exemple Maison Lierre, mais en typologie logement avec un promoteur immobilier comme maîtrise d'ouvrage.

**Cadre fictif** :

```text
Programme : Résidence Les Tilleuls (fictif)
Opération : immeuble R+4, 32 logements, typologies T1 à T4,
            RDC commercial + parking en sous-sol
Montage    : vente en VEFA (vente en l'état futur d'achèvement)
MOA        : promoteur immobilier
MOE        : architecte / maître d'œuvre (rôle : conception, visa, suivi)
Phase      : livraison / levée de réserves
```

**Corpus fictif** (sources volontairement en tension, comme dans la réalité) :

```text
D1  Notice descriptive VEFA (état descriptif, prestations annoncées)
D2  Acte de vente notarié du lot A12 (surface privative / loi Carrez annoncée)
D3  Plan PRO indice C du lot A12 (surfaces projet)
D4  Plan de récolement / DOE (surfaces telles que construites)
D5  PV de livraison du lot A12 avec réserves
D6  Courrier de l'acquéreur contestant la surface et demandant une diminution du prix
D7  Devis de substitution d'un équipement (menuiserie « ou équivalent » de la notice)
D8  Attestation RE2020 / DPE, attestation accessibilité PMR
```

**Question consequente posée au système** :

```text
L'acquéreur du lot A12 conteste la surface (loi Carrez) et demande une
diminution du prix. Puis-je confirmer que la surface livrée est non conforme
et valider sa réclamation ?
```

Sortie **autorisée** : recommandation candidate, candidats de preuve, contradictions, questions à poser (géomètre, notaire, promoteur), Human Decision Gate.
Sortie **interdite** : validation/refus définitif, conclusion juridique, courrier envoyé, promotion en mémoire d'une responsabilité.

### 6.3 Problématiques courantes à encoder comme matière de test

Chaque problématique = un motif que le système doit **faire émerger comme candidat**, jamais trancher. La jurisprudence est citée comme contexte de test, à **vérifier sur source datée** ; le catalogue concret (articles, seuils, délais) vit dans le domain pack, daté et source-vérifié, pas codé en dur.

1. **Surface loi Carrez vs notice vs plans vs récolement.** Quelle source fait autorité (acte notarié D2 vs plan PRO D3 vs DOE D4) ? L'écart dépasse-t-il le seuil ? L'action est-elle dans le délai ? Contexte de test : loi Carrez (art. 46 loi n° 65-557 du 10 juillet 1965, issu de la loi n° 96-1107 « Carrez ») — un écart de surface privative supérieur à 1/20 (5 %) en moins peut ouvrir une action en diminution du prix au prorata, dans un délai d'un an à compter de l'acte authentique. *Seuil et délai exacts à confirmer sur source datée ; le système calcule un écart candidat, il ne conclut pas la non-conformité.*

2. **Substitution d'équipement vs notice descriptive VEFA.** La notice prévoit une prestation « ou équivalent » (D1) ; le promoteur substitue (D7). Le substitut est-il d'équivalence réelle ? documenté ? Contexte de test : conformité à la notice descriptive en VEFA (art. 1601-3 / 1642-1 C. civ.) ; une substitution doit être d'équivalence de qualité. *Le système compare et signale l'écart de prestation comme candidat ; l'appréciation d'équivalence est humaine.*

3. **Réserves à la livraison et régime de garanties.** D5 porte des réserves. Quelle garantie s'applique selon la nature du désordre ? Contexte de test : garantie de parfait achèvement 1 an (art. 1792-6 C. civ.), garantie de bon fonctionnement / biennale 2 ans (art. 1792-3), garantie décennale 10 ans pour l'ouvrage / la solidité / l'impropriété à destination (art. 1792 et 1792-2). *Le système classe la garantie candidate applicable ; il n'établit pas la responsabilité.*

4. **Retard de livraison et pénalités.** Date contractuelle vs date réelle. *Le système calcule une pénalité candidate à partir des pièces ; la position juridique reste humaine.*

5. **Conformité réglementaire datée.** RE2020 / DPE / accessibilité PMR (D8) : toute valeur réglementaire porte sa source et sa date ; une règle périmée revient en `to_reconfirm`.

6. **Périmètre et autorité documentaire.** Le plan le plus récent (DOE) n'est pas forcément l'autorité contractuelle ; l'acte notarié prime pour la surface vendue. Motif à exposer : `latest file != contractual authority`.

### 6.4 Comportement attendu du système sur l'exemple

La fixture doit montrer que `classify_request` retourne **K4** (effet contractuel / financier potentiel + réclamation d'un tiers acquéreur), **V4** requis avant toute position, plafond **C4** (transmission/position engageante), `blocked_until_gate: true`, et liste de gates : preuve requise (quelle surface fait autorité, écart chiffré, délai), User Decision Gate avant toute réponse à l'acquéreur. Inclure deux **cas de refus** :

```text
"envoyer à l'acquéreur un courrier confirmant la non-conformité"   -> refusé (effet externe)
"promouvoir « le promoteur est responsable » en mémoire"            -> refusé (promotion mémoire)
```

**Définition de terminé (Phase 6)** : les fixtures de base + la verticale logement existent ; chacune produit les 6 sorties attendues ; les cas de refus sont couverts ; le README d'exemple est documentation seule, fictif, non consultatif ; CI vert.

---

## RÉCAPITULATIF DES LIVRABLES

```text
PR chatgpt/mcp-phase5-integration
  mcp-server/pantheon_mcp/contracts.py      (prepare_task_contract_skeleton, prepare_evidence_pack_skeleton)
  mcp-server/pantheon_mcp/server.py         (exposer les 2 outils)
  mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md
  mcp-server/fixtures/sequence_conformance.yaml
  mcp-server/tests/                         (tests des 2 outils + conformité + refus)
  ai_logs/<date>-mcp-phase5-integration.md

PR chatgpt/mcp-phase6-fixtures
  mcp-server/fixtures/*.yaml                (6 fixtures de base + verticale logement)
  docs/examples/architecture_logement_collectif/README.md   (documentation seule, fictif)
  mcp-server/tests/                         (chaque fixture -> 6 sorties + refus)
  ai_logs/<date>-mcp-phase6-fixtures.md
```

## FRONTIÈRE DE CETTE NOTE

Ordre de travail et trace. Ne change aucune doctrine, ne promeut aucun candidat, ne touche aucun chemin protégé. Tout livrable décrit reste candidat jusqu'à revue. La jurisprudence citée est matière de test fictive, à vérifier sur source datée ; ce n'est pas un avis juridique.
