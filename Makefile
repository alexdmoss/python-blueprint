.PHONY: run test lint clean

run:
	@poetry run blueprint

test:
	@poetry run pytest

lint:
	@echo "Running Flake8 against source and test files..."
	@poetry run flake8
	@echo "Running Bandit against source files..."
	@poetry run bandit -r --ini setup.cfg

clean:
	rm -rf .pytest_cache .coverage blueprint/__pycache__ tests/__pycache__
