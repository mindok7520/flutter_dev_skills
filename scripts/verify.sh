#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir/.."
validation_python=python3
if [[ -x .venv/bin/python ]]; then
  validation_python=.venv/bin/python
fi
"$validation_python" scripts/validate.py
"$validation_python" -m unittest discover -s tests -v
