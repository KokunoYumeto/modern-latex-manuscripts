# Macedonian column probe: core-spine concepts against the cached UKIM lexicon text.
# Handles the legacy font transliteration (~ = č, { = š, ` = ž) alongside Cyrillic.
# Output: mk column data for the marker table (dictionary-grade witnesses).
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
TXT = BASE / "shelves" / "underrepresented_slavic" / "macedonian" / "macedonian_ukim_math_lexicon.txt"

text = TXT.read_text(encoding="utf-8")
low = text.lower()

# concept -> mk candidate surfaces (legacy-Latin and/or Cyrillic as they appear in this PDF)
PROBES = {
    "ring": ["prsten"],
    "field": ["pole "],
    "group": ["grupa"],
    "ideal": ["ideal"],
    "module": ["modul"],
    "matrix": ["matrica", "матрица"],
    "determinant": ["determinanta", "детерминанта"],
    "polynomial": ["polinom"],
    "theorem": ["teorema", "теорема"],
    "lemma": ["lema"],
    "definition": ["definicija"],
    "proof": ["dokaz"],
    "set": ["mno`estvo"],
    "element": ["element"],
    "subset": ["podmno`estvo"],
    "homomorphism": ["homomorfizam"],
    "isomorphism": ["izomorfizam"],
    "automorphism": ["avtomorfizam"],
    "quotient": ["koli~nik"],
    "quotient field": ["pole na koli~nici", "koli~ni~ko pole"],
    "vector": ["vektor"],
    "basis": ["baza"],
    "dimension": ["dimenzija"],
    "kernel": ["jadro"],
    "norm": ["norma"],
    "trace": ["traga"],
    "extension (field)": ["ra{iruvawe", "pro{iruvawe"],
    "invariant": ["invarijanta"],
    "splitting field": ["pole na razlo`uvawe", "razlo`uvawe"],
    "noetherian": ["neterov", "noetherov"],
    "prime ideal": ["prost ideal"],
    "eigenvalue": ["sopstvena vrednost"],
    "equation": ["ravenka"],
    "function": ["funkcija"],
    "root": ["koren"],
    "degree": ["stepen"],
    "power-exponent": ["stepen"],
    "divisible": ["deliv"],
    "algebra (structure)": ["algebra"],
    "tensor product": ["tenzorski proizvod"],
    "direct sum": ["direktna suma"],
    "normal subgroup": ["normalna podgrupa"],
    "subgroup": ["podgrupa"],
}

rows = {}
found = 0
for concept, cands in PROBES.items():
    best = None
    for c in cands:
        n = low.count(c.lower())
        if n and (best is None or n > best[1]):
            best = (c.strip(), n)
    if best:
        found += 1
        i = low.find(best[0].lower())
        ctx = " ".join(text[max(0, i-50):i+130].split())
        rows[concept] = {"mk_form_as_encoded": best[0], "count": best[1], "context": ctx,
                         "witness_level": "concept_shelf (dictionary-grade native lexicon)",
                         "source": "macedonian_ukim_math_lexicon.pdf"}
    else:
        rows[concept] = {"mk_form_as_encoded": None, "count": 0,
                         "note": "no candidate hit — needs manual lexicon lookup (candidates were guesses)"}

out = {
    "artifact": "mk_column_probe_v1",
    "generated": "2026-07-04",
    "boundary": "dictionary-grade native witnesses at concept-shelf level; legacy-font forms need one decode pass "
                "(~=č {=š `=ž w=nj?) before entering the marker table as clean Cyrillic lemmas; counts are surface counts",
    "concepts_probed": len(PROBES),
    "concepts_with_hits": found,
    "rows": rows,
}
(BASE / "MK_COLUMN_PROBE_v1_20260704.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"mk probe: {found}/{len(PROBES)} concepts hit")
for k, v in rows.items():
    if v["count"]:
        print(f"  {k:22s} {v['mk_form_as_encoded']:24s} {v['count']}")
