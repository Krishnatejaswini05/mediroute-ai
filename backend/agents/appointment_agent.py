from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def handle_appointment_request(user_message):

    prompt = f"""
    You are an AI healthcare appointment scheduling assistant.

    Your responsibilities:
    - Identify medical specialty needed
    - Ask relevant follow-up scheduling questions
    - Help guide patient toward appointment booking

    Keep responses professional, short, and patient-friendly.

    Patient Message:
    {user_message}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a hospital appointment scheduling assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response = completion.choices[0].message.content

    return response