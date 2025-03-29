from pydantic import BaseModel

class AgentCreate(BaseModel):
    name: str
    description: str
    role: str
    system_prompt: str
    model: str = "gemini-pro"