"""Pantheon context bridge — Hermes plugin registration.

This plugin exposes read-only context tools only. Installation or enablement of the
plugin is an external Hermes capability action and is not performed by this repo.
Model-bound results pass through the Context Admission transform before they enter
the Hermes conversation.
"""

from . import context_admission, schemas, tools


def register(ctx):
    ctx.register_tool(
        name="pantheon_context_manifest",
        toolset="pantheon_context",
        schema=schemas.PANTHEON_CONTEXT_MANIFEST,
        handler=tools.pantheon_context_manifest,
        description="Read the exact admitted Pantheon context manifest for this Hermes session.",
    )
    ctx.register_tool(
        name="pantheon_context_entity",
        toolset="pantheon_context",
        schema=schemas.PANTHEON_CONTEXT_ENTITY,
        handler=tools.pantheon_context_entity,
        description="Read one exact entity already admitted for this Hermes session.",
    )
    ctx.register_hook(
        "transform_tool_result",
        context_admission.protect_model_bound_result,
    )
