"""Pantheon context bridge — Hermes plugin registration.

The plugin exposes bounded Pantheon context reads plus guarded read/search paths
for content with external provenance. Installation or enablement remains an
external Hermes capability action and is not performed by this repository.

Executable security invariants live in plugin handlers/hooks. The bundled skill
is guidance only and grants no authority.
"""

from pathlib import Path

from . import context_admission, external_content, schemas, tools

_PLUGIN_DIR = Path(__file__).resolve().parent


def _protected_handler(tool_name, handler):
    def protected(args, **kwargs):
        result = handler(args, **kwargs)
        protected_result = context_admission.protect_model_bound_result(
            tool_name=tool_name,
            result=result,
        )
        if protected_result is None:  # pragma: no cover - fixed reviewed tool names only
            raise RuntimeError("Pantheon context handler lost Context Admission coverage")
        return protected_result

    return protected


def register(ctx):
    ctx.register_tool(
        name="pantheon_context_manifest",
        toolset="pantheon_context",
        schema=schemas.PANTHEON_CONTEXT_MANIFEST,
        handler=_protected_handler(
            "pantheon_context_manifest",
            tools.pantheon_context_manifest,
        ),
        description="Read the exact admitted Pantheon context manifest for this Hermes session.",
    )
    ctx.register_tool(
        name="pantheon_context_entity",
        toolset="pantheon_context",
        schema=schemas.PANTHEON_CONTEXT_ENTITY,
        handler=_protected_handler(
            "pantheon_context_entity",
            tools.pantheon_context_entity,
        ),
        description="Read one exact entity already admitted for this Hermes session.",
    )
    ctx.register_tool(
        name="pantheon_untrusted_read",
        toolset="pantheon_context",
        schema=schemas.PANTHEON_UNTRUSTED_READ,
        handler=external_content.make_guarded_read_handler(ctx),
        description=(
            "Read an uploaded, downloaded, cloned, emailed, or otherwise external file "
            "through data-only Context Admission."
        ),
    )
    ctx.register_tool(
        name="pantheon_untrusted_search",
        toolset="pantheon_context",
        schema=schemas.PANTHEON_UNTRUSTED_SEARCH,
        handler=external_content.make_guarded_search_handler(ctx),
        description=(
            "Search externally sourced files through data-only Context Admission."
        ),
    )

    ctx.register_hook("pre_gateway_dispatch", external_content.pre_gateway_dispatch)
    ctx.register_hook("pre_tool_call", external_content.pre_tool_call)

    ctx.register_skill(
        "untrusted-content-reading",
        _PLUGIN_DIR / "skills" / "untrusted-content-reading" / "SKILL.md",
        "Use guarded read/search paths for uploaded or otherwise external content.",
    )
