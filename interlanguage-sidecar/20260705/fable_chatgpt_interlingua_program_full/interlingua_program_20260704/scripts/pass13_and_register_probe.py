# Insertion pass 13 + register-row W/S shelf probe (branch evidence for REGISTER lemmas).
# The probe is the weighting-coupling step: register vocabulary gets the same
# support/competitor typing as concept rows. Classification only.
import json
import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
SHELF = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\interslavic_triangulation\20260624_slavic_math_reference\text")

# --- pass 13 lexicon ---
lex = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
NEW = [
    {"id": "reduce-to", "lemma": "svesti", "en": "reduce to; bring back to", "class": "proof_operation",
     "variants": ["svesti", "svodi", "svedeno", "svede"]},
    {"id": "appears-pojaviti", "lemma": "pojaviti se", "en": "appears; shows up", "class": "sequence_predicate",
     "variants": ["pojavja", "pojavi", "pojavjaje"]},
    {"id": "form-shape", "lemma": "oblik", "en": "form; shape", "class": "math_general",
     "variants": ["oblik", "obliku", "oblika", "oblici"]},
    {"id": "curve", "lemma": "kriva", "en": "curve", "class": "math_general",
     "variants": ["kriva", "krive", "krivoj", "krivyh"]},
    {"id": "essence", "lemma": "bytnost", "en": "essence; essential nature", "class": "discourse_noun",
     "variants": ["bytnost", "bytnosti"]},
    {"id": "unknown-quantity", "lemma": "neizvěstna", "en": "unknown (quantity)", "class": "math_general",
     "variants": ["neizvěstn", "neizvestn", "neznam"]},
    {"id": "preceding", "lemma": "prědhodny", "en": "preceding; previous", "class": "proof_reference",
     "variants": ["prědhodn", "predhodn", "prědydu", "predydu"]},
]
for n in NEW:
    n.update({"provenance": ["fable_pass13"], "status": "proposed_internal_insert; needs linguistic review",
              "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35})
    lex["entries"].append(n)
for e in lex["entries"]:
    if e["lemma"].startswith("dopuščati"):
        e["variants"] = sorted(set(e["variants"]) | {"dopuskaje", "dopuska"})
lex["entry_count"] = len(lex["entries"])
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
print("pass13 lexicon:", len(lex["entries"]))

# --- register-row W/S probe ---
def lang_of(name):
    for p, l in (("czech", "cs"), ("polish", "pl"), ("slovak", "sk"), ("slovenian", "sl"),
                 ("croatian", "hr"), ("serbian", "sr"), ("bulgarian", "bg")):
        if name.lower().startswith(p):
            return l
    return "??"
BRANCH = {"cs": "west", "pl": "west", "sk": "west", "sl": "south", "hr": "south", "sr": "south", "bg": "south"}

REGISTER = {
    "nehaj (let/suppose)": {"isv": "nehaj", "support": ["neha"],
        "candidates": {"nechť": "cs nechť", "necht": "cs (ascii)", "nech ": "sk nech", "niech": "pl niech",
                       "neka ": "hr/sr neka", "naj ": "sl naj", "нека": "bg neka"}},
    "poněže (since/because)": {"isv": "poněže", "support": ["poněž", "ponež", "понеже"],
        "candidates": {"protože": "cs protože", "protoze": "cs (ascii)", "ponieważ": "pl ponieważ",
                       "poniewaz": "pl (ascii)", "budući": "hr budući", "pošto": "sr pošto", "ker ": "sl ker"}},
    "togda/teda (then/therefore)": {"isv": "togda/teda", "support": ["togda", "teda", "tada", "тогава"],
        "candidates": {"tedy": "cs/pl tedy", "tudíž": "cs tudíž", "tudiz": "cs (ascii)", "zatem": "pl zatem",
                       "więc": "pl więc", "wiec": "pl (ascii)", "dakle": "hr/sr dakle", "torej": "sl torej",
                       "следователно": "bg sledovatelno"}},
    "važi (holds)": {"isv": "važi", "support": ["važi", "vazi", "важи", "velja"],
        "candidates": {"platí": "cs/sk platí", "plati": "cs/sk (ascii)", "zachodzi": "pl zachodzi",
                       "vrijedi": "hr vrijedi", "vredi": "sr vredi"}},
    "mora (must)": {"isv": "mora", "support": ["mora", "мора"],
        "candidates": {"musí": "cs/sk musí", "musi": "cs/pl (ascii)", "trzeba": "pl trzeba", "треба": "bg/sr treba"}},
    "imenno (namely)": {"isv": "imenno", "support": ["imenno", "именно"],
        "candidates": {"totiž": "cs totiž", "totiz": "cs (ascii)", "mianowicie": "pl mianowicie",
                       "naime": "hr/sr naime", "namreč": "sl namreč", "namrec": "sl (ascii)", "именно ": "bg imenno"}},
}

def nfc(s):
    return unicodedata.normalize("NFC", s)

texts = {f.name: nfc(f.read_text(encoding="utf-8", errors="replace").lower()) for f in sorted(SHELF.glob("*.txt"))}
results = {}
for rname, spec in REGISTER.items():
    hits = []
    presence = defaultdict(set)
    stems = [(s, "support") for s in spec["support"]] + [(s, "competitor") for s in spec["candidates"]]
    for fname, text in texts.items():
        lg = lang_of(fname)
        for stem, kind in stems:
            n = len(re.findall(r"(?<![\wа-яёіїє])" + re.escape(nfc(stem.lower().strip())), text))
            if n:
                hits.append({"file": fname, "lang": lg, "branch": BRANCH.get(lg, "?"), "stem": stem.strip(),
                             "kind": kind, "count": n,
                             "note": spec["candidates"].get(stem, "cognate of ISV register form")})
                presence[BRANCH.get(lg, "?")].add(kind)
    results[rname] = {"isv": spec["isv"], "hits": hits,
                      "branch_summary": {b: sorted(k) for b, k in presence.items()}}

(BASE / "REGISTER_ROW_WS_PROBE_v1_20260704.json").write_text(json.dumps({
    "artifact": "register_row_ws_probe_v1", "generated": "2026-07-04",
    "boundary": "register lemmas get the same support/competitor typing as concept rows; "
                "shelf-level; math prose connective usage — context review pending",
    "rows": results}, ensure_ascii=False, indent=1), encoding="utf-8")

for rname, r in results.items():
    bs = r["branch_summary"]
    def tag(b):
        ks = bs.get(b, [])
        if "support" in ks and "competitor" in ks:
            return "support+competitor"
        if "support" in ks:
            return "support"
        if "competitor" in ks:
            return "COMPETITOR-ONLY"
        return "no-hit"
    print(f"  {rname:32s} west={tag('west'):20s} south={tag('south')}")
