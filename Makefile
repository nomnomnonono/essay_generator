PHONY: ruff
ruff:
	uvx ruff format .
	uvx ruff check . --fix

PHONY: mypy
mypy:
	uvx mypy .
