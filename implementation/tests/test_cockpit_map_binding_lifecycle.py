"""Lifecycle guards for the live Cockpit map binding."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BINDING = ROOT / "mvp_vertical" / "cockpit" / "map_binding.js"


def test_closing_live_map_destroys_subscription_and_allows_clean_remount() -> None:
    source = BINDING.read_text(encoding="utf-8")

    assert "function closePanel" in source
    assert "mount.destroy();" in source
    assert "mount = null;" in source
    assert "if (!mount) mount = window.PantheonMapMount.mountLive" in source


def test_live_map_supports_keyboard_close_and_restores_toggle_focus() -> None:
    source = BINDING.read_text(encoding="utf-8")

    assert 'event.key === "Escape"' in source
    assert "toggle.focus();" in source
    assert 'toggle.setAttribute("aria-expanded", "false")' in source
