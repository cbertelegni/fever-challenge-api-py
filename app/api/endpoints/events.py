from fastapi import APIRouter, Depends
from typing import List
from app.schemas.events import EventOutSchema
from app.services.events import EventService


router = APIRouter()


@router.get("/update_data_from_provider")
def update_events_from_provider(event_service: EventService = Depends(EventService.create)):
    event_service.update_events_from_provider()


@router.get("/search")
def get_events(event_service: EventService = Depends(EventService.create)) -> List[EventOutSchema]:
    return event_service.get_events()
