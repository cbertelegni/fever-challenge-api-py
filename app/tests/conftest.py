from app.main import app
import pytest
import responses
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="function", autouse=True)
def mocked_responses():
    with responses.RequestsMock() as mock_requests:
        yield mock_requests
