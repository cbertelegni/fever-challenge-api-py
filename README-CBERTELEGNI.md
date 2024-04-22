# Fever code challenge - Cristian Bertelegni

This is a FastAPI application. SQLAlchemy was used as ORM and Alembic to handle the migrations of the database.
Pydantic schemas were used to validate and format the input and output data.
This project has **100% coverage** in tests. You can run `make coverage` to see. The development process followed the TDD methodology. Pytest is the main library used for testing, and Responses is used to mock and block external requests.

## Project structure

- app: main app folder
  - alembic: Folder used by Alembic for the migrations
  - api: API routes
  - clients: Clients to consume external resources
  - core: Project settings
  - crud: Access to the database
  - db: Database/SQLAlchemy settings
  - models: Representation of the DB tables
  - schemas: Serializers for input and output data
  - services: Business logic
  - tests: Test folder
- db: Docker file for development purposes

## Data Update

The data is pre-calculated before being saved to avoid parsing it on each request. I added a response header (**x-process-time**) to show the processing time of the request. The expected time is between 3ms/17ms.

The data is updated when the server starts, and I added an API method to update the data on demand. The idea is to place this in a Celery task.

## API

The calculation of the min/max price, parsing the [start/end]-date and [start/end]-time is too expensive if we have a lot of requests. To avoid this, I pre-calculate when the data is scraped and stored.

If the API receives a lot of requests, we can:

- Add caching (Varnish, MaxCDN, Memcache).
- Scale the number of pods to serve the requests.
- Use asyncio to handle multiple requests.

## Known issues and Considerations:

- The `base_event_id="444"` has a bug in the date. I don't know if that's on purpose.
- The data update must be done from a Celery worker. For a faster implementation, the data update is on demand from an exposed method in the API.
- The tests fail the first time they are run through the migrations; you have to run the command again.

## Running the app:

1. Make a copy of `app/.template.env` and rename it to `app/.env`.

2. Open a terminal and run the migrations: `make run`.

3. Open a browser at `http://0.0.0.0:8000/docs` or `http://0.0.0.0:8000/redoc`.

## Prerequisites to contribute:

Intalling pre-commit

```bash
pip install -r requirements-dev.txt
pre-commit install -t pre-commit -t pre-push
```


## Makefile commands

* **make build**: Build the docker images
* **make run**: Run the application running on docker
* **make tests**: Run the tests application
* **make coverage**: Run the test coverage for the application
    * Open `./htmlcov/index.html` in a browser to see the test coverage for this aplication


## Used tools:

- Fastapi
- Pydantic
- SqlAlchemy
- Alembic
- Postgresql
- Pytest
- Responses
- Docker
- Docker-Compose
- Pre-commit[Flake8]
- Make

