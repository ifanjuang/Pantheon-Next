# Pantheon MVP

Status: external executable candidate — not adopted by Pantheon Next.

This repository hosts the executable MVP vertical slice for a governed Pantheon task loop.

It is external to Pantheon Next.

It may execute deterministic proof-loop code, tests and local fixtures.

It must not govern, approve, validate professional truth, promote memory, send external messages, schedule work, route providers or become Pantheon Next.

The candidate also contains a first controlled Work Issue persistence slice:
PostgreSQL stores issues, comments, Hermes run records and append-only material
events; Hermes receives no direct database authority. This storage is not a
queue, scheduler or automatic approval path.

```text
Pantheon Next governs.
Hermes-side execution occupies the runtime seat.
OpenWebUI or another cockpit exposes the review surface.
The human decides.
```

## Current repository status

```text
repo: ifanjuang/pantheon-mvp
status: Block 1 + Block 2 drafting seam present / adoption gates 1-7 have review evidence
adoption: not adopted
activation: not activated
production use: forbidden
```

The code in this repository remains classified as an external executable candidate until reviewed against Pantheon Next governance.

## Required boundaries

The repository must preserve these distinctions:

```text
external_repo != Pantheon runtime
stand_in_runner != Hermes Agent
terminal_gate != OpenWebUI cockpit
runtime_success != evidence
result_candidate != approved_result
evidence_pack_candidate != validated_evidence
draft != external_send_authorization
test_pass != adoption
```

---

# Executable vertical slice

The executable MVP vertical slice of the Pantheon Next governed task loop
(`MVP_GOVERNED_TASK_LOOP.md`), hosted in this separate repository per the
Option A arbitration of 2026-07-08 (`HERMES_CODE_HOSTING_BOUNDARY.md`,
`ai_logs/2026-07-08-hosting-arbitration-option-a.md` in Pantheon-Next). It
covers Block 1 (bounded ingestion, scoped retrieval, candidate/refusal) plus
the Block 2 drafting seam; the live LLM Drafter remains a Hermes-side slot.

## Boundary contract

This repository executes; it does not govern. It consumes doctrine, schemas
and validators from Pantheon-Next (vendored under `mvp_vertical/vendor/pantheon/`
with their upstream commit recorded, shipped as package data) and pushes
nothing executable back.

What this code does: bounded ingestion of a Task Contract's declared
sources into pgvector; **scope-filtered-in-SQL** retrieval; deterministic
candidate production (Result Candidate + Evidence Pack Candidate) or a
refusal / capability-gap report.

What this code never does: approve, send, promote memory, schedule, queue,
route providers, or read a source the contract did not declare.

```text
indexed            ≠ evidence
retrieved          ≠ truth
runtime_success    ≠ approval
```

## Quickstart

```bash
docker compose up -d              # pgvector on :5433
python -m pip install -e ".[test]"

# step 4 — bounded ingestion (declared sources only)
mvp-vertical ingest --contract dossiers/devis_reprise/task_contract.yaml

# step 4-5 — scoped retrieval and candidate return
mvp-vertical run --contract dossiers/devis_reprise/task_contract.yaml \
  --question "le devis correspond-il au périmètre du CCTP pour le lot 06 ?" \
  --output out/candidates.yaml

# the refusal path (Block 1 acceptance criterion)
mvp-vertical run --contract dossiers/devis_reprise/task_contract.yaml \
  --question "quel est le taux d'imposition au Portugal ?"

pytest -v                         # acceptance tests, incl. perimeter-breach test
```

## Document ingestion with Docling

The minimal document vertical keeps originals in the caller-controlled NAS
mount and persists only derived structure, chunks, provenance and embeddings in
PostgreSQL. Markdown and plain text retain the direct path. PDF, DOCX, PPTX,
XLSX, images and other binary documents use a pinned, self-hosted Docling Serve
adapter over its stable v1 API.

```bash
# Optional document profile; port is bound to loopback, not all interfaces.
docker compose --profile documents up -d

export DOCLING_SERVE_URL=http://127.0.0.1:5001
export DOCLING_SERVE_VERSION=v1.21.0

mvp-vertical ingest --contract dossiers/my_project/task_contract.yaml --root /mnt/nas
mvp-vertical intake-document \
  --contract dossiers/my_project/task_contract.yaml \
  --root /mnt/nas \
  --source-ref \
  'projects/MAISON-A/30_DCE/MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf'
mvp-vertical document-card \
  --dossier my_project \
  --source-ref \
  'projects/MAISON-A/30_DCE/MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf'
```

The adapter submits exactly one already-declared, root-contained file. It does
not crawl the NAS, accept an undeclared URL or let Docling become a source of
truth. The source digest plus Docling version and conversion-configuration
digest form the extraction cache identity. A failed or partial conversion is a
visible card status, never a silent success.

### Controlled NAS intake and naming

`intake-document` is the incremental path for daily use. It accepts one exact
`source_ref`, refuses it unless the Task Contract declared it, checks that the
resolved file stays below the mounted `--root`, validates its name and phase,
then replaces only that document's chunks. Other project documents remain
searchable. There is no implicit NAS crawl.

The project hierarchy is deliberately shallow:

```text
00_Gestion
10_Conception
20_Autorisations
30_DCE
40_Marche
50_Chantier
60_Reception
90_Sinistres
```

Project documents use the strict convention:

```text
Projet_indice_phase_distributeur_type_objet_date.ext
MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf
```

Indices use `A1`, `B1`, `B2`, etc. Dates use `YYYY-MM-DD`. Underscores are
reserved for the seven structural fields; compound values use hyphens. The
phase in the filename must match its direct parent folder. Parsed fields are
persisted separately from the original and exposed by the Project Document
Card as validated naming metadata.

Persistent roles:

```text
NAS                         original and distributed/contractual exports
source_documents            stable source registry and current analysis state
extraction_runs             Docling structure, provenance, versions and quality
chunks + pgvector           scoped retrieval units and embeddings
Project Document Card       projection only; not source, evidence or memory
```

## Design notes

- **Embedder**: deterministic local feature-hashing (`mvp_vertical/embedder.py`).
  Retrieval *quality* is not Block 1's subject; the scope boundary is. Zero
  data leaves the machine. Swapping in a real model is a reviewed decision,
  because it is the data-exposure decision.
- **Drafting**: a seam (`mvp_vertical/drafting.py`). The default drafter is
  deterministic and dossier-general — it assembles retrieved passages and
  asserts nothing; `verify_draft` rejects any citation to evidence not
  retrieved. The live LLM slot is a Hermes-side `Drafter`; this repository
  never wires or routes a provider.
- **Fixtures**: the `devis_reprise` dossier is fictional and carries the
  deliberate quote/CCTP contradiction (quote item 4 covers T2+T3; CCTP 3.2
  limits lot 06 to T2). The runner must *preserve* it, never resolve it.

## Relation to Pantheon-Next

| Here | There |
|---|---|
| runner, ingestion, store, fixtures-as-files | doctrine, schemas, guards, validator |
| produces candidates | defines what a candidate is |
| refuses outside the contract | decides at the gate |

The governance schema is vendored from Pantheon-Next at `UPSTREAM_COMMIT`. A
report-only monitor (`tools/check_schema_drift.py`, run weekly by the
`Schema drift monitor` workflow) compares the vendored copy against upstream and
flags a **structural** drift when a re-vendoring is due — a new upstream commit
alone is not treated as drift.
