(() => {
  "use strict";

  const stage = document.getElementById("v2-stage");
  if (!stage) return;

  const state = {
    materials: [],
    observer: null,
  };

  function hash(value) {
    let result = 2166136261;
    const text = String(value || "card");
    for (let index = 0; index < text.length; index += 1) {
      result ^= text.charCodeAt(index);
      result = Math.imul(result, 16777619);
    }
    return result >>> 0;
  }

  function cardKey(card, index) {
    return card.dataset.entityId
      || card.getAttribute("data-card-id")
      || card.querySelector("[data-entity-id]")?.dataset.entityId
      || card.querySelector("h1,h2,h3,.v2-card-title")?.textContent?.trim()
      || `projection-${index}`;
  }

  function setMaterial(card, index) {
    if (!state.materials.length) return;
    const key = cardKey(card, index);
    const material = state.materials[hash(key) % state.materials.length];
    card.dataset.v3Material = material.id;
    material.stops.forEach((stop, stopIndex) => {
      card.style.setProperty(`--v3-stop-${stopIndex + 1}`, stop);
    });
  }

  function isInteractive(target) {
    return Boolean(target.closest("button,a,input,select,textarea,label,[contenteditable='true'],[role='button']"));
  }

  function bindFlip(card) {
    if (card.dataset.v3FlipBound === "true") return;
    card.dataset.v3FlipBound = "true";
    card.tabIndex = card.tabIndex >= 0 ? card.tabIndex : 0;
    card.setAttribute("aria-roledescription", "carte recto verso");

    const toggle = () => {
      const flipped = card.dataset.flipped === "true";
      card.dataset.flipped = String(!flipped);
      card.setAttribute("aria-label", flipped ? "Carte, recto visible" : "Carte, verso visible");
    };

    card.addEventListener("click", event => {
      if (isInteractive(event.target)) return;
      toggle();
    });

    card.addEventListener("keydown", event => {
      if (event.key !== "Enter" && event.key !== " ") return;
      if (isInteractive(event.target) && event.target !== card) return;
      event.preventDefault();
      toggle();
    });
  }

  function decorate() {
    const cards = [...stage.querySelectorAll(".v2-card")];
    cards.forEach((card, index) => {
      card.dataset.cockpitV3 = "living-card";
      setMaterial(card, index);
      bindFlip(card);
    });
    document.documentElement.dataset.cockpitVisual = cards.length ? "v3" : "v2";
  }

  async function loadMaterials() {
    const response = await fetch("v3/materials.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`Material registry unavailable: ${response.status}`);
    const registry = await response.json();
    if (!Array.isArray(registry.materials) || !registry.materials.length) {
      throw new Error("Material registry is empty");
    }
    state.materials = registry.materials.filter(item => item?.id && Array.isArray(item.stops) && item.stops.length >= 5);
  }

  async function start() {
    try {
      await loadMaterials();
    } catch (error) {
      console.warn("Cockpit V3 materials disabled", error);
      return;
    }

    decorate();
    state.observer = new MutationObserver(decorate);
    state.observer.observe(stage, { childList: true, subtree: true });
    window.addEventListener("pagehide", () => state.observer?.disconnect(), { once: true });
  }

  window.PantheonCockpitV3 = Object.freeze({ start, decorate });
  start();
})();
