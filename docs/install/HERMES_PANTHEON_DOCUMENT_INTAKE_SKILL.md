# Hermes `pantheon-document-intake` — Installation Runbook

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook documents operator installation of the external Hermes skill candidate implemented in `ifanjuang/pantheon-mvp#59`.

It executes nothing, stores no secret, activates no real dossier and does not authorize a Paperless external mutation.

## 1. Preconditions

Record before installation:

```text
Hermes runtime version
Hermes runtime identity/service account
reviewed pantheon-mvp commit containing the skill
skill source URL or reviewed copied directory
Paperless gateway private endpoint
Hermes gateway secret owner/reference
Pantheon PDP endpoint/version
issuer key registry owner/reference when authenticated human decisions are required
rollback method
```

Required preceding components:

```text
Hermes Agent installed
Paperless-ngx installed on the private network
paperless-gateway deployed
Pantheon policy API deployed/reachable
Docling binding available when binary document intake is in scope
```

These dependencies being present does not authorize the skill for real project data.

## 2. Source package

The complete candidate skill directory is:

```text
hermes/skills/pantheon-document-intake/
├── SKILL.md
└── scripts/
    └── pantheon_document_intake.py
```

Do not recreate only the prose of `SKILL.md`; the bundled transport script is part of the reviewed candidate.

Hermes supports installation from an HTTP(S) `SKILL.md` URL and installs referenced supporting files. Use a commit-pinned source, not an unreviewed moving branch.

Illustrative operator variables:

```bash
export PANTHEON_MVP_SKILL_COMMIT='<reviewed-pantheon-mvp-commit>'
export PANTHEON_DOCUMENT_INTAKE_SKILL_URL="https://raw.githubusercontent.com/ifanjuang/pantheon-mvp/${PANTHEON_MVP_SKILL_COMMIT}/hermes/skills/pantheon-document-intake/SKILL.md"
```

The commit is a deployment input selected by the operator after review. Pantheon does not select or fetch it automatically.

## 3. Install with native Hermes tooling

Candidate command:

```bash
hermes skills install "$PANTHEON_DOCUMENT_INTAKE_SKILL_URL"
```

If immediate prompt-cache invalidation is intentionally required after review, the operator may use the native Hermes option appropriate to the observed version. Otherwise start a new Hermes session after installation.

Do not use Pantheon code to copy files into the Hermes skill directory.

```text
Hermes installs skill
Pantheon records/governs status
```

## 4. Verify complete installation

Check native inventory:

```bash
hermes skills list
```

Expected entry:

```text
pantheon-document-intake
```

Then verify the installed skill directory contains both the instruction document and script. Default per-user Hermes layout is under the Hermes data directory, commonly:

```text
~/.hermes/skills/pantheon-document-intake/
```

A custom Hermes profile or `HERMES_HOME` may relocate it. Resolve the effective runtime path instead of hard-coding it in Pantheon.

Minimum package check:

```text
SKILL.md present
scripts/pantheon_document_intake.py present
skill name/description readable by Hermes
```

```text
skill listed != skill healthy
skill healthy != capability safe
skill installed != Pantheon activation
```

## 5. Configure the Hermes-side gateway binding

The skill needs only:

```text
PANTHEON_PAPERLESS_GATEWAY_URL=http://paperless-gateway:8082
MVP_HERMES_API_KEY=<external-secret-reference/value injected into Hermes runtime>
```

Optional bounded timeout:

```text
PANTHEON_PAPERLESS_GATEWAY_TIMEOUT=30
```

The skill must not receive:

```text
PAPERLESS_API_TOKEN
PANTHEON_POLICY_API_KEY
PANTHEON_DECISION_ISSUER_KEYS_PATH
issuer signing secret
Paperless DB password
Pantheon DB administrative credential
```

The policy and issuer-verification secrets remain server-side/operator-side. Verify the runtime secret store owns the Hermes gateway key. Never write it into `SKILL.md`, a Task Contract, project file, Knowledge item or Pantheon log.

## 6. Read-only synthetic acceptance

Use a synthetic/non-client Paperless document first.

From a Hermes session, load:

```text
/pantheon-document-intake
```

Then ask it to search/inspect the synthetic source. The underlying bounded operations are:

```text
search
inspect
capture
```

Acceptance:

