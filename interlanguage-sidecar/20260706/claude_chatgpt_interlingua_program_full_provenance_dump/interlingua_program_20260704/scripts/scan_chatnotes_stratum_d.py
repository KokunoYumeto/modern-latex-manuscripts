# Stratum-D scan: per-folder file counts, sizes, and filename-detected language tags
# for the Chatnotes bilingual/aid corpus. Read-only.
import json
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
root = Path(r"C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

LANG = {"_de": "de", "german": "de", "_en": "en", "english": "en", "_fr": "fr", "french": "fr",
        "_es": "es", "spanish": "es", "_ja": "ja", "japanese": "ja", "_uk": "uk", "ukrain": "uk",
        "_ru": "ru", "russian": "ru", "_isv": "isv", "interslav": "isv", "_zh": "zh", "chinese": "zh",
        "_ar": "ar", "arabic": "ar", "sanskrit": "sa", "_it": "it", "_pt": "pt", "latin": "la"}

inv = {}
for d in sorted(root.iterdir()):
    if not d.is_dir():
        continue
    files = [f for f in d.rglob("*") if f.is_file()]
    langs = Counter()
    for f in files:
        n = f.name.lower()
        for pat, lg in LANG.items():
            if pat in n:
                langs[lg] += 1
    exts = Counter(f.suffix.lower() for f in files)
    inv[d.name] = {"files": len(files), "mb": round(sum(f.stat().st_size for f in files) / 1e6, 1),
                   "langs": dict(langs.most_common(8)),
                   "tex": exts.get(".tex", 0), "pdf": exts.get(".pdf", 0), "md": exts.get(".md", 0)}

(OUT / "chatnotes_stratum_d_scan_20260704.json").write_text(
    json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")

for name, v in sorted(inv.items(), key=lambda kv: -kv[1]["files"])[:40]:
    print("{:5d}f {:8.1f}MB tex{:4d} pdf{:4d} | {:44s} | {}".format(
        v["files"], v["mb"], v["tex"], v["pdf"], name[:44], v["langs"]))
print("TOTAL files:", sum(v["files"] for v in inv.values()),
      "MB:", round(sum(v["mb"] for v in inv.values()), 1))
