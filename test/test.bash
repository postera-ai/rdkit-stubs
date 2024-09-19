#!/usr/bin/env bash

set -euxo pipefail

this_script="$(realpath "$0")"
parent="$(dirname "$this_script")"
cd "$parent"

poetry install

export PYRIGHT_PYTHON_FORCE_VERSION="1.1.338"

# typecheck and run tests in this directory
poetry run pyright .
poetry run mypy .
poetry run pytest .

# typecheck the stubs themselves
cd "$parent"/..
poetry run --directory "$parent" pyright .
poetry run --directory "$parent" mypy .