```text
Hermes can call paperless-gateway
paperless-gateway accepts the Hermes key
Paperless token is not returned to Hermes
search result is marked operational/non-authoritative
exact capture returns version + hash + source_ref
```

A successful read is a reachability observation only.

## 7. Project Document candidate intake acceptance

Create a synthetic Task Contract whose declared source exactly matches the captured Paperless `source_ref`.

The human decision test object must match the effect identity/digest derived by the PEP for that exact Task Contract and source version.

When authenticated issuer proof is part of the target acceptance, additionally configure the Pantheon PDP issuer registry through the operator deployment layer and provide a decision carrying the matching signature produced by the reviewed signing producer. The Hermes document skill itself does not hold the issuer key.

Expected target path:

```text
human decision producer
-> signed bounded decision fields
-> Paperless gateway / PEP
-> Pantheon PDP
-> issuer registry lookup + signature verification
-> issuer_authenticated observation
-> ordinary decision/effect checks
```

Run the governed `intake` operation.

Expected sequence:

```text
Hermes skill
-> paperless-gateway
-> exact Paperless capture
-> Task Contract scope guard
-> Pantheon preflight
-> decision validation against PEP-owned expectation
-> issuer verification when configured
-> store.ingest
-> Docling/direct extraction
-> Project Document candidate
```

Expected result includes:

```text
status: applied
effect_ran: true
operation: project_document_intake
knowledge_published: false
evidence_admitted: false
```

Verify separately that a wrong source reference, wrong object identity, wrong digest, wrong scope, unknown issuer or invalid signature prevents the persistence executor from running when issuer authentication is configured.

```text
issuer_authenticated != approval
valid decision verdict != effect authorization
```

## 8. Current PDP V0 external-effect acceptance

The current Pantheon policy V0 keeps:

```text
external_effect_allowed = false
canonical_effect_allowed = false
```

Therefore a native Paperless metadata PATCH/upload must remain blocked on the live V0 path even if the supplied decision fields and issuer signature validate.

Acceptance test:

```text
request a synthetic metadata mirror change
-> preflight remains candidate-eligible but external effect not authorized
-> PEP returns blocked_external_effect_not_authorized
-> Paperless PATCH is not called
```

This blocked result is correct behavior for the current policy version.

Do not change the Hermes skill or gateway to bypass this result.

The external implementation also revalidates the exact source immediately before a future metadata PATCH: if the live Paperless bytes differ from the approved capture, the PATCH is refused and a new capture/decision is required.

## 9. Failure tests

Before any activation, verify:

```text
PDP unavailable -> governed effect blocked
Paperless unavailable -> source access unavailable, no fallback DMS
Hermes key invalid -> gateway 401
source outside Task Contract -> 422/refusal before policy/executor
malformed Task Contract YAML -> 422/refusal, not internal error
human object/digest mismatch -> effect blocked
invalid/unknown issuer signature -> decision invalid when issuer registry configured
changed metadata payload -> previous decision no longer matches
changed live Paperless source after decision -> metadata PATCH refused
caller external_effect=false cannot downgrade a known Paperless external executor
Docling unavailable -> Project Document intake fails without silent alternate derivation
```

Do not add background retries, cron or queue behavior as a workaround.

## 10. Rollback

Native Hermes rollback:

```bash
hermes skills uninstall pantheon-document-intake
```

Also remove/disable the runtime secret binding and gateway configuration through operator tooling as appropriate.

Rollback does not delete:

```text
Paperless originals
historical Source Capture references
already-created Project Document candidate records
existing Knowledge records
```

Any cleanup of governed records is a separate consequential operation.

## 11. Activation state

After successful installation and synthetic checks, record at most:

```text
skill installation: installed
skill package integrity: observed
Hermes -> gateway reachability: observed
Paperless read path: observed
Project Document synthetic intake: observed
current external mutation path: correctly blocked by PDP V0
```

When the signed-decision test is also completed, record its proof separately:

```text
target issuer registry: configured/observed
signed decision delivery: observed
issuer_authenticated round-trip: observed
```

Still separate:

```text
capability approved: no implication
real dossier scope: no implication
production activation: no implication
issuer_authenticated: no implication of approval
```

## Final boundary

```text
Hermes installs and executes the skill.
The gateway enforces runtime boundaries.
Pantheon governs policy/status and configured issuer verification.
Paperless stores and processes sources.
Docling derives structure.
The human decides consequential activation.
```
