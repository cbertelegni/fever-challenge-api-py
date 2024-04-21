from app.services.events import EventService


class TestEventService:
    def test_evenservice_create(self, session):
        evt_service = EventService.create(db=session)
        assert isinstance(evt_service, EventService)

    def test_update_data_from_provider(self, session):
        evt_service = EventService.create(db=session)
        evt_service.update_events_from_provider()
