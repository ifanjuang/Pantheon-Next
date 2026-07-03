# Runbook — `architecture_devis_reprise` vertical slice

Status: validation-only runbook. It specifies where the external runtime plugs into
the governed dossier so the loop can be closed the day the runtime exists. Pantheon
governs; it does not execute. This runbook lives under `docs/` (not `operations/`,
which stays protected) until an operations owner adopts it.

## The end-to-end loop and who owns each step

```text
1. OpenWebUI (surface)      exposes the request; shows gates and the decision.        [external]
2. Pantheon (PDP)           frames it: Task Contract + a forged Workflow Manifest
                            with signed capability_steps.                             [this repo]
3. Gate 1 (ZEUS)            pre_execution_eligibility → policy_decision as data
                            (allow / allow_with_gate / block / needs_*).              [this repo, data]
4. Hermes (PEP)             executes the bounded steps under the required envelope
                            (task_contract_in → candidate_out → evidence_pack_out).   [external]
5. mcp-server               read-only verification of the returned candidate +
                            evidence against the schemas and the passport.            [this repo, read-only]
6. Gate 2 (evidence)        post_execution_evidence → answer status (V/E/K).          [this repo, data]
7. User Decision Gate       the human decides; nothing is sent/approved before it.    [surface + human]
```

## Wiring contract (so the external runtime need not re-invent the framing)

```text
Hermes receives : task_contract.devis-reprise.yaml  +  the capability_steps of
                  workflow_manifest.devis-reprise.yaml (declared/forbidden scope,
                  required_task_contract, approval_ceiling, refusal_tests).
Hermes returns  : a Result Candidate + an Evidence Pack Candidate shaped like
                  evidence_pack.devis-reprise.yaml.
mcp-server      : validates that return read-only; it routes nothing and decides nothing.
Pantheon        : records answer_status + register_candidate as candidates; the gate decides.
```

## How to check the governed side today (no runtime)

```bash
python3 .github/scripts/check_vertical_slice.py
# or, via the doctor (single source of truth):
python3 -c "import sys; sys.path.insert(0,'mcp-server'); from pantheon_mcp.doctor import check_vertical_slice; print(check_vertical_slice())"
```

## Not in scope here

The actual OpenWebUI/Hermes execution, any live data, and any base_metier corpus
(kept out until its licence is qualified) are **out of scope** for this slice. The
slice proves the governance loop; phase 2 (a real run) lives outside the repo.

## Phase-2 bridge (candidate templates — non-executable)

Each external step now has a candidate template, so the runtime binds to the
governed dossier without re-inventing the framing. These are `candidate_template_only`;
they install and execute nothing.

```text
OpenWebUI exposes  → templates/openwebui/actions/request_hermes_execution.template.yaml
Hermes run         → templates/hermes/run_manifests/devis_reprise_run_manifest.template.yaml
  step 1           → templates/hermes/skills/quote-variation-review/SKILL.md
  step 2 (guard)   → templates/hermes/skills/external-commitment-guard/SKILL.md
mcp-server verifies→ check_vertical_slice (read-only)
```

The live run (a real OpenWebUI instance calling a real Hermes) is phase 2 proper and
lives outside this repo. These templates make it ready to wire; they do not run it.
