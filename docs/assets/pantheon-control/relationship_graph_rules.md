# Points de contrôle — règles de graphe relationnel

Statut : **documenté non implémenté**. Spécification candidate pour la maquette `evidence.html` et les futurs points de contrôle.

Objet : simplifier la logique entre fiches pour éviter les boucles, garder les décisions lisibles et permettre une revue globale par projet.

Cette règle ne crée pas de runtime. Pantheon gouverne les statuts, relations, notes, preuves et décisions. L’exécution éventuelle d’une vérification est demandée à un runtime externe sous contrat, par exemple Hermes.

## 1. Vocabulaire minimal

Utiliser trois types de relations, pas davantage.

### Dépendance

Une dépendance décrit un ordre logique, technique, documentaire ou temporel.

Elle ne dit pas qu’un problème existe.

Exemples :

- le couvreur dépend du maçon pour démarrer ;
- le plaquiste dépend de la couverture hors d’eau ;
- l’estimatif dépend de l’étude structure ;
- le dossier PC dépend de la qualification ERP ;
- le visa entreprise dépend d’une note de calcul.

### Impact

Un impact décrit un effet d’une fiche sur une autre.

Il peut changer un statut, demander une révision, bloquer une commande, demander un estimatif, ou ouvrir une version de réanalyse.

Un impact appliqué sort du graphe actif et devient trace passive.

### Cohérence

La cohérence dit si les fiches peuvent coexister.

Les états recommandés :

```text
coherent
watch
tension
conflict_potential
conflict_active
resolved
```

Le mot `conflit` est réservé aux cas où deux ou plusieurs hypothèses ne peuvent pas rester vraies ensemble sans arbitrage.

## 2. Les trois axes d’une fiche

Ne pas mettre toute l’information dans un seul statut.

Chaque fiche a au minimum :

```yaml
lifecycle_status: candidate | confirmed | archived | rejected
review_state: clean | to_check | to_revise | blocked | decision_expected
impact_state: none | candidate | applied | passive | needs_reanalysis
coherence_state: coherent | watch | tension | conflict_potential | conflict_active | resolved
```

Une fiche confirmée ne redevient pas candidate par propagation d’impact.

Si une nouvelle hypothèse l’affecte, elle devient plutôt :

```text
confirmée avec impact reçu
confirmée à réanalyser
confirmée avec révision candidate ouverte
confirmée en conflit actif
```

## 3. Activation manuelle

L’IA ne détectera pas tout.

L’utilisateur doit pouvoir créer manuellement :

- une dépendance ;
- un impact potentiel ;
- un impact confirmé ;
- une tension de cohérence ;
- un conflit potentiel ;
- un conflit actif ;
- une demande de réanalyse.

Chaque activation manuelle doit contenir une note.

Exemple :

```yaml
manual_relation:
  relation_type: impact
  source_card: SOL-001
  target_card: STRUCT-012
  state: candidate
  note: Grande dalle choisie par le client, support bois non démontré compatible par expérience chantier.
  actor: architecte
  date: 2026-06-17
```

Sans note, la relation reste invalide.

## 4. Notes obligatoires

Tout lien problématique doit avoir une note.

La note doit répondre à quatre questions :

```text
Pourquoi cette relation existe ?
Quelle hypothèse est concernée ?
Quel effet possible ou réel ?
Quelle vérification ou décision est attendue ?
```

Types de note recommandés :

```text
experience_note
technical_note
regulatory_note
budget_note
planning_note
client_decision_note
site_observation_note
ai_analysis_note
```

Une note IA reste candidate tant qu’elle n’est pas relue ou rattachée à une preuve.

## 5. Règle anti-boucle simple

Les seules opérations qui peuvent changer les autres fiches sont :

1. validation humaine d’une fiche candidate avec prévisualisation ;
2. validation humaine d’un conflit ou d’une résolution ;
3. modification manuelle explicite ;
4. décision humaine après revue globale.

