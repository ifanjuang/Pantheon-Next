# Sélection sols — modèle en 3 fiches

Statut : **documenté non implémenté**. Draft pour intégration dans `evidence.html`.

Objectif : remplacer le scénario trop éclaté en 5 fiches par une séquence claire en 3 fiches, sans créer une fiche par matériau.

```text
Dossier de sélection reçu
→ fiche candidate d’impact
→ analyse Pantheon / architecte
→ liste temporaire des fiches affectées + niveau de dégradation potentiel
→ confirmation, modification ou demande de détail
→ recalcul complet de l’impact candidat
→ si liste confirmée telle quelle : dégradation enregistrée sur les fiches concernées
→ liens d’impact conservés pour réanalyse ultérieure
→ décision client
```

## Règle de liste groupée

Les matériaux ne doivent pas produire automatiquement une fiche par matériau.

Une fiche `Dossier de sélection` peut contenir une liste complète de choix client : revêtement A, revêtement B, revêtement C, indices, dates, fichiers, statuts, compatibilités, réserves et choix retenu.

Des fiches séparées ne sont créées que si l’analyse détecte un **sujet métier autonome** : incompatibilité support / revêtement, impact structurel, surcoût significatif, délai, changement de hauteur finie, contradiction avec un choix validé, ou décision client à tracer.

Cette règle évite de créer 30 fiches pour 30 matériaux. Le système regroupe par sujet décisionnel, pas par item de catalogue.

## Règle de fiche candidate d’impact

Une nouvelle liste de matériaux crée d’abord une **fiche candidate d’impact**.

Cette fiche candidate contient :

- la nouvelle source reçue ;
- la version de liste analysée ;
- les matériaux concernés ;
- les hypothèses détectées ;
- la liste des fiches potentiellement affectées ;
- le niveau de dégradation potentiel pour chaque fiche ;
- les raisons de l’impact ;
- les pièces ou vérifications nécessaires ;
- la décision attendue.

Elle ne modifie rien dans les autres fiches tant qu’elle reste candidate.

Aucune fiche existante ne reçoit de nouveau statut, de nouveau risque ou de nouvelle relation active tant que la fiche candidate n’est pas confirmée.

La fiche candidate agit comme une **enveloppe temporaire d’analyse**. Elle contient le graphe d’impact, mais ce graphe n’est pas encore écrit comme effet sur les fiches cibles.

## Niveaux de dégradation potentielle

Les fiches affectées sont listées dans la fiche candidate avec un niveau de dégradation potentiel.

| Niveau | Sens | Effet tant que candidat |
|---|---|---|
| D0 — aucun effet | La nouvelle liste ne change pas l’hypothèse de la fiche | Aucun changement |
| D1 — à surveiller | La fiche reste valide mais une vérification légère est conseillée | Aucun changement sur la fiche cible |
| D2 — validation potentiellement insuffisante | La fiche validée pourrait ne plus couvrir la nouvelle hypothèse | Aucun changement sur la fiche cible |
| D3 — révision probable | Si la liste est confirmée, la fiche devra être révisée | Aucun changement sur la fiche cible |
| D4 — blocage probable | Si la liste est confirmée, une commande, un devis ou une exécution doit être bloqué | Aucun changement sur la fiche cible |
| C1 — conflit latent | Deux hypothèses validées peuvent devenir incompatibles après vérification | Aucun changement automatique |
| C2 — conflit actif | Une fiche confirmée entre en contradiction avec une autre fiche confirmée | À arbitrer après action humaine |

Les niveaux D1 à D4 et C1 restent **contenus dans la fiche candidate**. Ils ne se propagent pas automatiquement.

## Règle de régénération

La liste des fiches affectées est régénérée à chaque analyse.

Elle est recalculée quand :

- une nouvelle version de liste est reçue ;
- le client modifie un choix ;
- une source fournisseur est remplacée ;
- le bouton `Recherche+` ou `Demander détail` est utilisé ;
- l’IA vérifie une norme, un DTU, une fiche fabricant ou une prescription ;
- une pièce complémentaire arrive ;
- l’architecte demande une analyse plus fine ;
- une fiche liée est modifiée ou confirmée.

Le nouveau calcul remplace le précédent dans la fiche candidate. Il n’empile pas les anciens liens candidats.

Si une fiche n’est plus affectée après nouvelle analyse, elle disparaît de la liste candidate. Aucun lien candidat résiduel n’est conservé.

