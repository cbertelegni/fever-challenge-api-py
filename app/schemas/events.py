from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class EventBaseSchema(BaseModel):
    title: str = Field(title="Title of the plan")
    min_price: float = Field(default=None, title="Min price from all the available tickets")
    max_price: float = Field(default=None, title="Max price from all the available tickets")
    start_time: str = Field(default=None, title="Time when the event starts in local time")
    end_time: str = Field(default=None, title="Time when the event ends in local time")
    start_date: str = Field(default=None, title="Date when the event starts in local time")
    end_date: str = Field(default=None, title="Date when the event ends in local time")


class EventOrmSchema(EventBaseSchema):
    event_start_date: datetime = Field(title="Date when the event starts in local time")
    event_end_date: datetime = Field(default=None, title="Date when the event ends in local time")
    event_id: int = None
    base_event_id: int = None
    sell_mode: str = None


class EventOutSchema(EventBaseSchema):
    id: UUID = Field(title="Identifier for the plan")
