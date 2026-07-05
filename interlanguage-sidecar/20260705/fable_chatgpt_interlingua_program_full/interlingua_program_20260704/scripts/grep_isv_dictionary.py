# Search the community word list for ring-related entries. Read-only.
import csv
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704\data\isv_words_list.csv")

EXCLUDE = ("during", "string", "bring", "spring", "herring", "ringing", "hiring",
           "airing", "wiring", "tiring", "boring", "roaring", "gathering", "offering",
           "suffering", "watering", "shattering", "murmuring", "stirring")

with p.open(encoding="utf-8") as f:
    rd = csv.reader(f)
    hdr = next(rd)
    print("COLUMNS:", hdr[:22])
    idx = {c: hdr.index(c) for c in hdr}
    langs = [c for c in ("ru", "uk", "pl", "cs", "sk", "bg", "sr", "hr", "sl") if c in idx]
    for row in rd:
        if len(row) < len(hdr) - 4:
            continue
        isv = row[idx.get("isv", 1)]
        en = row[idx.get("en", 5)]
        enl = en.lower()
        hit_en = "ring" in enl and not any(x in enl for x in EXCLUDE)
        hit_isv = isv.lower().replace("ó", "o").startswith(("kolc", "prsten", "persten", "obruč", "obruc", "kolobar"))
        if hit_en or hit_isv:
            cells = [f"{lg}={row[idx[lg]]}" for lg in langs if row[idx[lg]].strip()]
            print(f"ISV: {isv:20s} EN: {en:40s} " + " ".join(cells)[:160])
