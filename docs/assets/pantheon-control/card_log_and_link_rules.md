# Journal par fiche et règles de liens — addendum

Statut : **documenté non implémenté**. Addendum à `impact_conflict_lifecycle.md`.

Objet : préciser le journal de changement par fiche, le cas manuel `validée → candidate`, et la cardinalité des liens d’impact / conflit.

## 1. Journal par fiche

Chaque fiche doit avoir un journal propre, append-only.

Le journal ne remplace pas le statut courant. Il explique comment la fiche est arrivée à ce statut.

### Entrée minimale de log

```yaml
log_entry:
  at: 2026-06-17T14:30:00Z
  actor: human | system | ai_assistant | connector
  action: status_change | impact_applied | conflict_detected | conflict_confirmed | reanalysis_requested | source_added | manual_override
  from_status: confirmed
  to_status: needs_reanalysis
  reason: Nouvelle liste de sols confirmée avec option grande dalle non démontrée compatible support OSB.
  source_card: SOL-001
  target_card: SOL-002
  source_version: SEL-03
  evidence_refs:
    - sources/SOL-001_selection_recue.md
    - pdf/selection-sols-client_SEL-03.pdf
  human_confirmation: true
```

### Règles

- Toute modification de statut produit une entrée de log.
- Toute application d’impact produit une entrée sur la fiche source et sur la fiche cible.
- Toute création de conflit produit une entrée sur les deux fiches impliquées.
- Une analyse candidate produit un log uniquement sur la fiche candidate.
- Les fiches ciblées ne reçoivent aucun log tant que l’impact reste candidat.
- Un log ne déclenche jamais de nouvelle analyse par lui-même.

## 2. Cas manuel : fiche validée repassée en candidate

Un retour manuel de `confirmée` vers `candidate` doit rester exceptionnel.

Il ne doit pas être utilisé pour tout impact reçu.

Cas légitimes :

- la validation a été faite par erreur ;
- la source utilisée était mauvaise ;
- la fiche ne correspondait pas au bon projet ;
- la fiche validée mélangeait deux sujets ;
- une personne habilitée décide explicitement de rouvrir la fiche comme hypothèse non stabilisée.

Dans ce cas, le changement est un **manual override**.

### Effet sur les conflits liés

Si une fiche confirmée avec conflits actifs est manuellement repassée en candidate, les conflits liés ne doivent pas disparaître automatiquement.

Règle recommandée :

```text
confirmed + conflict_active → candidate + conflict_suspended
```

Sur les autres fiches liées :

```text
conflict_active → conflict_suspended_due_to_source_reopened
```

Donc :

- les conflits ne sont pas effacés ;
- ils deviennent suspendus ;
- ils restent visibles comme historique et périmètre de réanalyse ;
- ils ne sont plus actifs tant que la fiche source n’est pas reconfirmée.

### Pourquoi ne pas supprimer le conflit ?

Parce que supprimer le conflit ferait perdre le fait important : ces fiches ont déjà été jugées incompatibles sous une hypothèse précédente.

La bonne règle est :

```text
On suspend le conflit parce que l’une des hypothèses n’est plus confirmée.
On ne l’efface pas.
```

### Réactivation

Si la fiche candidate est reconfirmée avec la même hypothèse, le conflit peut redevenir actif après prévisualisation et confirmation humaine.

Si la fiche candidate est modifiée et que l’incompatibilité disparaît, le conflit suspendu peut passer en `resolved` après validation humaine.

## 3. Une fiche peut avoir plusieurs liens

Oui. Une fiche peut avoir plusieurs liens d’impact et plusieurs liens de conflit.

### Cardinalité

```text
one card → many impact links
one card → many conflict links
one card pair → at most one active conflict link per conflict reason / hypothesis version
```

Une fiche peut impacter plusieurs autres fiches : structure, estimatif, commande, planning, CCTP, accessibilité, sécurité.

Une fiche peut aussi être en conflit avec plusieurs fiches si plusieurs hypothèses confirmées ne peuvent pas coexister.

## 4. Un lien par fiche détectée ?

Oui, mais pas seulement par fiche. Il faut distinguer la cible et la raison.

Un lien doit être identifié par :

```text
source_card
source_version
target_card
relation_type
reason_key
hypothesis_id
```

Exemple :

```yaml
conflict_link:
  source_card: SOL-001
  source_version: SEL-03
  target_card: SOL-002
  relation_type: conflict
  reason_key: large_tile_on_osb_support
  hypothesis_id: H2_large_tile_osb
  state: active
```

Deux fiches peuvent avoir plusieurs tensions historiques, mais une seule relation active pour la même raison et la même hypothèse.

### Exemple acceptable

`SOL-001` peut avoir :

- impact vers `SOL-003 Estimatif` pour coût ;
- impact vers `CMD-003 Commande` pour blocage ;
- conflit avec `SOL-002 Structure` pour support incompatible ;
- tension avec `ACCESS-004 Seuils` pour hauteur finie.

Ce sont des liens distincts.

### Exemple à éviter

Créer cinq liens identiques entre `SOL-001` et `SOL-002` pour la même incompatibilité support.

Le bon comportement est de mettre à jour le lien existant : statut, date, source, niveau, commentaire, version.

## 5. Statuts de lien recommandés

### Impact link

```text
candidate
applied
closed
rejected
needs_reanalysis
```

### Conflict link

```text
potential
detected
active
suspended
resolved
rejected
```

`suspended` sert précisément au cas où une fiche confirmée redevient candidate.

## 6. Règle d’affichage UX

Sur une fiche, afficher séparément :

```text
Impacts sortants
Impacts reçus
Conflits actifs
Conflits suspendus
Historique
```

Ne pas mélanger tout dans une seule liste.

Une fiche confirmée peut donc afficher :

```text
Statut : confirmée
Impact : 2 impacts appliqués, 1 impact à réanalyser
Cohérence : 1 conflit actif, 1 conflit suspendu
```

## 7. Règle anti-boucle supplémentaire

Les logs et les liens ne déclenchent rien seuls.

Déclencheurs autorisés :

- validation humaine ;
- demande `Recherche+` ;
- demande de détail ;
- nouvelle source ;
- modification explicite ;
- réouverture manuelle ;
- résolution humaine d’un conflit.

Les éléments suivants ne déclenchent jamais automatiquement une cascade :

- ajout d’une entrée de log ;
- existence d’un lien passif ;
- existence d’un conflit suspendu ;
- impact déjà appliqué ;
- ancienne relation candidate archivée.

## 8. Réponse synthétique aux cas posés

### Faut-il un log par fiche ?

Oui. Append-only. Chaque changement daté, motivé, sourcé, avec acteur et confirmation humaine si applicable.

### Si une fiche confirmée repasse candidate manuellement, les conflits des autres fiches s’enlèvent-ils ?

Non. Ils ne s’effacent pas. Ils passent en `suspended_due_to_source_reopened` ou `suspended`.

Ils peuvent redevenir actifs si la fiche est reconfirmée avec la même hypothèse, ou être résolus si la nouvelle version supprime l’incompatibilité.

### Une fiche peut-elle avoir plusieurs liens d’impact ou conflit ?

Oui.

Une fiche peut avoir plusieurs impacts sortants, plusieurs impacts reçus, plusieurs conflits actifs ou suspendus.

Mais il faut éviter les doublons : un seul lien actif par couple `source / cible / raison / hypothèse`.
