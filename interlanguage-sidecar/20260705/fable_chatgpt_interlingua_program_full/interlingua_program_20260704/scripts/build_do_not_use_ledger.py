# DO_NOT_USE ledger: typed adverse-evidence relations harvested from EXISTING records.
# Classification only — no new target-language wording, no promotions, no score arithmetic.
# Adverse evidence is not zero evidence: entries carry typed relations + source pointers.
import json
import hashlib
from pathlib import Path
from collections import Counter

OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
LOGS = Path(r"C:\Users\Floris\Downloads\codex backup dump 7-4\codex backup\logs")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

entries = []
def add(candidate, scope, relation, blocked, reason, pointer, action, positive=None):
    entries.append({
        "entry_id": f"DNU-{len(entries)+1:04d}",
        "candidate": candidate,
        "scope": scope,
        "relation_type": relation,
        "positive_concept": positive,
        "blocked_target": blocked,
        "reason": reason,
        "source_pointer": pointer,
        "action": action,
    })

# --- 1. Template cases (linker-level collisions, confirmed 2026-07-04) --------
add("Ränderung", "de->concept linking", "false_friend_or_collision", "ring",
    "bordering operation (Clebsch transfer principle); substring collision with 'ring'; "
    "confirmed false link in pre-fix gloss matching",
    "data/concept_ledger_seed.json (bordering-operation row); CONCORDANCE.md triangulation log",
    "do_not_merge", positive="bordering-operation")
add("irreduzibel / irreducible*", "en gloss linking", "semantic_opposite", "reducible",
    "polarity reversal: 'irreducible' contains 'reducible'; substring match links to the semantic opposite",
    "CONCORDANCE.md triangulation log; linker fix in build_slavic_dataset.py",
    "polarity_guard_in_all_linkers", positive="irreducible")

# --- 2. F10-3 dominance-risk rows (kolco family) -------------------------------
audit = json.loads((OUT / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json").read_text(encoding="utf-8"))
f103 = [a for a in audit["rows"] if a["bias_flag"] == "F10-3"]
for a in f103:
    add(a.get("chosen_form_latin"), "interslavic lane", "dominance_risk",
        "unreviewed use as broadly-Slavic bridge form",
        "kolco family: East-Slavic continuity choice vs cs/sk okruh, S-Slavic prsten, sl kolobar; "
        "triangulation log: 'not derivable mechanically from a majority vote'",
        f"F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json#{a['term_id']}",
        "review_before_external_contact")

# --- 3. Triangulation-log competitor evidence ----------------------------------
add("razpadno polje", "interslavic lane", "competitor_support", None,
    "cs/pl topic sources prefer the rozklad- family (rozkladove teleso, cialo rozkladu); "
    "razpadno kept for continuity; rozkladno polje flagged as authority-preference alternative",
    "SLAVIC_TRIANGULATION_REFERENCE_LOG.md 2026-06-24T02:31Z",
    "present_both_to_reviewer", positive="splitting field")
add("svijanje (for Faltung)", "interslavic lane", "register_mismatch", None,
    "logbook: in invariant theory Faltung may behave closer to 'contraction'; "
    "native folding term may mislead specialists",
    "INTERSLAVIC_LOGBOOK.md Paper01 Key Terms (Faltung row)",
    "reviewer_check_semantics", positive="folding")

# --- 4. Romance warning-comparator rows ----------------------------------------
spine1 = json.loads((OUT / "frozen" / "UNION_TERM_SPINE_v1_preSlavic.json").read_text(encoding="utf-8"))
warn = 0
for k, u in spine1["concepts"].items():
    pr = u["lanes"].get("pan_romance")
    if pr and pr.get("status") == "esperanto_warning_source_hit":
        warn += 1
        add(f"promoted-register surface for '{k}'", "pan-romance comparator layer",
            "authority_needed", "use of comparator surface as bridge evidence",
            "only warning-comparator (Esperanto-family) hits exist in the promoted-register shelf; "
            "no Romance-constructed-comparator support; native Romance evidence must decide",
            f"frozen/UNION_TERM_SPINE_v1_preSlavic.json#{k}",
            "native_evidence_required")

# --- 5. Persianate rejection lanes (non-inheritance vetoes) ---------------------
afp = json.loads((LOGS / "R3_ARABIC_FARSI_PERSIANATE_60_TERM_LEDGER_20260629T073239Z.json")
                 .read_text(encoding="utf-8-sig"))
rej = 0
for r in afp["rows"]:
    lanes = r.get("rejection_lanes") or []
    if lanes and r.get("persianate_bridge_candidate"):
        rej += 1
        add(r["persianate_bridge_candidate"], "persianate bridge",
            "do_not_inherit_into_lane", ", ".join(lanes),
            f"bridge candidate for '{r.get('english') or r['term_id']}' must not inherit into named lanes "
            "without their own review (non-erasure boundary)",
            f"R3_ARABIC_FARSI_PERSIANATE_60_TERM_LEDGER#{r['term_id']}",
            "paired_review_lane_required", positive=r.get("english"))

dist = Counter(e["relation_type"] for e in entries)
out = {
    "artifact": "do_not_use_ledger_v1",
    "generated": "2026-07-04",
    "boundary": "classification of existing records only; adverse evidence is typed, never folded into "
                "the positive concentration statistic; veto relations are not scores",
    "run_manifest": {
        "inputs": {
            "F10 audit": sha(OUT / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json"),
            "spine v1 frozen": sha(OUT / "frozen" / "UNION_TERM_SPINE_v1_preSlavic.json"),
            "AR/FA/Persianate ledger": sha(LOGS / "R3_ARABIC_FARSI_PERSIANATE_60_TERM_LEDGER_20260629T073239Z.json"),
        },
        "entry_count": len(entries),
        "relation_distribution": dict(dist),
    },
    "entries": entries,
}
(OUT / "DO_NOT_USE_LEDGER_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Do-Not-Use Ledger — v1 (typed adverse evidence)", "",
      "2026-07-04. Adverse evidence is not zero evidence: absence of support, competing support, and harmful collision are three different states. Entries are typed relations on existing records; no wording was changed; vetoes are not scores.",
      "",
      f"- Entries: **{len(entries)}** — " + ", ".join(f"{k} {v}" for k, v in dist.most_common()),
      "",
      "| ID | Candidate | Relation | Blocked / scope | Action |", "| --- | --- | --- | --- | --- |"]
for e in entries[:60]:
    md.append(f"| {e['entry_id']} | {str(e['candidate'])[:38]} | {e['relation_type']} | {str(e['blocked_target'])[:40]} | {e['action']} |")
if len(entries) > 60:
    md.append(f"| … | +{len(entries)-60} more in json | | | |")
(OUT / "DO_NOT_USE_LEDGER_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"entries {len(entries)} | relations {dict(dist)} | romance-warning {warn} | persianate-rejection {rej}")
