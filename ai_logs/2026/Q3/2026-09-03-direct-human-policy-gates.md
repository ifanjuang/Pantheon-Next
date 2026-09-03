# Direct human effects are not delegated runtime tasks

Date: 2026-09-03

Status: implemented on candidate branch — CI/review pending.
Boundary profile: bounded_implementation_change.

## Objective

Repair the real-PDP refusal found on 2026-09-02 without inventing Task Contracts
or Evidence Packs for direct human Cockpit/CLI state transitions.

The change is deliberately smaller than the temporal-knowledge work that
prompted the audit. The repository showed a more immediate P0 defect: five
already-wired consequential gates described direct human effects, while the
policy classifier treated every K2-K4 request as delegated runtime work.

## Observed repository state

At base commit:

```text
Pantheon-Next/main
= 5820c7fb97956d314d670f1e70bacc40e97fb18d
```

`ai_logs/2026/Q3/2026-09-02-act-information-policy-facts.md` had already proved
against the real `PantheonPolicyService` that:

- the PDP exists and classifies the five gated human writes as K3/C2 after the
  Information external-effect correction;
- every K3 request nevertheless required `task_contract_ref`,
  `evidence_pack_candidate_ref` and `human_decision_ref`;
- the five newly wired human-originated effects supplied the decision reference
  but structurally had no Task Contract;
- only the older bounded Knowledge UPDATE path supplied all three references.

The active Task Contract doctrine states that a Task Contract defines the
execution boundary for a task delegated to an external runtime. Therefore:

```text
direct human governed-state effect
!= delegated runtime task

writes_state
!= reason to fabricate a Task Contract
```

## Scope

Changed:

- `mcp-server/pantheon_mcp/policy.py`;
- `implementation/mvp_vertical/policy_request.py`;
- `mcp-server/docs/HTTP_API_CONTRACT.md`;
- policy/PEP tests;
- this log.

Not changed:

- canonical schemas;
- APU contracts or persistence;
- Task Contract doctrine;
- Evidence admission;
- decision-validation semantics;
- external-effect permission;
- replay protection;
- temporal ProjectClaim/APU work;
- deployment configuration.

## Implementation

### 1. Policy distinguishes execution boundary from consequence

`classify_request` now accepts:

```text
delegated_execution: bool
```

Omission defaults to `true`.

For K2-K4 requests:

```text
delegated_execution = true
→ Task Contract remains required

delegated_execution = false
→ no Task Contract is fabricated solely because the effect writes state
```

The consequence level is unchanged. A direct human local state write remains
K3 when `writes_state=true`.

### 2. Direct human writes still stop at the human gate

A direct human state write now sets `blocked_until_gate=true` even at K3.
Therefore it still requires `human_decision_ref` and the normal exact decision
validation performed by `enforce_consequential`.

The decision remains bound to:

```text
scope
object identity
content/effect digest
required ceiling
human signer
```

So:

```text
no Task Contract required
!= effect authorized
```

### 3. Evidence requirement is not removed globally

A direct human local state transition does not require an Evidence Pack when
K3 arises solely because it writes governed state.

Evidence remains required for consequential requests carrying any of the
existing evidence-bearing semantics, including:

- delegated consequential work;
- external or unknown external effect;
- transmission;
- memory/Registre behavior;
- professional position;
- financial/contractual effect;
- register material;
- K3/K4 semantic intent triggers such as project surface, cost, contract,
  responsibility or validation claims.

This preserves:

```text
human action != Evidence
state write != assertion
professional assertion != unsupported state write
```

The K/V axes are not redesigned by this patch. `required_verification` remains
the consequence-class posture; `evidence_required` states whether this effect
requires the Evidence Pack gate artifact.

### 4. The operational PEP owns the direct-human classification

The generic policy API accepts the boolean but remains read-only and grants no
authority from it.

`implementation/mvp_vertical/policy_request.py` recognizes only the closed set
of already-audited direct-human intents:

```text
bind_oidc_identity
store_reviewed_dossier
publish_knowledge_reviewed
apply_edit_request
act_working_information
```

Only those are translated to `delegated_execution=false`.

Every other runtime candidate is forced to `delegated_execution=true`, even if
its caller tries to send `false`.

This avoids turning the new field into a caller-controlled Task Contract bypass.
A future direct-human effect must be reviewed and added explicitly.

### 5. External effects are unchanged

Existing PEP-owned Paperless/external-effect facts still win after caller input
normalization. External effects remain K4, Task-Contract/Evidence gated, and
`enforce_consequential` still refuses them unless the PDP explicitly emits an
external permission.

## Tests added/updated

The branch now checks:

- ordinary/external runtime requests remain delegated;
- existing Task Contract gate signals are preserved;
- `act_working_information` is translated as direct-human;
- an unknown runtime candidate cannot self-exempt with
  `delegated_execution=false`;
- direct-human local state write remains K3 and human-decision gated;
- it does not require a fabricated Task Contract or Evidence Pack when no
  assertion-bearing trigger exists;
- a direct-human `record project surface` request still requires Evidence;
- omission defaults to delegated/fail-conservative;
- invalid non-boolean delegation posture is refused;
- the real `PantheonPolicyService.evaluate_preflight` accepts the bounded K3
  direct-human shape when its C2 human decision reference is present;
- the same preflight still fails closed when the decision reference is absent.

## What this does not prove

Until CI runs on the candidate PR, this branch is implemented but not verified
by the repository test suites.

It also does not prove production activation. Repository/CI success remains:

```text
implementation success != authorization
test success != deployment
PDP reachable in tests != PDP configured in production
```

## Follow-up

After this P0 is reviewed and green, resume the previously planned vertical
knowledge improvement:

```text
P1 temporal semantics convergence
P2 structured derivation/provenance
P3 known-as-of / valid-as-of ProjectClaim reads
```

Do not begin that work by introducing a new fact store or temporal engine.
Reuse the existing ProjectClaim and APU carriers.

## Local distinctions

```text
consequential != delegated
human decision != Task Contract
writes state != Evidence
no Evidence Pack needed for this effect != evidence is optional for assertions
classification flag != authorization
PEP-recognized direct intent != caller self-classification
repository implementation != production activation
```