## Règle de confirmation

### Cas 1 — Fiche candidate non confirmée

La fiche candidate reste un brouillon d’impact.

Les fiches ciblées ne changent pas :

- pas de perte de validation ;
- pas de statut modifié ;
- pas de mémoire canonique ;
- pas de commande bloquée automatiquement.

L’utilisateur voit seulement, dans la fiche candidate, la liste des impacts possibles.

### Cas 2 — Nouvelle liste modifiée

Si le client modifie la liste, la fiche candidate est réanalysée.

Les liens d’impact sont recalculés depuis zéro.

Si l’incompatibilité disparaît, les liens candidats vers `Structure`, `Estimatif` ou `Commande` sont supprimés de la fiche candidate.

Les fiches précédemment listées ne sont pas touchées.

### Cas 3 — Nouvelle liste confirmée telle quelle

Si le client confirme la liste contenant l’option incompatible ou non démontrée, la fiche candidate peut être validée par action humaine.

La validation déclenche une opération atomique :

1. enregistrer la nouvelle liste comme source confirmée ;
2. appliquer les changements d’état uniquement aux fiches explicitement listées ;
3. enregistrer la raison de la dégradation sur chaque fiche affectée ;
4. conserver les liens d’impact entre la fiche source et les fiches affectées ;
5. transformer les liens candidats en **liens d’impact confirmés** ;
6. conserver une trace courte : `liste confirmée — impact appliqué le JJ/MM/AAAA`.

Contrairement à une première hypothèse, les liens ne sont pas retirés après confirmation.

Ils restent visibles parce que la fiche source devra pouvoir être réanalysée si une fiche liée est modifiée, validée ou vérifiée plus tard.

Ces liens ne sont pas des déclencheurs automatiques. Ce sont des relations d’impact historisées, réanalysables et human-gated.

## Règle de liens confirmés

Un lien d’impact confirmé signifie :

- cette fiche a déjà affecté cette autre fiche ;
- l’effet a été appliqué ou arbitré ;
- la relation reste utile pour comprendre le dossier ;
- la relation peut servir de périmètre lors d’une nouvelle analyse ;
- la relation ne relance pas seule une dégradation.

Un lien confirmé peut avoir plusieurs états :

| État du lien | Sens |
|---|---|
| `impact_appliqué` | la fiche source a déjà dégradé ou modifié la fiche cible |
| `impact_refusé` | l’impact a été examiné et refusé |
| `impact_clôturé` | l’impact n’est plus actif mais reste historique |
| `à_réanalyser` | une modification liée impose une nouvelle vérification |
| `conflit` | deux fiches confirmées ne peuvent pas coexister sans arbitrage |

## Règle de conflit entre fiches confirmées

Une fiche déjà confirmée peut être vérifiée à nouveau.

Si cette vérification détecte un conflit avec d’autres fiches confirmées, le système ne dégrade pas immédiatement tout le graphe.

Règle par défaut : **la fiche récemment vérifiée ou récemment validée porte d’abord le conflit**.

Elle passe par exemple en :

`Confirmée — conflit détecté`

ou :

`À arbitrer — conflit avec fiches liées`.

Les autres fiches restent dans leur état propre, mais elles apparaissent dans la liste de conflit de la fiche vérifiée.

### Validation d’une fiche en conflit

Si l’humain confirme explicitement une fiche qui porte un conflit, alors les fiches conflictuelles rattachées peuvent à leur tour passer en mode conflit.

Exemple :

1. `SOL-001` est confirmée avec grande dalle.
2. `SOL-002` structure est vérifiée ensuite et confirme que le support OSB est incompatible sans reprise.
3. `SOL-002` porte d’abord le conflit : `Confirmée — conflit avec SOL-001`.
4. Si l’humain valide cette fiche conflit, alors `SOL-001` et `SOL-003` peuvent passer en `Conflit à arbitrer`, car la structure confirmée rend la liste et l’estimatif insuffisants.

Ce mécanisme évite de propager un conflit à chaque simple vérification.

La propagation du conflit demande une action humaine de validation du conflit.

## Règle anti-boucle

Une fiche dégradée par confirmation ne déclenche pas automatiquement une nouvelle dégradation en cascade.

Le système applique seulement les impacts listés dans la fiche candidate validée, puis conserve les liens pour audit et réanalyse.

Une nouvelle analyse peut être créée ensuite, mais seulement par :

