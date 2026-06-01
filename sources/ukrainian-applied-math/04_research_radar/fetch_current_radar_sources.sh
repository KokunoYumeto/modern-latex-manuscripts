#!/usr/bin/env bash
set -euo pipefail
mkdir -p arxiv_sources_current_radar
cd arxiv_sources_current_radar
for id in 2510.01348 2605.03678 2502.00575 2410.15480 2506.19769 2605.04355 2604.08060 2602.06995 2601.06095 2508.11687 2502.04963 2512.08341 2604.24033; do
  echo "Fetching arXiv source $id"
  mkdir -p "$id"
  curl -L "https://arxiv.org/e-print/$id" -o "$id/source.tar" || true
  (cd "$id" && tar -xf source.tar 2>/dev/null || true)
  find "$id" -maxdepth 2 -type f | sed "s#^#  #" | head -80 > "$id/inventory_head.txt" || true
done
