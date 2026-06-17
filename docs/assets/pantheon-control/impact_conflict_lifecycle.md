# Impact et conflit entre fiches — logique algorithmique

Statut : **documenté non implémenté**. Spécification candidate pour la logique de fiches `Points de contrôle`.

Objet : définir comment une fiche candidate, une fiche confirmée, une modification ou une vérification peuvent affecter d’autres fiches sans créer de propagation récursive incontrôlée.

## Principe central

Une fiche ne modifie pas le projet parce qu’elle existe.

Elle peut seulement :

1. contenir une analyse candidate ;
2. prévisualiser un impact ;
3. demander confirmation humaine ;
4. appliquer une transaction bornée ;
5. conserver des liens d’impact réanalysables ;
6. porter un conflit si elle devient incompatible avec une autre fiche confirmée.

La règle de base est :

```text
Calculer n’applique rien.
Prévisualiser n’applique rien.
Confirmer applique une transaction bornée.
Un conflit potentiel demande confirmation avant application.
Un conflit confirmé marque les fiches impliquées.
Les liens persistants servent à réanalyser, pas à propager seuls.
```

## Entités logiques

### Fiche

Une fiche contient :

- `id` ;
- `type` : sélection, structure, estimatif, programme, technique, chantier, sécurité, etc. ;
- `status` ;
- `source_version` ;
- `assumptions` ;
- `validated_scope` ;
- `impact_links` ;
- `conflict_links` ;
- `audit_log`.

### Lien d’impact

Un lien d’impact relie une fiche source à une fiche cible.

Il peut être :

| État | Sens |
|---|---|
| `candidate` | effet possible, contenu dans la fiche source seulement |
| `confirmed` | effet appliqué ou arbitré, conservé pour réanalyse |
| `rejected` | effet refusé après arbitrage |
| `closed` | effet historique sans impact actif |
| `needs_reanalysis` | lien à réexaminer après modification ou validation liée |
| `conflict` | deux fiches ne peuvent pas coexister telles quelles |

### Impact

Un impact est une modification potentielle ou réelle sur une fiche cible.

Il contient :

- fiche cible ;
- état actuel ;
- état proposé ;
- niveau de dégradation ;
- raison ;
- seuil déclenché ;
- source de preuve ;
- besoin de confirmation ;
- effet immédiat ou différé.

## Niveaux de dégradation

| Niveau | Signification | Action par défaut |
|---|---|---|
| D0 | Aucun effet | Rien |
| D1 | À surveiller | Mention seulement dans la fiche source |
| D2 | Validation potentiellement insuffisante | Pré-alerte, confirmation requise si validation source |
| D3 | Révision probable | Pré-alerte forte, confirmation requise |
| D4 | Blocage probable | Confirmation explicite obligatoire avant application |
| C1 | Conflit potentiel | Alerter avant validation |
| C2 | Conflit confirmé | Marquer les fiches impliquées après confirmation humaine |

## Seuils de détection

Un impact ne doit pas être créé pour chaque micro-changement.

### Seuil financier

Créer une alerte coût seulement si au moins un des critères est vrai :

- l’écart dépasse un montant minimal défini par projet ;
- l’écart dépasse un pourcentage du lot ;
- l’écart dépasse un pourcentage du budget global ;
- l’écart demande un avenant ;
- l’écart demande arbitrage client ;
- l’écart modifie la commande ou le planning.

### Seuil de nature technique

Créer une alerte même sans coût exact si la modification change la nature du système :

- changement de type de plancher ;
- reprise de solives ;
- changement support OSB / chape / complexe sec ;
- ajout plancher chauffant ;
- ajout PAC, CTA, ventilation lourde, extraction ou groupe extérieur ;
- changement de système constructif ;
- ajout ou suppression de pièce ;
- changement de programme ;
- modification feu, structure, acoustique, accessibilité, hygiène, ABF ou sécurité ;
- changement d’épaisseur touchant seuils, portes, escaliers ou hauteur libre.

## Validation d’une fiche candidate sans conflit

