# Apply the curated concept ledger seed to the retrofit rows:
# produces INTERLINGUAL_CONCEPT_LEDGER_20260704.json/.md/.csv with per-language labels
# (de | en | uk | ru | isv | isv_cyr) harvested from existing records, coverage stats,
# and the unmapped-term list for the next curation pass. No new wording invented.
import csv
import json
import re
import unicodedata
from pathlib import Path
from collections import defaultdict

OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
seed = json.loads((OUT / "data" / "concept_ledger_seed.json").read_text(encoding="utf-8"))
retro = json.loads((OUT / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json").read_text(encoding="utf-8"))
audit = {a["term_id"]: a for a in json.loads(
    (OUT / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json").read_text(encoding="utf-8"))["rows"]}
slav = json.loads((OUT / "slavic_term_dataset_20260704.json").read_text(encoding="utf-8"))

def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower().strip())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = s.replace("ß", "ss")
    return re.sub(r"\s+", " ", s)

de_to_concept = {}
for c in seed["concepts"]:
    for v in c["de"]:
        de_to_concept[norm(v)] = c["id"]
noise_rx = [re.compile(p) for p in seed["noise_patterns"]]
by_id = {c["id"]: c for c in seed["concepts"]}

def lookup(term):
    n = norm(term)
    if any(rx.search(n) for rx in noise_rx):
        return "NOISE", None
    if n in de_to_concept:
        return "mapped", de_to_concept[n]
    # variant splitting: "x / y" or "x, y" compound source terms
    for part in re.split(r"\s*/\s*|,\s*", n):
        if part in de_to_concept:
            return "mapped_partial", de_to_concept[part]
    # suffix match for inflected heads (e.g. "...körper", "...ideal")
    for head in ("korper", "ideal", "modul", "gruppe", "ring", "form", "darstellung"):
        if n.endswith(head) and head in de_to_concept:
            return "mapped_head", de_to_concept[head]
    # word-boundary containment: a phrase mentioning a known concept maps to it
    # (longest variant wins so "primideal" beats "ideal")
    best = None
    for v, cid in de_to_concept.items():
        if len(v) >= 4 and re.search(r"(?<![a-z0-9])" + re.escape(v) + r"(?![a-z0-9])", n):
            if best is None or len(v) > len(best[0]):
                best = (v, cid)
    if best:
        return "mapped_phrase", best[1]
    return "unmapped", None

# collect per-concept language labels from retrofit rows + raw slavic records
concept_rows = defaultdict(lambda: {"de_variants": set(), "labels": defaultdict(set),
                                    "term_ids": [], "flags": []})
unmapped = defaultdict(int)
noise = defaultdict(int)
mapped_rows = 0

# language labels straight from the raw dataset (richer than retrofit rows)
def get(rec, *keys):
    ex = rec.get("extra_fields") or {}
    for k in keys:
        v = rec.get(k) or ex.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None

raw_by_de = defaultdict(list)
for rec in slav["records"]:
    de = get(rec, "de") or (rec.get("extra_fields") or {}).get("german") or \
         (rec.get("extra_fields") or {}).get("source_de")
    if de:
        raw_by_de[norm(de)].append(rec)

for r in retro["rows"]:
    st = r.get("source_term") or ""
    kind, cid = lookup(st)
    if kind == "NOISE":
        noise[st] += 1
        continue
    if not cid:
        unmapped[st] += r.get("record_count", 1)
        continue
    mapped_rows += 1
    e = concept_rows[cid]
    e["de_variants"].add(st)
    e["term_ids"].append(r["term_id"])
    a = audit.get(r["term_id"])
    if a:
        e["flags"].append(a["bias_flag"])
    if r.get("chosen_form_latin"):
        e["labels"]["isv"].add(r["chosen_form_latin"])
    if r.get("chosen_form_cyrillic"):
        e["labels"]["isv_cyr"].add(r["chosen_form_cyrillic"])
    for rec in raw_by_de.get(norm(st), []):
        for lang, keys in (("uk", ("uk", "ukrainian")), ("ru", ("ru", "russian"))):
            v = get(rec, *keys)
            if v:
                e["labels"][lang].add(v)

ledger = []
for cid, e in sorted(concept_rows.items()):
    c = by_id[cid]
    ledger.append({
        "concept_id": cid, "en": c["en"], "stratum": c["stratum"],
        "de": sorted(e["de_variants"]),
        "uk": sorted(e["labels"]["uk"])[:4], "ru": sorted(e["labels"]["ru"])[:4],
        "isv": sorted(e["labels"]["isv"])[:4], "isv_cyr": sorted(e["labels"]["isv_cyr"])[:4],
        "term_rows": len(e["term_ids"]),
        "f10_flags": sorted(set(e["flags"])),
    })

out = {
    "artifact": "interlingual_concept_ledger_v1",
    "generated": "2026-07-04",
    "seed_concepts": len(seed["concepts"]),
    "concepts_with_data": len(ledger),
    "retrofit_rows_mapped": mapped_rows,
    "retrofit_rows_unmapped": sum(unmapped.values()),
    "noise_rows": sum(noise.values()),
    "boundary": "labels harvested from existing records only; en labels are curated standard usage; no new target-language wording",
    "concepts": ledger,
    "unmapped_terms_top": sorted(unmapped.items(), key=lambda kv: -kv[1])[:80],
}
(OUT / "INTERLINGUAL_CONCEPT_LEDGER_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

with (OUT / "INTERLINGUAL_CONCEPT_LEDGER_20260704.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["concept_id", "stratum", "en", "de", "uk", "ru", "isv", "isv_cyr", "rows", "f10_flags"])
    for c in ledger:
        w.writerow([c["concept_id"], c["stratum"], c["en"], " | ".join(c["de"]),
                    " | ".join(c["uk"]), " | ".join(c["ru"]), " | ".join(c["isv"]),
                    " | ".join(c["isv_cyr"]), c["term_rows"], ",".join(c["f10_flags"])])

md = ["# Interlingual Concept Ledger — v1", "",
      "2026-07-04. Language-neutral concepts with per-language labels harvested from the lane's own records. de→en curated; uk/ru/isv/isv_cyr from glossaries; future columns: ar, fa, es, fr, my/id from the other lanes' spines.",
      "",
      f"- Seed concepts: {len(seed['concepts'])}; with data: {len(ledger)}; retrofit rows mapped: {mapped_rows}; unmapped: {sum(unmapped.values())}; noise rows filtered: {sum(noise.values())}",
      "",
      "| Concept (en) | Stratum | de | isv | uk | ru |", "| --- | --- | --- | --- | --- | --- |"]
for c in ledger:
    md.append(f"| {c['en']} | {c['stratum'][:10]} | {'; '.join(c['de'])[:40]} | {'; '.join(c['isv'])[:30]} | {'; '.join(c['uk'])[:26]} | {'; '.join(c['ru'])[:26]} |")
md += ["", "## Top unmapped (next curation pass)", ""]
for t, n in out["unmapped_terms_top"][:40]:
    md.append(f"- ({n}) {t}")
(OUT / "INTERLINGUAL_CONCEPT_LEDGER_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"seed {len(seed['concepts'])} | with data {len(ledger)} | mapped rows {mapped_rows} | unmapped {sum(unmapped.values())} | noise {sum(noise.values())}")
