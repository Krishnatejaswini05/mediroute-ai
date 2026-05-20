from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def detect_intent(user_message):

    prompt = f"""
    You are an AI healthcare intent classification agent.

    Your task is to classify the patient's intent into ONE of these categories:

    - appointment
    - emergency
    - insurance
    - reschedule
    - navigation
    - general_query

    Only return the category name.

    Patient Message:
    {user_message}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a healthcare intent classification assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    intent = completion.choices[0].message.content

    return intent.strip()