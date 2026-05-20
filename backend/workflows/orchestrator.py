from agents.intent_agent import detect_intent
from agents.escalation_agent import detect_escalation

def orchestrate_patient_flow(user_message):

    # Step 1: Detect intent
    intent = detect_intent(user_message)

    # Step 2: Detect escalation level
    escalation = detect_escalation(user_message)

    # Step 3: Conditional routing
    if escalation == "emergency":

        return {
            "status": "critical",
            "message": "Emergency case detected. Escalating immediately.",
            "intent": intent,
            "escalation": escalation
        }

    elif intent == "appointment":

        return {
            "status": "appointment_workflow",
            "message": "Routing patient to appointment scheduling.",
            "intent": intent,
            "escalation": escalation
        }

    elif intent == "insurance":

        return {
            "status": "insurance_workflow",
            "message": "Routing patient to insurance assistance.",
            "intent": intent,
            "escalation": escalation
        }

    else:

        return {
            "status": "general_support",
            "message": "Handling as general healthcare support request.",
            "intent": intent,
            "escalation": escalation
        }