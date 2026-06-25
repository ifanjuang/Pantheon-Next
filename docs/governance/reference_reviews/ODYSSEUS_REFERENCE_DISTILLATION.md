# Odysseus Reference Distillation

Status: external reference / support review — candidate distillation only.

Sources reviewed:

```text
https://github.com/pewdiepie-archdaemon/odysseus
https://github.com/pewdiepie-archdaemon/odysseus/blob/main/README.md
https://github.com/pewdiepie-archdaemon/odysseus/blob/main/docs/setup.md
https://github.com/pewdiepie-archdaemon/odysseus/blob/dev/THREAT_MODEL.md
https://github.com/pewdiepie-archdaemon/odysseus/blob/dev/docker-compose.yml
```

This document records what Pantheon Next may distill from Odysseus without importing Odysseus as a Pantheon runtime, source of truth, approval authority, memory authority, scheduler, provider router, connector gateway or execution dependency.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## External system posture

Odysseus presents itself as a self-hosted AI workspace for chat, agents, research, documents, email, notes, calendar and local model workflows.

Relevant operational surfaces observed:

```text
chat and agents
local / API models
tools and MCP
files
shell-capable admin surface
skills
memory
hardware-aware model recommendation and serving
multi-step research
model comparison
writing / document surface
email
notes, tasks, calendar and scheduled agent tasks
image editor
uploads, search, presets, sessions and 2FA
```

Pantheon classification:

```text
external system: Odysseus
primary class: exposure surface + execution runtime + local AI workspace
Pantheon status: external reference / support review
allowed use: inspiration and adapter review only
forbidden use: Pantheon core dependency or source of governance authority
```

## Boundary verdict

Accepted:

```text
Odysseus as a useful reference for AI workspace UX.
Odysseus as a useful reference for runtime threat modeling.
Cookbook as inspiration for model capability passporting.
Deep Research as inspiration for a Research Run Candidate.
Compare as inspiration for a Comparison Candidate.
Untrusted context wrapping as inspiration for source-admission discipline.
Setup posture as inspiration for capability health and exposure checks.
```

Refused:

```text
Odysseus as Pantheon runtime.
Odysseus as Pantheon governance layer.
Odysseus memory as canonical memory.
Odysseus workspace state as dossier state.
Odysseus scheduled tasks as approved action.
Odysseus email / calendar actions as external effects without Pantheon gate.
Privileged local tools in client or agency dossiers without sandbox, scope and explicit approval.
Host-control access as a normal capability.
Successful Odysseus execution as proof, approval, validation or memory promotion.
```

To verify:

```text
Whether Hermes already covers the useful Cookbook placement better than Odysseus.
Whether OpenWebUI can expose the useful workspace / comparison / research views without adding a new product.
Whether Langfuse or another observability layer covers comparison and trace review more cleanly.
Whether the MCP Policy Server should expose read-only checks for model passports, research runs and runtime threat reviews.
Whether a separate adapters repository is needed before any runnable Odysseus-inspired configuration exists.
```

To arbitrate:

```text
Should Pantheon Next create a generic Model Capability Passport before adding any Hermes model-selection adapter?
Should Research Run Candidate and Comparison Candidate become first-class governance objects?
Should host-control surfaces automatically force critical risk classification?
Should workspace projection boundaries become a dedicated support doctrine document?
```

## Distillation 1 — External Runtime Threat Model Review

Odysseus is valuable because it states the operational danger plainly: the system is a self-hosted AI workspace with privileged local access. Pantheon should distill that into a review object for any external runtime or workspace.

Candidate fields:

```text
external system
version or reviewed reference
trusted-user assumption
public-exposure posture
authentication posture
role model
privileged capability list
network exposure posture
untrusted content paths
prompt-injection controls
token-scope granularity
known gaps
Pantheon gate required
decision: accepted | refused | to_verify | to_arbitrate
```

Pantheon rule:

```text
A runtime with privileged local access is not just a tool. It is an external effect surface.
```

## Distillation 2 — Model Capability Passport

Cookbook is useful because it treats model use as situated: recommendation, hardware fit, local or remote serving and runtime path. Pantheon should not import Cookbook. It should distill a model passport that makes model use reviewable before Hermes or any runtime uses it for consequential work.

Candidate fields:

```text
model identifier
provider or runtime
local or external posture
serving surface
version or digest
context window
modality
cost class
latency class
hardware requirement
data exposure
retention unknowns
authorized task families
forbidden task families
professional-use ceiling
evidence expectation
approval required for use
known failure modes
fallback model
status
```

Pantheon rule:

```text
Model available does not mean model appropriate.
Model selected does not mean output approved.
```

## Distillation 3 — Research Run Candidate

Deep Research is useful as a product pattern, not as proof. It performs multi-step research with source reading and report generation. Pantheon should distill the run itself as an auditable candidate.

