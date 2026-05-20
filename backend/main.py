from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from agents.intent_agent import detect_intent
from agents.escalation_agent import detect_escalation
from workflows.orchestrator import orchestrate_patient_flow

import os

# Load environment variables
load_dotenv()
print(os.getenv("GROQ_API_KEY"))

# Create FastAPI app
app = FastAPI()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Request body model
class ChatRequest(BaseModel):
    message: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "MediRoute AI Backend Running"}

# Chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message

    result = orchestrate_patient_flow(user_message)

    return result