# Pre-Execution Simulation — owner retention decision — 2026-08-29

## Objective

Close the #787 owner test for `PRE_EXECUTION_SIMULATION.md` after #807 narrowed it to simulation-specific doctrine.

Exact base: `47325d4433c465e31900e4b85922754c9cdfce7c`.

## Prior convergence

#807 removed 235 net lines of duplicated Task Contract, Evidence, approval, memory, User Decision Gate and Hermes/client/Cockpit doctrine from `PRE_EXECUTION_SIMULATION.md`.

The retained file now explicitly specializes Movement 6 — `Test` of `GOVERNED_METHOD_STANDARD.md` and delegates downstream responsibilities to their existing owners.

## Owner test

#787 asks:

> If all rules already owned elsewhere are removed from this file, does enough distinct normative responsibility remain to justify an independent owner?

For the narrowed simulation document, the answer is **yes**.

The remaining responsibility is not generic Test doctrine. It specifically owns:

```text
when bounded pre-execution simulation is justified
bounded scenario-set semantics
simulation-request method seam
Simulation Result Candidate meaning and status vocabulary
interpretation of evaluation / guardrail / trajectory signals
Improvement Candidate boundary
safe simulation-specific outcomes
handoff to the Hermes simulation capability candidate
```

Moving all of this into `GOVERNED_METHOD_STANDARD.md` would make the parent method document carry a specialized stress-test protocol and would reverse the intended parent/specialization split.

## Relationship to parent owner

```text
GOVERNED_METHOD_STANDARD.md
  owns generic Produce Candidate -> Test -> Status discipline

PRE_EXECUTION_SIMULATION.md
  owns one specialized Test technique when consequence justifies simulation
```

The specialization does not redefine generic Evidence, approvals, memory, PDP/PEP, Cockpit or runtime semantics.

## Consumer evidence

Current consumers include:

- `DISTILLATION_REGISTRY.md`, which records the external-pattern provenance;
- `hermes/profiles/_base/EVALUATION_AND_SIMULATION_CANDIDATE.md`, which describes the non-installed Hermes-side execution candidate and needs a Pantheon governance owner for what simulation means.

These consumers support a stable governance specialization rather than a purely local paragraph in the parent method.

## Authority correction

Before this decision, `PRE_EXECUTION_SIMULATION.md` declared active support doctrine but had no row in `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`.

This slice adds one row:

```text
PRE_EXECUTION_SIMULATION.md
active support doctrine
documented non-implemented
specialized Movement 6 Test owner for bounded simulation
```

This records existing authority; it does not promote the document to a new authority class.

## Truncation acknowledgement cleanup

#807 temporarily added `PRE_EXECUTION_SIMULATION.md` to `.github/scripts/truncation_ack.txt` because its deliberate 499 -> 264 line reduction crossed the net-truncation guard.

The guard file states that acknowledgements should be removed once the deliberate shrink has merged. #807 is merged, so this slice removes that six-line temporary acknowledgement.

No guard logic changes.

## Exact change before this log

```text
GOVERNANCE_AUTHORITY_INDEX.md   +1 / -0
truncation_ack.txt               +0 / -6
```

## Authority impact

No new authority class or runtime capability is created. A previously unindexed active-support specialization is made explicit in the existing authority map.

## Runtime impact

None.

## Preserved invariants

```text
specialization != duplicate owner
simulation pass != approval
simulation result != Evidence admission
simulation repetition != Registre Probatoire entry
evaluation score != policy decision
runtime success != authorization
PDP decision != PEP execution
projection != approval
```

## Verification rule

The PR must pass Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on its exact final HEAD. The final patch, reviews, threads and comments must be read before merge. Any later HEAD modification invalidates earlier evidence.
