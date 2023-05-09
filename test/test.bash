#!/usr/bin/env bash

set -euxo pipefail

this_script="$(realpath "$0")"
parent="$(dirname "$this_script")"
cd "$parent"

poetry install

# typecheck and run tests in this directory
poetry run pyright .
poetry run mypy .
poetry run pytest .

# typecheck the stubs themselves
cd ../rdkit-stubs
poetry run --directory "$parent" pyright .
poetry run --directory "$parent" mypy .