```text
validateCandidate(card):
  impacts = snapshot(card.candidate_impacts)
  conflicts = detectConflicts(card, impacts)

  if conflicts is empty and impacts are below confirmation threshold:
      confirm card
      keep confirmed impact links if any
      do not mutate unrelated cards

  if impacts require confirmation:
      show preflight warning
      wait human confirmation
```

## Validation d’une fiche candidate avec risque de conflit

Avant d’appliquer, le système doit afficher une confirmation explicite.

Message attendu côté interface :

```text
Attention : cette validation peut affecter d’autres fiches.

Si vous confirmez cette fiche :
- STRUCT-012 passera en Conflit / À revérifier.
- BUDG-006 passera en À réviser.
- CMD-003 restera bloquée avant commande.

Raison : la liste confirmée contient une option incompatible avec l’hypothèse structure validée.

Confirmer l’application ?
```

Tant que l’utilisateur ne confirme pas, rien n’est écrit sur les autres fiches.

## Transaction de validation avec conflit confirmé

Si l’utilisateur confirme malgré l’alerte, la transaction doit être atomique.

```text
applyConfirmedCandidate(card):
  begin transaction

  card.status = confirmed
  card.source_version = confirmed_version

  for each impact in card.candidate_impacts:
      create confirmed impact link card -> impact.target
      apply target status only if impact level >= threshold
      write degradation reason on target

  for each conflict in detected_conflicts:
      mark card as conflict participant
      mark conflict.target as conflict participant
      create bidirectional conflict link
      write conflict reason on both cards

  clear only temporary candidate queue
  keep confirmed impact links

  commit transaction
```

Donc, si une fiche confirmée entre réellement en conflit avec une autre fiche déjà confirmée, les deux deviennent conflit.

La différence importante : ce changement n’arrive pas lors d’une simple analyse. Il arrive uniquement après validation explicite avec prévisualisation des effets.

## Cas où une fiche validée crée un conflit avec une autre fiche validée

Exemple :

- `SOL-001` est confirmée : liste de matériaux avec grande dalle.
- `SOL-002` était confirmée avant : support OSB / plancher bois validé pour un usage courant.
- La validation de `SOL-001` révèle que l’hypothèse de `SOL-002` ne couvre pas cette grande dalle.

Prévalidation :

```text
Risque de conflit détecté :
SOL-001 ↔ SOL-002

SOL-001 veut confirmer une option grande dalle.
SOL-002 confirme un support bois non démontré compatible.

Si vous validez SOL-001 telle quelle :
- SOL-001 deviendra Confirmée — conflit avec SOL-002.
- SOL-002 deviendra Confirmée — conflit avec SOL-001.
- SOL-003 Estimatif passera À réviser si le seuil coût est atteint.
```

Après confirmation humaine :

- `SOL-001` : `Confirmée — conflit avec SOL-002` ;
- `SOL-002` : `Confirmée — conflit avec SOL-001` ;
- `SOL-003` : `À réviser` ou `Conflit coût`, selon seuil ;
- liens d’impact confirmés conservés.

## Cas où la vérification d’une fiche déjà confirmée détecte un conflit

Une fiche confirmée peut être réanalysée après demande `Recherche+`, nouvelle source, nouvelle norme, DTU, fiche fabricant, avis BET ou validation liée.

```text
recheckConfirmedCard(card):
  conflicts = detectConflicts(card, confirmedImpactLinks(card))

  if conflicts found:
      show preflight warning
      if user only requests analysis:
          card.status = confirmed_with_conflict_detected
          do not mutate linked cards
      if user validates conflict:
          mark card and linked confirmed conflicting cards as conflict
```

Ici, il y a deux niveaux :

1. conflit détecté ;
2. conflit validé.

Un conflit détecté ne propage pas automatiquement.

Un conflit validé marque toutes les fiches confirmées impliquées.

## Propagation contrôlée du conflit

La propagation n’est autorisée que dans un cas : l’humain valide une fiche ou une vérification qui indique clairement les fiches qui vont être affectées.

