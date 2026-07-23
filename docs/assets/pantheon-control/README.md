# Pantheon Control — orientation vers le cockpit MVP

Statut : **prototype statique historique / point d’entrée remplacé par un lien externe**.

`index.html` n’exécute plus le thème, les fixtures ni les renderers de l’ancienne maquette Pantheon Next. Il expose uniquement une page d’orientation vers le cockpit canonique porté par le dépôt externe `ifanjuang/pantheon-mvp`.

## Source canonique actuelle

La surface exécutable et sa démonstration sont maintenues dans :

```text
ifanjuang/pantheon-mvp
mvp_vertical/cockpit/
```

La démonstration no-network fusionnée par `pantheon-mvp#46` au commit `4ee41a845ec51db3118a584db0411a300450ccbd` charge directement :

```text
styles/index.css
app.js
resources.js
effects.js
knowledge_updates.js
```

Elle ajoute uniquement `demo.js`, qui fournit des projections synthétiques locales et bloque les appels réseau avant le chargement des scripts du cockpit.

## Ce qui reste dans ce répertoire

Les anciens fichiers HTML, JavaScript, CSS et fixtures restent des **assets historiques de prototype** tant qu’un nettoyage séparé ne les retire pas. Leur présence ne leur donne plus le rôle de démonstration canonique et ne prouve aucun runtime.

Le point d’entrée `index.html` ne les charge plus.

## Déploiement

Après installation séparée du runtime externe MVP, la démo pourra être servie à :

```text
/cockpit/demo.html
```

Aucune URL publique, installation, activation ou autorisation de production n’est créée par Pantheon Next.

```text
lien disponible != service déployé
prototype historique != cockpit canonique
static demo != live cockpit
implemented externally != adopted
runtime_success != Evidence
```
