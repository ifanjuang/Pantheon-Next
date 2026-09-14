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

When an observed Pantheon `classify_request` result contains
`handling.metathoughts`, surface each returned question unchanged as governed
attention. This is presentation of an observed policy result, not a new Role
consultation or Rite activation.

Use this compact public shape:

```text
⚙ Hermes · Attention gouvernée
<question exactly as returned by handling.metathoughts[].question>
Limite: attention_only — question ≠ symptôme confirmé ≠ Rite activé
```

For the currently implemented `tests_pass_completion` signal, the returned
question is:

```text
What would passing these tests still not establish?
```

Do not answer the metathought as though Pantheon had already supplied a verdict.
Do not convert `related_rite` into an activated Rite, do not invent a Role handoff,
and do not call `delegate_task` solely because a metathought is present. If later
observable work independently confirms the symptom and the existing governance
path authorizes a Rite, report that later transition separately.

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
