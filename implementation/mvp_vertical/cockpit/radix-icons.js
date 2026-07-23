(() => {
  const supportedIcons = new Set([
    "document",
    "knowledge",
    "work",
    "questionnaire",
    "source",
    "review",
    "scope",
    "memory",
    "history",
    "decision",
    "hermes",
    "comment",
    "project",
    "evidence",
    "gate",
    "close",
  ]);

  window.icon = function icon(name) {
    const glyph = document.createElement("span");
    glyph.className = "radix-icon";
    glyph.dataset.icon = supportedIcons.has(name) ? name : "document";
    glyph.setAttribute("aria-hidden", "true");
    return glyph;
  };

  // app.js performs an initial render before this compatibility layer loads.
  // Re-render immediately so every visible Cockpit icon uses the vendored Radix binding.
  if (typeof window.render === "function") window.render();
})();
