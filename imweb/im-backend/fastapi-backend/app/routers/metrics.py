from fastapi import APIRouter
from app.models import performance_metrics

router = APIRouter()

@router.get("/")
def get_metrics():
    return performance_metrics