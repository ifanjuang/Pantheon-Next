# 2026-09-06 — Obsidian workspace knowledge convergence

Date: 2026-09-06

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added a detailed non-authoritative convergence record for the current Obsidian / Hermes / Pantheon workspace direction.
- Recorded five conceptual Workspace roles: source, derived representation, dialogue, knowledge note, and navigation / Map of Content.
- Recorded the current Inspector note/dialogue UX, cumulative-knowledge direction, implementation order and explicit non-decisions.
- Related the convergence to the existing Obsidian/Hindsight reference model and prior second-brain / obsidian-wiki qualification logs rather than creating a new doctrine owner.

## Why

The current direction emerged across several implementation slices and external PKM/agent references. Without one convergence trace, future work could accidentally conflate source files, derived Markdown, Hermes dialogue, durable knowledge notes, navigation notes, Hindsight memory or governed Pantheon state, or could prematurely introduce a new PKM/wiki authority.

This record preserves the reasoning while keeping implementation and authority in their existing owners.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: none.
Schema/test/CI impact: none, apart from ordinary repository validation of this documentation change.
External action: repository documentation only.
Memory behavior: none.

## Local distinctions

```text
external reference != Pantheon authority
workspace role != new schema
Markdown != source by default
knowledge note != Evidence
wikilink != governed relation
folder != governed identity
Hermes result != professional truth
dialogue log != durable professional record
```

## Objective

Capture the current Obsidian / Hermes / Pantheon workspace direction in enough detail that future implementation does not lose the distinctions reached during the September 2026 convergence work.

The goal is specifically **not** to introduce a new PKM subsystem, a new `LLM Wiki` owner, a new memory authority or a mandatory vault taxonomy. The goal is to retain the smallest useful model for the workspace and plugin while keeping existing Pantheon owners authoritative.

## Repository state checked

At the start of this record:

