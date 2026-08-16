# Obsidian / Hindsight Workspace Model

Status: candidate support doctrine — workspace and memory-use model. Windows + Synology Hindsight topology qualified; LiveSync/CouchDB and optional Obsidian Web remain separate work in stabilization. This document does not install, bind, activate or authorize a runtime.

Authority note: `docs/governance/HERMES_CAPABILITY_BINDINGS.md` remains authoritative for the `external_runtime_memory` binding posture. `catalog/bindings/external-runtime-memory-unbound.yaml` remains the machine-checkable selection record. This document defines workspace topology and circulation rules only.

Qualification record: `ai_logs/2026/Q3/2026-08-16-655-memory-workspace-qualification.md` and Pantheon-Next #655.

## Purpose

Provide one simple model for agency knowledge, project workspaces, document intake, CR preparation, media-derived notes and later archival without creating a second Pantheon knowledge or project authority.

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

## Current qualified workspace topology

Use one Obsidian vault and one Hindsight bank per durable trust domain, not per project.

The banks actually created and qualified in #655 are:

```text
IFJA-Agence     -> ifja-agency
IFJA-Projets    -> ifja-projects
IFJA-Sandbox    -> ifja-sandbox
```

A separate Hindsight server per bank is not required. The observed Synology deployment uses one Hindsight `0.9.1` service hosting isolated banks.

The earlier proposed personal domain remains possible but is **not part of the current qualified deployment**:

```text
IFJA-Perso      -> ifja-personal   # proposed / not deployed / not qualified
```

Do not present `ifja-personal` as existing until it is actually created and qualified.

### IFJA-Agence / `ifja-agency`

Purpose:

- reusable agency methods;
- technical reference notes;
- templates and guidance;
- generalized lessons learned;
- shared working knowledge that should outlive individual projects.

Lifecycle: long-lived organizational workspace memory.

Typical question:

```text
What method or lesson has the agency already documented for this recurring situation?
```

Agency memory remains non-authoritative unless separately qualified into a governed Pantheon Knowledge object or another existing owner.

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

### Future personal domain

A personal trust domain may still be useful for architectural thinking, preferences, reading notes and ideas that should not automatically circulate into agency/project memory.

If later created, it should remain a separate vault/bank and must be qualified before use:

```text
IFJA-Perso -> ifja-personal
```

Its presence in this doctrine is a future option, not evidence of deployment.

## Qualified runtime/source observations

The #655 Windows + Synology campaign established the following current observations:

- Hindsight is running as `0.9.1` on the always-on Synology host and persistence survived migration/restart checks;
- the official `vectorize-io/hindsight-obsidian` code/assets used for current qualification correspond to release `0.2.1`;
- the upstream `0.2.1` release manifest still reports `0.2.0`, so UI/manifest version display alone is not sufficient to identify the installed code;
- Obsidian create/edit/rename/delete/reconcile behavior was verified and synthetic test documents were removed;
- deterministic document listing is preferred when verifying source-document presence/deletion because Hindsight recall may transform source text into semantic facts;
- Hermes reaches the three banks through single-bank MCP endpoints in addition to the historical provider-style qualification path;
- bank isolation and tool filtering were verified, but neither is authentication or authorization.

These are observed compatibility/deployment facts. They do not bind `external_runtime_memory` or create Pantheon authority.

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
memory != Evidence
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

Hermes must not convert recall or technical write success into professional validation or ingestion authority.

```text
Hindsight recall != truth
Hermes memory success != task authorization
runtime success != Evidence
MCP tool available != write authorized
technical write success != ingestion authority
```

## One-ingestion-authority rule

Durable banks should have one clearly designated ingestion authority for synchronized workspace notes.

The stable target is:

```text
Obsidian Markdown source
        -> designated synchronization/ingestion path
        -> Hindsight derived bank
        -> read consumers
```

A second producer must not be enabled merely because its tool exists.

The #655 campaign technically verified an Hermes `sync_retain` route into `ifja-projects` with synthetic data. That test proves routing and bank isolation only. It is **not** the durable posture.

Until #659 explicitly decides and qualifies ingestion authority:

```text
Hermes -> ifja-agency   = read-only
Hermes -> ifja-projects = read-only target posture
Hermes durable writes   = disabled / to remove from live surface
```

This removes the contradiction between `Obsidian is the intentional source` and an independently writable durable Hermes memory surface.