- réception d’une nouvelle source ;
- demande explicite `Recherche+` / `Demander détail` ;
- action humaine ;
- modification ou validation d’une fiche liée ;
- analyse d’une modification réellement reçue.

Une fiche affectée ne peut pas réactiver automatiquement la fiche source qui l’a affectée.

Une fiche candidate ne peut pas dégrader une autre fiche candidate.

Deux fiches candidates ne peuvent pas se valider mutuellement.

Une fiche en conflit ne propage pas son conflit tant que ce conflit n’est pas validé par action humaine.

Le graphe d’impact est donc **persistant pour mémoire, non récursif pour action, recalculé et human-gated**.

## SOL-001 — Dossier de sélection reçu et analysé

Phase : Conception · Choix matériaux.

Statut : Fiche candidate d’impact. Risque : Élevé. Décideur attendu : client + architecte.

Sources du dossier de sélection :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| PDF | Client | 2026-06-19 | `selection-sols-client.pdf` | SEL-03 | Reçue | Brute |
| PDF | Fournisseur | 2026-06-19 | `option-a-grande-dalle-minerale.pdf` | MAT-A | Indicée | Candidate |
| PDF | Fournisseur | 2026-06-19 | `option-b-lames-aspect-pierre.pdf` | MAT-B | Indicée | Candidate |
| PDF | Fournisseur | 2026-06-19 | `option-c-parquet-contrecolle.pdf` | MAT-C | Indicée | Candidate |

Établi : le dossier de sélection client est réceptionné avec plusieurs revêtements datés, indicés et comparables.

Incertain : l’analyse détecte une alerte : l’option `grande dalle minérale` n’est pas démontrée compatible avec le support OSB / plancher bois.

Impact candidat : si le client confirme cette nouvelle liste sans modification, les fiches `Structure / support` et `Estimatif` devront probablement être révisées ou complétées.

Liste candidate des fiches affectées :

| Fiche potentiellement affectée | Niveau | Raison | Effet immédiat |
|---|---|---|---|
| SOL-002 — Étude de structure | D3 — révision probable | Support OSB / plancher bois non démontré compatible avec grande dalle | Aucun tant que candidat |
| SOL-003 — Estimatif | D3 — révision probable | Surcoût possible : support, solives, hauteur finie, seuils | Aucun tant que candidat |
| Commande matériaux | D4 — blocage probable | Commande risquée si option non vérifiée | Aucun tant que candidat |

Action recommandée : garder toutes les options dans la même fiche, marquer la grande dalle comme option à risque technique, puis demander confirmation, modification ou analyse complémentaire.

Bouton bas droite recommandé : `Recherche+ / Vérifier DTU-fabricant`.

Ce bouton relance l’analyse de la fiche candidate : support, DTU, fiches fabricant, prescriptions de pose, planéité, rigidité, charges et humidité éventuelle.

Manque : nature du support, état OSB, entraxe solives, planéité, hauteur disponible, prescriptions fabricant, conditions de pose.

Décision attendue : confirmer la liste, modifier la liste, ou déclencher étude structure et estimatif si l’option à risque est maintenue.

Dépendances :

- Relations candidates tant que la fiche n’est pas confirmée.
- Relations transformées en liens d’impact confirmés si la liste est validée telle quelle.
- Relations régénérées à chaque nouvelle analyse ou demande de détail.

## SOL-002 — Étude de structure déclenchée par confirmation de la liste

Phase : Conception · Compatibilité support.

Statut avant confirmation : Validé précédemment ou non affecté dans sa fiche propre. L’impact reste uniquement visible dans SOL-001.

Statut après confirmation de l’option à risque : À produire ou À revérifier, si SOL-001 est validée telle quelle.

Risque : Critique. Décideur attendu : BET structure + architecte.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| MD | Agence | 2026-06-20 | `analyse-incompatibilite-sol-osb.md` | AN-01 | Interne | Candidate dans SOL-001 |
| PDF | BET structure à demander | 2026-06-20 | `avis-plancher-solives.pdf` | STR-00 | Technique | À produire si confirmé |
| MD | Registre projet | 2026-06-10 | `validation-support-plancher.md` | VAL-01 | Interne | Validé précédemment |

Établi : une hypothèse de support avait été validée précédemment pour un usage courant.

Incertain : cette validation ne couvre pas nécessairement une grande dalle minérale sur support OSB / plancher bois.

