# Devoir de conseil et objectivité — ancrage déontologique de la cage

Ce document ancre le comportement de la cage dans les règles professionnelles
de l'architecte. Il n'est pas un avis juridique : il énonce les règles **par
leur substance**, avec une référence stable. Le code de déontologie a été
**recodifié le 1er juillet 2026** (décret n° 2026-568) ; un seul numéro d'article
a pu être rattaché de façon fiable en session (**article 23**, ci-dessous), les
autres restent cités par substance.

> ⚠️ **À confirmer sur le texte officiel** : les numéros d'articles du nouveau
> code sont issus de **synthèses secondaires** (l'accès direct à Légifrance/CNOA
> renvoie 403 en session). L'article 23 est le mieux étayé ; les autres règles
> restent volontairement citées **sans numéro**. Vérifier avant toute citation
> article par article.

## Référence

- **Code de déontologie des architectes** — décret n° 2026-568 du 26 juin 2026
  (JO du 30 juin 2026, en vigueur le 1er juillet 2026) :
  [Légifrance (décret)](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054341539),
  [Ordre des architectes — ce qui change](https://www.architectes.org/actualites/code-de-deontologie-des-architectes-independance-formation-conflits-dinterets-ce-qui).
  Article 23 (objectivité + motivation dans les missions de contrôle/conseil/
  jugement) rattaché en session ; autres numéros à confirmer.
- **MAF (Mutuelle des Architectes Français)** — recommandations de prévention :
  - [Devoir de conseil : 9 recommandations pour sécuriser le choix de l'entreprise](https://www.maf.fr/actualite/boite-outils-chantiers-devoir-de-conseil-9-recommandations-pour-securiser-le-choix-de)
  - [Travaux sur existants : la responsabilité des maîtres d'œuvre en 12 recommandations](https://www.maf.fr/actualite/travaux-sur-existants-la-responsabilite-des-maitres-doeuvre-en-12-recommandations)
  - [Bien comprendre le devoir de conseil](https://www.maf.fr/actualite/bien-comprendre-le-devoir-de-conseil)

## Les règles, par leur substance

1. **Objectivité et impartialité.** Lorsqu'il donne son avis sur la proposition
   d'un entrepreneur, sur un document contractuel liant le maître d'ouvrage à un
   entrepreneur ou un fournisseur, ou lorsqu'il apprécie la compétence, la
   qualité d'une entreprise ou l'exécution de ses ouvrages, l'architecte fait
   preuve d'**objectivité et d'impartialité** (formulation du code recodifié
   2026). *C'est le nom déontologique de la règle de la cage* `retrieved != truth`
   / `citation présente != conclusion validée` : la cage restitue, elle ne
   tranche pas.

2. **Missions de contrôle, de conseil ou de jugement — article 23.** Dans ses
   missions de contrôle, de conseil ou de jugement, l'architecte fait preuve
   d'objectivité ; ses décisions, avis ou jugements sont **motivés et formulés
   avec clarté**, leur auteur s'affranchissant de ses conceptions personnelles.
   C'est l'ancrage le plus direct de la posture de la cage : elle **ne rend
   jamais un avis non motivé ni non tracé** — elle émet un candidat écrit +
   evidence pack, et un refus porte toujours son motif. *(Numéro d'article
   fiable en session ; à confirmer sur Légifrance.)*

3. **Devoir de conseil, continu.** Pendant toute la durée de son contrat,
   l'architecte apporte à son client son savoir et son expérience sur tous les
   aspects du projet. La cage soutient ce conseil en produisant un candidat
   tracé, jamais une conclusion assurée à la place de l'humain.

4. **Convention écrite préalable.** Tout engagement professionnel fait l'objet
   d'une convention écrite préalable (nature, étendue, rémunération). Côté cage,
   le `task_contract` joue ce rôle de périmètre déclaré : hors de lui, la cage
   refuse (élargir le périmètre est une révision de contrat, pas une décision du
   runner).

5. **Un avis (surtout négatif) se motive par écrit** (MAF). La preuve que le
   devoir de conseil a été rempli est l'écrit. La cage ne produit donc jamais un
   avis oral non tracé : elle émet un candidat écrit + evidence pack, et un refus
   porte toujours un motif.

6. **Vérifications sur l'entreprise** (MAF, 9 recommandations) : assurance
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
