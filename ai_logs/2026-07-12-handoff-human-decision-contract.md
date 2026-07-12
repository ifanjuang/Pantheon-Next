# AI intervention trace — handoff human decision contract

Date: 2026-07-12
Status: validation-only trace

## Change

Added a bounded `HandoffDecision` contract for explicit human review of a `ProvisionerHandoffCandidate`.

The contract supports:

- approval;
- refusal;
- revocation;
- expiration;
- identified human decision-maker;
- C2-C5 decision level;
- exact one-time scope;
- effective and expiry timestamps;
- evidence references;
- supersession.

A synthetic Docling example contains an approval followed by revocation before execution.

## Enforced boundary

```text
approval != execution
approval != runtime callback
automatic approval is forbidden
handoff approval != activation authorization
approved scope must match the selected provisioner
approval is one-time and expires
revocation supersedes the earlier decision
```

No approval engine, user identity system, signature service, provisioner call, Docker/Portainer access, shell execution or runtime activation is implemented.
