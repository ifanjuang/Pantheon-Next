(() => {
  "use strict";

  if (typeof window.Swiper !== "function") return;
  const stage = document.getElementById("v2-stage");
  if (!stage) return;

  const MOBILE_QUERY = "(max-width: 620px)";
  const mobileMedia = window.matchMedia(MOBILE_QUERY);
  const nativeReplaceChildren = stage.replaceChildren.bind(stage);
  const nativeAppend = stage.append.bind(stage);
  const nativeAppendChild = stage.appendChild.bind(stage);
  const nativeAddEventListener = stage.addEventListener.bind(stage);
  let activeSwiper = null;
  let navigationLocked = false;
  let latestNodes = [];
  let rendererClearedStage = false;

  stage.addEventListener = function boundedStageListener(type, listener, options) {
    if (mobileMedia.matches && (type === "pointerdown" || type === "pointerup")) return undefined;
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

  function createActionSlide() {
    const slide = document.createElement("div");
    slide.className = "swiper-slide v2-swiper-slide v2-swiper-slide--create";
    slide.dataset.swiperAction = "create";

    const button = document.createElement("button");
    button.type = "button";
    button.className = "v2-swiper-create-card";
    button.setAttribute("aria-label", "Ajouter un nouvel élément");

    const mark = document.createElement("span");
    mark.className = "v2-swiper-create-mark";
    mark.textContent = "+";

    const copy = document.createElement("span");
    copy.className = "v2-swiper-create-copy";
    const title = document.createElement("strong");
    title.textContent = "Nouvel élément";
    const detail = document.createElement("small");
    detail.textContent = "Créer dans la collection courante";
    copy.append(title, detail);
    button.append(mark, copy);

    button.addEventListener("click", () => {
      if (window.PantheonInformationCreate?.open) {
        try {
          window.PantheonInformationCreate.open();
          return;
        } catch (error) {
          window.alert(error.message || String(error));
          return;
        }
      }
      stage.dispatchEvent(new CustomEvent("pantheon:create-requested", { bubbles: true }));
    });

    slide.append(button);
    return slide;
  }

  function moveFromSwiper(swiper) {
    if (navigationLocked) return;
    const active = swiper.slides[swiper.activeIndex];
    if (active?.dataset?.swiperAction === "create") return;

    const currentIndex = Number(swiper.el.dataset.currentSlideIndex || 1);
    if (swiper.activeIndex === currentIndex) return;

    const buttonId = swiper.activeIndex < currentIndex ? "v2-previous" : "v2-next";
    const button = document.getElementById(buttonId);
    navigationLocked = true;
    if (button && !button.disabled) button.click();
    else swiper.slideTo(currentIndex, 180);
    queueMicrotask(() => {
      navigationLocked = false;
    });
  }

  function buildProjection(node) {
    const shell = document.createElement("div");
    shell.className = mobileMedia.matches ? "swiper v2-swiper" : "v2-card-grid";
    shell.setAttribute("aria-roledescription", mobileMedia.matches ? "carrousel" : "grille de cartes");

    const wrapper = document.createElement("div");
    wrapper.className = mobileMedia.matches ? "swiper-wrapper v2-swiper-wrapper" : "v2-card-grid-wrapper";

    const previous = document.getElementById("v2-previous");
    const isFirstCard = !previous || previous.disabled;
    if (isFirstCard) wrapper.append(createActionSlide());
    else wrapper.append(previewSlide(node, "previous"));
    wrapper.append(currentSlide(node), previewSlide(node, "next"));

    shell.append(wrapper);
    return { shell, wrapper };
  }

  function mount(nodes) {
    latestNodes = nodes;
    activeSwiper?.destroy(true, true);
    activeSwiper = null;

    const node = nodes.find(item => item instanceof Node) || null;
    if (!node || node.classList?.contains("v2-empty")) {
      nativeReplaceChildren(...nodes);
      return;
    }

    const { shell } = buildProjection(node);
    nativeReplaceChildren(shell);

    if (!mobileMedia.matches) return;

    const currentSlideIndex = 1;
    shell.dataset.currentSlideIndex = String(currentSlideIndex);
    activeSwiper = new window.Swiper(shell, {
      initialSlide: currentSlideIndex,
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

  stage.replaceChildren = (...nodes) => {
    rendererClearedStage = nodes.length === 0;
    if (rendererClearedStage) {
      activeSwiper?.destroy(true, true);
      activeSwiper = null;
      latestNodes = [];
      nativeReplaceChildren();
      return;
    }
    mount(nodes);
  };

  stage.append = (...nodes) => {
    if (rendererClearedStage) {
      rendererClearedStage = false;
      mount(nodes);
      return;
    }
    nativeAppend(...nodes);
  };

  stage.appendChild = node => {
    if (rendererClearedStage) {
      rendererClearedStage = false;
      mount([node]);
      return node;
    }
    return nativeAppendChild(node);
  };

  mobileMedia.addEventListener?.("change", () => {
    if (latestNodes.length) mount(latestNodes);
  });
  window.addEventListener("pagehide", () => activeSwiper?.destroy(true, true), { once: true });
})();