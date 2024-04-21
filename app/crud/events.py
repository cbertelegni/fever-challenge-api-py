from sqlalchemy.orm import Session
from app.models.events import Event
from app.schemas.events import EventSchema


class EventsCrud:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_or_update(self, payload: EventSchema):
        event = self.db.query(Event).filter(Event.event_id == payload.event_id).one_or_none()
        if event:
            event.update(**payload.model_dump_json())
        else:
            event = Event(**payload.dict())
        self.db.add(event)
        self.db.commit()
