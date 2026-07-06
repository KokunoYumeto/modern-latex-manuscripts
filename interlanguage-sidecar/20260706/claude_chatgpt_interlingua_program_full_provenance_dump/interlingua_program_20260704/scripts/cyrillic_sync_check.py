# Cyrillic synchronization check: which Latin-script ISV translation files lack a
# Cyrillic sibling (validator-coverage gaps), plus kolc*/колц* totals cross-check.
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
T = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\translations")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

latin_files = []
for f in T.rglob("*.tex"):
    s = str(f).lower()
    if "interslavic" in s and "cyrillic" not in s:
        latin_files.append(f)

missing = []
paired = 0
for f in latin_files:
    s = str(f)
    cands = [
        s.replace("\\interslavic\\", "\\interslavic-cyrillic\\").replace("_Interslavic_", "_Interslavic_Cyrillic_"),
        s.replace("\\interslavic\\", "\\interslavic-cyrillic\\"),
    ]
    if any(Path(c).exists() for c in cands):
        paired += 1
    else:
        missing.append(str(f.relative_to(T)))

kolc = kolc_cyr = 0
seen = set()
for f in T.rglob("*.tex"):
    s = str(f).lower()
    if "interslavic" not in s:
        continue
    txt = f.read_text(encoding="utf-8", errors="replace")
    h = hash(txt)
    if h in seen:
        continue
    seen.add(h)
    if "cyrillic" in s:
        kolc_cyr += len(re.findall(r"колц", txt, re.IGNORECASE))
    else:
        kolc += len(re.findall(r"kolc", txt, re.IGNORECASE))

out = {
    "artifact": "cyrillic_sync_check_v1",
    "generated": "2026-07-04",
    "latin_files": len(latin_files),
    "with_cyrillic_sibling": paired,
    "missing_cyrillic_sibling": len(missing),
    "missing_list_first_40": missing[:40],
    "kolc_latin_total": kolc,
    "kolc_cyrillic_total": kolc_cyr,
    "note": "sibling matching is path-heuristic (two candidate patterns); misses may include naming variants — "
            "treat the missing list as a triage queue, not verdicts. kolc totals include working files (dedup by content).",
}
(OUT / "CYRILLIC_SYNC_CHECK_v1_20260704.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"latin files {len(latin_files)} | paired {paired} | missing sibling {len(missing)}")
print(f"kolc latin {kolc} vs колц cyrillic {kolc_cyr}")
for m in missing[:12]:
    print("  MISSING:", m)
