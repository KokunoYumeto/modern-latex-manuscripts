#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT/src"
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
mkdir -p "$ROOT/pdf"
cp main.pdf "$ROOT/pdf/ukrainian_applied_math_core_session06.pdf"
