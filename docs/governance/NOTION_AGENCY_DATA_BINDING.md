# Notion Agency Data Binding for Pantheon Cockpit V2

Status: candidate support doctrine — documented non-implemented live connector; executable read-only projection seam exists externally in `pantheon-mvp` PR #65.

Boundary profile: candidate_support_note.

Decision date: 2026-07-24.

## 1. Purpose

Pantheon Cockpit V2 may use Notion as an optional Agency Data binding when a professional workspace already contains structured project, person, organization, participation or agency-decision records.

Notion is not required for Pantheon Cockpit V2.

```text
Notion binding enabled  -> Cockpit may project declared Notion-owned records
Notion binding disabled -> Cockpit remains functional with other owner bindings
```

The binding exists to reuse an agency's structured data rather than rebuild it prematurely.

It does not make Notion:

```text
Pantheon governance authority;
Evidence authority;
Hermes runtime;
canonical Tag registry by default;
capability registry;
runtime health authority;
a mandatory Pantheon dependency.
```

Core allocation remains:

```text
OpenWebUI / Cockpit exposes.
Hermes Agent executes bounded external connector operations.
Pantheon Next governs status, scope, evidence, consequential decisions and activation.
Notion owns only the agency records/fields explicitly assigned to it.
The human decides consequential effects.
```

## 2. Capability-slot interpretation

The integration must be reasoned as an optional binding, not a hard dependency.

```text
abstract function
  agency_structured_records
        ↓
candidate binding
  Notion workspace
        ↓
connector path candidate
  external_connector_gateway / Hermes + reviewed connector gateway where required
        ↓
status
  optional / read-only first
        ↓
Pantheon gates
  only for consequential writes or authority changes
```

This specializes the existing external connector doctrine.

The generic `external_connector_gateway` capability already identifies Notion as a supported third-party API domain and keeps credentials/execution external to Pantheon.

```text
binding_selected != dependency_adopted
connector reachable != data adopted
read permission != write authorization
external API success != Evidence
```

## 3. Pilot workspace observation

The connected IFJA Notion workspace currently exposes business structures that align well with Cockpit V2 concepts.

The observed names below describe a pilot mapping. They are not global Pantheon schema names.

### `_Affaires`

Observed relevant properties include:

```text
Code
Statut
Phase
Lieu
Description
Budget
Contrat
DROC
Date Arrêté
Date dépot
Réception
Levée des réserves
No Permis
Numéro de Parcelle
Zone PLU
Srf Terrain
Srf Construite
Srf Démol
Srf plancher Existante
surface Taxable
Emprise Existante
Emprise Créée
Emprise supprimé
GEORISQUE
Lien GNAU
dossier MAF
type ERP
Intervenants
_Décisions
```

This is a strong candidate owner for the first Project Card fields in the IFJA pilot.

### `_Personnes`

Observed fields:

```text
Nom
E-mail
Numéro
adresse
Société
```

Candidate Cockpit object:

```text
Person
```

### `_Sociétés`

Observed fields:

```text
Name
E-mail
Téléphone
Adresse
siret
RIB
Personnes
```

Candidate Cockpit object:

```text
Organization
```

Sensitive or unnecessary properties must not be exposed just because they exist. For example a banking document such as `RIB` is not part of normal Context Resolver search.

### `_Intervenants`

Observed fields include:

```text
Affaire
Responsable
Rôle
Type
Société
Code
HT
TTC
Fichiers et médias
```

This is close to a project-scoped relation record.

Candidate Cockpit interpretation:

```text
ProjectParticipation
or CompanyEngagement projection depending on the record
```

The adapter may normalize the record for display, but it must not silently rewrite the Notion schema or claim that all participants and companies have the same lifecycle.

### `_Décisions`

The existing agency data source contains fields such as:

```text
Arbitrage
Argumentaire
Conseil Pantheon
Contenu
Date de décision
Décideur / validateur
Description du choix
Effet
Impact métier
Lien source canonique
Mots-clés
Moyen de décision
```

These records are potentially valuable agency/project decisions.

They are not automatically Pantheon governance Decisions.

```text
AgencyDecisionRecord in Notion
!=
PantheonGovernanceDecision
```

A relation may connect them where legitimate.

## 4. Owner-field rule

The binding must declare ownership at field/relation level rather than merely at application level.

Example pilot allocation:

| Information | Candidate owner | Cockpit behavior |
|---|---|---|
| Project code | Notion `_Affaires` | read/project |
| Project business status | Notion `_Affaires` | read/project |
| Project phase | Notion `_Affaires` | read/project |
| Project location | Notion `_Affaires` | read/project |
| Permit/admin dates | Notion `_Affaires` when declared | read/project |
| Surface values | Notion `_Affaires` when declared | read/project |
| Person contact identity | Notion `_Personnes` | read/person |
| Company identity | Notion `_Sociétés` | read/organization |
| Project participant relation | Notion `_Intervenants` | read/relation |
| Original PDF/email/file | source system such as Paperless/NAS/Drive/Gmail | link only |
| Evidence status | Pantheon governance | never inferred from Notion |
| Formal Pantheon Decision | Pantheon governance | never replaced by Notion choice |
| Hermes Run | Hermes runtime | observation only |
| Capability activation | Pantheon governance + external runtime | never Notion-owned |
| canonical Tag vocabulary | dedicated Tag owner/registry | Notion may project only |

