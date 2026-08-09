# Capability Registry

Status: candidate / to verify — governance declaration of capabilities, organized as a dependency graph for governed composition.

A capability registry is a governance declaration of *what capabilities exist*, *what each may and may not do*, and *which other capabilities each one depends on*. It is the index from which HEPHAISTOS forges a Workflow Manifest candidate (`WORKFLOW_SCHEMA.md`).

It is not a runtime. It is not a skill installer. It is not a plugin manager. It is not a tool dispatch table. It does not execute, schedule, queue or route anything.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Candidate posture

This document is useful, but it remains `candidate / to verify` until explicitly promoted in `AUTHORITY_INDEX.md`.

A capability declaration inside this registry is also a candidate until reviewed.

Candidate status is intentional: the registry introduces a new organizing surface and must remain visibly non-canonical until its interactions with Workflow Manifests, HEPHAISTOS, Registre Probatoire and module preflight are reconciled.

## Core principle

A capability is declared by its governance metadata only.

An executable Skill, plugin, MCP server, connector or other implementation lives outside Pantheon, in the execution runtime or adapter layer. It is not the Capability identity.

Pantheon holds the abstract declaration; the runtime or adapter holds an implementation.

```text
The registry declares the Capability.
An explicit binding may reference an admitted implementation.
The forge composes declared capabilities.
The runtime executes the selected implementation.
Pantheon governs eligibility, evidence support and status.
```

A capability declaration is a candidate until reviewed. Availability is not authorization.

Installability is not capability approval.

```text
Capability != Skill
Capability != Tool Card
Capability != implementation
capability_id != skill_id by rule
```

Identifiers may happen to use the same lexical string in legacy or external material. Such equality never establishes identity, admission, binding or authorization.

## Capability declaration

A capability declaration should remain structurally small. Canonical fields:

```text
Identity        stable abstract governance identifier and clear title
Purpose         the professional outcome it serves
Inputs          expected inputs
Outputs         allowed outputs
Forbidden       forbidden outputs and forbidden effects
Risk class      consequence if it goes wrong
Authority       what it may decide; what it must escalate
Dependencies    other capabilities it relies on
Domain scope    where it applies (domain pack, dossier, scope_id)
Evidence        expected Evidence Pack Candidate shape and probative support
Provenance      where the declaration came from, and when
Status          candidate / sandbox_only / project_enabled / reviewed / suspended / superseded / rejected
```

A declaration describes governance.

It does not describe scheduling, retries, provider routing or tool dispatch.

Implementation identity, release/version identity and runtime binding are separate concerns. One Capability may later have several implementation candidates or releases without becoming several Capabilities.

## Skill admission guard

External skill catalogues, public repositories and package installers may expose or distribute Skills that could implement one or more declared capabilities. They do not create, approve or authorize those capabilities.

A Skill may be easy to install, recommended by a catalogue, popular, discoverable, synced across agents or already present in a runtime. None of those states makes it eligible to back a Pantheon-governed Capability use.

```text
visible       != admitted
available     != authorized
installed     != approved
synced        != reviewed
discoverable  != trusted
recommended   != safe
popular       != safe
MCP available != task-authorized
```

Before a runtime Skill may be used as an admitted backing implementation, its Skill admission material must record at least:

```text
Source          repository, package, catalogue entry or local origin
Version         pinned version, commit hash, content hash or immutable release reference
Author          upstream author, maintainer or internal owner
Installer       how the runtime obtains it, if relevant
Permissions     requested file, network, command, connector or write perimeter
Scope           allowed dossier, project, domain, user or organization scope
Forbidden       forbidden effects, forbidden outputs and forbidden persistence
Risk class      consequence if it fails or exceeds its declared boundary
Approval ceiling maximum approval level it may reach without human decision
Evidence        required Evidence Pack Candidate shape
Owner           person accountable for admission review
Reviewed by     reviewer and review date
Status          candidate / sandbox_only / project_enabled / reviewed / suspended / superseded / rejected
```

A Skill with unknown source, floating version, broad command access, hidden network access, write access to doctrine, free access to private material or external side effects is not eligible by default.

The safe default is project-scoped admission, pinned version, minimum permissions and explicit review. Global skill installation, multi-agent installation, remote synchronization and automatic skill update are governance risks unless separately reviewed and bounded.

