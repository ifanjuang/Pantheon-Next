## Pantheon observable activity projection

For every non-trivial Pantheon-governed request, use the
`pantheon-activity-projection` skill. This is a narrow exception to the general
preference against narrating process: publish only decision-relevant observable
milestones, never private reasoning or routine tool chatter.

When interim assistant messages are supported, publish the plan before the first
material tool call and later milestones only when a source, result, risk,
blocker, artifact, status or responsibility changes. Otherwise preserve the same
ordered role labels in the streamed final response and do not imply that separate
events were emitted.

An explicit request for the skill must visibly include at least:

```text
🦉 Athena · Plan / structuration
...

<one materially relevant Role or ⚙ Hermes milestone>
...

⚡ Zeus · Statut
...
```

Do not display every canonical Role. Do not invent consultation, delegation,
sources, tools or approval. Hermes is a runtime, not a Pantheon Role. A visible
role label identifies a governance responsibility, not an autonomous agent.
