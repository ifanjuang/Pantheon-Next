# Changelog

All notable changes to this repository. This is an **external executable
candidate** — every release is a reproducibility snapshot of a proof loop, never
a production or adoption event (`test_pass != adoption`).

## Unreleased

- **Real HTTP policy client** (`policy_gate.HttpPolicyClient`) — consults the
  Pantheon `mcp-server` PDP over HTTP (`/v1/policy/preflights:evaluate`,
  `/v1/policy/decisions:validate`) with a bearer key. Any transport/HTTP error
  becomes a fail-closed block via `enforce_consequential`. `httpx` is lazily
  imported (core package unaffected); added to the `cockpit` extra. 5 tests use
  a mock transport, no network.
- **Capability management slice** (`capability_manager.py`, Phase D) — a bounded
  governed lifecycle for one capability: `plan_action` authors a candidate,
  `governed_execute` routes a consequential action (install / enable / update /
  suspend / retire) through the chokepoint and asks an injected native executor
  to perform exactly one operation, returning a technical receipt and a fresh
  observation. It executes nothing itself; the executor is external. 8 tests.

- **Policy chokepoint seam** (`mvp_vertical/policy_gate.py`) — a consequential
  effect now routes through a `PolicyClient` (Pantheon preflight + decision
  validation) before it runs. Fail-closed on an unavailable PDP or a non-allow
  verdict; smart-approvals are neutralized structurally (the seam never
  auto-approves; only an eligible preflight plus a valid human decision permit
  the effect). Ships with a deterministic offline stand-in and 6 tests; a live
  Pantheon PDP is not wired here.

