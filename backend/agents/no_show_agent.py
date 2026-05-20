from groq import Groq
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def predict_no_show_risk(user_message):

    prompt = f"""
    You are an AI healthcare no-show risk prediction assistant.

    Analyze the patient's message and determine:

    - risk_level (low, medium, high)
    - reason for prediction
    - recommended intervention

    Return response ONLY in this JSON format:

    {{
        "risk_level": "...",
        "reason": "...",
        "recommended_action": "..."
    }}

    Patient Message:
    {user_message}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a healthcare no-show prediction assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response = completion.choices[0].message.content

    parsed_response = json.loads(response)

    return parsed_response