# 2026-07-23 — Governed document lifecycle RFC

Status: validation-only intervention trace.

## Request

The maintainer requested that the complete document-lifecycle discussion be placed in the repository as a pull request.

The requested target includes:

- unclassified document drop;
- direct intake into general Knowledge;
- direct intake into one or more projects;
- flat project phase folders without mandatory subfolders;
- preservation and authorized download of the original source;
- PDF, URL, Office, image, email and connector sources;
- native extraction, OCR when required, Markdown generation and normalization;
- description, short summary and detailed summary;
- provenance-bearing chunks and embeddings;
- project Document and general Knowledge separation;
- multi-project Document links;
- multi-source Knowledge;
- a first Hermes comprehension/reformulation exchange before processing when useful;
- a structured bounded execution request after interpretation;
- simple Cockpit actions centered on search, consultation and context;
- Cockpit display of real Hermes progress when available;
- no fabricated percentages;
- Pantheon governance of scope, status, gates, index publication, activation and rollback;
- no Pantheon OCR, queue, scheduler, model host, vector store or installer.

## Active documents read

The intervention was reconciled against:

- `docs/governance/STATUS.md`;
- `docs/governance/WHAT_RUNS.md`;
- `docs/governance/AUTHORITY_INDEX.md`;
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/README.md`;
- `CONTRIBUTING.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/PANTHEON_MVP_COCKPIT_RECONCILIATION.md`;
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`.

## Classification

```text
change class: candidate support doctrine + validation-only trace
documentation state: implemented as documentation
runtime state: unchanged
protected paths touched: none
external candidate adoption: none
installation or activation: none
```

## Files changed

- added `docs/governance/DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- indexed it in `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`;
- added this intervention trace.

## Main reconciliation decisions

```text
Intake Item owns received-but-unclassified or directly targeted intake.
Source Capture owns the immutable captured bytes and hash.
Intake Intent records what the user requested.
Intake Brief records what Hermes understood and proposed.
Pipeline Run and Projection preserve external execution and derived versions.
Document Record and Project Document Link support one or more projects.
Knowledge Item and Knowledge Source Link support general multi-source Knowledge.
Index Publication remains distinct from classification and Knowledge publication.
Cockpit displays and contextualizes; Hermes executes; Pantheon governs.
```

A user's explicit destination selection may count as the classification decision. A second confirmation is not mandatory unless policy, uncertainty, sensitivity or conflict requires it.

## Non-effects

This intervention:

- installs no document engine;
- creates no Hermes Skill;
- changes no external MVP route;
- changes no schema or test;
- activates no binding;
- authorizes no real-dossier processing;
- changes no memory or Evidence status;
- creates no queue, worker or scheduler.

## Follow-up

Executable implementation belongs outside Pantheon Next:

- Cockpit, database and OpenWebUI integration in `ifanjuang/pantheon-mvp`;
- executable `pantheon-document-intake` behavior in the Hermes-side runtime or sibling executable repository;
- binding installation, health, update and activation through separate reviewed decisions.