The Skill admission contract may record that a Skill exists and is eligible to back a Capability. The Capability Registry must not install it, update it or treat an external catalogue as a source of authority.

### MCP write-capable skill managers

A SkillsGate-like tool is a skill manager, not a governance authority. It may expose skill inventory, discovery, preview, installation, removal, update and synchronization through CLI, TUI, desktop UI or MCP tools.

Pantheon may use that operational model to define admission metadata. It must not import the manager as Pantheon machinery.

Read-only skill inventory is low-risk only when it remains inventory:

```text
list installed skills
show source and installed path
show target agents
show installedAt / updatedAt metadata
show lockfile or hash metadata
show catalogue source
```

Preview-before-install is also only a candidate step:

```text
list discovered skills without installing
read SKILL.md metadata
surface declared tools and permissions
prepare Skill Admission Candidate
```

Write-capable operations are external actions and must be gated:

```text
install skill into one agent
install skill into several agents
remove skill
update skill
sync skills from packages or remote servers
edit local skill content
```

Those operations may be available through MCP, but MCP availability is not authorization. A write-capable MCP tool may prepare a candidate review or ask for a User Decision Gate. It must not silently install, update, remove or sync skills for governed work.

Suggested refusal tests for any SkillsGate-like admission path:

```text
refuse public-skill global install without review
refuse multi-agent install without explicit target scope
refuse package sync without inventory review
refuse unpinned source or floating branch for governed work
refuse broad filesystem, shell, network or connector access without permission mapping
refuse catalogue ranking as a safety signal
refuse local skill edits that preserve reviewed status without re-review
refuse use on client or project data before project-scoped admission
refuse skill output as proof, approval or Registre Probatoire material without evidence review
```

The useful pattern to keep is the admission gap:

```text
The catalogue discovers.
The manager installs.
The runtime exposes implementation inventory.
Pantheon admits or blocks implementation eligibility.
An explicit binding links an admitted implementation to a Capability use.
Task Contract / Execution Admission separately authorizes a runtime opportunity.
The human approves consequential use.
```

## Why a graph, not a list

Capabilities are declared with their dependencies, so the registry forms a graph,
not a flat list. This lets the forge retrieve a capability *and the capabilities it
structurally needs*, instead of matching free text.

```text
high-level capability   "prepare the project form"
  depends on
mid-level capabilities  "fetch form template", "resolve known field", "verify entity"
  depends on
low-level capabilities  "read scoped source", "render annotated document"
```

Retrieval starts from a small seed selected by declared purpose, then follows
declared dependencies to recover what is structurally required. The graph is a
governance map of dependency, not an execution graph.

## Metadata-first selection

Only the Capability declaration is read during composition. A backing implementation is referenced explicitly and invoked only after the forged manifest is found eligible and execution is authorized, outside Pantheon. This keeps composition reviewable and cheap: a reviewer reads declarations, not runtime code, and the registry can hold many capabilities while a recipe references only the few it needs.

```text
read the Capability declaration to compose
resolve an admitted backing implementation explicitly
invoke that implementation only when separately authorized, outside Pantheon
```

## Enrichment is governed

The registry may be enriched over time — new capabilities, new domain sources,
new declarations. Enrichment is a governed step.

```text
a new capability declaration enters as candidate
review may promote it
a superseded declaration is archived, not deleted (CHARON)
```

No capability self-registers as authority. No implementation self-promotes into a Capability. No enrichment auto-promotes. The registry must not become a marketplace, an automatic installer or a capability runtime.

## Relationship to the forge

HEPHAISTOS reads this registry to assemble a Workflow Manifest candidate. The
registry supplies the eligible capabilities and their dependencies; the forge
supplies the topology and the per-step signatures; Pantheon supplies the cap,
the gates and the status.

```text
registry   -> what abstract capabilities exist and what they may do
forge      -> how declared capabilities are composed for this cap
binding    -> which admitted implementation may back a capability step
Pantheon   -> whether the recipe is eligible, evidence-supported and approved
runtime    -> execution, outside Pantheon
```

## Relationship to skills and modules

A Capability declaration is a governance declaration of a professional or system function. It is not a Skill declaration and it is not an executable Hermes Skill.

