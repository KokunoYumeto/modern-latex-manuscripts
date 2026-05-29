import json
from pathlib import Path
from pypdf import PdfWriter, PdfReader

OUT = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
inv = json.loads((OUT / "_inventory.json").read_text(encoding="utf-8"))

ROMAN = {"vol00":"Front Matter","vol01":"Vol I","vol02":"Vol II","vol03":"Vol III",
         "vol04":"Vol IV","vol05":"Vol V","vol06":"Vol VI","vol07":"Vol VII",
         "vol08":"Vol VIII","vol09":"Vol IX","vol10":"Vol X","vol11":"Vol XI",
         "vol12":"Vol XII","vol13":"Vol XIII"}

results = []
for vol, info in sorted(inv.items()):
    chunks = info["chunks"]
    if not chunks:
        continue
    out_pdf = OUT / f"Cayley_Collected_Mathematical_Papers_{ROMAN[vol].replace(' ','_')}.pdf"
    writer = PdfWriter()
    total_pages = 0
    missing_pdfs = []
    for c in chunks:
        if not c["pdf_path"]:
            missing_pdfs.append(c["name"])
            continue
        try:
            reader = PdfReader(c["pdf_path"])
            for page in reader.pages:
                writer.add_page(page)
            # Add bookmark for chunk
            writer.add_outline_item(
                f"Pages {c['start']}-{c['end']}",
                total_pages
            )
            total_pages += len(reader.pages)
        except Exception as e:
            missing_pdfs.append(f"{c['name']}: {e}")
    with open(out_pdf, "wb") as f:
        writer.write(f)
    results.append({
        "vol": vol, "label": ROMAN[vol],
        "pdf": str(out_pdf), "pages": total_pages,
        "chunks": len(chunks), "missing_pdfs": missing_pdfs,
        "missing_page_ranges": info["missing_ranges"],
    })
    print(f"  {vol} -> {out_pdf.name}: {total_pages} pages from {len(chunks)} chunks"
          + (f" (missing: {missing_pdfs})" if missing_pdfs else ""))

(OUT / "_merge_summary.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
print(f"\nWrote summary to _merge_summary.json")
