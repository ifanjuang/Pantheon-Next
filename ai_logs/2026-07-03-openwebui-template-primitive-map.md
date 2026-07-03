# AI log — map the OpenWebUI template classes to real primitives

Date: 2026-07-03.

Actor: Claude Code.

## Intent

Close the last upstream mismatch found while checking OpenWebUI 0.10.2: the
`templates/openwebui/` classes were listed without saying which are native OpenWebUI
primitives and which are Pantheon cockpit concepts realized through one. In particular
`forms/` and `model_profiles/` are not native OpenWebUI primitives.

## Change

- `templates/openwebui/README.md`: replace "First template classes" with a mapping
  table — `actions/` -> Action function, `filters/` -> Filter function, `events/` ->
  Event function (native, 0.10.x), `model_profiles/` -> a model connection/config
  (not native; realized via an OpenAI-compatible connection), `forms/` -> an Action or
  a Tool (not native). Note the Hermes connection (OpenAI-compatible) and the
  `agentskills.io` SKILL.md skill form. Update the intro primitive list to include
  Event functions.

## Boundary

Documentation clarification only. No new template, no runtime, nothing installable.
Candidate scaffold unchanged in substance; it is now honest about the upstream
primitive each class maps to.
