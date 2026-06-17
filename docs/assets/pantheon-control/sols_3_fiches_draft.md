# Sélection sols — modèle en 3 fiches

Statut : **documenté non implémenté**. Draft pour intégration dans `evidence.html`.

Objectif : remplacer le scénario trop éclaté en 5 fiches par une séquence claire en 3 fiches.

```text
Dossier de sélection reçu
→ analyse Pantheon / architecte
→ alerte incompatibilité support OSB / plancher bois
→ déclenche Étude de structure
→ déclenche Estimatif
→ décision client
```

## SOL-001 — Dossier de sélection reçu et analysé

Phase : Conception · Choix matériaux.

Statut : À vérifier. Risque : Élevé. Décideur attendu : client + architecte.

Sources du dossier de sélection :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| PDF | Client | 2026-06-19 | `selection-sols-client.pdf` | SEL-03 | Reçue | Brute |
| PDF | Fournisseur | 2026-06-19 | `option-a-grande-dalle-minerale.pdf` | MAT-A | Indicée | Candidate |
| PDF | Fournisseur | 2026-06-19 | `option-b-lames-aspect-pierre.pdf` | MAT-B | Indicée | Candidate |
| PDF | Fournisseur | 2026-06-19 | `option-c-parquet-contrecolle.pdf` | MAT-C | Indicée | Candidate |

Établi : le dossier de sélection client est réceptionné avec plusieurs revêtements datés, indicés et comparables.

Incertain : l’analyse détecte une alerte : l’option `grande dalle minérale` n’est pas démontrée compatible avec le support OSB / plancher bois.

Action recommandée : garder toutes les options dans la même fiche, mais marquer la grande dalle comme option à risque technique.

Manque : nature du support, état OSB, entraxe solives, planéité, hauteur disponible, prescriptions fabricant, conditions de pose.

Décision attendue : déclencher une étude structure et un estimatif avant validation client ou commande.

Dépendances :

- Aval : SOL-002 — Étude de structure déclenchée.
- Aval : SOL-003 — Estimatif déclenché.

## SOL-002 — Étude de structure déclenchée par l’analyse du sol

Phase : Conception · Compatibilité support.

Statut : À produire. Risque : Critique. Décideur attendu : BET structure + architecte.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| MD | Agence | 2026-06-20 | `analyse-incompatibilite-sol-osb.md` | AN-01 | Interne | Candidate |
| PDF | BET structure à demander | 2026-06-20 | `avis-plancher-solives.pdf` | STR-00 | Technique | À produire |

Établi : l’analyse du dossier de sélection déclenche un contrôle structurel du support bois / OSB.

Incertain : rigidité, flèche, entraxe solives, surcharge admissible et compatibilité avec une grande dalle ne sont pas établis.

Action recommandée : demander un avis structure ciblé : support existant, solives, charge ajoutée, besoin de chape sèche, panneau complémentaire ou renfort.

Manque : avis BET, sondage plancher, charges admissibles, prescription fabricant et système complet support + revêtement.

Décision attendue : autoriser l’option grande dalle uniquement si le système complet est validé, ou l’écarter.

Dépendances :

- Amont : SOL-001 — Dossier de sélection reçu et analysé.
- Aval : SOL-003 — Estimatif déclenché.

## SOL-003 — Estimatif déclenché par l’incompatibilité support / revêtement

Phase : Conception · Arbitrage coût / matériau.

Statut : Décision attendue. Risque : Élevé. Décideur attendu : client + architecte + économiste.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| XLSX | Agence | 2026-06-20 | `estimatif-options-sols.xlsx` | EST-01 | Interne | Candidate |
| PDF | Agence | 2026-06-20 | `tableau-choix-sols.pdf` | SEL-04 | Indicée | Candidate |

Établi : l’incompatibilité potentielle déclenche un estimatif comparatif.

Incertain : le montant dépend de l’avis structure, du système support, des hauteurs finies, des seuils et du choix client.

Action recommandée : présenter trois scénarios :

1. Maintien de la grande dalle avec changement de support ou reprise des solives.
2. Revêtement alternatif dans le même esprit, plus compatible avec support bois.
3. Option parquet / lame / dalle souple compatible avec contrainte de plancher.

Manque : prix reprise support, renfort solives, finition alternative, impact seuils, hauteur finie, délai et incidence sur les autres lots.

Décision attendue : choisir entre surcoût assumé, variante esthétique compatible, ou abandon de l’option grande dalle.

Dépendances :

- Amont : SOL-001 — Dossier de sélection reçu et analysé.
- Amont : SOL-002 — Étude de structure.

## Lecture métier

Le dossier de sélection reste unique : il contient la liste client, les options, indices et dates.

Les fiches `Structure` et `Estimatif` ne sont pas des fiches indépendantes ouvertes par hasard. Elles sont déclenchées par l’analyse du dossier reçu.

Ce modèle évite deux erreurs :

1. accepter une option esthétique sans vérifier le support ;
2. refuser trop vite une option sans montrer au client la possibilité technique et le coût réel.
