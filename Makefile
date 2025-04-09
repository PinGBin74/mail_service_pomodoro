# DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8080

.PHONY: run install uninstall help

run: ## Run the application using uvicorn with provided arguments on defaults
	#poetry run gunicorn app.main:app -c gunicorn.conf.py
	#poetry run gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker
	#uvicorn main:app --host $(HOST) --port $(PORT) --reload --env-file $(ENV_FILE)
	uvicorn main:app --host 0.0.0.0 --port 8000

install: ## Install a dependency using poetry
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: ## Uninstall a dependency using poetry
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)
migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
	alembic upgrade head
help: ## Show this help message
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)