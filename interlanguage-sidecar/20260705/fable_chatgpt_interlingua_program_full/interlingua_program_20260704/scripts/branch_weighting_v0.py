# Branch-weighting v0: quantify witness concentration over the Slavic family tree.
# Validates the weighted-tree idea empirically on current (pre-backfill) data.
# CPU-only, read-only inputs.
import json
import math
from pathlib import Path
from collections import Counter, defaultdict

OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
audit = json.loads((OUT / "F10_EAST_SLAVIC_SKEW_AUDIT_20260704.json").read_text(encoding="utf-8"))
ledger = json.loads((OUT / "INTERSLAVIC_LEDGER_RETROFIT_20260704.json").read_text(encoding="utf-8"))

# Slavic family tree (top-level clades = the witness-vector axes).
# Depth-1 clades used because that is the resolution the current data supports.
# I/X are not family branches (Interslavic-authority, international) -> kept separate.
CLADES = ["E", "W_S", "S"]  # East, West, South Slavic
# equal-splits / fair-proportion weight target: 3 balanced family branches
TARGET = {c: 1/3 for c in CLADES}

def entropy(dist):
    ps = [p for p in dist.values() if p > 0]
    return -sum(p * math.log(p) for p in ps)

def eff_branches(mass):
    tot = sum(mass.get(c, 0) for c in CLADES)
    if tot == 0:
        return 0.0, {c: 0.0 for c in CLADES}
    dist = {c: mass.get(c, 0)/tot for c in CLADES}
    return math.exp(entropy(dist)), dist

def kl_to_target(dist):
    # KL(observed || uniform-over-branches); undefined if a target branch has 0 obs -> report inf-capped
    s = 0.0
    for c in CLADES:
        p = dist.get(c, 0)
        if p > 0:
            s += p * math.log(p / TARGET[c])
    return s

# aggregate branch mass across all terms (family branches only)
total_mass = Counter()
per_reason = defaultdict(Counter)
ledger_by_id = {r["term_id"]: r for r in ledger["rows"]}
for a in audit["rows"]:
    wv = a["witness_vector"]
    for c in CLADES:
        total_mass[c] += wv.get(c, 0)
    rc = ledger_by_id.get(a["term_id"], {}).get("reason_class", ["unstated"])
    for r in rc:
        for c in CLADES:
            per_reason[r][c] += wv.get(c, 0)

eff_all, dist_all = eff_branches(total_mass)
report = {
    "artifact": "branch_weighting_v0",
    "generated": "2026-07-04",
    "model_note": "Rooted Slavic tree at depth 1 (E/W_S/S). I and X axes excluded (not family branches). Family-branch witness mass only; current data has leaf-level attestation only for East (uk/ru), so this measures the pre-backfill floor.",
    "family_branch_mass_total": dict(total_mass),
    "normalized_distribution": {c: round(dist_all[c], 4) for c in CLADES},
    "effective_number_of_branches": round(eff_all, 3),
    "max_possible": len(CLADES),
    "kl_divergence_from_balanced": round(kl_to_target(dist_all), 3),
    "interpretation": "effective branches near 1.0 = monoculture; near 3.0 = balanced family coverage",
    "per_reason_class": {},
}
for rc, mass in sorted(per_reason.items(), key=lambda kv: -sum(kv[1].values())):
    eff, dist = eff_branches(mass)
    report["per_reason_class"][rc] = {
        "mass": dict(mass),
        "effective_branches": round(eff, 3),
        "kl_from_balanced": round(kl_to_target(dist), 3) if sum(mass.values()) else None,
    }

(OUT / "branch_weighting_v0_20260704.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({k: report[k] for k in
      ["family_branch_mass_total", "normalized_distribution",
       "effective_number_of_branches", "kl_divergence_from_balanced"]}, indent=1))
print("per-reason effective-branch counts:")
for rc, v in report["per_reason_class"].items():
    print(f"  {rc:24s} eff={v['effective_branches']:.2f}  mass={dict(v['mass'])}")
