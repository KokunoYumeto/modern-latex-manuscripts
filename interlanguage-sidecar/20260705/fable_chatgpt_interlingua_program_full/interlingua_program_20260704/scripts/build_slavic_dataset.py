# Aggregate all glossary/*.json Interslavic term records into one dataset;
# compute stats; link to union spine concepts (coarse); emit slavic dataset JSON.
import json
import re
from pathlib import Path
from collections import Counter

G = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\codex backup\glossary")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

records = []
files_used, files_skipped = 0, 0
for f in sorted(G.glob("*.json")):
    try:
        j = json.loads(f.read_text(encoding="utf-8-sig", errors="replace"))
    except Exception:
        files_skipped += 1
        continue
    terms = j.get("terms") if isinstance(j, dict) else None
    if not isinstance(terms, list):
        files_skipped += 1
        continue
    files_used += 1
    unit = j.get("unit_id") or f.stem
    for t in terms:
        if not isinstance(t, dict):
            continue
        rec = {
            "unit": unit, "file": f.name,
            "de": t.get("de"), "concept_gloss": t.get("modern_concept"),
            "uk": t.get("uk"), "ru": t.get("ru"),
            "isv": t.get("isv"), "isv_cyr": t.get("interslavic_cyrillic"),
            "status": t.get("status"), "motivation": t.get("motivation"),
        }
        extra_langs = [k for k in t.keys() if k not in
                       {"de", "modern_concept", "uk", "ru", "isv", "interslavic_cyrillic", "status", "motivation"}]
        if extra_langs:
            rec["extra_fields"] = {k: t[k] for k in extra_langs}
        records.append(rec)

# witness-column audit: which language fields exist anywhere in the schema?
field_presence = Counter()
for r in records:
    for k in ("uk", "ru", "isv", "isv_cyr"):
        if r.get(k):
            field_presence[k] += 1
    for k in (r.get("extra_fields") or {}):
        field_presence[f"extra:{k}"] += 1

status_dist = Counter(r["status"] or "none" for r in records)

# review-flag mining from motivations + rationale/review extra fields
flags = Counter()
for r in records:
    parts = [r.get("motivation") or ""]
    ex = r.get("extra_fields") or {}
    for k in ("rationale", "review", "reviewer_flag", "reviewer_flag_interslavic", "review_flag", "raw"):
        v = ex.get(k)
        if isinstance(v, str):
            parts.append(v)
    m = " ".join(parts).lower()
    if "review" in m: flags["mentions_review"] += 1
    if "false friend" in m: flags["mentions_false_friend"] += 1
    if re.search(r"\binternational", m): flags["mentions_international"] += 1
    if re.search(r"pan-?slav", m): flags["mentions_pan_slavic"] += 1
    if re.search(r"polish|czech|croat|serb|bulgar|sloven|macedon|slovak", m): flags["mentions_west_south_slavic"] += 1
    if re.search(r"ukrain|russian", m): flags["mentions_east_slavic"] += 1

# link to union spine — word-boundary + plural-tolerant (substring matching
# produced false links: ring<-"bordering", reducible<-"irreducible"; fixed 2026-07-04)
spine = json.loads((OUT / "UNION_TERM_SPINE_20260704.json").read_text(encoding="utf-8"))
spine_rx = {k: re.compile(r"(?<![a-z])" + re.escape(k) + r"(e?s)?(?![a-z])")
            for k in spine["concepts"] if k}
links = {}
for r in records:
    gloss = (r.get("concept_gloss") or "").lower()
    if not gloss:
        continue
    for k, rx in spine_rx.items():
        if rx.search(gloss):
            links.setdefault(k, []).append(r["de"])

out = {
    "artifact": "slavic_term_dataset",
    "generated": "2026-07-04",
    "glossary_files_used": files_used,
    "glossary_files_skipped": files_skipped,
    "record_count": len(records),
    "witness_field_presence": dict(field_presence),
    "status_distribution": dict(status_dist),
    "motivation_flags": dict(flags),
    "union_spine_links": {k: sorted(set(v)) for k, v in sorted(links.items())},
    "records": records,
}
(OUT / "slavic_term_dataset_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"files used {files_used}, skipped {files_skipped}, records {len(records)}")
print("witness fields:", dict(field_presence))
print("status:", dict(status_dist.most_common(8)))
print("flags:", dict(flags))
print(f"union-spine concept links: {len(links)}")
