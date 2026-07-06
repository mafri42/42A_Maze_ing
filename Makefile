VENV = ./.venv
BIN = $(VENV)/bin

all: install run

install:
	python3 -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt
	$(BIN)/pip install -e .

run:
	$(BIN)/python3 a_maze_ing.py config.txt

debug:
	$(BIN)/python3 -m pdb a_maze_ing.py config.txt

clean:
	@-rm $(VENV) -fr
	@-rm -rf __pycache__ .mypy_cache -fr

lint:
	@flake8 ./src
	@mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs ./src

build:
	$(BIN)/pip install build
	$(BIN)/python3 -m build --wheel --outdir . --config-setting=--build-option=--plat-name=linux_x86_64

.PHONY: all install run debug clean lint lint-strict build
