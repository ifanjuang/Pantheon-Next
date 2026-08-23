# Synthetic document runtime check

Status: operator acceptance candidate — implemented helper / not run on a target deployment.

This procedure is for a synthetic non-production fixture only. It is not authorized for a real professional dossier.

## Phase 1 — read-only observation

Run:

```bash
python scripts/document_runtime_synthetic_check.py \
  --observer-url http://document-runtime-observer:8083
```

Expected bounded result:

```text
candidate_ready_for_synthetic_intake = true | false
production_authorization = false
technical_receipt_is_evidence = false
```

Independent prerequisites:

```text
Paperless source path reachable
Pantheon PDP ready observed
Docling health endpoint reachable
pantheon-document-intake listed by Hermes native inventory
```

A failed prerequisite is a technical observation to diagnose at its own source; it is not automatically a safety judgment.

## Phase 2 — optional synthetic Project Document candidate intake

This step creates candidate state in the MVP store and is never implicit.

Prerequisites:

1. a synthetic document exists in the non-production Paperless instance;
2. its exact version id is known;
3. a synthetic Task Contract contains the exact `source_ref` returned by capture;
4. a human decision payload is explicitly provided;
5. `MVP_HERMES_API_KEY` is available to the operator runtime;
6. the installed Hermes skill package is present under the effective Hermes skill directory.

Run:

```bash
python scripts/document_runtime_synthetic_check.py \
  --observer-url http://document-runtime-observer:8083 \
  --run-intake \
  --ack SYNTHETIC_ONLY \
  --document-id 42 \
  --version-id 7 \
  --contract /path/to/synthetic-task-contract.yaml \
  --decision /path/to/synthetic-decision.json
```

The helper first executes the installed skill transport's exact `capture` operation. It refuses to continue unless the Task Contract explicitly contains `synthetic` and the exact returned `source_ref`.

It then invokes the installed skill transport's governed `intake` operation.

## Phase 3 — optional authenticated human-issuer proof

When target acceptance requires cryptographic proof of who issued the synthetic human decision, set operator-only secrets through the deployment secret manager:

```text
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
PANTHEON_POLICY_API_KEY
PANTHEON_POLICY_API_URL
```

The PDP itself must already have its own read-only issuer registry configured through `PANTHEON_DECISION_ISSUER_KEYS_PATH`.

Run the same intake with:

```bash
python scripts/document_runtime_synthetic_check.py \
  --observer-url http://document-runtime-observer:8083 \
  --run-intake \
  --require-issuer-auth \
  --ack SYNTHETIC_ONLY \
  --document-id 42 \
  --version-id 7 \
  --contract /path/to/synthetic-task-contract.yaml \
  --decision /path/to/synthetic-decision.json
```

The decision JSON remains a human-provided decision object. The helper does not choose approval level, scope, object or digest for the human. It signs the supplied bounded decision fields, passes a temporary signed copy through the installed skill, then takes the **PEP-derived `decision_expectation` returned by the gateway** and performs a separate read-only PDP validation.

The proof is successful only when:

```text
PDP validation verdict = valid
issuer_authenticated = true
```

The receipt records that result separately from intake success.

```text
issuer_authenticated != approval
valid decision verdict != effect authorization
runtime success != Evidence
```

## Secret isolation

Operator-only PDP/signing secrets are explicitly removed from the environment passed to the skill subprocess:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
PANTHEON_DECISION_ISSUER_SIGNING_SECRET
```

The installed skill retains only the bounded gateway inputs required by its normal runtime contract.

## Expected boundaries

The helper never performs:

```text
Paperless upload
Paperless metadata mutation
delete
version replacement
Knowledge publication
Evidence admission
activation
installation
update
external send
```

A successful receipt remains a technical trace:

```text
technical_receipt_is_evidence = false
activation_changed = false
production_authorization = false
agent_skill_selection_proven = false
```

Issuer state is explicit:

```text
human_issuer_authentication_status = not_attempted | not_observed | not_proven | proven
human_issuer_authentication_proven = false | true
```

The unresolved normal-agent proof gap remains OPEN even if an operator invokes the installed skill transport successfully: direct operator execution is not proof that an ordinary Hermes conversation selected the skill.
