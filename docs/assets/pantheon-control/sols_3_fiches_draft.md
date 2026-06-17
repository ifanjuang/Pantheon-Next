# Sélection sols — modèle en 3 fiches

Statut : **documenté non implémenté**. Draft pour intégration dans `evidence.html`.

Objectif : remplacer le scénario trop éclaté en 5 fiches par une séquence claire en 3 fiches.

```text
Dossier de sélection reçu
→ analyse Pantheon / architecte
→ alerte incompatibilité support OSB / plancher bois
→ régression contrôlée des fiches déjà validées
→ déclenche Étude de structure
→ déclenche Estimatif
→ décision client
```

## Règle de régression contrôlée

Quand une nouvelle liste de matériaux est réceptionnée, elle ne remplace pas silencieusement les validations précédentes.

Si l’analyse montre que continuer sans modifier créerait une incompatibilité technique ou budgétaire, alors les fiches déjà validées qui dépendent de ce choix passent dans un état de révision.

Statut recommandé : **Validé précédemment — remis en question par nouvelle source**.

Ce statut ne supprime pas la validation antérieure. Il indique qu’elle n’est plus suffisante pour continuer sans arbitrage.

Fiches typiquement touchées :

- fiche `Choix client / matériaux` : le choix reste tracé, mais n’est plus directement exécutable ;
- fiche `Structure / support` : le support précédemment validé doit être revérifié contre le nouveau matériau ;
- fiche `Estimatif / budget` : l’estimatif antérieur devient potentiellement obsolète si reprise de support, chape sèche, renfort ou solives sont nécessaires ;
- fiche `Commande / entreprise` : aucune commande ne doit partir tant que la compatibilité n’est pas rétablie.

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

Régression détectée : si le projet continue avec cette nouvelle liste sans modification, les fiches `Choix client`, `Structure / support` et `Estimatif` sortent de leur état validé précédent.

Action recommandée : garder toutes les options dans la même fiche, mais marquer la grande dalle comme option à risque technique et rouvrir les fiches dépendantes.

Manque : nature du support, état OSB, entraxe solives, planéité, hauteur disponible, prescriptions fabricant, conditions de pose.

Décision attendue : déclencher une étude structure et un estimatif avant validation client ou commande.

Dépendances :

- Aval : SOL-002 — Étude de structure déclenchée.
- Aval : SOL-003 — Estimatif déclenché.

## SOL-002 — Étude de structure déclenchée par l’analyse du sol

Phase : Conception · Compatibilité support.

Statut : Validé précédemment — remis en question par nouvelle source. Risque : Critique. Décideur attendu : BET structure + architecte.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| MD | Agence | 2026-06-20 | `analyse-incompatibilite-sol-osb.md` | AN-01 | Interne | Candidate |
| PDF | BET structure à demander | 2026-06-20 | `avis-plancher-solives.pdf` | STR-00 | Technique | À produire |
| MD | Registre projet | 2026-06-10 | `validation-support-plancher.md` | VAL-01 | Interne | Validé précédemment |

Établi : une hypothèse de support avait été validée précédemment pour un usage courant.

Incertain : cette validation ne couvre pas nécessairement une grande dalle minérale sur support OSB / plancher bois.

Régression détectée : la fiche structure ne devient pas fausse, mais elle devient insuffisante pour autoriser le nouveau choix client.

Action recommandée : demander un avis structure ciblé : support existant, solives, charge ajoutée, besoin de chape sèche, panneau complémentaire ou renfort.

Manque : avis BET, sondage plancher, charges admissibles, prescription fabricant et système complet support + revêtement.

Décision attendue : confirmer que la validation structure précédente reste valable, la compléter, ou la retirer pour cette option.

Dépendances :

- Amont : SOL-001 — Dossier de sélection reçu et analysé.
- Aval : SOL-003 — Estimatif déclenché.

## SOL-003 — Estimatif déclenché par l’incompatibilité support / revêtement

Phase : Conception · Arbitrage coût / matériau.

Statut : Validé précédemment — remis en question par nouvelle source. Risque : Élevé. Décideur attendu : client + architecte + économiste.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| XLSX | Agence | 2026-06-20 | `estimatif-options-sols.xlsx` | EST-01 | Interne | Candidate |
| PDF | Agence | 2026-06-20 | `tableau-choix-sols.pdf` | SEL-04 | Indicée | Candidate |
| XLSX | Agence | 2026-06-12 | `estimatif-sols-valide.xlsx` | EST-00 | Interne | Validé précédemment |

Établi : un estimatif antérieur a pu être validé sur la base d’un complexe de sol courant.

Incertain : le montant validé ne couvre peut-être pas un changement de support, une reprise de solives ou une chape sèche.

Régression détectée : l’estimatif précédent ne doit plus être utilisé comme base ferme si l’option grande dalle est maintenue.

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

La nouvelle liste peut provoquer une régression contrôlée : on ne détruit pas les validations précédentes, mais on les sort de l’état `validé exécutable` tant que le nouveau choix n’a pas été vérifié.

Ce modèle évite trois erreurs :

1. accepter une option esthétique sans vérifier le support ;
2. refuser trop vite une option sans montrer au client la possibilité technique et le coût réel ;
3. continuer avec des fiches `choix`, `structure` ou `estimatif` validées sur une hypothèse qui n’est plus celle du projet.
