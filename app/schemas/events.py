from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date

class EventSummarySchema(BaseModel):
    id: UUID = Field(title="Identifier for the plan")
    title: str = Field(title="Title of the plan")

    min_price: float = Field(default=None, title="Min price from all the available tickets")
    max_price: float = Field(default=None, title="Max price from all the available tickets")
    start_date: date = Field(title="Date when the event starts in local time")
    end_date: date = Field(default=None, title="Date when the event ends in local time")

    # start_time*	string($time)
    # nullable: true
    # example: 22:38:19
    # Time when the event starts in local time

    # end_time*	string($time)
    # nullable: true
    # example: 14:45:15
    # Time when the event ends in local time

