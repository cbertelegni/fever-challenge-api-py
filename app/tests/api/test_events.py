import pytest
from fastapi import status


class TestEventsSearch:

    def test_search_must_be_exists(self, test_client):
        api_method = "/search"
        response = test_client.get(api_method)

        assert response.status_code == status.HTTP_200_OK
