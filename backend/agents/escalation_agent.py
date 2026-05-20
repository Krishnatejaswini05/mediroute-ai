from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def detect_escalation(user_message):

    prompt = f"""
    You are an AI healthcare emergency escalation agent.

    Your task is to determine whether the patient's message indicates:
    
    - emergency
    - non_emergency

    Only return one category.

    Patient Message:
    {user_message}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a healthcare emergency detection assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    escalation = completion.choices[0].message.content

    return escalation.strip()