# Codex integration — coherence review and merge order — 2026-07-25

Statut : audit externe, validation-only. Constat de cohérence des PR Codex en vol et ordre de merge sûr. N'installe rien, n'approuve rien, ne modifie aucune PR Codex.

Périmètre : les PR `agent/*` (ChatGPT Codex) ouvertes sur `ifanjuang/Pantheon-Next` et `ifanjuang/pantheon-mvp` au 2026-07-25, confrontées au tronc commun (chokepoint effet-centré + gate-validation) mergé plus tôt.

## 1. Ce que Codex construit — deux programmes

### Programme 1 — Runtime documentaire Paperless + intake Hermès (pile)
```
Next #467 (Paperless = Capability Slot doc-source)      → mvp #56 (adapter + Source Capture + Document→Knowledge)
   ↓ #468 (Paperless dans la baseline d'install)        → mvp #56
   ↓ #469 (skill Hermès pantheon-document-intake + PEP) → mvp #59  (durcissement PEP/PDP)
   ↓ #470 (carte statut runtime read-only)              → mvp #61
   ↓ #471 (observations live sourcées + acceptance)     → mvp #62
```

### Programme 2 — Cockpit V2 + Agency Data + pont d'admission Hermès
```
Next #472  → mvp #65
- Cockpit V2 : navigation Pantheon / Décisions / Affaires / Connaissances / Outils
- Agency Data : PostgreSQL system of record (Project / Person / Organization / ProjectParticipation)
- Pont d'admission Hermès : Work Issue → admission bornée (read_only, ttl, version WI) → pull → callbacks start/return
```

## 2. Revue de cohérence — vérifiée par merge d'essai + tests (pas seulement lue)

| PR | Merge d'essai sur `main` | Suite | Verdict |
|---|---|---|---|
| mvp #59 (durcissement PEP) | **0 conflit** | **254 passed, 0 échec** | cohérent avec le chokepoint mergé |
| mvp #65 (Cockpit V2 + admission) | **0 conflit** | — | pas de queue/scheduler (assertions d'absence vérifiées) |

Constats :

- **#59 durcit correctement `enforce_consequential`** : préflight normalisé `request + gate_signals` (nouveau `policy_request.py`), application des flags V0 (`external_effect_allowed` / `canonical_effect_allowed`), `decision_expectation` **PEP-owned** (le caller ne peut plus fabriquer une fausse décision + fausse expectation). Rétro-compatibilité explicite avec les sites d'appel antérieurs.
- **#65 respecte la frontière** : `Pantheon n'a rien dispatché`, expiration à la demande, pull par ID, callbacks — aucune primitive `claim-next-job` / lease / scheduler / retry-worker.
- Les deux **construisent sur le chokepoint** sans le contredire.

**Conclusion : travail Codex de haute qualité, cohérent. Aucun conflit d'architecture.**

## 3. Deux modèles Hermès — composés, pas concurrents

Réconciliés dans `docs/governance/HERMES_INTEGRATION_MODELS_RECONCILIATION.md` :

```text
Execution Admission (#472/#65) = permission bornée de DÉMARRER un run
Chokepoint (effet-centré + PEP #59) = gate PAR effet PENDANT le run
admission accordée != effet autorisé ; read_only admission ⇒ effets conséquents refusés
```

## 4. Chaînon d'assurance — fermé

Le gap `validated fields != authenticated human issuer`, laissé OPEN par toutes les PR Codex et déféré au PDP, est fermé :

- **PDP (Next)** : `gate_validation` authentifie l'émetteur via signature HMAC contre un registre de clés (`PANTHEON_DECISION_ISSUER_KEYS_PATH`).
- **Producteur (mvp)** : `decision_signing` signe la décision (algorithme identique, vecteur épinglé).

Reste opérateur : gestion des clés + registre PDP live.

## 5. Ordre de merge sûr

Conflits attendus : **mécaniques uniquement** (index d'autorité, `INDEX.md`, `GOVERNANCE_STATUS` / `CHANGELOG`), jamais de code.

**Next :**
```
1. la fondation issuer-auth + réconciliation (déjà mergée : #473)
2. pile bas-en-haut :  #467 → #468 → #469 → #470 → #471
3. #472                (parallèle, en dernier)
```

**mvp :**
```
1. pile bas-en-haut :  #56 → #59 → #61 → #62
2. le producteur de signature (issuer signing)
3. #65                 (parallèle, en dernier — rebase, résoudre GOVERNANCE_STATUS/CHANGELOG contre #59)
```

Règles :
- merger **bas-en-haut dans chaque pile** ; jamais une PR empilée avant sa base ;
- après chaque merge, régénérer `INDEX.md` et re-poser la ligne d'autorité si le fichier a bougé ;
- `#59` et `#65` se chevauchent sur `GOVERNANCE_STATUS`/`CHANGELOG` → `#65` en dernier.

## 6. Bornes

```text
revue != adoption
merge d'essai vert != autorisation de production
authenticated issuer != approval
admission != effect authorization
```

Aucune donnée réelle, aucun déploiement, aucune activation. Gate 8 humain reste ouvert.