## Initial durable memory posture

Keep the operational posture conservative:

```text
conversation_retention = off
Obsidian prefix document ids = on
Hermes durable-bank recall = explicit / tool-mediated
Hermes durable-bank writes = off pending #659
```

Historical O1-O3 provider tests used:

```text
memory_mode = tools
auto_recall = false
auto_retain = false
```

Those historical settings remain useful evidence for that exact fixture but do not by themselves describe the newer single-bank MCP topology.

Rationale:

- Obsidian remains the intentional Markdown producer;
- Hindsight remains a derived memory/index;
- professional questions can query governed Pantheon sources before optional informal recall;
- recall remains observable and debuggable;
- conversation history is not silently promoted into long-term memory;
- multiple producers do not compete for ownership of one durable bank.

## Security / exposure gate

#655 observed Hindsight API/MCP without authentication on the tested path and with service ports published on the LAN.

Bank isolation is not a substitute for access control:

```text
bank isolation != authorization
healthy != safe
LAN reachable != approved exposure
```

Because durable agency/project vaults now exist, broader professional-data use is blocked on the hardening work in Pantheon-Next #659:

- authoritative Portainer image pin / redeploy proof;
- private/authenticated exposure posture;
- one ingestion authority per bank;
- removal of the durable Hermes write surface unless separately authorized;
- outage/recovery qualification;
- isolated full restore drill.

This document does not claim those items are already complete.

## Hybrid synchronization direction — in stabilization

The agreed future topology is hybrid. The always-on NAS does not replace native Obsidian by doctrine.

```text
PC / portable / mobile
        │
        │ native Obsidian + future Self-hosted LiveSync
        ▼
CouchDB on always-on Synology
        │
        └─ optional Obsidian Web/Docker client
           for browser / always-available access
```

Responsibilities remain distinct:

```text
CouchDB / LiveSync = vault synchronization
Obsidian Markdown  = human workspace/source notes
Hindsight          = derived associative memory/index
Hermes             = execution, mediation and candidate generation
Pantheon           = governed professional authority
```

Self-hosted LiveSync/CouchDB and optional Obsidian Web are **not yet qualified**. They are owned by #660.

Rules for that future qualification:

- start with synthetic vaults;
- do not let independent clients write directly into one shared NAS filesystem vault;
- test create/edit/rename/delete, offline/reconnect and conflict behavior;
- do not create a second Hindsight ingestion path before the bank producer authority is decided;
- native Obsidian remains the preferred daily/offline client where installed;
- Obsidian Web/NAS is optional and may later be evaluated as an always-on client, not as a new authority.

## Additional bounded clients

Other interfaces may consume Hindsight context if they preserve the same boundaries.

For example, Rowboat is tracked separately in #661 as a possible bounded workspace client. Its own local graph/background agents remain its working context and must not automatically become Hindsight durable memory, Pantheon Knowledge, Evidence or a replacement scheduler/orchestrator.

```text
client-local memory != IFJA durable memory
client automation != Pantheon authorization
```

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

Promotion means an explicit change in responsibility, not a file move or successful recall alone.

### Personal -> Agency

If a personal domain is later deployed:

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

This workspace model does not change the registry posture:

```text
external_runtime_memory.preferred_binding = unbound
assistant-personal sandbox qualification = historical evidence
pantheon-governed external memory = forbidden
production activation = not authorized by this document
```

The current qualified Windows + Synology source/consumer relationship is better represented as:

```text
Obsidian vault
-> official one-way hindsight-obsidian source sync
-> isolated Hindsight bank
-> bounded read consumers, including Hermes MCP
```

Historical O1-O3 provider fixtures remain valid only for their exact pinned versions and must not be read as the current deployed baseline.

Observed asynchronous constraint remains useful:

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
- automatic Hindsight publication from Rowboat or another assistant;
- a LangChain or LangGraph dependency;
- authorization from successful MCP routing;
- production authorization for Hindsight, CouchDB, LiveSync or Obsidian Web.

## Final rule

```text
Obsidian organizes human work.
Synchronization moves vault state but owns no truth.
Hindsight remembers within bounded trust domains.
Hermes retrieves, connects and proposes.
Pantheon governs professional state.
Original sources remain identifiable.
Projections remain views, not authority.
One successful runtime path never creates authorization by itself.
```
