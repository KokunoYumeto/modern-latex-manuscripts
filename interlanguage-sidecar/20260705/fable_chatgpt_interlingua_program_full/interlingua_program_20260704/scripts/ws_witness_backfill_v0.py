# W/S Slavic witness backfill v0 — search the LOCAL 20-source triangulation shelf
# (extracted text) for branch forms of priority concepts. Classification only:
# each hit is typed support (cognate of ISV choice) or competitor (different lexeme).
# No wording changes, no promotions. Output carries counts + file pointers.
import json
import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SHELF = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\interslavic_triangulation\20260624_slavic_math_reference\text")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

# language from filename prefix
def lang_of(name):
    for p, l in (("czech", "cs"), ("polish", "pl"), ("slovak", "sk"), ("slovenian", "sl"),
                 ("croatian", "hr"), ("serbian", "sr"), ("bulgarian", "bg")):
        if name.lower().startswith(p):
            return l
    return "??"

BRANCH = {"cs": "west", "pl": "west", "sk": "west", "sl": "south", "hr": "south", "sr": "south", "bg": "south"}

# Priority concepts: ISV chosen form + branch candidate forms (stems, lowercase).
# support = same lexeme family as ISV choice; everything else found = competitor.
# Stems chosen to catch inflections; word-boundary-left anchored.
CONCEPTS = {
    "ring": {"isv": "kolco", "support_stems": ["kolc", "kolec"],
             "candidates": {"okruh": "cs/sk okruh", "pierścien": "pl pierścień", "pierscien": "pl (ascii)",
                            "prsten": "hr/sr prsten", "kolobar": "sl kolobar", "пръстен": "bg prăsten"}},
    "field": {"isv": "polje", "support_stems": ["polj", "pole", "поле"],
              "candidates": {"ciał": "pl ciało(field)", "cial": "pl (ascii)", "těles": "cs těleso", "teles": "cs/sk (ascii)",
                             "obseg": "sl obseg", "поле": "bg pole"}},
    "division ring / body": {"isv": "tělo", "support_stems": ["těl", "tel", "tijel", "тял"],
              "candidates": {"nekomutativ": "noncommutative marker", "tijel": "hr tijelo", "тяло": "bg tjalo",
                             "ciał": "pl ciało(niepr.)", "těles": "cs těleso"}},
    "ideal": {"isv": "ideal", "support_stems": ["ideal", "ideál", "ideał", "идеал"], "candidates": {}},
    "module": {"isv": "modul", "support_stems": ["modul", "moduł", "модул"], "candidates": {}},
    "group": {"isv": "grupa", "support_stems": ["grup", "груп"], "candidates": {}},
    "noetherian": {"isv": "noetherov", "support_stems": ["noether", "нётер", "ньотер", "нетер"],
              "candidates": {"noetherski": "sl noetherski", "noetherowsk": "pl noetherowski", "noetherovsk": "cs noetherovský"}},
    "homomorphism": {"isv": "homomorfizm", "support_stems": ["homomorf", "хомоморф", "homomorph"], "candidates": {}},
    "idempotent": {"isv": "idempotent", "support_stems": ["idempotent", "идемпотент"], "candidates": {}},
    "splitting field": {"isv": "razpadno polje", "support_stems": ["razpad", "razkla", "распад"],
              "candidates": {"rozklad": "cs/pl rozklad- family", "rozkład": "pl rozkład"}},
    "determinant": {"isv": "determinanta", "support_stems": ["determinant", "детерминант"],
              "candidates": {"wyznacznik": "pl wyznacznik"}},
    "polynomial": {"isv": "polinom", "support_stems": ["polynom", "polinom", "полином"],
              "candidates": {"wielomian": "pl wielomian", "mnohočlen": "cs mnohočlen", "mnohoclen": "cs (ascii)"}},
    "basis": {"isv": "baza", "support_stems": ["baz", "báz", "базис", "база"], "candidates": {}},
    "invariant": {"isv": "invariant", "support_stems": ["invariant", "inwariant", "invarijant", "инвариант"], "candidates": {}},
    "quotient field": {"isv": "polje častnikov?", "support_stems": [],
              "candidates": {"podílov": "cs podílové těleso", "podilov": "cs (ascii)", "ułamk": "pl ciało ułamków", "ulamk": "pl (ascii)"}},
    # --- v1 extension: proof-grammar + curriculum layer -------------------
    "theorem": {"isv": "teorema", "support_stems": ["teorem", "теорем"],
              "candidates": {"věta": "cs věta", "veta": "cs/sk (ascii)", "twierdzeni": "pl twierdzenie"}},
    "proof": {"isv": "dokaz", "support_stems": ["dokaz", "доказ"],
              "candidates": {"důkaz": "cs důkaz", "dukaz": "cs (ascii)", "dowód": "pl dowód", "dowod": "pl (ascii)"}},
    "lemma": {"isv": "lema", "support_stems": ["lemma", "lema", "лема"],
              "candidates": {"lemat": "pl lemat"}},
    "corollary": {"isv": "korolar?", "support_stems": ["korolar"],
              "candidates": {"důsledek": "cs důsledek", "dusledek": "cs (ascii)", "wniosek": "pl wniosek", "posljedic": "hr posljedica", "следстви": "bg sledstvie"}},
    "definition": {"isv": "definicija", "support_stems": ["definic", "definicj", "дефиниц"], "candidates": {}},
    "example": {"isv": "priklad?", "support_stems": ["příklad", "priklad", "przykład", "przyklad", "primjer", "пример"], "candidates": {}},
    "set": {"isv": "množstvo?", "support_stems": ["množ", "mnoz", "множеств"],
              "candidates": {"zbiór": "pl zbiór", "zbior": "pl (ascii)", "skup": "hr/sr skup"}},
    "element": {"isv": "element", "support_stems": ["element", "елемент"],
              "candidates": {"prvek": "cs prvek", "prvk": "cs (infl)"}},
    "subset": {"isv": "podmnožstvo?", "support_stems": ["podmnož", "podmnoz", "подмножеств"],
              "candidates": {"podzbiór": "pl podzbiór", "podzbior": "pl (ascii)", "podskup": "hr/sr podskup"}},
    "isomorphism": {"isv": "izomorfizm", "support_stems": ["izomorf", "isomorf", "изоморф"], "candidates": {}},
    "automorphism": {"isv": "avtomorfizm", "support_stems": ["automorf", "avtomorf", "автоморф"], "candidates": {}},
    "representation": {"isv": "predstavjenje?", "support_stems": ["reprezentac", "представ", "predstav"],
              "candidates": {"przedstawieni": "pl przedstawienie", "zobrazení": "cs zobrazení(map!)"}},
    "matrix": {"isv": "matrica", "support_stems": ["matric", "матриц", "macierz"],
              "candidates": {"matice": "cs matice"}},
    "vector": {"isv": "vektor", "support_stems": ["vektor", "wektor", "вектор"], "candidates": {}},
    "dimension": {"isv": "dimenzija", "support_stems": ["dimenz", "dimensi", "димензи", "измерени"],
              "candidates": {"wymiar": "pl wymiar", "rozměr": "cs rozměr", "rozmer": "cs/sk (ascii)", "размерност": "bg razmernost"}},
    "kernel": {"isv": "jadro", "support_stems": ["jádr", "jadr", "jądr", "jadr", "ядр"], "candidates": {}},
    "trace": {"isv": "sled?", "support_stems": ["след"],
              "candidates": {"stopa": "cs/pl stopa", "ślad": "pl ślad", "slad": "pl (ascii)", "trag": "hr/sr trag"}},
    "norm": {"isv": "norma", "support_stems": ["norm", "норм"], "candidates": {}},
    "center": {"isv": "centr", "support_stems": ["centr", "центр", "център"],
              "candidates": {"střed": "cs střed", "stred": "cs/sk (ascii)", "środek": "pl środek", "srodek": "pl (ascii)", "središt": "hr središte"}},
    "extension (field)": {"isv": "razširjenje?", "support_stems": ["razšir", "razsir", "разшир"],
              "candidates": {"rozšířen": "cs rozšíření", "rozsiren": "cs/sk (ascii)", "rozszerzeni": "pl rozszerzenie", "proširenj": "hr proširenje"}},
    "prime ideal": {"isv": "prosty ideal?", "support_stems": ["prost"],
              "candidates": {"prvoideál": "cs prvoideál", "prvoideal": "cs (ascii)", "pierwszy": "pl ideał pierwszy", "прост идеал": "bg prost ideal"}},
    "algebra (structure)": {"isv": "algebra", "support_stems": ["algebr", "алгебр"], "candidates": {}},
}

