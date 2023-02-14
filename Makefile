.DEFAULT_GOAL := help

.PHONY: help lint test

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

include config.env
include Makefile.hooks

update-deps: ## Update project dependencies
	@poetry update

format: ## Run code formatter
	@poetry run black $(SRC_DIR)

lint: ## Run linter on project code
	@echo '##### Running static code analysis with pylint... #####'
	@poetry run pylint $(SRC_DIR)

unit: ## Run unit tests2
	@poetry run pytest -vs --log-level=INFO --cov=$(SRC_DIR) -p no:warnings

test: format lint unit ## Run code formatter, linter and unit tests
