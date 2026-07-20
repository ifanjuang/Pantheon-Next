# Governance Status

Status: external executable candidate — implemented and tested / not adopted.

This repository is not Pantheon Next.

It is an external executable candidate intended to host the MVP vertical slice for governed task-loop testing.

## Boundary

```text
executed_by: this external repository, when code is present and explicitly run
exposed_by: terminal decision stand-in plus committed read-only OpenWebUI Document Card candidate; not installed
governed_by: Pantheon Next doctrine and adoption gates
approved_by: human decision only
forbidden: self-approval, external send, memory promotion, provider routing, scheduling, unrestricted source access
```

## Current status

```text
implementation_status: blocks_1_2_3_plus_work_issues_and_document_vertical_complete_as_candidates
# Block 1 (bounded ingestion, scoped retrieval, candidates + refusals),
# Block 2 (drafting seam + advisory flags), Block 3 (register candidate + B1
# retention authorization), controlled Work Issue persistence, Docling-backed
# extraction, strict incremental NAS intake and a read-only OpenWebUI Document
# Card cockpit candidate. The external-review hardening lot also covers gate
# input validation, closed decision vocabulary, register-seam anti-forgery,
# decision/retrieval identities and digests, systematic runner-output schema
# validation, CI fail-not-skip and packaged vendored files. Schema is vendored
# at UPSTREAM_COMMIT 7afdc2148f77333f6a472200f334d32f7f358a68; the report-only
# drift checker distinguishes a newer upstream commit from structural drift.
binding_status: candidate
installation_status: not installed by Pantheon Next
activation_status: not activated
health_status: acceptance_tests_pass    # test_pass != adoption
ci_status: green_on_main
production_status: forbidden
knowledge_publication_status: absent     # no generated_unreviewed publication or Knowledge Card yet
```

## Stand-in rule

Any file occupying another actor's role must declare its status.

```text
runner.py -> explicit Hermes stand-in header (met: module docstring declares stand_in_runner != Hermes Agent)
gate.py   -> terminal_gate_standin.py (met: named + header declares terminal_gate != OpenWebUI cockpit)
```

Both stand-ins now declare their status explicitly. The separate OpenWebUI
Document Card Tool is a committed read-only candidate, not a live installation.
These surfaces prove the governance cage; they are not adoption or activation.

## Required non-equivalence rules

```text
runtime_success != evidence
test_pass != adoption
candidate != approval
retrieved != truth
source_declared != path_safe
stand_in_runner != Hermes Agent
terminal_gate != OpenWebUI cockpit
external_repo != Pantheon runtime
```

## Adoption gates

Before adoption, this repository needs visible review evidence for the gates
below. That evidence now exists for gates 1–7 — as *candidate* evidence, not
approval (`test_pass != adoption`). Only the human approves activation.

```text
Task Contract schema alignment          -> met: contract validated against the vendored schema at load (PR #6)
source path boundary (abs/traversal/symlink) -> met: assert_source_path_safe + symlink-safe resolve_source_within (PR #4)
fixture-specific drafting status        -> generalised: the Drafter seam makes drafting dossier-general (PR #9);
                                           a draft verifier rejects fabricated sourcing (PR #10). Provider routing
                                           stays forbidden here — the LLM slot is a Hermes-side Drafter.
human gate decision semantics           -> met: terminal_gate_standin.record_decision emits a decision_record (PR #7)
system-signer refusal                   -> met: decided_by refuses system identities; only a human may sign (PR #7)
external-send refusal                   -> met: structural (no transport) + advisory detector (PR #5)
CI result after code push               -> met: acceptance tests green on main (adversarial dossier included, PR #8)
human approval for activation           -> OPEN: the human decides
```

The review that opened these gates is recorded in `ADOPTION_REVIEW.md`. A
subsequent external review drove a hardening lot (gate input validation, closed
decision vocabulary, register-seam anti-forgery, decision/retrieval audit
identity, systematic output validation, CI fail-not-skip, packaging) — all
*candidate* evidence reinforcing gates 1–7, none of it adoption. Gates being met
does not adopt, install, or activate this repository. Gate 8 stays OPEN.

## Final rule

```text
This repository may execute an external proof loop.
Pantheon Next governs the status of that loop.
The human decides.
```
