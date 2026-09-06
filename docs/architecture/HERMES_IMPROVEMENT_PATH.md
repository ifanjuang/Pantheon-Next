# Hermes improvement path — evaluation first, training only on a proven model gap

Status: selected architectural direction / external optimization and training tooling remain candidate and unactivated.
Boundary profile: candidate_support_note.

Date: 2026-09-06

## Objective

Keep Hermes as the single external execution runtime and improve it at the cheapest, most reversible layer first.

The selected order is:

```text
observe Hermes behavior
        |
        v
measure against bounded evaluation cases
        |
        v
classify the failure
        |
        +--> skill / prompt / tool / context / retrieval / binding
        |        |
        |        `--> fix that layer, then re-evaluate
        |
        `--> residual model limitation proven
                 |
                 v
             LlamaFactory
                 |
                 `--> optional Unsloth acceleration when compatible
                 |
                 v
          trained artifact candidate
                 |
                 v
         separate model qualification
                 |
                 v
       existing serving path only
```

This document does not create an evaluation runtime, optimizer runtime, training service, provider router, model server, deployment, dataset authority or authorization path.

## Verified repository baseline

Observed before this rewrite:

```text
Pantheon main = 232e78b1e7b9114a3f6be2e7d40c412ca33209c1
PAIR + Unsloth qualification planning = merged through #970
Hermes improvement PR #976 = 36 commits behind main before reconciliation
```

Since #976 was first written, current `main` has added further bounded Hermes-facing surfaces, including explicit PDF qualification preparation and continued Context Admission/security work. Those existing contracts and labs are useful evaluation cases. They are not replaced by a new benchmark owner here.

## Existing owners reused

The selected path reuses current responsibilities:

```text
Pantheon                 -> governance, eligibility, scope, approval and Evidence boundaries
Hermes                   -> external agent/tool execution
existing tests/labs      -> bounded executable behavior checks
PAIR                     -> physical request routing qualification across local nodes
Ollama / LM Studio       -> local model serving candidates behind PAIR
LlamaFactory             -> candidate training facade only when weight tuning is justified
Unsloth                  -> optional acceleration inside the training path when compatible
```

No second agent runtime, scheduler, provider router, evaluation service or model-serving path is added.

## The durable owner is the improvement method, not Self-Evolution

The architectural primitive is the **Hermes evaluation / improvement loop**:

```text
observe -> measure -> classify -> change one layer -> compare -> review
```

`NousResearch/hermes-agent-self-evolution`, DSPy and GEPA are possible automation mechanisms for parts of that loop. They are not the loop itself and are not required dependencies.

### Current Self-Evolution observation

Observed upstream repository: `NousResearch/hermes-agent-self-evolution`.

Observed `main` head on 2026-09-06:

```text
0a929e3aa20e15cf04dc7c28492a7d41a5139125
```

No newer commit was observed after 2026-06-17.

Upstream issue #141 remains open. It reports that the skill-evolution path can improve optimizer state while the emitted `SKILL.md` remains byte-identical to the input. Therefore:

```text
Self-Evolution role = optional future automation candidate
Self-Evolution activation = unresolved / blocked pending independent qualification
Self-Evolution dependency = not selected
```

An optimizer score is never accepted as proof that the persisted skill improved.

## Evaluation comes before optimization tooling

Pantheon should first maintain a bounded set of Hermes behavior cases assembled from already-owned contracts and qualification surfaces rather than inventing a second testing framework.

Useful categories include:

```text
structured tool calling
scope isolation
refusal / approval boundaries
Context Admission and untrusted external content
PDF/document understanding qualification
provenance preservation
retrieval behavior
memory != Evidence boundaries
provider/binding fallback behavior
professional structured extraction where a deterministic contract exists
```

The evaluation set may aggregate references to existing fixtures/tests/labs and add small synthetic cases where gaps exist. It must not duplicate the implementation owner of those checks.

```text
evaluation case != Evidence
evaluation score != professional correctness
runtime trace != Evidence
benchmark corpus != training dataset
```

## Failure classification gate

Before changing model weights, a failure must be classified against the layers that can already explain it:

1. Skill or instruction defect.
2. Prompt/system instruction defect.
3. Tool description or tool contract defect.
4. Context Admission/context-budget defect.
5. Retrieval/ranking/provenance defect.
6. Provider/binding/routing defect.
7. Residual model capability defect.

Weight tuning is downstream of items 1–6. A model must not be trained to compensate for a defect owned elsewhere.

## One training facade: LlamaFactory

Observed upstream repository: `hiyouga/LlamaFactory`.

Latest published stable release observed for this decision:

```text
v0.9.5
7af909522a951e3ad9f022ea6f88b6755257eaa5
```

Observed upstream `main` head on 2026-09-06:

```text
dced5f8804bfbf7109ef7c14401db6bd5cce7e53
```

LlamaFactory already exposes Unsloth as an optional LoRA optimization through `use_unsloth`. Pantheon therefore does not need two competing training workflows.

Selected placement:

```text
model adaptation / fine-tuning facade
        |
        v
   LlamaFactory
        |
        +--> standard supported training path
        |
        `--> use_unsloth: true
             when the selected model/method/runtime combination is compatible
```

