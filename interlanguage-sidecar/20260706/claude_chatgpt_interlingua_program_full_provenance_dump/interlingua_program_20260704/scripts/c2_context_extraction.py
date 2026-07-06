# C2-row context extraction over the 20-source W/S shelf (local extracted texts).
# Covers all C2 concepts that have curated branch stems (backfill v1 set + C2 extension);
# rows without stems are listed as pending — never guessed. Classification only.
import json
import re
import sys
import unicodedata
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
SHELF = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\interslavic_triangulation\20260624_slavic_math_reference\text")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

def lang_of(name):
    for p, l in (("czech", "cs"), ("polish", "pl"), ("slovak", "sk"), ("slovenian", "sl"),
                 ("croatian", "hr"), ("serbian", "sr"), ("bulgarian", "bg")):
        if name.lower().startswith(p):
            return l
    return "??"

# stems per concept: reuse backfill v1 concept stems + C2 extension (confident stems only)
bf = json.loads((OUT / "WS_WITNESS_BACKFILL_v1_20260704.json").read_text(encoding="utf-8"))
STEMS = {}
for cname, spec in bf["concepts"].items():
    stems = sorted({h["stem"] for h in spec.get("hits", [])})
    STEMS[cname] = [s for s in stems if len(s) >= 4]

C2_EXTENSION = {
    "injective": ["injektiv", "injekt", "prost́", "инектив", "инјектив"],
    "surjective": ["surjektiv", "surjekt", "сюректив", "сурјектив"],
    "bijective": ["bijektiv", "bijekt", "биектив", "бијектив"],
    "tensor product": ["tenzor", "tensor", "тензор"],
    "normal subgroup": ["normální podgrup", "normalna podgrup", "podgrupa normalna", "normalni podgrup", "нормална подгруп"],
    "subgroup": ["podgrup", "podskupin", "подгруп"],
    "eigenvalue": ["vlastní čísl", "vlastní hodnot", "wartość własn", "wartosc wlasn", "lastna vrednost", "svojstven", "собствен"],
    "direct sum": ["přímý souč", "primy souc", "suma prosta", "direktna suma", "direktna vsota", "директна сума", "директна всота"],
    "quotient / factor structure": ["faktorov", "kvocientn", "ilorazow", "faktor-", "količnik", "факторн"],
    "characteristic": ["charakteristik", "charakterystyk", "karakteristik", "характеристик"],
    "commutative": ["komutativ", "przemienn", "комутатив"],
    "associative": ["asociativ", "łączn", "laczn", "асоциатив"],
    "distributive": ["distributiv", "rozdzieln", "дистрибутив"],
    "identity element": ["jednotk", "jedynk", "jedinic", "единиц", "enot"],
    "inverse": ["inverzn", "odwrotn", "inverz", "обратн", "инверз"],
    "linear": ["lineárn", "linearn", "liniow", "линейн", "линеарн"],
    "map/mapping": ["zobrazen", "przekształcen", "przeksztalcen", "preslikav", "изображени", "пресликав"],
    "root": ["kořen", "koren", "pierwiast", "корен"],
    "degree": ["stupeň", "stupen", "stopien", "stopn", "степен"],
    "coefficient": ["koeficient", "współczynnik", "wspolczynnik", "коефициент"],
    # proof-grammar connectives (F12-sensitive stratum; confident stems only)
    "conversely": ["naopak", "odwrotnie", "obratno", "обратно"],
    "exists": ["existuj", "istniej", "obstaja", "postoji", "съществува"],
    "for all": ["pro každ", "pre každ", "dla każd", "dla kazd", "za vsak", "za svak", "за всяко", "за всеки"],
    "assumption": ["předpoklad", "predpoklad", "założeni", "zalozeni", "predpostavk", "претпоставк", "предположени"],
    "finite": ["konečn", "konecn", "skończon", "skonczon", "končn", "konačn", "крайн"],
    "equation": ["rovnic", "równan", "rownan", "enačb", "jednačin", "jednadžb", "уравнени"],
    "function": ["funkce", "funkci", "funkcj", "funkcij", "функци"],
    "formula": ["formul", "vzorec", "vzorc", "wzór", "wzor", "формул", "obrazec"],
    "decomposition": ["rozklad", "rozkład", "razcep", "rastav", "разлож", "разлаган"],
    "exercise": ["cvičen", "cvicen", "ćwiczen", "cwiczen", "nalog", "задач"],
    "statement": ["tvrzen", "tvrden", "trditv", "тврђењ", "твърдени"],
    "product": ["součin", "soucin", "iloczyn", "produkt", "umnožak", "produkt", "произведени"],
    "if and only if": ["právě tehdy", "prave tehdy", "wtedy i tylko wtedy", "če in samo če", "ce in samo ce", "ako i samo ako", "тогава и само тогава", "akko"],
    "image": ["obraz"],
    "notation": ["označen", "oznacen", "oznaczen", "oznak", "означени"],
    "relation": ["relac", "relacj", "релаци", "odnos"],
    "problem": ["úloh", "uloh", "zadani", "zadań", "задач", "problém", "problem"],
}
STEMS.update(C2_EXTENSION)

