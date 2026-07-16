# Hermes bounded night-operation controls

Date: 2026-07-16

Status: validation-only trace — external Hermes dashboard integration.

## Change

The Pantheon Modules `Night ops` cards now expose three distinct native Hermes
control paths for one existing, unambiguous Cron job:

```text
pause / resume
retime while paused
run now while enabled
```

Every mutation has an immediate human confirmation. The confirmation names the
operation, Hermes profile, observed or proposed timing, finite-run posture and
material effect where applicable.

The plugin remains unable to create or delete jobs. It never changes the job's
prompt/script, workdir, profile, delivery, source scope, output scope, command,
resource budget or finite repeat limit.

## Fail-closed rules

- Missing or ambiguous matching jobs expose no mutation.
- A unique unbounded job may be paused but cannot be resumed, retimed or run.
- An exhausted finite trial cannot be resumed, retimed or run.
- Timing may change only while a unique finite job is paused.
- `Run now` requires a unique finite job that is already enabled.
- Saving timing does not enable or run the job.
- Enabling does not launch the job immediately.
- Runtime success does not approve evidence, resolve contradictions or promote
  memory.

## Runtime boundary

```text
OpenWebUI / dashboard exposes
Hermes native Cron executes and owns state
Pantheon supplies the governance contract
the human confirms every operational mutation
```

The public GitHub demonstration continues to run the exact same renderer, but
its synthetic SDK keeps every mutation disabled.

## Verification basis

The control signatures were checked against Hermes Agent commit
`8b209e0dd7b8e308d5b923fa80f7a72f71042636`:

```text
pauseCronJob(id, profile)
resumeCronJob(id, profile)
updateCronJob(id, updates, profile)
triggerCronJob(id, profile)
```

No Pantheon scheduler, queue, worker, memory engine or automatic approval path
was added.
