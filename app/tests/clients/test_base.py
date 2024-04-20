import pytest
import responses
from urllib.parse import urljoin
from fastapi import status
from requests import Response
from app.clients.base import BaseClient


class TestProviderClient:
    @pytest.fixture(scope='function')
    def base_url(self):
        return 'https://test-expernal.com'

    @pytest.fixture(scope='function')
    def test_method(self):
        return 'api/test'

    @pytest.fixture(scope='function')
    def mocked_apitest_request(self, mocked_responses, base_url, test_method):
        mocked_responses.add(
            responses.GET,
            urljoin(base_url, test_method),
            json={},
            status=status.HTTP_200_OK
        )
        yield mocked_responses

    def test_build_url(self, base_url):
        client = BaseClient(base_url=base_url)
        url = client.get_url('api/test')
        assert url == f'{base_url}/api/test'

    def test_get_method_must_return_response(self, base_url, test_method, mocked_apitest_request):
        client = BaseClient(base_url=base_url)
        response = client.get(test_method)

        assert isinstance(response, Response)
