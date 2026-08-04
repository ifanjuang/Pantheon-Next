(() => {
  "use strict";

  // App glue: opt-in mount of the read-only knowledge-map lens into the live
  // cockpit. It reads the projection snapshot via PantheonMapMount and builds
  // tokens from the loaded tag registry (colour + icon) and a status palette.
  // No fetch, no mutation of governed state — the lens stays read-only.

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
    const toggle = document.getElementById("v2-map-toggle");
    const panel = document.getElementById("v2-map-panel");
    const svg = document.getElementById("v2-map");
    if (!toggle || !panel || !svg || !window.PantheonMapMount) return;

    const opts = { tokens: buildTokens(), layout: "cluster", groupBy: "subject" };
    let mount = null;
    let open = false;

    function ensure() {
      if (!mount) mount = window.PantheonMapMount.mountLive(svg, opts);
      else mount.rebuild();
    }

    function closePanel({ restoreFocus = true } = {}) {
      open = false;
      panel.hidden = true;
      toggle.setAttribute("aria-expanded", "false");
      if (mount) {
        mount.destroy();
        mount = null;
      }
      if (restoreFocus) toggle.focus();
    }

    toggle.addEventListener("click", () => {
      if (open) {
        closePanel({ restoreFocus: false });
        return;
      }
      open = true;
      panel.hidden = false;
      toggle.setAttribute("aria-expanded", "true");
      ensure();
    });

    const close = document.getElementById("v2-map-close");
    if (close) close.addEventListener("click", () => closePanel());

    document.addEventListener("keydown", event => {
      if (open && event.key === "Escape") closePanel();
    });

    panel.querySelectorAll("[data-map-layout]").forEach(button => {
      button.addEventListener("click", () => {
        const layout = button.dataset.mapLayout;
        opts.layout = layout;
        opts.groupBy = (layout === "radial" || layout === "chain") ? "family" : "subject";
        panel.querySelectorAll("[data-map-layout]").forEach(other =>
          other.setAttribute("aria-pressed", String(other === button)));
        if (mount && mount.view) { mount.view.setGroupBy(opts.groupBy); mount.view.setLayout(layout); }
      });
    });

    const support = document.getElementById("v2-map-support-toggle");
    if (support) support.addEventListener("change", () => {
      opts.support = support.checked;
      if (mount && mount.view) mount.view.setSupport(support.checked);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
