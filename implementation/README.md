# pantheon-mvp-vertical

Executable **Block 1** of the Pantheon Next MVP governed task loop
(`MVP_GOVERNED_TASK_LOOP.md`), hosted in a separate repository per the
Option A arbitration of 2026-07-08 (`HERMES_CODE_HOSTING_BOUNDARY.md`,
`ai_logs/2026-07-08-hosting-arbitration-option-a.md` in Pantheon-Next).

## Boundary contract

This repository executes; it does not govern. It consumes doctrine, schemas
and validators from Pantheon-Next (vendored under `vendor/pantheon/` with
their upstream commit recorded) and pushes nothing executable back.

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
- **Drafting**: template-based and deterministic in Block 1. The LLM slot
  belongs to the Hermes profile (Block 2+).
- **Fixtures**: the `devis_reprise` dossier is fictional and carries the
  deliberate quote/CCTP contradiction (quote item 4 covers T2+T3; CCTP 3.2
  limits lot 06 to T2). The runner must *preserve* it, never resolve it.

## Relation to Pantheon-Next

| Here | There |
|---|---|
| runner, ingestion, store, fixtures-as-files | doctrine, schemas, guards, validator |
| produces candidates | defines what a candidate is |
| refuses outside the contract | decides at the gate |
