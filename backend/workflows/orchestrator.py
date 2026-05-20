from agents.intent_agent import detect_intent
from agents.escalation_agent import detect_escalation
from agents.appointment_agent import handle_appointment_request
from agents.no_show_agent import predict_no_show_risk

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

        appointment_response = handle_appointment_request(user_message)

        no_show_prediction = predict_no_show_risk(user_message)

        return {
            "status": "appointment_workflow",
            "intent": intent,
            "escalation": escalation,
            "appointment_response": appointment_response,
            "no_show_prediction": no_show_prediction
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