A normalized cache or PostgreSQL projection does not automatically become owner of a Notion-owned field.

## 5. Integration modes

### 5.1 Disabled

```text
mode = disabled
```

No Notion provider is registered.

No error should prevent Cockpit operation merely because Notion is absent.

### 5.2 Read-only projection

First supported target mode:

```text
mode = read_only
```

Allowed behavior:

```text
query declared data sources;
return normalized card/search projections;
retain source attribution;
use stable external IDs;
expose freshness/observation time when available;
show missing fields rather than fabricate them.
```

Forbidden behavior:

```text
create pages;
edit properties;
change relations;
create/select options;
upload files;
modify workspace schema;
automatically mirror Cockpit data back to Notion.
```

### 5.3 Future bounded write-back

A later write mode may be considered only for fields whose declared owner is Notion.

Conceptual flow:

```text
user/Hermes proposes change
        ↓
resolve target owner
        ↓
Notion owns field?
  no -> route elsewhere / refuse
  yes
        ↓
classify effect
        ↓
Pantheon gate if consequential
        ↓
explicit human Decision when required
        ↓
Hermes/external connector executes bounded Notion mutation
        ↓
receipt + re-read
```

There is no `sync_everything` mode.

## 6. Connector placement

A browser must not hold a Notion API secret.

The preferred architectural shape is:

```text
Cockpit
   ↓ bounded query intent
normalized Agency Data projection seam
   ↓
external connector binding
   ↓
Notion
```

Where private API credentials or real provider access are needed, execution belongs behind the external connector capability boundary. The current candidate external gateway is Nango executed through Hermes, as documented by `NANGO_HERMES_CONNECTOR_GATEWAY.md` and `HERMES_CAPABILITY_BINDINGS.md`.

Pantheon does not become the credential store or connector runtime.

```text
Cockpit direct Notion token = forbidden design
Pantheon-owned OAuth runtime = forbidden design
Hermes/external gateway scoped retrieval = candidate
```

## 7. Context Resolver mapping

Cockpit V2 namespaces may use the Notion binding when enabled.

### `_` Affaires

```text
_LIE
```

may search `_Affaires` using project identity fields.

Ranking preference:

```text
exact/prefix Code or display identity
then title/identity contains
then explicitly permitted aliases
```

Project search must not return cross-workspace material unless that workspace is explicitly in scope.

### `@` People

```text
@lebre
```

may query `_Personnes` using name plus safe contact/search fields.

Normal search should not expose sensitive unrelated fields.

### `*` Global permitted search

Notion may contribute:

```text
Affaires
People
Organizations
Project participations
```

to the global resolver alongside Documents, Knowledge, capabilities and other owner providers.

The resolver must support multiple providers simultaneously.

```text
Notion global contribution != global data ownership
```

Each result should preserve:

```text
entity_id
entity_type
label
secondary_label
source.system = notion
source.collection
source.external_id
source.url
match reason
scope
```

## 8. Normalization contract

The Cockpit should consume normalized projections rather than raw Notion blocks/schema internals.

### Project projection candidate

```text
entity_type: project
entity_id: stable Notion external identity
label: Code / declared project name
secondary_label: status · phase · location
description
status
search_terms:
  parcel
  PLU zone
  permit number
  ERP type
source
scope
```

### Person projection candidate

```text
entity_type: person
label: Nom
secondary_label: company display name when resolved
search_terms:
  email
  phone
  address
source
scope
```

### Organization projection candidate

```text
entity_type: organization
label: Name
secondary_label: SIRET when appropriate
search_terms:
  email
  phone
  address
source
scope
```

### Participation projection candidate

```text
entity_type: project_participation
label: Code or role/person/company summary
secondary_label: Type · Rôle · Société
search_terms:
  responsible person
  company
  role
  project
source
scope
```

These are exposure projections, not replacements for the underlying owner record.

## 9. Project Card composition

For the IFJA pilot, a Project Card may combine Notion owner fields with other source systems.

Example:

```text
Project Card Lieurey
├── identity/status/phase/location        Notion
├── participants                         Notion
├── administrative facts                Notion where declared owner
├── tags                                 Tag Registry
├── source documents                     Paperless/NAS/Drive/etc.
├── Knowledge applicable relations       Knowledge owner + governed relation
├── Evidence                             Pantheon governance
├── human attention/Decision projections Pantheon + owner statuses
└── Hermes answers/runs                  Hermes/runtime observations
```

The user sees one coherent card while authority remains distributed.

## 10. Tags and Notion

The Cockpit Tag Registry is richer than a generic Notion multi-select.