Ne déclenchent jamais de propagation automatique :

- existence d’un lien ;
- ajout d’un log ;
- impact passif ;
- conflit potentiel ;
- conflit suspendu ;
- demande de détail ;
- analyse IA seule ;
- réanalyse globale seule.

Formule :

```text
analyser calcule.
prévisualiser avertit.
valider applique.
les liens mémorisent.
les conflits actifs attendent résolution.
```

## 6. Revue locale et revue globale

Il ne suffit pas de vérifier fiche par fiche.

Certains problèmes n’existent qu’à l’échelle de plusieurs fiches.

### Revue locale

Une revue locale part d’une fiche.

Elle vérifie :

- ses sources ;
- ses notes ;
- ses impacts sortants ;
- ses impacts reçus ;
- ses conflits ou tensions ;
- ses dépendances directes.

### Revue globale projet

Une revue globale part de toutes les fiches du projet.

Elle vérifie :

- dépendances circulaires ;
- contradictions multi-fiches ;
- impacts cumulés ;
- conflits latents ;
- décisions anciennes rendues hors hypothèse ;
- séquences chantier impossibles ;
- coût cumulé dépassant seuil ;
- changement de nature technique ;
- changement de programme ;
- incohérences entre notes utilisateur et statuts IA.

La revue globale peut produire une fiche spécifique de résolution.

## 7. Fiche de résolution

Quand un problème n’appartient pas clairement à une seule fiche, créer une fiche de résolution.

Nom recommandé :

```text
RES-XXX — Arbitrage relationnel
```

Elle sert à traiter un nœud de problème, pas à remplacer les fiches sources.

Elle contient :

- fiches impliquées ;
- dépendances concernées ;
- impacts concernés ;
- conflits ou tensions ;
- notes pertinentes ;
- scénarios de résolution ;
- décision attendue ;
- arbitrage retenu.

Exemple chantier :

```text
Maçon attend plaquiste.
Plaquiste doit passer après couvreur.
Couvreur ne commence pas avant maçon.
```

Ce n’est pas un problème de fiche isolée. C’est un cycle de dépendance chantier.

Le système doit créer ou proposer :

```text
RES-041 — Cycle de dépendance maçon / couvreur / plaquiste
```

Cette fiche demande un arbitrage : changer l’ordre, phaser, protéger provisoirement, modifier un lot ou convoquer les entreprises.

## 8. Relation cardinality

Une fiche peut avoir plusieurs relations.

```text
one card -> many dependencies
one card -> many impacts
one card -> many coherence links
```

Mais il faut éviter les doublons.

Un lien est unique par :

```text
source_card
target_card
relation_type
reason_key
hypothesis_id
source_version
```

Si la même relation réapparaît, on met à jour le lien existant : date, note, niveau, preuve, état.

On ne crée pas un doublon.

## 9. Etats des relations

### Dépendance

```text
candidate
confirmed
blocked
satisfied
obsolete
suspended
```

### Impact

```text
candidate
applied
passive
closed
rejected
needs_reanalysis
```

### Cohérence

```text
watch
tension
conflict_potential
conflict_active
suspended
resolved
rejected
```

## 10. Demande `Dépendants / vérifier`

Quand l’utilisateur demande une vérification des dépendants, Pantheon ne lance pas lui-même un runtime.

Il prépare une demande gouvernée pour l’exécution externe.

Forme logique :

```text
Task Contract
→ scope : projet entier ou sous-graphe
→ question : vérifier dépendances, impacts, cohérence
→ sources autorisées
→ notes utilisateur
→ seuils de détection
→ résultat attendu : Result Candidate + Evidence Pack Candidate
```

Le runtime externe, par exemple Hermes, exécute la vérification si autorisé.

Pantheon reçoit ensuite des candidats :

- relations candidates ;
- fiches problématiques ;
- proposition de fiche de résolution ;
- preuves ;
- notes à valider ;
- actions humaines attendues.

