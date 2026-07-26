# Architecture Project Card Deck Composition

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document owns one rule for the architecture domain: **a project is not a
wide row of fields — it is a deck of source-backed cards that accumulates as the
affair progresses.** It specializes `CARD_STACK_MODEL.md` and
`PROJECT_NAVIGATION_UX.md`, and it constrains what belongs in the minimal
`AGENCY_DATA_SYSTEM_OF_RECORD.md` project record versus what belongs in a linked
card.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## 1. The core rule

```text
agency_projects record = stable identity + revision + a few operational fields
everything rich          = a linked card with its own owner, provenance and status
the Project Card display = claims that CITE a backing card, status-qualified
the deck                 = grows au fur et à mesure, by phase, never as one big form
```

A value shown on a project (`Zone: UB`, `risque argiles: moyen`) is a **claim**
that points at the card that backs it. It is never authoritative on its own:

```text
displayed != opposable
surface displayed != filing value approved
zone displayed != regulatory conclusion
document held != Evidence admitted
```

## 2. What stays in the minimal project record

`agency_projects` (system of record) keeps only what is stable and identity-like:

```text
project_id, code, display_name, status, phase, location, primary_client,
revision + audit, permit_number, parcels[]
```

It does **not** grow columns for surfaces, PLU, géorisques, contracts, insurance,
budget or administrative dates. Those become cards or thin claims.

## 3. Card families and their owners

Each rich element is one of these card families, governed by its existing owner:

| Card family | Owner doctrine | What it is | Lifecycle statuses |
|---|---|---|---|
| Document | Document lifecycle / Paperless source | the raw source file (rapport, arrêté, contrat, notice) | captured → à relire → filed → superseded |
| Evidence | Registre Probatoire / Evidence | a Document admitted as proof backing a claim | candidate → admitted → contested → retired |
| Knowledge / Référence | Knowledge | reusable reference (PLU règlement, DTU, CCAG) | generated_unreviewed → reviewed → published |
| Décision | Agency decision record (≠ Pantheon governance Decision) | an arbitrage / choix | proposed → decided → superseded |
| Surface / Fact | project claim + backing Document | a typed, source-backed value | asserted → source-backed → verified |
| Jalon / Phase event | phase_state / append-only event | a dated milestone (arrêté, DROC, réception) | expected → reached → contested |
| Participation / Engagement | Agency Data relations | intervenant / entreprise link | identified → engaged → closed |

```text
Document != Evidence           (admission required)
Knowledge != Evidence          (reusable reference is not proof of a specific claim)
Agency Decision != Pantheon governance Decision
claim != source                (a claim cites the card that backs it)
```

## 4. IFJA `_Affaires` field → card mapping

The rich Notion `_Affaires` fields resolve to cards, not columns:

| Notion field | Becomes | Note |
|---|---|---|
| No Permis | project record `permit_number` | identity |
| Numéro de Parcelle | project record `parcels[]` | often multi-parcel |
| Zone PLU / PLUi | Knowledge/Référence card + parcel Evidence | claim: `zone` cites it |
| type ERP | claim backed by a regulatory card | claim, not column |
| Budget | Fact backed by devis/contrat Documents | sensitive; dated + revised |
| Srf / Emprise (all) | one typed **Surface** card set (type, value, unit, provenance, status) | derived values (créée/supprimée/démol) are computed, not stored |
| DROC, Date Arrêté, Date dépôt, Réception, Levée des réserves | **Jalon** timeline (dated events) | dates derive from the backing Document |
| Contrat | Document card (relation) | not a scalar |
| GEORISQUE | Document card → Evidence when it backs a risk claim | derivable from parcelle/location |
| Lien GNAU | attribute of the authorization dossier | not a project field |
| dossier MAF | insurance/responsibility record | separate owner |
| Intervenants, _Décisions | Participation / Décision cards | already relations |

"Voués à disparaître" means removed **from the project record**, not deleted:
they become cards with provenance, status and a lifecycle a flat Notion field
never had.

## 5. Progressive accumulation by phase

A fresh affair holds only its identity. The deck fills as sources arrive, along
the existing phase folders (`PROJECT_NAVIGATION_UX.md`):

```text
00_Gestion      identity, participants, budget fact
10_Conception   program, site notes, first Knowledge references
20_Autorisations PLU (Knowledge) · Géorisques (Document→Evidence) · Arrêté (Document + jalon)
30_DCE          CCTP/CCAP Documents, surfaces (notice), lots
40_Marche       contrats (Documents), engagements entreprises
50_Chantier     DROC, CR, réception, levée des réserves (jalons + Documents)
90_Sinistres    claims, insurance (MAF) records
```

Each card carries its own status; the Project Card recto/verso reads claims off
the current cards. Nothing is stored flat on the project.

## 6. Boundary

```text
project record != project source of truth deck
field migrated out != field deleted
claim displayed != approved value
card present != Evidence admitted
progressive accumulation != automatic ingestion (each card is governed)
```

This document changes no schema, creates no ingestion runtime and admits no
Evidence. It states where architecture project richness lives: in a governed,
source-backed, progressively accumulated card deck — not in the minimal Agency
Data record.
