# Hermes Role dialogue V4 — admitted-run attachment and Cockpit view

Date: 2026-09-12

## Outcome

The composed Cockpit now attaches its bounded Role relay only after Pantheon
has recorded an exact external Hermes runtime start. Attachment is optional and
requires the explicit `MVP_HERMES_ROLE_TRACE_BASE_URL` and
`MVP_HERMES_ROLE_TRACE_API_KEY` pair.

The Hermes dock contains a compact progressive dialogue list. It uses an
authenticated `fetch` SSE reader, resumes with `Last-Event-ID`, updates one DOM
item per `stage_id`, collapses observable details, and marks the origin as
`dérivé` or `natif`.

## Boundaries

- the display callback has no run-control method;
- callback replay cannot create a second upstream reader;
- a display failure cannot roll back the canonical recorded runtime start;
- the UI states that no private reasoning is shown;
- a visible Role remains a governance responsibility, not an autonomous agent;
- the filesystem-only Ubuntu Workspace Cockpit remains a distinct application;
  its optional V4 sidecar is explicitly configured, transient and read-only;
- the browser proxy never exposes the Hermes or internal sidecar credentials;
- the sidecar cannot create, approve, retry or stop a run.

## Verification

- 78 targeted Python/static-boundary tests passed in the derived Workspace
  Cockpit image based on Hermes v2026.9.11 with ephemeral test dependencies;
- Python compilation passed;
- Node syntax checks passed for the new dialogue reader and modified shell;
- `git diff --check` is required before handoff.
