import json, re, subprocess
from pathlib import Path
from collections import Counter

OUT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
inv = json.loads((OUT / "_inventory.json").read_text(encoding="utf-8"))
PDFTOTEXT = r"local workspace\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe"

cmds = ("frac|partial|delta|psi|phi|displaystyle|ldots|text|begin|end|cdot|"
        "sqrt|sum|int|sigma|alpha|beta|gamma|theta|lambda|mu|nu|rho|tau|"
        "omega|infty|pi|cos|sin|log|left|right|raisebox|scriptstyle")
LEAK = re.compile(r"\\(" + cmds + r")\b")

# Also: count chunks in BOTH 50-page and 52-page series so we can pick the cleaner one
source system_VOL04_DIR = Path(r"local workspace\Documents\Papors\Chatnotes\CHat translates and clean\source system\source system 7\source system 7\latex_typesetting_CONTINUED_WORK\cayley\vol04")

results = {}
swap_candidates = []  # chunks where alt series might be cleaner

for vol, info in sorted(inv.items()):
    chunks = info["chunks"]
    vol_results = []
    for c in chunks:
        pdf = c["pdf_path"]
        if not pdf:
            vol_results.append({"chunk": c["name"], "pdf": None, "leaks": "n/a"})
            continue
        try:
            txt = subprocess.run([PDFTOTEXT, pdf, "-"], capture_output=True, text=True,
                                 errors="replace", timeout=60).stdout
            leaks = LEAK.findall(txt)
            vol_results.append({
                "chunk": c["name"], "pdf": pdf, "leaks": len(leaks),
                "top_leaks": Counter(leaks).most_common(5) if leaks else [],
                "pages": f"{c['start']}-{c['end']}",
            })
            # If this chunk has many leaks, look for an alternative chunk in same vol
            # with overlapping pages but different span
            if len(leaks) > 50:
                alt_dir = Path(pdf).parent
                for alt_pdf in alt_dir.glob("cayley_*_pages_*.pdf"):
                    if alt_pdf.name == Path(pdf).name:
                        continue
                    m = re.match(r"cayley_(vol\d+)_pages_(\d+)_(\d+)\.pdf$", alt_pdf.name)
                    if not m:
                        continue
                    a_start, a_end = int(m.group(2)), int(m.group(3))
                    # Overlapping pages
                    if a_start <= c["start"] <= a_end or c["start"] <= a_start <= c["end"]:
                        try:
                            atxt = subprocess.run([PDFTOTEXT, str(alt_pdf), "-"],
                                                  capture_output=True, text=True,
                                                  errors="replace", timeout=60).stdout
                            aleaks = LEAK.findall(atxt)
                            if len(aleaks) < len(leaks):
                                swap_candidates.append({
                                    "vol": vol, "current_chunk": c["name"],
                                    "current_leaks": len(leaks),
                                    "alt_chunk": alt_pdf.name, "alt_leaks": len(aleaks),
                                    "alt_path": str(alt_pdf.with_suffix(".tex")),
                                    "alt_pdf_path": str(alt_pdf),
                                    "alt_start": a_start, "alt_end": a_end,
                                })
                        except Exception:
                            pass
        except Exception as e:
            vol_results.append({"chunk": c["name"], "pdf": pdf, "leaks": "err", "err": str(e)})
    results[vol] = vol_results

(OUT / "_chunk_leak_audit.json").write_text(
    json.dumps({"per_chunk": results, "swap_candidates": swap_candidates}, indent=2),
    encoding="utf-8")

print("=== Bad chunks (>10 leaks) ===")
bad = []
for vol, recs in results.items():
    for r in recs:
        if isinstance(r["leaks"], int) and r["leaks"] > 10:
            print(f"  {vol}: {r['chunk']}: {r['leaks']} leaks, top: {r['top_leaks']}")
            bad.append((vol, r["chunk"], r["leaks"]))

print(f"\nTotal bad chunks: {len(bad)}")
print(f"Swap candidates found: {len(swap_candidates)}")
for s in swap_candidates:
    print(f"  {s['vol']} {s['current_chunk']} ({s['current_leaks']}) -> {s['alt_chunk']} ({s['alt_leaks']})")