`schemas/skill_manifest.schema.yaml` governs Skill-oriented admission material. Hermes Skills or other runtime implementations execute outside Pantheon under Task Contract.

Skill catalogues and installers are distribution surfaces for the execution runtime. They are not Pantheon authority. A discovered or installed Skill must still be admitted as an implementation before it may explicitly back a governed Capability step.

### Shared vocabulary with Skill admission and the forge

The Capability Registry, Skill admission and forged recipe participate in one chain, but they keep separate identities. The current executable schemas already model this separation:

```text
Capability identity     = capability_step.capability_id
Skill identity          = skill_manifest.skill_id
backing link            = capability_step.skill_manifest_ref
                          -> skill_manifest.skill_id
risk vocabulary         = shared scale: low / medium / high / critical
                          (skill_manifest.risk_level compatible with capability_step.risk_class)
status                  = distinct lifecycles:
                          Capability / composition status
                          Skill admission status
                          task/run authorization status
```

There is no required identifier equality between `capability_id` and `skill_id`.

A Skill may potentially back more than one Capability use when each binding is explicit and eligible. A Capability may later have several implementation candidates or releases. Neither direction changes the abstract `capability_id`.

A forged step that relies on a Skill should reference the admitted Skill explicitly with `skill_manifest_ref`. A step that requires a backing Skill but references an unadmitted Skill is not eligible: implementation admission precedes binding, composition precedes task authorization, and execution remains external.

```text
admit implementation
-> bind explicitly to Capability use
-> compose the recipe
-> arbitrate eligibility
-> authorize task/run separately
-> execute outside Pantheon
```

## Relationship to scope and memory

A capability declares its domain scope (`SCOPE_ISOLATION.md`, `CORE_RECORDS_MODEL.md`).
A capability that crosses scopes must say so and is governed accordingly. The
registry records declarations; it does not promote memory and it is not a Registre Probatoire entry.

## Bonus tool candidate map

Bonus tools are optional adapters or references that may enrich the execution surface, but are not required for Pantheon governance.

They remain implementation or binding candidates until separately admitted and explicitly associated with a governed Capability use.

```text
bonus tool visible       != admitted implementation
bonus tool documented    != installed tool
bonus adapter reachable  != Capability declared
bonus adapter reachable  != task authorization
bonus output generated   != evidence, proof, approval or memory
```

### `bfl_openai_image_proxy`

```text
id: bfl_openai_image_proxy
label: BFL OpenAI Image Proxy
source_review: BFL_OPENAI_IMAGE_PROXY_REVIEW.md
cartography_class: bonus_tool_candidate
primary_layer: adapter / binding
exposure_surface: OpenWebUI
execution_provider: Black Forest Labs FLUX
purpose: expose FLUX text-to-image generation through an OpenAI-compatible image endpoint for OpenWebUI
allowed_outputs:
  - Image Candidate
  - Result Candidate
  - Trace Reference
  - Evidence Pack Candidate only if separately reviewed
forbidden_outputs:
  - proof
  - professional validation
  - approved client deliverable
  - Registre Probatoire entry
  - memory promotion
  - provider routing authority
risk_class: medium when client-facing or project-decision support is possible
approval_ceiling: candidate-only unless a User Decision Gate approves narrow use
memory_behavior: none by default
status: optional_bonus_candidate / documented_non_implemented
```

Placement phrase:

```text
OpenWebUI exposes image generation.
The proxy adapts the OpenAI-compatible request.
BFL executes image generation.
Pantheon governs status, scope, evidence, delivery and memory.
```

This entry only adds the tool to the cartography. It does not create a Capability declaration, install, configure, admit or authorize the proxy.

## Boundary

Documentation only. This registry is a governance declaration. It does not
implement a runtime, an installer, a scheduler, a queue, a provider router, tool
dispatch, external catalogue integration, automatic skill update, automatic skill
promotion or automatic memory promotion. Execution remains external.

```text
The registry declares abstract capabilities and their dependencies.
Explicit references bind admitted implementations when needed.
The forge composes capabilities for a cap.
Pantheon governs eligibility, evidence support and status.
Task Contract / Execution Admission governs task/run legitimacy.
The execution runtime executes outside.
The human engages.
```
