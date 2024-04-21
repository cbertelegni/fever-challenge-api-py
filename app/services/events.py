from typing import List
import xml.etree.ElementTree as ET
from pydantic import ValidationError
from fastapi import Depends
from app.clients.provider import ProviderClient
from app.schemas.events import EventOrmSchema
from app.crud.events import EventsCrud
from sqlalchemy.orm import Session
from app.db.session import get_db
import logging


class EventsXmlParserService:

    def _get_event_data(self, base_event):
        event_node = base_event.find('event')
        event_prices = [float(zone.get('price')) for zone in event_node.findall('zone')]
        event_data = event_node.attrib
        event_data.update(base_event.attrib)
        event_data.update(dict(
            max_price=max(event_prices),
            min_price=min(event_prices)
        ))
        return event_data

    def _fill_event_dates(self, event: EventOrmSchema):
        event.start_date = event.event_start_date.strftime("%Y-%m-%d")
        event.start_time = event.event_start_date.strftime("%H:%M:%S")
        event.end_date = event.event_end_date.strftime("%Y-%m-%d")
        event.end_time = event.event_end_date.strftime("%H:%M:%S")

    def parse_events(self, xml_str: str) -> List[EventOrmSchema]:
        root = ET.fromstring(xml_str)
        events = []
        for base_event in root.findall('output')[0].findall('base_event'):
            event_data = self._get_event_data(base_event=base_event)
            try:
                event = EventOrmSchema(**event_data)
                self._fill_event_dates(event=event)
            except ValidationError:
                logging.exception('Event Bad formated!')
            else:
                events.append(event)
        return events


class EventService:
    def __init__(
            self,
            provider_client: ProviderClient,
            parser_service: EventsXmlParserService,
            events_crud: EventsCrud) -> None:
        self.provider_client = provider_client
        self.parser_service = parser_service
        self.events_crud = events_crud

    @classmethod
    def create(cls, db: Session = Depends(get_db)):
        provider_client = ProviderClient.create()
        parser_service = EventsXmlParserService()
        events_crud = EventsCrud(db=db)
        return cls(
            provider_client=provider_client,
            parser_service=parser_service,
            events_crud=events_crud
        )

    def update_events_from_provider(self):
        events_xml = self.provider_client.fetch_xml_events()
        events = self.parser_service.parse_events(events_xml)
        for event in events:
            self.events_crud.create_or_update(payload=event)

    def get_events(self):
        return self.events_crud.get_events()
