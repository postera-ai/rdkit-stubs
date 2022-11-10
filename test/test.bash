#!/usr/bin/env bash

set -euxo pipefail

this_script="$(realpath "$0")"

# typecheck and run tests in this directory
cd  "$(dirname "$this_script")"
pyright .
mypy .
pytest .

# typecheck the stubs themselves
cd  "$(dirname "$(dirname "$this_script")")"/rdkit-stubs
pyright .
mypy .
