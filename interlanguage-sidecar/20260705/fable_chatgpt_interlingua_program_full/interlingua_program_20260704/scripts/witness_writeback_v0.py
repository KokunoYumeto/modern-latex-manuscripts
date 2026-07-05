# Witness write-back v0: attach W/S branch witnesses from the backfill (support hits only)
# to term rows via the concept ledger, then re-measure branch balance = state (c) partial.
# Typed provenance: witness_level = concept_shelf (concept-level attestation from the
# 20-source shelf; per-row form verification still pending). Competitor hits are NOT
# witnesses — they live in the adverse channel. No wording changes.
import json
import math
import re
import sys
import unicodedata
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")

backfill = json.loads((OUT / "WS_WITNESS_BACKFILL_v1_20260704.json").read_text(encoding="utf-8"))
retro = json.loads((OUT / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json").read_text(encoding="utf-8"))
audit = json.loads((OUT / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json").read_text(encoding="utf-8"))
seed = json.loads((OUT / "data" / "concept_ledger_seed.json").read_text(encoding="utf-8"))

# --- backfill concept -> branch support map -----------------------------------
def branch_support(cname):
    bs = backfill["concepts"][cname]["branch_summary"]
    return {"west": "support" in bs.get("west", []), "south": "support" in bs.get("south", [])}

# map backfill concept names -> ledger concept ids (en label match, loose)
ALIAS = {"division ring / body": "division ring", "algebra (structure)": "algebra",
         "extension (field)": "extension of the ground field", "noetherian": "noetherian"}
support_by_en = {}
for cname in backfill["concepts"]:
    en = ALIAS.get(cname, cname).lower()
    support_by_en[en] = branch_support(cname)

# --- German-term -> en concept via seed (same lookup as apply_concept_ledger) --
def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower().strip())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", s.replace("ß", "ss"))

de_to_en = {}
for c in seed["concepts"]:
    for v in c["de"]:
        de_to_en[norm(v)] = c["en"].lower()

def en_of(source_term):
    n = norm(source_term or "")
    if n in de_to_en:
        return de_to_en[n]
    for part in re.split(r"\s*/\s*|,\s*", n):
        if part in de_to_en:
            return de_to_en[part]
    best = None
    for v, en in de_to_en.items():
        if len(v) >= 4 and re.search(r"(?<![a-z0-9])" + re.escape(v) + r"(?![a-z0-9])", n):
            if best is None or len(v) > len(best[0]):
                best = (v, en)
    return best[1] if best else None

# --- write-back over audit rows -------------------------------------------------
retro_by_id = {r["term_id"]: r for r in retro["rows"]}
upgraded, touched_concepts = 0, Counter()
for a in audit["rows"]:
    r = retro_by_id.get(a["term_id"])
    if not r:
        continue
    en = en_of(r.get("source_term"))
    sup = support_by_en.get(en) if en else None
    if not sup or not (sup["west"] or sup["south"]):
        continue
    wv = a["witness_vector"]
    before = (wv.get("W_S", 0), wv.get("S", 0))
    if sup["west"]:
        wv["W_S"] = max(wv.get("W_S", 0), 1)
    if sup["south"]:
        wv["S"] = max(wv.get("S", 0), 1)
    if (wv["W_S"], wv["S"]) != before:
        upgraded += 1
        touched_concepts[en] += 1
        a["witness_writeback"] = {"level": "concept_shelf", "concept": en,
                                  "west": sup["west"], "south": sup["south"],
                                  "source": "WS_WITNESS_BACKFILL_v1 (20-source shelf)"}

# --- re-measure branch balance (same statistic as branch_weighting_v0) ----------
CLADES = ["E", "W_S", "S"]
mass = Counter()
for a in audit["rows"]:
    for c in CLADES:
        mass[c] += a["witness_vector"].get(c, 0)
tot = sum(mass.values())
dist = {c: mass[c] / tot for c in CLADES}
H = -sum(p * math.log(p) for p in dist.values() if p > 0)
D1 = math.exp(H)
KL = sum(p * math.log(p / (1/3)) for p in dist.values() if p > 0)

out = {
    "artifact": "witness_writeback_v0_state_c_partial",
    "generated": "2026-07-04",
    "boundary": "concept_shelf-level witnesses only (support hits from 20-source shelf routed via concept ledger); "
                "per-row form verification pending; competitor hits remain adverse-channel; baseline artifacts frozen unchanged",
    "rows_upgraded": upgraded,
    "concepts_touched": dict(touched_concepts),
    "branch_mass_after": dict(mass),
    "distribution_after": {c: round(dist[c], 4) for c in CLADES},
    "effective_branches_after": round(D1, 3),
    "kl_from_balanced_after": round(KL, 3),
    "baseline": {"effective_branches": 1.255, "distribution": {"E": 0.9516, "W_S": 0.0252, "S": 0.0232},
                 "source": "frozen/branch_weighting_v0_run1.json + rerun after re-keying"},
}
(OUT / "WITNESS_WRITEBACK_v0_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
# audit with write-back annotations saved as NEW artifact (baseline file untouched)
(OUT / "F10_AUDIT_postwriteback_20260704.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"rows upgraded: {upgraded} across {len(touched_concepts)} concepts")
print(f"branch mass after: {dict(mass)}")
print(f"effective branches: 1.255 -> {D1:.3f} (of 3); KL: 0.871 -> {KL:.3f}")
