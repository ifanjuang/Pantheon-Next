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
Un impact appliqué sort du graphe actif et devient trace passive.
Un conflit confirmé reste actif jusqu’à résolution ou réanalyse validée.
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

### Impact et conflit : deux axes séparés

Un **impact** est un effet produit par une fiche sur une autre : révision, blocage, changement d’hypothèse, besoin de chiffrage, besoin d’avis technique.

Un **conflit** est une incohérence entre deux fiches qui ne peuvent pas rester valides ensemble sans arbitrage.

Une fiche peut donc avoir :

```text
lifecycle_status = candidate / confirmed / archived / rejected
impact_state = none / candidate / applied / closed / needs_reanalysis
coherence_state = coherent / tension / conflict_potential / conflict_active / resolved
```

Il ne faut pas fusionner `impact_state` et `coherence_state`.

## Lien d’impact

Un lien d’impact relie une fiche source à une fiche cible.

Il peut être :

| État | Sens |
|---|---|
| `candidate` | effet possible, contenu dans la fiche source seulement |
| `applied` | effet appliqué à la fiche cible, sorti du graphe actif |
| `closed` | effet historique sans impact actif |
| `rejected` | effet refusé après arbitrage |
| `needs_reanalysis` | lien passif à réexaminer après modification ou validation liée |

Un impact appliqué n’est pas supprimé de l’historique. Il est retiré de la file active d’impact.

Il reste comme trace passive : qui a impacté quoi, quand, pourquoi, avec quelle source et quelle décision.

## Lien de conflit

Un lien de conflit relie deux fiches dont les hypothèses ne peuvent pas coexister.

Il peut être :

| État | Sens |
|---|---|
| `potential` | conflit possible avant confirmation |
| `detected` | conflit détecté lors d’une vérification, non appliqué aux autres fiches |
| `active` | conflit confirmé, visible sur les fiches impliquées |
| `to_recheck` | conflit conservé en attente de réanalyse |
| `resolved` | conflit arbitré et historisé |

Un conflit actif reste actif tant qu’il n’est pas résolu, refusé ou réanalysé avec validation humaine.

C’est la différence majeure avec l’impact :

```text
Impact appliqué → sort du graphe actif, reste en audit.
Conflit confirmé → reste dans le graphe actif jusqu’à résolution.
```

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
      keep passive impact links if any
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

Impacts appliqués si vous confirmez :
- BUDG-006 passera en À réviser.
- CMD-003 restera bloquée avant commande.

Conflits créés si vous confirmez :
- SOL-001 passera en Conflit actif avec STRUCT-012.
- STRUCT-012 passera en Conflit actif avec SOL-001.

Raison : la liste confirmée contient une option incompatible avec l’hypothèse structure validée.

Confirmer l’application ?
```

Tant que l’utilisateur ne confirme pas, rien n’est écrit sur les autres fiches.

## Transaction de validation avec impacts et conflits

Si l’utilisateur confirme malgré l’alerte, la transaction doit être atomique.

```text
applyConfirmedCandidate(card):
  begin transaction

  card.status = confirmed
  card.source_version = confirmed_version

  for each impact in card.candidate_impacts:
      create impact link card -> impact.target
      apply target status only if impact level >= threshold
      write degradation reason on target
      mark impact link as applied or closed
      remove impact from active queue

  for each conflict in detected_conflicts:
      mark card as conflict participant
      mark conflict.target as conflict participant
      create bidirectional active conflict link
      write conflict reason on both cards

  clear temporary candidate queue
  keep passive impact audit links
  keep active conflict links

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
- SOL-001 deviendra Confirmée — conflit actif avec SOL-002.
- SOL-002 deviendra Confirmée — conflit actif avec SOL-001.
- SOL-003 Estimatif passera À réviser si le seuil coût est atteint.
```

Après confirmation humaine :

- `SOL-001` : `Confirmée — conflit actif avec SOL-002` ;
- `SOL-002` : `Confirmée — conflit actif avec SOL-001` ;
- `SOL-003` : `À réviser`, si le seuil coût est atteint ;
- lien d’impact `SOL-001 → SOL-003` : `applied` puis passif ;
- lien de conflit `SOL-001 ↔ SOL-002` : `active`.

## Cas où la vérification d’une fiche déjà confirmée détecte un conflit

Une fiche confirmée peut être réanalysée après demande `Recherche+`, nouvelle source, nouvelle norme, DTU, fiche fabricant, avis BET ou validation liée.

```text
recheckConfirmedCard(card):
  conflicts = detectConflicts(card, activeOrReanalysisLinks(card))

  if conflicts found:
      show preflight warning
      if user only requests analysis:
          card.status = confirmed_with_conflict_detected
          card.conflict_links = detected but not active on targets
          do not mutate linked cards
      if user validates conflict:
          mark card and linked confirmed conflicting cards as conflict
          create active bidirectional conflict links
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

## Cas de modification qui supprime un impact ou un conflit

Si le client modifie la liste et retire l’option incompatible :

```text
modifyCandidate(card):
  new_impacts = recomputeImpacts(card)
  new_conflicts = recomputeConflicts(card)

  if candidate impact no longer exists:
      remove it from candidate preview
      do not mutate target cards

  if applied impact already existed:
      create reanalysis proposal
      require human validation to close the passive impact link if needed

  if active conflict already existed:
      create resolution proposal
      require human validation to resolve conflict on both cards
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
  {target: BUDG-006, state: revise, reason: cost threshold reached},
  {target: CMD-003, state: blocked, reason: command not allowed before support validation}
]

conflict_set = [
  {target: STRUCT-012, state: conflict_active, reason: support incompatible with retained floor finish}
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
6. Un impact appliqué sort du graphe actif et devient audit passif.
7. Un conflit actif reste actif jusqu’à résolution ou réanalyse validée.
8. Un conflit détecté ne propage rien sans validation humaine.
9. Un conflit validé marque les fiches explicitement listées.
10. Une résolution de conflit confirmé demande validation humaine.
11. Toute réanalyse remplace le graphe candidat précédent, elle ne l’empile pas.

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
      createOrUpdateImpactLink(card, impact.target, applied)
      if impact.level >= threshold:
          applyStatus(impact.target, impact.proposed_status)
          appendReason(impact.target, impact.reason)
      markImpactPassive(impact)

  for each conflict in graph.conflicts:
      if conflict.confirmed_target_status == confirmed:
          markConflict(card, conflict.target)
          markConflict(conflict.target, card)
          createActiveConflictLink(card, conflict.target)

  archiveCandidateGraph(card)
  keepPassiveImpactLinks(card)
  keepActiveConflictLinks(card)

  commit transaction

recheck(card):
  graph = computeConflictsAgainstActiveAndReanalysisLinks(card)
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

**Après validation : les impacts appliqués sortent du graphe actif et restent en audit passif.**

**Après validation : les conflits confirmés restent actifs jusqu’à résolution ou réanalyse validée.**
