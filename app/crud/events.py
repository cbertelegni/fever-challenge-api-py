from datetime import datetime
from sqlalchemy.orm import Session
from app.models.events import Event
from app.schemas.events import EventOrmSchema


class EventsCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_or_update(self, payload: EventOrmSchema):
        event = self.db.query(Event).filter_by(event_id=payload.event_id, base_event_id=payload.base_event_id)
        if event.one_or_none():
            event.update(payload.dict())
        else:
            event = Event(**payload.dict())
            self.db.add(event)
        self.db.commit()

    def get_events(self, event_start_date: datetime = None, event_end_date: datetime = None):
        events = self.db.query(Event).filter_by(sell_mode='online')
        if event_start_date:
            events = events.filter(Event.event_start_date >= event_start_date)
        if event_end_date:
            events = events.filter(Event.event_end_date <= event_end_date)
        return events.all()
