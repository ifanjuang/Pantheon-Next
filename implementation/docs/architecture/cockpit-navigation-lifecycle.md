# Cockpit — cycle de vie de la navigation et des projections

Status: active implementation support — current Cockpit navigation contract.

Ce document décrit la mécanique actuelle du Cockpit dans `pantheon-mvp`. Il ne définit aucune autorité métier, aucun statut de vérité et aucune autorisation d’action.

## Principe

L’état projeté reste indépendant du moteur d’animation :

```text
SnapshotProvider
→ CockpitSnapshot
→ NavigationState
→ CollectionController
→ Card renderer
→ MotionAdapter
```

Swiper est un adaptateur de mouvement remplaçable. Il ne possède ni la collection, ni l’identité des cartes, ni la navigation métier.

## Contrat unique : CockpitSnapshot

Le contrat est défini dans :

```text
mvp_vertical/cockpit/collection/cockpit_snapshot.js
```

Les producteurs actuels sont :

```text
mvp_vertical/cockpit/providers/demo_provider.js
mvp_vertical/cockpit/providers/live_provider.js
```

Ils produisent la même forme :

```text
{
  schema: {
    id: "cockpit.snapshot",
    revision: 1
  },
  generated_at,
  revision,
  source,
  space,
  collection,
  items,
  navigation,
  warnings
}
```

Deux révisions distinctes sont conservées :

- `schema.revision` : révision technique du contrat de projection ;
- `revision` : révision éventuelle des données projetées.

```text
schema revision != product generation
projection revision != authority status
```

Une projection dont l’identifiant ou la révision de schéma ne sont pas reconnus est refusée explicitement. Il n’existe pas de conversion silencieuse vers une collection vide ni d’ancien format maintenu en parallèle.

Les champs `actions` et `schemas` peuvent être transportés, mais ils restent définis par le serveur. Le navigateur ne les transforme pas en autorisation.

```text
visible != authorized
projection received != action permitted
```

## État de navigation

`collection/navigation_state.js` conserve les données de navigation sans dépendre du DOM ni de Swiper :

```text
spaceId
collectionId
activeEntityId
activeIndex
path
face
overlay
```

La collection reste en données. Le nombre de cartes montées est une décision de présentation.

`collection/collection_provider.js` accepte :

- un tableau déjà résident, appliqué directement ;
- un véritable `AsyncIterable`, consommé progressivement.

Un tableau n’est pas artificiellement transformé en flux image par image.

## Contrôleur et mouvement

`collection/collection_controller.js` relie l’état, la source et le mouvement.

`collection/motion_adapter.js` est le seul propriétaire de l’instance Swiper et de ses appels de navigation. Sa surface reste bornée :

```text
mount()
goTo(index)
lock()
unlock()
dispose()
```

Les autres modules ne doivent pas appeler directement :

```text
appendSlide
removeAllSlides
updateSlides
slideTo
slidePrev
slideNext
```

## Fenêtre DOM bornée

Le Cockpit utilise les slides virtuelles de Swiper avec cache désactivé et une fenêtre réduite autour de la carte active.

```text
… | précédente | active | suivante | …
```

La collection entière reste disponible dans l’état, mais elle n’est pas intégralement matérialisée dans le DOM.

Cette séparation réduit :

- les nœuds et écouteurs résidents ;
- les formulaires masqués ;
- les collisions d’identifiants ;
- les recalculs de layout ;
- la consommation mémoire mobile.

La propriété recherchée est une fenêtre bornée, indépendante de la taille totale de la collection. Le nombre exact de slides peut varier selon le calcul interne de Swiper.

## Chemins live et démonstration

Le démarrage commun est assuré par :

```text
cockpit_bootstrap.js
→ live_bootstrap.js
```

Le mode démonstration ajoute `demo_bootstrap.js`, puis utilise les mêmes contrats de snapshot, de collection, de navigation et de rendu que le chemin live.

Le chemin live passe par :

```text
providers/live_provider.js
→ live_collection_adapter.js
→ collection/collection_controller.js
→ collection/motion_adapter.js
```

Le Cockpit ne déduit pas l’autorité depuis le mode `demo` ou `live`.

```text
demo data != Evidence
live projection != validated truth
UI mode != authorization
```

## Rendu et matériaux

Le rendu structurel des cartes appartient à :

```text
mvp_vertical/cockpit/rendering/card_renderer.js
```

Le registre de matériaux appartient à :

```text
mvp_vertical/cockpit/registries/materials.json
```

Son identité est stable :

```text
schema_id = cockpit.materials
revision = 1
```

Les matériaux sont des métadonnées de présentation. Ils ne représentent pas un statut, une sécurité, une approbation ou une autorisation de tâche.

## Compatibilité encore active

Certains sélecteurs CSS et identifiants DOM historiques commençant par `v2-` ou `v3-` restent consommés par les surfaces HTML, CSS et les tests de régression.

Ils constituent une dette de compatibilité à retirer par tranches prouvées. Ils ne doivent pas être utilisés pour nommer de nouveaux modules, contrats, routes ou documents.

Avant suppression d’un identifiant de compatibilité, vérifier :

```text
HTML
CSS
JavaScript classique
imports statiques et dynamiques
globals produits et consommés
tests
surfaces publiées
```

## Validation

Les contrats sont couverts notamment par :

```text
tests/test_cockpit_snapshot_contract.py
tests/test_cockpit_navigation_state.py
tests/test_cockpit_navigation_lifecycle.py   cible de renommage du test historique restant
```

Les contrôles vérifient :

- la lecture et le refus déterministes des snapshots ;
- la conservation d’une identité stable ;
- le confinement de Swiper dans `MotionAdapter` ;
- l’absence d’appels directs aux API de slides ;
- la fenêtre DOM bornée ;
- l’absence de faux streaming des tableaux ;
- l’isolation des chargements asynchrones annulés.

Les tests statiques ou Node ne remplacent pas une vérification visuelle dans un navigateur. Les matières, safe areas, gestes tactiles et animations restent des propriétés à vérifier sur la surface rendue.

## Prochaine convergence

```text
1. retirer les noms de génération des documents et tests restants
2. migrer les sélecteurs DOM historiques seulement avec leur graphe de consommation
3. faire émettre le snapshot par une projection serveur cohérente
4. conserver le navigateur comme consommateur, jamais comme autorité
```

## Frontières

```text
projection montée != état gouverné validé
projection != source de vérité
transition UI != autorisation
visible != authorized
runtime success != Evidence
```
