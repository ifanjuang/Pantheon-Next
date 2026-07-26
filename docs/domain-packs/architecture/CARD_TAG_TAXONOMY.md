# Architecture Card Tag Taxonomy

Status: candidate support specification — documented non-implemented.

This note refines the simplified architecture Cockpit card model by separating two independent tag vocabularies.

```text
type tag != subject tag
```

## Type tags

Type tags describe the nature, medium or professional kind of the card/content.

Examples:

```text
email
dossier
etude
cctp
ccap
compte-rendu
contrat
note
courrier
plan
photo
outil
skill
function
connector
```

They belong to a dedicated Type Tag Registry with at least:

```text
slug
title
description
icon_key
color
```

Recto projection:

```text
top left
family/project icon
category
then type-tag icon(s)
then index/date underneath when applicable
```

Type tags are identity/classification aids. They are not status, limit, approval or evidence qualifiers.

## Subject tags

Subject tags describe what the card is about across card families.

Examples:

```text
erp
re2020
maison-individuelle
logement
tertiaire
ecole
zone-naturelle
structure
electricite
urbanisme
chantier
```

They belong to a separate Subject Tag Registry with the same minimal metadata shape:

```text
slug
title
description
icon_key
color
```

Recto projection:

```text
bottom right
icon only
circular colored CSS treatment
```

Verso projection:

```text
bottom left
text labels
rectangular colored background
no pill-radius treatment
```

## Hermes rule

Hermes may primarily manage ordinary tag assignment and may propose/add missing vocabulary under registry policy.

Hermes should resolve aliases and reuse an existing canonical entry before creating a new tag.

Hermes must not convert tags into governance state.

```text
type tag != status
subject tag != status
tag != limit/posture
tag != approval
tag != Evidence
tag != authorization
tag != safe
```

## Implementation posture

```text
implemented:
- none by this note.

documented non-implemented:
- separate type_tags and subject_tags registries;
- top-left type-tag recto projection;
- bottom-right subject-tag recto projection;
- bottom-left subject-tag verso labels.
```

This remains candidate support material and requires practical Cockpit testing before promotion.
