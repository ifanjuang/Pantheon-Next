# Langfuse Dashboard Link Card Candidate

Status: candidate / to verify — Dashboard exposure pattern, documented non-implemented.

This document defines the first Dashboard integration pattern for Langfuse.

It does not add Dashboard runtime code, create a route, install Langfuse, start containers, read client traces, embed Langfuse, create secrets, approve results, promote memory, create Evidence Packs or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The Dashboard may expose Langfuse as an observability card.

The card answers only:

```text
Is Langfuse configured?
Is Langfuse reachable?
Where can the operator open Langfuse?
Which synthetic trace references were produced during first test?
What runtime status is reported?
What governance status remains assigned by Pantheon?
```

It must not answer:

```text
Is the result true?
Is the result approved?
Can this be remembered?
Can this be sent?
Is this an Evidence Pack?
```

## First implementation posture

```text
Dashboard_posture: link_only
embedded_view: refused_for_first_test
trace_visibility: synthetic_refs_only
client_dossier_traces: refused_until_redaction_review
health_check: allowed
secrets_in_frontend: refused
Langfuse_api_keys_in_browser: refused
```

## Card content

Recommended card:

```text
Title: Observabilité — Langfuse
Subtitle: Trace runtime only. Not proof, approval or memory.
Status: unknown | reachable | degraded | unavailable
URL: internal Langfuse URL
Primary action: Ouvrir Langfuse
Secondary action: Vérifier santé
Last synthetic trace refs: optional
Runtime task status: not_started | success | partial | failed | blocked | unknown
Governance result status: candidate | to_verify | approved | rejected | blocked
Warning: Une trace réussie ne valide pas le résultat.
```

## Read model

The Dashboard may read a local configuration object equivalent to:

```yaml
observability:
  langfuse:
    enabled: true
    ui_url: "http://localhost:3000"
    health_url: "http://localhost:3000/api/public/health"
    mode: "external_link"
    embedded_view: false
    trace_visibility: "synthetic_refs_only"
```

The Dashboard may call `health_url` from a backend-safe context. If the request is made from a browser context, CORS, network exposure and authentication must be reviewed first.

The Dashboard must not store or expose Langfuse secret keys.

## Health interpretation

Health status is operational only.

```text
reachable != valid
reachable != approved
reachable != evidence
reachable != memory
reachable != production-ready
```

A reachable Langfuse instance proves only that the observability service answered a health request.

## Trace reference interpretation

A trace reference may support review. It is not proof by itself.

```text
trace_ref -> observation support
result_candidate -> output requiring qualification
evidence_pack_candidate -> candidate support bundle
governance_result_status -> Pantheon-governed status
```

For the first test, only synthetic trace refs may be shown.

## Refused for first test

```text
iframe embed
client trace listing
client dossier trace emission
Langfuse API key in frontend
automatic trace ingestion into Evidence Pack
automatic Result Candidate approval
automatic memory promotion
external action based on trace success
```

## Template binding

Template reference:

```text
templates/langfuse-hermes/dashboard-module.langfuse.example.yaml
templates/langfuse-hermes/dashboard-card.langfuse.example.html
```

## Promotion criteria

This candidate may become an implementation task only when:

```text
- Dashboard runtime location is identified;
- config location is identified;
- health check execution context is identified;
- Langfuse UI URL is known;
- authentication exposure is reviewed;
- first synthetic trace path is named;
- client traces remain blocked;
- issue #146 records the decision.
```

## Boundary phrase

```text
The Dashboard may expose the observability doorway.
It must not turn observation into proof, approval, memory or authorization.
```
