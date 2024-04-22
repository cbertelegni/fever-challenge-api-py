import responses
from urllib.parse import urljoin
from fastapi import status
from app.services.events import EventService
from app.core.config import settings
from app.tests.fixtures import events_xml_response, events_xml_invalid_date_response
from app.models.events import Event


class TestEventService:
    def test_evenservice_create(self, session):
        evt_service = EventService.create(db=session)
        assert isinstance(evt_service, EventService)

    def test_update_data_from_provider(self, session, mocked_responses):
        mocked_responses.add(
            responses.GET,
            urljoin(settings.PROVIDER_BASE_URL, 'api/events'),
            body=events_xml_response,
            content_type='text/xml',
            status=status.HTTP_200_OK
        )
        evt_service = EventService.create(db=session)
        evt_service.update_events_from_provider()

        events = session.query(Event).all()
        assert len(events) == 3

    def test_update_data_from_provider_must_update_the_same_obj(self, session, mocked_responses):
        mocked_responses.add(
            responses.GET,
            urljoin(settings.PROVIDER_BASE_URL, 'api/events'),
            body=events_xml_response,
            content_type='text/xml',
            status=status.HTTP_200_OK
        )
        evt_service = EventService.create(db=session)
        evt_service.update_events_from_provider()

        events = session.query(Event).all()
        assert len(events) == 3

        evt_service.update_events_from_provider()
        events = session.query(Event).all()
        assert len(events) == 3

    def test_update_data_from_provider_must_skip_broken_dates(self, session, mocked_responses):
        mocked_responses.add(
            responses.GET,
            urljoin(settings.PROVIDER_BASE_URL, 'api/events'),
            body=events_xml_invalid_date_response,
            content_type='text/xml',
            status=status.HTTP_200_OK
        )
        evt_service = EventService.create(db=session)
        evt_service.update_events_from_provider()

        events = session.query(Event).all()
        assert len(events) == 0

    def test_get_events_must_filter_by_sell_mode(self, session, mocked_responses):
        # Load data
        mocked_responses.add(
            responses.GET,
            urljoin(settings.PROVIDER_BASE_URL, 'api/events'),
            body=events_xml_response,
            content_type='text/xml',
            status=status.HTTP_200_OK
        )
        evt_service = EventService.create(db=session)
        evt_service.update_events_from_provider()

        total_events = session.query(Event).all()
        assert len(total_events) == 3
        assert len(evt_service.get_events()) == 2
