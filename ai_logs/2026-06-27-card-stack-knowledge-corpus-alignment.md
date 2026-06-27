# AI Log — Card stack knowledge corpus alignment

Date: 2026-06-27

Actor: ChatGPT

## Context

The user clarified that `Connaissance` in the card deck should cover documentary material outside projects: PLU, MAF recommendations, CCTP guides, lexicons and other non-project documentary references.

This corrected the earlier ambiguity where Connaissance could be read as including project-specific knowledge.

## Change made

Created:

- `docs/governance/CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md`

Updated:

- `docs/governance/README.md`

The new note defines:

```text
Connaissance = non-project documentary corpus, qualified or structured for professional reuse.
```

It distinguishes:

- Document / Source;
- Connaissance;
- Context;
- Evidence;
- Memory Candidate;
- Register Entry;
- Competence;
- Guide / Resource de competence;
- Template.

It also defines a Connaissances Scene organized around documentary families such as:

- Urbanisme / PLU;
- Assurance / MAF;
- CCTP / marchés;
- Réglementation;
- Construction / chantier;
- Lexiques;
- Agence / doctrine interne;
- Méthodes professionnelles;
- Références techniques.

## Boundary preserved

Documentation and navigation only.

No UI, dashboard, search engine, RAG pipeline, document ingestion engine, vector database, OCR pipeline, knowledge registry, evidence engine, memory engine, approval engine, OpenWebUI plugin, Hermes skill, connector or external action was implemented.

No Registre Probatoire entry was created.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- `Connaissance` as reusable non-project documentary corpus;
- project-specific items remain Document/Source, Context, Evidence, Memory Candidate or Register depending on use;
- PLU, MAF recommendations, CCTP guides and lexicons are good Connaissance examples;
- Connaissance is not proof by itself;
- Connaissance does not become project-owned because a project uses it.

Refused:

- classifying every project note as Connaissance;
- letting project-specific facts pollute the general knowledge corpus;
- treating Connaissance as Evidence without scoped assertion;
- treating Connaissance as canonical memory;
- treating Connaissance as a competence or template.

To verify:

- whether `AUTHORITY_INDEX.md` should receive a direct row for `CARD_STACK_KNOWLEDGE_CORPUS_ALIGNMENT.md` in a later index pass;
- whether `CARD_STACK_MODEL.md` itself should later be revised directly to replace its broader Connaissance definition.

To arbitrate:

- whether the future cockpit should separate Documents and Connaissances into two scenes or keep one scene with clear filters.
