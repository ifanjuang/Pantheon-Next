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

## Documents added

```text
docs/governance/CAPABILITY_CANDIDATE_MODEL.md
docs/governance/rites/EXTERNAL_REPO_QUALIFICATION_RITE.md
docs/governance/reference_reviews/CHUNKY_CAPABILITY_REVIEW.md
docs/governance/reference_reviews/MEETILY_CAPABILITY_REVIEW.md
docs/governance/reference_reviews/SURGICALFS_MCPSERVER_CAPABILITY_REVIEW.md
```

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

### CHUNKY_CAPABILITY_REVIEW.md

External reference / capability candidate review.

Recommended status:

```text
accepted_for_sandbox
```

Safe default:

```text
non-sensitive PDFs only;
local execution only;
no Cloud API by default;
no indexation without human approval;
outputs remain candidates.
```

### MEETILY_CAPABILITY_REVIEW.md

External reference / sensitive capability candidate review.

Recommended status:

```text
quarantined_capability_candidate
```

Safe default:

```text
reference review only;
no agency installation;
no client meeting use;
analytics and updater must be reviewed before any sandbox;
external providers blocked unless explicitly approved.
```

### SURGICALFS_MCPSERVER_CAPABILITY_REVIEW.md

External reference / filesystem capability candidate review.

Recommended status:

```text
accepted_for_adapter_design
```

Preferred initial binding:

```text
surgicalfs-local-readonly
```

Safe default:

```text
local stdio only;
read-only mode;
test directory only;
no client data;
no repository write;
no HTTP transport;
no tunnel;
no dashboard exposure;
no analytics file logging;
no mutation tools.
```

Write mode and remote HTTP remain blocked pending explicit gates.

## Boundary decision

No dependency was added.

No implementation was started.

No external runtime was installed.

No OpenWebUI plugin was created.

No Hermes skill was created.

No MCP host was added.

No schema, test, Docker, operation, platform or `.env` path was modified.

## Pending manual index work

`docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` should receive a row for:

```text
docs/governance/CAPABILITY_CANDIDATE_MODEL.md
```

Suggested row:

```markdown
| `docs/governance/CAPABILITY_CANDIDATE_MODEL.md` | candidate support doctrine | documented non-implemented | Candidate grammar for external repositories, tools, bindings and runtime candidates. Defines Capability Slot, Capability Candidate, Binding Candidate and gates without creating a runtime, installer, tool registry, connector gateway, provider router, scheduler, queue, plugin manager, MCP host, memory engine, approval engine, OpenWebUI plugin or Hermes skill. |
```

The three reference reviews are covered by the grouped row:

```text
docs/governance/reference_reviews/
```

The rite is covered by the grouped row:

```text
docs/governance/rites/
```

## Next recommended step

Keep PR as documentation-only change.

Then either:

```text
1. add the authority-index row manually; or
2. split the authority-index update into a smaller reviewed patch.
```

No sandbox execution should start until the PR is reviewed.

First execution candidate, after review, should be a SurgicalFS read-only sandbox profile against a disposable test directory only. This is adapter design, not installation approval.
