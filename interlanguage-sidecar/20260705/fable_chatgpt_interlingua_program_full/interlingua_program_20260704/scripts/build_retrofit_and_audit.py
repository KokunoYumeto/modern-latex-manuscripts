# Build INTERSLAVIC_LEDGER_RETROFIT_20260704 (.json/.md/.csv) and
# F10_EAST_SLAVIC_SKEW_AUDIT_20260704 (.json/.md) from the two extraction datasets.
# Boundary: no term promotion, no new wording; flags and fields are mechanical
# classifications of EXISTING records, marked for editorial/review passes.
import csv
import hashlib
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
SLAVIC = OUT / "slavic_term_dataset_20260704.json"
LOGBOOK = OUT / "interslavic_term_decisions_20260704.json"

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

slav = json.loads(SLAVIC.read_text(encoding="utf-8"))
logb = json.loads(LOGBOOK.read_text(encoding="utf-8"))

# --- helpers -----------------------------------------------------------------
WEST = r"polish|czech|slovak|\bpl\b|\bcs\b|\bsk\b"
SOUTH = r"croat|serb|bulgar|sloven|macedon|\bhr\b|\bsr\b|\bbg\b|\bsl\b|\bmk\b"
EAST = r"ukrain|russian|\buk\b|\bru\b|русск|україн"
ISV_AUTH = r"interslavic dictionary|interslavic reference|interslavic project|medžuslovjansk|steen|voting"
INTL = r"\binternational|latinism|classical (?:invariant )?theory term|greek|latin\b|transvectant"
BROAD_CLAIM = r"pan-?slav|all slav|broadly (?:slav|intelligib)|transparent (?:to|across) (?:all|slav)"

# flagship terms spot-triangulated on the 20-source W/S shelf (triangulation log 2026-06-24)
SHELF = {
    "tělo": "nekomutativno tělo backed cs/pl/bg/hr (division ring/body)",
    "telo": "nekomutativno tělo backed cs/pl/bg/hr",
    "polje": "polje = commutative field, hr + shelf backed",
    "jednostran": "jednostranno prosty ideal backed cs/pl topic sources",
    "idempotent": "primitivny idempotent backed cs/pl topic sources",
    "razpad": "razpadno polje kept for continuity; cs/pl prefer rozklad- family (flagged alternative rozkladno polje)",
}
DOMINANCE_RISK = {
    "kolco": "ring: E-Slavic continuity vs cs/sk okruh, S-Slavic prsten, sl kolobar; log: 'not derivable mechanically from a majority vote'; reviewer-sensitive",
}

REASON_RX = {
    "pan_slavic_native": r"pan-?slav|all slav|broad|native|transparent",
    "international": INTL,
    "east_slavic_continuity": r"mirrors (?:uk|ru|ukrain|russian)|continuity|carried forward|ряд",
    "coinage": r"coinage|coined|neologism|reducent",
    "source_fidelity": r"source fidelity|historical term|noether",
    "script_stability": r"script stability|translit|cyrillic",
    "disambiguation": r"ambigu|disambig|avoids? confusion|clash",
}

def blob_of(rec):
    parts = [rec.get("motivation") or ""]
    ex = rec.get("extra_fields") or {}
    for k in ("rationale", "review", "reviewer_flag", "reviewer_flag_interslavic", "review_flag", "raw"):
        if isinstance(ex.get(k), str):
            parts.append(ex[k])
    return " ".join(parts)

def get_lang(rec, *keys):
    ex = rec.get("extra_fields") or {}
    for k in keys:
        v = rec.get(k) or ex.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None

def slug(s):
    s = re.sub(r"[^\w\s-]", "", (s or "").lower())
    return re.sub(r"[\s/]+", "_", s.strip())[:60] or "unnamed"

# --- merge glossary records to term level -------------------------------------
groups = defaultdict(list)
for rec in slav["records"]:
    ex0 = rec.get("extra_fields") or {}
    de = get_lang(rec, "de") or ex0.get("german") or ex0.get("german_source") or \
         ex0.get("source_de") or ex0.get("source_term") or ex0.get("source") or \
         ex0.get("concept") or rec.get("concept_gloss") or "?"
    isv = get_lang(rec, "isv") or (rec.get("extra_fields") or {}).get("interslavic_latin") or \
          (rec.get("extra_fields") or {}).get("interslavic")
    key = (slug(de), slug(isv or ""))
    groups[key].append(rec)

# logbook decisions indexed for merge
logb_by_form = defaultdict(list)
for d in logb["decisions"]:
    logb_by_form[slug(d.get("chosen_form"))].append(d)

rows, audit_rows = [], []
used_logbook = set()