core = json.loads((OUT / "STRATIFIED_CORE_SPINE_PROPOSAL_20260704.json").read_text(encoding="utf-8"))
c2_labels = [r["concept_label"] for r in core["rows"]]

def nfc(s):
    return unicodedata.normalize("NFC", s)

texts = {}
for f in sorted(SHELF.glob("*.txt")):
    texts[f.name] = nfc(f.read_text(encoding="utf-8", errors="replace"))

ALIAS = {"division ring": "division ring / body", "algebra": "algebra (structure)",
         "extension of the ground field": "extension (field)", "map": "map/mapping"}

windows = {}
pending = []
covered = 0
for label in c2_labels:
    key = ALIAS.get(label, label)
    stems = STEMS.get(key) or STEMS.get(label)
    if not stems:
        pending.append(label)
        continue
    covered += 1
    per_lang = defaultdict(list)
    for fname, text in texts.items():
        lg = lang_of(fname)
        low = text.lower()
        for stem in stems:
            sn = nfc(stem.lower())
            for m in list(re.finditer(r"(?<![\wа-яёіїє])" + re.escape(sn), low))[:2]:
                if len(per_lang[lg]) >= 3:
                    break
                a, b = max(0, m.start() - 90), min(len(text), m.start() + 160)
                per_lang[lg].append({"file": fname, "stem": stem,
                                     "window": re.sub(r"\s+", " ", text[a:b]).strip()})
    windows[label] = {k: v for k, v in per_lang.items() if v}

out = {
    "artifact": "c2_context_windows_v1",
    "generated": "2026-07-04",
    "boundary": "context-review aids from the 20-source native shelf; concept-shelf level; not row-certified witnesses; stems curated, never guessed",
    "c2_rows": len(c2_labels),
    "covered": covered,
    "pending_stems": pending,
    "windows": windows,
}
(OUT / "C2_CONTEXT_WINDOWS_v1_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# C2 Context Windows — v1 (native W/S shelf)", "",
      f"2026-07-04. {covered}/{len(c2_labels)} C2 rows covered with curated stems; {len(pending)} pending stems (listed at end). "
      "Context-review aids, concept-shelf level; not row-certified witnesses.", ""]
for label in sorted(windows):
    md.append(f"## {label}")
    for lg, ws in sorted(windows[label].items()):
        for w in ws[:2]:
            md.append(f"- **{lg}** ({w['file'][:40]}): …{w['window'][:180]}…")
    md.append("")
md += ["## Pending stems (no guessing)", ""] + [f"- {p}" for p in pending]
(OUT / "C2_CONTEXT_WINDOWS_v1_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"C2 rows {len(c2_labels)} | covered {covered} | pending {len(pending)}")
print("pending:", ", ".join(pending[:20]))
