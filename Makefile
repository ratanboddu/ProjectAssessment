HOST=127.0.0.1
TEST_PATH=./

test:
	pytest --verbose

pylint:
	pylint myflask.py

run:
	python myflask.py

alembic:
	alembic upgrade head
