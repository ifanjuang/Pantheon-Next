# Architecture Document and Knowledge Organization

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document records the architecture-agency organization chosen on 2026-07-19 for project originals and the reusable Markdown knowledge corpus.

It specializes `KNOWLEDGE_TAXONOMY.md` and `SOURCE_INGESTION_RETRIEVAL_MODEL.md`. It does not create NAS folders, move or rename files, install a Markdown surface, run OCR, vectorize content, write PostgreSQL records, promote memory or authorize external action.

```text
Project originals stay on the NAS.
Reusable knowledge is written in Markdown.
Hermes may derive and propose.
Pantheon governs scope and status.
The human decides consequential promotion.
```

## Two separate spaces

The project documentary space and the reusable knowledge corpus must remain distinct.

```text
project document != Knowledge Item
Markdown note != original source
retrieved passage != evidence
indexed content != Registre Probatoire entry
```

A project-specific contract, estimate, CCTP, DPGF, report, notice, study, letter, email export or reception record remains a project source. It does not become reusable knowledge merely because it was converted, indexed or retrieved.

## Project originals on the NAS

Each project uses one shallow phase hierarchy:

```text
00_GESTION/
10_CONCEPTION/
20_AUTORISATIONS/
30_DCE/
40_MARCHES/
50_CHANTIER/
60_RECEPTION/
90_SINISTRES/
```

No mandatory subfolder exists inside these phase folders. Classification relies on the phase folder and a strict filename.

The candidate filename pattern is:

```text
PROJET_INDICE_PHASE_DISTRIBUTEUR_TYPE_OBJET_DATE.ext
```

Field meaning:

```text
PROJET         stable project name or code
INDICE         revision such as A1, B1 or B2
PHASE          phase identifier aligned with the folder
DISTRIBUTEUR   agency-defined issuer or distributor identifier
TYPE           document type such as CONTRAT, CCTP, DPGF, NOTICE, ESTIMATIF,
               ETUDE, COURRIER, MAIL, CR, PV or DOE
OBJET          short human-readable subject
DATE           document date in YYYY-MM-DD when known
ext            original file extension
```

Example:

```text
LIEUREY_B2_DCE_IFJ_CCTP_GROS-OEUVRE_2026-10-15.pdf
```

The original file is preserved. Hermes may propose a classification or rename, but must not silently apply it.

## Reusable Markdown knowledge corpus

The human-facing corpus uses exactly five first-level families:

```text
KNOWLEDGE/
├── Référentiels/
├── Responsabilité/
├── Méthodologie/
├── Techniques/
└── Réglementations/
```

These folders are navigation aids, not authority levels, security boundaries or memory states.

### Référentiels

Stable lookup material, dictionaries, catalogues and nomenclatures.

Examples:

```text
Dictionnaire des plantes.md
Matériaux courants.md
Acteurs d'une opération.md
Phases et livrables.md
Lots de travaux.md
```

A very large referential, such as thousands of plant records, should remain structured data in an external store such as PostgreSQL. Markdown may expose thematic or editorial views; one file per plant is not the default.

### Responsabilité

Contracts, insurance, duties, liability boundaries and jurisprudence.

Examples:

```text
Marché à forfait.md
Responsabilité du maître d'œuvre.md
Assurance dommages-ouvrage.md
Jurisprudence sur les travaux supplémentaires.md
```

### Méthodologie

Ways of working used by the agency across design, estimating, tendering, construction, reception and claims.

Examples:

```text
Préparer un DCE.md
Analyser une offre.md
Conduire une réunion de chantier.md
Organiser une réception.md
Traiter un sinistre.md
```

### Techniques

Construction systems, materials, landscape, building services, domotics and other technical disciplines.

Examples:

```text
Toitures végétalisées.md
Domotique résidentielle.md
Pathologies des enduits.md
Drainage des espaces extérieurs.md
```

A DTU may be referenced here as technical guidance, but the source document and its legal applicability remain explicit. Mandatory requirements belong under Réglementations.

### Réglementations

Mandatory legal, regulatory and administrative rules.

Examples:

