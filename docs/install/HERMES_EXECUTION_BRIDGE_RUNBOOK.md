# Hermes Execution Bridge — Operator Runbook

Status: candidate manual runbook — no automatic installation, activation or task authorization.

This runbook complements `COMMON_BASELINE_RUNBOOK.md` for the bounded Pantheon execution bridge implemented in `pantheon-mvp`. It describes explicit operator actions only.

## Responsibility boundary

```text
Pantheon-Next owns  -> contracts, boundaries and distribution schema
pantheon-mvp owns   -> candidate run binding, context bridge, observer and CLI
Hermes owns         -> runtime process, tools, sessions and model execution
Human owns          -> installation, secrets, activation and consequential decisions
```

```text
component copied != component enabled
component enabled != binding activated
binding activated != task authorized
runtime return != accepted result
runtime output != Evidence
```

## 1. Select exact artifacts

Record outside the repositories:

```text
PANTHEON_NEXT_COMMIT
PANTHEON_MVP_COMMIT
HERMES_VERSION
HERMES_ARTIFACT_DIGEST
DISTRIBUTION_LOCK_PATH
OPERATOR_ID
INSTALLATION_TARGET
ROLLBACK_TARGET
```

Use an exact Hermes version such as `0.19.0`, not `0.19+`, `latest` or another range. Record the digest of the installed package, image or immutable runtime artifact. A reviewed version without an observed artifact digest remains a candidate only.

## 2. Verify the distribution lock

Use the `pantheon-hermes` CLI from the pinned `pantheon-mvp` checkout:

```bash
pantheon-hermes verify-distribution \
  --manifest hermes/distribution/pantheon-standard.lock.yaml \
  --schema /opt/pantheon-next/templates/hermes/distribution/distribution-lock.schema.yaml \
  --mvp-root /opt/pantheon-mvp \
  --next-root /opt/pantheon-next
```

Expected:

```text
schema valid
all component paths bounded to their repository roots
all file and tree digests match
stable Pantheon routes present
retired internal /v1/hermes routes absent
authority_effect = none
```

Digest validation proves source integrity only. It does not prove installation, health, safety, activation or task authorization.

## 3. Configure the external API seam

Keep secrets outside the repositories:

```text
PANTHEON_HERMES_API_BASE
PANTHEON_HERMES_API_KEY
PANTHEON_HERMES_ACTOR
HERMES_API_BASE
HERMES_API_KEY
```

Required separation:

```text
PANTHEON_HERMES_API_KEY -> bounded Pantheon execution API
HERMES_API_KEY          -> external Hermes Runs API
```

Do not reuse a provider credential as either bridge credential. Do not grant the bridge Docker, SSH, database-administrator or repository-write authority.

## 4. Install the context bridge plugin

Command Candidate — execute only after reviewing the pinned checkout and digest:

```bash
docker exec -it <HERMES_CONTAINER> \
  hermes plugins install \
  "file:///opt/pantheon-mvp#hermes/plugins/pantheon-context-bridge" \
  --no-enable
```

Review the copied plugin and configure:

```text
PANTHEON_HERMES_API_BASE
PANTHEON_HERMES_API_KEY
```

Enable separately only after review:

```bash
docker exec -it <HERMES_CONTAINER> \
  hermes plugins enable pantheon-context-bridge
```

The plugin exposes only:

```text
pantheon_context_manifest
pantheon_context_entity
```

It must not expose global search, global listing, arbitrary source dereferencing or mutation.

## 5. Observe the Hermes Runs API

Supply an operator-reviewed tool allowlist. Do not qualify an unspecified tool surface.

```bash
pantheon-hermes observe \
  --allowed-tool pantheon_context_manifest \
  --allowed-tool pantheon_context_entity \
  --required-tool pantheon_context_manifest \
  --required-tool pantheon_context_entity \
  --output runtime-observation.json
```

Verify:

```text
runs_api_status = compatible
safety_status = qualified
unexpected_tools = []
missing_required_tools = []
run_submission_performed = false
authority_effect = none
```

```text
reachable != healthy
healthy != safe
tool surface qualified != production activated
observation != Evidence
```

## 6. Activate the binding separately

Activation is an explicit human deployment decision outside the distribution lock. Record:

```text
binding identity
operator identity
exact distribution lock digest
activation scope
activation time
expiry or review date
rollback target
```

Do not encode persistent task authorization in the plugin, lock or CLI.

## 7. Launch one admitted task

Create and human-admit the handoff through Pantheon first. Then execute one explicit launch:

```bash
pantheon-hermes launch \
  --admission-id admission-<ID> \
  --idempotency-key <UNIQUE-OPERATOR-KEY> \
  --output launch-receipt.json
```

The CLI performs one sequence only:

```text
observe reviewed Hermes surface
→ reserve one admitted launch
→ submit one Hermes run
→ record the exact runtime start
→ exit
```

It performs no daemon loop, scheduler, queue, automatic retry, provider routing or model override.

A replayed reservation or ambiguous network outcome requires manual reconciliation. Do not rerun the command with a new key merely to bypass uncertainty.

## 8. Verify host correlation and bounded context

For the admitted run, verify on the real Hermes version:

```text
Hermes host task_id == Pantheon admission_id
Hermes session_id == Pantheon admission_id
```

The context bridge must fail closed if the host does not provide an `admission-...` identity or if the observed task/session correlation differs from the reviewed runtime behavior.

Verify one manifest read and one admitted entity read. Confirm that an entity outside the Context Pack is refused.

## 9. Reconcile once

After observing a terminal Hermes status, execute one explicit reconciliation:

```bash
pantheon-hermes reconcile \
  --receipt launch-receipt.json \
  --idempotency-key <UNIQUE-OPERATOR-KEY> \
  --output return-receipt.json
```

The command observes the run once and records a terminal candidate when safely mappable. It does not poll, retry, accept the result, mutate a Project or admit Evidence.

Expected for a completed read-only run:

```text
pantheon_return_recorded = true
result_accepted = false
evidence_admitted = false
project_mutated = false
technical_receipt_is_evidence = false
```

## 10. Record factual observations

Preserve as technical trace:

```text
exact repository commits
component digests
Hermes exact version and artifact digest
plugin inventory
Runs API capability response
toolset response
launch reservation identity
run identity
context access results
return receipt
operator identity and timestamps
```

Do not rewrite the candidate distribution lock to `observed` or `qualified` unless the runtime artifact digest and corresponding observation references are present.

## 11. Revoke and rollback

Revocation order:

```text
revoke or expire active admissions
disable the binding entrypoint
disable pantheon-context-bridge
restore the previous reviewed Hermes configuration when required
verify that bounded Pantheon context reads fail
preserve logs and receipts
```

Routine rollback must not delete Hermes sessions, PostgreSQL data, models or application volumes.

## Acceptance boundary

A real installation is accepted only when all of the following are observed together:

```text
distribution digests match
exact Hermes artifact recorded
Runs API compatible
reviewed tool surface qualified
context bridge installed and bounded
host task/session correlation verified
one human-admitted read-only run completed
candidate returned without automatic acceptance, mutation or Evidence admission
rollback verified
```

This acceptance remains an operational qualification. It does not authorize future tasks.
