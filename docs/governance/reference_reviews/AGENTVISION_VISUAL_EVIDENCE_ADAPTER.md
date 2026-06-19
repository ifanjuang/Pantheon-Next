# AgentVision / Visual Evidence Adapter

Status: external reference / support review — candidate visual evidence placement, documented non-implemented.

This document records how AgentVision may be considered as a visual evidence adapter for rendered artifacts produced or modified around Pantheon Next.

It does not install AgentVision, add a Python dependency, modify `pyproject.toml`, add Docker Compose, modify `operations/`, create a platform service, create a renderer service, add MCP or REST wiring, add CI enforcement, add a schema, create an approval engine, create a memory engine, create an Evidence Pack authority, create a workflow builder or authorize external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## External reference

AgentVision is treated here as an external candidate tool reference.

The public project describes a visual feedback loop for coding agents:

```text
render
-> perceive
-> report
-> fix
-> re-render
-> diff
```

The useful distinction is the split between:

```text
grounded checks
semantic critique
```

Grounded checks may include DOM geometry, computed-style contrast, broken image detection, JavaScript console and network failures, blank-render detection, and located visual or structural issues.

Semantic critique may be produced by a vision model, but any model-proposed location or interpretation remains advisory unless grounded by DOM, computer-vision, OCR, console, network or another verifiable locator.

Reference URLs:

```text
https://github.com/amitpatole/agent-vision
https://pypi.org/project/agentvision/
```

These URLs are references only. Package maturity, release state, security posture and interface stability must be rechecked before any implementation work.

## Placement

AgentVision belongs outside Pantheon core.

It is a candidate execution / observability adapter that may generate visual evidence candidates.

Hermes may request a visual observation.

The Dashboard may expose a read-only visual report or status summary.

Pantheon governs status, evidence, approval, scope and memory.

```text
Hermes executes or requests the render check.
AgentVision observes the rendered artifact.
The Dashboard exposes the visual report.
Pantheon qualifies what status the report may support.
The human decides.
```

## Accepted

Accepted as a candidate adapter pattern:

- AgentVision may be evaluated as a visual evidence adapter for static HTML, generated HTML, SVG, PDF, image or dashboard artifacts.
- AgentVision may support review of `docs/assets/` mockups, including Pantheon Control pages.
- AgentVision may emit screenshots, visual diffs, console findings, network findings, broken image findings, contrast findings, overflow findings and blank-render findings.
- AgentVision may help detect regressions before a human review, especially when a code change alters rendering without breaking tests.
- AgentVision may produce a Visual Evidence Pack Candidate, never a final validation.
- AgentVision may be paired with Langfuse-style observability, but it answers a different question: what did the artifact look like after render?

A Visual Evidence Pack Candidate may contain:

```text
visual_evidence_candidate_id
artifact_ref
render_target
render_backend
viewport
screenshot_ref
visual_diff_ref
grounded_issues
semantic_observations
console_findings
network_findings
verdict
confidence_or_certainty_notes
limitations
```

The term `verdict` here means adapter verdict only:

```text
pass
warn
fail
error
```

It is not Pantheon approval.

## Refused

Refused as Pantheon authority or professional validation:

- AgentVision PASS = approval.
- AgentVision PASS = professional adequacy.
- AgentVision PASS = accessibility compliance.
- AgentVision report = Evidence Pack.
- Vision-model critique = source of truth.
- Screenshot diff = canonical proof.
- Visual report = memory promotion.
- Visual report = external-action authorization.
- Auto-fix loop = permission to commit, merge, publish or deploy.
- A rendered mockup = implemented product behavior.

A visual report may support review.

It must not become the review.

## Dashboard projection

The Dashboard may expose a module such as:

```text
Visual evidence
  adapter: AgentVision
  configured: true | false
  health: unknown | reachable | degraded | unavailable
  last_run_status: not_run | pass | warn | fail | error
  last_report_ref:
  last_screenshot_ref:
  open_report_action: external_link | local_report
```

For a dossier, PR, task or artifact, the Dashboard may show:

```text
Visual report available
Render completed / partial / failed / blocked
Grounded issues found / none found
Semantic observations available / skipped
Result Candidate affected / not affected
Evidence Pack Candidate available / missing
Validation required
No external action authorized unless explicitly approved
Canonical memory unchanged unless validated
```

The Dashboard must not collapse visual status and governance status.

Minimum distinction:

```text
render_status: not_started | success | partial | failed | blocked | unknown
visual_adapter_verdict: pass | warn | fail | error | not_run
governance_result_status: candidate | to_verify | approved | rejected | blocked
external_action_status: unauthorized | approved | executed | refused | failed
```

## Repo signal

Recent dashboard and landing-page work shows why a visual evidence adapter is useful.

Observed review signals include:

- a shared toast style collision affecting `evidence.html` layout;
- mobile source-card selectors that failed to match nested rows, leaving possible overflow or cramped display;
- a JavaScript syntax error caused by typographic quotes in `drafting.html`, preventing the page from rendering its intended UI.

These are not AgentVision findings.

They are repository review signals showing the class of regression a visual feedback loop should help surface earlier.

## Security and source boundary

Rendered artifacts may contain sensitive client, project or professional material.

Before any real use, the following must be decided:

```text
sandboxing
network access
external URL access
artifact retention
screenshot retention
report retention
redaction
who may view reports
whether reports may leave the local environment
```

If the adapter reads external content or generated pages containing untrusted content, indirect prompt injection remains in scope for any semantic critique layer.

The adapter must treat external content as data, not as instruction.

## Relationship with Langfuse / trace observability

Langfuse-style observability and AgentVision-style visual evidence are complementary.

```text
Langfuse observes the run.
AgentVision observes the rendered artifact.
Evidence Pack Candidates preserve support and limitations.
Pantheon qualifies status.
```

Neither trace success nor visual pass validates the professional consequence.

## To verify

- Current AgentVision package state, license, release maturity and maintenance signals.
- Stable CLI, Python, MCP and REST interfaces.
- Whether output can be serialized into a stable report format.
- Whether grounded checks are sufficient without a vision model for first use.
- How screenshots and diffs behave under deterministic viewport settings.
- Whether contrast findings are limited to HTML/CSS and must avoid broad WCAG claims on raster content.
- Whether the tool can run safely in an internal sandbox without exposing project material.
- Whether a generic `Visual Evidence Candidate` contract is needed before schema work.

## To arbitrate

- First evaluation scope: `docs/assets/pantheon-control/` only, or all GitHub Pages artifacts.
- Whether the first pass is manual CLI, Hermes-side adapter, MCP server, REST service or CI advisory check.
- Whether visual failures should block PRs or only create review warnings.
- Where visual reports are stored.
- How long screenshots and diffs are retained.
- Whether semantic critique is disabled initially to keep the first pass fully grounded and local.

## Boundary phrase

```text
AgentVision observes the artifact.
It may produce visual evidence candidates.
It does not validate adequacy, accessibility, approval, memory or action.
Pantheon governs the consequence.
The human decides.
```
