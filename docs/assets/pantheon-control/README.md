# Pantheon Control — orientation externe

Statut : **point d’orientation documentaire / non-runtime**.

Ce répertoire ne contient plus de dashboard Pantheon Next. Le cockpit, ses renderers, ses données synthétiques et ses scénarios de démonstration sont portés par le dépôt externe :

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
README.md   -> explique la frontière et le statut
index.html  -> conserve un lien stable depuis Pantheon Next
```

Les anciens HTML, JavaScript, CSS, fixtures et renderers du dashboard local ont été retirés du working tree. Ils restent consultables dans l’historique Git, mais ne constituent plus une surface active, un prototype canonique ou une implémentation de secours.

## Responsabilités

```text
Pantheon Next -> gouverne les contrats, statuts, preuves, gates et décisions.
pantheon-mvp  -> porte l’implémentation candidate, le cockpit et les démos.
OpenWebUI     -> expose la surface opérationnelle lorsqu’elle est installée.
Hermes        -> exécute les handoffs autorisés.
Humain        -> approuve adoption, activation et action conséquente.
```

## Limites

```text
public demo != live cockpit
external implementation != adoption
installed != approved
healthy != safe
runtime_success != Evidence
```
