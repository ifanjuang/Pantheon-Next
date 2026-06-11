"""Policy decision as data.

Classifies a described request on the GLOSSARY axes: consequence (K0-K4),
required answer verification (V0-V4) and approval ceiling (C0-C5), and
states what the chokepoint requires before the effect may happen. The
server itself performs no effect: anything asking it to act is refused.

Memory first. Evidence when consequential. Status when deciding.
Approval when acting.
"""

from __future__ import annotations

import re

# Effects the policy server must refuse to perform itself (Phase 7 posture).
REFUSED_EFFECTS = {
    "send": "sending anything externally",
    "write": "writing files or external state",
    "delete": "deleting anything",
    "merge": "merging code or content",
    "approve": "approving an output",
    "promote_memory": "promoting memory / writing the Registre Probatoire",
    "install": "installing skills or modules",
    "schedule": "scheduling jobs",
    "route_provider": "routing model providers",
    "execute": "executing a capability or tool",
}

# French and English action words mapped to the refused effects above, so a
# request phrased in the maintainer's working language is refused identically.
_REFUSAL_RE = {
    "send": r"send|envoyer|envoi|transmettre|transmission",
    "write": r"write|écrire|ecrire",
    "delete": r"delete|supprimer",
    "merge": r"merge|fusionner",
    "approve": r"approve|approuver",
    "promote_memory": r"promote|promouvoir|canonize|canoniser",
    "install": r"install|installer",
    "schedule": r"schedule|planifier",
    "route_provider": r"route|router",
    "execute": r"execute|exécuter|executer",
}
_REFUSAL_RE = {
    key: re.compile(r"(?:\b|_)(" + pattern + r")(?:\b|_)", re.IGNORECASE)
    for key, pattern in _REFUSAL_RE.items()
}

_K3_TRIGGERS = re.compile(
    r"\b(cost|budget|price|amount|contract|contractual|compliance|regulat|"
    r"deadline|liabilit|responsib|surface|permit|insurance|visa|client|"
    r"plus.?value|payment|invoice|devis|march[eé]|cctp|dpgf|"
    r"contradict|authorit|autorit|quantit|supersed)\b",
    re.IGNORECASE,
)

_K4_TRIGGERS = re.compile(
    r"\b(non[- ]?conform|claim|réclamation|reclamation|liability|responsibility|"
    r"responsabilité|validate|valider|confirm|confirmer|price reduction|diminution du prix|"
    r"vefa|carrez|notarial|acqu[eé]reur|purchaser)\b",
    re.IGNORECASE,
)

_K_TO_V = {"K0": "V0", "K1": "V1", "K2": "V2", "K3": "V3", "K4": "V4"}

_DOCTRINE_REFS = [
    "docs/governance/GLOSSARY.md",
    "docs/governance/ANSWER_VERIFICATION_GATE.md",
    "docs/governance/APPROVALS.md",
    "docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md",
    "docs/governance/USER_DECISION_GATE.md",
]

_AUTHORITY_NOTE = (
    "Policy decision as data. The runtime executes outside Pantheon under a "
    "Task Contract; the gate decides; the human decides."
)


def _refusals_in(request: dict) -> list[str]:
    asked = request.get("perform") or request.get("actions_requested") or []
    if isinstance(asked, str):
        asked = [asked]
    hits = []
    for action in asked:
        a = str(action).strip().lower().replace(" ", "_")
        for key, label in REFUSED_EFFECTS.items():
            if key in a or _REFUSAL_RE[key].search(str(action)):
                hits.append(label)
    return sorted(set(hits))


def classify_request(request: dict) -> dict:
    """Classify a described request. Input fields (all optional):

    intent (str), external_effect (bool|"unknown"), writes_state (bool),
    memory_promotion_requested (bool), transmission_requested (bool),
    professional_position (bool), financial_or_contractual_effect (bool),
    scope (dict with scope_type/scope_id), perform (list of actions the
    caller asks THIS server to do — these are refused, never done).
    """
    refused = _refusals_in(request)
    if refused:
        return {
            "result": "refused",
            "refused_effects": refused,
            "reason": (
                "the MCP policy server may frame the work; it may not do the "
                "work. Requested effects must run in the execution runtime "
                "under a Task Contract and pass the gate."
            ),
            "doctrine_refs": _DOCTRINE_REFS,
            "authority_note": _AUTHORITY_NOTE,
        }

    intent = str(request.get("intent", ""))
    external = request.get("external_effect", False)
    transmission = bool(request.get("transmission_requested", False))
    memory = bool(request.get("memory_promotion_requested", False))
    writes = bool(request.get("writes_state", False))
    professional_position = bool(request.get("professional_position", False))
    financial_or_contractual = bool(request.get("financial_or_contractual_effect", False))
    # Proposing Registre Probatoire material is evidence-class work (K3+),
    # even though the candidate itself is never promoted here.
    register_material = bool(request.get("register_candidates"))
    scope = request.get("scope") or {}

    if external is True or transmission or memory or professional_position or financial_or_contractual:
        consequence = "K4"
    elif external == "unknown":
        consequence = "K4"  # unknown external effect escalates, never relaxes
    elif _K4_TRIGGERS.search(intent):
        consequence = "K4"
    elif writes or register_material or _K3_TRIGGERS.search(intent):
        consequence = "K3"
    elif intent.strip():
        consequence = "K2"
    else:
        consequence = "K1"

    verification = _K_TO_V[consequence]
    approval = {
        "K4": "C3",
        "K3": "C2",
        "K2": "C1",
        "K1": "C0",
        "K0": "C0",
    }[consequence]
    if transmission or memory or professional_position or financial_or_contractual:
        approval = "C4"
    elif consequence == "K4" and _K4_TRIGGERS.search(intent):
        # A professional-position / financial-claim intent is a C4-class
        # effect even when no explicit flag was set.
        approval = "C4"

    gates: list[str] = []
    if consequence in ("K3", "K4"):
        gates.append("evidence required (Registre Probatoire citation for assertions)")
    if consequence == "K4":
        gates.append("User Decision Gate before any external effect or Registre write")
    if not scope:
        gates.append("scope missing: declare scope_type/scope_id before work starts")

    return {
        "result": "classified",
        "consequence_level": consequence,
        "required_verification": verification,
        "required_approval_ceiling": approval,
        "task_contract_required": consequence in ("K2", "K3", "K4"),
        "evidence_required": consequence in ("K3", "K4"),
        "blocked_until_gate": consequence == "K4",
        "required_gates": gates,
        "allowed_output": "candidate only (Result Candidate + Evidence Pack Candidate)",
        "scope_seen": scope or None,
        "doctrine_refs": _DOCTRINE_REFS,
        "authority_note": _AUTHORITY_NOTE,
    }


def check_external_action(description: str) -> dict:
    """An external action is blocked by default; the report states what
    legitimizing it would require. The server never performs it."""
    return {
        "action": description,
        "status": "blocked_by_default",
        "requires": [
            "Task Contract naming the action and its scope",
            "approval at C3 or above (C4 for transmission or Registre writes)",
            "Evidence Pack Candidate prepared for review",
            "User Decision Gate: the human decides",
        ],
        "doctrine_refs": _DOCTRINE_REFS,
        "authority_note": _AUTHORITY_NOTE,
    }
