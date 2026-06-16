# Points de contrôle — scénarios métier détaillés — passe 2

Statut : **documenté non implémenté**. Complément au draft `evidence_scenarios_draft.md`.

Objet : préparer une future intégration dans `evidence.html` avec des projets crédibles, lisibles et contrôlables. Ces fiches restent fictives. Elles ne valident pas une règle, ne remplacent pas une consultation technique, ne créent pas de registre probatoire et ne produisent aucun effet externe.

## Ce que cette passe ajoute

- Un cadrage par projet : phase, contexte, intervenants, tension principale.
- Une sélection de 4 à 5 fiches intégrables par projet.
- Des manques précis pour le bouton `Recherche+`.
- Une logique de dépendance plus exploitable en mode dézoom.
- Une séparation entre source forte, source candidate, hypothèse et contradiction.

## Taxonomie courte des sources

| Force | Usage dans une fiche |
|---|---|
| Officielle | arrêté, autorisation, règlement, avis ABF, règlement PPRI, courrier mairie |
| Signée | contrat, devis signé, avenant, OS, PV, réception |
| Indicée | plan, notice, CCTP, rapport, étude, PDF avec date et indice |
| Reçue | email, courrier, compte rendu reçu, transmission entreprise |
| Technique | rapport BET, étude de sol, note CVC, diagnostic pathologie, note de bureau de contrôle |
| Interne | note agence, hypothèse de conception, synthèse de réunion |
| IA / extraction | extraction RAG ou synthèse automatique, toujours candidate |
| Hypothèse | déduction plausible non confirmée |

## Projet A — Clinique esthétique en secteur ABF

Phase : **Conception · APS / programme médical à stabiliser**.

Contexte : un projet de transformation d’un plateau existant en clinique esthétique glisse progressivement vers un programme technique plus lourd : demande de locaux ISO 4, sas, salle interventionnelle, local technique, équipements CVC, table ou équipement lourd. Le bâtiment est en secteur ABF, les façades sont sensibles, les hauteurs sous plafond sont faibles et l’étage inférieur contient des moulures que le client souhaite conserver.

Intervenants : architecte, client exploitant, hygiéniste ou conseil médical, BET CVC, BET structure, bureau de contrôle, ABF, autorité sanitaire à qualifier selon l’activité réelle.

### Fiches retenues pour intégration

#### MED-001 — Qualification réelle de la demande ISO 4

Statut : Contradictoire. Risque : Critique. Décideur attendu : client exploitant + hygiéniste + BET CVC.

Sources à rattacher :

- Email client demandant ISO 4 — force reçue — statut brut.
- Note programme initial — force indicée — statut vérifiée si signée ou validée.
- Extraction ISO 14644-1 — force IA / extraction ou référence — statut candidate à vérifier.

Établi : le client demande un niveau de propreté très supérieur au programme initial.

Incertain : la demande relève-t-elle d’une salle propre ISO, d’une salle interventionnelle, d’un bloc opératoire, d’une salle de soins renforcée ou d’une exigence marketing mal formulée ?

Contradiction : le programme initial ne prévoyait pas les contraintes CVC, sas et maintenance associées.

Action : demander une note programme médical courte : acte pratiqué, temps de présence patient, niveau de propreté, sas, flux, nettoyage, maintenance, équipements.

Manque `Recherche+` : programme médical stabilisé, note hygiène, niveau ISO réellement exigé, mode d’exploitation.

Décision attendue : maintenir, abaisser ou abandonner la cible ISO 4 avant poursuite APS.

Dépendances : MED-002, MED-003, MED-004, MED-005.

#### MED-002 — Sas, flux et local technique créé par suppression d’une pièce

Statut : Décision attendue. Risque : Élevé. Décideur attendu : client + architecte + BET CVC.

Établi : une pièce fonctionnelle est supprimée pour devenir local technique.

Incertain : la perte programmatique, les accès maintenance et les flux propre / sale sont acceptables.

Action : produire un schéma très simple : patient, praticien, matériel propre, matériel sale, déchets, maintenance.

