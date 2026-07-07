# AI log — Capability candidate stack

Date: 2026-07-07

Branch: `card-stack-capability-candidates`

Status: candidate documentation work — non-executable.

## Context

The work follows the current Pantheon Next doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The repository already contained `docs/governance/CARD_STACK_MODEL.md`, indexed as candidate support doctrine / documented non-implemented. The task therefore did not recreate the card-stack model. It added the missing capability-candidate layer around external repositories and tool bindings.

After the governance cleanup (#279), the durable form of external reviews is no longer a set of long one-shot review files. New external reviews must be distilled promptly into `docs/governance/reference_reviews/README.md`; a review is a working document, not doctrine.

## Documents retained as durable PR content

```text
docs/governance/CAPABILITY_CANDIDATE_MODEL.md
docs/governance/rites/EXTERNAL_REPO_QUALIFICATION_RITE.md
docs/governance/reference_reviews/README.md
docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md
ai_logs/2026-07-07-capability-candidate-stack.md
```

## Transient reviews distilled

The original PR carried three detailed external reviews. Their durable content is now distilled into `docs/governance/reference_reviews/README.md`, section `Capability candidate distillations (2026-07-07)`.

```text
Chunky       -> accepted_for_sandbox
Meetily      -> quarantined_capability_candidate
SurgicalFS   -> accepted_for_adapter_design
```

The retained rows record only:

```text
tool / repo
abstract capability
Hermes binding candidate
status
safe default
main risk
target doctrine document
```

This keeps the strategic value without recreating the reference-review sprawl removed by #279.

## Classification

### CAPABILITY_CANDIDATE_MODEL.md

Candidate support doctrine.

Defines:

```text
Capability Slot
Capability Candidate
Binding Candidate
Runtime Status Candidate
required gates
card-stack projection
safe defaults
```

Does not implement runtime, installer, connector, tool registry, scheduler, queue, provider router, approval engine, memory engine, OpenWebUI plugin or Hermes skill.

### EXTERNAL_REPO_QUALIFICATION_RITE.md

Candidate support rite.

Defines a bounded review method for external repositories.

Does not clone, install, execute, scan, sandbox, benchmark, approve or create adapters.

## Distilled candidate postures

### Chunky

```text
abstract capability: prepare, inspect and chunk documents before RAG
candidate binding: chunky-local-docker
recommended status: accepted_for_sandbox
safe default: non-sensitive PDFs only; local execution; no Cloud API; no indexation without human approval
main risk: chunks or Markdown candidates treated as evidence, truth or memory
```

### Meetily

```text
abstract capability: meeting summary candidate
candidate binding: none approved
recommended status: quarantined_capability_candidate
safe default: reference review only; no agency install; no client meeting use; external providers blocked pending review
main risk: sensitive meeting material escaping governed scope
```

### SurgicalFS

```text
abstract capability: local filesystem access candidate for adapter design
candidate binding: surgicalfs-local-readonly
recommended status: accepted_for_adapter_design
safe default: local stdio; read-only; disposable test directory; no client data; no repository write; no HTTP/tunnel/dashboard exposure
main risk: filesystem capability escalating into write/runtime authority
```

## Boundary decision

No dependency was added.

No implementation was started.

No external runtime was installed.

No OpenWebUI plugin was created.

No Hermes skill was created.

No MCP host was added.

No schema, test, Docker, operation, platform or `.env` path was modified.

## Index state

`docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` carries a row for:

```text
docs/governance/CAPABILITY_CANDIDATE_MODEL.md
```

The retained distillations are covered by:

```text
docs/governance/reference_reviews/README.md
```

The rite is covered by:

```text
docs/governance/rites/
```

## Non-equivalences preserved

```text
installed != approved
healthy != safe
runtime_success != evidence
binding_selected != dependency_adopted
review_file != doctrine
sandbox_candidate != install_instruction
```

## Next recommended step

Keep PR as documentation-only change.

No sandbox execution should start until the PR is reviewed.

First execution candidate, after review, should be a SurgicalFS read-only sandbox profile against a disposable test directory only. This is adapter design, not installation approval.
