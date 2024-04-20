from app.services.events import EventService


class TestEventService:
    def test_evenservice_create(self):
        evt_service = EventService.create()
        assert isinstance(evt_service, EventService)

    def test_update_data_from_provider(self):
        evt_service = EventService.create()
        evt_service.update_events_from_provider()
