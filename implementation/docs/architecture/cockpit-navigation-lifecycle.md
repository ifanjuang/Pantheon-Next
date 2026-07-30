# Cockpit — cycle de vie de la navigation et des projections

Ce document décrit le noyau de navigation du Cockpit. Il s'applique aux deux
surfaces : la démonstration (univers fictif, `demo-data.json`) et le chemin live
(renderer schématisé).

## Principe

L'état métier est **indépendant du moteur d'animation**. Swiper n'est qu'un
adaptateur de mouvement, confiné dans un seul module et remplaçable.

```
SnapshotProvider ─► CockpitSnapshot ─► NavigationState ─► CollectionController ─► CardHost ─► MotionAdapter
   (source)            (contrat)         (état pur)           (liaison)            (DOM)      (mouvement)
```

## Une seule forme d'entrée : `CockpitSnapshot`

```text
DemoProvider ─┐
              ├→ CockpitSnapshot → même Cockpit
LiveProvider ─┘
```

`v3/collection/cockpit_snapshot.js` définit le contrat versionné
(`cockpit.snapshot.v1`) que le Cockpit consomme, quelle qu'en soit la source —
fixture de démonstration, renderer live, ou un futur point d'entrée serveur :

```text
{ snapshot_version, generated_at, revision, source,
  space, collection, items, navigation, warnings }
```

Règles :

- **refus explicite** — une version inconnue, un payload non-objet, des `items`
  invalides ou une carte **sans identité stable** sont refusés. Le refus reste
  visible (`Projection refusée (raison)`) ; il n'est jamais dégradé en collection
  vide ni en succès silencieux ;
- `actions` et `schemas` sont **réservés au serveur** : transportés tels quels,
  jamais interprétés ici. Le Cockpit affiche ce qu'un serveur expose, il ne
  décide pas de ce qui est autorisé (`visible != authorized`) ;
- `generated_at` et `revision` portent la fraîcheur de la projection.

Les deux producteurs vivent dans `v3/providers/` (`demo_provider.js`,
`live_provider.js`) et ne font que projeter : ils ne récupèrent, ne décident et
n'autorisent rien.

- **NavigationState** (`v3/collection/navigation_state.js`) — données pures, sans
  DOM ni Swiper, testables sans navigateur :

  ```text
  { spaceId, collectionId, activeEntityId, activeIndex, path, face, overlay }
  ```

  La collection entière y vit **en données**. Le nombre de projections montées
  est une décision de présentation, pas d'état.

- **CollectionProvider** (`collection_provider.js`) — applique une source à
  l'état. Un **tableau déjà résident est appliqué d'un coup** ; seul un vrai
  `AsyncIterable` est consommé progressivement. Pas de faux streaming par frame.

- **CollectionController** (`collection_controller.js`) — relie état, source et
  mouvement. Le reste du Cockpit lui parle ; il ne fuit aucune API Swiper.

- **Renderer** (`card_renderer.js`) — fonctions DOM pures.

- **MotionAdapter** (`motion_adapter.js`) — **seul module qui connaît Swiper**.
  Surface volontairement réduite :

  ```text
  mount() · goTo(index) · lock() · unlock() · dispose()
  ```

  `appendSlide()`, `removeAllSlides()` et `updateSlides()` restent internes.

## Une fenêtre bornée, pas la collection entière

Seule une tranche glissante de la collection existe dans le DOM (slides
virtuelles de Swiper, `addSlidesBefore/After: 1`, `cache: false`) :

```text
… | previous | active | next | …
```

- la carte active est complète et interactive ;
- les voisines sont des aperçus légers et inertes ;
- tout le reste demeure **des données** dans `NavigationState` ;
- les slides sont recyclées pendant la navigation.

**Mesuré** (Chromium, viewport 390×844, collection de 43 éléments) : la fenêtre
DOM plafonne à **5 slides** et ne croît pas avec la collection — elle reste
identique aux index 1, 5, 9 et 13. C'est la propriété qui compte : le DOM est
**borné et indépendant de la taille de la collection**, pas égal à un chiffre
précis. La valeur exacte dépend de la façon dont Swiper calcule sa fenêtre.

Cela réduit les nœuds DOM, les écouteurs, les formulaires cachés, les calculs de
layout, la mémoire mobile et les risques de collision d'identifiants.

### Contrat d'affichage préservé

Le comportement visible reste celui attendu :

1. la slide synthétique **`New`** est en tête (index 0) pour les collections
   créables ;
2. la première carte visible est un **placeholder** tant que rien n'est arrivé ;
3. son contenu est **remplacé** par la première fiche ;
4. les fiches suivantes apparaissent au fur et à mesure du chargement.

Seule la stratégie DOM change : on ne matérialise plus une slide par élément.

## Deux axes de la démonstration

`level_controller.js` est **transitoire** : c'est la présentation deux axes de la
démo, pas la cible générale. Trois hôtes de niveau (parent · courant · enfant)
sont recyclés en place ; l'hôte courant possède l'unique `CollectionController`
horizontal et n'est jamais reconstruit. Une projection desktop maître/détail le
remplacerait sans toucher à l'état.