- `Pantheon-Next/main = 7c9bc48a26a7885618b47211a0debc4449fbb0d7` (merge #1002, Workspace Hermes dialogue + targeted rework);
- `Pantheon-plugins/main = 1e3991a15a4cd5551a776a928530382655aea8da` (merge #3, Obsidian Hermes dialogue + targeted rework);
- no open Pantheon-Next PR matching `workspace Obsidian knowledge` was found;
- existing relevant convergence records were reviewed before adding this one:
  - `ai_logs/2026/Q3/2026-08-29-optional-obsidian-second-brain-boundary.md`;
  - `ai_logs/2026/Q3/2026-08-30-obsidian-wiki-pattern-convergence.md`;
- `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` remains the current qualified/recommended reference implementation profile and already owns the important Obsidian/Hindsight boundary statements. This log does not replace or supersede it.

Before merge, `Pantheon-Next/main` advanced to `dd82fcf35e7acb9f8b8414698365e78db13a9429` through #1003 (`refactor(hermes): minimize external content admission boundary`). That change was inspected as a separate Hermes context-admission simplification and does not overlap the workspace-knowledge log path. This branch was rebuilt on that exact current `main` before requalification.

## Reference corpus considered

The following external references informed the UX/knowledge-management discussion. They are inspiration inputs only, not Pantheon authorities or dependencies:

- Steph Ango vault / `kepano-obsidian` — file-first, portable Markdown, lightweight conventions:
  - https://stephango.com/vault
  - https://github.com/kepano/kepano-obsidian
- Karpathy cumulative LLM wiki pattern — agent-maintained cumulative knowledge over source material:
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Linking Your Thinking — relation-first navigation / Maps of Content:
  - https://www.linkingyourthinking.com/
- Zettelkasten — linked notes and separation between source description, interpretation and synthesis:
  - https://zettelkasten.de/overview
- PARA — simple action-oriented filesystem organization:
  - https://fortelabs.com/blog/para/
- Jared Rhodenizer — agent/vault memory and task-specific priming patterns discussed as an implementation reference:
  - https://jaredrhod.com/

```text
external reference != Pantheon authority
useful pattern != provider adoption
similar UX != architecture equivalence
```

## Core convergence

The current direction is deliberately small:

```text
Obsidian = human-facing workspace and knowledge environment
Hermes   = reasoning / synthesis / candidate-production agent
Pantheon = governance / provenance / identity / authorization boundary
```

Pantheon should not attempt to reproduce a complete personal-knowledge-management product inside Cockpit or the Obsidian plugin. Obsidian already provides files, Markdown, links, backlinks, Bases and navigation ergonomics. Pantheon should supply the things Obsidian does not own: exact source basis, governed identities, provenance, Evidence, professional status, bounded writes, Task Contracts, Context Packs and capability/runtime authorization.

Hermes bridges the two layers, but Hermes output remains candidate/workspace material until an existing Pantheon owner explicitly accepts or governs it.

## Five conceptual Workspace roles

The following five roles are useful **conceptual distinctions**, not five new schemas or authorities.

### 1. Source

Examples:

```text
Plan-RDC-D.pdf
Photo-façade.jpg
Notice-incendie.pdf
model.ifc
```

Meaning:

- original professional/source material;
- keeps its existing source/document/image/model identity owner;
- not silently rewritten by Hermes;
- folder/name/location does not create governed identity;
- a retrieved/parsed representation does not replace the source.

```text
source bytes != extracted Markdown
source path != governed identity
source present != Evidence admission
```

### 2. Derived representation

Example:

```text
Plan-RDC-D.md
```

Meaning:

- reconstructible representation produced from one exact source version;
- current preferred document structural-analysis candidate may be Docling, but the UI/contract remains provider-neutral through `document_structural_analysis`;
- must record exact source basis and converter/config provenance when persisted;
- can become stale when the source digest changes;
- must not silently overwrite conflicting human changes.

Conceptual flow:

```text
exact source
-> document_structural_analysis
-> derived Markdown candidate
-> protected explicit write
-> source-linked derivative
```

```text
derived representation != source
converter success != professional validation
derivative currentness != Evidence admission
```

### 3. Dialogue

Example:

```text
Plan-RDC-D.dialogue.md
```

Meaning:

- readable local projection/log of human <-> Hermes work around one source;
- may contain questions, verification requests, result summaries, requests for tables/schematics/notes and rework instructions;
- dispensable by design;
- deleting it must not invalidate the source, manifest, Work Issue, Hermes result, Document or Evidence;
- disappearance resets the local projected thread in the Inspector;
- hidden markers may carry handoff/run linkage while the visible file remains normal Markdown.

Important qualification:

`dialogue.md` is **dispensable**, not guaranteed to be perfectly reconstructible byte-for-byte. A human may have written wording that is lost when deleting it. Deletion is acceptable by product design because the dialogue file is not an authority or required professional record.

```text
dialogue projection != chat authority
dialogue text != Evidence
Hermes answer != professional truth
```

### 4. Knowledge note

Examples:

```text
Sécurité incendie.md
Surfaces du projet.md
Points BET.md
Historique des modifications.md
```

Meaning:

- intentionally durable human/agent workspace synthesis;
- created or updated only after explicit workspace-persistence intent such as `crée une note`, `mets à jour notre synthèse`, `consolide cette discussion`;
- should prefer search-before-create and patch/enrich an existing natural note where possible;
- may link back to source files and derived representations;
- remains working Knowledge/workspace material unless an existing Pantheon Knowledge owner is explicitly invoked;
- should not be confused with the dialogue transcript that produced it.

Desired interaction:

```text
human: "Compare le plan et la notice incendie."
Hermes: candidate analysis in dialogue
human: "Crée une note de synthèse à côté."
-> Sécurité incendie.md
```

```text
knowledge note != Evidence
knowledge note != accepted Claim
repeated recall != promotion
Hermes-authored note != professional approval
```

### 5. Navigation / Map of Content

Examples:

```text
Projet - Synthèse.md
Réglementation - Index.md
Coordination - Synthèse.md
```

Meaning:

- optional human-readable navigation over useful workspace notes;
- may use Obsidian links, backlinks, properties or Bases;
- can be maintained manually or proposed/updated by Hermes with explicit write intent;
- is a view/navigation aid only;
- must not become Project identity, applicability authority, governed ordering or professional status.

```text
navigation map != canonical model
link graph != Project Anatomy relation
folder / MOC != governed Project
```

## Human note / manifest decision

The Inspector keeps a separate `Note / commentaire` field for durable human annotation around the selected source.

Current merged behavior:

```text
human note
-> bounded Pantheon Workspace note API
-> plugin-owned delimited fragment in adjacent document.yaml
```

The note is deliberately distinct from Hermes dialogue:

```text
Note / commentaire
= human-authored, durable, non-reconstructible workspace material
= not sent to Hermes automatically
= persisted through Pantheon

Discussion Hermes
= human/agent interaction
= projected locally to *.dialogue.md
= dispensable
```

A first non-empty human note may justify creating the minimal owned fragment in `document.yaml`. A simple file drop does not.

The current note seam does **not** adopt a full production `document.yaml` schema.

## Current Inspector UX direction

The Inspector Card remains progressively disclosed and intentionally small.

Empty/minimal source state:

```text
PLAN-RDC-D.pdf

[ Qualifier avec Hermès ]
[ Ingérer ]                 # only once the real backend path exists

Note / commentaire
[ ... ]
[ Enregistrer ]

Discussion avec Hermès
[ ... ]
[ Envoyer / Qualifier ]
```

Core display rule:

```text
information absent
-> section not rendered

information available
-> section appears
```

Always-visible concepts are limited to:

```text
file name
actions actually available
human note field
Hermes discussion input
```

Do not render decorative placeholder fields such as `Type: —`, `Indice: —`, `Résumé: —`.

Right-click and Card actions must call the same plugin/backend semantics, not separate code paths.

## Current dialogue / rework model

The merged plugin/backend deliberately do not create a new persistent chat owner.

Current pattern:

```text
initial source qualification
-> Work Issue / handoff / Hermes run/result
-> local dialogue projection

human targeted rework
-> prior candidate used only as bounded context
-> current exact source re-read
-> fresh Work Issue / handoff
-> prior Work Issue/result remains immutable
-> same local dialogue projection
```

A rework may ask Hermes to retain still-supported conclusions and verify only the challenged point, including by another provider-neutral method when available.

Example:

```text
"La date n'est pas bonne.
Garde le reste.
Vérifie le cartouche et le tableau des révisions,
et utilise une autre méthode si nécessaire."
```

Previous candidate context remains candidate-only. It is never silently promoted to truth merely because the user asks to keep part of it.

If the source digest has changed, old findings may be comparative context but must not be silently carried as qualification of the new source version.

```text
old digest != current digest
-> source version changed
-> current source must be re-read
```

## Knowledge accumulation direction

The Karpathy-style cumulative-wiki insight is retained as a **behavioral direction**, not a new `LLM Wiki` subsystem.

Useful behavior:

```text
new sources / dialogue
-> Hermes understands durable delta
-> search existing authorized workspace notes
-> update/link a natural existing note where appropriate
-> create a new note only when genuinely needed
```

Example:

```text
Plan-RDC-D.pdf
Notice-incendie.pdf
CR-BET-12.pdf
        |
        v
Hermes comparison
        |
        v
Sécurité incendie.md
```

Later source change:

```text
Plan-RDC-E.pdf appears
-> derived/source basis changes
-> Hermes may report that Sécurité incendie.md is potentially stale
-> human explicitly chooses review/update
```

This is cumulative workspace knowledge, not automatic professional currentness.

## Linking / MOC direction

LYT-style linking and Maps of Content are useful as a workspace navigation pattern:

```text
Projet - Synthèse.md
├── [[Sécurité incendie]]
├── [[Accessibilité]]
├── [[Surfaces]]
├── [[Points BET]]
└── [[Historique des indices]]
```

Hermes may suggest missing links or propose a navigation note, but this remains optional workspace organization.

Pantheon should prefer native Obsidian links/properties/Bases where they solve the UX instead of rebuilding equivalent graph/navigation UI in Cockpit.

## PARA direction

PARA contributes one narrow principle: filesystem organization should remain understandable and action-oriented.

Pantheon must **not** adopt PARA folder names as governed identity semantics. An IFJA vault may use projects/resources/archive-like organization if useful, but:

```text
folder = convenience
folder != Project
folder movement != governed lifecycle transition
```

The plugin must discover and respect the user's existing folder organization rather than bootstrap or require a global folder taxonomy.

## Zettelkasten direction

The useful Zettelkasten insight is conceptual separation between:

```text
source description / extraction
interpretation
synthesis
```

Pantheon should preserve that distinction in provenance and UI, but should **not** force a note-per-fact or atomic-note topology for professional project material.

Fine-grained governed facts/relations belong in existing owners such as Project Anatomy when appropriate. Markdown notes should be created at a useful human knowledge granularity, not because a methodology requires atomization.

## Task-specific priming direction

The useful `AI memory vault` / task-priming pattern is that an agent should receive context appropriate to the current job, not an indiscriminate whole-vault dump.

Pantheon already has the correct generic owners for this behavior:

```text
Task Contract
+
Context Pack
+
bounded Hindsight retrieval when selected
+
Project Anatomy / source context as authorized
```

Do not introduce parallel files such as a second permanent Hermes project-memory authority solely to implement priming.

```text
task priming != memory authority
context selected != truth
retrieved context != Evidence
```

## Workspace maintenance / lint direction

The previously accepted report-only maintenance posture remains valid and is strengthened by this convergence.

Potential future explicit `Lint workspace` / maintenance behavior may report:

- broken or malformed links;
- orphan candidate notes;
- likely duplicate notes;
- stale summaries based on older source digests;
- contradiction candidates;
- missing useful cross-links;
- derived Markdown whose source basis no longer matches the current source;
- dialogue projections whose source has moved/deleted.

Default output is findings only.

```text
lint finding != confirmed defect
stale candidate != automatic rewrite authorization
contradiction candidate != adjudication
clean lint != professional currentness
```

Automatic whole-vault rewriting, contradiction resolution, renaming, archiving or cross-note propagation remains excluded unless later bounded by a demonstrated requirement and existing write owners.

## Plugin product boundary

The plugin should remain a thin Obsidian assistant rather than becoming a parallel document-management application.

Primary local surface:

```text
selected source
-> minimal Inspector Card
-> exact-source actions
-> human note
-> Hermes discussion
-> optional production of standard Markdown artifacts
```

Expected future Hermès outputs from dialogue may include:

```text
[ Créer une note ]
[ Créer un tableau ]
[ Créer un schéma ]
```

The resulting artifacts should be ordinary readable Markdown whenever possible and should live in the workspace under explicit user-directed placement.

The plugin should not require Pantheon-specific rendering for ordinary knowledge notes to remain useful.

## Current implementation status at this record

Merged and available in the current development baseline:

- Obsidian Inspector V0;
- active-source minimal Card;
- durable human `Note / commentaire` through bounded `document.yaml` fragment;
- file-explorer contextual actions;
- explicit PDF qualification preview/submit;
- local `<basename>.dialogue.md` creation after explicit Hermes interaction;
- projection of returned Hermes candidate material;
- targeted `Refaire avec Hermès` through a fresh handoff/Work Issue;
- deletion of `.dialogue.md` as a local reset without invalidating Pantheon state;
- session-only Pantheon editor token in the plugin.

Still open / not yet demonstrated end-to-end:

1. automatic/operational Hermes launch bridge after plugin handoff creation;
2. packaged/released plugin installation rather than development/manual build only;
3. image/scan qualification for JPG/JPEG/PNG/TIFF/WEBP;
4. bounded `Ingérer` path through `document_structural_analysis` and protected Markdown persistence;
5. explicit creation/update of durable knowledge notes/tables/schematics from dialogue;
6. optional link/MOC maintenance and workspace lint after real usage demonstrates the need.

## Recommended implementation order

Do not jump directly to a generalized PKM or wiki subsystem.

Current priority order:

```text
1. Close plugin end-to-end Hermes execution
   click -> admitted launch -> Hermes -> return -> Card/dialogue

2. Qualify real installation/release path
   install plugin in a real IFJA vault
   run one exact PDF dialogue/rework scenario

3. Add bounded ingestion
   source -> document_structural_analysis -> protected derived Markdown

4. Add explicit production from dialogue
   note / table / schema

5. Add image/scan qualification where the real source-reading path is qualified

6. Observe real project usage

7. Only then formalize link maintenance, MOC generation, stale-knowledge lint or any role metadata that proves necessary
```

The ordering may change if repository state demonstrates that an implementation already covers one of these seams. Re-check `main`, open PRs/issues and current owners before each slice.

## Explicit non-decisions

This convergence does **not** decide or authorize:

- a mandatory PARA vault folder structure;
- Zettelkasten IDs or one-note-per-concept rules;
- a new `LLM Wiki` database/service;
- automatic whole-vault Knowledge maintenance;
- a new chat persistence owner;
- direct Hermes writes to Hindsight;
- frontmatter as governed identity/provenance authority;
- five production schemas named `source`, `derived`, `dialogue`, `knowledge`, `navigation`;
- automatic Document or Evidence admission from Markdown creation;
- replacing Project Anatomy with wikilinks;
- replacing Hindsight with workspace Markdown;
- replacing Pantheon Knowledge owners with Obsidian files;
- binding generic runtime memory to a provider;
- Docling becoming the permanent UI/architecture contract.

The five workspace roles remain conceptual until real implementation needs justify a minimal contract field or explicit owner extension.

## Preserved authority boundaries

```text
retrieved data != truth
memory != Evidence
execution success != authorization
projection != persistence
folder != governed identity
Markdown != source by default
Hermes result != professional truth
knowledge note != Evidence
wikilink != governed relation
navigation note != Project identity
derived representation != source
human note != Hermes result
dialogue log != durable professional record
```

## Relationship to existing records

This record complements rather than duplicates:

- `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`
  - owns the qualified recommended reference implementation profile and provider-neutral responsibility split;
- `ai_logs/2026/Q3/2026-08-29-optional-obsidian-second-brain-boundary.md`
  - records that second-brain behavior is optional and subordinate to existing workspace/manifest/memory/governance owners;
- `ai_logs/2026/Q3/2026-08-30-obsidian-wiki-pattern-convergence.md`
  - records the bounded report-only maintenance patterns and rejected provider-wide adoption;
- Workspace qualification/dialogue implementation merged through #991, #994, #999 and #1002;
- Pantheon-plugins Inspector V0 and dialogue/rework implementation merged through plugin PRs #2 and #3.

If future work promotes one of the conceptual roles into a real contract, update the actual owning contract/schema/test and treat this log as historical convergence context rather than authority.

## Done criteria for this record

This record is complete when the direction is recoverable without relying on conversation history:

- why Obsidian stays the human knowledge/workspace environment is explicit;
- why Pantheon does not become a PKM product is explicit;
- the five conceptual workspace roles are distinguishable;
- dialogue vs durable human note vs derived representation vs knowledge note is explicit;
- external PKM references are retained as inspiration, not authority;
- implementation order and current gaps are recorded;
- governance non-equivalences remain visible;
- no runtime, schema, provider binding or professional state changes merely because this log exists.

## Status

Recorded as a non-authoritative convergence trace. No runtime, binding, schema, Project identity, Evidence, Knowledge approval, Hindsight state or Workspace file outside this repository is changed by this record.
