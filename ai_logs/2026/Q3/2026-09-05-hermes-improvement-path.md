# Hermes improvement path — converged on evaluation first

Date: 2026-09-06

Status: candidate architecture rewrite for #976; no live runtime, training or model activation performed.
Boundary profile: validation_only.

## Objective

Reconcile the original #976 proposal with current Pantheon `main` and simplify the selected path:

```text
Hermes evaluation/improvement method
  -> durable direction
Self-Evolution / DSPy / GEPA
  -> optional automation candidate, not a dependency
LlamaFactory
  -> one candidate training facade
Unsloth
  -> optional accelerator under that facade when compatible
PAIR + Ollama/LM Studio
  -> unchanged serving direction
```

## Repository state checked

Before rewriting the branch:

```text
current main = 232e78b1e7b9114a3f6be2e7d40c412ca33209c1
old #976 head = 5264987c526d2ca9df11cadd6eb4c9cef867c7a0
#976 behind main = 36 commits
```

Current `main` already contains merged #970 and later Hermes-facing work, including explicit PDF qualification preparation and additional Context Admission/security work. No current owner for a generic Hermes evaluation/improvement loop was found by repository search. Existing tests and qualification labs are therefore reused as case owners rather than replaced.

## Upstream state checked

### Hermes Agent Self-Evolution

Observed `main`:

```text
0a929e3aa20e15cf04dc7c28492a7d41a5139125
```

No newer commit was observed after 2026-06-17. Upstream issue #141 remains the activation blocker described in the original slice: claimed optimization may not correspond to a changed persisted skill artifact.

Decision:

```text
method selected != Self-Evolution selected
Self-Evolution = optional future automation candidate
activation = blocked / unresolved
```

### LlamaFactory

Observed stable release:

```text
v0.9.5
7af909522a951e3ad9f022ea6f88b6755257eaa5
```

Observed `main`:

```text
dced5f8804bfbf7109ef7c14401db6bd5cce7e53
```

Current source exposes `use_unsloth` for LoRA optimization. This removes the need to present LlamaFactory and Unsloth as two peer training architectures.

Decision:

```text
LlamaFactory = preferred qualification facade for model adaptation
Unsloth = optional accelerator/binding when compatible
```

No new qualification pin is added by this rewrite. Observed upstream state is not adoption.

## Convergence

The previous path risked reading as:

```text
Self-Evolution -> LlamaFactory or Unsloth
```

The selected path is now:

```text
observe / measure / classify
        |
        +--> fix skill/prompt/tool/context/retrieval/binding
        |
        `--> proven residual model gap
                 |
                 v
             LlamaFactory
                 |
                 `--> optional Unsloth acceleration
                 |
                 v
          model candidate
                 |
                 v
          separate qualification
```

Self-Evolution can later automate part of the first branch, but cannot become the architecture owner.

## Operational priority

Training is not the next runtime task. Merged #970 already defines the bounded PAIR hardware lab. The next execution priority remains:

```text
Q1A 4080 Linux
Q1B 4080 Linux + 4090 Windows
Q1C Hermes container -> PAIR
```

After real serving observations, assemble an evaluation reference set from existing tests/labs and measure baseline behavior before changing weights.

## Explicit non-changes

- no production Compose change;
- no Hermes distribution lock change;
- no provider configuration change;
- no scheduler/router/runtime owner added;
- no new evaluation runtime;
- no Self-Evolution installation/execution;
- no LlamaFactory installation/execution;
- no Unsloth training execution;
- no project/client training dataset created;
- no model or skill activation;
- no Evidence admission.

## Governance boundaries

```text
retrieved data != truth
memory != Evidence
runtime success != authorization
projection != persistence
optimizer score gain != reviewed skill improvement
evaluation score != professional correctness
benchmark corpus != training dataset
training completed != model qualified
model qualified != model activated
project data available != training authorized
PAIR routing != Pantheon authorization
```

## Done gate for this slice

The rewrite is complete when:

1. #976 is based on current `main` while preserving only its four intended files in the diff;
2. the architecture names the improvement method rather than Self-Evolution as durable owner;
3. LlamaFactory is the single candidate training facade and Unsloth is optional acceleration;
4. PAIR hardware execution precedes training work;
5. CI is green;
6. no runtime, deployment, dataset or authority change is introduced.
