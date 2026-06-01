#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../src"
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
mkdir -p ../pdf
cp main.pdf ../pdf/ukrainian_applied_math_core_session05.pdf
