.DEFAULT_GOAL := help

.PHONY: help lint test

SRC_DIR=patterns

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

update: ## Update project dependencies
	@poetry update

install: ## Install project dependencies and pre-commit hooks
	@poetry install
	@poetry run pre-commit install

test: ## Run unit tests
	@poetry run pytest -s -v --log-level=INFO --cov=$(SRC_DIR)
