import pytest
import responses
from urllib.parse import urljoin
from fastapi import status
from datetime import datetime
from app.core.config import settings
from app.services.events import EventService
from app.tests.fixtures import events_xml_response


class TestEventsSearch:
    @pytest.fixture(scope="function")
    def mock_data_provider(self, session, mocked_responses):
        mocked_responses.add(
            responses.GET,
            urljoin(settings.PROVIDER_BASE_URL, 'api/events'),
            body=events_xml_response,
            content_type='text/xml',
            status=status.HTTP_200_OK
        )
        evt_service = EventService.create(db=session)
        evt_service.update_events_from_provider()

    def test_search_without_data_in_db(self, test_client, session):
        api_method = "/search"
        response = test_client.get(
            api_method,
            params={
                "starts_at": datetime(year=2020, month=1, day=1).isoformat(),
                "ends_at": datetime(year=2025, month=1, day=1).isoformat()
            }
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 0

    def test_search_between_dates(self, test_client, session, mock_data_provider):
        api_method = "/search"
        response = test_client.get(
            api_method,
            params={
                "starts_at": datetime(year=2021, month=7, day=1).isoformat(),
                "ends_at": datetime(year=2021, month=8, day=1).isoformat()
            }
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1

    def test_search_must_exclude_sell_mode_offline(self, test_client, session, mock_data_provider):
        api_method = "/search"
        response = test_client.get(
            api_method,
            params={
                "starts_at": datetime(year=2020, month=7, day=1).isoformat(),
                "ends_at": datetime(year=2022, month=8, day=1).isoformat()
            }
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 2

    def test_update_data_provider_endpoint(self, test_client, session, mock_data_provider):
        api_method = "/update_data_from_provider"
        response = test_client.get(
            api_method
        )

        assert response.status_code == status.HTTP_200_OK
