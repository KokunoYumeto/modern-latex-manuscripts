# Build UNION_TERM_SPINE: merge per-lane 60-term spines into one concept x lane matrix.
# Inputs are read-only; outputs land in the program folder. CPU-only, no network.
import json
import re
from pathlib import Path
from collections import defaultdict

LOGS = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\codex backup\logs")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

ALIASES = {
    "coprime/foreign ideals": "coprime ideals",
    "gcd": "greatest common divisor",
    "lcm": "least common multiple",
    "morphism/homomorphism": "homomorphism",
    "map/mapping": "map",
    "unit/identity": "identity",
}

def norm(c):
    c = re.sub(r"\s+", " ", c.strip().lower())
    return ALIASES.get(c, c)

union = defaultdict(lambda: {"concept_variants": set(), "clusters": set(), "lanes": {}})

def add(concept, lane, record, cluster=None):
    key = norm(concept)
    u = union[key]
    u["concept_variants"].add(concept.strip())
    if cluster:
        u["clusters"].add(cluster)
    u["lanes"][lane] = record

# --- 1. Pan-Romance: promoted-register hit table (seeds + comparator evidence) ---
rom = json.loads((LOGS / "PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.json").read_text(encoding="utf-8-sig"))
rom_rows = {}
for r in rom["rows"]:
    comparator_groups_with_hits = sum(
        1 for g, v in (r.get("source_groups") or {}).items()
        if isinstance(v, dict) and (v.get("documents_with_hits") or 0) > 0
    )
    rom_rows[r["id"]] = {
        "spine_id": r["id"],
        "forms": {"es": r.get("spanish_seed"), "fr": r.get("french_seed")},
        "evidence": {"es": r.get("spanish_evidence"), "fr": r.get("french_evidence")},
        "status": r.get("status"),
        "review_note": r.get("review_note"),
        "comparator_groups_with_hits": comparator_groups_with_hits,
        "concept": r["concept"],
    }

# --- 2. Pan-Romance fallback: attested forms in pt/gl/ca/it/ro/rm ---
fb = json.loads((LOGS / "PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.json").read_text(encoding="utf-8-sig"))
for r in fb["rows"]:
    base = rom_rows.get(r["id"])
    if base is None:
        base = {"spine_id": r["id"], "forms": {}, "evidence": {}, "status": None, "concept": r["concept"]}
        rom_rows[r["id"]] = base
    for lang, hit in (r.get("hits") or {}).items():
        if isinstance(hit, dict) and hit.get("matched"):
            base["forms"][lang] = hit["matched"]
    base["fallback_patterns"] = r.get("patterns")
    base["fallback_status"] = r.get("status")
    base["fallback_major_hit_count"] = r.get("major_hit_count")

for r in rom_rows.values():
    add(r.pop("concept"), "pan_romance", r, cluster="algebra_invariant_theory")

# --- 3. Controlled Arabic spine (markdown table) ---
ar_md = (LOGS / "CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.md").read_text(encoding="utf-8")
in_rows = False
for line in ar_md.splitlines():
    if line.startswith("| # | Concept"):
        in_rows = True
        continue
    if in_rows:
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 10 or cells[0].startswith("---") or cells[0] == "#":
            continue
        num, concept, cluster, candidates, preferred, hits, native, fallback, status, rationale = cells[:10]
        add(concept, "controlled_arabic", {
            "spine_id": f"AR{int(num):02d}" if num.isdigit() else num,
            "forms": {"ar_candidates": candidates, "ar_preferred": preferred or None},
            "hit_count": int(hits) if hits.isdigit() else None,
            "native_sources": int(native) if native.isdigit() else None,
            "fallback_sources": int(fallback) if fallback.isdigit() else None,
            "status": status,
        }, cluster=cluster)

# --- 4. Arabic/Farsi/Persianate ledger ---
afp = json.loads((LOGS / "R3_ARABIC_FARSI_PERSIANATE_60_TERM_LEDGER_20260629T073239Z.json").read_text(encoding="utf-8-sig"))
for r in afp["rows"]:
    add(r.get("english") or r["term_id"], "arabic_farsi_persianate", {
        "spine_id": r["term_id"],
        "forms": {
            "ar": r.get("controlled_arabic_candidate"),
            "fa": r.get("persian_farsi_candidate"),
            "persianate_bridge": r.get("persianate_bridge_candidate"),
        },
        "status": {
            "ar": r.get("controlled_arabic_status"),
            "fa": r.get("persian_farsi_status"),
            "bridge": r.get("bridge_status"),
        },
        "hit_counts": {
            "ar": r.get("controlled_arabic_hit_count"),
            "fa": r.get("persian_farsi_hit_count"),
        },
        "rejection_lanes": r.get("rejection_lanes"),
        "notes": r.get("notes"),
    }, cluster=r.get("cluster"))

# --- 5. Malay-Indonesian spine ---
mi = json.loads((LOGS / "MALAY_INDONESIAN_60_TERM_SPINE_AND_PROOF_GRAMMAR_20260629T033558Z.json").read_text(encoding="utf-8-sig"))
for r in mi["term_spine"]:
    add(r["concept"], "malay_indonesian", {
        "spine_id": f"MI{r['id']:02d}",
        "forms": {"my_id": r.get("candidate")},
        "hit_counts": r.get("counts"),
        "status": r.get("status"),
        "evidence_marker": r.get("evidence_marker"),
    })

