from app.main import app
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client