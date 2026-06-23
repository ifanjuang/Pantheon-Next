# MVP dossier fictif — Architecture

Status: fictional example — document intelligence and evidence workflow scaffold.

This dossier is entirely fictive.

It is not a real project, not a client file, not professional advice, not a deliverable and not a Registre Probatoire entry.

## Purpose

This example exists to test a narrow Pantheon Next vertical slice:

```text
Document Source
-> Source Inventory Candidate
-> Fragment Candidate
-> Retrieval / Graph Candidate
-> Evidence Pack Candidate
-> Result Candidate
-> User Decision Gate
-> human decision
```

The goal is not to test a full GraphRAG platform first.

The goal is to test whether the system can separate:

```text
received source;
source authority;
fragment;
claim;
assumption;
contradiction;
risk;
missing evidence;
result candidate;
human decision.
```

## Boundaries

```text
No auto-sync.
No MCP tool.
No external connector.
No cloud parser by default.
No memory promotion.
No external action.
No client-facing delivery.
No schema change.
No runtime created by this folder.
```

## Recommended first run

1. Read `corpus/00_manifest.md`.
2. Create a Context Pack Candidate using `templates/architecture/context_pack_candidate.md`.
3. Create an Evidence Pack Candidate using `templates/architecture/evidence_pack_candidate.md`.
4. Create a Result Candidate using `templates/architecture/result_candidate_note.md`.
5. Stop at a User Decision Gate.

## Corpus

The corpus contains 10 small Markdown source documents:

```text
01_mail_client_programme.md
02_extrait_plu_fictif.md
03_notice_site_existante.md
04_cctp_lot_maconnerie.md
05_cctp_lot_menuiseries.md
06_cr_chantier_fictif.md
07_devis_entreprise_fictif.md
08_note_structure_fictive.md
09_notice_thermique_fictive.md
10_photo_commentee_fictive.md
```

## Built-in tensions to detect

```text
- the client asks for a fast external-facing answer;
- the PLU excerpt is fictive and must not be treated as current law;
- the masonry CCTP suggests opening enlargement without structural confirmation;
- the site meeting report states that the existing lintel is unknown;
- the contractor estimate excludes structural reinforcement;
- the thermal note assumes insulation continuity that other sources do not prove;
- photo comments suggest dampness but do not prove pathology;
- no plan dimensioned at scale is provided.
```

## Expected MVP behavior

A good run should produce:

```text
- corpus inventory;
- received / absent / excluded source list;
- source authority classes;
- fragment list;
- supported claims;
- unsupported claims;
- contradictions;
- missing documents;
- architecture-domain risk triggers;
- Result Candidate only;
- clear User Decision Gate.
```

## Expected refusal / gap behavior

The system should refuse to produce:

```text
- a definitive regulatory conclusion;
- a structural validation;
- a client-ready instruction;
- a contractor order;
- a Registre Probatoire memory;
- a transmitted email;
- a final professional visa.
```
