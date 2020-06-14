# This will set the env variables from source.sh
IGNORE := $(shell bash -c "source setup.sh; env | sed 's/=/:=/' | sed 's/^/export /' > makeenv")                         
include makeenv 

DB_NAME := postgres


# run: DATABASE_URL=postgres://postgres:postgres@localhost:5432/postgres
run:
	FLASK_APP=app.py FLASK_ENV=development flask run

setup:
	source setup.sh

reset-db:
	dropdb $(DB_NAME) && createdb $(DB_NAME)
	flask db upgrade

start-db-server:
	pg_ctl -D /usr/local/var/postgres start

stop-db-server:
	pg_ctl -D /usr/local/var/postgres stop

connect-to-db:
	psql $(DB_NAME)