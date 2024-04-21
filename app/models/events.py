from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, Text, Float, INT
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    title = Column(Text, nullable=False)
    event_start_date = Column(DateTime, nullable=True)
    event_end_date = Column(DateTime, nullable=True)
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    event_id = Column(INT, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