# --- Slavic placeholder (ledger retrofit pending) ---
SLAVIC_NOTE = "pending: retrofit from INTERSLAVIC_LOGBOOK term decisions + glossary/ files"

# --- Emit ---
LANES = ["pan_romance", "controlled_arabic", "arabic_farsi_persianate", "malay_indonesian"]
concepts_sorted = sorted(union.keys())
out_json = {
    "artifact": "union_term_spine",
    "generated": "2026-07-04",
    "inputs": [
        "PAN_ROMANCE_PROMOTED_REGISTER_60_TERM_SOURCE_HIT_TABLE_20260629.json",
        "PAN_ROMANCE_FALLBACK_TERM_HIT_REVIEW_20260629.json",
        "CONTROLLED_ARABIC_60_TERM_SPINE_20260629T021500Z.md",
        "R3_ARABIC_FARSI_PERSIANATE_60_TERM_LEDGER_20260629T073239Z.json",
        "MALAY_INDONESIAN_60_TERM_SPINE_AND_PROOF_GRAMMAR_20260629T033558Z.json",
    ],
    "slavic_lane": SLAVIC_NOTE,
    "boundary": "Evidence merge only. No term promotion, no new wording, no authority claims. Statuses are copied from lane artifacts.",
    "concept_count": len(concepts_sorted),
    "concepts": {
        k: {
            "concept_variants": sorted(union[k]["concept_variants"]),
            "clusters": sorted(union[k]["clusters"]),
            "lane_count": len(union[k]["lanes"]),
            "lanes": union[k]["lanes"],
        } for k in concepts_sorted
    },
}
(OUT / "UNION_TERM_SPINE_20260704.json").write_text(
    json.dumps(out_json, ensure_ascii=False, indent=1), encoding="utf-8")

# Markdown summary
overlap = defaultdict(int)
for k in concepts_sorted:
    overlap[len(union[k]["lanes"])] += 1
core = [k for k in concepts_sorted if len(union[k]["lanes"]) >= 3]
per_lane = {ln: sum(1 for k in concepts_sorted if ln in union[k]["lanes"]) for ln in LANES}

md = []
md.append("# Union Term Spine (v1) — concept × lane matrix")
md.append("")
md.append("Generated 2026-07-04 by `scripts/build_union_spine.py`. Evidence merge only — no promotion, no new wording; statuses copied from lane artifacts. Slavic column: " + SLAVIC_NOTE + ".")
md.append("")
md.append(f"- Unique concepts across lanes: **{len(concepts_sorted)}** (each lane's '60-term spine' is lane-relative; the union is the real inventory)")
md.append(f"- Per-lane coverage: " + ", ".join(f"{ln} {n}" for ln, n in per_lane.items()))
md.append(f"- Overlap histogram (concept present in N lanes): " + ", ".join(f"{n} lanes: {c}" for n, c in sorted(overlap.items(), reverse=True)))
md.append(f"- Core set (≥3 lanes): **{len(core)}** concepts: " + ", ".join(core))
md.append("")
md.append("| Concept | Clusters | PanRom | CtrlAr | Ar/Fa/Pers | My/Id | Lanes |")
md.append("| --- | --- | --- | --- | --- | --- | ---: |")

def cell(k, lane):
    rec = union[k]["lanes"].get(lane)
    if not rec:
        return ""
    st = rec.get("status")
    if isinstance(st, dict):
        st = st.get("bridge") or st.get("ar") or ""
    st = (st or "")
    short = {
        "interlingua_source_hit": "hit",
        "esperanto_warning_source_hit": "warn-hit",
        "no_promoted_register_source_hit": "no-hit",
        "source_backed_promotable_seed": "seed",
        "attested_needs_review": "attested",
        "fallback_attested_needs_review": "fb-attested",
        "open_no_direct_evidence": "GAP",
        "open_specialist_evidence_required": "GAP-spec",
        "promotable_seed_with_review": "seed",
        "source_backed_seed": "seed",
        "shared_promotable_seed": "seed",
        "variant_pair_required": "variant-pair",
    }.get(st, st[:18] if st else "•")
    return short

for k in concepts_sorted:
    u = union[k]
    md.append("| {} | {} | {} | {} | {} | {} | {} |".format(
        k, ",".join(sorted(u["clusters"]))[:40],
        cell(k, "pan_romance"), cell(k, "controlled_arabic"),
        cell(k, "arabic_farsi_persianate"), cell(k, "malay_indonesian"),
        len(u["lanes"])))

(OUT / "UNION_TERM_SPINE_20260704.md").write_text("\n".join(md), encoding="utf-8")
print(f"concepts: {len(concepts_sorted)}")
print(f"per-lane: {per_lane}")
print(f"overlap: {dict(sorted(overlap.items(), reverse=True))}")
print(f"core(>=3 lanes): {len(core)}")
print("wrote UNION_TERM_SPINE_20260704.json / .md")