## Chemin live

Le renderer live (`v2_app_schema.js`) détient déjà toute la fratrie. Il la
**présente comme données** à l'adaptateur `v3_swiper.js`, qui n'en monte que
trois projections.

Invariant conservé : **une seule `.v2-card` interactive** (la projection active) ;
les voisines sont des aperçus inertes `.v2-card-preview`, pour que
`#v2-stage .v2-card` continue de désigner la carte active ciblée par les modules
historiques. Leur migration vers un registre d'hôtes explicite
(`cardRegistry.getActiveHost()`) est une étape séparée.

## Config Swiper

Les défauts de Swiper sont utilisés pour **tout**, y compris `speed`. Une seule
surcharge subsiste (`motion_adapter.js`, `BASE_OPTIONS`) :

- `noSwipingSelector` — un glissement démarré dans un contrôle de formulaire
  doit interagir avec ce contrôle, pas faire défiler le deck.

Cette exception n'est pas cosmétique : mesurée dans Chromium, sa suppression
fait passer le deck de la carte 0 à la carte 1 quand on glisse dans un champ de
texte, rendant la sélection impossible. Le cockpit live rend ses éditeurs à
l'intérieur des cartes, donc elle reste.

Deux surcharges antérieures ont été retirées après mesure :

| option | défaut | pourquoi retirée |
|---|---|---|
| `roundLengths` | `false` | aucun effet mesuré : une slide par vue à pleine largeur donne déjà des entiers (393 px à 393 px) |
| `touchReleaseOnEdges` | `false` | rend le geste à un parent défilable aux extrémités ; ici la page est fixe (`touch-action: none`), il n'y a rien à qui le rendre |

Sur la vitesse : `followFinger` étant actif par défaut, la carte suit le doigt
pendant le geste — `speed` ne gouverne que le calage après relâchement (300 ms).
La surdéfinir ne rendrait pas le swipe plus rapide.

Le Swiper imbriqué (horizontal dans le deck vertical) reçoit `nested: true`,
conformément à l'API.

## Budgets

Vérifiés statiquement par `tests/test_cockpit_v3_lifecycle.py` :

```text
modules construisant Swiper         = 1 (MotionAdapter)
appels slide API hors adaptateur    = 0
fenêtre DOM                         bornée (virtual + cache: false)
faux streaming d'un tableau         = aucun
```

`NavigationState` (`tests/test_cockpit_navigation_state.py`) et
`CockpitSnapshot` (`tests/test_cockpit_snapshot_contract.py`) sont en plus
exercés réellement, sans navigateur.

## Vérification navigateur

Ces tests sont statiques ou sans DOM : ils ne prouvent pas le rendu. Une
vérification a été menée dans Chromium (Playwright, viewport 390×844, tactile
activé), Swiper `14.0.7` servi localement — le CDN étant inaccessible depuis
l'environnement d'exécution.

Constaté :

```text
démarrage                     cartes rendues, aucune erreur JS
swipe horizontal réel         change la carte active
descente de niveau            fil d'Ariane « Pantheon / Décisions »
fenêtre DOM (43 éléments)     5 slides, stable aux index 1 · 5 · 9 · 13
requêtes en échec             aucune (hors /favicon.ico du navigateur)
```

Deux défauts ont été trouvés ainsi, invisibles pour `node --check` et pour les
tests de contrat :

1. les points de montage `.v3-level-host` / `.v3-collection-host` n'avaient
   aucune règle CSS — la largeur partait à 2²⁵ px et **plus rien ne bougeait** ;
2. le wrapper avait perdu la classe `v2-swiper-wrapper` que cible la géométrie.

**Limite** : la barre de navigation étant masquée sur mobile, les contrôles
`#v2-previous/#v2-next/#v2-descend` ont été pilotés par script pour certaines
étapes ; le geste horizontal, lui, a été rejoué réellement. Le rendu visuel
(matières, animations, safe areas iOS) n'est pas couvert.

## Suite prévue

```text
snapshot émis par le serveur → registre de cartes schema-driven →
migration des sélecteurs .v2-card vers un registre d'hôtes →
invalidation incrémentale
```

Contrat d'actions, autorisations, conflits de révision et politique de fraîcheur
sont des contrats **serveur** : le Cockpit les consomme, il ne les invente pas.
Aujourd'hui les deux providers construisent le snapshot côté client ; l'étape
suivante est qu'un point d'entrée serveur émette directement
`cockpit.snapshot.v1`, sans changer ce que le Cockpit consomme.

## Frontière

Ceci ne change que la mécanique de rendu et de navigation. Aucune autorité de
gouvernance, Evidence, approbation, autorisation de tâche ou vérité serveur n'est
affectée.

```text
projection montée != état gouverné validé
projection != source de vérité
transition UI != autorisation
visible != authorized
runtime success != Evidence
```
