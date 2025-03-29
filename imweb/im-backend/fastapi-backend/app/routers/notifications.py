from fastapi import APIRouter, HTTPException
from app.models import notifications

router = APIRouter()

@router.get("/")
def get_notifications():
    return notifications

@router.post("/{notification_id}/read")
def mark_notification_read(notification_id: int):
    notification = next((n for n in notifications if n["id"] == notification_id), None)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    notification["read"] = True
    return notification