Manque `Recherche+` : plans avant / après, nomenclature pièces, principe de ventilation, accès maintenance, surfaces nettes restantes.

Décision attendue : confirmer le local technique, déplacer les équipements ou réduire l’ambition de la salle.

Dépendances : MED-001 en amont ; MED-004 en aval.

#### MED-003 — Équipements techniques visibles en secteur ABF

Statut : À vérifier. Risque : Élevé. Décideur attendu : architecte + ABF + BET CVC.

Établi : la demande CVC peut entraîner des équipements visibles en façade, cour, toiture ou combles.

Incertain : les équipements sont-ils visibles depuis l’espace public ou modifient-ils l’aspect extérieur ?

Action : produire trois scénarios : invisible intérieur, cour intégrée, toiture / façade avec habillage. Ne pas promettre la solution sans avis ABF.

Manque `Recherche+` : repérage ABF, façades concernées, photos, gabarits équipements, bruit, rejet air, maintenance.

Décision attendue : retenir un système compatible avec le secteur patrimonial ou revoir le programme.

Dépendances : MED-001, MED-004.

#### MED-004 — Faible hauteur sous plafond et faisabilité CVC

Statut : Bloquant potentiel. Risque : Critique. Décideur attendu : BET CVC + architecte + bureau de contrôle.

Établi : la hauteur sous plafond est faible.

Incertain : réseaux, filtration, reprise, soufflage, trappes, maintenance et hauteur libre finale tiennent-ils réellement ?

Action : produire une coupe technique critique avant validation APS : plafond existant, faux plafond, réseaux, filtres, luminaires, passage, maintenance.

Manque `Recherche+` : relevé altimétrique précis, encombrements CVC, principe de filtration, hauteur libre exigée.

Décision attendue : accepter perte de hauteur, déplacer équipements, changer de système ou revoir le programme.

Dépendances : MED-002, MED-003, MED-005.

#### MED-005 — Charges d’équipements, table lourde et moulures conservées

Statut : Contradictoire. Risque : Critique. Décideur attendu : BET structure + client.

Établi : une table ou un équipement lourd est envisagé au-dessus d’un niveau dont les moulures doivent être conservées.

Incertain : poids, charges dynamiques, fixations, renforts et interventions par dessous.

Contradiction : le client demande consolidation, mais la consolidation par le dessous peut être incompatible avec les moulures à conserver.

Action : demander fiches techniques équipements : marque, modèle, poids, appuis, charges dynamiques, réservations, vibrations.

Manque `Recherche+` : fiches techniques, diagnostic plancher, charges admissibles, relevé moulures, scénario de renfort.

Décision attendue : déplacer équipement, limiter charge, renforcer par le dessus, ou déclarer l’option non faisable dans l’état.

Dépendances : MED-001, MED-004, MED-006.

#### MED-006 — Sommeil, sédation, réveil ou surveillance prolongée

Statut : À qualifier. Risque : Critique. Décideur attendu : client exploitant + bureau de contrôle + prévention incendie.

Établi : le client emploie un vocabulaire proche de salle opératoire.

Incertain : l’activité comporte-t-elle des patients endormis, sédatés, en réveil ou surveillés plus longtemps qu’un acte courant ?

Action : poser une question fermée dans le programme : sommeil ? sédation ? réveil ? lits ? surveillance prolongée ? hospitalisation de jour ?

Manque `Recherche+` : programme d’exploitation, avis bureau de contrôle, qualification ERP éventuelle.

Décision attendue : qualifier le type d’activité avant toute synthèse réglementaire.

Dépendances : MED-001, MED-005.

## Projet B — École en pisé

Phase : **Concours / APS · stratégie constructive**.

Contexte : la maîtrise d’ouvrage souhaite une école bas carbone en pisé. Le sujet doit rester professionnel : le pisé peut être porteur, remplissage ou démonstrateur. Les questions critiques sont l’eau, le feu, l’assurance, les entreprises disponibles, le planning et la maintenance.

### Fiches retenues pour intégration