def nfc(s):
    return unicodedata.normalize("NFC", s)

files = sorted(SHELF.glob("*.txt"))
texts = {}
for f in files:
    try:
        texts[f.name] = nfc(f.read_text(encoding="utf-8", errors="replace").lower())
    except Exception:
        pass

results = {}
branch_presence = defaultdict(lambda: defaultdict(set))  # concept -> branch -> set(kind)
for cname, spec in CONCEPTS.items():
    hits = []
    stems = [(s, "support") for s in spec["support_stems"]] + \
            [(s, "competitor") for s in spec["candidates"]]
    for fname, text in texts.items():
        lg = lang_of(fname)
        for stem, kind in stems:
            stem_n = nfc(stem.lower())
            n = len(re.findall(r"(?<![\wа-яёіїє])" + re.escape(stem_n), text))
            if n:
                label = spec["candidates"].get(stem, "cognate of ISV form") if kind == "competitor" else "cognate of ISV form"
                hits.append({"file": fname, "lang": lg, "branch": BRANCH.get(lg, "?"),
                             "stem": stem, "kind": kind, "count": n, "note": label})
                branch_presence[cname][BRANCH.get(lg, "?")].add(kind)
    results[cname] = {
        "isv_choice": spec["isv"],
        "hits": hits,
        "branch_summary": {b: sorted(k) for b, k in branch_presence[cname].items()},
    }

