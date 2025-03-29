import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import agents, conversations, notifications, metrics
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateText"

# Initialize FastAPI app
app = FastAPI(title="NexusOps AI Workforce Platform")

# Correctly resolve the static directory path
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
print("Static directory path:", static_dir)

# Serve frontend static files
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(agents.router, prefix="/api/agents", tags=["Agents"])
app.include_router(conversations.router, prefix="/api/conversations", tags=["Conversations"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(metrics.router, prefix="/api/metrics", tags=["Metrics"])

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Chat request model
class ChatRequest(BaseModel):
    agent_id: int
    message: str

# Chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Handles chat messages sent by the user and generates a response using the Gemini API.
    """
    # Prepare the prompt for the Gemini API
    prompt = f"Agent {request.agent_id}: {request.message}"
    print("Prompt sent to Gemini API:", prompt)

    try:
        # Call the Gemini API
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            json={
                "prompt": prompt,  # Pass the prompt as a string
                "temperature": 0.7,  # Adjust creativity level
                "maxOutputTokens": 150,  # Limit the response length
            },
            headers={"Content-Type": "application/json"},
        )

        # Handle the Gemini API response
        if response.status_code == 200:
            result = response.json()
            print("Gemini API response:", result)
            reply = result.get("candidates", [{}])[0].get("output", {}).get("text", "No response available")
            return {"response": reply}
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        print("Error communicating with Gemini API:", str(e))
        raise HTTPException(status_code=500, detail=str(e))