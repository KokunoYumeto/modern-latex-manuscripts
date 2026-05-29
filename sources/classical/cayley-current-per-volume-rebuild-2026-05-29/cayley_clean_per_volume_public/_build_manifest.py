import csv, json, hashlib
from pathlib import Path

OUT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
inv = json.loads((OUT / "_inventory.json").read_text(encoding="utf-8"))

ROMAN_PRETTY = {"vol00":"Front Matter","vol01":"Vol. I","vol02":"Vol. II","vol03":"Vol. III",
                "vol04":"Vol. IV","vol05":"Vol. V","vol06":"Vol. VI","vol07":"Vol. VII",
                "vol09":"Vol. IX","vol10":"Vol. X","vol11":"Vol. XI","vol12":"Vol. XII",
                "vol13":"Vol. XIII"}
ROMAN_LABEL = {"vol00":"Front_Matter","vol01":"Vol_I","vol02":"Vol_II","vol03":"Vol_III",
               "vol04":"Vol_IV","vol05":"Vol_V","vol06":"Vol_VI","vol07":"Vol_VII",
               "vol09":"Vol_IX","vol10":"Vol_X","vol11":"Vol_XI","vol12":"Vol_XII",
               "vol13":"Vol_XIII"}

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

from pypdf import PdfReader
rows = []
for vol, info in sorted(inv.items()):
    label = ROMAN_LABEL[vol]
    pretty = ROMAN_PRETTY[vol]
    pdf = OUT / f"Cayley_Collected_Mathematical_Papers_{label}.pdf"
    tex = OUT / f"Cayley_Collected_Mathematical_Papers_{label}.tex"
    sources_dir = OUT / f"sources_tex_{label}"
    pdf_pages = len(PdfReader(str(pdf)).pages) if pdf.exists() else 0
    pdf_bytes = pdf.stat().st_size if pdf.exists() else 0
    tex_bytes = tex.stat().st_size if tex.exists() else 0
    chunk_files = sorted(sources_dir.glob("*.tex")) if sources_dir.exists() else []
    rows.append({
        "label": pretty,
        "pdf_filename": pdf.name,
        "pdf_pages": pdf_pages,
        "pdf_bytes": pdf_bytes,
        "pdf_sha256": sha256(pdf) if pdf.exists() else "",
        "master_tex_filename": tex.name,
        "master_tex_bytes": tex_bytes,
        "source_chunks_dir": sources_dir.name,
        "source_chunks_count": len(chunk_files),
        "chunks_first_page": info["chunks"][0]["start"] if info["chunks"] else 0,
        "chunks_last_page": info["chunks"][-1]["end"] if info["chunks"] else 0,
        "missing_internal_ranges": "; ".join(info["missing_ranges"]) or "none",
    })

# Vol VIII: source scan placeholder available; modern LaTeX typesetting in progress
viii_pdf = OUT / "Cayley_Collected_Mathematical_Papers_Vol_VIII_source_scan.pdf"
viii_tex_dir = OUT / "sources_tex_Vol_VIII"
viii_pages = len(PdfReader(str(viii_pdf)).pages) if viii_pdf.exists() else 0
viii_tex_count = len(list(viii_tex_dir.glob("*.tex"))) if viii_tex_dir.exists() else 0
rows.append({
    "label": "Vol. VIII (source scan placeholder)",
    "pdf_filename": viii_pdf.name if viii_pdf.exists() else "(not produced)",
    "pdf_pages": viii_pages,
    "pdf_bytes": viii_pdf.stat().st_size if viii_pdf.exists() else 0,
    "pdf_sha256": sha256(viii_pdf) if viii_pdf.exists() else "",
    "master_tex_filename": "(modern LaTeX typesetting in progress)",
    "master_tex_bytes": 0,
    "source_chunks_dir": "sources_tex_Vol_VIII" if viii_tex_dir.exists() else "(none yet)",
    "source_chunks_count": viii_tex_count,
    "chunks_first_page": 0,
    "chunks_last_page": 0,
    "missing_internal_ranges": "PLACEHOLDER: source scan only; modern LaTeX typesetting underway via direct-from-image pipeline",
})

with open(OUT / "MANIFEST.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

(OUT / "MANIFEST.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")

total_pages = sum(r["pdf_pages"] for r in rows)
total_bytes = sum(r["pdf_bytes"] for r in rows)
print(f"Manifest written: {len(rows)} entries, {total_pages:,} total pages, "
      f"{total_bytes/1024/1024:.1f} MB total")
