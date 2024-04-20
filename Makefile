build:
	docker-compose build
run:
	docker-compose up
run.debug:
	docker-compose -f docker-compose.yml -f docker-compose.debug.yml up
tests:
	docker-compose run --entrypoint "pytest -v --disable-warnings app/tests" feverchallenge
coverage:
	docker-compose run --entrypoint "bash -c 'coverage run -m pytest -v --disable-warnings app/tests && coverage html'" feverchallenge