#### PISE-001 — Rôle du pisé : porteur, remplissage ou parement pédagogique

Statut : Décision attendue. Risque : Élevé. Décideur attendu : MOA + BET structure + bureau de contrôle.

Action : dissocier l’image du matériau de son rôle constructif.

Manque `Recherche+` : principe structure, retour bureau de contrôle, références entreprise.

Décision attendue : pisé porteur, non porteur ou limité à des zones démonstratrices.

#### PISE-002 — Eau, pied de mur et protection de la terre crue

Statut : À vérifier. Risque : Critique. Décideur attendu : architecte + entreprise terre crue.

Action : produire détails pied de mur, soubassement, tête de mur, baie, ruissellement, seuil extérieur.

Manque `Recherche+` : carnet de détails, stratégie entretien, avis entreprise spécialisée.

Décision attendue : valider ou réduire l’usage du pisé en zones exposées.

#### PISE-003 — ERP scolaire, feu et justification du complexe

Statut : À vérifier. Risque : Élevé. Décideur attendu : bureau de contrôle + prévention incendie.

Action : demander la stratégie de preuve feu attendue avant APD.

Manque `Recherche+` : réaction / résistance feu du complexe, avis bureau de contrôle, documentation technique.

Décision attendue : maintenir, hybrider ou limiter le système.

#### PISE-004 — Planning, séchage, météo et chantier scolaire

Statut : Bloquant potentiel. Risque : Moyen. Décideur attendu : OPC + entreprise.

Action : intégrer les contraintes météo, protection provisoire et cadence de mise en œuvre.

Manque `Recherche+` : méthode entreprise, planning séchage, protections, période d’intervention.

Décision attendue : valider planning ou basculer en solution mixte.

#### PISE-005 — Assurabilité et disponibilité des entreprises

Statut : Décision attendue. Risque : Élevé. Décideur attendu : MOA + économiste + assureur.

Action : identifier les entreprises capables et leur assurabilité.

Manque `Recherche+` : retours entreprises, assurances, références comparables.

Décision attendue : maintenir ou réduire le pisé.

## Projet C — Médiathèque bois et IT 249

Phase : **APD · sécurité incendie façade**.

Contexte : médiathèque ERP avec structure et façade bois. Le point majeur est la propagation du feu par façade : règle C + D, vides, lame d’air, recoupements, réaction au feu, cohérence avec l’image architecturale.

### Fiches retenues pour intégration

#### MEDI-001 — Façade bois et IT 249

Statut : À vérifier. Risque : Critique. Décideur attendu : bureau de contrôle + BET façade.

Action : produire une coupe façade incendie avec composition complète.

Manque `Recherche+` : coupe façade, C + D, isolant, lame d’air, recoupements, justification.

Décision attendue : confirmer, modifier ou abandonner le complexe façade.

#### MEDI-002 — Recoupements invisibles et dessin architectural

Statut : Décision attendue. Risque : Élevé. Décideur attendu : architecte + bureau de contrôle.

Action : intégrer les recoupements au dessin au lieu de les découvrir en PRO.

Manque `Recherche+` : détails horizontaux / verticaux, trames, calepinage, baies.

Décision attendue : arbitrer continuité visuelle / sécurité.

#### MEDI-003 — Accès pompiers et parvis public

Statut : À vérifier. Risque : Élevé. Décideur attendu : prévention incendie + paysagiste + architecte.

Action : superposer voie engin, mobilier, plantations, portance, giration.

Manque `Recherche+` : plan pompier, coupe parvis, préavis prévention.

Décision attendue : modifier parvis ou valider accès.

#### MEDI-004 — Bois apparent intérieur, acoustique et feu

Statut : À vérifier. Risque : Moyen. Décideur attendu : architecte + acousticien + bureau de contrôle.

Action : faire une fiche matériau unique qui croise acoustique, feu, nettoyage et usage public.

Manque `Recherche+` : fiche produit, classement, traitement, maintenance.

Décision attendue : maintenir, limiter ou remplacer le bois apparent.

