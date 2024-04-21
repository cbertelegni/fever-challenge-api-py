from fastapi import APIRouter, Depends
from typing import List
from app.schemas.events import EventSummarySchema
from app.services.events import EventService


router = APIRouter()


@router.get("/search")
def get_events(event_service=Depends(EventService.create)) -> List[EventSummarySchema]:
    return event_service.get_events()
