from fastapi import APIRouter
from typing import List
from app.schemas.events import EventSummarySchema

router = APIRouter()


@router.get("/search")
def get_events() -> List[EventSummarySchema]:
    return []
