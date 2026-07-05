# Extract text from the Macedonian lexicon + Sorbian terminology PDFs and probe
# ring + core-spine rows. Extracted text cached to shelf; classification only.
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import fitz

SHELF = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704\shelves\underrepresented_slavic")

TARGETS = {
    "mk": SHELF / "macedonian" / "macedonian_ukim_math_lexicon.pdf",
    "hsb_2008": SHELF / "sorbian_upper" / "sorbian_domowina_math_terminology_2008.pdf",
    "hsb_1996": SHELF / "sorbian_upper" / "sorbian_institute_text_corpus_termmat_1996.pdf",
}
PROBES = {
    "mk": ["прстен", "поле", "идеал", "група", "теорема", "полином", "матрица", "детерминанта", "количник"],
    "hsb_2008": ["kruh", "rink", "ćěleso", "polo", "ideal", "skupina", "wobłuk", "梁", "koło", "cyłk"],
    "hsb_1996": ["kruh", "rink", "ćěleso", "polo", "ideal", "skupina", "koło"],
}

for key, pdf in TARGETS.items():
    if not pdf.exists():
        print(f"{key}: MISSING {pdf.name}")
        continue
    try:
        doc = fitz.open(pdf)
        txt = "\n".join(page.get_text() for page in doc)
        doc.close()
    except Exception as ex:
        print(f"{key}: extraction failed: {ex}")
        continue
    out = pdf.with_suffix(".txt")
    out.write_text(txt, encoding="utf-8")
    low = txt.lower()
    print(f"== {key}: {pdf.name} | pages-extracted chars {len(txt):,}")
    for p in PROBES[key]:
        n = low.count(p.lower())
        if n:
            i = low.find(p.lower())
            ctx = " ".join(txt[max(0, i-60):i+120].split())
            print(f"   {p}: {n}  | …{ctx}…")
