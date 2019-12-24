.PHONY: tests


# Development

dependencies:
	poetry install

development: dependencies

# Testing

unit-tests:
	poetry run py.test tests/unit

functional-tests:
	poetry run py.test tests/functional

tests: unit-tests functional-tests

# Static analysis

lint-code:
	poetry run flake8 intcode

lint-tests:
	poetry run flake8 tests

lint: lint-code lint-tests

type-check:
	poetry run mypy -p intcode

# Packaging

build: tests lint
	poetry build

publish: build
	poetry publish
