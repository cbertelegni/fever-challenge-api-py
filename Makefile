log_error = (>&2 echo "\x1B[31m>> $1\x1B[39m" && exit 1)
build:
	docker-compose build
run:
	docker-compose up
run.debug:
	docker-compose -f docker-compose.yml -f docker-compose.debug.yml up
tests:
	docker-compose run --entrypoint "pytest -v --disable-warnings app/tests" feverchallenge
tests.debug:
	docker-compose run --publish 5678:5678 --entrypoint "python -u -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pytest -v --disable-warnings app/tests" feverchallenge
coverage:
	docker-compose run --entrypoint "bash -c 'coverage run -m pytest -v --disable-warnings app/tests && coverage html'" feverchallenge
checkmigrations:
	docker-compose run --entrypoint "alembic -c app/alembic.ini history" feverchallenge
makemigration:
	@[ "$(msg)" ] || $(call log_error, "You must set the message migration! msg=\'migration message\'")
	docker-compose run --entrypoint "alembic -c app/alembic.ini revision --autogenerate -m '$(msg)'" feverchallenge
db upgrade:
	docker-compose run --entrypoint "alembic -c app/alembic.ini upgrade head" feverchallenge
