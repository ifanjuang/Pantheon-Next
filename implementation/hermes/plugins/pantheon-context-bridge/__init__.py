"""Pantheon context bridge — Hermes plugin registration.

This plugin exposes read-only context tools only. Installation or enablement of the
plugin is an external Hermes capability action and is not performed by this repo.
Every registered model-bound handler applies Context Admission before its result
leaves the Pantheon plugin.
"""

from . import context_admission, schemas, tools


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
