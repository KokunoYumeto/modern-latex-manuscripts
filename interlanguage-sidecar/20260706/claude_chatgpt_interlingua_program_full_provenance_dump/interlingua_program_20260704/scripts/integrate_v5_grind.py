# Integrate ChatGPT v5/expanded-grind drops after Fable audit:
# 1) PAN_ROMANCE_C2_FILL_LEDGER_v3 — 39 rows with audited statuses (sense-traps flagged).
# 2) Slavic branch patch -> candidate-layer branch weighting (state D), frozen baselines untouched.
# 3) Normalization action-table v2 vs Fable decision-table v1.1 cross-check.
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"
W = DROP / "v5_1_workpass"
G = DROP / "expanded_grind_v1"

# ---------- 1. Pan-Romance C2 fill ledger v3 ----------
pr = json.loads((W / "PAN_ROMANCE_C2_CURATED_SOURCEBODY_PROBE_v2_1_20260705.json").read_text(encoding="utf-8-sig"))
SENSE_FLAG = {
    "modulus": "ES módulo / FR module conflate module-structure with mod-arithmetic (FR 'modulo' 625 = arithmetic); sense split needed before witness use",
    "ground form": "ES 'forma fundamental' 103 hits are almost certainly differential-geometry 'fundamental form', NOT invariant-theory Grundform — REJECT as ground-form evidence pending KWIC sense check",
    "complete system": "ES 'sistema completo' may be 'sistema completo de residuos' (complete residue system) — sense check needed",
}
LOW_CONF = {"binary form": "2 hits/2 files", "invariant theory": "2 ES + 1 FR hits"}
NOETHER_GAP = {"absolutely complete system", "biquadratic form", "form system",
               "relatively complete system", "ternary form", "transvection"}

ledger = []
counts = {"witness_candidate": 0, "sense_review": 0, "low_confidence": 0, "gap_specialist": 0}
for r in pr["rows"]:
    has = bool(r.get("es")) or bool(r.get("fr"))
    c = r["concept"]
    if c in NOETHER_GAP:
        status, note = "gap_specialist_noether_intake", "do not fill from general shelves (ChatGPT concurs)"
        counts["gap_specialist"] += 1
    elif c in SENSE_FLAG:
        status, note = "witness_candidate_SENSE_REVIEW", SENSE_FLAG[c]
        counts["sense_review"] += 1
    elif c in LOW_CONF:
        status, note = "witness_candidate_low_confidence", LOW_CONF[c]
        counts["low_confidence"] += 1
    elif has:
        status, note = "witness_candidate_sourcebody_context_review", ""
        counts["witness_candidate"] += 1
    else:
        status, note = "gap", "no hits"
    ledger.append({
        "concept_id": r["concept_id"], "concept": c, "stratum": r.get("stratum"),
        "status": status, "note": note,
        "es_forms": [{k: h[k] for k in ("form", "count", "file_count")} for h in (r.get("es") or [])],
        "fr_forms": [{k: h[k] for k in ("form", "count", "file_count")} for h in (r.get("fr") or [])],
        "counting_caveat": "FR/ES diacritic-folded spellings are double-listed with identical counts — never sum spellings; use max per lexeme",
        "evidence": "SOURCEBODY probe v2.1 (ChatGPT) + Fable audit 2026-07-05",
    })
out1 = {"artifact": "pan_romance_c2_fill_ledger_v3", "generated": "2026-07-05",
        "boundary": "witness CANDIDATES pending row-context review; source-body hits witness native usage of the "
                    "language-family, not bridge-form validity; nothing certified",
        "status_counts": counts, "rows": ledger}
