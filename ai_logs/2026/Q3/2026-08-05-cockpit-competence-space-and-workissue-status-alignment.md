# Cockpit competence space and WorkIssue status alignment — 2026-08-05

Status: completed documentation trace — no implementation or activation.

## Objective

Close the remaining convergence findings on PR #543 by aligning the adaptive
project roadmap with the canonical WorkIssue vocabulary and by promoting
`Compétences` into the Cockpit owner doctrine as a distinct sixth root space.

## Changes

### WorkIssue status vocabulary

The roadmap now reuses the canonical statuses from
`schemas/work_issue_slice.schema.yaml`:

```text
open
in_progress
waiting
review
done
cancelled
```

The user-facing labels are projections only:

```text
À faire
En cours
En attente
À relire
Terminé
Annulé
```

```text
UX label != canonical status
blocked presentation != new blocked lifecycle state
completed wording != canonical done value
```

### Sixth Cockpit space

`docs/governance/PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md` now owns six
root spaces:

```text
Pantheon
Décisions
Affaires
Connaissances
Compétences
Outils
```

`Compétences` owns the user-facing projection of governed reusable business
abilities. `Outils` remains limited to replaceable technical means.

### Capability and Hermes implementation boundary

```text
Créer une compétence
-> crée ou propose une Capability candidate gouvernée dans Pantheon.

Implémenter cette compétence
-> peut demander à Hermes de préparer un Skill ou Workflow candidat.

Capability candidate created
!= Hermes Skill implemented
!= Capability admitted
!= Task authorized
```

Pantheon remains the semantic and governance owner of the Capability. Hermes may
prepare bounded implementation candidates but does not own admission or task
authorization.

## Files

```text
docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md
docs/governance/PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md
```

## Non-effects

```text
no schema change
no WorkIssue lifecycle change
no migration
no API
no Cockpit implementation
no Hermes Skill creation
no Workflow creation
no capability admission
no installation
no activation
no task authorization
```

```text
documentation aligned != implementation completed
Capability candidate != runtime implementation
runtime implementation != admitted capability
admitted capability != authorized task
```
