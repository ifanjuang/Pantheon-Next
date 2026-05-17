# AI Log — README TOC, worked examples and reader-oriented next steps

Date: 2026-05-17

## Scope

Iterated on both README files following a reader review. Goal: push the bilingual front door from "very good for non-technical professionals" to "actionable for non-technical professionals", without changing doctrine.

## Files changed

- `README.md`
- `README.fr.md`
- `ai_logs/2026-05-17-readme-toc-worked-examples-reader-actions.md`

## Main changes

Added a collapsible table of contents near the top of both files. Eleven entries, anchored on existing section titles. The TOC sits inside a `<details>` block so the landing remains uncluttered.

Replaced the "in 1 minute" two-column table with five verb-first bullets covering: framing the request, keeping proof visible, leaving the decision to the professional, compartmentalizing memory, and supporting both external services and a local model. Reduces scan time and removes the previous "table inside a 1-minute summary" friction.

Replaced the generic "concrete example" section with two named, fully worked-out scenarios:

- **Law firm preparing a case management hearing** — based on real lawyer-AI use cases documented by the Conseil National des Barreaux and reported French hallucination incidents. Shows mission framing, party-name minimization before external transmission, evidence-folder content with exhibit numbers, and a candidate strategy note pending professional validation.
- **General practitioner writing a referral letter to a cardiologist** — based on guidance from the French medical council and HDS-hosting considerations. Shows mission scope, pseudonymization before any external call, evidence-folder content with clinical and biology elements, and a candidate letter signed and filed only by the doctor.

Both examples follow the same five-step pattern (mission sheet, minimization or pseudonymization, proof folder, candidate deliverable, validation), so a reader from another profession can transpose the structure.

Rewrote the "What next?" section into two distinct sub-sections:

- For the professional reader: test the doctrine on a real case, follow the project via Watch, propose a professional case as an issue, and go deeper into the doctrine documents.
- For contributors and the project team: build a fictional demo dossier, provide full sample Task Contract and Evidence Pack, document use-case packs per profession, and prepare OpenWebUI ↔ Hermes handoff examples.

The previous version listed only project priorities, which gave non-developer readers no concrete action after finishing the README.

## Research sources

Profession-specific AI use cases were grounded in public references from the Conseil National des Barreaux, Village-Justice, France Num, MACSF, Le Quotidien du Médecin, the Ordre des architectes, the Conseil Supérieur de l'Ordre des Experts-Comptables and Hub France IA. The README itself remains generic and does not cite these directly; sources support realism of the worked examples.

## Boundary check

This intervention is README copy and structure only.

It does not implement runtime behavior, OpenWebUI integration, Hermes integration, Evidence Pack generation, memory promotion, provider routing, plugin management or execution tooling.

The two worked scenarios are illustrative narratives, not executable workflows.

## Status

Both READMEs now offer a collapsible TOC, a scannable one-minute summary, two professional worked examples (legal and medical), and a reader-actionable "What next?". Total length: 448 lines per file.
