# External live run protocol — `architecture_devis_reprise`

Status: validation-only / external-infra protocol.

Issue: #273.

This protocol frames the first fictional OpenWebUI → Hermes run. It does not
implement the bridge, install a runtime, approve a result, send a message or
admit anything to the Registre Probatoire.

## Boundary ownership

```text
exposed_by  -> an external OpenWebUI surface
executed_by -> an externally installed Hermes Agent and the two bounded skills
governed_by -> Pantheon Task Contract, return contract, Evidence Pack and gates
approved_by -> the human operator before execution and the professional before use
forbidden   -> real dossier data, external send, signature, payment approval,
               enterprise instruction, automatic approval or register admission
```

## Repository-side status

Implemented and testable in this repository:

```text
docs/examples/vertical_devis_reprise/task_contract.devis-reprise.yaml
docs/examples/vertical_devis_reprise/workflow_manifest.devis-reprise.yaml
docs/examples/vertical_devis_reprise/policy_decision.gate1.yaml
docs/examples/vertical_devis_reprise/evidence_pack.devis-reprise.yaml
docs/examples/vertical_devis_reprise/answer_status.devis-reprise.yaml
docs/examples/vertical_devis_reprise/register_candidate.devis-reprise.yaml
docs/examples/external_run_returns/architecture_devis_reprise.example.yaml
scripts/validate_devis_reprise_return.py
```

Documented but not implemented by this repository:

```text
OpenWebUI Action implementation
OpenWebUI → Hermes transport or adapter
Hermes installation and configuration
model/provider selection
external credentials and network policy
live execution and rollback
```

A template or successful static fixture does not prove that the bridge exists.

## Gate 0 — qualify the external bridge

Before calling the test a complete OpenWebUI → Hermes run, record:

```text
bridge implementation repository or installed artifact
exact version or commit
OpenWebUI instance and version
Hermes instance and version
transport used
request-candidate identifier
operator
installation and rollback procedure
```

The bridge must remain external. Pantheon may validate its declared return and
govern its status, but must not become the connector, queue, scheduler or MCP
host.

When no executable bridge exists, only a direct Hermes smoke test is permitted.
That test must report:

```yaml
bridge:
  surface: hermes_cli
  status: bypassed_for_preflight
  implementation_ref: direct-cli-smoke-test
```

The validator will classify that result with `BRIDGE_NOT_PROVEN`. It must not be
reported as the complete OpenWebUI → Hermes loop.

## Source dossier

Use only the fictional dossier under:

```text
docs/examples/vertical_devis_reprise/
```

Use the candidate external bindings:

```text
templates/openwebui/actions/request_hermes_execution.template.yaml
templates/hermes/run_manifests/devis_reprise_run_manifest.template.yaml
templates/hermes/skills/quote-variation-review/SKILL.md
templates/hermes/skills/external-commitment-guard/SKILL.md
```

The two skills remain candidates until separately installed and approved on the
external Hermes host.

## Environment record

Record before execution:

```text
run_id
run_date
operator
Pantheon tag or exact commit
Pantheon wheel SHA-256 and resolved dependencies
OpenWebUI version
bridge implementation ref
Hermes version
Hermes MCP configuration ref
model and provider
network boundary
secrets location class, never the secret
read-only repository mount
rollback method
```

Rules:

```text
No production project or client data.
No credential in this repository or the returned fixture.
No Docker socket or unrestricted host control for the policy MCP.
No email, signature, payment approval or enterprise instruction.
No automatic approval or Registre Probatoire admission.
```

## Return file contract

Hermes or the external bridge must persist the exact returned envelope as a YAML
file shaped like:

```text
docs/examples/external_run_returns/architecture_devis_reprise.example.yaml
```

Copy the example, then replace every fictional value. In particular,
`pantheon_ref` must be the exact audited tag or commit used by the external
runtime.

The envelope supports three outcome types:

```text
candidate_return -> Result Candidate + Evidence Pack Candidate
capability_gap   -> structured missing capability or evidence
refusal          -> structured bounded refusal
```

A `candidate_return` must include:

- the governed Task Contract id;
- the Context Pack id;
- the exact Pantheon ref;
- runtime and bridge identity;
- at least one sanitized trace reference;
- a Result Candidate that remains `candidate`;
- an Evidence Pack Candidate valid against `schemas/evidence_pack.schema.yaml`;
- explicit false flags for approval, send, signature, enterprise instruction and
  Registre Probatoire admission;
- a still-open human decision.

The Evidence Pack schema retains the legacy `confidence` compatibility field.
That field is not the governed E-axis and must not be interpreted as approval,
truth or certainty authority.

## Static dossier validation

This validates the versioned governed fixture only:

```bash
python3 .github/scripts/check_vertical_slice.py
```

It does not consume the runtime return and therefore cannot prove that Hermes
returned a conforming result.

## Actual return validation

Save the exact external return, then run:

```bash
python3 scripts/validate_devis_reprise_return.py \
  --return-file /path/to/sanitized-external-return.yaml \
  --task-contract docs/examples/vertical_devis_reprise/task_contract.devis-reprise.yaml \
  --expected-pantheon-ref "$PANTHEON_PIN"
```

The validator reads caller-provided files only. It checks:

- Task Contract and Context Pack presence;
- exact Pantheon pin;
- runtime and bridge declaration;
- trace presence;
- outcome shape;
- Result Candidate status and forbidden-effect flags;
- Evidence Pack schema, project scope and C3 ceiling;
- unresolved approval and review state;
- explicit absence of external effect and register-admission claims.

It does not probe the host or prove that the self-reported effect flags are true.
Operator evidence and rollback evidence remain separate.

## Classifications

Passing classifications:

```text
PASS_STRUCTURAL
PASS_WITH_GOVERNANCE_GAPS
```

`PASS_WITH_GOVERNANCE_GAPS` includes a valid Capability Gap, bounded refusal,
unresolved evidence, or an unproven OpenWebUI bridge. It remains reviewable; it
is not a production or professional acceptance.

Failing classifications:

```text
FAIL_RUNTIME_UNAVAILABLE
FAIL_EXTERNAL_EFFECT_ATTEMPTED
FAIL_APPROVAL_COLLAPSE
FAIL_REGISTER_ADMISSION_ATTEMPTED
FAIL_MISSING_TASK_CONTRACT
FAIL_MISSING_CONTEXT_PACK
FAIL_MISSING_EVIDENCE_PACK
FAIL_SCOPE_MISMATCH
FAIL_INVALID_EVIDENCE_PACK
FAIL_INVALID_RESULT_CANDIDATE
FAIL_INVALID_RETURN
```

## Required evidence for issue #273

Attach sanitized evidence for:

```text
exact runtime and surface versions
Pantheon pin, wheel hash and resolved dependencies
MCP discovery and six-tool allowlist
bridge request candidate and implementation ref
exact external return YAML
validator JSON report
runtime trace references
human decision
rollback and credential-removal confirmation
```

Runtime traces are operational trace until reviewed. A validator pass concerns
structure, scope and declared boundaries only.

## Rollback

After the fictional test:

1. remove or disable the MCP configuration fragment;
2. remove the disposable virtual environment or container;
3. confirm that no schedule, task, credential or writable mount remains;
4. record the rollback result separately from the runtime result.

## Final distinctions

```text
static fixture valid != runtime return valid
template present != bridge implemented
bridge executed != result approved
runtime success != evidence
validator pass != professional truth
trace != proof
candidate != Registre Probatoire entry
human decision remains required
```
