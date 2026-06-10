# AI log — CHANGELOG rotation (archive older entries)

Date: 2026-06-10.

## Intent

The active `CHANGELOG.md` had grown to 775 lines / 32 versions (0.1.12 -> 0.1.49),
too long to edit reliably through the connector — appending a new release entry
was failing. Rotate it: keep the recent versions active, move the older ones to
an archive file, lose no history.

## Change

- `CHANGELOG.md`: keeps the header and the recent versions (0.1.42 -> 0.1.50,
  where 0.1.50 records this rotation), plus a footer pointing to the archive.
  Now ~152 lines, editable again.
- `CHANGELOG_ARCHIVE.md` (new): the rotated-out versions 0.1.12 -> 0.1.41, with a
  short header.

## Boundary

Documentation housekeeping only. No doctrine, schema, test, runtime or
protected-path change. The governance CI only checks that `CHANGELOG.md` exists
(it still does), not its structure, so the split breaks nothing. No changelog
content was lost; entries were moved, not deleted.

Repo state: documented; the active changelog is short enough to maintain again.