Candidate fields:

```text
run identifier
initial question
scope
source policy
freshness requirement
search queries
sources found
sources read
sources rejected
rejection reasons
claims extracted
claims without source
contradictions
freshness check
unresolved unknowns
result candidate reference
evidence pack candidate reference
output status
```

Pantheon rule:

```text
Deep research produces a research dossier candidate, not truth.
```

## Distillation 4 — Comparison Candidate

Odysseus Compare is useful because it frames blind side-by-side model comparison and synthesis. Pantheon should distill comparison as a review aid while refusing the consensus fallacy.

Candidate fields:

```text
comparison identifier
question
task contract reference
compared outputs
agreement points
conflicts
missing evidence
stronger candidate
reason for preference
reviewer role
human decision required
final status
```

Pantheon rule:

```text
Two models agreeing is not proof.
A comparison supports review; it does not validate.
```

## Distillation 5 — Workspace Projection Boundaries

Odysseus combines many workspace objects in one product surface: chat, documents, notes, memory, email, calendar, tasks, research and images. Pantheon should make the projection boundary explicit.

Candidate vocabulary:

```text
workspace_item
project_source
dossier_piece
context_candidate
evidence_candidate
result_candidate
register_candidate
registre_probatoire_entry
```

Pantheon rule:

```text
Workspace proximity does not imply dossier inclusion.
Dossier inclusion does not imply evidence.
Evidence candidate does not imply approval.
Register candidate does not imply canonical memory.
```

## Distillation 6 — Scheduled Intent Candidate

Odysseus includes reminders, tasks, calendar and scheduled agent tasks. This is useful for professional workflows, but dangerous if schedule is confused with authority.

Candidate fields:

```text
intent identifier
trigger kind
observed context
proposed task
target scope
possible external effect
possible memory effect
possible truth claim
approval required
safe default
admissibility status
```

Pantheon rule:

```text
A schedule can reopen a question.
It cannot approve the answer or authorize the action.
```

## Distillation 7 — Untrusted Context Admission Rule

Odysseus treats external content reaching the LLM as untrusted. Web results, fetched pages, read emails, saved memories, skill text, notes and external tool outputs are data before they are instructions or evidence.

Candidate fields:

```text
source reference
origin
channel
received as
instruction authority
trusted status
claim-use status
evidence requirement
allowed task use
forbidden task use
minimization requirement
prompt-injection risk
```

Pantheon rule:

```text
External content is data before it is source.
A source is candidate before it is evidence.
Evidence supports; approval validates.
```

## Distillation 8 — Host Control Surface Classification

Odysseus shows that a workspace can include local privileged operational surfaces. Pantheon should classify those surfaces explicitly instead of treating them as ordinary skills.

Candidate vocabulary:

```text
host_control_surface:
none
scoped_filesystem
broad_filesystem
shell_user
shell_admin
container_host_control
ssh
cloud_admin
```

Pantheon rule:

```text
A capability with host-control power is critical runtime power by default.
It must not be treated as a normal skill.
```

## Placement

| Distilled object | Pantheon placement | External execution surface | Exposure surface |
|---|---|---|---|
| External Runtime Threat Model Review | support doctrine / review template | none by default | dashboard status |
| Model Capability Passport | capability governance | Hermes / model runtime | model picker / health view |
| Research Run Candidate | evidence / source policy support | Hermes research skill | research report view |
| Comparison Candidate | review / decision support | Hermes or comparison tool | side-by-side review view |
| Workspace Projection Boundaries | scope / memory / evidence doctrine | none by default | cockpit labels |
| Scheduled Intent Candidate | request lifecycle / approval doctrine | scheduler outside Pantheon | task / reminder surface |
| Untrusted Context Admission | source policy / context packs | runtime prompt wrapper | source admission warning |
| Host Control Surface Classification | external tools policy | runtime / deployment | admin cockpit warning |

## Repository state

```text
Documented non-implemented.
No runtime.
No schema.
No tests.
No operations file.
No platform file.
No Docker file.
No OpenWebUI configuration.
No Hermes skill.
No adapter repository.
No external action.
No memory promotion.
```

## Follow-up candidates

```text
1. Promote External Runtime Threat Model Review into a generic support doctrine template.
2. Draft Model Capability Passport as the first practical bridge between Hermes model choice and Pantheon governance.
3. Draft Research Run Candidate and Comparison Candidate only if architecture-domain workflows need them immediately.
4. Add host_control_surface to the external-tool review vocabulary.
5. Keep any Odysseus runtime experiment outside Pantheon Next and behind sandbox rules.
```

## Boundary phrase

```text
Odysseus shows what a powerful AI workspace can expose and execute.
Pantheon distills the conditions under which such power may be used.
The workspace does not decide.
The runtime does not validate.
The human decides.
Only the validated remains.
```
