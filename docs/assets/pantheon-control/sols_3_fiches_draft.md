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
→ suppression des liens candidats depuis la fiche confirmée
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

Aucune fiche existante ne reçoit de nouveau statut, de nouveau lien, de nouveau risque ou de nouvelle relation tant que la fiche candidate n’est pas confirmée.

La fiche candidate agit comme une **enveloppe temporaire d’analyse**. Elle contient le graphe d’impact, mais ce graphe n’est pas encore écrit dans le projet.

## Niveaux de dégradation potentielle

Les fiches affectées sont listées dans la fiche candidate avec un niveau de dégradation potentiel.

| Niveau | Sens | Effet tant que candidat |
|---|---|---|
| D0 — aucun effet | La nouvelle liste ne change pas l’hypothèse de la fiche | Aucun changement |
| D1 — à surveiller | La fiche reste valide mais une vérification légère est conseillée | Aucun changement sur la fiche cible |
| D2 — validation potentiellement insuffisante | La fiche validée pourrait ne plus couvrir la nouvelle hypothèse | Aucun changement sur la fiche cible |
| D3 — révision probable | Si la liste est confirmée, la fiche devra être révisée | Aucun changement sur la fiche cible |
| D4 — blocage probable | Si la liste est confirmée, une commande, un devis ou une exécution doit être bloqué | Aucun changement sur la fiche cible |

Les niveaux D1 à D4 restent **contenus dans la fiche candidate**. Ils ne se propagent pas automatiquement.

## Règle de régénération

La liste des fiches affectées est régénérée à chaque analyse.

Elle est recalculée quand :

- une nouvelle version de liste est reçue ;
- le client modifie un choix ;
- une source fournisseur est remplacée ;
- le bouton `Recherche+` ou `Demander détail` est utilisé ;
- l’IA vérifie une norme, un DTU, une fiche fabricant ou une prescription ;
- une pièce complémentaire arrive ;
- l’architecte demande une analyse plus fine.

Le nouveau calcul remplace le précédent dans la fiche candidate. Il n’empile pas les anciens liens.

Si une fiche n’est plus affectée après nouvelle analyse, elle disparaît de la liste candidate. Aucun lien résiduel n’est conservé.

## Règle de confirmation

### Cas 1 — Fiche candidate non confirmée

La fiche candidate reste un brouillon d’impact.

Les fiches ciblées ne changent pas :

- pas de perte de validation ;
- pas de nouveau lien écrit ;
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
4. supprimer les liens candidats de la fiche source confirmée ;
5. conserver une trace courte : `liste confirmée — impact appliqué le JJ/MM/AAAA`.

La fiche source devenue validée ne garde pas ses liens candidats vers les autres fiches. Les relations d’impact ont servi à appliquer la décision, elles ne deviennent pas des dépendances permanentes par défaut.

Les liens permanents ne sont créés que si l’humain ou la règle de gouvernance décide qu’un lien métier doit rester visible.

## Règle anti-boucle

Une fiche dégradée par confirmation ne déclenche pas automatiquement une nouvelle dégradation en cascade.

Le système applique seulement les impacts listés dans la fiche candidate validée.

Une nouvelle fiche candidate peut être créée ensuite, mais seulement par :

- réception d’une nouvelle source ;
- demande explicite `Recherche+` / `Demander détail` ;
- action humaine ;
- analyse d’une modification réellement reçue.

Une fiche affectée ne peut pas réactiver la fiche source qui l’a affectée.

Une fiche candidate ne peut pas dégrader une autre fiche candidate.

Deux fiches candidates ne peuvent pas se valider mutuellement.

Le graphe d’impact est donc **temporaire, non récursif, recalculé et human-gated**.

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

- Relations candidates uniquement : SOL-002 et SOL-003.
- Aucune relation permanente tant que la fiche n’est pas confirmée.
- Relations régénérées à chaque nouvelle analyse.

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

Les liens d’impact sont régénérés à chaque analyse, modification ou demande de détail. Ils ne sont pas des liens permanents.

Si la fiche candidate est confirmée telle quelle, les dégradations sont appliquées puis les liens candidats sont retirés de la fiche source devenue validée.

Si la liste est modifiée, les liens candidats sont recalculés. Si l’incompatibilité disparaît, les liens sont fermés.

Ce modèle évite cinq erreurs :

1. créer une fiche par matériau au lieu de regrouper par sujet ;
2. accepter une option esthétique sans vérifier le support ;
3. refuser trop vite une option sans montrer au client la possibilité technique et le coût réel ;
4. sortir des fiches validées de leur état avant que la nouvelle liste soit confirmée ;
5. créer des boucles d’activation entre fiches candidates, fiches dégradées et nouvelles analyses.
