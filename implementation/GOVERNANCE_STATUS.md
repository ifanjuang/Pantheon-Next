# Governance Status

Status: external executable candidate — initialized / not adopted.

This repository is not Pantheon Next.

It is an external executable candidate intended to host the MVP vertical slice for governed task-loop testing.

## Boundary

```text
executed_by: this external repository, when code is present and explicitly run
exposed_by: terminal stand-ins now; future OpenWebUI or cockpit surface only after review
governed_by: Pantheon Next doctrine and adoption gates
approved_by: human decision only
forbidden: self-approval, external send, memory promotion, provider routing, scheduling, unrestricted source access
```

## Current status

```text
implementation_status: block1_candidate_code_present
binding_status: candidate
installation_status: not installed by Pantheon Next
activation_status: not activated
health_status: to_verify
ci_status: to_verify
production_status: forbidden
```

## Stand-in rule

Any file occupying another actor's role must declare its status.

```text
runner.py -> hermes_standin_runner.py or explicit Hermes stand-in header
gate.py -> terminal_gate_standin.py or explicit OpenWebUI/terminal stand-in header
```

The stand-ins prove the governance cage. They are not the final actors.

## Required non-equivalence rules

```text
runtime_success != evidence
test_pass != adoption
candidate != approval
retrieved != truth
source_declared != path_safe
stand_in_runner != Hermes Agent
terminal_gate != OpenWebUI cockpit
external_repo != Pantheon runtime
```

## Adoption gates

Before adoption, this repository needs visible review evidence for:

```text
Task Contract schema alignment
source path boundary checks against absolute paths, traversal and symlink escape
fixture-specific drafting status
human gate decision semantics
system-signer refusal
external-send refusal
CI result after code push
human approval for activation
```

## Final rule

```text
This repository may execute an external proof loop.
Pantheon Next governs the status of that loop.
The human decides.
```
