# 2026-09-07 — Workspace source package and per-source Infos sidecar

Date: 2026-09-07

Status: implementation convergence trace — implementation candidate in progress.
Boundary profile: workspace_local_write_candidate.

## Change

This intervention converges the Obsidian / Workspace file-native vocabulary and the local sidecar layout around one source package.

The agreed human-facing terms are:

```text
Source
Infos
Contenu
Dialogue
Notes
```

`Connaissances` remains the existing reusable cross-project Pantheon knowledge corpus. Project Notes are not renamed or auto-promoted to Connaissances.

For a source `Plan-RDC-D.pdf`, the explicit qualification workflow may organize the source as:

```text
Plans/
└── Plan-RDC-D/
    ├── Plan-RDC-D.pdf
    ├── Plan-RDC-D.yaml
    └── Plan-RDC-D.dialogue.md
```

A later explicit ingestion operation may add:

```text
Plan-RDC-D.md
```

The Markdown content representation is therefore not created merely because the source was qualified.

## Why

The previous adjacent `document.yaml` candidate created a practical conflict when several source files shared one folder: one sidecar could be bound to only one exact source path. A deterministic `<source-basename>.yaml` sidecar removes that accidental folder-level contention and keeps each local Infos carrier recognizable if it is copied, moved or shown outside its package folder.

The package folder also keeps generated/projection artifacts close to their source without making the folder an identity owner.

The source filename remains unchanged inside the package. Generated files keep the source basename so they remain intelligible when detached from the package.

## Boundary

This change is Workspace organization and bounded local metadata only.

```text
package folder != governed identity
<basename>.yaml != Document admission
Infos != Agency Information
Notes != Connaissances
Contenu != Source
Dialogue != chat authority
qualification != ingestion
workspace move != professional currentness
Hermes candidate != Evidence
```

The first-slice YAML continues to own only the bounded `pantheon_workspace` fragment used by the human note path. It does not adopt a broad production document manifest schema and does not make semantic qualification output authoritative.

## Local distinctions

### Source

The exact professional/workspace artifact, for example:

```text
Plan-RDC-D.pdf
Photo-facade.jpg
modele.ifc
```

A single source is not a representation of the whole Project.

### Infos

`<basename>.yaml` is the local source-adjacent information carrier.

The current implementation-managed fragment uses the source filename, not the full folder path, as its local binding basis:

```yaml
pantheon_workspace:
  source_file: Plan-RDC-D.pdf
  human_note: "..."
```

This makes the source + Infos pair relocatable together without silently changing its meaning.

The filename binding remains a local package invariant only:

```text
source_file match != governed Document identity
```

### Contenu

`<basename>.md` is the human-readable/exploitable content representation produced by a separate explicit ingestion/structural-analysis path.

```text
qualification may exist without Contenu
Contenu may be regenerated from an exact source basis
Contenu != source bytes
```

### Dialogue

`<basename>.dialogue.md` is the readable local projection of source-scoped Hermes exchanges. It remains optional/dispensable and does not own server-side Work Issues or result candidates.

### Notes

Ordinary Markdown working notes remain free workspace material. A Note may relate several source packages, project Information, Project Anatomy material and reusable Connaissances.

Links are relationships, not a fifth content type. They may be expressed through Obsidian/Markdown links for humans and/or a reconstructible JSON projection for machine use where useful.

## Project-wide understanding remains composed

No new "project overview source" is introduced.

Hermes project understanding continues to come from bounded composition of relevant Project context:

```text
Project
+ several Sources
+ Informations
+ Project Anatomy
+ admitted relations/context
+ relevant Connaissances when explicitly in scope
→ Context Pack / bounded runtime context
→ Hermes synthesis/candidates
```

A `Plan-RDC-D.md` representation therefore remains local to `Plan-RDC-D.pdf`; it is never treated as the whole Project.

## Qualification/package ordering

The existing Workspace dialogue contract binds a handoff to an exact `workspace://...` path and SHA-256. Moving the source after the first durable handoff would break later targeted rework against that stored path.

The intended initial-qualification sequence is therefore:

```text
observe original source + SHA-256
→ show explicit human preview
→ human confirms local packaging + Hermes qualification
→ create <basename>/ package and move source there
→ move an existing <basename>.yaml with the source when present
→ re-observe final path and SHA-256
→ require the final digest to equal the confirmed original digest
→ build a fresh qualification preview on the final path
→ submit the final handoff
→ create/project <basename>.dialogue.md beside the final source
```

The local package mutation and the Hermes read-only handoff remain separate effects even when exposed by one explicit confirmation UI.

```text
package created != Hermes admitted
Hermes admitted != run launched
run completed != YAML truth
```

## Implemented in the current candidate branch

Branch baseline was `Pantheon-Next/main@b2085bab39b05485e5476208e90d508777417575`.

Candidate changes:

- `implementation/mvp_vertical/workspace_human_note.py`
  - sidecar changes from shared `document.yaml` to `<source-basename>.yaml`;
  - managed markers become `Pantheon workspace info`;
  - local binding uses `source_file` so source + sidecar can move together;
  - legacy `source_path` is accepted only as a compatibility read and reduced to its filename;
  - no-follow traversal, optimistic digest protection, unrelated YAML preservation, mode/owner/xattr preservation and atomic replacement remain intact.
- `implementation/mvp_vertical/workspace_collection_read.py`
  - passive observation now checks the matching `<source-basename>.yaml`;
  - Card detail label becomes `Infos YAML adjacentes`.
- tests cover independent sidecars for several source files, explicit mismatch refusal and package relocation.

## Deliberately not implemented by this slice

This slice does not yet:

- make Pantheon create/move the Workspace folder;
- make a package folder a governed object;
- generate semantic qualification fields from arbitrary Hermes prose;
- create `<basename>.md` during qualification;
- admit a Document, Evidence, Knowledge or Agency Information object;
- solve the separate exact-PDF-content transport gap to the Hermes runtime;
- add a scheduler/queue/dispatcher;
- promote a Note to Connaissance automatically.

The Obsidian plugin is the intended owner of the explicit local Vault organization effect because it already owns the user-facing vault interaction and can use Obsidian's mobile-compatible Vault/FileManager APIs. Pantheon remains the owner of bounded sidecar writes and the exact qualification/handoff contracts.

## Next convergence slices

1. Obsidian initial qualification: create `<basename>/`, move source and optional existing `<basename>.yaml`, re-preview final exact path/digest, then submit the first handoff.
2. Reconcile the current Workspace Manifest Inspector candidate documentation from shared `document.yaml` wording to per-source Infos packages without adopting a broad production schema.
3. Close exact source-content delivery to Hermes so qualification actually reads the PDF contents.
4. Close the explicit one-shot execution link from admitted handoff to Hermes return.
5. Add a structured Workspace qualification result envelope before persisting Hermes semantic candidates into `<basename>.yaml`.
6. Keep `Ingérer` separate; only that path may later produce `<basename>.md` Contenu.

## Done criteria for this slice

The sidecar portion is complete only when:

- two sources in one folder can have independent Infos YAML files;
- source + sidecar can be relocated together without invalidating the local binding;
- passive Card observation reports the matching basename YAML;
- existing non-authority boundaries remain explicit;
- tests and repository CI are green.

The full user workflow is not complete until the Obsidian package move and final-path qualification submission are implemented and verified.
