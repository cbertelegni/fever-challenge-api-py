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

    def get_events(self):
        events = self.db.query(Event).filter_by(sell_mode='online')
        return events.all()
