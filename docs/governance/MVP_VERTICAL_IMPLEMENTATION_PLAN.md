# MVP Vertical Implementation Plan

Status: candidate support doctrine — implementation plan for the loop specified in `MVP_GOVERNED_TASK_LOOP.md`; documented non-implemented.

Date: 2026-07-07

This plan sequences the first real implementation of the governed task loop. It is documentation only: it adds no runtime, no scheduler, no queue, no provider router, no plugin manager, no automatic memory promotion and no automatic approval. Everything executable described here lives on the Hermes side, outside the governance core, under the hosting arbitration below.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## The one blocking decision

**Where executable loop code lives.** `HERMES_CODE_HOSTING_BOUNDARY.md` already frames the arbitration: Option A — a separate Hermes-side repository (its own recommendation) — versus Option B — a bounded in-repo zone via explicit `CLAUDE.md` amendment. Nothing in this plan requires Option B. The plan assumes **Option A**: a sibling repository (working name `pantheon-mvp-vertical`) that consumes this repository's doctrine and the `mcp-server/` policy plane, and pushes nothing back except Evidence Packs and ai_log-able traces. The first line of code waits for this arbitration; every other step below can be prepared meanwhile.

## Block 1 — steps 4–5: bounded execution and candidate return

Goal: from a Task Contract and fictional fixtures, produce a Result Candidate and an Evidence Pack Candidate that satisfy the loop's retrieval boundary.

Components (all Hermes-side):

- **Store** — Postgres + pgvector, one schema per dossier. Ingestion reads only the contract's declared sources, chunks them, embeds them, and stores each chunk with its `source_ref`. The index is rebuildable from sources at any time and holds nothing the sources do not hold.
- **Scoped retrieval** — the SQL filter on `source_ref ∈ declared_scope.sources` applies **before** vector ranking. A query cannot see outside the contract's perimeter by construction, not by prompt.
- **Runner** — a Hermes profile/skill `mvp-governed-task-loop`: load contract → check scope (via the read-only `mcp-server` classification tools) → retrieve scoped passages → draft → emit `result_candidate` + `evidence_pack_candidate` YAML in the shapes of `docs/governance/examples/`. Runtime completion sets no status beyond `draft_to_review`.
- **Fixtures** — the fictional `devis_reprise` pieces as real files: client email, quote Q-2026-041, CCTP excerpt lot 06. Fictional data only; no masking pipeline is needed for the MVP because nothing real enters it.

Acceptance (block 1 is done when):

1. running the contract `mvp.devis-reprise.tc-001` over the fixtures yields an Evidence Pack Candidate whose **every** evidence item carries a `source_ref` inside the declared perimeter, with its retrieval trace;
2. the same runner, asked a question whose answer lies outside the perimeter, returns a **capability gap / refusal report** — not an answer;
3. the returned YAML validates against `schemas/evidence_pack.schema.yaml` wherever the existing schema covers it (`schemas/` itself stays untouched);
4. the run leaves a trace sufficient for an `ai_logs/` entry.

Estimated effort: one focused week.

## Block 2 — steps 1–2 and 6–7: capture, contract, display, decision

Goal: the practitioner drives the loop from OpenWebUI.

- **Capture and contract (steps 1–2)** — an OpenWebUI form captures the request and the selected sources; the Task Contract skeleton comes from the already-implemented `mcp-server` tool `prepare_task_contract_skeleton`; the practitioner completes and confirms it. Producing a contract is not approving its execution.
- **Display and decision (steps 6–7)** — one OpenWebUI Function (candidate until reviewed, per `OPENWEBUI_INTEGRATION.md`) renders the Result Candidate with its Evidence Pack: sources, assumptions, limits, contradictions preserved, commitment flags, open risks — and exactly four actions: approve, refuse, request revision, request more evidence. The Function displays and captures; it decides nothing and sends nothing externally.

Acceptance: a full pass driven from the screen, including at least one `request_revision` round-trip (the gate must be exercised); the decision captured as data matching `mvp_decision_record.yaml`.

Estimated effort: one week.

## Block 3 — steps 8–9: decision record and authorized register candidate

Goal: the loop's writes become governed.

- **Decision Records** — append-only YAML files in the dossier workspace (Hermes-side), one per decision, shaped like `mvp_decision_record.yaml`. Writing the record of a decision that already happened at the gate is trace, not authority.
- **Register Candidate** — created only when a Decision Record carries an explicit retention authorization; shaped like `mvp_memory_candidate.yaml`; scoped to the dossier; admission to the Registre Probatoire remains a separate human review. No write path into this repository: a proposed register entry routes through the governed-edit chokepoint as a candidate, never a direct write.

Acceptance: one demonstration run ends with exactly one Register Candidate, created after — and traceably because of — an authorizing decision; a second run ending in refusal ends with zero.

Estimated effort: three to four days.

## Demonstration and exit

The vertical is **demonstrated** (not promoted) when one full pass satisfies the acceptance criteria of `MVP_GOVERNED_TASK_LOOP.md` end to end. The demonstration produces: the run's Evidence Pack, the Decision Records, at most one Register Candidate, and an `ai_logs/` entry in this repository. What gets promoted afterwards — the OpenWebUI Function, the Hermes skill, any schema alignment of the example shapes — is a list of separate reviewed decisions, not a side effect of the demo.

## Risks and open questions

- **Embedding provider** — local model versus API is a data-exposure decision; the MVP dodges it with fictional fixtures, but the choice must be arbitrated before any real dossier enters the loop.
- **OpenWebUI Function surface** — the Function is an execution surface and stays a candidate until reviewed; its only privileged act is capturing the decision.
- **Doctrine friction is a result, not a failure** — wherever a step cannot be implemented as specified, the finding routes back as a correction candidate against `MVP_GOVERNED_TASK_LOOP.md`. The loop exists to be falsifiable.

## What this plan does not do

It modifies no schema, no test, no CI, no `mcp-server/` code; it installs nothing; it creates no repository. Each block lands through its own reviewed PR (in the sibling repository once arbitrated, with traces here), and the ARBITRAGE list of the governance cleanup stays untouched.
