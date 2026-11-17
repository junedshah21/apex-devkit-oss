#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
export PYTHONPATH="${PWD}/src"
python -m compileall -q src tests
python -m unittest discover -s tests -v
python -m apex_devkit --help >/dev/null
