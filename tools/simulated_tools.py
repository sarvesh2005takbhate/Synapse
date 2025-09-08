# tools/simulated_tools.py
import json

# -----------------------------
# Existing Tools
# -----------------------------

def check_traffic(origin=None, destination=None):
    return {"severity": "major", "delay_minutes": 18, "alternatives": [{"route": "A->C->D", "extra_mins": 6}]}

def get_merchant_status(merchant_id=None):
    return {"merchant_id": merchant_id, "prep_time_min": 40, "open_status": "open", "backlog": 12}

def get_nearby_merchants(merchant_type=None, location=None, radius_km=3):
    return {"nearby": [{"merchant_id": "m_102", "name": "QuickBites", "prep_time_min": 12}]}

def notify_customer(customer_id=None, message=None):
    return {"customer_id": customer_id, "notified": True, "message": message}

def re_route_driver(driver_id=None, new_route=None):
    return {"driver_id": driver_id, "new_route": new_route, "status": "assigned"}

def collect_evidence(order_id=None):
    return {"order_id": order_id, "evidence": ["photo_driver.jpg", "photo_customer.jpg"], "notes": "images_collected"}

def analyze_evidence(evidence=None):
    return {"likely_cause": "merchant", "confidence": 0.85}

def issue_instant_refund(order_id=None, amount=0, order_total=100):
    # ✅ Guardrail: prevent refunds > 20% of order_total
    max_allowed = 0.2 * order_total
    if amount > max_allowed:
        return {"order_id": order_id, "refund_issued": False, "amount": amount, "reason": "Refund exceeds 20% policy"}
    return {"order_id": order_id, "refund_issued": True, "amount": amount}

def exonerate_driver(driver_id=None):
    return {"driver_id": driver_id, "exonerated": True}

def find_nearby_locker(location=None):
    return {"locker_id": "locker_77", "distance_m": 300, "available": True}

def check_flight_status(flight_number=None):
    return {"flight_number": flight_number, "status": "on_time", "delay_minutes": 0}

def initiate_mediation_flow(order_id=None):
    return {"order_id": order_id, "mediation_session": f"med_{order_id}", "status": "started"}

def log_merchant_packaging_feedback(merchant_id=None, feedback=None):
    return {"merchant_id": merchant_id, "logged": True, "feedback": feedback or "no_feedback"}

def notify_resolution(order_id=None, resolution=None):
    return {"order_id": order_id, "notified": True, "resolution": resolution}

def contact_recipient_via_chat(recipient_id=None, message=None):
    return {"recipient_id": recipient_id, "message_sent": True, "recipient_response": "no_response"}

def suggest_safe_drop_off(location=None):
    return {"suggestion": "leave_with_concierge", "details": f"concierge at {location}", "requires_permission": True}

def calculate_alternative_route(origin=None, destination=None):
    return {"route": f"{origin}->{destination} via alt", "eta_change_minutes": 5, "reason": "accident_avoidance"}

def notify_passenger_and_driver(passenger_id=None, driver_id=None, message=None):
    return {
        "passenger_id": passenger_id,
        "driver_id": driver_id,
        "passenger_notified": True,
        "driver_notified": True,
        "message": message,
    }

# -----------------------------
# New Tools
# -----------------------------

def verify_address(address_text=None):
    """Simulate address verification and normalization."""
    return {"verified": True, "normalized_address": address_text.strip().title(), "confidence": 0.95}

def check_weather(location=None):
    """Simulate weather check."""
    return {"location": location, "weather": "Rainy", "impact": "Possible delays"}

def merchant_menu_equivalents(item=None, merchant_id=None):
    """Suggest alternative menu items."""
    return {"requested_item": item, "merchant_id": merchant_id, "alternatives": ["Veg Burger", "Chicken Wrap"]}

def voucher_policy_decider(context=None):
    """Decide voucher eligibility (caps abuse)."""
    return {"eligible": True, "max_discount_percent": 20, "reason": "Goodwill gesture"}

def pii_redact(text=None):
    """Redact personal identifiers."""
    if text is None:
        return {"redacted": ""}
    return {"redacted": text.replace("1234", "****").replace("Aarav", "[REDACTED]")}

def policy_guard(action=None, args=None):
    """Allowlist/Denylist enforcement."""
    if action == "issue_instant_refund":
        order_total = args.get("order_total", 100)
        if args.get("amount", 0) > 0.2 * order_total:
            return {"deny": True, "reason": "Refund exceeds 20% policy"}
    return {"deny": False}

def fraud_signal_check(order_id=None, customer_id=None):
    """Fraud detection signals."""
    return {"order_id": order_id, "customer_id": customer_id, "fraud_risk": "low"}

def resource_lock_manager(resource_id=None, action=None):
    """Prevent double-assignment of resources."""
    return {"resource_id": resource_id, "action": action, "status": "locked"}

def audit_log(entry=None):
    """Append-only safety audit log."""
    return {"logged": True, "entry": entry}

def metrics_emit(metric_name=None, value=None):
    """Emit operational metrics."""
    return {"metric": metric_name, "value": value, "status": "recorded"}
