# Run 001 — Task Contract Candidate

Status: run output candidate — fictional MVP manual run.

This document is not an executable instruction, not an approval, not professional validation and not a client-facing deliverable.

## Task identity

```text
task_id: TC-MVP-ARCH-FICTIF-001-RUN-001
project_alias: MVP-ARCH-FICTIF-001
request_date: 2026-06-22
requested_by: Pantheon Next manual MVP slice
prepared_for: internal governance review
```

## User request

```text
Original request:
Run the fictive architecture MVP slice manually from the admitted corpus.

Normalized request:
Create an internal Context Pack Candidate, Evidence Pack Candidate and Result Candidate from the 10 fictive corpus documents, preserving source status, contradictions, missing evidence and decision gates.
```

## Scope

```text
In scope:
- classify the 10 fictive source documents;
- identify missing documents;
- extract material claims and source fragments;
- surface contradictions and risk triggers;
- prepare a Result Candidate for internal review.

Out of scope:
- regulatory validation;
- structural validation;
- thermal validation;
- contractor instruction;
- client-facing email;
- Registre Probatoire entry;
- GraphRAG installation or runtime test;
- Flexible GraphRAG ingestion;
- auto-sync, MCP, connector or cloud parser use.

Unknown / requires confirmation:
- whether graph extraction should be tested later;
- whether a future sandbox may use cloud parsing on non-sensitive material;
- whether the MVP should later include a UI decision card.
```

## Admitted corpus

```text
Context Pack Candidate ref: CP-MVP-ARCH-FICTIF-001-RUN-001
Corpus manifest ref: examples/architecture/mvp_dossier_fictif/corpus/00_manifest.md
Allowed source folder: examples/architecture/mvp_dossier_fictif/corpus/
Excluded source folders: all other repository content for this run
```

## Requested effect

```text
requested_effect: internal_state_change

Reason:
This run creates candidate review artifacts inside a fictional example folder. It does not execute externally and does not create canonical state.
```

## Allowed outputs

```text
- Context Pack Candidate
- Evidence Pack Candidate
- Result Candidate
- Capability Gap
- User Decision Gate Candidate
```

## Forbidden outputs

```text
- approval
- professional validation
- final regulatory conclusion
- structural validation
- thermal regulatory validation
- client-facing delivery
- Registre Probatoire entry
- canonical memory
- external send
- contractor instruction
- commit / publish / file to third party
- autonomous ingestion or auto-sync
```

## Evidence expectation

```text
Every material claim must link to one or more source refs.
Claims without sufficient support must be marked unsupported, contradicted or assumption.
Contradictions must be surfaced rather than smoothed over.
Missing documents must be listed.
Retrieved excerpts or source snippets are candidates, not proof.
```

## Approval ceiling

```text
approval_ceiling: C1

Meaning:
Internal candidate review only. No external delivery, no client/contractor response, no memory promotion.
```

## Return expected

```text
handoff_delivery_status: not_sent
runtime_task_status: success
result_candidate: examples/architecture/mvp_dossier_fictif/run_001_manual/03_result_candidate_note.md
evidence_pack_candidate: examples/architecture/mvp_dossier_fictif/run_001_manual/02_evidence_pack_candidate.md
capability_gaps: see Evidence Pack Candidate and Result Candidate
approval_gap: external action and stronger conclusion require explicit human gate
memory_impact: none; no Registre Probatoire entry proposed
external_effect_status: none
unchanged_objects: schemas, tests, operations, platform, Docker, .env, runtime, connectors, databases
```

## Stop conditions applied

```text
- no definitive PLU conclusion because PLU source is fictive and not official;
- no structural validation because linteau, wall function and reinforcement are unresolved;
- no contractor response because external action lacks approval and evidence;
- no thermal validation because wall composition and dimensions are missing;
- no memory promotion because this is a fictional MVP run.
```
