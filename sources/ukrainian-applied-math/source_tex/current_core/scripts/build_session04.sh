#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../src"
mkdir -p ../pdf ../build_logs
xelatex -interaction=nonstopmode -halt-on-error main.tex > ../build_logs/build_session04.log 2>&1
xelatex -interaction=nonstopmode -halt-on-error main.tex >> ../build_logs/build_session04.log 2>&1
cp main.pdf ../pdf/ukrainian_applied_math_core_session04.pdf
