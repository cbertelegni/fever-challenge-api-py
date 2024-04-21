from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class EventSchema(BaseModel):
    title: str = Field(title="Title of the plan")
    min_price: float = Field(default=None, title="Min price from all the available tickets")
    max_price: float = Field(default=None, title="Max price from all the available tickets")
    event_start_date: datetime = Field(title="Date when the event starts in local time")
    event_end_date: datetime = Field(default=None, title="Date when the event ends in local time")
    event_id: int = None


class EventSummarySchema(EventSchema):
    id: UUID = Field(title="Identifier for the plan")
    start_time: str = Field(default=None, title="Time when the event starts in local time")
    end_time: str = Field(default=None, title="Time when the event ends in local time")
    # example: 22:38:19
