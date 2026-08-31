#!/usr/bin/env bash
# One bounded retry for the real-Obsidian e2e qualification labs, with the flake
# recorded rather than hidden.
#
# Why this exists
# ---------------
# Four labs (S2, S3, S4, S5) start a real Obsidian/Electron session under Xvfb.
# All four go through the upstream harness call
# `startObsidianPluginSession` (@vrtmrz/obsidian-test-session), which waits a
# fixed 60 s for the plugin session to become ready.
#
# That wait is exceeded under runner contention even though the scenario itself
# takes far less. Observed on 2026-08-31, same commit, same pins:
#
#     S4  timeout at 60 s under 35 parallel checks  ->  19 s when re-run alone
#     S3  timeout at 60 s under 35 parallel checks  ->  33 s when re-run alone
#
# And it is not new: of the 28 runs of the S3 workflow preceding that date — on
# branches touching no LiveSync pin — 11 failed. Roughly 39 %.
#
# A check that fails a third of the time for reasons unrelated to the change
# under review does not gate anything. It trains reviewers to re-run until
# green, which is worse than no check: it produces the appearance of a
# qualification while selecting for persistence rather than correctness.
#
# What this does, and what it deliberately does not do
# ----------------------------------------------------
# One bounded retry restores the gate's meaning: a real regression still fails
# twice. It is not a skipped, disabled or quarantined test — the scenario runs
# in full and must pass.
#
# The flake is never silent. A first-attempt failure is always written to the
# run summary, so the fragility stays visible and countable instead of being
# absorbed by a green tick.
#
#     bounded retry != skipped test
#     silent retry != honest gate
#     green after retry != green
#
# The real fix is upstream: `startObsidianPluginSession` needs a configurable
# timeout, or these labs need to stop competing for one runner. This script also
# dumps the harness's wait site into the summary on a flake, so that fix can be
# specified from a real observation rather than guessed at.

set -uo pipefail

if [ "$#" -lt 1 ]; then
    echo "usage: $0 <command> [args...]" >&2
    exit 2
fi

SUMMARY="${GITHUB_STEP_SUMMARY:-/dev/null}"
HARNESS="node_modules/@vrtmrz/obsidian-test-session"

"$@"
first_status=$?
if [ "$first_status" -eq 0 ]; then
    exit 0
fi

echo "::warning title=Obsidian e2e first attempt failed::Retrying once. The flake is recorded in the run summary; a real regression fails both attempts."

{
    echo "### Obsidian e2e — first attempt failed (exit ${first_status})"
    echo
    echo "Command: \`$*\`"
    echo
    echo "Retrying once. This is recorded so the flake stays countable."
    echo
    echo '```text'
    echo "bounded retry != skipped test"
    echo "green after retry != green"
    echo '```'
} >> "$SUMMARY"

# Investigative half: report how the upstream harness handles its readiness
# wait, so the durable fix can be specified instead of guessed. Best-effort —
# never fails the step.
{
    echo
    echo "#### Upstream harness readiness wait"
    echo
    if [ -d "$HARNESS" ]; then
        version="$(node -e "process.stdout.write(require('./${HARNESS}/package.json').version)" 2>/dev/null || echo unknown)"
        echo "\`@vrtmrz/obsidian-test-session\` version: \`${version}\`"
        echo
        matches="$(grep -rnE 'waitForFunction|timeout' "$HARNESS/src" "$HARNESS/dist" 2>/dev/null | head -25 || true)"
        if [ -n "$matches" ]; then
            echo "Timeout and wait sites, to establish whether the 60 s wait is configurable:"
            echo
            echo '```text'
            printf '%s\n' "$matches"
            echo '```'
        else
            echo "No \`waitForFunction\` or \`timeout\` reference found in the shipped sources."
        fi
    else
        echo "Harness not found at \`${HARNESS}\` — nothing to report."
    fi
} >> "$SUMMARY" 2>/dev/null || true

"$@"
second_status=$?

if [ "$second_status" -eq 0 ]; then
    {
        echo
        echo "**Second attempt passed.** Recorded as a flake of the shared session-start"
        echo "wait, not as a qualification failure. The pins under test are unaffected."
    } >> "$SUMMARY"
    exit 0
fi

{
    echo
    echo "**Second attempt failed as well** (exit ${second_status}). Two consecutive"
    echo "failures are treated as real: this is a qualification failure, not contention."
} >> "$SUMMARY"
exit "$second_status"
