# Adaptive project lifecycle and Cockpit plan — 2026-08-05

Status: completed documentation trace — no implementation or activation.

## Objective

Record the converged implementation plan for a project lifecycle that can begin
from any practical agency input and remain coherent through design, works,
reception, GPA, claim and dispute, while keeping the Cockpit progressively simple.

## Repository state checked

```text
Pantheon-Next main
latest observed merge: a55fa3e0e5cf15e872eaa536228a58166c1be3d3
execution-result and review contract present

pantheon-mvp main
latest observed commit: 76929853ab30441f92cbcc14e1c49c6a4f622b1e
execution-result persistence present
Hermes 0.20.0 ephemeral laboratory acceptance present
```

Open MVP work considered:

```text
#93  WorkIssue close_reason validation
#94  New information synthetic Project child projection
#165 mobile editor review, deferred pending convergence
#227 real agency/NAS Hermes qualification
```

Branch posture considered:

```text
agent/execution-result-persistence-clean
  no unique commit ahead of main; obsolete work branch

agent/mobile-knowledge-variant-review
  divergent; useful UX may be recovered later
  parallel review storage/lifecycle must not be merged as a second architecture
```

## Decisions recorded

1. The Cockpit is an adaptive projection, not a fixed storage tree.
2. Project navigation uses four primary sections: overview, content, attention and
   decisions.
3. Contacts, memory, tools, APU and Evidence are optional lenses.
4. Phase, reception, claim and dispute are facets/contexts, not exclusive folders.
5. Any source may be preserved before full classification.
6. `document_source` and Dossier Situation Intake are reused; no universal
   `InboxItem` concept is created.
7. `Information Card` remains a broad visual family, while an Information semantic
   object is limited to intentionally authored professional content.
8. Documents are not duplicated as Information solely for display.
9. ProjectClaims carry consequential project values requiring provenance.
10. The existing ExecutionResult -> ResultCandidate -> ClarificationRequest ->
    ReviewDisposition path remains the single Hermes review conduit.
11. Review does not apply a project mutation; a separate domain command is required.
12. Mnemosyne remains optional external cognitive memory and non-blocking for
    project reads.
13. The first usable increment must work without Hermes, Mnemosyne, APU, Paperless,
    Docling or Revit.

## Artifact added

```text
docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md
```

The roadmap defines authority distinctions, target UX hierarchy, lifecycle
coverage, source intake, document/Information convergence, ProjectClaim use, one
attention surface, governed application, Mnemosyne boundaries, ten implementation
slices, PR sequencing and completion criteria.

## Non-effects

```text
no schema
no migration
no API
no Cockpit implementation
no adapter
no runtime execution
no installation
no activation
no task authorization
no Evidence admission
no memory promotion
no project mutation
```

```text
plan documented != implementation completed
review path present != domain mutation implemented
lab acceptance != agency production qualification
```