for (de_s, isv_s), recs in sorted(groups.items()):
    r0 = recs[0]
    ex_r0 = r0.get("extra_fields") or {}
    de = get_lang(r0, "de") or ex_r0.get("german") or ex_r0.get("german_source") or \
         ex_r0.get("source_de") or ex_r0.get("source_term") or ex_r0.get("source") or \
         ex_r0.get("concept") or r0.get("concept_gloss")
    isv = get_lang(r0, "isv") or (r0.get("extra_fields") or {}).get("interslavic_latin") or \
          (r0.get("extra_fields") or {}).get("interslavic")
    cyr = None
    for r in recs:
        cyr = cyr or get_lang(r, "isv_cyr") or (r.get("extra_fields") or {}).get("interslavic_cyrillic")
    blob = " ".join(blob_of(r) for r in recs).lower()
    lb_matches = logb_by_form.get(isv_s, []) if isv_s else []
    for d in lb_matches:
        used_logbook.add(id(d))
        blob += " " + " ".join(d.get("notes", [])).lower()

    reason_class = [k for k, rx in REASON_RX.items() if re.search(rx, blob)] or ["unstated"]
    statuses = [r.get("status") for r in recs if r.get("status")]
    status = statuses[-1] if statuses else "unstated"

    has_uk = any(get_lang(r, "uk") or (r.get("extra_fields") or {}).get("ukrainian") for r in recs)
    has_ru = any(get_lang(r, "ru") or (r.get("extra_fields") or {}).get("russian") for r in recs)
    E = int(has_uk) + int(has_ru) + (1 if re.search(EAST, blob) else 0)
    W_S = 1 if re.search(WEST, blob) else 0
    S = 1 if re.search(SOUTH, blob) else 0
    I = 1 if re.search(ISV_AUTH, blob) else 0
    X = 1 if re.search(INTL, blob) else 0
    shelf_hit = next((note for frag, note in SHELF.items() if isv and frag in isv.lower()), None)
    dom_hit = next((note for frag, note in DOMINANCE_RISK.items() if isv and frag in isv.lower()), None)
    if shelf_hit:
        W_S, S = max(W_S, 1), max(S, 1)

    # flag assignment (conservative, mechanical)
    if dom_hit:
        flag, reason_f = "F10-3", dom_hit
        fix = "resolve vs okruh/prsten/kolobar with access-gain ledger + Interslavic authority input before external showing"
        safe = "no_fix_first"
    elif "coinage" in reason_class:
        flag, reason_f = "F10-4", "constructed/specialist term; transparent but needs community certification"
        fix = "keep explicit definition at first use; mark authority-needed in review packet"
        safe = "yes_with_definition"
    elif shelf_hit or W_S or S:
        flag, reason_f = "F10-0", (shelf_hit or "rationale cites W/S Slavic evidence")
        fix = "record witness forms in the term row (currently prose/shelf only)"
        safe = "yes"
    elif I or X:
        flag, reason_f = "F10-0", "Interslavic-authority or international rationale present (no W/S witness)"
        fix = "add W/S witness forms or explicit gap note from the 20-source shelf"
        safe = "yes"
    elif re.search(BROAD_CLAIM, blob):
        flag, reason_f = "F10-2", "broad-Slavic claim with East-only witness vector"
        fix = "back the claim with W/S witness forms from the shelf, or weaken the claim"
        safe = "no_fix_first"
    else:
        flag, reason_f = "F10-1", "no non-East witness or rationale recorded"
        fix = "backfill witness vector from 20-source shelf or mark explicit gap"
        safe = "review"

    term_id = f"ISV-{de_s[:40]}" + (f"--{isv_s[:20]}" if isv_s else "")
    rows.append({
        "term_id": term_id,
        "source_term": de,
        "chosen_form_latin": isv,
        "chosen_form_cyrillic": cyr,
        "concept_link": None,  # filled below from union spine
        "reason_class": reason_class,
        "access_gain_fields": {
            "main_register_retention": None, "marginal_inter_intelligibility_gain": None,
            "cross_standard_recognition": ("shelf_spot_triangulated" if shelf_hit else None),
            "source_strength": ("east_slavic_witnessed" if (has_uk or has_ru) else "unwitnessed"),
            "script_access": ("dual_script" if cyr else "latin_only_recorded"),
            "dominance_penalty": ("flagged" if dom_hit else None),
            "note": "values require editorial pass; nulls are honest blanks, not zeros",
        },
        "status": status,
        "reviewer_need": flag in ("F10-1", "F10-2", "F10-3", "F10-4"),
        "source_pointer": sorted({r["file"] for r in recs}) + [f"logbook:{d['entry']}" for d in lb_matches],
        "record_count": len(recs),
    })
    audit_rows.append({
        "term_id": term_id,
        "chosen_form_latin": isv,
        "witness_vector": {"E": E, "W_S": W_S, "S": S, "I": I, "X": X},
        "bias_flag": flag,
        "reason_for_flag": reason_f,
        "required_fix": fix,
        "safe_to_show_external": safe,
    })

