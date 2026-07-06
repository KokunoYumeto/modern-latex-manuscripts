# Comparative term analysis v1: for each backfilled concept, compare the current
# Interslavic choice against branch-attested alternatives. Evidence display only —
# no promotions; "review_priority" flags where an alternative out-covers the current
# form. Weighted scoring is delegated to the math lane (see CHATGPT_PRO_TASK_SPEC).
import json
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
OUT = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
bf = json.loads((OUT / "WS_WITNESS_BACKFILL_v1_20260704.json").read_text(encoding="utf-8"))

rows = []
for cname, spec in bf["concepts"].items():
    isv = spec["isv_choice"]
    unpinned = isinstance(isv, str) and isv.endswith("?")
    # aggregate evidence per candidate lexeme family
    cand = defaultdict(lambda: {"branches": set(), "langs": set(), "hits": 0, "files": set(), "kind": None})
    for h in spec["hits"]:
        key = h["note"] if h["kind"] == "competitor" else f"ISV-family ({isv})"
        c = cand[key]
        c["branches"].add(h["branch"])
        c["langs"].add(h["lang"])
        c["hits"] += h["count"]
        c["files"].add(h["file"])
        c["kind"] = h["kind"]
    # current form is East-attested by corpus construction (uk/ru pipeline)
    cur_key = f"ISV-family ({isv})"
    if cur_key in cand:
        cand[cur_key]["branches"].add("east")
    cur_branches = cand.get(cur_key, {"branches": {"east"}})["branches"]
    best_alt = None
    for k, c in cand.items():
        if k == cur_key:
            continue
        alt_b = set(c["branches"]) | set()  # competitors are W/S-attested only in shelf
        if best_alt is None or len(alt_b) > len(best_alt[1]["branches"]):
            best_alt = (k, c)
    review_priority = bool(best_alt and len(best_alt[1]["branches"]) >= len(cur_branches - {"east"}) + 1)
    rows.append({
        "concept": cname,
        "current_isv": isv,
        "isv_pinned": not unpinned,
        "current_branch_coverage": sorted(cur_branches),
        "candidates": {k: {"kind": c["kind"], "branches": sorted(c["branches"]),
                           "langs": sorted(c["langs"]), "hits": c["hits"],
                           "files": sorted(c["files"])[:4]} for k, c in cand.items()},
        "review_priority": review_priority,
        "review_question": (
            f"Current '{isv}' vs branch-attested alternatives: which serves family-central "
            f"passive recognizability best, and is a doublet required for West readers?"
            if review_priority else
            f"Confirm '{isv}' (support pattern acceptable) or note preferred variant policy."),
    })

prio = [r for r in rows if r["review_priority"]]
out = {
    "artifact": "comparative_term_analysis_v1",
    "generated": "2026-07-04",
    "boundary": "evidence comparison only; no promotion; weighted scoring delegated to math lane; "
                "review questions for Interslavic authority, not decisions",
    "concept_count": len(rows),
    "review_priority_count": len(prio),
    "rows": rows,
}
(OUT / "COMPARATIVE_TERM_ANALYSIS_v1_20260704.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Comparative Term Analysis — v1 (current ISV choice vs branch-attested alternatives)",
      "",
      "2026-07-04. Per concept: the lane's current form, its branch coverage, and every alternative attested in the 20-source W/S shelf, with hit counts and files. `review_priority` = an alternative's branch coverage rivals or beats the current form's non-East coverage. Questions, not verdicts — the packet format for the 'which is better and why' review.",
      "",
      f"Concepts: {len(rows)} · review-priority: {len(prio)}",
      "",
      "| Concept | Current (ISV) | Covers | Strongest alternative | Covers | Priority |",
      "| --- | --- | --- | --- | --- | --- |"]
for r in sorted(rows, key=lambda x: (not x["review_priority"], x["concept"])):
    alts = [(k, v) for k, v in r["candidates"].items() if v["kind"] == "competitor"]
    alts.sort(key=lambda kv: -len(kv[1]["branches"]))
    alt_s = f"{alts[0][0][:34]} ({'+'.join(alts[0][1]['branches'])})" if alts else "—"
    md.append("| {} | {} | {} | {} | {} | {} |".format(
        r["concept"], r["current_isv"], "+".join(r["current_branch_coverage"]),
        alt_s.split(" (")[0], alt_s.split("(")[-1].rstrip(")") if alts else "",
        "**REVIEW**" if r["review_priority"] else "confirm"))
(OUT / "COMPARATIVE_TERM_ANALYSIS_v1_20260704.md").write_text("\n".join(md), encoding="utf-8")

print(f"concepts {len(rows)} | review-priority {len(prio)}")
for r in prio:
    print("  REVIEW:", r["concept"], "| current:", r["current_isv"])
