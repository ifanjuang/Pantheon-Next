# 2026-09-04 — Governed document identity candidates

## Objective

Continue P4 governed entity resolution by filling the concrete gap already named by
the Project Document Inbox: semantic candidate assistance when exact deterministic
professional lineage cannot resolve a preserved Source.

This slice does not create a generic identity engine. It extends the existing
read-only document reconciliation projection only.

## Repository state checked

Work started from current `Pantheon-Next/main`:

```text
10f7ada57f83cbfa1a8ac662c7c1e1b5d842ac71
```

The immediately preceding main change retired the Obsidian Sync alternative and did
not overlap document reconciliation or governed identity files.

Open PRs/issues and branches were checked for entity resolution, identity
reconciliation and merge/canonicalization work. No parallel P4 implementation was
found.

## Existing responsibility reused

The audit found that much of the originally expected P4 capability already exists:

- `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json` already names
  `governed_identity`; no new owner is required.
- `project_document_inbox.reconcile_source()` already performs deterministic,
  read-only Source reconciliation for exact checksum/reference, admitted bindings,
  exact professional digest and unique technical lineage.
- `project_document_admission.admit_source_as_revision()` already owns the bounded
  authorized mutation seam once a human supplies an explicit target Document.
- APU already has its own governed `identity.represents` review/application path;
  P4 must not replace or generalize it into a competing universal engine.
- generic `entity_relations` remains a semantic relation lifecycle and is not made
  an identity-merge owner.
- `DOCUMENT_IDENTITY_RECONCILIATION_OWNER_MATRIX.md` already states that Hermes may
  rank/explain candidates but must not bind identity, while exact identifiers and
  deterministic matches precede semantic assistance.

## Gap filled

A5 previously ended unresolved new-content cases with:

```text
needs_document_identity
```

and explicitly required user context or a separately admitted semantic candidate,
without implementing a bounded semantic-candidate projection.

P4 now allows `reconcile_source()` to receive optional advisory semantic candidates.
Each candidate must contain exactly:

```text
document_id
score
basis
producer
created_at
```

The projection validates that:

- the candidate Document exists;
- it belongs to the same governed Project as the Source;
- candidate IDs are unique;
- score is numeric and in `[0, 1]`;
- basis is a non-empty list;
- producer and creation timestamp are present;
- at most 50 candidates are supplied.

Candidates are sorted deterministically by descending score and then Document ID.
This ordering is presentation/review assistance only.

## Exact-first precedence

Semantic candidates are considered only after all existing deterministic paths fail.
They cannot override:

- an already admitted binding;
- Source Intake project-link posture;
- technical-capture ambiguity;
- exact professional content digest;
- unique existing professional lineage.

An exact professional match therefore wins even if a semantic caller supplies a
higher-scored competing candidate.

## Authority ceiling

The new status is:

```text
document_identity_candidates
```

It remains a read-only projection. It does not expose a selected Document and does
not persist a candidate set.

```text
candidate score != identity binding
candidate producer output != Evidence
candidate ranking != professional approval
candidate projection != persistence
candidate discovery != Document creation
Hermes confidence != admission
```

The existing authority flags remain false for professional identity confirmation,
revision admission, Evidence and project-truth mutation.

## Persistence and contracts

No SQL migration is added. No `DocumentIdentityCandidate` canonical owner or new
identity schema is created.

The candidate set is reconstructible caller-supplied review context. Professional
identity remains with `project_documents`; authorized admission remains with
`project_document_admission`.

## Tests

Added focused contract tests covering:

- advisory ranking with authority ceiling preserved;
- deterministic tie ordering without winner selection;
- unknown, duplicate and cross-Project candidate refusal;
- malformed basis/score refusal;
- exact professional digest precedence over semantic ranking.

## Out of scope

- no fuzzy/vector/model runtime inside Pantheon;
- no embedding store;
- no automatic candidate generation;
- no automatic winner;
- no identity merge/split;
- no APU identity change;
- no generic entity relation change;
- no new admission writer;
- no API/Cockpit exposure;
- no Evidence/Decision/ProjectClaim mutation;
- no migration or durable candidate store.

## Status

Implementation candidate prepared on
`feat/governed-document-identity-candidates`. Full repository CI and current-main
reconciliation remain the merge gate.
