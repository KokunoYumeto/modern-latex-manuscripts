# Bulk adjudication of ChatGPT v4 context_review / unresolved / stop_or_register rows
# using the supplied KWIC windows + the v2.4 lexicon.
# Pass A: stop_or_register_review (dict-confirmed function words) -> function_word entries.
# Pass B1: strict auto-attach against v2.4 (head-stem >=6 or vowel-stripped equality vs variants).
# Pass B2: remainder -> review dump (count>=5 for inline hand adjudication; tail queued).
# Everything logged; nothing promoted.
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

lex = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
triage = json.loads((DROP / "ISV_LONGTAIL_TYPE_TRIAGE_PASS_v4_20260704.json").read_text(encoding="utf-8-sig"))
ctx = json.loads((DROP / "ISV_LONGTAIL_CONTEXT_WINDOWS_PASS_v4_20260704.json").read_text(encoding="utf-8-sig"))["contexts"]

VOWELS = "aeiouyěęųåéíóúàâäöüáî"
def stem(t):
    return t.rstrip(VOWELS)

have = {v.lower() for e in lex["entries"] for v in e["variants"]}
heads = {}   # head-stem(>=6) -> entry
varstems = {}  # vowel-stripped variant stem -> entry id (only stems >=5)
for e in lex["entries"]:
    h = e["lemma"].split()[0].split("/")[0].lower()
    if len(h) >= 6:
        heads[h[:6]] = e
    for v in e["variants"]:
        s = stem(v.lower())
        if len(s) >= 5:
            varstems.setdefault(s, e["id"])
by_id = {e["id"]: e for e in lex["entries"]}

rows = triage["rows"]
A = [r for r in rows if r.get("recommended_action") == "stop_or_register_review"]
B = [r for r in rows if r.get("recommended_action") == "context_review"]

log = {"A_function_words": [], "B1_auto_attach": [], "B2_review": [], "already_covered": []}

# --- Pass A: function words from community-dict matches ---
fw_groups = {}
for r in A:
    tok = r["token"]
    if tok.lower() in have:
        log["already_covered"].append(tok)
        continue
    m = re.search(r"head_(\w+)|\(exact\)", r.get("note", ""))
    head = None
    if m and m.group(1):
        head = m.group(1)
    else:
        head = tok
    pos = ""
    pm = re.search(r"POS=([^;]+);", r.get("note", ""))
    if pm:
        pos = pm.group(1)
    fw_groups.setdefault(head, {"tokens": [], "pos": pos})["tokens"].append(tok)

for head, d in fw_groups.items():
    eid = f"fw-{head}"
    if eid in by_id:
        e = by_id[eid]
        e["variants"] = sorted(set(e["variants"]) | set(d["tokens"]))
    else:
        e = {"id": eid, "lemma": head, "en": f"function word ({d['pos'] or 'register'})",
             "class": "function_word",
             "variants": sorted(set(d["tokens"] + [head])),
             "provenance": ["chatgpt_v4_dict", "fable_pass27"],
             "status": "proposed_internal_insert; needs linguistic review",
             "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35,
             "note": "register function word per unstoplist policy (togda/teper precedent); dict-confirmed"}
        lex["entries"].append(e)
        by_id[eid] = e
    for t in d["tokens"]:
        have.add(t.lower())
        log["A_function_words"].append((t, eid))

# --- Pass B1: strict auto-attach ---
for r in B:
    tok = r["token"]
    tl = tok.lower()
    if tl in have:
        log["already_covered"].append(tok)
        continue
    target = None
    how = ""
    s = stem(tl)
    if len(s) >= 5 and s in varstems:
        target, how = varstems[s], f"vowel-stem=={s}"
    elif len(tl) >= 6 and tl[:6] in heads:
        target, how = heads[tl[:6]]["id"], f"head6={tl[:6]}"
    if target:
        e = by_id[target]
        e["variants"] = sorted(set(e["variants"]) | {tok})
        have.add(tl)
        log["B1_auto_attach"].append((tok, target, how, r.get("count", 0)))

# --- Pass B2: dump remainder with windows ---
rem = []
for r in B:
    tok = r["token"]
    if tok.lower() in have:
        continue
    w = ""
    if tok in ctx and ctx[tok]:
        w = ctx[tok][0].get("window", "")[:220]
    rem.append({"token": tok, "count": r.get("count", 0), "window": w})
rem.sort(key=lambda x: -x["count"])
log["B2_review"] = rem

lex["artifact"] = "proof_prose_lexicon_v2_5_prelim"
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(json.dumps(lex, ensure_ascii=False, indent=1), encoding="utf-8")
(BASE / "CONTEXT_REVIEW_ADJUDICATION_LOG_20260705.json").write_text(
    json.dumps(log, ensure_ascii=False, indent=1, default=str), encoding="utf-8")

print(f"A: function-word tokens lexicalized: {len(log['A_function_words'])} into {len(fw_groups)} groups")
print(f"B1: strict auto-attaches: {len(log['B1_auto_attach'])}")
print(f"already covered by v2.4: {len(log['already_covered'])}")
print(f"B2: remainder for hand review: {len(rem)} (count>=5: {sum(1 for x in rem if x['count']>=5)})")
print("\n--- B1 sample (verify by eye, first 25) ---")
for tok, tgt, how, c in log["B1_auto_attach"][:25]:
    print(f"  {tok} -> {tgt} [{how}] n={c}")
print("\n--- B2 count>=5 with windows ---")
for x in rem:
    if x["count"] >= 5:
        print(f"  {x['token']} (n={x['count']}): {x['window'][:150]}")
