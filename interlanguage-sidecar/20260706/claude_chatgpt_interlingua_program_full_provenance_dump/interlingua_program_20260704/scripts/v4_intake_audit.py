# Intake audit of ChatGPT pass-v4 drop (long-tail triage + v2.3 lexicon proposal).
# Mechanical checks: cross-group variant collisions, new-entry/existing-group dups,
# risky short-stem attaches, en-hint dump for gloss review.
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

v2 = json.loads((BASE / "data" / "proof_prose_lexicon_v2.json").read_text(encoding="utf-8"))
v23 = json.loads((DROP / "proof_prose_lexicon_v2_3_chatgpt_longtail_proposal.json").read_text(encoding="utf-8-sig"))
triage = json.loads((DROP / "ISV_LONGTAIL_TYPE_TRIAGE_PASS_v4_20260704.json").read_text(encoding="utf-8-sig"))

print("v2 entries:", len(v2["entries"]), "| v2.3 entries:", len(v23["entries"]))
print("triage keys:", list(triage.keys())[:8])
rows = triage.get("rows") or triage.get("items") or triage.get("types")
print("triage rows:", len(rows) if rows else "??", "| sample:", json.dumps(rows[0], ensure_ascii=False)[:200] if rows else "")

# A: variant -> groups collisions in v2.3
owner = defaultdict(list)
for e in v23["entries"]:
    for v in e["variants"]:
        owner[v.lower()].append(e["id"])
collisions = {v: ids for v, ids in owner.items() if len(ids) > 1}
print(f"\nA) cross-group variant collisions: {len(collisions)}")
for v, ids in sorted(collisions.items()):
    print(f"   {v}: {ids}")

# B: new entries (not in v2 by id) whose lemma-head or variants overlap an existing v2 group
v2_ids = {e["id"] for e in v2["entries"]}
v2_var_owner = {}
v2_heads = {}
for e in v2["entries"]:
    h = e["lemma"].split()[0].split("/")[0].lower()
    v2_heads[e["id"]] = h
    for v in e["variants"]:
        v2_var_owner[v.lower()] = e["id"]
new_entries = [e for e in v23["entries"] if e["id"] not in v2_ids]
print(f"\nB) new entries in v2.3: {len(new_entries)}")
dup_like = []
for e in new_entries:
    h = e["lemma"].split()[0].split("/")[0].lower()
    hits = set()
    for v in e["variants"]:
        if v.lower() in v2_var_owner:
            hits.add(v2_var_owner[v.lower()])
    for gid, gh in v2_heads.items():
        if len(h) >= 5 and len(gh) >= 5 and h[:5] == gh[:5]:
            hits.add(gid)
    if hits:
        dup_like.append((e["id"], e["lemma"], sorted(hits)))
print(f"   new-entry/existing-group overlaps: {len(dup_like)}")
for i, l, hits in dup_like:
    print(f"   {i} ({l}) ~ {hits}")

# C: en-hint dump of all new entries for gloss review
print("\nC) new-entry en hints:")
for e in sorted(new_entries, key=lambda x: x["id"]):
    print(f"   {e['id']} | {e['lemma']} | {e.get('class','')} | EN: {e.get('en','')}")

# D: risky attaches from triage: head_match with short stems
if rows:
    risky = []
    for r in rows:
        note = r.get("note", "") or r.get("reason", "")
        act = r.get("action") or r.get("recommended_action") or ""
        if act == "attach_variant" and "head_match" in note:
            stem = note.split("head_match_")[-1].rstrip(")").split(";")[0].strip()
            risky.append((r.get("token"), stem, note))
    short = [x for x in risky if len(x[1]) <= 5]
    print(f"\nD) head_match attaches: {len(risky)} | stem<=5: {len(short)}")
    for tok, stem, note in short:
        print(f"   {tok} <- {stem} | {note[:110]}")
