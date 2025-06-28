# Makefile for LinkedIn Job Searcher
# Modern Python development workflow automation

.PHONY: help install install-dev test lint format check clean run

help: ## Show this help message
	@echo "LinkedIn Job Searcher - Development Commands"
	@echo "============================================"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install production dependencies
	pip install -e .

install-dev: ## Install development dependencies
	pip install -e ".[dev]"

test: ## Run tests with pytest
	pytest -v

test-cov: ## Run tests with coverage
	pytest --cov=linkedin_url_builder --cov-report=html --cov-report=term

lint: ## Run linting checks
	flake8 .
	isort --check-only .
	black --check .

format: ## Format code
	isort .
	black .

check: ## Run all checks (lint + test)
	$(MAKE) lint
	$(MAKE) test

clean: ## Clean up build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

run: ## Run the web application
	python start_app.py

run-cli: ## Show CLI help
	python cli.py --help

build: ## Build distribution packages
	python -m build

release: clean lint test build ## Prepare for release
	@echo "Ready for release! Run: twine upload dist/*"
