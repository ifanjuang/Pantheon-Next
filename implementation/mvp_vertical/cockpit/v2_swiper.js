(() => {
  "use strict";

  if (typeof window.Swiper !== "function") return;
  const stage = document.getElementById("v2-stage");
  if (!stage) return;

  const nativeReplaceChildren = stage.replaceChildren.bind(stage);
  const nativeAddEventListener = stage.addEventListener.bind(stage);
  let activeSwiper = null;
  let navigationLocked = false;

  stage.addEventListener = function boundedStageListener(type, listener, options) {
    if (type === "pointerdown" || type === "pointerup") return undefined;
    return nativeAddEventListener(type, listener, options);
  };

  function inertPreview(node) {
    const clone = node.cloneNode(true);
    clone.removeAttribute?.("id");
    clone.querySelectorAll?.("[id]").forEach(item => item.removeAttribute("id"));
    clone.querySelectorAll?.("button, input, select, textarea, a, [tabindex]").forEach(item => {
      item.setAttribute("tabindex", "-1");
      if ("disabled" in item) item.disabled = true;
    });
    return clone;
  }

  function previewSlide(node, direction) {
    const slide = document.createElement("div");
    slide.className = `swiper-slide v2-swiper-slide v2-swiper-slide--preview v2-swiper-slide--${direction}`;
    slide.setAttribute("aria-hidden", "true");
    slide.inert = true;
    if (node) slide.append(inertPreview(node));
    return slide;
  }

  function currentSlide(node) {
    const slide = document.createElement("div");
    slide.className = "swiper-slide v2-swiper-slide v2-swiper-slide--current";
    slide.append(node);
    return slide;
  }

  function moveFromSwiper(swiper) {
    if (navigationLocked || swiper.activeIndex === 1) return;
    const buttonId = swiper.activeIndex < 1 ? "v2-previous" : "v2-next";
    const button = document.getElementById(buttonId);
    navigationLocked = true;
    if (button && !button.disabled) button.click();
    else swiper.slideTo(1, 180);
    queueMicrotask(() => {
      navigationLocked = false;
    });
  }

  function mount(nodes) {
    activeSwiper?.destroy(true, true);
    activeSwiper = null;

    const node = nodes.find(item => item instanceof Node) || null;
    if (!node || node.classList?.contains("v2-empty")) {
      nativeReplaceChildren(...nodes);
      return;
    }

    const shell = document.createElement("div");
    shell.className = "swiper v2-swiper";
    shell.setAttribute("aria-roledescription", "carrousel");

    const wrapper = document.createElement("div");
    wrapper.className = "swiper-wrapper v2-swiper-wrapper";
    wrapper.append(previewSlide(node, "previous"), currentSlide(node), previewSlide(node, "next"));
    shell.append(wrapper);
    nativeReplaceChildren(shell);

    activeSwiper = new window.Swiper(shell, {
      initialSlide: 1,
      speed: 360,
      threshold: 12,
      resistanceRatio: 0.72,
      grabCursor: true,
      watchOverflow: false,
      allowTouchMove: true,
      keyboard: { enabled: false },
      a11y: {
        enabled: true,
        containerMessage: "Navigation horizontale entre les cartes sœurs",
        slideLabelMessage: "Carte {{index}} sur {{slidesLength}}",
      },
      on: {
        slideChangeTransitionEnd: moveFromSwiper,
      },
    });
  }

  stage.replaceChildren = (...nodes) => mount(nodes);
  window.addEventListener("pagehide", () => activeSwiper?.destroy(true, true), { once: true });
})();
