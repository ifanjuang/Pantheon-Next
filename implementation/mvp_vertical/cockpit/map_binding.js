(() => {
  "use strict";

  // App glue for the read-only knowledge-map lens. The canonical renderer owns
  // the Pantheon verso host; this binding only mounts the existing graph view
  // into that host. It never fetches or mutates governed state.

  function buildTokens() {
    const icons = window.PantheonTagIcons;
    const NAMED = (window.PantheonMapTokens && window.PantheonMapTokens.NAMED) || {};
    const STATUS_COLOR = {
      draft: "slate", in_progress: "amber", running: "cyan", review: "amber",
      needs_review: "amber", pending_review: "amber", acted: "green", ready: "green",
      reviewed: "green", active: "green", done: "slate", waiting: "amber",
      conflict: "red", failed: "red", superseded: "slate", generated_unreviewed: "amber",
      neutral: "slate",
    };
    const hex = name => NAMED[name] || "#8b98a6";
    const present = subj => (subj && icons && icons.tagPresentation ? icons.tagPresentation(subj, "subject") : null);
    return {
      subjectColor: subj => { const p = present(subj); return p && p.color ? hex(p.color) : "#66758c"; },
      subjectIconKey: subj => { const p = present(subj); return p ? p.icon_key : null; },
      statusColor: st => hex(STATUS_COLOR[st] || "slate"),
      originStroke: origin =>
        origin === "hermes" ? { stroke: "#9aa4b4", dash: "4 3" }
        : origin === "knowledge" ? { stroke: "#6f7a8c", dash: "" }
        : { stroke: "#8492a8", dash: "" },
      radius: (m, b = 9) => (m > 1 ? Math.min(20, b + Math.sqrt(m) * 1.3) : b),
    };
  }

  function init() {
    const stage = document.getElementById("v2-stage");
    if (!stage || !window.PantheonMapMount || typeof MutationObserver !== "function") return;

    const mounts = new Map();

    function destroyLens(lens) {
      const state = mounts.get(lens);
      if (!state) return;
      state.mount.destroy();
      mounts.delete(lens);
    }

    function mountLens(lens) {
      if (mounts.has(lens)) return;
      const svg = lens.querySelector("[data-pantheon-map]");
      if (!svg) return;

      const opts = { tokens: buildTokens(), layout: "cluster", groupBy: "subject" };
      const mount = window.PantheonMapMount.mountLive(svg, opts);
      mounts.set(lens, { mount, opts });

      lens.querySelectorAll("[data-map-layout]").forEach(button => {
        button.addEventListener("click", () => {
          const layout = button.dataset.mapLayout;
          opts.layout = layout;
          opts.groupBy = (layout === "radial" || layout === "chain") ? "family" : "subject";
          lens.querySelectorAll("[data-map-layout]").forEach(other =>
            other.setAttribute("aria-pressed", String(other === button)));
          if (mount.view) {
            mount.view.setGroupBy(opts.groupBy);
            mount.view.setLayout(layout);
          }
        });
      });

      const support = lens.querySelector("[data-map-support-toggle]");
      support?.addEventListener("change", () => {
        opts.support = support.checked;
        if (mount.view) mount.view.setSupport(support.checked);
      });
    }

    function sync() {
      const live = new Set(stage.querySelectorAll('.card[data-family="pantheon"] [data-pantheon-map-lens]'));
      for (const lens of mounts.keys()) {
        if (!live.has(lens)) destroyLens(lens);
      }
      for (const lens of live) mountLens(lens);
    }

    const observer = new MutationObserver(sync);
    observer.observe(stage, { childList: true, subtree: true });
    sync();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
