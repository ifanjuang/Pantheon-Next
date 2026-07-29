document.documentElement.dataset.cockpitVersion = "3";
document.documentElement.classList.add("cockpit-v3");

const params = new URLSearchParams(window.location.search);
if (params.get("mode") === "demo") {
  await import("./v3/demo_collection_app.js");
  await import("./v2_shell_controls.js");
} else {
  await import("./v2_bootstrap.js");
}
