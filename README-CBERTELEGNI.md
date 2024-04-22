# Fever code challenge - Cristian Bertelegni

This is a FastApi application. Sqlalchemy was used as ORM and Alembic to handle the migrations of the data base.
Pydantic Schemas was used to validate and formating the input and output data. 
This project has **100% of coverage** tests. You can run `make coverage` to see it.
The developed process was using TDD metodology.
Pytest is the main library to do tests and Responses to mock and block externals request.


## Project structure

* app: main app folder
    * alembic: Folder used by alembic for the migrations
    * api: API rutes
    * clients: Cients to consume external resources
    * core: Project settings
    * crud: Access to the database
    * db: Database/SqlAlchemy settings
    * models: Representation of the DB tables
    * schemas: Serialaizers for input and output data
    * services: Bussines logic
    * tests: Folder tests 
* db: docker file for dev porpousal


## Data Update

The data is pre-calculate before save to avoid parsing it on each request.
I added a header response (**x-process-time**) to know the time process of the resquest. The expected time is between 3ms/17ms.

The data is updated when the server start and I added a API method to update the data on demand. The idea is place this in a celery task.

## API

The calc of the min/max price, parse the [start/end]-date and [start/end]-time is to expensive if we have a lot of requests, to avoid it I'm precalculating when the data is scrapped and storage.

If the API have a lot of requests we can do:

* Adding cache (varnish, maxcdn, memcache).
* Scale the numbrer of pods to serve the requests.
* Using asyncio to handle multiple requests.


## Knowed issued and Considerations:

* The `base_event_id="444"` has a bug in the date. I don't know if that's on purpose.
* The data update must be from a celery worker, for a faster implementation the data update is on demand from an exposed method in the API 
* The tests fail the first time they are run through the migrations, you have to run the command again.


## Running the app:

1 - Make a copy of `app/.template.env` to `app/.env`

2 - Open a terminal and run the migrations: `make run`

3 - Open a browser on `http://0.0.0.0:8000/docs` or `http://0.0.0.0:8000/redoc`


## Prerequisites to contribute:

Intalling precommit to pre-commit

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