#### MEDI-005 — Budget façade bois et variantes

Statut : Décision attendue. Risque : Moyen. Décideur attendu : MOA + économiste.

Action : produire variantes chiffrées : bois complet, bois partiel, façade minérale.

Manque `Recherche+` : estimation et impact architectural.

Décision attendue : arbitrer budget / image / sécurité.

## Projet D — Logements en zone PPRI

Phase : **Faisabilité / PC · risque inondation**.

Contexte : projet de logements en zone de risque inondation. Les sujets critiques sont l’accès, le stationnement, le niveau plancher, les locaux techniques, les champs d’expansion, l’information client.

### Fiches retenues pour intégration

#### PPRI-001 — Accès à la parcelle et secours en crue

Statut : À vérifier. Risque : Critique. Décideur attendu : architecte + urbanisme + bureau hydraulique.

Action : vérifier zonage PPRI, cote de référence, accès secours, niveau de voirie.

Manque `Recherche+` : règlement PPRI, plan topo, coupe altimétrique.

Décision attendue : maintenir, déplacer ou refuser l’accès.

#### PPRI-002 — Stationnement et surfaces perméables

Statut : Décision attendue. Risque : Élevé. Décideur attendu : architecte + client + urbanisme.

Action : comparer stationnement perméable, réduit, déplacé ou mutualisé.

Manque `Recherche+` : PLU, PPRI, règle pleine terre, gestion EP.

Décision attendue : arbitrer nombre de places et traitement du sol.

#### PPRI-003 — Niveau plancher, seuils et locaux techniques

Statut : Bloquant potentiel. Risque : Critique. Décideur attendu : architecte + bureau hydraulique.

Action : dessiner coupe altimétrique avec cote PPRI et niveaux d’usage.

Manque `Recherche+` : relevé géomètre, cote de référence, prescriptions.

Décision attendue : modifier altimétrie ou programme.

#### PPRI-004 — Emprise bâtie et transparence hydraulique

Statut : À vérifier. Risque : Élevé. Décideur attendu : urbanisme + bureau hydraulique.

Action : vérifier si le projet aggrave l’écoulement ou réduit les zones d’expansion.

Manque `Recherche+` : note hydraulique ou préavis instructeur.

Décision attendue : adapter emprise, pilotis, vide sanitaire ou implantation.

#### PPRI-005 — Information client et responsabilité de poursuite

Statut : À faire. Risque : Élevé. Décideur attendu : architecte + client.

Action : produire note risque / prescription / limites avant poursuite.

Manque `Recherche+` : validation écrite client.

Décision attendue : poursuivre avec réserve ou modifier le programme.

## Projet E — Château en rénovation avec mérule

Phase : **Chantier · découverte pathologie après curage**.

Contexte : une rénovation de château ou grande demeure révèle une suspicion de mérule ou autre champignon lignivore. La fiche doit empêcher le réflexe dangereux : traiter localement sans comprendre l’eau, la ventilation, les bois porteurs et le patrimoine.

### Fiches retenues pour intégration

#### MER-001 — Découverte de mérule ou champignon lignivore

Statut : Bloquant. Risque : Critique. Décideur attendu : architecte + MOA + diagnostiqueur.

Action : stopper la zone, documenter, isoler, diagnostiquer.

Manque `Recherche+` : diagnostic fongique cartographié, photos, humidité.

Décision attendue : confirmer pathologie et périmètre de traitement.

#### MER-002 — Cause d’humidité non traitée

Statut : À vérifier. Risque : Critique. Décideur attendu : architecte + spécialiste ancien.

Action : chercher fuite, remontées, ventilation, couverture, drainage.

Manque `Recherche+` : diagnostic humidité et cause racine.

Décision attendue : traiter la cause avant finition.

#### MER-003 — Planchers bois et sécurité chantier

Statut : Bloquant potentiel. Risque : Critique. Décideur attendu : BET structure + SPS.

Action : sécuriser, étayer si besoin, limiter accès.

Manque `Recherche+` : sondages bois, avis structure, état porteur.

