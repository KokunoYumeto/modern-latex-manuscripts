#!/usr/bin/env bash
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOGDIR="$ROOT/build_logs/claude_standalone_logs"
mkdir -p "$LOGDIR" "$ROOT/pdf/claude_standalones"

build_one() {
  local dir="$1" tex="$2" outname="$3"
  echo "== Building $outname =="
  (cd "$dir" && xelatex -interaction=nonstopmode -halt-on-error "$tex" > "$LOGDIR/${outname}.log" 2>&1 && xelatex -interaction=nonstopmode -halt-on-error "$tex" >> "$LOGDIR/${outname}.log" 2>&1)
  if [ -f "$dir/${tex%.tex}.pdf" ]; then cp "$dir/${tex%.tex}.pdf" "$ROOT/pdf/claude_standalones/${outname}.pdf"; fi
}

build_one "$ROOT/paper_modules/claude_standalone_patched/sdr_survey_1804_06564_patched" "paper_uk_core_patched.tex" "sdr_survey_1804_06564_uk_patched" || true
build_one "$ROOT/paper_modules/claude_standalone_patched/sensor_fusion_2506_19769_patched" "0_main.tex" "sensor_fusion_2506_19769_uk_patched" || true
build_one "$ROOT/paper_modules/claude_standalone_patched/antenna_maxwell_foundations_patched" "antenna_maxwell_patched.tex" "antenna_maxwell_foundations_uk_patched" || true
build_one "$ROOT/paper_modules/claude_standalone_patched/zuazua_wave_chapter01_patched" "zuazua_chapter01_patched.tex" "zuazua_wave_chapter01_uk_patched" || true
