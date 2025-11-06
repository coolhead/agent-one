PY=python3.12

.PHONY: setup dev up down lint test ingest

setup:
	@(cd apps/api && $(PY) -m venv .venv && . .venv/bin/activate && pip -q install -U pip && pip -q install -e .)
	@(cd apps/ui && npm i)

dev:
	@make -j2 api ui

api:
	@(cd apps/api && . .venv/bin/activate && uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload)

ui:
	@(cd apps/ui && npm run dev -- --host 0.0.0.0 --port 8501)

ingest:
	@(cd apps/api && . .venv/bin/activate && PYTHONPATH=./ $(PY) -m src.rag.ingest --path ../../data)

lint:
	@(cd apps/api && . .venv/bin/activate && ruff check . && mypy src)

test:
	@(cd apps/api && . .venv/bin/activate && pytest -q)

up:
	docker compose -f infra/docker-compose.yml up -d --build

down:
	docker compose -f infra/docker-compose.yml down -v
