# 2026-07-23 — Hermes Agent v0.19.0 release boundary review

Status: validation-only intervention trace.
Boundary profile: external_reference_review.

## Change

Recorded the Hermes Agent **v0.19.0 (v2026.7.20, "Quicksilver")** release against
the existing per-version review mechanism, without absorbing runtime reach and
without mutating any adapter pin.

```text
docs/governance/HERMES_INTEGRATION.md      -> new "Hermes 0.19 runtime surface review" section
                                              + MoA bridge note (0.19 preset keys → template to re-verify)
docs/governance/HERMES_RUNTIME_GOVERNANCE.md -> latest observed release bumped to v0.19.0
```

## Why

Repository adapters, templates and runbook pin Hermes `0.17 / 0.18.0 / 0.18.2`.
The real latest release is `0.19.0`, a large release over 0.18.x. Doctrine
requires that every major Hermes version change be reviewed against the same
governance table before use (`HERMES_INTEGRATION.md` version-change review rule).

## Surfaces mapped (external runtime, not Pantheon doctrine)

```text
smart approvals default (in-runtime LLM reviewer)   -> critical: must not stand in for the human gate
user-defined deny rules / /deny                      -> runtime guardrail, not approval
MCP tool naming mcp__server__tool                    -> re-verify pantheon-policy fragment tool list
stricter config.yaml validation                      -> re-verify disabled MoA + api_server restriction
MoA preset refinements (reference_max_tokens, ...)   -> deliberation template to re-verify
pluggable secrets (SecretSource, op://)              -> custody stays in deployment layer / secret manager
provider control (enabled:false, excluded_providers) -> provider routing stays outside Pantheon
profile-based gateway multiplex routing              -> no Pantheon Role authority created
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The one surface with a doctrinal edge is **smart approvals on by default**: an
in-runtime model review is not a Pantheon approval. The live Hermes Policy
Enforcement Point must disable it for consequential (K2+) effects and stay
fail-closed. This is a required item for the external PEP adapter, not a Pantheon
change.

## Deliberate limits

Template and runbook version pins are **not** changed: the exact runtime version
must be observed on a real 0.19 install before any adapter mutation (the config
documentation was not independently readable at review time). Nothing here
installs, activates, updates, routes a provider, schedules, promotes memory or
approves an effect.

## Boundary

```text
release reviewed != release adopted
surface mapped != adapter re-pinned
smart-approval default != Pantheon approval
observed latest != installed version
```

No runtime, schema, test, protected path, `mcp-server/` code, CI script or
external action is introduced.
