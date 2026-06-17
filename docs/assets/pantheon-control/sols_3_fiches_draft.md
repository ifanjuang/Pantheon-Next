# Sélection sols — modèle en 3 fiches

Statut : **documenté non implémenté**. Draft pour intégration dans `evidence.html`.

Objectif : remplacer le scénario trop éclaté en 5 fiches par une séquence claire en 3 fiches, sans créer une fiche par matériau.

```text
Dossier de sélection reçu
→ analyse Pantheon / architecte
→ impact candidat sur les fiches dépendantes
→ confirmation ou modification de la nouvelle liste
→ si liste confirmée avec incompatibilité : alerte structure + estimatif
→ si liste modifiée sans incompatibilité : fermeture des liens d’alerte
→ décision client
```

## Règle de liste groupée

Les matériaux ne doivent pas produire automatiquement une fiche par matériau.

Une fiche `Dossier de sélection` peut contenir une liste complète de choix client : revêtement A, revêtement B, revêtement C, indices, dates, fichiers, statuts, compatibilités, réserves et choix retenu.

Des fiches séparées ne sont créées que si l’analyse détecte un **sujet métier autonome** : incompatibilité support / revêtement, impact structurel, surcoût significatif, délai, changement de hauteur finie, contradiction avec un choix validé, ou décision client à tracer.

Cette règle évite de créer 30 fiches pour 30 matériaux. Le système regroupe par sujet décisionnel, pas par item de catalogue.

## Règle d’impact candidat

Quand une nouvelle liste de matériaux est réceptionnée, elle ne remplace pas silencieusement les validations précédentes.

L’analyse peut indiquer que, **si le projet continue avec cette nouvelle liste sans modification**, certaines fiches validées précédemment deviendraient insuffisantes ou devraient être révisées.

Mais tant que la nouvelle liste n’est pas confirmée, les fiches dépendantes ne sortent pas réellement de leur état validé.

Statut recommandé pendant cette période : **Impact candidat — validation potentiellement affectée**.

Ce statut signifie :

- la validation précédente reste tracée ;
- elle n’est pas annulée ;
- elle n’est pas encore remise en état de révision ;
- le système signale seulement qu’une nouvelle source pourrait la rendre insuffisante si elle est confirmée.

Fiches typiquement observées :

- fiche `Choix client / matériaux` : le choix reste validé dans sa version précédente ;
- fiche `Structure / support` : le support validé précédemment pourrait devoir être revérifié ;
- fiche `Estimatif / budget` : l’estimatif antérieur pourrait devenir incomplet si reprise de support, chape sèche, renfort ou solives sont nécessaires ;
- fiche `Commande / entreprise` : aucune commande ne doit partir sur la nouvelle liste tant que l’impact n’est pas arbitré.

## Règle de confirmation

### Cas 1 — Nouvelle liste confirmée sans modification

Si le client confirme la nouvelle liste contenant l’option incompatible ou non démontrée, l’impact candidat devient une alerte active.

Les fiches dépendantes peuvent alors changer d’état :

- `Structure / support` passe en `À revérifier` ou `À produire` ;
- `Estimatif / budget` passe en `À réviser` ou `Décision attendue` ;
- `Commande / entreprise` reste bloquée jusqu’à arbitrage.

La validation précédente n’est pas effacée. Elle devient une validation ancienne, valable pour l’hypothèse précédente, mais insuffisante pour la nouvelle hypothèse.

### Cas 2 — Nouvelle liste modifiée

Si le client modifie la liste et retire l’option qui causait l’incompatibilité, les alertes candidates et relations dépendantes sont fermées.

Les fiches `Structure` et `Estimatif` ne restent pas liées par inertie.

Elles ne sont réouvertes que si l’analyse de la liste modifiée détecte un autre sujet autonome : nouveau poids, nouvelle épaisseur, nouveau support, contrainte acoustique, changement de seuil, délai, coût ou contradiction documentaire.

### Cas 3 — Nouvelle liste confirmée avec variante compatible

Si la nouvelle liste garde l’intention esthétique mais remplace l’option risquée par une variante compatible, le système peut clôturer l’alerte grande dalle et garder seulement une trace :

`Option grande dalle écartée — variante compatible retenue`.

Dans ce cas, l’étude structure et l’estimatif ne sont déclenchés que si la variante produit encore un effet mesurable.

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

Impact candidat : si le client confirme cette nouvelle liste sans modification, les fiches `Choix client`, `Structure / support` et `Estimatif` devront être révisées ou complétées.

Action recommandée : garder toutes les options dans la même fiche, marquer la grande dalle comme option à risque technique, puis demander confirmation ou modification de la liste.

Manque : nature du support, état OSB, entraxe solives, planéité, hauteur disponible, prescriptions fabricant, conditions de pose.

Décision attendue : confirmer la liste, modifier la liste, ou déclencher étude structure et estimatif si l’option à risque est maintenue.

