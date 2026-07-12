# AI intervention trace — handoff decision hardening

Date: 2026-07-12
Status: validation-only trace

## Change

Hardened the non-executable `HandoffDecision` contract and validator.

The schema now:

- binds `metadata.status` to `spec.decision`;
- requires `authorized_scope` only for approvals;
- uses `reviewed_scope` for refusal, revocation and expiration;
- requires expiry only for approvals;
- requires supersession for revocation and expiration;
- forbids an approval from superseding another decision.

The fixture now includes the referenced `InstallationCandidate` and the validator checks exact resource, preset and provisioner scope against the installation and handoff candidates.

Temporal comparisons use parsed timezone-aware datetimes rather than lexical string comparison.

## Boundary

No decision resolver, approval engine, identity provider, runtime callback, provisioner API, installation, activation or external action is implemented.

## Local distinctions

```text
schema_valid != decision_current
approval_recorded != execution_authorized
reviewed_scope != authorized_scope
scope_match != activation
validator_pass != human_approval
```
