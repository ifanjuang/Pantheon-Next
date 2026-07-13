# Devoir de conseil et objectivité — ancrage déontologique de la cage

Ce document ancre le comportement de la cage dans les règles professionnelles
de l'architecte. Il n'est pas un avis juridique : il énonce les règles **par
leur substance**, avec une référence stable, et **sans numéro d'article** —
parce que le code de déontologie a été **recodifié le 1er juillet 2026** et que
les numéros exacts n'ont pas pu être confirmés sur le texte officiel dans cette
session (accès Légifrance/CNOA indisponible).

> ⚠️ **À confirmer** : les numéros d'articles du nouveau code
> (décret n° 2026-568 du 26 juin 2026) restent à vérifier sur le texte officiel
> avant toute citation article par article. Ne rien graver de plus précis que
> la substance ci-dessous sans cette vérification.

## Référence

- **Code de déontologie des architectes** — décret n° 2026-568 du 26 juin 2026
  (JO du 30 juin 2026, en vigueur le 1er juillet 2026). Numéros d'articles à
  confirmer.
- **MAF (Mutuelle des Architectes Français)** — recommandations de prévention :
  - [Devoir de conseil : 9 recommandations pour sécuriser le choix de l'entreprise](https://www.maf.fr/actualite/boite-outils-chantiers-devoir-de-conseil-9-recommandations-pour-securiser-le-choix-de)
  - [Travaux sur existants : la responsabilité des maîtres d'œuvre en 12 recommandations](https://www.maf.fr/actualite/travaux-sur-existants-la-responsabilite-des-maitres-doeuvre-en-12-recommandations)
  - [Bien comprendre le devoir de conseil](https://www.maf.fr/actualite/bien-comprendre-le-devoir-de-conseil)

## Les règles, par leur substance

1. **Objectivité et équité.** Lorsqu'il donne son avis sur la proposition d'une
   entreprise, sur un document contractuel liant le maître d'ouvrage à une
   entreprise ou un fournisseur, ou lorsqu'il apprécie la compétence, la qualité
   d'une entreprise ou l'exécution de ses ouvrages, l'architecte fait preuve
   d'objectivité et d'équité. *C'est le nom déontologique de la règle de la
   cage* `retrieved != truth` / `citation présente != conclusion validée` : la
   cage restitue, elle ne tranche pas.

2. **Devoir de conseil, continu.** Pendant toute la durée de son contrat,
   l'architecte apporte à son client son savoir et son expérience sur tous les
   aspects du projet. La cage soutient ce conseil en produisant un candidat
   tracé, jamais une conclusion asseurée à la place de l'humain.

3. **Convention écrite préalable.** Tout engagement professionnel fait l'objet
   d'une convention écrite préalable (nature, étendue, rémunération). Côté cage,
   le `task_contract` joue ce rôle de périmètre déclaré : hors de lui, la cage
   refuse (élargir le périmètre est une révision de contrat, pas une décision du
   runner).

4. **Un avis (surtout négatif) se motive par écrit** (MAF). La preuve que le
   devoir de conseil a été rempli est l'écrit. La cage ne produit donc jamais un
   avis oral non tracé : elle émet un candidat écrit + evidence pack, et un refus
   porte toujours un motif.

5. **Vérifications sur l'entreprise** (MAF, 9 recommandations) : assurance
   décennale / RC pro, qualifications métier, références, trésorerie. La cage
   **ne dispose d'aucune source** pour ces vérifications ; elle ne peut donc pas
   les affirmer faites. Elle les **signale** comme non établies (advisory),
   jamais comme validées :

       verified_here == false  (toujours, pour ces points)

## Ce que la cage fait — et ne fait pas

- Elle **signale** (advisory, non bloquant) quand un brouillon juge ou retient
  une entreprise, ou formule une qualification juridique — `duty_of_care_flags`
  et `professional_assertion_flags`. Ces signaux vont à l'humain.
- Elle **n'affirme jamais** qu'une entreprise est sérieuse/qualifiée/assurée, ni
  qu'une clause juridique est correcte. Ce jugement, motivé par écrit, reste la
  responsabilité du maître d'œuvre humain.
