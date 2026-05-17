# Pantheon RPG References

Status: reference workspace — not governance doctrine.

This directory may store non-confidential visual references, notes and external inspiration summaries for the Pantheon RPG visual system.

Do not store copyrighted image files unless usage rights are clear.

Prefer written reference notes over copied assets.

## Asset register

The current visual asset inventory and README integration status are tracked in:

```text
../ASSET_REGISTER.md
```

Use that register before adding, replacing, renaming or removing JPG assets.

## Rename plan

The safe binary rename pass is documented in:

```text
../RENAME_ASSETS.md
```

Use that file to rename raw `IMG_*.jpeg` exports into stable semantic board names with `git mv`.

Do not rewrite JPEG binaries through a text-only API.

## Allowed content

- visual reference notes;
- palette notes;
- architectural vocabulary notes;
- pixel art style notes;
- Greek antique urban composition notes;
- non-confidential public-domain or self-produced references;
- reviewed self-produced RPG board exports intended for README or documentation use.

## Forbidden content

- private project images;
- client documents;
- confidential plans;
- copyrighted images copied without rights;
- generated outputs that are not reviewed;
- raw camera or ChatGPT export filenames in README links after the planned rename pass;
- any reference that introduces runtime or backend visual metaphors.

## Naming rule

Prefer stable board names:

```text
<board_slug>_<version>_<lang>.<ext>
```

Examples:

```text
player_01_fr.jpg
worldmap_01_fr.jpg
port_01_fr.jpg
citadel_01_fr.jpg
evidence_01_fr.jpg
livrables_01_fr.jpg
ui_hermes_pantheon_01_fr.jpg
before_after_01_fr.jpg
```

If an existing README-linked file does not yet use the language suffix, keep the link stable until a deliberate binary rename pass is completed.

## Suggested notes

```text
reference-greek-antique-city.md
reference-isometric-pixel-art.md
reference-rpg-map-composition.md
reference-memory-city-metaphor.md
```

## Current caution

The visual system is explanatory.

A board in this directory must not be interpreted as implemented runtime capability, OpenWebUI plugin, Hermes tool, automatic memory promotion or Evidence Pack automation.
