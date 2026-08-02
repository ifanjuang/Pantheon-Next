(() => {
  "use strict";

  async function start() {
    const params = new URLSearchParams(window.location.search);
    const isDemo = params.get("mode") === "demo";

    window.PANTHEON_COCKPIT_DEMO = isDemo;
    document.documentElement.dataset.cockpitMode = isDemo ? "demo" : "live";

    if (isDemo) await import("./demo_bootstrap.js");

    const tagIcons = await import("./rendering/tag_icons.js");
    await tagIcons.loadTagIconRegistries();

    const { ensureSwiper } = await import("./navigation/swiper_loader.js");
    const swiperReady = await ensureSwiper();
    if (swiperReady) await import("./live_collection_adapter.js");

    const { loadClassicScriptsInOrder } = await import("./boot/classic_script_loader.js");
    const scripts = [
      "shell_controls.js",
      "structured_interface.js",
      "context_resolver.js",
      "agency_data_binding.js",
      "spatial_navigation.js",
      "data/cockpit_data_loader.js",
      "projection/cockpit_projection.js",
      "interactions/interaction_policy.js",
      "project_claim_view_adapter.js",
      "information_view_adapter.js",
      "context/context_selection.js",
      "handoff/handoff_lifecycle.js",
      "handoff/handoff_send.js",
      "actions/card_actions.js",
      "actions/change_candidate_actions.js",
      "schema_editor.js",
      "contacts_editor.js",
      "information_create.js",
      "interactions/card_interactions.js",
    ];

    await loadClassicScriptsInOrder(scripts);

    if (isDemo && window.PantheonDemoBootstrap?.start) {
      await window.PantheonDemoBootstrap.start();
    }

    const network = document.getElementById("v2-network");
    if (network && window.matchMedia("(max-width: 620px)").matches && !swiperReady) {
      network.textContent = "navigation tactile simplifiée";
    }
  }

  start().catch(async error => {
    try {
      const { projectBootFailure } = await import("./shell/boot_failure.js");
      projectBootFailure(error);
    } catch (projectionError) {
      console.error(error, projectionError);
      document.documentElement.dataset.cockpitLoad = "failed";
    }
  });
})();
