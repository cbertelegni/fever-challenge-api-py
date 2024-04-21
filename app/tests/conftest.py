from app.main import app
import pytest
import responses
from fastapi.testclient import TestClient
from app.db.session import make_sqlalchemy_database_uri, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base_class import Base


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client


@pytest.fixture(scope="function", autouse=False)
def mocked_responses():
    with responses.RequestsMock() as mock_requests:
        yield mock_requests


engine = create_engine(make_sqlalchemy_database_uri() + "_test")
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_db_session():
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope="module")
def connection():
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope="function")
def session(connection):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    transaction = connection.begin()
    session = Session()
    try:
        yield session
    finally:
        session.close()
        transaction.rollback()


app.dependency_overrides[get_db] = override_db_session
