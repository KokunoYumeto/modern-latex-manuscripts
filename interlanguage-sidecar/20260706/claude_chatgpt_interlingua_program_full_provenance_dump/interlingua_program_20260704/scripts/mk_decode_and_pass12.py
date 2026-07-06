# mk legacy-font decode -> marker-column file; insertion pass 12 lexicon additions.
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

BACKTICK = chr(96)
MAP = {"~": "ч", "{": "ш", BACKTICK: "ж", "w": "њ", "q": "љ", "x": "џ"}
TR = {"a": "а", "b": "б", "v": "в", "g": "г", "d": "д", "e": "е", "z": "з", "i": "и", "j": "ј",
      "k": "к", "l": "л", "m": "м", "n": "н", "o": "о", "p": "п", "r": "р", "s": "с", "t": "т",
      "u": "у", "f": "ф", "h": "х", "c": "ц"}

def to_cyr(s):
    s = "".join(MAP.get(c, c) for c in s)
    return "".join(TR.get(c, c) for c in s)

probe = json.loads((BASE / "MK_COLUMN_PROBE_v1_20260704.json").read_text(encoding="utf-8"))
rows = {}
for k, v in probe["rows"].items():
    if v.get("count"):
        enc = v["mk_form_as_encoded"]
        rows[k] = {"mk_cyrillic": to_cyr(enc.lower()), "mk_as_in_pdf": enc, "count": v["count"],
                   "witness_level": "concept_shelf (dictionary-grade)",
                   "source": "macedonian_ukim_math_lexicon"}
(BASE / "MK_MARKER_COLUMN_v1_20260704.json").write_text(json.dumps({
    "artifact": "mk_marker_column_v1", "generated": "2026-07-04",
    "note": "legacy-font decoded + Latin->Cyrillic; mechanical — spot-check before marker-table merge",
    "rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")
print("mk column decoded:", len(rows), "| ring:", rows["ring"]["mk_cyrillic"],
      "| set:", rows["set"]["mk_cyrillic"], "| quotient:", rows["quotient"]["mk_cyrillic"])

lex = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
NEW = [
    {"id": "uses", "lemma": "koristiti", "en": "uses; makes use of", "class": "proof_operation",
     "variants": ["koristi", "korist"]},
    {"id": "transfer", "lemma": "prěnesti", "en": "transfer; carry over", "class": "proof_operation",
     "variants": ["prěnes", "prenes", "prěnos", "prenos"]},
    {"id": "later", "lemma": "pozdněje", "en": "later; subsequently", "class": "proof_sequence",
     "variants": ["pozdněje", "pozdneje", "pozdnějše"]},
    {"id": "originally", "lemma": "izvorno", "en": "originally; in the original", "class": "proof_reference",
     "variants": ["izvorno", "izvorn"]},
    {"id": "in-contrast", "lemma": "nasuprot", "en": "in contrast; as opposed to", "class": "proof_connective",
     "variants": ["nasuprot"]},
    {"id": "step", "lemma": "korak", "en": "step (of a proof/algorithm)", "class": "proof_grammar",
     "variants": ["korak", "koraka", "korakov", "kroky", "krokov"]},
    {"id": "arrived-came", "lemma": "dojdti", "en": "came (to); arrived at", "class": "proof_sequence",
     "variants": ["došel", "dosel", "došli"]},
    {"id": "defined-part", "lemma": "definovany", "en": "defined (participle)", "class": "proof_grammar",
     "variants": ["definovan"]},
]
for n in NEW:
    n.update({"provenance": ["fable_pass12"], "status": "proposed_internal_insert; needs linguistic review",
              "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35})
    lex["entries"].append(n)
for e in lex["entries"]:
    if e["lemma"].startswith("dopuščati"):
        e["variants"] = sorted(set(e["variants"]) | {"dopušća", "dopusca"})
    if e["lemma"].startswith("porođati"):
        e["variants"] = sorted(set(e["variants"]) | {"porađa", "porada"})
    if e["lemma"] == "osoblivo":
        e["variants"] = sorted(set(e["variants"]) | {"osobito"})
    if e["lemma"] == "ostati":
        e["variants"] = sorted(set(e["variants"]) | {"obstava"})
    if e["lemma"].startswith("ležati"):
        e["variants"] = sorted(set(e["variants"]) | {"ležet", "lezet"})
    if e["lemma"].startswith("vměsto"):
        e["variants"] = sorted(set(e["variants"]) | {"vmesto"})
lex["entry_count"] = len(lex["entries"])
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(
    json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
print("pass12 lexicon:", len(lex["entries"]))
