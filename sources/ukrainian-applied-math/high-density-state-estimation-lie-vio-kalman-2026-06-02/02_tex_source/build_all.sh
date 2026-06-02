#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
# Integrated
OSFONTDIR=/usr/share/fonts/truetype/dejavu xelatex -interaction=nonstopmode -halt-on-error main.tex > build_main_pass1.log
OSFONTDIR=/usr/share/fonts/truetype/dejavu xelatex -interaction=nonstopmode -halt-on-error main.tex > build_main_pass2.log
# Standalones
cd standalone
for f in *.tex; do
  b="${f%.tex}"
  OSFONTDIR=/usr/share/fonts/truetype/dejavu xelatex -interaction=nonstopmode -halt-on-error "$f" > "${b}_pass1.log"
  OSFONTDIR=/usr/share/fonts/truetype/dejavu xelatex -interaction=nonstopmode -halt-on-error "$f" > "${b}_pass2.log"
done
