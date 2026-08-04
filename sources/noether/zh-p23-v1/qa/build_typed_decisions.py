#!/usr/bin/env python3
"""Build Paper 23 typed decisions from the already validated connection record."""
from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEC = ROOT / "decisions"
BASE = json.loads((DEC / "NOE-P23-CONNECTION.zh-Hans-CN.json").read_text(encoding="utf-8"))

CONFIGS = [
    ("FINITE-GENERATION", "NOE-FINITE-GENERATION", "NOE-P23-U01/U02/U03/U04/U05", "finite algebra generation", "A ring or algebra has a finite algebra generating set.", ["finite cardinality", "finite dimension", "finite field-extension degree"], "有限生成", "internally_accepted", "internally_reviewed_for_use", "The explicit generation term prevents source endlich from being misread as finite cardinality.", "endlich", "finite algebra generating set", "pass"),
    ("INTEGRITY-BASIS", "NOE-INTEGRITY-BASIS", "NOE-P23-U01/U02/U03/U05", "Noether's finite algebra-generating system", "A finite set generating the invariant ring as an algebra.", ["number-field integral basis", "free module basis"], "整性基（即有限代数生成组）", "candidate", "candidate_after_context_check", "The controlled gloss preserves the historical source term while excluding the independently attested number-field 整基 sense.", "Integritätsbasis", "finite algebra-generating system for the invariant ring", "pending"),
    ("IDEAL-GENERATING-BASIS", "NOE-IDEAL-GENERATING-BASIS", "NOE-P23-U02/U03/U05", "finite ideal-generating set", "A finite set generating an ideal under ring addition and multiplication.", ["free basis", "vector-space basis", "orthogonal basis"], "理想生成基", "candidate", "candidate_after_context_check", "The explanatory compound distinguishes ideal generation from a vector-space or free-module basis.", "Idealbasis", "finite ideal-generating set", "pending"),
    ("CONTRAGREDIENT", "NOE-CONTRAGREDIENT", "NOE-P23-U02", "contragredient matrix action", "The inverse-transpose action on dual coordinates paired with a linear transformation.", ["ordinary inverse transformation", "conjugate transpose alone", "vague opposite change"], "逆转置（反变）变换", "held", "held", "The explanatory form preserves the matrix relation, but exact independent Chinese historical attestation is absent.", "kontragredient", "inverse-transpose action", "pending"),
    ("KOGREDIENT", "NOE-KOGREDIENT", "NOE-P23-U06", "same-way transformation relation", "The psi expressions transform in the same way as d x under the induced group.", ["covariant derivative operator", "statistical covariance", "colloquial simultaneous change"], "同变", "held", "held", "The source relation is clear, but modern 协变 evidence is only near-register evidence and does not attest historical Kogredienz.", "kogredient", "psi transforms as d x", "pending"),
    ("NORMAL-COORDINATES", "NOE-NORMAL-COORDINATES", "NOE-P23-U06", "Riemann normal coordinates", "Coordinates straightening extremals issuing from a point.", ["normal family", "statistical normalization", "generic coordinate regularization"], "Riemann 正规坐标", "candidate", "candidate_after_context_check", "The historical candidate is retained with an explicit modern PRC competitor 法坐标 and no regional promotion.", "Riemannsche Normalkoordinaten", "coordinates straightening extremals", "pending"),
]

