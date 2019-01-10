HOST=127.0.0.1
TEST_PATH=./

test:
	coverage run -m pytest
	coverage report myflask.py

pylint:
	pylint myflask.py

run:
	python myflask.py

db:
	alembic upgrade f5d0c232f24e
	alembic upgrade 4f273a4a6371
