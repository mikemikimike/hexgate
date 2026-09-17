"""The one interface this slice still consumes from a PR landing beside it.

``AgentClassification`` is specified in ``Specs/ai_act_evidence_report.md`` and
owned by PR 1 (agent AI Act classification), which has not merged. It is not
reproduced here — this module only resolves it, so the slice imports and tests
cleanly either way and picks the table up unchanged once it lands.

The degraded reading is the truthful one, not a placeholder: no
``AgentClassification`` table means no operator has recorded an entry, so every
agent reads as **incomplete** — which is exactly how PR 1 defines an agent with
no row.

The matrix half of this shim is gone: ``hexgate.security.matrix`` is on main
(#238), and the SDK is an install-time dependency of the API rather than an
optional one, so ``features.ai_act.service`` imports ``authorisation_matrix``
directly.
"""

from __future__ import annotations


def classification_model() -> type | None:
    """PR 1's ``AgentClassification`` table, or None before it lands."""
    try:
        from hexgate_api.models import AgentClassification
    except ImportError:
        return None
    return AgentClassification