Comportement tant que SOL-001 est candidate : ne rien écrire sur SOL-002. La fiche SOL-002 n’affiche pas d’alerte active, sauf si l’utilisateur ouvre la fiche candidate SOL-001.

Comportement après confirmation de SOL-001 : appliquer l’état `À produire` ou `À revérifier`, avec motif : `nouvelle liste de sols confirmée avec option grande dalle non démontrée compatible`.

Comportement après vérification structure : si le BET confirme l’incompatibilité, SOL-002 porte d’abord le conflit. Les autres fiches liées ne passent en conflit qu’après validation humaine de cette fiche conflit.

Action recommandée après confirmation : demander un avis structure ciblé : support existant, solives, charge ajoutée, besoin de chape sèche, panneau complémentaire ou renfort.

Manque : confirmation de la liste, avis BET, sondage plancher, charges admissibles, prescription fabricant et système complet support + revêtement.

Décision attendue : confirmer que la validation structure précédente reste valable, la compléter, ou la retirer pour cette option.

## SOL-003 — Estimatif déclenché par confirmation de l’incompatibilité support / revêtement

Phase : Conception · Arbitrage coût / matériau.

Statut avant confirmation : Validé précédemment ou non affecté dans sa fiche propre. L’impact reste uniquement visible dans SOL-001.

Statut après confirmation de l’option à risque : À réviser ou Décision attendue, si SOL-001 est validée telle quelle.

Risque : Élevé. Décideur attendu : client + architecte + économiste.

Sources :

| Type | Origine | Date | Fichier | Indice | Force | Statut |
|---|---|---:|---|---|---|---|
| XLSX | Agence | 2026-06-20 | `estimatif-options-sols.xlsx` | EST-01 | Interne | Candidate dans SOL-001 |
| PDF | Agence | 2026-06-20 | `tableau-choix-sols.pdf` | SEL-04 | Indicée | Candidate |
| XLSX | Agence | 2026-06-12 | `estimatif-sols-valide.xlsx` | EST-00 | Interne | Validé précédemment |

Établi : un estimatif antérieur a pu être validé sur la base d’un complexe de sol courant.

Incertain : le montant validé ne couvre peut-être pas un changement de support, une reprise de solives ou une chape sèche.

Comportement tant que SOL-001 est candidate : ne rien écrire sur SOL-003. Le budget antérieur reste dans son état propre, mais SOL-001 signale un impact candidat.

Comportement après confirmation de SOL-001 : appliquer l’état `À réviser` ou `Décision attendue`, avec motif : `nouvelle liste de sols confirmée avec effet support / coût possible`.

Action recommandée après confirmation : présenter trois scénarios :

1. Maintien de la grande dalle avec changement de support ou reprise des solives.
2. Revêtement alternatif dans le même esprit, plus compatible avec support bois.
3. Option parquet / lame / dalle souple compatible avec contrainte de plancher.

Manque : confirmation de la liste, prix reprise support, renfort solives, finition alternative, impact seuils, hauteur finie, délai et incidence sur les autres lots.

Décision attendue : choisir entre surcoût assumé, variante esthétique compatible, ou abandon de l’option grande dalle.

## Lecture métier

Le dossier de sélection reste unique : il contient la liste client, les options, indices et dates.

La fiche candidate contient la liste des fiches affectées et leurs niveaux de dégradation potentiels. Les fiches ciblées ne sont pas modifiées tant que cette fiche reste candidate.

Après confirmation, les liens candidats deviennent des liens d’impact confirmés. Ils restent visibles pour audit, compréhension et réanalyse future.

Les liens ne déclenchent rien seuls. Ils servent de périmètre de vérification quand une fiche liée est modifiée, confirmée ou réanalysée.

Si une fiche confirmée est vérifiée et entre en conflit avec d’autres fiches, la fiche vérifiée ou récemment validée porte d’abord le conflit. Les fiches conflictuelles rattachées ne passent à leur tour en conflit qu’après validation humaine de cette fiche conflit.

Ce modèle évite six erreurs :

1. créer une fiche par matériau au lieu de regrouper par sujet ;
2. accepter une option esthétique sans vérifier le support ;
3. refuser trop vite une option sans montrer au client la possibilité technique et le coût réel ;
4. sortir des fiches validées de leur état avant que la nouvelle liste soit confirmée ;
5. supprimer trop tôt les liens utiles à la réanalyse ;
6. créer des boucles d’activation entre fiches candidates, fiches confirmées et fiches en conflit.
