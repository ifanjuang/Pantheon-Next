# Skill Forge Runtimes Reference Review (Voyager, DSPy)

Status: external reference — candidate vocabulary only.

Date: 2026-06-03

Voyager and DSPy are useful external references for *how* capabilities can be
forged on the fly and composed declaratively. They are execution-side systems.

They are not Pantheon architecture models.

They do not authorize a runtime, a forge, generated-skill execution, automatic
memory promotion or autonomous approval inside Pantheon.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## The references

- **Voyager** (`https://github.com/MineDojo/Voyager`) — an LLM agent that writes
  executable skills on the fly, validates them, stores them in an ever-growing
  skill library indexed by natural-language description, and reuses them on new
  tasks. The closest external example of "forge on the fly + reusable library".
- **DSPy** (`https://github.com/stanfordnlp/dspy`) — declares pipeline steps as
  *signatures* (input/output specs), composes them as modules, and compiles the
  composition. The closest external example of declarative composition.

## Accepted distillation

Pantheon may use these as vocabulary sources for:

- a forged recipe assembled from reusable capabilities (HÉPHAÏSTOS, `WORKFLOW_SCHEMA.md`);
- per-step signatures as governance contracts (`CAPABILITY_REGISTRY.md`);
- a capability library indexed by declared purpose, not free text;
- the principle that a forged artifact is a candidate until reviewed.

This is support vocabulary only.

It does not create a module, runtime, forge engine, compiler, schema, OpenWebUI
extension, Hermes skill or approval engine.

## Rejected import

Pantheon must not import these as:

- a runtime that writes and runs generated skills;
- a self-improving execution loop;
- an automatic skill installer or skill library writer;
- a scheduler, a queue or a provider router;
- a memory promotion mechanism;
- a Pantheon Role model;
- a source-of-truth system.

Voyager's skill writing and DSPy's compilation are execution-side concerns. They
belong outside Pantheon, on the runtime side, under Task Contract. Pantheon
governs whether a forged recipe is eligible, proven and approved; it does not
write or run it.

## Forge mechanics as runtime concern

A runtime may write a skill. A runtime may compile a pipeline. Pantheon may govern
whether the resulting capability is eligible. No generated skill is authorized by
the fact of being generated.

```text
forged != authorized
compiled != approved
```

Any generated code, signature, prompt or recipe remains candidate material until
reviewed under Task Contract, Evidence Pack and approval rules.

## Signatures as governance contracts

DSPy-style signatures are useful as a review aid: declaring expected inputs,
allowed outputs and forbidden outputs per step lets a reviewer read a recipe
without running it. A signature in Pantheon is a governance contract for a step,
not a function call. It makes the recipe auditable; it does not make the step
sovereign.

## Boundary phrase

```text
Voyager and DSPy are useful as forge and composition vocabulary.
They are rejected as Pantheon architecture.
The runtime may forge and compile.
Pantheon governs eligibility, proof, status and approval.
The human decides.
```
