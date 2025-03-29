from fastapi import APIRouter, HTTPException
from app.models import conversations, messages

router = APIRouter()

@router.get("/")
def list_conversations():
    return conversations

@router.get("/{conversation_id}")
def get_conversation(conversation_id: str):
    conversation = next((c for c in conversations if c["id"] == conversation_id), None)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation