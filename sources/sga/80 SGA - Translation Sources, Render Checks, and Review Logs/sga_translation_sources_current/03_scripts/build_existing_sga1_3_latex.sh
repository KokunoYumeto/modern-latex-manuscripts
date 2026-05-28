#!/usr/bin/env bash
set -euo pipefail
# Run from the root of an extracted source work folder containing:
# input/01_SGA_1_4_BASELINES_TRANSLATIONS_AND_REPOS/05_SOURCE_REPOS/jcreinhold_sga_llm_translation
BASE="${1:-/mnt/data/sga_work/input/01_SGA_1_4_BASELINES_TRANSLATIONS_AND_REPOS/05_SOURCE_REPOS/jcreinhold_sga_llm_translation}"
OUT="${2:-/mnt/data/sga_work/output/01_existing_translations_latex}"
mkdir -p "$OUT"
python - <<PY
from pathlib import Path
base=Path('$BASE')
out=Path('$OUT')
vols={'i':'SGA1_existing_english_from_jcreinhold.md','ii':'SGA2_existing_english_from_jcreinhold.md','iii':'SGA3_existing_english_from_jcreinhold.md'}
titles={'i':'SGA 1: Étale Coverings and the Fundamental Group', 'ii':'SGA 2: Local Cohomology and Lefschetz Theorems', 'iii':'SGA 3: Group Schemes'}
for vol, fname in vols.items():
    files=sorted((base/vol).glob('*.md'))
    content=[f'# {titles[vol]}\n\n', '> Consolidated from the jcreinhold Markdown snapshot. Not mathematically proofed in this conversion pass.\n\n']
    for p in files:
        content.append(f'\n\n<!-- SOURCE: {p.name} -->\n\n')
        content.append(p.read_text(encoding='utf-8', errors='replace'))
    (out/fname).write_text(''.join(content), encoding='utf-8')
PY
for f in "$OUT"/*.md; do
  b="$(basename "$f" .md)"
  pandoc --from=markdown+tex_math_dollars --to=latex --standalone --metadata=lang:en-US "$f" -o "$OUT/${b}.tex"
done
