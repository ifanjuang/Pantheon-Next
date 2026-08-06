"""Every relative module specifier we ship must resolve to a real file.

`node --check` parses a file; it never resolves what that file imports. A module
whose specifier points at a missing path parses cleanly and fails only in the
browser, at load time, as a generic boot failure. That is exactly how the demo
entry point stayed broken while the suite stayed green.

This check closes the class rather than one instance: it walks every browser
script we own, extracts every relative specifier — static `import`/`export ...
from`, dynamic `import(...)` and `new Worker(...)` — and asserts the target
exists. It is pure filesystem work, so it needs no Node and never skips.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCAN_ROOTS = (
    ROOT / "mvp_vertical" / "cockpit",
    ROOT / "mvp_vertical" / "mobile_editor",
)

# from "./x.js" | import "./x.js" | import("./x.js") | export ... from "./x.js"
SPECIFIER = re.compile(
    r"""(?:\bfrom|\bimport|\bnew\s+Worker)\s*\(?\s*["'](?P<spec>\.[^"']*)["']""",
)


def _sources() -> list[Path]:
    found = [
        path
        for root in SCAN_ROOTS
        if root.exists()
        for path in root.rglob("*.js")
        if "vendor" not in path.relative_to(ROOT).parts
    ]
    assert found, "no browser JavaScript discovered"
    return sorted(found)


def _references(path: Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8")
    out: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("//"):
            continue
        for match in SPECIFIER.finditer(line):
            out.append((number, match.group("spec")))
    return out


@pytest.mark.parametrize("source", _sources(), ids=lambda p: str(p.relative_to(ROOT)))
def test_relative_module_specifiers_resolve(source: Path) -> None:
    unresolved = [
        f"{source.relative_to(ROOT)}:{number} -> {spec} "
        f"(resolves to {(source.parent / spec).resolve().relative_to(ROOT)})"
        for number, spec in _references(source)
        if not (source.parent / spec).is_file()
    ]
    assert not unresolved, "unresolvable relative import(s):\n" + "\n".join(unresolved)


def test_the_check_would_catch_a_broken_specifier(tmp_path: Path) -> None:
    """A guard is only worth its false-negative rate; prove this one bites."""
    broken = tmp_path / "broken.js"
    broken.write_text('import { thing } from "./missing/module.js";\n', encoding="utf-8")

    references = _references(broken)
    assert references == [(1, "./missing/module.js")]
    assert not (broken.parent / references[0][1]).is_file()


def test_every_shipped_script_is_covered() -> None:
    """The scan must follow the tree, not a list that silently stops matching."""
    discovered = {path.relative_to(ROOT) for path in _sources()}
    on_disk = {
        path.relative_to(ROOT)
        for root in SCAN_ROOTS
        if root.exists()
        for path in root.rglob("*.js")
        if "vendor" not in path.relative_to(ROOT).parts
    }
    assert discovered == on_disk
