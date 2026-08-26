# Agent Passport distillation

Date: 2026-08-26

## Objective

Distill the useful runtime-enforcement patterns observed in `prabindersinghh/agent-passport` without importing a second governance authority, runtime dependency or parallel Pantheon policy path.

## Repository state checked

Pantheon Next `main` was verified at:

```text
161f6f63c26a3b8d11d9be558a5c4604d09fb023
```

Open Pantheon pull requests were searched for overlapping PEP, enforcement, Agent Passport, replay, execution-admission and policy work. No overlapping active PR was found.

Relevant existing owners checked:

```text
docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md
docs/governance/HERMES_INTEGRATION.md
docs/governance/HERMES_EXECUTION_ADMISSION_BRIDGE.md
docs/governance/HERMES_EXECUTION_TRACE_SUMMARY.md
docs/governance/DISTILLATION_REGISTRY.md
docs/governance/REJECTED_PATTERNS.md
mcp-server/docs/HTTP_API_CONTRACT.md
docs/governance/WHAT_RUNS.md
```

## External reference observed

Reference:

```text
repository: prabindersinghh/agent-passport
release: v0.2.0
reviewed main commit: 640b4c523cd2f6d8687c9f695d11baea51cb7d83
```

Observed implementation surfaces included:

```text
MCP tools/call interception before upstream forward
HTTP authorization gateway
policy evaluation with deny / approval / allow precedence
fail-closed behavior
one-use approval consumption
explicit agent/runtime identity
machine-derived run summaries from audit/tool events
```

These observations are implementation/reference facts. They are not evidence that the project should be adopted by Pantheon.

## Distilled pattern

Pantheon retains the implementation-independent pattern:

```text
runtime request
-> PEP intercepts before the native tool/effect
-> Pantheon remains the sole PDP for consequential effects
-> PEP fails closed when the required Pantheon decision cannot be validated
-> request is bound to an explicit runtime principal and exact effect identity
-> one-use authorization is consumed by the operational PEP
-> actual execution outcome produces runtime trace material
```

This converges with existing Pantheon doctrine rather than creating a new architecture.

## Explicit rejection

Rejected import:

```text
Agent Passport PolicyEngine as a second Pantheon policy authority
parallel project/passport policy store as an independent allow path
runtime approval database as Pantheon approval authority
runtime audit/log as Evidence or Registre Probatoire authority
```

A runtime PEP may apply local deny-only hardening because it can narrow authority. It must not independently widen the authority granted by Pantheon.

## Changes

Updated existing owners only:

```text
docs/governance/DISTILLATION_REGISTRY.md
  -> added External PEP enforcement gateway distilled pattern

docs/governance/REJECTED_PATTERNS.md
  -> added Parallel runtime policy authority rejection
```

No new governance document was created.
No schema was changed.
No runtime code was changed.
No dependency was added.
No capability was activated.
No external tool was installed.

## Interpretation

Agent Passport is currently useful as an external implementation reference for the PEP side of the Pantheon/Hermes boundary. Its product-level policy authority is not adopted.

The existing architecture already owns the relevant distinctions:

```text
Execution Admission != effect authorization
Pantheon PDP != Hermes/runtime PEP
valid decision != consumed decision
runtime success != Evidence
trace != proof
installed/available != authorized
```

## Remaining open question

A future bounded technical qualification may test whether the Agent Passport MCP proxy can be configured or adapted to delegate consequential policy decisions exclusively to the Pantheon policy service without retaining an independent allow-authority path.

That qualification is not performed or authorized by this distillation change.

## Closure

Distillation complete for doctrine/reference purposes.

External component adoption remains open and separately reviewable.