- **Governance schemas re-vendored** to Pantheon-Next `UPSTREAM_COMMIT f8bc3bd`
  (PR #50), superseding the v0.2.0 snapshot pin `782afb47`. All three vendored
  schemas and the derived decision vocabulary remain structurally coherent with
  upstream. The v0.2.0 notes below intentionally keep their original `782afb47`
  citation as the historical snapshot pin.
- **Offline pin guard added** — `tools/check_schema_drift.py` now checks that the
  live `GOVERNANCE_STATUS.md` pin citation equals
  `mvp_vertical/vendor/pantheon/UPSTREAM_COMMIT`, so a future re-vendoring cannot
  leave the status document citing a stale commit. Hermetic, network-free, run in
  the blocking test lane.

## v0.2.0 — candidate milestone

> **Status: external executable candidate.** Not adopted, not installed, not
> activated by Pantheon Next. **Production use is forbidden.** Adoption Gate 8
> (human approval for activation) remains **OPEN**. Green tests are not adoption
> (`test_pass != adoption`); a candidate is not an approval.
>
> Pantheon Next governs the status of this loop. Hermes-side execution occupies
> the runtime seat. OpenWebUI / a cockpit exposes the review surface. **The human
> decides.**

This milestone snapshots the executable MVP vertical of the Pantheon Next
governed task loop, hosted in this separate repository (Option A arbitration,
2026-07-08). It is a **reproducibility tag over a proof loop**, not a product.

- 157 tests, CI green on `main` (unit lane + a pgvector integration lane that
  **fails rather than skips** when the database is configured).
- 3 governance schemas vendored from Pantheon-Next at
  `UPSTREAM_COMMIT 782afb47`, every emitted object validated against them.

### Governed task loop — Blocks 1–3

- **Block 1 — bounded ingestion & scoped retrieval.** Ingestion reads only a
  Task Contract's *declared* sources; source paths are checked for absolute /
  `..` / symlink escape before any file is touched. Retrieval filters the
  declared perimeter **in SQL before** vector ranking — a query cannot see
  outside the contract by construction. Out-of-perimeter and forbidden asks
  return a motivated refusal, never an improvisation. (PRs #4–#8)
- **Block 2 — drafting seam.** A `Drafter` protocol with a deterministic,
  dossier-general default; the live LLM slot is a Hermes-side drafter, never
  wired here (provider routing forbidden). A structural verifier rejects a draft
  that cites evidence it was not given. Advisory, non-blocking flags surface to
  the human gate: professional-verdict, grounding visibility, duty-of-care.
  (PRs #9–#11, #19, #25)
- **Block 3 — human decision gate & register.** A terminal decision-gate
  stand-in records a human `decision_record` and **executes no consequence** —
  even `approve` sends nothing. The system may never sign (Gate 5). A register
  candidate can be proposed only from a gate-produced approved decision plus an
  explicit, human retention authorization; it is **never** memory. (PRs #7,
  #18, #20)

### External-review hardening lot

Driven by an adversarial review, all *candidate* evidence — none of it adoption:

- Gate input validation + a **closed decision vocabulary** read from a governed
  file, never from the candidate stream (PR #21).
- Register-seam anti-forgery: only a gate-shaped decision (digests, identity
  assurance, non-system signer) can propose retention (PR #22).
- Decision & retrieval **identity and digests** — content digests bind a
  decision to exactly what was reviewed; every retrieved chunk carries its
  contract / ingestion / source identity for audit (PRs #16, #17, #28).
- **Systematic runner-output schema validation** — every emitted object is
  validated in-band, so a divergent shape cannot ship silently (PR #29).
- CI **fails rather than skips** when pgvector is configured (PR #27); vendored
  schema + vocabulary **shipped as package data** so an installed wheel works
  (PR #30); deontological anchor for the advisory flags (PRs #25, #31).
- Test scenarios from real, anonymized practice: 5 dossiers, standard and
  critical situations C1–C8 / S1–S6 (PRs #24, #26).

### Document → Knowledge vertical

A minimal, bounded document vertical. Originals stay in the caller-controlled
NAS mount; only derived structure, chunks, provenance and embeddings are
persisted. **Docling never becomes a source of truth.**

- **Bounded Docling ingestion (PR #36).** Markdown / plain text keep the direct
  path; PDF, DOCX, PPTX, XLSX, images go through a pinned, self-hosted Docling
  Serve adapter over its stable v1 API, bound to loopback. The extraction cache
  identity is `source_digest + Docling version + conversion-config digest`. A
  failed or partial conversion is a **visible card status, never a silent
  success**.
- **Controlled NAS intake & naming (PR #37).** `intake-document` accepts exactly
  one already-declared, root-contained `source_ref`; it refuses anything the
  contract did not declare, validates the strict name
  (`Projet_indice_phase_distributeur_type_objet_date.ext`) and the phase↔folder
  match, then replaces **only that document's** chunks. No implicit NAS crawl.
- **Cockpit API — three key-scoped surfaces (PRs #38, #41).** One bounded API
  (`cockpit_api.py`) with three separate bearer keys, each strictly scoped:
  - **read key** — `GET`-only Document / Knowledge **cards**: a thin read-only
    projection over PostgreSQL and a read-only NAS mount. A projection, never
    source / evidence / memory. (the OpenWebUI Document Card path, PR #38)
  - **editor key** — the mobile editor's **constrained write** surface:
    transactional, versioned Knowledge publication / revision and edit requests
    only. It **cannot** mutate NAS originals, admit Evidence, promote memory or
    approve professional truth. Publication is optimistic-versioned with
    immutable idempotency keys; `knowledge_events` is append-only. (PR #41)
  - **hermes key** — an edit-request *proposal* endpoint for an admitted
    Hermes adapter; a queued edit request is not a Hermes proposal, and Hermes
    holds no database credentials.
- **Mobile offline editor (PR #41).** A PWA served from the same surface for
  offline Markdown editing; offline replay is not overwrite permission.
- **Controlled Work Issue persistence (PR #35).** PostgreSQL stores issues,
  comments, Hermes run records and append-only material events; Hermes receives
  **no direct database authority**. Not a queue, scheduler or auto-approval.

New non-equivalences this vertical must preserve:
`Knowledge != Evidence` · `offline replay != overwrite permission` ·
`queued edit request != Hermes proposal`.

### Coherence with Pantheon-Next

- Three schemas vendored at `UPSTREAM_COMMIT 782afb47`:
  `mvp_governed_loop_objects`, `work_issue_slice`, `document_knowledge_slice`.
- A **report-only drift monitor** (`tools/check_schema_drift.py`, weekly
  workflow) auto-discovers every vendored `*.schema.yaml` and flags a
  **structural** drift against live upstream — a new upstream commit alone is not
  drift. All three are currently coherent. (PRs #33, #34, #42)

### What this release is NOT

- Not adopted, not installed, not activated by Pantheon Next.
- Not production-usable: the terminal decision gate records a **declared**
  identity, never an authenticated principal (`declared != authenticated`) — the
  cockpit's bearer keys are client/transport auth, not proof of who decided at
  the gate; there is no append-only decision journal, no live LLM, no transport.
- Not a governance authority: it consumes doctrine and schemas from
  Pantheon-Next and pushes nothing executable back.

---

*Provenance note: these notes are compiled from the Git history and the shipped
docs. Blocks 1–3, the hardening lot, the test scenarios and the drift monitor
were built and reviewed in-session; the document / knowledge / mobile verticals
(PRs #35–#41) are summarized from their merged history and code, not from an
independent line-by-line review.*
