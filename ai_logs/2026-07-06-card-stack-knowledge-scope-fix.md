# Card Stack Knowledge Scope Fix

Date: 2026-07-06

Status: documented non-implemented

Type: follow-up correction

Related PR: #294

Related issue: #293

## Summary

Corrected `docs/governance/CARD_STACK_HARDENING_NOTE.md` after review feedback identified that `Connaissance Card` had been scoped too broadly.

The hardening note now keeps `Connaissance Card` reserved for non-project knowledge corpus and routes project files, project-specific facts and dossier material to the proper governed objects: Document/Source, Context, Evidence, Memory Candidate or Register.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Correction

Before:

```text
Connaissance Card = professional, regulatory, contractual, project or dossier knowledge.
```

After:

```text
Connaissance Card = non-project professional, regulatory, contractual, methodological or corpus knowledge.
```

Additional forbidden collapses:

```text
Project fact ≠ Connaissance Card.
Dossier material ≠ reusable knowledge corpus.
```

## Boundary

Documentation only.

No schema, test, UI, renderer, runtime, OpenWebUI plugin, Hermes skill, connector, approval engine, memory engine or external action.
