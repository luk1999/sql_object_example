BASE_DIR=$(shell pwd)
SQLITE_CONNECTION="sqlite://$(BASE_DIR)/db.sqlite"

format:
	black --line-length 119 --target-version py312 .

init:
	PYTHONPATH=src python src/init_db.py

migrate-add-first:
	PYTHONPATH=src sqlobject-admin record --egg=example --module=models --connection=$(SQLITE_CONNECTION) 

migrate-add-next:
	PYTHONPATH=src sqlobject-admin record --egg=example --module=models --connection=$(SQLITE_CONNECTION) --no-db-record

migrate-upgrade:
	PYTHONPATH=src sqlobject-admin upgrade --egg=example --connection=$(SQLITE_CONNECTION)

migrate-list-models:
	PYTHONPATH=src sqlobject-admin list --module=models

migrate-status:
	PYTHONPATH=src sqlobject-admin status --module=models --connection=$(SQLITE_CONNECTION)

requirements:
	pipenv requirements > requirements.txt

run:
	PYTHONPATH=src uvicorn main:app --reload