LlamaFactory remains replaceable and candidate. Selecting it as the preferred qualification facade does not install or authorize it.

## Unsloth is an accelerator, not a second architecture

Merged #970 retains useful Unsloth compatibility observations and a bounded direct-provider experiment. Those observations are not discarded.

The selected role is narrower:

```text
Unsloth primary role = optional VRAM-efficient LoRA/training acceleration under LlamaFactory when supported
Unsloth independent training facade = not selected
Unsloth permanent serving role = not selected
```

A future qualification may still run Unsloth directly to understand performance or compatibility. That does not create a second production path.

```text
Unsloth provider compatible != Unsloth selected for serving
Unsloth acceleration enabled != trained model qualified
```

## Serving remains separate

The serving direction remains unchanged:

```text
Pantheon governs
      |
      v
Hermes executes
      |
      v
PAIR routes one request to an eligible node
      |
      v
Ollama / LM Studio serve
      |
      v
GPU nodes
```

PAIR routing does not pool VRAM, approve a model, authorize a task or admit Evidence.

## Operational priority

The immediate priority is not training.

The merged #970 runbook already defines the bounded physical-routing work. Execute that before investing in model adaptation:

```text
Q1A -> Linux RTX 4080 isolated PAIR + Ollama observation
Q1B -> Linux RTX 4080 + Windows RTX 4090 routing / failover / rejoin
Q1C -> current Hermes container -> local PAIR ingress compatibility
```

Only after the serving path has real observations should the evaluation inventory be used to establish a Hermes/model baseline.

## Weight-tuning admission gate

If evaluation leaves a repeated residual model limitation after the other layers are corrected, a LlamaFactory qualification may be prepared.

It must capture at least:

```text
base model identity + license
training facade version/ref
whether Unsloth acceleration is enabled
training configuration
source dataset manifest and scope
train / validation / held-out separation
adapter/checkpoint identity + hash
GPU/VRAM/RAM observations
reproducibility inputs
held-out quality and refusal/regression results
structured tool-call behavior after export
export format and artifact identity
```

Project/client material is **not training data by default**. Synthetic or explicitly scoped, minimized and authorized data is the default qualification posture.

## Model adoption remains separate

A successful training run produces a model/adapter candidate only.

```text
training completed != model qualified
model qualified != model activated
model activated != task authorized
benchmark gain != professional correctness
dataset != Evidence
runtime trace != Evidence
memory != Evidence
project data available != training authorized
export succeeded != deployment selected
```

Before serving, the trained artifact requires separate qualification for its intended Hermes workload, structured tool use, refusal regressions, context behavior, provenance, licensing and rollback.

## Next bounded slices

In order:

1. Execute the existing PAIR Q1A/Q1B/Q1C hardware observations from the merged #970 runbook.
2. Inventory existing Hermes/Pantheon tests and qualification cases into one evaluation reference set without moving their ownership.
3. Measure baseline behavior on the selected local models.
4. Correct skill/prompt/tool/context/retrieval/binding defects where measured.
5. Re-evaluate.
6. Only if a residual model defect is proven, prepare one LlamaFactory training qualification; enable Unsloth only as an optional accelerator when compatible.
7. Revisit Self-Evolution only after its upstream defect is resolved or independently bounded by a reproducible fix.

Magnitude remains outside the selected path.

## Boundary

This document selects responsibility placement and evaluation order. It claims no live runtime or training result.

```text
live PAIR observations = still required
Hermes evaluation reference set = to assemble from existing owners
Self-Evolution activation = unresolved / blocked
LlamaFactory activation = not_run
Unsloth acceleration = not_run
serving topology change = none
```