```text
Accessibilité des ERP.md
Réglementation environnementale RE2020.md
Autorisations d'urbanisme.md
Règles de sécurité incendie.md
```

## Markdown naming rule

A knowledge note uses a free, natural subject title:

```text
Titre libre du sujet.md
```

No project name, phase, index, distributor, type prefix or date is required.

Default rules:

```text
one useful stable subject per note;
no mandatory subfolder below the five families;
prefer a title a person would naturally search for;
rename the note when its subject changes materially;
split only when a note becomes hard to consult;
merge duplicates only after review.
```

## Source and provenance boundary

A knowledge note may cite a PDF, regulation, contract model, email, study or web source. The source remains separate and superior to the note.

Machine metadata should not clutter the filename. A supporting registry may retain:

```text
source reference;
source digest;
scope and confidentiality;
extraction method and version;
page or section references;
review status;
validity and supersession;
index and embedding references.
```

This metadata is support material. It does not turn the note into evidence or governed memory.

## Candidate ingestion path

When a PDF is supplied for possible knowledge reuse, the bounded path is:

```text
original PDF on NAS or approved source system
→ linked or cached source reference
→ text/OCR/Markdown derivative candidate
→ proposed family and free subject title
→ duplicate and scope check
→ human review
→ Markdown Knowledge Item
→ selective indexing or vectorization
```

Hermes may execute extraction, segmentation and retrieval under an explicit bounded handoff. Pantheon governs source scope, candidate status, provenance expectations and gates. A Markdown surface such as SilverBullet may expose the corpus, but no particular product is adopted by this document.

## Card projections

Cards are generated consultation views. They are not new source files, storage objects or authority objects.

```text
NAS original / Markdown note / structured referential
→ bounded projection
→ card displayed for the current consultation
```

### Project Document Card

A Project Document Card projects one NAS source without duplicating it.

Minimum visible fields:

```text
parent_project_id;
project display name;
phase;
distributor;
document type;
subject;
index;
date;
link to the original;
analysis status.
```

Candidate actions remain bounded:

```text
open;
summarize;
compare;
propose extraction.
```

### Knowledge Card

A Knowledge Card projects reusable knowledge. Its default source is one Markdown subject. The family `Référentiels` is a knowledge family, not a separate authority class.

Minimum visible fields:

```text
free subject title;
family;
short summary;
principal source references;
freshness or review signal.
```

Candidate actions remain bounded:

```text
consult;
search nearby knowledge;
cite a source;
propose an update.
```

### Structured referential projection

A large structured referential may generate specialized Knowledge Cards directly from PostgreSQL or another approved external store. A plant catalogue can therefore expose one Knowledge Card per plant without creating one Markdown file per plant.

```text
Knowledge Card
├── editorial subject backed by Markdown
└── referential record backed by structured data
```

The distinction concerns source shape and consultation mode:

```text
editorial knowledge
= an explained subject intended to be read;

referential knowledge
= a normalized record or catalogue intended to be looked up, filtered and compared.
```

Both remain Knowledge Items.

### Card boundary

```text
Document Card parent_project_id required
card != source
card != duplicate document
card != Evidence
card != Registre Probatoire entry
card action != external-action authorization
card status != source validity
```

The card may expose a proposal from Hermes, but consequential acceptance remains human.

## Placement test

Use these questions in order:

```text
Is it specific to one project?
→ keep it in the project NAS space.

Is it mainly a dictionary, catalogue or nomenclature?
→ Référentiels.

Is it about obligations, contracts, insurance or liability?
→ Responsabilité.

Is it a reusable way of working?
→ Méthodologie.

Is it about how something is built, installed, diagnosed or maintained?
→ Techniques.

Is it a mandatory legal, regulatory or administrative rule?
→ Réglementations.
```

If a subject genuinely spans two families, choose the dominant consultation purpose and link to it from another note if useful. Do not duplicate the whole note.

## Non-equivalences

```text
folder placement != truth
strict filename != provenance complete
Markdown conversion != source replacement
knowledge publication != evidence admission
vectorization != memory
Hermes proposal != human acceptance
NAS presence != connector activation
documentation in this repository != deployed organization
```