Canonical Tag candidate shape:

```text
tag_id
name
description
icon_key
color
aliases
category
status
provenance
```

A Notion multi-select may be mapped to or display an existing Tag.

It must not automatically create canonical vocabulary.

Example:

```text
Notion text "Secteur ABF"
   ↓ similarity / alias lookup
existing Tag ABF found
   ↓
TagAssignment Candidate
```

If no adequate tag exists:

```text
new Tag Candidate
```

not immediate canonical creation.

## 11. Decision separation

Cockpit `Décisions` is a Scene/projection across objects requiring human attention.

It may include:

```text
agency decisions from Notion;
Documents requiring review;
Work Issues;
Decision Requests;
formal Pantheon Decisions.
```

The UI must show underlying type/status clearly.

```text
appears in Décisions != formal governance Decision
agency arbitration Accepted != Pantheon effect authorization
```

An agency decision may be a source/context relation for a Pantheon Decision but never an automatic substitute.

## 12. Data sensitivity and minimization

Notion access may expose more workspace data than a task needs.

The adapter must minimize at three levels:

```text
workspace scope
collection scope
field/object scope
```

Examples:

```text
Project resolver does not need RIB attachments.
People autocomplete does not need unrelated project financial fields.
A Lieurey card context does not silently retrieve all other Affaires.
```

Connector responses and logs must avoid raw tokens and unnecessary sensitive fields.

## 13. Freshness and conflict

A Notion field is an observation of the owner record at a time.

Recommended projection metadata:

```text
observed_at
source_last_edited_time when available
source_ref
owner_system = notion
```

If a normalized cache exists:

```text
cache value != current Notion value
```

Conflict handling must prefer an explicit owner rule rather than last-write-wins across systems.

## 14. Outils projection

When the binding becomes observable, `Outils → Connecteurs → Notion` may expose a read-only status card.

Front candidate:

```text
NOTION
workspace label
binding mode
number of declared collection bindings
```

Back candidate:

```text
provider
workspace label
binding status
configured scopes/collections
read/write posture
last observation
health observation
permissions summary
owner mappings
next decision
```

Required distinctions:

```text
configured != connected
connected != adopted
reachable != healthy
healthy != safe
readable != authoritative for every field
write-capable != write-authorized
```

## 15. Responsibility allocation

### Pantheon governs

```text
whether the binding may be adopted;
which scopes/collections are legitimate;
owner mapping declarations;
consequential write gates;
status qualification;
relations to Evidence/Decision/Context;
activation and suspension posture.
```

### Hermes executes

```text
bounded provider queries/actions through the selected external connector binding;
normalization/enrichment tasks when delegated;
connector error reporting;
write actions only after applicable authorization.
```

### OpenWebUI / Cockpit displays

```text
Notion-backed Project/Person/Organization projections;
source attribution;
connection/binding status;
Context Resolver results;
card fields and relations;
visible write candidates and gates.
```

### Human approves

```text
adoption of a write-capable binding;
consequential external mutations;
owner-map changes with material consequences;
formal Pantheon Decisions.
```

### Forbidden

```text
browser-held Notion secrets;
Pantheon as OAuth/connector runtime;
implicit cross-workspace retrieval;
full bidirectional synchronization by default;
last-write-wins authority collapse;
Notion agency choice treated as Pantheon approval;
Notion multi-select treated as canonical Tag without review;
API success treated as Evidence;
automatic external write.
```

## 16. Implementation stages

### Stage N0 — documented mapping

```text
status: implemented in documentation
```

Record pilot owner map and boundaries.

### Stage N1 — read-only projection seam

```text
pantheon-mvp notion_agency_binding.js
Context Resolver provider composition
normalized source attribution
```

Status at drafting time:

```text
implemented candidate in external MVP PR
live transport not connected
```

### Stage N2 — live scoped read transport

```text
select/review connector binding
configure external credential handling
bind only declared IFJA workspace/collections
return normalized projections
acceptance-test scope and stale/error handling
```

Not yet implemented by this document.

### Stage N3 — Project Card real-data pilot

```text
Affaires cards
People/Organizations
Intervenants
owner-field source labels
```

Not yet implemented.

### Stage N4 — bounded agency decision projection

Map `_Décisions` as `AgencyDecisionRecord` without collapsing governance Decision semantics.

Not yet implemented.

### Stage N5 — optional write-back

Only after explicit owner mapping, gate design, connector review and human authorization.

Not yet authorized.

## 17. Status summary

```text
Notion optional Agency Data concept              documented
IFJA pilot schema observation                    observed
owner-field boundary                             documented
Notion read-only projection seam in MVP          implemented candidate
Context Resolver Notion provider composition     implemented candidate
live Notion connector transport                  not connected
Nango/Hermes connector adoption                  not decided
Notion Project Card live data                    not connected
Notion Person/Organization live data             not connected
Notion agency Decision projection                not connected
Notion write-back                                not implemented
production adoption                              not authorized
```