# logbook-only decisions (no glossary twin)
for d in logb["decisions"]:
    if id(d) in used_logbook:
        continue
    blob = " ".join(d.get("notes", [])).lower()
    reason_class = [k for k, rx in REASON_RX.items() if re.search(rx, blob)] or ["unstated"]
    isv = d.get("chosen_form")
    dom_hit = next((n for frag, n in DOMINANCE_RISK.items() if isv and frag in isv.lower()), None)
    shelf_hit = next((n for frag, n in SHELF.items() if isv and frag in isv.lower()), None)
    flag = "F10-3" if dom_hit else ("F10-0" if shelf_hit else ("F10-4" if "coinage" in reason_class else "F10-1"))
    term_id = f"ISV-LB-{slug(d.get('source_term'))[:40]}"
    rows.append({
        "term_id": term_id, "source_term": d.get("source_term"),
        "chosen_form_latin": isv, "chosen_form_cyrillic": None, "concept_link": None,
        "reason_class": reason_class,
        "access_gain_fields": {"note": "logbook-only decision; editorial pass required"},
        "status": d.get("status_class", "unstated"),
        "reviewer_need": flag != "F10-0",
        "source_pointer": [f"logbook:{d['entry']} / {d['section']}"],
        "record_count": 1,
    })
    audit_rows.append({
        "term_id": term_id, "chosen_form_latin": isv,
        "witness_vector": {"E": 1 if re.search(EAST, blob) else 0,
                           "W_S": 1 if re.search(WEST, blob) else 0,
                           "S": 1 if re.search(SOUTH, blob) else 0,
                           "I": 1 if re.search(ISV_AUTH, blob) else 0,
                           "X": 1 if re.search(INTL, blob) else 0},
        "bias_flag": flag,
        "reason_for_flag": dom_hit or shelf_hit or "logbook-era decision, witnesses generic",
        "required_fix": "merge into glossary schema during backfill",
        "safe_to_show_external": "no_fix_first" if flag == "F10-3" else "review",
    })

# concept links from frozen union spine
spine = json.loads((OUT / "frozen" / "UNION_TERM_SPINE_v1_preSlavic.json").read_text(encoding="utf-8"))
for row in rows:
    gloss = " ".join(filter(None, [row.get("source_term") or ""])).lower()
    for k in spine["concepts"]:
        if k and k in gloss:
            row["concept_link"] = k
            break

flag_dist = Counter(a["bias_flag"] for a in audit_rows)
safe_dist = Counter(a["safe_to_show_external"] for a in audit_rows)

manifest = {
    "inputs": {SLAVIC.name: sha256(SLAVIC), LOGBOOK.name: sha256(LOGBOOK)},
    "term_rows": len(rows), "audit_rows": len(audit_rows),
    "flag_distribution": dict(flag_dist), "safe_distribution": dict(safe_dist),
    "boundary": "mechanical classification of existing records; no promotion, no new wording; F10 flags are review triage, not verdicts",
}

retro = {"artifact": "interslavic_ledger_retrofit_v1", "generated": "2026-07-04",
         "run_manifest": manifest, "rows": rows}
(OUT / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json").write_text(
    json.dumps(retro, ensure_ascii=False, indent=1), encoding="utf-8")
audit = {"artifact": "f10_east_slavic_skew_audit_v1", "generated": "2026-07-04",
         "run_manifest": manifest, "flag_schema": {
             "F10-0": "clean: adequately witnessed/rationalized",
             "F10-1": "missing witness: rationale lacks non-East support",
             "F10-2": "East-heavy: broad-Slavic claim on East-only evidence",
             "F10-3": "dominance-risk: review before external contact",
             "F10-4": "authority-needed: constructed/specialist term"},
         "rows": audit_rows}
(OUT / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=1), encoding="utf-8")

with (OUT / "INTERSLAVIC_LEDGER_RETROFIT_20260704.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["term_id", "source_term", "isv_latin", "isv_cyrillic", "concept_link",
                "reason_class", "status", "bias_flag", "safe_external", "records", "sources"])
    audit_by_id = {a["term_id"]: a for a in audit_rows}
    for r in rows:
        a = audit_by_id.get(r["term_id"], {})
        w.writerow([r["term_id"], r["source_term"], r["chosen_form_latin"], r["chosen_form_cyrillic"],
                    r["concept_link"], "|".join(r["reason_class"]), r["status"],
                    a.get("bias_flag"), a.get("safe_to_show_external"),
                    r["record_count"], "; ".join(map(str, r["source_pointer"][:4]))])

print(json.dumps(manifest, indent=1))
