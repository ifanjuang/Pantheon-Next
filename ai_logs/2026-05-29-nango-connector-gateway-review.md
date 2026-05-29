# Nango connector gateway review

Date: 2026-05-29

Status: documentation-only support intervention.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## What changed

This intervention added documentation-level support for evaluating Nango as an external connector gateway candidate.

Created:

- `docs/governance/reference_reviews/NANGO.md`;
- `docs/governance/NANGO_HERMES_CONNECTOR_GATEWAY.md`.

Updated:

- `docs/governance/reference_reviews/README.md` to index the Nango reference review.

## Why

Nango is useful as an external API integration and credential gateway because it can centralize OAuth, provider credentials, connector actions, retries, rate limits, logs and tool-callable action functions outside Pantheon.

The governance value is not to make Pantheon execute Nango.

The governance value is to preserve the boundary:

```text
Nango = external connector gateway
Hermes = external runtime caller under Task Contract
OpenWebUI = consent, scope, approval and result exposure
Pantheon = policy, approval, evidence and memory boundary
```

## Boundary preserved

This intervention does not:

- install Nango;
- configure Nango;
- configure OAuth providers;
- create Nango connections;
- add credentials;
- create a Hermes skill;
- create an OpenWebUI Function, Tool, Pipe, Filter, Action or Pipeline;
- create a Pantheon runtime;
- create a connector marketplace;
- create a provider router;
- create an internal MCP layer;
- create schedules, queues or webhooks;
- create automatic approval;
- create automatic memory promotion.

## Main doctrine captured

Nango may be considered only as an external connector gateway candidate.

Hermes may call it only under a governed Task Contract.

OpenWebUI may expose provider, scope, consent, approval, result candidate and Evidence Pack Candidate.

Pantheon may govern authorization, approval level, evidence expectation, scope isolation, memory rules and User Decision Gate triggers.

## Risks and limitations

- Nango combines credential handling and executable functions, so it is a trust-boundary surface.
- Nango schedules, webhooks and MCP/tool schemas can drift toward hidden runtime behavior if not explicitly blocked.
- API results retrieved through Nango are Raw Source or Retrieved Knowledge at most, not Canonical Memory.
- Connector logs may support an Evidence Pack Candidate, but they are not Evidence Packs by themselves.
- The review is based on observed public documentation and repository information on 2026-05-29; operational details must be rechecked before any real configuration.
- No runtime test, installation test, OAuth test or provider integration test was performed.

## Approval posture

This is a support doctrine change.

It records a candidate pattern and its boundaries.

It is not an implementation approval, dependency approval, installation approval, credential approval or provider approval.

## Follow-up candidates

Possible future work, each requiring separate governance review:

- add a Nango entry to broader external tool watchlists;
- define a fictional Evidence Pack example for a Nango-mediated read-only API retrieval;
- define a fictional User Decision Gate example for a Nango-mediated external write;
- evaluate Nango self-hosting and license posture before any operational proposal;
- compare Nango against direct provider connectors, OpenWebUI tools and Hermes-native connector patterns.
