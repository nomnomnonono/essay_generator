PHONY: ruff
ruff:
	uvx ruff format .
	uvx ruff check . --fix

PHONY: mypy
mypy:
	uvx mypy .

PHONY: test
test:
	uv run pytest .

PHONY: setup
setup:
	uv sync

PHONY: run
run:
	uv run uvicorn app.main:app --reload