def write_json(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

for slug, concept_id, unit, gloss, sense, excluded, form, candidate_status, decision_status, rationale, observed, window, source_gate in CONFIGS:
    d = deepcopy(BASE)
    d["record_id"] = f"NOE-P23-{slug}.zh-Hans-CN"
    d["work"]["source_unit_id"] = unit
    d["concept"] = {
        "concept_id": concept_id,
        "preferred_gloss": gloss,
        "intended_sense": sense,
        "excluded_senses": excluded,
        "stratum": "work_specific_historical",
        "trap_flags": ["other"] if slug != "FINITE-GENERATION" else []
    }
    cid = f"C-{slug}"
    d["candidates"] = [{
        "candidate_id": cid, "form": form,
        "script_forms": {"Hans": form}, "variants": [],
        "status": candidate_status, "definition_or_gloss": gloss
    }]
    src = deepcopy(BASE["evidence"]["support"][0])
    src["evidence_id"] = f"EV-P31-{slug}"
    src["candidate_id"] = cid
    src["language"] = "de"
    src["observed_form"] = observed
    src["context_window"] = window
    src["concept_match"] = "exact"
    src["source"]["source_id"] = "SRC-P31-P23"
    src["source"]["path_or_uri"] = "source/Noether_Paper23_German_P31_Sealed_exact_slice.tex"
    src["source"]["sha256_or_version"] = "7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5"
    src["weight_semantics"]["notes"] = "Canonical German source fixes the mathematical sense, not independent Chinese usage."
    d["evidence"] = {
        "support": [src], "candidate": [], "competitor": [], "adverse": [], "veto": [],
        "absence": [
            {"language_or_branch": "zh-Hans-SG", "search_scope": "Paper 23 checked evidence shelf", "search_date": "2026-07-18", "status": "searched_no_evidence", "notes": "No Singapore-specific source or reviewer return."},
            {"language_or_branch": "zh-Hant-TW/HK/MO", "search_scope": "Paper 23 checked evidence shelf", "search_date": "2026-07-18", "status": "searched_no_evidence", "notes": "Controlled script conversion is not regional evidence."}
        ]
    }
    for key in d["risk_controls"]:
        d["risk_controls"][key] = {"status": "risk", "notes": "Controlled by the exact source sense; independent Chinese and regional evidence remain limited."}
    d["risk_controls"]["dominance"] = {"status": "risk", "notes": "The shelf is PRC-Simplified dominated; no numeric readiness penalty is computed."}
    d["risk_controls"]["script"] = {"status": "clear", "notes": "This lexical record decides zh-Hans-CN only."}
    d["readiness_gates"]["source_floor"] = {"status": source_gate, "evidence_or_reason": "Sealed P31 fixes the source sense; independent exact Chinese attestation is absent where this gate remains pending."}
    d["readiness_gates"]["context_review"] = {"status": "pass", "evidence_or_reason": "Exact source window and excluded senses were reviewed."}
    d["readiness_gates"]["adverse_review"] = {"status": "pass", "evidence_or_reason": "Known ambiguity and absence debt are explicit in the terminology/crosswalk ledgers."}
    d["readiness_gates"]["branch_or_cohort_review"] = {"status": "pending", "evidence_or_reason": "Singapore and regional Hant cohorts remain absent."}
    d["readiness_gates"]["script_policy"] = {"status": "pass", "evidence_or_reason": "Scoped to zh-Hans-CN; Hant is governed by a separate script bridge."}
    d["readiness_gates"]["internal_qa"] = {"status": "pass", "evidence_or_reason": "Source loci, builds, ordered math spans, and all final Hans/Hant pages were checked internally."}
    d["decision"] = {
        "status": decision_status, "selected_candidate_id": cid, "rationale": rationale,
        "reviewer_question": "Can an independent Chinese historical or regional mathematical source confirm or replace this controlled form?",
        "auto_promotion_prohibited": True,
        "decision_authority": "Chinese Noether production lane internal source-and-context audit",
        "decision_date": "2026-07-18"
    }
    d["invariants"] = [{
        "invariant_id": f"INV-{slug}-SENSE", "must_preserve": sense,
        "may_change": "surface term after independent local-standard review",
        "test": f"check {unit} against the exact sealed P31 slice and SOURCE_UNIT_MAP.csv", "status": "pass"
    }]
    d["provenance"]["created_at"] = "2026-07-18T17:55:00+02:00"
    d["provenance"]["input_artifacts"] = [
        {"path_or_uri": "source/Noether_Paper23_German_P31_Sealed_exact_slice.tex", "version_or_hash": "7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5", "role": "canonical source unit"},
        {"path_or_uri": "evidence/NOE-P23_CJKV_CROSSWALK.csv", "version_or_hash": "E42B4E41D1BF1A95285E03C8ECE4CDCD4121B2B023EF4DFF9E5AA80D0F9AA2C9", "role": "sense, basin, dominance, and cohort control"}
    ]
    d["provenance"]["notes"] = "Independent native support varies by concept. Basin and qualitative dominance debt remain in the separate CJKV crosswalk; no external or regional validation is claimed."
    write_json(DEC / f"NOE-P23-{slug}.zh-Hans-CN.json", d)

# Update the already validated connection record's internal QA gate after final Hans/Hant checks.
connection = deepcopy(BASE)
connection["readiness_gates"]["internal_qa"] = {"status": "pass", "evidence_or_reason": "Final Hans/Hant two-pass builds, ordered 124-span math comparison, and all-page rendered inspection pass internally."}
connection["provenance"]["notes"] += " Internal Hant/build/render QA was completed under ZH-D023."
write_json(DEC / "NOE-P23-CONNECTION.zh-Hans-CN.json", connection)

# Adapt the validated Paper 29 script-bridge record to Paper 23 and its measured invariants.
p29 = ROOT.parent / "noether_paper29_zh_rebase_001_20260718" / "decisions" / "NOE-P29-ZH-HANT-SCRIPT.json"
h = json.loads(p29.read_text(encoding="utf-8"))
h["record_id"] = "NOE-P23-ZH-HANT-SCRIPT"
h["work"] = deepcopy(BASE["work"])
h["work"]["source_unit_id"] = "NOE-P23-U00--U07"
h["concept"]["concept_id"] = "NOE-P23-CONTROLLED-HANT-SCRIPT"
h["candidates"][0]["form"] = "OpenCC s2t plus controlled 為/群/裡/個/眾/才 normalization"
h["candidates"][0]["script_forms"] = {"Hant": "為 / 群 / 裡 / 個 / 眾 / 才"}
h["evidence"]["support"][0]["source"]["source_id"] = "SRC-P31-P23"
h["evidence"]["support"][0]["source"]["path_or_uri"] = "source/Noether_Paper23_German_P31_Sealed_exact_slice.tex"
h["evidence"]["support"][0]["source"]["sha256_or_version"] = "7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5"
h["evidence"]["candidate"][0]["source"]["path_or_uri"] = "zh-Hans-CN/Noether_Paper23_Chinese_P31Reconciled_zh-Hans-CN_v001.tex"
h["evidence"]["candidate"][0]["source"]["sha256_or_version"] = "7D3F73762F556712AA8036794125EE2118C6FD4BBFB1D0DC45CC076F4057E4B1"
h["risk_controls"]["script"]["notes"] = "OpenCC s2t plus explicit 為/群/裡/個/眾/才 normalization; output was separately compiled and rendered."
h["readiness_gates"]["context_review"]["evidence_or_reason"] = "All eight source units and script/math invariants are checked internally."
h["readiness_gates"]["internal_qa"]["evidence_or_reason"] = "Hans/Hant contain 124 ordered math spans with identical canonical sequences; each has 3 primed sums, 2 g(y,d y) loci, and 5 numbered displays; both compile twice to four pages and every page was inspected."
h["provenance"]["created_at"] = "2026-07-18T17:55:00+02:00"
h["provenance"]["input_artifacts"] = [
    {"path_or_uri": "source/Noether_Paper23_German_P31_Sealed_exact_slice.tex", "version_or_hash": "7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5", "role": "canonical source unit"},
    {"path_or_uri": "zh-Hans-CN/Noether_Paper23_Chinese_P31Reconciled_zh-Hans-CN_v001.tex", "version_or_hash": "7D3F73762F556712AA8036794125EE2118C6FD4BBFB1D0DC45CC076F4057E4B1", "role": "audited script base"},
    {"path_or_uri": "opencc-python-reimplemented", "version_or_hash": "lane declaration 0.1.7:s2t; runtime metadata unavailable", "role": "mechanical script conversion"}
]
h["provenance"]["applied_diff_path_or_uri"] = "zh-Hant-controlled/Noether_Paper23_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex"
h["provenance"]["notes"] = "Controlled non-localized Hant only. Basin and qualitative dominance debt remain in the crosswalk; no regional or external certification is claimed."
write_json(DEC / "NOE-P23-ZH-HANT-SCRIPT.json", h)

print(json.dumps({"written": sorted(p.name for p in DEC.glob("*.json")), "count": len(list(DEC.glob("*.json")))}, ensure_ascii=False, indent=2))
