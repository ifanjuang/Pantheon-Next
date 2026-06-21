# 2026-06-21 CI: exclude reference_reviews from forbidden-phrase guard

Status: CI fix — documented.

main turned red on the "Governance files do not suggest Pantheon executes" CI
step after `docs/governance/reference_reviews/ROW_BOT_4_2_0_REVIEW.md` was merged:
its line 24 ("write-lock and queue safeguards") describes an external product but
trips the `queue` guard. That step has no baseline, so it scanned the whole tree
and failed on every PR and every main push.

Fix: the guard now skips `docs/governance/reference_reviews/`. These are reviews
of third-party tools that legitimately mention queue / scheduler / provider
router; the doctrine guard targets Pantheon's own docs claiming to execute, not
descriptions of external tools. Root-cause fix that unblocks main for everyone.

Verified locally by replicating the exact step logic over the current main tree
with the exclusion: 0 failures (ROW_BOT no longer flagged; nothing else trips).

No schema, runtime or governance-doctrine change. CI guard scope only.
