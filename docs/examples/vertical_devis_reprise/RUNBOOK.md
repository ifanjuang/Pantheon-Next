# Runbook — `architecture_devis_reprise` vertical slice

Status: validation-only runbook.

This runbook identifies the governed artifacts and the external execution seam.
It is not an operations procedure, OpenWebUI Action, Hermes installation or
runtime bridge.

## Ownership

```text
exposed_by  -> external OpenWebUI surface
executed_by -> externally installed Hermes Agent
governed_by -> Pantheon Task Contract, gates, Evidence Pack and return validator
approved_by -> human operator and professional reviewer
forbidden   -> external effect, automatic approval or register admission
```

## End-to-end sequence

```text
1. OpenWebUI exposes a bounded request candidate.                     [external]
2. Pantheon artifacts frame Task Contract, scope and gates.          [this repo]
3. The external bridge passes the request to Hermes.                 [external]
4. Hermes executes only the two candidate skills.                    [external]
5. Hermes/bridge persists the exact external return YAML.            [external]
6. Pantheon validates that caller-provided return read-only.         [this repo]
7. OpenWebUI exposes the candidate, gaps and expected decision.       [external]
8. The human accepts, refuses or requests revision.                  [human]
```

The bridge in step 3 is not implemented in this repository. Without a separately
installed bridge, only a direct Hermes smoke test is possible and the return must
remain classified with `BRIDGE_NOT_PROVEN`.

## Governed inputs

```text
task_contract.devis-reprise.yaml
workflow_manifest.devis-reprise.yaml
policy_decision.gate1.yaml
```

Hermes may load only:

```text
templates/hermes/skills/quote-variation-review/SKILL.md
templates/hermes/skills/external-commitment-guard/SKILL.md
```

## Required return

Use the contract fixture:

```text
external_run_return.example.yaml
```

The actual return must identify the exact Pantheon tag or commit and contain one
of:

```text
candidate_return
capability_gap
refusal
```

A candidate return includes a Result Candidate and a complete Evidence Pack
Candidate. It must leave approval and the User Decision Gate unresolved.

## Two separate checks

The repository fixture check validates the versioned static dossier:

```bash
python3 .github/scripts/check_vertical_slice.py
```

It does not validate a runtime return.

The external-return check consumes the exact YAML returned by the bridge or
Hermes:

```bash
python3 scripts/validate_devis_reprise_return.py \
  --return-file /path/to/sanitized-external-return.yaml \
  --expected-pantheon-ref "$PANTHEON_PIN"
```

Both checks are read-only. Neither proves professional truth, no external effect,
approval, activation or Registre Probatoire admission.

## External bridge candidates

```text
OpenWebUI request template -> templates/openwebui/actions/request_hermes_execution.template.yaml
Hermes run manifest        -> templates/hermes/run_manifests/devis_reprise_run_manifest.template.yaml
```

These files are declarative candidates. Presence in git does not mean installed,
reachable, healthy, approved or used.

## Data boundary

The first run uses fictional data only. The `base_metier/architecte/` corpus and
all real client documents remain excluded until licence, storage, access and
professional-use gates are separately qualified.

## Stop condition

The run always stops at the human decision surface. Nothing is sent, signed,
approved, paid, instructed or admitted to the Registre Probatoire.

```text
static fixture valid != runtime return valid
template present != bridge implemented
runtime success != evidence
validator pass != professional approval
```
