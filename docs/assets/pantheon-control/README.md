# Pantheon Control — orientation externe

Statut : **point d’orientation documentaire / non-runtime**, avec un preview Hermès synthétique conservé séparément.

Ce répertoire ne contient plus de dashboard Pantheon Next. Le cockpit, ses renderers, ses données synthétiques de projet et ses scénarios de démonstration sont portés par le dépôt externe :

```text
ifanjuang/pantheon-mvp
mvp_vertical/cockpit/
```

Point public ciblé :

```text
https://ifanjuang.github.io/pantheon-mvp/
```

Révision externe observée lors de ce nettoyage :

```text
7f3faf74afd59a07a9ab6026360881eb374df905
```

## Contenu conservé ici

```text
README.md                 -> explique la frontière et le statut
index.html                -> conserve un lien stable vers le cockpit MVP externe
hermes-modules.html       -> preview synthétique du renderer du plugin dashboard Hermès
hermes-modules-demo.json  -> fixture explicitement fictive du preview Hermès
hermes-preview/           -> bundle statique du preview Hermès, couvert par les tests protégés
card_revision_proposal_lifecycle.md
                           -> spécification de gouvernance encore référencée par le modèle Work Issue
```

Le preview Hermès n’est pas le dashboard Pantheon Control. Il montre le renderer d’un plugin externe avec données fictives et mutations désactivées. Sa conservation ne prouve ni installation, ni activation, ni inventaire runtime réel.

La spécification de cycle de révision reste temporairement à son chemin historique parce qu’un document de gouvernance actif la référence. Elle est conservée pour éviter une perte de doctrine ; son futur déplacement devra mettre à jour le propriétaire actif dans le même changement.

Tous les autres HTML, JavaScript, CSS, fixtures et renderers de l’ancien dashboard local ont été retirés du working tree. Ils restent consultables dans l’historique Git, mais ne constituent plus une surface active, un prototype canonique ou une implémentation de secours.

## Responsabilités

```text
Pantheon Next -> gouverne les contrats, statuts, preuves, gates et décisions.
pantheon-mvp  -> porte l’implémentation candidate, le cockpit et les démos projet.
OpenWebUI     -> expose la surface opérationnelle lorsqu’elle est installée.
Hermes        -> exécute les handoffs autorisés et porte son dashboard natif.
Humain        -> approuve adoption, activation et action conséquente.
```

## Limites

```text
public demo != live cockpit
synthetic Hermes preview != installed Hermes dashboard
external implementation != adoption
installed != approved
healthy != safe
runtime_success != Evidence
```
