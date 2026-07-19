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
