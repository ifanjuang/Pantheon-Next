(() => {
  "use strict";

  const hermesToggle = document.getElementById("v2-hermes-toggle");
  const hermesDock = document.getElementById("v2-hermes-dock");
  const hermesClose = document.getElementById("v2-hermes-close");
  const menuToggle = document.getElementById("v2-menu-toggle");
  const headerMenu = document.getElementById("v2-header-menu");
  const demoButton = document.getElementById("v2-load-demo");

  function setHermesOpen(open) {
    if (!hermesToggle || !hermesDock) return;
    hermesDock.hidden = !open;
    hermesToggle.setAttribute("aria-expanded", String(open));
    document.body.classList.toggle("v2-hermes-open", open);
    if (open) {
      setMenuOpen(false);
      requestAnimationFrame(() => document.getElementById("v2-handoff-question")?.focus());
    } else if (document.activeElement === hermesClose) {
      hermesToggle.focus();
    }
  }

  function setMenuOpen(open) {
    if (!menuToggle || !headerMenu) return;
    headerMenu.hidden = !open;
    menuToggle.setAttribute("aria-expanded", String(open));
    document.body.classList.toggle("v2-header-menu-open", open);
    if (open) {
      setHermesOpen(false);
      requestAnimationFrame(() => document.getElementById("v2-project")?.focus());
    }
  }

  hermesToggle?.addEventListener("click", () => setHermesOpen(Boolean(hermesDock?.hidden)));
  hermesClose?.addEventListener("click", () => setHermesOpen(false));
  menuToggle?.addEventListener("click", () => setMenuOpen(Boolean(headerMenu?.hidden)));

  demoButton?.addEventListener("click", () => {
    const project = document.getElementById("v2-project");
    const token = document.getElementById("v2-token");
    if (project) project.value = "ORANGERIE";
    if (token) token.value = "demo-read-only";
    document.getElementById("v2-load")?.click();
    setMenuOpen(false);
  });

  document.getElementById("v2-load")?.addEventListener("click", () => setMenuOpen(false));

  document.addEventListener("pointerdown", event => {
    if (!headerMenu || headerMenu.hidden || !menuToggle) return;
    if (headerMenu.contains(event.target) || menuToggle.contains(event.target)) return;
    setMenuOpen(false);
  });

  document.addEventListener("keydown", event => {
    if (event.key !== "Escape") return;
    if (hermesDock && !hermesDock.hidden) setHermesOpen(false);
    else if (headerMenu && !headerMenu.hidden) setMenuOpen(false);
  });
})();