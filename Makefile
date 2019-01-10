HOST=127.0.0.1
TEST_PATH=./

test:
	coverage run -m pytest
	coverage report myflask.py

pylint:
	pylint myflask.py

run:
	python myflask.py

alembic:
	alembic upgrade head