Avant application, l’interface doit annoncer :

- fiches affectées ;
- nouveau statut proposé ;
- raison ;
- niveau de gravité ;
- seuil déclenché ;
- possibilité d’annuler.

Aucune propagation silencieuse.

## Cas de modification qui supprime le conflit

Si le client modifie la liste et retire l’option incompatible :

```text
modifyCandidate(card):
  new_impacts = recomputeImpacts(card)

  if conflict no longer exists:
      mark candidate conflict link as closed
      do not mutate target cards

  if confirmed conflict already existed:
      create resolution proposal
      require human validation to close conflict on both cards
```

Si le conflit était seulement candidat, il disparaît de la fiche candidate.

Si le conflit était déjà confirmé, sa clôture demande validation humaine, car les fiches avaient déjà changé d’état.

## Cas de plusieurs fiches potentiellement dégradées

Une fiche peut affecter plusieurs fiches.

Exemple : une liste de matériaux confirmée peut affecter :

- structure ;
- estimatif ;
- commande ;
- planning ;
- CCTP ;
- seuils / accessibilité.

Règle : chaque effet doit être explicitement listé avant validation.

```text
impact_set = [
  {target: STRUCT-012, state: conflict, reason: support incompatible},
  {target: BUDG-006, state: revise, reason: cost threshold reached},
  {target: CMD-003, state: blocked, reason: command not allowed before support validation}
]
```

L’utilisateur valide ou refuse l’ensemble de la transaction.

Pas d’application partielle silencieuse.

## Anti-boucle

Les règles anti-boucle sont :

1. Une analyse ne modifie rien.
2. Une prévisualisation ne modifie rien.
3. Une confirmation applique uniquement la liste prévisualisée.
4. Une fiche candidate ne peut pas dégrader une autre fiche candidate.
5. Une fiche affectée ne réactive pas automatiquement la fiche source.
6. Un lien confirmé est passif par défaut.
7. Un conflit détecté ne propage rien sans validation humaine.
8. Un conflit validé marque les fiches explicitement listées.
9. Une résolution de conflit confirmé demande validation humaine.
10. Toute réanalyse remplace le graphe candidat précédent, elle ne l’empile pas.

## Pseudo-code complet

```text
analyze(card):
  impacts = computeImpacts(card)
  conflicts = computePotentialConflicts(card, impacts)
  card.candidate_graph = { impacts, conflicts }
  return preview(card.candidate_graph)

validate(card):
  graph = snapshot(card.candidate_graph)
  affected = graph.impacts + graph.conflicts

  if affected is not empty:
      warning = buildPreflightWarning(affected)
      human_confirmed = requestHumanConfirmation(warning)
      if not human_confirmed:
          return no_change

  begin transaction

  card.status = confirmed

  for each impact in graph.impacts:
      createOrUpdateImpactLink(card, impact.target, confirmed)
      if impact.level >= threshold:
          applyStatus(impact.target, impact.proposed_status)
          appendReason(impact.target, impact.reason)

  for each conflict in graph.conflicts:
      if conflict.confirmed_target_status == confirmed:
          markConflict(card, conflict.target)
          markConflict(conflict.target, card)
          createConflictLink(card, conflict.target)

  archiveCandidateGraph(card)
  keepConfirmedLinks(card)

  commit transaction

recheck(card):
  graph = computeConflictsAgainstConfirmedLinks(card)
  if graph.conflicts:
      warning = buildPreflightWarning(graph.conflicts)
      if user_confirms_conflict:
          begin transaction
          for each conflict in graph.conflicts:
              markConflict(card, conflict.target)
              markConflict(conflict.target, card)
          commit
      else:
          card.status = confirmed_conflict_detected
          card.pending_conflicts = graph.conflicts
```

## Formule courte

La bonne règle est :

**Avant validation : calculer et avertir.**

**Pendant validation : appliquer une transaction explicite.**

**Après validation : garder les liens pour réanalyse, mais interdire toute propagation automatique.**

**En conflit confirmé : les deux fiches confirmées deviennent conflit.**
