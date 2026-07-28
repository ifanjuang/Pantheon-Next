(() => {
  "use strict";

  async function ensureSwiper() {
    if (typeof window.Swiper === "function") return true;

    const candidates = [
      "https://cdn.jsdelivr.net/npm/swiper@14.0.6/swiper-bundle.min.mjs",
      "https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.mjs",
    ];

    for (const src of candidates) {
      try {
        const module = await import(src);
        const Swiper = module.default || module.Swiper;
        if (typeof Swiper === "function") {
          window.Swiper = Swiper;
          document.documentElement.dataset.swiperReady = "true";
          return true;
        }
      } catch (error) {
        console.warn(`Swiper indisponible depuis ${src}`, error);
      }
    }

    document.documentElement.dataset.swiperReady = "false";
    return false;
  }

  async function start() {
    const params = new URLSearchParams(window.location.search);
    const isDemo = params.get("mode") === "demo";

    window.PANTHEON_COCKPIT_DEMO = isDemo;
    document.documentElement.dataset.cockpitMode = isDemo ? "demo" : "live";

    function loadScript(src) {
      return new Promise((resolve, reject) => {
        const script = document.createElement("script");
        script.src = src;
        script.onload = resolve;
        script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
        document.body.append(script);
      });
    }

    if (isDemo) await import("./demo_bootstrap.js");

    const swiperReady = await ensureSwiper();
    const scripts = [
      ...(swiperReady ? ["v2_swiper.js"] : []),
      "v2_shell_controls.js",
      "structured_interface.js",
      "context_resolver.js",
      "agency_data_binding.js",
      "spatial_navigation.js",
      "v2_app_schema.js",
      "v2_interaction_policy.js",
      "project_claim_view_adapter.js",
      "information_view_adapter.js",
      "v2_context.js",
      "v2_handoff.js",
      "v2_hermes_send.js",
      "v2_actions.js",
      "v2_candidate_actions.js",
      "schema_editor.js",
      "contacts_editor.js",
      "information_create.js",
    ];

    for (const src of scripts) await loadScript(src);

    if (isDemo && window.PantheonDemoBootstrap?.start) {
      await window.PantheonDemoBootstrap.start();
    }

    const network = document.getElementById("v2-network");
    if (network && window.matchMedia("(max-width: 620px)").matches && !swiperReady) {
      network.textContent = "Swiper indisponible";
    }
  }

  start().catch(error => {
    console.error(error);
    const network = document.getElementById("v2-network");
    if (network) network.textContent = "chargement impossible";
  });
})();