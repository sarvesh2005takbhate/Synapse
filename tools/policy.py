# tools/policy.py

# Simple confidence thresholds
CONF_HIGH = 0.80
CONF_LOW  = 0.50

def estimate_confidence(tool_name: str, args: dict, obs: dict) -> float:
    """Heuristic confidence for each tool's output (0.0–1.0)."""
    # Match tools you already have; default = medium confidence
    if tool_name == "analyze_evidence":
        # Use model-provided confidence if present
        return float(obs.get("confidence", 0.5))
    if tool_name == "get_merchant_status":
        ok = obs.get("open_status") in ("open", "closed")
        prep = obs.get("prep_time_min", None)
        return 0.85 if ok and isinstance(prep, (int, float)) else 0.45
    if tool_name == "check_traffic":
        # Simulated tool is quite reliable
        return 0.8
    if tool_name == "contact_recipient_via_chat":
        # If no response, confidence in proceeding is low
        return 0.35 if obs.get("recipient_response") == "no_response" else 0.7
    if tool_name == "find_nearby_locker":
        return 0.75 if obs.get("available") else 0.4
    if tool_name in {"issue_instant_refund", "exonerate_driver", "notify_customer",
                     "notify_passenger_and_driver"}:
        # Administrative actions are low-risk
        return 0.9
    # Default
    return 0.6

def policy_advice(tool_name: str, args: dict, obs: dict, confidence: float) -> dict:
    """
    Return policy guidance for the agent. If escalate=True, the agent should either:
    - gather more info, or
    - take conservative action, or
    - end with NEED HUMAN REVIEW.
    """
    advice = ""
    escalate = False
    suggested_action = None
    suggested_args = None

    # Generic low-confidence guardrail
    if confidence < CONF_LOW:
        escalate = True
        advice = "Confidence is low; prefer conservative actions or gather more info."

    # Special-cases that benefit from safe fallbacks
    if tool_name == "contact_recipient_via_chat" and obs.get("recipient_response") == "no_response":
        escalate = True
        advice = ("No response from recipient. Consider safe drop-off with permission "
                  "or use a nearby locker; otherwise escalate to human.")
        suggested_action = "find_nearby_locker"
        suggested_args = {"location": args.get("location", "destination")}

    if tool_name == "analyze_evidence" and obs.get("likely_cause") == "merchant" and confidence >= 0.8:
        advice = ("High confidence merchant fault. Proceed to refund customer, "
                  "exonerate driver, and log merchant packaging feedback.")
        escalate = False  # high confidence, go ahead

    return {
        "confidence": round(float(confidence), 2),
        "escalate": bool(escalate),
        "advice": advice,
        "suggested_action": suggested_action,
        "suggested_args": suggested_args,
    }
