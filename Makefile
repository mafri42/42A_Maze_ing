VENV = ./.venv
BIN = $(VENV)/bin

all: install run

build:
	python3 -m venv $(VENV)
	$(BIN)/pip install poetry
	$(BIN)/poetry build

install: build
	python3 -m venv $(VENV)
	$(BIN)/pip install dist/*.whl

run:
	$(BIN)/python3 a_maze_ing.py config.txt

debug:
	$(BIN)/python3 -m pdb a_maze_ing.py config.txt

clean:
	@-rm $(VENV) -fr
	@-rm -rf __pycache__ .mypy_cache -fr
	@-rm -rf build && rm -rf dist

lint:
	@flake8 ./src
	@mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs ./src

lint-strict: lint
	@mypy ./src --strict

.PHONY: all install run debug clean lint lint-strict build
