from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, Query
from app.schemas.events import EventOutSchema
from app.services.events import EventService


router = APIRouter()


@router.get("/update_data_from_provider")
def update_events_from_provider(event_service: EventService = Depends(EventService.create)):
    event_service.update_events_from_provider()


@router.get("/search")
def get_events(
        starts_at: datetime = Query(
            default=None, description="Date when the event starts", example="2017-07-21T17:32:28Z"),
        ends_at: datetime = Query(
            default=None, description="Date when the event ends", example="2021-07-21T17:32:28Z"),
        event_service: EventService = Depends(EventService.create)
        ) -> List[EventOutSchema]:
    return event_service.get_events(event_start_date=starts_at, event_end_date=ends_at)
