# Row-context review pass (Fable, KWIC-verified):
# 1) Pan-Romance ledger v3 -> v3.1 with per-row verdicts from sample windows.
# 2) Slavic patch row-review -> state-D-certified effective branches on
#    UNIT-CONSISTENT (concept x language)-presence units, pre vs post.
import json
import math
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
DROP = BASE / "user made flr with chat web stuff"

# ---------- 1. Pan-Romance v3.1 ----------
led = json.loads((BASE / "PAN_ROMANCE_C2_FILL_LEDGER_v3_20260705.json").read_text(encoding="utf-8"))
VERDICTS = {
    # upgraded: window shows exact math sense in native ES AND FR independent sources
    **{c: ("witnessed_sourcebody_internal", "") for c in [
        "coefficient", "determinant", "dimension", "direct sum", "element", "function", "image",
        "polynomial", "set", "subset", "vector", "vector space", "reduction", "assumption",
        "corollary", "equation", "example", "exercise", "formula", "notation", "problem",
        "proposition", "relation", "statement"]},
    "kernel": ("witnessed_sourcebody_internal",
               "EXCLUDE ES loan 'kernel:52' — sample is statistics kernel-density (EstadisticaI.tex); núcleo/noyau are the witnesses"),
    "resultant": ("witnessed_sourcebody_internal",
                  "ES 'resultante' mixes generic 'resulting' adjective (punto resultante, EDOs resultantes); real witness = cimat-tna 3-algebra-lineal.tex (Res(f,f') discriminant context)"),
    "modulus": ("witnessed_sourcebody_internal_MODULE_SENSE",
                "sense resolved from windows: ES 'R-módulo o módulo sobre R' + FR module = MODULE structure (Noether Modul); "
                "FR 'modulo:625' = arithmetic mod, EXCLUDED from this row's evidence"),
    "covariant": ("witness_candidate_SENSE_REVIEW",
                  "DEMOTED: ES hits = diff-geometry 'tensores covariantes', FR hits = category-theory 'covariant functor' — right word, WRONG SENSE for invariant-theory covariants; needs invariant-theory-context hits"),
    "contravariant": ("witness_candidate_SENSE_REVIEW",
                      "DEMOTED: same as covariant (tensor/functor senses); invariant-theory sense unwitnessed in these shelves"),
    "binary form": ("rejected_false_sense",
                    "window = Neurocomputación 'hybrid (binary/bipolar) form of Hebb rule' — neural nets, not binary forms; REJECTED"),
    "complete system": ("rejected_false_sense",
                        "window = ODE 'solución particular del sistema completo (no homogéneo)' — complete linear ODE system, not vollständiges System; REJECTED"),
    "ground form": ("rejected_false_sense",
                    "window = Riemannian geometry second fundamental form (II_p, ω_i, h_ij) — confirmed diff-geo trap; REJECTED"),
    "invariant theory": ("witness_candidate_low_confidence",
                         "FR math_0107137v2 window IS real invariant theory (anneau de polynômes / factorise) — FR anchor stands; ES window inconclusive"),
}
counts = {}
for r in led["rows"]:
    v = VERDICTS.get(r["concept"])
    if v:
        r["status"], extra = v
        if extra:
            r["note"] = (r["note"] + " | " if r.get("note") else "") + extra
        r["row_review"] = "fable_kwic_20260705"
    counts[r["status"]] = counts.get(r["status"], 0) + 1
led["artifact"] = "pan_romance_c2_fill_ledger_v3_1_row_reviewed"
led["status_counts"] = counts
led["review_note"] = ("v3.1: every row with hits row-reviewed against sample KWIC windows. 26 witnessed_sourcebody_internal "
                      "(incl. modulus resolved to MODULE sense; kernel/resultant with exclusions), 2 demoted to sense-review "
                      "(covariant/contravariant: tensor/functor senses), 3 rejected_false_sense (binary form=Hebb rule!, "
                      "complete system=ODE, ground form=fundamental form), 1 low-confidence (invariant theory, FR anchor), "
                      "6 specialist gaps + 1 no-hit gap. 'witnessed_sourcebody_internal' = internal evidence tier only; "
                      "NOT community/external certification.")
(BASE / "PAN_ROMANCE_C2_FILL_LEDGER_v3_20260705.json").write_text(json.dumps(led, ensure_ascii=False, indent=1), encoding="utf-8")

md = ["# Pan-Romance C2 fill ledger v3.1 (row-reviewed)", "",
      "2026-07-05. " + led["review_note"], "",
      "| Concept | Status | Note |", "| --- | --- | --- |"]
for r in led["rows"]:
    md.append(f"| {r['concept']} | {r['status']} | {r.get('note','')[:160]} |")
(BASE / "PAN_ROMANCE_C2_FILL_LEDGER_v3_20260705.md").write_text("\n".join(md), encoding="utf-8")

