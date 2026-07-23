# 2026-07-23 — Knowledge navigation UX extension

Status: validation-only intervention trace.

## Request

The maintainer specified that the Cockpit `Knowledge` tab should support:

- folders and nested subfolders;
- file deposit inside a selected folder;
- conversion of deposited sources into visible Knowledge cards;
- a visual distinction where folders use a gradient-filled background and Knowledge cards use only a thick gradient outline.

## Decision recorded

A dedicated UX specialization was added:

```text
docs/governance/KNOWLEDGE_NAVIGATION_UX.md
```

The specification defines:

- logical folder hierarchy rather than mandatory physical directories;
- one parent per folder and no cycles;
- optional multi-folder links for one Knowledge Item without source duplication;
- breadcrumb, grid, list, mobile and search behavior;
- file-drop intake placeholders and real Hermes progress display;
- source download posture;
- move, link, archive and permission distinctions;
- accessibility and status-color separation;
- mandatory review before a generated document is sectorized into Knowledge.

## Visual rule

```text
folder card
= full gradient-filled background

Knowledge item card
= neutral interior with a thick gradient outline
```

The gradient identifies object family, not approval, certainty, Evidence or runtime state.

Status remains expressed through separate badges, icons and text.

## Important reconciliation

The existing statement that no mandatory subfolder structure is imposed is preserved.

```text
no mandatory subfolder taxonomy
!= no user-created subfolders
```

Folders are Cockpit navigation collections. They do not require physical NAS directory creation and do not move or delete source bytes by themselves.

## Classification

```text
authority class: candidate support specification
repository state: documented non-implemented
runtime status: unchanged
protected paths touched: none
installation or activation: none
```

## Boundary

Cockpit displays and captures organizational intent.

Pantheon governs identity, scope, permissions, publication, archive and review conditions.

Hermes may process deposited sources and report progress through separately reviewed capabilities.

This extension implements no frontend, component library, upload API, database schema, physical folder operation, source store, Hermes Skill, archive service or authorization engine.
