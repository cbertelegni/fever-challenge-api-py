import pytest
import responses
from fastapi import status
from app.core.config import settings
from urllib.parse import urljoin
from app.clients.provider import ProviderClient
from app.tests.fixtures import events_xml_response


class TestProviderClient:
    @pytest.fixture(scope='function')
    def mocked_apievents_xml(self, mocked_responses):
        mocked_responses.add(
            responses.GET,
            urljoin(settings.PROVIDER_BASE_URL, 'api/events'),
            body=events_xml_response,
            content_type='text/xml',
            status=status.HTTP_200_OK
        )
        yield mocked_responses

    def test_create_provicer_client(self):
        provider = ProviderClient.create()
        assert isinstance(provider, ProviderClient)

    def test_fetch_events(self, mocked_apievents_xml):
        provider = ProviderClient.create()
        content = provider.fetch_xml_events()
        assert content == events_xml_response
