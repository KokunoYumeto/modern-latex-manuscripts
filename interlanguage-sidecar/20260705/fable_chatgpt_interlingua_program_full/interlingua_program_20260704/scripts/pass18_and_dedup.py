# Insertion pass 18 + lexicon v2.2 dedup (merge near-duplicate lemma groups:
# overlapping variants or shared 5+char lemma-head stems; union variants+provenance).
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
p = BASE / "data" / "proof_prose_lexicon_v2.json"
lex = json.loads(p.read_text(encoding="utf-8"))

NEW = [
    {"id": "bilinear", "lemma": "bilinearny", "en": "bilinear", "class": "math_general",
     "variants": ["bilinearn"]},
    {"id": "accepted-adopted", "lemma": "prijeti", "en": "accepted; adopted (convention)", "class": "proof_reference",
     "variants": ["prijeto", "prijet", "prijem"]},
    {"id": "arrives-prihoditi", "lemma": "prihoditi", "en": "arrives (at); comes to", "class": "proof_sequence",
     "variants": ["prihodi", "prihod"]},
    {"id": "against", "lemma": "proti", "en": "against; versus", "class": "discourse_connective",
     "variants": ["proti", "protiv"]},
    {"id": "letter-symbol", "lemma": "bukva", "en": "letter (symbol)", "class": "proof_grammar",
     "variants": ["bukva", "bukvami", "bukvy", "bukvoju"]},
    {"id": "pass-over", "lemma": "prějdti", "en": "pass over (to); proceed to", "class": "proof_sequence",
     "variants": ["prějd", "prejd", "prějti", "prejti"]},
    {"id": "ascribes", "lemma": "pripisovati", "en": "ascribes; attributes", "class": "proof_predicate",
     "variants": ["pripisuje", "pripisa"]},
    {"id": "connected", "lemma": "povezany", "en": "connected; linked", "class": "math_general",
     "variants": ["povezan", "svezan"]},
]
for n in NEW:
    n.update({"provenance": ["fable_pass18"], "status": "proposed_internal_insert; needs linguistic review",
              "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35})
    lex["entries"].append(n)
for e in lex["entries"]:
    if e["lemma"].startswith("pokazati") or "pokazuje" in e.get("variants", []):
        e["variants"] = sorted(set(e["variants"]) | {"pokaže", "pokaz"})
    if "slěduj" in str(e.get("variants", "")) or e["lemma"].startswith("slěduje") or e.get("id") == "follows-from":
        e["variants"] = sorted(set(e["variants"]) | {"slijedi", "sledi"})

# --- v2.2 dedup ---
def head(e):
    return e["lemma"].split()[0].split("/")[0].lower()

entries = lex["entries"]
merged = []
used = [False] * len(entries)
merges = 0
for i, a in enumerate(entries):
    if used[i]:
        continue
    va = set(v.lower() for v in a["variants"])
    ha = head(a)
    group = dict(a)
    group["variants"] = sorted(va)
    group["provenance"] = sorted(set(a.get("provenance", [])))
    for k in range(i + 1, len(entries)):
        if used[k]:
            continue
        b = entries[k]
        vb = set(v.lower() for v in b["variants"])
        hb = head(b)
        stem_share = len(ha) >= 5 and len(hb) >= 5 and (ha[:5] == hb[:5])
        if va & vb or stem_share:
            used[k] = True
            merges += 1
            group["variants"] = sorted(set(group["variants"]) | vb | {hb})
            group["provenance"] = sorted(set(group["provenance"]) | set(b.get("provenance", [])))
            if len(b.get("en", "")) > len(group.get("en", "")):
                group["en"] = b["en"]
            group.setdefault("merged_ids", []).append(b.get("id"))
    merged.append(group)
    used[i] = True

lex["entries"] = merged
lex["entry_count"] = len(merged)
lex["artifact"] = "proof_prose_lexicon_v2_2"
lex["dedup_note"] = f"v2.2: {merges} near-duplicate groups merged (variant overlap or shared 5-char lemma head); provenance unioned"
p.write_text(json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"v2.2: {len(merged)} groups after {merges} merges")