# ---------- 2. Slavic patch: presence-unit state D ----------
sp = json.loads((DROP / "expanded_grind_v1" / "EXPANDED_SOURCE_ANCHOR_SLAVIC_BRANCH_PATCH_v1_20260705.json").read_text(encoding="utf-8-sig"))
bf = json.loads((BASE / "ws_witness_backfill_v1_20260704.json").read_text(encoding="utf-8"))
BRANCH = {"cs": "W", "pl": "W", "sk": "W", "dsb": "W", "hsb": "W",
          "sl": "S", "hr": "S", "sr": "S", "bg": "S", "mk": "S", "bs": "S", "cnr": "S",
          "be": "E"}
# map patch concept -> backfill concept name (pre-patch presence source)
BF_NAME = {"basis": "basis", "determinant": "determinant", "dimension": "dimension",
           "field": "field", "group": "group", "ideal": "ideal", "matrix": "matrix",
           "module": "module", "polynomial": "polynomial", "proof": "proof",
           "quotient field": "quotient field", "ring": "ring", "theorem": "theorem",
           "vector space": "vector", "equation": None}
pre_pairs = {"E": 0, "W": 0, "S": 0}
post_pairs = {"E": 0, "W": 0, "S": 0}
detail = []
for r in sp["rows"]:
    c = r["concept"]
    # pre: E = uk+ru (2, all 15 core concepts are E-witnessed); W/S langs from backfill hits
    pre_langs = set()
    bfc = BF_NAME.get(c, c)
    if bfc and bfc in bf["concepts"]:
        for h in bf["concepts"][bfc]["hits"]:
            pre_langs.add(h["lang"])
    preW = {l for l in pre_langs if BRANCH.get(l) == "W"}
    preS = {l for l in pre_langs if BRANCH.get(l) == "S"}
    pre_pairs["E"] += 2
    pre_pairs["W"] += len(preW)
    pre_pairs["S"] += len(preS)
    # post: union of pre and patch languages (sr latin+cyr = one language)
    post_langs = set(pre_langs) | set(r["languages"].keys())
    postW = {l for l in post_langs if BRANCH.get(l) == "W"}
    postS = {l for l in post_langs if BRANCH.get(l) == "S"}
    postE = 2 + (1 if "be" in post_langs else 0)
    post_pairs["E"] += postE
    post_pairs["W"] += len(postW)
    post_pairs["S"] += len(postS)
    detail.append({"concept": c, "pre": {"E": 2, "W": sorted(preW), "S": sorted(preS)},
                   "post": {"E": postE, "W": sorted(postW), "S": sorted(postS)}})

def eff(d):
    t = sum(d.values())
    ps = [v / t for v in d.values() if v > 0]
    H = -sum(p * math.log(p) for p in ps)
    return round(math.exp(H), 3), {k: round(v / t, 4) for k, v in d.items()}
effPre, distPre = eff(pre_pairs)
effPost, distPost = eff(post_pairs)

out = {"artifact": "branch_weighting_state_d_certified_presence_units", "generated": "2026-07-05",
       "units": "(concept x language) presence pairs over the 15 patched core concepts; E=uk+ru(+be), "
                "W=cs/pl/sk, S=sl/hr/sr/bg/mk/bs; sr Latin+Cyrillic = one language; UNIT-CONSISTENT pre/post",
       "row_review": "Fable 2026-07-05: all 15 concept rows lexeme-checked per language (correct); file-path genre check: "
                     "GitHub-sourced native academic materials (student notes/course texts) — genuine native usage, "
                     "sub-textbook register; flags: cs skupina non-math-sense risk (group), hr tijelo sense-mix (field)",
       "pre_patch": {"pairs": pre_pairs, "effective_branches": effPre, "distribution": distPre},
       "post_patch": {"pairs": post_pairs, "effective_branches": effPost, "distribution": distPost},
       "reading": f"On the 15 core concepts, witness-presence pairs go {sum(pre_pairs.values())} -> {sum(post_pairs.values())}; "
                  f"effective branches {effPre} -> {effPost} of 3 (presence units). This is the honest replacement for the "
                  "withdrawn 2.62 figure; register remains sub-textbook pending shelf-grade sources.",
       "per_concept": detail}
(BASE / "BRANCH_WEIGHTING_STATE_D_20260705.json").write_text(json.dumps({
    **json.loads((BASE / "BRANCH_WEIGHTING_STATE_D_20260705.json").read_text(encoding="utf-8")),
    "state_d_certified_presence_units": out}, ensure_ascii=False, indent=1), encoding="utf-8")

print("1) Pan-Romance v3.1 status counts:", counts)
print(f"2) presence units 15 concepts: pre {pre_pairs} eff {effPre} {distPre}")
print(f"   post {post_pairs} eff {effPost} {distPost}")
