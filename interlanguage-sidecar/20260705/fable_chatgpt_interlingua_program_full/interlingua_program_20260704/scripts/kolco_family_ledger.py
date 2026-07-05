# KOLCO family internal-consistency ledger + quotient-field internal audit.
# Scans local Interslavic Latin translation TeX (v001 trees); classification only.
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
T = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\translations")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

KOLC = re.compile(r"\b(\w*kolc\w*)", re.IGNORECASE)
PRSTEN = re.compile(r"\b(\w*prsten\w*)", re.IGNORECASE)
# quotient-field candidates in ISV/uk/ru layers
QF = {
    "isv_castnik": re.compile(r"polje\s+častnik\w*|častnik\w*", re.IGNORECASE),
    "isv_ulomk": re.compile(r"ulomk\w*", re.IGNORECASE),
    "isv_quotient": re.compile(r"kvocient\w*|quotient\w*", re.IGNORECASE),
    "isv_polje_castnyh": re.compile(r"polje\s+častn\w*", re.IGNORECASE),
}

def paper_of(p):
    m = re.search(r"(paper\d+|endmatter)", str(p))
    return m.group(1) if m else "?"

kolco_terms = Counter()
kolco_by_paper = defaultdict(Counter)
prsten_hits = []
qf_hits = defaultdict(list)
seen_content = set()
files = 0
for f in T.rglob("*.tex"):
    s = str(f)
    if "interslavic" not in s or "cyrillic" in s:
        continue
    try:
        txt = f.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    h = hash(txt)
    if h in seen_content:
        continue
    seen_content.add(h)
    files += 1
    pp = paper_of(f)
    for m in KOLC.finditer(txt):
        w = m.group(1).lower()
        kolco_terms[w] += 1
        kolco_by_paper[pp][w] += 1
    for m in PRSTEN.finditer(txt):
        line = txt[:m.start()].count("\n") + 1
        prsten_hits.append({"paper": pp, "file": f.name, "line": line, "form": m.group(1)})
    for key, rx in QF.items():
        for m in rx.finditer(txt):
            if len(qf_hits[key]) < 12:
                line = txt[:m.start()].count("\n") + 1
                ctx = txt[max(0, m.start()-60):m.end()+60].replace("\n", " ")
                qf_hits[key].append({"paper": pp, "file": f.name, "line": line, "ctx": ctx.strip()})

out = {
    "artifact": "kolco_family_internal_consistency_ledger_v1",
    "generated": "2026-07-04",
    "boundary": "internal-consistency evidence from the corpus's own TeX (generated corpus); NOT witness material",
    "files_scanned_dedup": files,
    "kolco_distinct_forms": len(kolco_terms),
    "kolco_total_occurrences": sum(kolco_terms.values()),
    "kolco_form_counts": dict(kolco_terms.most_common()),
    "papers_with_kolco": len(kolco_by_paper),
    "prsten_occurrences": prsten_hits,
    "quotient_field_candidates": {k: v for k, v in qf_hits.items()},
}
(OUT / "KOLCO_FAMILY_INTERNAL_CONSISTENCY_LEDGER_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Kolco-Family Internal Consistency Ledger + Quotient-Field Internal Audit", "",
      "2026-07-04. Corpus's own Latin-script TeX (deduplicated). Internal-consistency evidence only — not witnesses.",
      "",
      f"- Files scanned (dedup): {files}; kolc* total {sum(kolco_terms.values())} across {len(kolco_terms)} distinct forms in {len(kolco_by_paper)} papers.",
      f"- prsten* occurrences: {len(prsten_hits)} — " + "; ".join(f"{h['paper']} L{h['line']} ({h['form']})" for h in prsten_hits[:6]),
      "", "## Top kolc* forms (compound inventory)", ""]
for w, n in kolco_terms.most_common(25):
    md.append(f"- {n:5d}  {w}")
md += ["", "## Quotient-field internal usage", ""]
for k, hits in qf_hits.items():
    md.append(f"### {k} — {len(hits)} sampled hits")
    for h in hits[:5]:
        md.append(f"- {h['paper']} L{h['line']}: …{h['ctx'][:120]}…")
(OUT / "KOLCO_FAMILY_INTERNAL_CONSISTENCY_LEDGER_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"files {files} | kolc* {sum(kolco_terms.values())} occ / {len(kolco_terms)} forms / {len(kolco_by_paper)} papers | prsten {len(prsten_hits)}")
print("QF candidate hits:", {k: len(v) for k, v in qf_hits.items()})