Dépendances :

- Aval candidat : SOL-002 — Étude de structure déclenchée seulement si la liste est confirmée avec l’option à risque.
- Aval candidat : SOL-003 — Estimatif déclenché seulement si la liste est confirmée avec effet coût / support.

## SOL-002 — Étude de structure déclenchée par confirmation de la liste

Phase : Conception · Compatibilité support.

Statut avant confirmation : Impact candidat — validation potentiellement affectée. Risque : Critique. Décideur attendu : BET structure + architecte.

Statut après confirmation de l’option à risque : À produire.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| MD | Agence | 2026-06-20 | `analyse-incompatibilite-sol-osb.md` | AN-01 | Interne | Candidate |
| PDF | BET structure à demander | 2026-06-20 | `avis-plancher-solives.pdf` | STR-00 | Technique | À produire si confirmé |
| MD | Registre projet | 2026-06-10 | `validation-support-plancher.md` | VAL-01 | Interne | Validé précédemment |

Établi : une hypothèse de support avait été validée précédemment pour un usage courant.

Incertain : cette validation ne couvre pas nécessairement une grande dalle minérale sur support OSB / plancher bois.

Impact candidat : la fiche structure ne devient pas fausse. Elle devient potentiellement insuffisante si la nouvelle liste est confirmée sans modification.

Action recommandée : ne pas sortir la fiche de son état validé tant que la nouvelle liste n’est pas confirmée ; préparer seulement la demande d’avis structure.

Manque : confirmation de la liste, avis BET, sondage plancher, charges admissibles, prescription fabricant et système complet support + revêtement.

Décision attendue : après confirmation, confirmer que la validation structure précédente reste valable, la compléter, ou la retirer pour cette option.

Dépendances :

- Amont : SOL-001 — Dossier de sélection reçu et analysé.
- Aval conditionnel : SOL-003 — Estimatif déclenché si l’étude structure ou le choix maintenu implique un surcoût.

## SOL-003 — Estimatif déclenché par confirmation de l’incompatibilité support / revêtement

Phase : Conception · Arbitrage coût / matériau.

Statut avant confirmation : Impact candidat — budget potentiellement affecté. Risque : Élevé. Décideur attendu : client + architecte + économiste.

Statut après confirmation de l’option à risque : À réviser ou Décision attendue.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| XLSX | Agence | 2026-06-20 | `estimatif-options-sols.xlsx` | EST-01 | Interne | Candidate si confirmé |
| PDF | Agence | 2026-06-20 | `tableau-choix-sols.pdf` | SEL-04 | Indicée | Candidate |
| XLSX | Agence | 2026-06-12 | `estimatif-sols-valide.xlsx` | EST-00 | Interne | Validé précédemment |

Établi : un estimatif antérieur a pu être validé sur la base d’un complexe de sol courant.

Incertain : le montant validé ne couvre peut-être pas un changement de support, une reprise de solives ou une chape sèche.

Impact candidat : l’estimatif précédent reste valable pour l’hypothèse précédente. Il devient potentiellement incomplet seulement si l’option grande dalle est confirmée.

Action recommandée : préparer trois scénarios sans les activer tant que la liste n’est pas confirmée :

1. Maintien de la grande dalle avec changement de support ou reprise des solives.
2. Revêtement alternatif dans le même esprit, plus compatible avec support bois.
3. Option parquet / lame / dalle souple compatible avec contrainte de plancher.

Manque : confirmation de la liste, prix reprise support, renfort solives, finition alternative, impact seuils, hauteur finie, délai et incidence sur les autres lots.

Décision attendue : choisir entre surcoût assumé, variante esthétique compatible, ou abandon de l’option grande dalle.

Dépendances :

- Amont : SOL-001 — Dossier de sélection reçu et analysé.
- Amont conditionnel : SOL-002 — Étude de structure si le choix maintenu l’exige.

## Lecture métier

Le dossier de sélection reste unique : il contient la liste client, les options, indices et dates.

Les fiches `Structure` et `Estimatif` ne sont pas des fiches indépendantes ouvertes par hasard. Elles sont déclenchées par l’analyse du dossier reçu, mais leur état ne change réellement qu’après confirmation de la nouvelle liste.

La nouvelle liste peut produire un impact candidat : on ne détruit pas les validations précédentes, on signale seulement qu’elles pourraient devenir insuffisantes si la nouvelle hypothèse est confirmée.

Si la liste est modifiée et que l’incompatibilité disparaît, les relations candidates sont fermées. Elles ne restent pas reliées par inertie.

Ce modèle évite quatre erreurs :

1. créer une fiche par matériau au lieu de regrouper par sujet ;
2. accepter une option esthétique sans vérifier le support ;
3. refuser trop vite une option sans montrer au client la possibilité technique et le coût réel ;
4. sortir des fiches validées de leur état avant que la nouvelle liste soit confirmée.
