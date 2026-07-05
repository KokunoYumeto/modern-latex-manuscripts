# Merge Fable proof_prose_lexicon_v1 + ChatGPT ISV_PROOF_REGISTER_INSERTIONS_v1
# into proof_prose_lexicon_v2 (union, lemma-grouped, provenance-tagged).
# Also emits the list of over-stoplisted register words to be UN-stoplisted
# (correction: proof connectives/modals are register vocabulary, not noise).
import csv
import json
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

v1 = json.loads((BASE / "data" / "proof_prose_lexicon_v1.json").read_text(encoding="utf-8"))
lemmas = {}
for e in v1["entries"]:
    key = e["isv"].split()[0].lower()
    lemmas[key] = {"lemma": e["isv"], "en": e["en"], "class": e["stratum"],
                   "variants": set(e["stems"]), "provenance": {"fable_v1"}, "id": e["id"]}

with (DROP / "ISV_PROOF_REGISTER_INSERTIONS_v1_20260704.csv").open(encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        lem = (row["lemma"] or row["token"]).split("/")[0].strip().lower()
        tok = row["token"].strip().lower()
        if lem in lemmas:
            lemmas[lem]["variants"].add(tok)
            lemmas[lem]["provenance"].add("chatgpt_v1")
            if "proof" not in lemmas[lem]["class"]:
                lemmas[lem]["class"] = row["insert_class"]
        else:
            lemmas[lem] = {"lemma": row["lemma"], "en": row["proposed_english_gloss"],
                           "class": row["insert_class"], "variants": {tok, lem},
                           "provenance": {"chatgpt_v1"}, "id": f"reg-{lem}"}

entries = []
for k, v in sorted(lemmas.items()):
    entries.append({"id": v["id"], "lemma": v["lemma"], "en": v["en"], "class": v["class"],
                    "variants": sorted(x for x in v["variants"] if x),
                    "provenance": sorted(v["provenance"]),
                    "status": "proposed_internal_insert; needs linguistic review",
                    "source_use": "generated_internal_consistency", "permitted_use_weight": 0.35})

out = {
    "artifact": "proof_prose_lexicon_v2",
    "generated": "2026-07-04",
    "note": "Union of Fable v1 (25 concepts) and ChatGPT proof-register insertions v1 (70 lemma groups). "
            "Correction applied: proof connectives/modals/sequencers (togda, teper, teda, imenno, mora, kromě, "
            "znovu, ješče, jeden, osoblivo, nakonec, inače, zbog, tada…) are REGISTER vocabulary, not stopwords "
            "— they are what a controlled register standardizes. Stoplist shrinks to true function words "
            "(pronouns, pure auxiliaries, prepositions).",
    "entry_count": len(entries),
    "entries": entries,
}
(BASE / "data" / "proof_prose_lexicon_v2.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

# words to remove from the coverage stoplist (now lexicalized)
unstop = sorted({v for e in entries for v in e["variants"]})
(BASE / "data" / "unstoplist_v2.json").write_text(json.dumps(unstop, ensure_ascii=False), encoding="utf-8")
prov = defaultdict(int)
for e in entries:
    prov["+".join(e["provenance"])] += 1
print(f"lexicon v2: {len(entries)} lemma groups | provenance {dict(prov)} | unstoplisted variants {len(unstop)}")