## 11. Algorithme de vérification globale

```text
verifyProjectGraph(project):
  cards = load_project_cards(project)
  relations = load_relations(project)
  notes = load_notes(project)

  graph = build_graph(cards, relations)

  local_findings = []
  for card in cards:
      local_findings += check_card(card, relations, notes)

  global_findings = []
  global_findings += detect_dependency_cycles(graph)
  global_findings += detect_multi_card_conflicts(graph)
  global_findings += detect_cumulative_impacts(graph)
  global_findings += detect_changed_assumptions(graph)
  global_findings += detect_status_note_mismatch(graph)

  findings = merge_and_deduplicate(local_findings, global_findings)

  for finding in findings:
      if belongs_to_single_card(finding):
          propose_card_update(finding)
      else:
          propose_resolution_card(finding)

  return ResultCandidate(findings)
```

Aucune modification n’est appliquée sans validation humaine.

## 12. Exemple : sols

Fiches :

- `SOL-001` dossier de sélection ;
- `STRUCT-012` structure plancher ;
- `BUDG-006` estimatif ;
- `CMD-003` commande.

Relations :

```text
SOL-001 impacte BUDG-006 : coût à réviser.
SOL-001 impacte CMD-003 : commande bloquée.
SOL-001 tension/conflit avec STRUCT-012 : grande dalle / support OSB.
STRUCT-012 dépend de SOL-001 pour l’hypothèse de revêtement.
BUDG-006 dépend de STRUCT-012 pour chiffrer reprise éventuelle.
```

L’impact coût appliqué devient passif.

Le conflit structure reste actif jusqu’à résolution.

## 13. Exemple : ERP médical

Fiches :

- `PROG-009` ajout activité avec sommeil ou surveillance ;
- `SEC-004` sécurité incendie ;
- `CVC-003` filtration / CTA ;
- `ABF-002` équipements visibles ;
- `BUDG-011` budget.

Relations possibles :

```text
PROG-009 impacte SEC-004 : réglementation à réviser.
PROG-009 impacte CVC-003 : besoins techniques renforcés.
CVC-003 impacte ABF-002 : équipements visibles possibles.
CVC-003 impacte BUDG-011 : coût à réviser si seuil dépassé.
SEC-004 peut entrer en conflit avec PROG-009 si l’usage confirmé n’est pas compatible avec le dossier précédent.
```

Une revue globale peut détecter que le problème réel n’est pas CVC seul ni sécurité seule, mais changement de programme.

Créer alors :

```text
RES-ERP-001 — Arbitrage programme médical / sécurité / CVC / ABF
```

## 14. Exemple : chantier

Fiches :

- `MAC-001` maçonnerie ;
- `COUV-001` couverture ;
- `PLA-001` plaquiste ;
- `PLN-001` planning.

Dépendances :

```text
PLA-001 dépend de COUV-001 : hors d’eau.
COUV-001 dépend de MAC-001 : support / relevés.
MAC-001 attend PLA-001 : réservation ou accès intérieur.
```

La revue globale détecte un cycle.

Ce n’est pas un impact simple.

Ce n’est pas forcément un conflit réglementaire.

C’est une incohérence de séquence.

Créer :

```text
RES-CHANTIER-001 — Cycle planning maçon / couvreur / plaquiste
```

Décision attendue : arbitrage de phasage.

## 15. Règle finale simplifiée

```text
Dépendance = ordre ou condition.
Impact = effet appliqué ou candidat.
Cohérence = possibilité de coexistence.
Note = justification humaine ou technique obligatoire.
Log = trace de changement.
Résolution = fiche créée quand le problème dépasse une fiche.
```

Ne jamais laisser les relations agir seules.

Toujours passer par :

```text
analyse
prévisualisation
confirmation humaine
transaction bornée
journalisation
réanalyse possible
```
