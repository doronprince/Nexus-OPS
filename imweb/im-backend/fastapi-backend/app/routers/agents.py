from fastapi import APIRouter, HTTPException
from app.schemas import AgentCreate
from app.models import agents

router = APIRouter()

@router.get("/")
def list_agents():
    return agents

@router.post("/")
def create_agent(agent: AgentCreate):
    agent_id = max([a["id"] for a in agents], default=0) + 1
    new_agent = agent.dict()
    new_agent["id"] = agent_id
    agents.append(new_agent)
    return new_agent