summary_lines = []
for cname, r in results.items():
    bs = r["branch_summary"]
    def tag(b):
        ks = bs.get(b, [])
        if "support" in ks and "competitor" in ks: return "support+competitor"
        if "support" in ks: return "support"
        if "competitor" in ks: return "COMPETITOR-ONLY"
        return "no-hit"
    summary_lines.append((cname, r["isv_choice"], tag("west"), tag("south")))

out = {
    "artifact": "ws_witness_backfill_v0",
    "generated": "2026-07-04",
    "shelf": str(SHELF),
    "files_searched": list(texts.keys()),
    "boundary": "mechanical stem search; support/competitor typing by lexeme family; hits are FORM attestations "
                "needing context review before use as concept witnesses; no promotions",
    "concepts": results,
}
(OUT / "WS_WITNESS_BACKFILL_v0_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# W/S Witness Backfill v0 — local shelf search", "",
      f"2026-07-04. Searched {len(texts)} extracted texts of the 20-source triangulation shelf (already on disk — no new collection). "
      "Hits are form attestations, typed support (cognate of the ISV choice) vs competitor (different lexeme). Context review still required.",
      "", "| Concept | ISV choice | West branch | South branch |", "| --- | --- | --- | --- |"]
for cname, isv, w, s in summary_lines:
    md.append(f"| {cname} | {isv} | {w} | {s} |")
md += ["", "Full hits with file pointers in the json. COMPETITOR-ONLY rows are the review agenda."]
(OUT / "WS_WITNESS_BACKFILL_v0_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"files searched: {len(texts)}")
for cname, isv, w, s in summary_lines:
    print(f"  {cname:24s} isv={isv:18s} west={w:22s} south={s}")