Décision attendue : renforcer, remplacer ou déposer.

#### MER-004 — Conservation patrimoniale ou purge

Statut : Décision attendue. Risque : Élevé. Décideur attendu : MOA + architecte + patrimoine.

Action : classer les éléments : conserver, traiter, déposer, remplacer.

Manque `Recherche+` : avis spécialiste bois / patrimoine.

Décision attendue : arbitrer conservation et sécurité.

#### MER-005 — Avenants, planning et information MOA

Statut : Décision attendue. Risque : Élevé. Décideur attendu : MOA + économiste + entreprises.

Action : état contradictoire, devis, planning révisé, notification.

Manque `Recherche+` : chiffrage, planning, impact lots.

Décision attendue : avenant, phasage ou suspension partielle.

## Projet F — Rénovation en chantier avec entreprise en dépôt de bilan

Phase : **Chantier · incident entreprise / reprise**.

Contexte : entreprise titulaire d’un lot important cesse d’intervenir. La difficulté est à la fois contractuelle, financière, technique et probatoire. L’interface doit aider à figer les faits avant toute reprise.

### Fiches retenues pour intégration

#### DEPOT-001 — Arrêt de chantier et procédure collective

Statut : Bloquant. Risque : Critique. Décideur attendu : MOA + architecte + conseil juridique.

Action : vérifier procédure officielle, mandataire, marché, paiements, situation de travaux.

Manque `Recherche+` : extrait procédure, mandataire, situation comptable.

Décision attendue : mise en demeure, déclaration de créance, résiliation ou reprise.

#### DEPOT-002 — Constat contradictoire d’avancement

Statut : À faire. Risque : Critique. Décideur attendu : architecte + MOA + commissaire de justice si nécessaire.

Action : constater avancement, qualité, réserves, trop-perçu, interfaces, protections.

Manque `Recherche+` : PV contradictoire, photos datées, état financier.

Décision attendue : figer la preuve avant consultation de reprise.

#### DEPOT-003 — Reprise par une nouvelle entreprise

Statut : Décision attendue. Risque : Élevé. Décideur attendu : MOA + architecte + économiste.

Action : consulter avec limites claires : existant, reprises, exclusions, garanties.

Manque `Recherche+` : devis de reprise, analyse technique, planning.

Décision attendue : choisir entreprise et stratégie financière.

#### DEPOT-004 — Interfaces et protection des ouvrages

Statut : À vérifier. Risque : Élevé. Décideur attendu : architecte + OPC + entreprises restantes.

Action : cartographier ce qui bloque les autres lots et ce qui risque de se dégrader.

Manque `Recherche+` : planning révisé, protections provisoires, interfaces.

Décision attendue : suspendre certains lots ou réordonner le chantier.

#### DEPOT-005 — Assurances, garanties et information client

Statut : À vérifier. Risque : Élevé. Décideur attendu : MOA + architecte + conseil assurance.

Action : réunir attestations, marchés, factures, CR, photos et échanges.

Manque `Recherche+` : analyse juridique / assurance.

Décision attendue : notifier, déclarer ou engager la procédure adaptée.

## Priorité d’intégration dans `evidence.html`

1. Ajouter deux nouveaux projets visibles d’abord : `Clinique ABF` et `Rénovation chantier — dépôt de bilan`.
2. Ajouter ensuite `Médiathèque bois IT 249` et `Logements PPRI`.
3. Garder `École pisé` et `Château mérule` comme deuxième lot pour éviter de surcharger la maquette.
4. Limiter chaque projet affiché à 4 ou 5 fiches dans la vue dézoom.

## Contrôle de crédibilité avant promotion

Avant toute promotion de ces scénarios vers un pack métier ou une base de connaissance :

- vérifier chaque source réglementaire dans sa version active ;
- distinguer norme, règlement, guide, avis technique et hypothèse agence ;
- remplacer les sources fictives par des chemins réels ;
- ajouter les décideurs réels ;
- ne jamais laisser une extraction IA devenir une source forte.
