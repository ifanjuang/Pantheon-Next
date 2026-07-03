# AI log — align templates/configs with upstream OpenWebUI 0.10.2 / Hermes 0.18 / agentskills.io

Date: 2026-07-02.

Actor: Claude Code.

## Intent

After checking upstream docs/git, align the repo's OpenWebUI/Hermes candidate templates
and integration docs with the real, current versions: OpenWebUI `0.10.2` (Event function
+ webhook event system), Hermes Agent (NousResearch) `0.18.0` (OpenAI-compatible API,
`agentskills.io` / `SKILL.md` skills, own memory / automation / sub-agents).

## Change (candidate, non-executable)

- `templates/hermes/skills/quote-variation-review/SKILL.md` and
  `external-commitment-guard/SKILL.md` — the two slice capabilities re-expressed in the
  `agentskills.io` / `SKILL.md` standard Hermes actually loads (YAML frontmatter
  name/description + governed boundary in the body). The bespoke `*_skill_candidate.template.yaml`
  forms are removed; the run manifest and RUNBOOK now reference the SKILL.md paths.
- `templates/hermes/connection/hermes_openai_connection.template.yaml` — records the
  OpenAI-compatible connection (host `:8642/v1`, bearer key, server-to-server,
  `ENABLE_OLLAMA_API=false`) and the `hermes config set` keys; keys live on the operator
  host, never in the repo.
- `templates/openwebui/events/governed_audit_event.template.yaml` — an Event-function
  template consuming OpenWebUI's 28+ typed events read-only as an audit / evidence trail.
- `HERMES_INTEGRATION.md` and `OPENWEBUI_INTEGRATION.md` gain an "Upstream reference"
  section pinning the versions, the transport, the SKILL.md skill form, and the events
  audit feed. Hermes-side memory / automation / sub-agents are named as outside Pantheon
  and gated; the chokepoint is unchanged.

## Boundary

Candidate templates + doctrine reference notes only. Nothing is installed or executed;
no key is stored; the runtime stays external. Governance guard, link, coverage, axis and
retired-vocabulary checks green locally.
