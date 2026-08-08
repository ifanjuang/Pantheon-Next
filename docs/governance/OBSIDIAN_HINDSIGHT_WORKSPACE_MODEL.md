# Obsidian / Hindsight Workspace Model

Status: candidate support doctrine — workspace and memory-use model. This document does not install, bind or activate any runtime.

Authority note: `docs/governance/HERMES_CAPABILITY_BINDINGS.md` remains authoritative for the `external_runtime_memory` binding posture. This document only defines the recommended workspace topology and circulation rules for the already sandbox-qualified Obsidian → Hindsight → Hermes path.

## Purpose

Provide one simple model that works across personal notes, agency knowledge, project workspaces, project lifecycle, document intake, CR preparation, media-derived notes and later archival without creating a second Pantheon knowledge or project authority.

The model is:

```text
BANK
= trust / memory-isolation boundary

TAG / FOLDER
= project, phase, topic and working-context scope

SOURCE
= exact origin of information

PANTHEON
= professional authority and governed state

PROJECTION
= human-facing view or editable representation

HERMES
= mediation, retrieval, reasoning, transformation and candidate generation
```

These responsibilities are orthogonal. A folder does not become an authority. A bank does not become a project. A projection does not become persistence. A recalled memory does not become truth.

## Workspace topology

Use one Obsidian vault and one Hindsight bank per durable trust domain, not per project.

```text
IFJA-Perso      -> ifja-personal
IFJA-Agence     -> ifja-agency
IFJA-Projets    -> ifja-projects
IFJA-Sandbox    -> ifja-sandbox
```

A separate Hindsight server per bank is not required. One Hindsight service may host these isolated banks.

### IFJA-Perso / `ifja-personal`

Purpose:

- personal architectural thinking;
- preferences and recurring ideas;
- reading notes;
- research notes;
- personal working journal;
- ideas not yet promoted into agency knowledge or project state.

Lifecycle: long-lived across projects and years.

Typical question:

```text
What had I previously thought about this kind of facade or spatial strategy?
```

This bank is intentionally associative. Cross-project personal recall can be useful here.

### IFJA-Agence / `ifja-agency`

Purpose:

- reusable agency methods;
- technical reference notes;
- templates and guidance;
- generalized lessons learned;
- shared working knowledge that should outlive individual projects.

Lifecycle: long-lived organizational memory.

Typical question:

```text
What method or lesson has the agency already documented for this recurring situation?
```

Agency memory remains non-authoritative unless separately qualified into a governed Pantheon Knowledge object or other existing owner.

### IFJA-Projets / `ifja-projects`

Purpose:

- project-specific working notes;
- meeting notes;
- visit notes;
- CR drafts;
- informal hypotheses;
- contextual reminders;
- project-specific reasoning around governed sources.

Lifecycle: prospect -> design -> studies -> consultation -> site -> reception -> archive.

Projects are folders/scopes inside this vault and bank. They are not separate banks by default.

Example:

```text
IFJA-Projets/
  Saint-Gatien/
    Notes/
    Reunions/
    CR/
    Travail/
    References/
  Bois-Guillaume/
  Trouville/
  Archives/
```

Hindsight recall should normally apply strict project/folder scope for project questions.

Example memory scope:

```text
bank_id = ifja-projects
recall_tags = [vault:IFJA-Projets, folder:Saint-Gatien]
recall_tags_match = all_strict
```

Cross-project recall is an explicit broader operation, not the normal default.

### IFJA-Sandbox / `ifja-sandbox`

Purpose:

- synthetic fixtures;
- integration tests;
- migration trials;
- new provider/version evaluation;
- non-client experiments.

Sandbox data must not be mistaken for agency or project memory.

## Why projects are not banks

A project is a working context, not normally a different trust domain.

Creating one bank per project would fragment cross-project retrieval, complicate lifecycle transitions, increase operational overhead and make archival or comparison unnecessarily expensive.

Use a separate bank only when a real trust/isolation requirement exists that cannot safely be represented by vault/folder scope.

```text
project identity != bank identity
folder location != Pantheon Project identity
```

## Source rule

Original material keeps its own identity and provenance.

Examples:

```text
PDF -> source file / Document lifecycle owner
photo -> source image
recording -> source audio
email -> source message
Revit / IFC -> source representation
Obsidian note -> Markdown source note
```

Hindsight may retain text or derived memory related to these sources, but does not become their canonical storage or professional authority.

```text
stored != validated
retrieved != truth
memory != source
```

For governed documents, media, BIM and professional records, Pantheon-side source/provenance owners remain authoritative.

## Projection rule

A projection is where a human sees or edits a representation.

Examples:

```text
Obsidian note
Cockpit card
CR draft
Project Anatomy graph
Document preview
Knowledge page
```

Editing a projection does not automatically change governed state.

```text
projected != persisted
edited text != approved state change
```

A consequential change discovered through an editable projection should create or use an existing candidate/change path rather than silently mutate another owner.

## Hermes rule

Hermes connects the layers but owns none of their truth.

Hermes may:

- recall scoped Hindsight memory;
- read governed Pantheon context when authorized;
- compare source material;
- synthesize notes;
- prepare CR candidates;
- propose mappings or promotions;
- create candidate outputs through existing bounded contracts.

Hermes must not convert recall success into professional validation.

```text
Hindsight recall != truth
Hermes memory success != task authorization
runtime success != Evidence
```

## Initial durable memory posture

For the sandbox-qualified Hindsight path, keep the initial operational posture conservative:

```text
memory_mode = tools
auto_recall = false
auto_retain = false
conversation_retention = off
```

Rationale:

- Obsidian remains the intentional producer for synchronized workspace memory;
- Hermes consumes memory without introducing a second ingestion path;
- professional questions can query Pantheon before optional informal recall;
- recall remains observable and debuggable;
- conversation history is not silently promoted into long-term memory.

Any later use of automatic recall, automatic retain, observation consolidation or reflection is a separate evaluation and does not alter Pantheon authority.

## Project lifecycle

### Prospect / early contact

Obsidian/Hindsight may hold informal context, ideas, meeting fragments and exploratory notes.

Pantheon receives only information that belongs in an existing governed project/intake owner.

### Design

Obsidian supports thinking and drafting.

Hindsight supports contextual recall.

Pantheon owns governed project state, documents, decisions and existing Project Anatomy structures.

### Studies / DCE / consultation

Professional documents, revisions and currentness belong to the existing Document lifecycle.

Hindsight may help answer why something was discussed, but must not determine which professional revision is currently authoritative.

### Site / construction

Typical composition:

```text
Obsidian visit notes
+ Hindsight project recall
+ Pantheon open issues / documents / decisions
+ source photos / audio / email
-> Hermes
-> CR / Information / Work / relation candidates through existing owners
```

A note, photograph or recalled memory is not a decision merely because it appears in a CR draft.

### Reception / closeout

Governed records remain in Pantheon and its source/document owners.

Working notes may remain in the project vault for continuity and later lessons learned.

### Archive

A project folder may move under `Archives/` without changing Pantheon Project identity.

Hindsight reconciliation follows the workspace source path; Pantheon identity and professional history remain unchanged.

## Promotion paths

Promotion means an explicit change in responsibility, not a file move alone.

### Personal -> Agency

```text
personal idea / repeated pattern
-> explicit review or author decision
-> agency note or existing Knowledge candidate path
```

A repeated personal preference is not automatically agency doctrine.

### Project -> Agency

```text
project-specific experience
-> generalized lesson candidate
-> review
-> agency workspace and/or governed Knowledge through existing owner
```

A project incident is not automatically a reusable rule.

### Project workspace -> Pantheon

```text
Obsidian note / Hindsight recall
-> Hermes candidate
-> existing Pantheon owner / validation path
```

No direct memory-to-authority promotion is allowed.

### Agency -> Project

Prefer references/contextual retrieval over uncontrolled duplication. If an agency method becomes a project requirement, that professional adoption must be represented through the appropriate existing Pantheon object or document path.

## Examples across domains

### PDF revision

```text
BANK        not primary
TAG/FOLDER  optional working context
SOURCE      exact PDF received
PANTHEON    logical Document + revision + currentness
PROJECTION  Cockpit / preview / derived Markdown
HERMES      extraction / comparison / impact candidate
```

### CR preparation

```text
BANK        ifja-projects
TAG/FOLDER  project + visit/date/topic
SOURCE      notes + photos + audio + mails + prior CR
PANTHEON    admitted CR and governed related states
PROJECTION  editable CR in Obsidian/Cockpit
HERMES      reconciliation + drafting + candidates
```

### Project Anatomy

```text
BANK        contextual memory only
TAG/FOLDER  project context
SOURCE      Revit / IFC / plan / photo / document
PANTHEON    stable_object / source_representation / attribute_claim / relation_claim
PROJECTION  Cockpit graph / read model
HERMES      matching and relation candidates
```

### Agency Knowledge

```text
BANK        ifja-agency
TAG/FOLDER  domain / method / topic
SOURCE      note / project / regulation / document
PANTHEON    governed Knowledge when explicitly qualified
PROJECTION  Obsidian / Cockpit knowledge view
HERMES      retrieval / synthesis / promotion candidate
```

## Trust, scope and authority rules

```text
BANK
answers: who or what may share this memory domain?

TAG / FOLDER
answers: which project, phase, topic or working context applies?

SOURCE
answers: where did this information come from exactly?

PANTHEON
answers: what professional state is governed and retained?

PROJECTION
answers: where is that state or candidate shown or edited?

HERMES
answers: how are sources, memory and governed context connected into useful candidates?
```

The layers must remain separable and replaceable.

## External-memory authority boundary

This workspace model does not change the existing registry posture:

```text
external_runtime_memory.preferred_binding = unbound
assistant-personal = sandbox-qualified path allowed
pantheon-governed = external memory forbidden
production activation = not authorized by this document
```

The qualified source path remains:

```text
Obsidian vault
-> official one-way hindsight-obsidian sync
-> Hindsight bank
-> scoped Hermes assistant-personal recall
```

Observed constraint retained from O1-O3:

```text
sync accepted != materialized
```

A completed sync/reconcile may precede Hindsight worker materialization.

## Non-goals

This document does not create:

- a Pantheon memory owner;
- a vault registry;
- a bank registry;
- a new Capability Slot;
- a project-per-bank rule;
- bidirectional Pantheon/Obsidian synchronization;
- automatic Evidence, Decision, Knowledge, Project Anatomy or Project mutation;
- a new runtime, scheduler, queue or provider router;
- a LangChain or LangGraph dependency;
- production/NAS activation.

## Final rule

```text
Obsidian organizes human work.
Hindsight remembers within bounded trust domains.
Hermes retrieves, connects and proposes.
Pantheon governs professional state.
Original sources remain identifiable.
Projections remain views, not authority.
```