(BASE / "PAN_ROMANCE_C2_FILL_LEDGER_v3_20260705.json").write_text(json.dumps(out1, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Pan-Romance C2 fill ledger v3", "",
      "2026-07-05. ChatGPT source-body probe v2.1 + Fable sense audit. Statuses: "
      f"{counts['witness_candidate']} clean witness-candidates, {counts['sense_review']} sense-review "
      f"(modulus/ground-form/complete-system traps), {counts['low_confidence']} low-confidence, "
      f"{counts['gap_specialist']} specialist-Noether gaps (stay open for the Noether source-intake lane).", "",
      "| Concept | Status | Top ES | Top FR | Note |", "| --- | --- | --- | --- | --- |"]
for r in ledger:
    es = r["es_forms"][0]["form"] + f":{r['es_forms'][0]['count']}" if r["es_forms"] else ""
    fr = r["fr_forms"][0]["form"] + f":{r['fr_forms'][0]['count']}" if r["fr_forms"] else ""
    md.append(f"| {r['concept']} | {r['status']} | {es} | {fr} | {r['note'][:90]} |")
(BASE / "PAN_ROMANCE_C2_FILL_LEDGER_v3_20260705.md").write_text("\n".join(md), encoding="utf-8")

# ---------- 2. Slavic patch -> candidate-layer branch weighting (state D) ----------
sp = json.loads((G / "EXPANDED_SOURCE_ANCHOR_SLAVIC_BRANCH_PATCH_v1_20260705.json").read_text(encoding="utf-8-sig"))
import math
add = {"W": 0, "S": 0, "E": 0}
per_concept = []
for r in sp["rows"]:
    m = r["branch_mass_raw"]
    add["W"] += m.get("W", 0)
    add["S"] += m.get("S", 0)
    add["E"] += m.get("E_adjacent", 0)  # be = East branch
    per_concept.append((r["concept"], m))
# post-writeback certified state C: E 2341 / W 223 / S 239 (concept_shelf level)
C = {"E": 2341, "W": 223, "S": 239}
D = {k: C[k] + add[k] for k in C}
def eff(d):
    t = sum(d.values())
    ps = [v / t for v in d.values() if v > 0]
    H = -sum(p * math.log(p) for p in ps)
    return math.exp(H), {k: round(v / t, 4) for k, v in d.items()}
effC, distC = eff(C)
effD, distD = eff(D)
out2 = {"artifact": "branch_weighting_state_d_candidates", "generated": "2026-07-05",
        "boundary": "STATE D = state C (certified concept-shelf writeback) + expanded-anchor PATCH CANDIDATES "
                    "(pre row-review; probe layer; be counted as East). Baselines frozen; this is a projection, "
                    "not a certified measurement.",
        "patch_added_mass": add, "patch_concepts": len(sp["rows"]),
        "state_c": {"mass": C, "effective_branches": round(effC, 3), "distribution": distC},
        "state_d_candidate": {"mass": D, "effective_branches": round(effD, 3), "distribution": distD},
        "homograph_flags": ["cs skupina (23) may include non-math sense", "hr tijelo (19) = body/division-ring sense inside field row"],
        "confirmations": ["be ring evidence = kolco-family (кольц 18/6f) — be sides with East on ring; strengthens kolco be-support",
                          "sl izrek=theorem (674/58f) independently confirms Fable statement-izreka gloss",
                          "cs těleso-as-field (306/48f) consistent with F12 West calque preference"],
        "per_concept": [{"concept": c, "mass": m} for c, m in per_concept]}
(BASE / "BRANCH_WEIGHTING_STATE_D_20260705.json").write_text(json.dumps(out2, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- 3. normalization band cross-check ----------
na = json.loads((W / "NORMALIZATION_ACTION_TABLE_v2_CHATGPT_20260705.json").read_text(encoding="utf-8-sig"))
dt = json.loads((BASE / "NORMALIZATION_DECISION_TABLE_v1_20260704.json").read_text(encoding="utf-8"))
dt_by = {r["entry_id"]: r for r in dt["rows"]}
na_rows = na.get("rows") or na.get("actions") or []
agree, disagree, unmatched = [], [], []
for r in na_rows:
    eid = r.get("entry_id") or r.get("group_id") or ""
    band = r.get("action_band") or r.get("band") or ""
    mine = dt_by.get(eid)
    if not mine:
        unmatched.append(eid)
        continue
    v = mine["draft_verdict"]
    ok = (("R1_review_doublet" in band and "doublet" in v) or
          ("R2_pan_anchor" in band and "pan-root" in v) or
          ("R3" in band) or ("R0" in band) or ("R1_branch_specific" in band and ("W-specific" in v or "S-specific" in v or "insufficient" in v)))
    (agree if ok else disagree).append({"entry_id": eid, "chatgpt_band": band, "fable_verdict": v[:110]})
out3 = {"artifact": "normalization_band_crosscheck", "generated": "2026-07-05",
        "agree": len(agree), "disagree": len(disagree), "unmatched": unmatched,
        "disagreements": disagree}
(BASE / "NORMALIZATION_BAND_CROSSCHECK_20260705.json").write_text(json.dumps(out3, ensure_ascii=False, indent=1), encoding="utf-8")

print("1) Pan-Romance ledger v3:", counts)
print("2) branch weighting: state C eff", round(effC, 3), distC, "-> state D(candidate) eff", round(effD, 3), distD)
print("   patch mass added:", add)
print("3) normalization cross-check: agree", len(agree), "| disagree", len(disagree), "| unmatched", len(unmatched))
for d in disagree[:12]:
    print("   DISAGREE:", d["entry_id"], "|", d["chatgpt_band"], "| fable:", d["fable_verdict"][:80])
